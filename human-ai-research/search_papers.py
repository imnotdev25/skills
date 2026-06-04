#!/usr/bin/env python3
"""
search_papers.py — literature retrieval for the research-pipeline skill.

Queries arXiv, Semantic Scholar, and OpenAlex, normalizes the results into one
schema, de-duplicates across sources, and emits JSON or a Markdown evidence-card
table (the same card shape used in 02_literature/selected_papers.md).

Standard library only — no `pip install` required. Works anywhere Python 3.8+ runs.

NETWORK: needs outbound HTTPS to:
  - export.arxiv.org
  - api.semanticscholar.org
  - api.openalex.org
If your environment blocks these (e.g. a sandbox allowlist), run it where they're
reachable or update the network settings. The skill's `web_search` tool is a
coverage/recency fallback.

Examples:
  python search_papers.py --query "salary bias large language models" --limit 20
  python search_papers.py --query "MXFP4 quantization inference" \\
      --sources arxiv,openalex --from-year 2023 \\
      --format markdown --out run-01.md --email you@example.com
"""

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

USER_AGENT = "research-pipeline-skill/1.0 (literature search; stdlib urllib)"

ARXIV_NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}


# --------------------------------------------------------------------------- #
# HTTP helper                                                                 #
# --------------------------------------------------------------------------- #
def http_get(url, timeout=30, retries=3, accept=None):
    """GET a URL with a polite UA and simple exponential backoff. Returns bytes."""
    headers = {"User-Agent": USER_AGENT}
    if accept:
        headers["Accept"] = accept
    last_err = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            last_err = e
            # 429 / 5xx are worth retrying; 4xx (else) are not.
            if e.code != 429 and e.code < 500:
                break
        except (urllib.error.URLError, TimeoutError) as e:
            last_err = e
        time.sleep(1.5 * (attempt + 1))
    raise last_err if last_err else RuntimeError("request failed")


# --------------------------------------------------------------------------- #
# Normalization helpers                                                       #
# --------------------------------------------------------------------------- #
def norm_doi(doi):
    if not doi:
        return None
    doi = doi.strip()
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi, flags=re.I)
    return doi.lower() or None


def norm_title_key(title):
    return re.sub(r"[^a-z0-9]", "", (title or "").lower())


def record(source, title, authors, year, venue, doi, url, abstract, citations):
    return {
        "source": source,
        "title": (title or "").strip(),
        "authors": authors or [],
        "year": year,
        "venue": (venue or None),
        "doi": norm_doi(doi),
        "url": url,
        "abstract": (abstract or None),
        "citations": citations,
    }


# --------------------------------------------------------------------------- #
# Source: arXiv (Atom XML)                                                    #
# --------------------------------------------------------------------------- #
def search_arxiv(query, limit, from_year, timeout, retries):
    q = urllib.parse.quote(f"all:{query}")
    url = (
        "http://export.arxiv.org/api/query?"
        f"search_query={q}&start=0&max_results={limit}"
        "&sortBy=relevance&sortOrder=descending"
    )
    raw = http_get(url, timeout=timeout, retries=retries)
    root = ET.fromstring(raw)
    out = []
    for entry in root.findall("atom:entry", ARXIV_NS):
        title = (entry.findtext("atom:title", default="", namespaces=ARXIV_NS) or "").strip()
        summary = (entry.findtext("atom:summary", default="", namespaces=ARXIV_NS) or "").strip()
        published = entry.findtext("atom:published", default="", namespaces=ARXIV_NS) or ""
        year = int(published[:4]) if published[:4].isdigit() else None
        if from_year and year and year < from_year:
            continue
        link = (entry.findtext("atom:id", default="", namespaces=ARXIV_NS) or "").strip()
        doi = entry.findtext("arxiv:doi", default=None, namespaces=ARXIV_NS)
        authors = [
            (a.findtext("atom:name", default="", namespaces=ARXIV_NS) or "").strip()
            for a in entry.findall("atom:author", ARXIV_NS)
        ]
        out.append(
            record("arxiv", title, [a for a in authors if a], year,
                   "arXiv", doi, link, summary, None)
        )
    return out


# --------------------------------------------------------------------------- #
# Source: Semantic Scholar (JSON)                                             #
# --------------------------------------------------------------------------- #
def search_semantic_scholar(query, limit, from_year, timeout, retries):
    fields = "title,year,venue,authors,abstract,externalIds,url,citationCount"
    params = {"query": query, "limit": min(limit, 100), "fields": fields}
    if from_year:
        params["year"] = f"{from_year}-"
    url = "https://api.semanticscholar.org/graph/v1/paper/search?" + urllib.parse.urlencode(params)
    raw = http_get(url, timeout=timeout, retries=retries, accept="application/json")
    data = json.loads(raw)
    out = []
    for p in data.get("data", []) or []:
        ext = p.get("externalIds") or {}
        authors = [a.get("name", "") for a in (p.get("authors") or [])]
        out.append(
            record("semanticscholar", p.get("title"), [a for a in authors if a],
                   p.get("year"), p.get("venue"), ext.get("DOI"),
                   p.get("url"), p.get("abstract"), p.get("citationCount"))
        )
    return out


# --------------------------------------------------------------------------- #
# Source: OpenAlex (JSON, inverted-index abstracts)                           #
# --------------------------------------------------------------------------- #
def _invert_abstract(inv):
    if not inv:
        return None
    positions = {}
    for word, idxs in inv.items():
        for i in idxs:
            positions[i] = word
    if not positions:
        return None
    return " ".join(positions[i] for i in sorted(positions))


def search_openalex(query, limit, from_year, timeout, retries, email=None):
    params = {"search": query, "per-page": min(limit, 200)}
    if from_year:
        params["filter"] = f"from_publication_date:{from_year}-01-01"
    if email:
        params["mailto"] = email
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
    raw = http_get(url, timeout=timeout, retries=retries, accept="application/json")
    data = json.loads(raw)
    out = []
    for w in data.get("results", []) or []:
        venue = None
        loc = w.get("primary_location") or {}
        src = loc.get("source") or {}
        venue = src.get("display_name")
        authors = [
            ((a.get("author") or {}).get("display_name") or "")
            for a in (w.get("authorships") or [])
        ]
        out.append(
            record("openalex", w.get("display_name"), [a for a in authors if a],
                   w.get("publication_year"), venue, w.get("doi"),
                   w.get("id"), _invert_abstract(w.get("abstract_inverted_index")),
                   w.get("cited_by_count"))
        )
    return out


# --------------------------------------------------------------------------- #
# Merge / dedup                                                               #
# --------------------------------------------------------------------------- #
def dedup(records):
    """De-duplicate across sources. A record matches an existing one if EITHER its
    DOI or its normalized title matches — so the same paper that carries a DOI in one
    source but not another still collapses. First seen wins for scalar fields; missing
    fields are backfilled from duplicates, and contributing sources are noted in
    `also_in`. (Title-only matches can rarely be false positives; the researcher
    reviews the set anyway.)"""
    by_doi = {}
    by_title = {}
    result = []  # canonical records, in first-seen order

    def register(canon):
        if canon["doi"]:
            by_doi[canon["doi"]] = canon
        tk = norm_title_key(canon["title"])
        if tk:
            by_title[tk] = canon

    for r in records:
        tk = norm_title_key(r["title"])
        dk = r["doi"]
        if not tk and not dk:
            continue  # nothing to key on
        canon = (by_doi.get(dk) if dk else None) or (by_title.get(tk) if tk else None)
        if canon is not None:
            canon.setdefault("also_in", [])
            if r["source"] != canon["source"] and r["source"] not in canon["also_in"]:
                canon["also_in"].append(r["source"])
            for f in ("abstract", "venue", "year", "citations", "doi", "url"):
                if not canon.get(f) and r.get(f):
                    canon[f] = r[f]
            register(canon)  # re-index in case a DOI/title was just backfilled
        else:
            canon = dict(r)
            result.append(canon)
            register(canon)
    return result


# --------------------------------------------------------------------------- #
# Output                                                                      #
# --------------------------------------------------------------------------- #
def to_markdown(records, query):
    lines = [f"# Search results — \"{query}\"", "",
             f"_{len(records)} unique papers after de-dup. Fill the blank fields by reading each paper._", ""]
    for r in records:
        first = r["authors"][0].split()[-1] if r["authors"] else "Unknown"
        year = r["year"] or "n.d."
        lines.append(f"### {first} {year} — {r['title']}")
        srcs = "/".join([r["source"]] + r.get("also_in", []))
        lines.append(f"- Source / venue / year: {srcs} / {r['venue'] or '—'} / {year}")
        lines.append(f"- DOI / URL: {r['doi'] or r['url'] or '—'}")
        if r.get("citations") is not None:
            lines.append(f"- Citations: {r['citations']}")
        abs = (r["abstract"] or "").replace("\n", " ")
        if abs:
            lines.append(f"- Abstract: {abs[:400]}{'…' if len(abs) > 400 else ''}")
        lines.append("- Relevant claim / method / result: ")
        lines.append("- Limitation (the crack our idea might exploit): ")
        lines.append("- Relation to our idea: [supports | contrasts | builds-on | same-dataset | competes]")
        lines.append("- Gap note: ")
        lines.append("")
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# Main                                                                        #
# --------------------------------------------------------------------------- #
def main(argv=None):
    ap = argparse.ArgumentParser(description="Search arXiv + Semantic Scholar + OpenAlex.")
    ap.add_argument("--query", required=True, help="search string")
    ap.add_argument("--sources", default="arxiv,semanticscholar,openalex",
                    help="comma list: arxiv,semanticscholar,openalex")
    ap.add_argument("--limit", type=int, default=25, help="max results PER source")
    ap.add_argument("--from-year", type=int, default=None, help="only papers from this year onward")
    ap.add_argument("--format", choices=["json", "markdown"], default="json")
    ap.add_argument("--out", default=None, help="output file path (default: stdout)")
    ap.add_argument("--email", default=None, help="email for OpenAlex polite pool")
    ap.add_argument("--timeout", type=int, default=30)
    ap.add_argument("--retries", type=int, default=3)
    args = ap.parse_args(argv)

    sources = [s.strip().lower() for s in args.sources.split(",") if s.strip()]
    dispatch = {
        "arxiv": lambda: search_arxiv(args.query, args.limit, args.from_year, args.timeout, args.retries),
        "semanticscholar": lambda: search_semantic_scholar(args.query, args.limit, args.from_year, args.timeout, args.retries),
        "openalex": lambda: search_openalex(args.query, args.limit, args.from_year, args.timeout, args.retries, args.email),
    }

    all_records = []
    for s in sources:
        fn = dispatch.get(s)
        if not fn:
            print(f"[warn] unknown source '{s}', skipping", file=sys.stderr)
            continue
        try:
            recs = fn()
            print(f"[ok] {s}: {len(recs)} results", file=sys.stderr)
            all_records.extend(recs)
        except Exception as e:  # noqa: BLE001 — one source failing shouldn't kill the run
            print(f"[warn] {s} failed: {e}", file=sys.stderr)

    merged = dedup(all_records)
    print(f"[ok] {len(merged)} unique after de-dup", file=sys.stderr)

    if args.format == "markdown":
        text = to_markdown(merged, args.query)
    else:
        text = json.dumps({"query": args.query, "count": len(merged), "results": merged},
                          indent=2, ensure_ascii=False)

    if args.out:
        import os
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"[ok] wrote {args.out}", file=sys.stderr)
    else:
        print(text)


if __name__ == "__main__":
    main()
