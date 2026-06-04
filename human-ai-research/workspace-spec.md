# Workspace specification

The workspace is the single source of truth for a research project. Use this exact
layout. Create files lazily (only when a phase reaches them), but never improvise the
structure or the provenance discipline.

## Locating / creating the workspace

- **First action of every session:** check for an existing workspace (look for a
  directory containing `00_README.md`). If found, read `00_README.md` for the current
  stage and continue. If not, create one.
- Name the directory with a short project slug, e.g. `rupeebias-followup/`. Put it where
  the researcher keeps work (ask if unsure — do not assume a path).

## Canonical layout

```
<project-slug>/
├── 00_README.md                      # overview, CURRENT STAGE, status, file index
├── 01_ideation/
│   ├── framing.md                    # Frame step
│   ├── proposals.md                  # Propose step (2–4 candidates)
│   └── selection.md                  # Select step — Gate A (researcher's choice + reasoning)
├── 02_literature/
│   ├── search_log.md                 # every query + every result link (incl. dead ends)
│   ├── screening.md                  # include/exclude decisions + reasons
│   ├── selected_papers.md            # evidence cards — Gate B
│   └── papers/                       # raw structured output from search_papers.py
├── 03_problem/
│   ├── problem_statement.md          # idea / problem / existing workarounds
│   └── novelty_memo.md               # researcher's novelty claim + differentiation — Gate C
├── _provenance/
│   ├── links.md                      # every URL used, with purpose
│   ├── glossary.md                   # every term / acronym
│   ├── assumptions.md                # every assumption Claude made (flagged to confirm)
│   └── decisions.md                  # who decided what, when, why
└── _stages/                          # Stages II–V land here as they're co-developed
    ├── 02_hypothesis_planning.md
    ├── 03_experimentation.md
    ├── 04_validation.md
    └── 05_reporting.md
```

---

## Provenance logging rules (the "dump everything" mechanism)

Append to these continuously — at the moment the thing occurs, not in a batch later.

- **A URL is used / cited** -> append to `_provenance/links.md`.
- **A term or acronym is used or defined** -> append to `_provenance/glossary.md`.
- **Claude makes an assumption or an inference** -> append to `_provenance/assumptions.md`,
  flagged `[to confirm]` until the researcher confirms it.
- **A decision is taken at any point** -> append to `_provenance/decisions.md` with who
  decided (researcher vs. Claude-suggested-and-adopted) and the reasoning.

Rule of thumb: *if Claude is about to assert, assume, define, link, or decide, and it is
not landing in one of these files, write it down first.*

---

## File templates

Instantiate these as-is, filling the brackets. Keep them terse and current.

### `00_README.md`
```
# <Project title>

**Current stage:** I — Grounding (phase: <Frame|Propose|Select|Search|Screen|Select|Problem|Novelty>)
**Status:** <one line>
**Last updated:** <YYYY-MM-DD>

## One-paragraph overview
<what this project is, in the researcher's words>

## File index
- 01_ideation/ — framing, proposals, selection
- 02_literature/ — search_log, screening, selected_papers, papers/
- 03_problem/ — problem_statement, novelty_memo
- _provenance/ — links, glossary, assumptions, decisions
- _stages/ — Stages II–V (status: not started)

## Open gates
- [ ] Gate A — direction selected & committed
- [ ] Gate B — papers screened & selected with evidence cards
- [ ] Gate C — novelty claim survives the literature
```

### `01_ideation/framing.md`
```
# Framing

## Idea (plain language)
## Motivation / the itch
## Problem & stakeholder (whose pain, how often/bad)
## Current workaround & why it's inadequate
## In scope / out of scope
## Smallest interesting version
## Top assumptions  (also -> _provenance/assumptions.md)
## Success criteria / what a skeptic demands
## Constraints (time, compute, data, budget, ethics)
## Prior art the researcher already knows
```

### `01_ideation/proposals.md`
```
# Candidate directions (NOT recommendations — researcher selects)

## Candidate 1 — <one-line direction>
- Assumption:
- Method sketch:
- Expected evidence:
- Nearest known prior work: <source or "to check">

## Candidate 2 — ...
## Candidate 3 — ...
```

### `01_ideation/selection.md`
```
# Selection — Gate A

**Chosen direction:** <candidate #, restated>
**Researcher's refinements:** <how they changed it>
**Why this one (researcher's reasoning):** <their words>
**Decided by:** researcher — <date>
```

### `02_literature/search_log.md`
```
# Search log

## Run <N> — <date> — tool: <search_papers.py | web_search>
- Query: "<query string>"  | sources: <...> | from-year: <...>
- Results (link per line):
  - <title> — <url/DOI>
  - ...
- Notes: <why this query; dead end? promising?>
```

### `02_literature/screening.md`
```
# Screening

**Inclusion criteria (agreed with researcher):** <...>
**Exclusion criteria:** <...>

| Paper | Keep? | Reason |
|---|---|---|
| <Author Year> | keep / drop | <one line> |
```

### `02_literature/selected_papers.md`
```
# Selected papers — evidence cards (Gate B)

### <Author Year> — <short title>
- Venue / year / DOI or URL:
- Relevant claim / method / result:
- Limitation (the crack our idea might exploit):
- Relation to our idea: [supports | contrasts | builds-on | same-dataset | competes]
- Gap note:
```

### `03_problem/problem_statement.md`
```
# Problem statement

## The idea we propose
## The problem we solve (concrete) & whose problem it is
## Why it matters
## Existing workarounds & their limits  (each -> an evidence card / link)
```

### `03_problem/novelty_memo.md`
```
# Novelty memo — Gate C   (authored by the researcher)

## Novelty claim (researcher's words)
## Differentiation vs. each overlapping paper
- vs. <Author Year> (collides on <X>): different because <researcher's answer>
- vs. ...
## Claude's literature check (NOT a novelty verdict)
- Survives: <papers it clears>
- Collides until differentiated: <papers>  -> status: <resolved? open?>
**Gate C decision (researcher):** move ahead / loop back — <date, reasoning>
```

### `_provenance/links.md`
```
# Links
| Date | URL | Used for |
|---|---|---|
```

### `_provenance/glossary.md`
```
# Glossary
| Term | Definition | First used in |
|---|---|---|
```

### `_provenance/assumptions.md`
```
# Assumptions (Claude-made unless noted)
| Date | Assumption | Status |
|---|---|---|
| <date> | <assumption> | [to confirm] / confirmed / rejected |
```

### `_provenance/decisions.md`
```
# Decision log
| Date | Decision | Decided by | Reasoning |
|---|---|---|---|
```

### `_stages/02..05_*.md`
Leave as stubs until that stage is co-developed:
```
# Stage <N> — <name>
STATUS: not started — to be co-developed with the researcher (see stages-2-5-roadmap.md)
```
