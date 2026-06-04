# Stage I — Grounding

Goal: turn a raw idea into a *grounded, novel, defensible* problem — owned by the
researcher, evidenced against the literature, and fully logged. Three sub-phases:
**Ideation** -> **Literature review** -> **Problem & novelty**. Each ends at a gate
(A, B, C) defined in SKILL.md Section 5.

Throughout: counter when the user offloads thinking (SKILL.md Section 2), and write
every link / term / assumption / inference / decision to the workspace as it happens
(SKILL.md Section 3, templates in `workspace-spec.md`).

---

## Phase 1 — Ideation: Frame -> Propose -> Select

### 1a. Frame

Before any search or any proposal, interrogate the idea until it is genuinely pinned
down. This is where "ask as many counter-questions as possible" lives — but ask in
**small focused batches (2–4 at a time)**, adapt to the answers, and keep going until the
framing is real. A dumped wall of 30 questions gets shallow answers; a probing dialogue
gets depth.

Use the battery below as a well to draw from, not a script to read aloud. Prioritize the
questions whose answers are currently missing or vague.

**Counter-question battery**

*Core idea & motivation*
- In one sentence, what is the idea? Now say it again without any jargon.
- What made you think of this? What's the itch?
- If this worked perfectly, what becomes possible that isn't today?

*Problem & stakeholder*
- What problem does this solve? Be concrete.
- *Whose* problem is it — who feels the pain, and how often / how badly?
- What do they do today instead (the current workaround)? Why is it inadequate?

*Scope & boundaries*
- What is explicitly **in** scope? What is explicitly **out**?
- What's the smallest version of this that would still be interesting?
- Is this one idea or three? If three, which one are we doing first?

*Assumptions*
- What are you assuming is true for this to make sense? (List them; each goes to
  `_provenance/assumptions.md`.)
- What would have to be false for this idea to collapse?

*Success criteria*
- How would you know it worked? What's the measurable signal?
- What would a skeptic demand to see before believing it?

*Constraints & resources*
- What are your hard constraints — time, compute, data, budget, expertise, ethics/IRB?
- What data or tools do you already have access to?

*Prior art the user already knows*
- What's the closest existing work you're aware of? How is yours different (rough cut)?
- Whose paper would feel threatened if yours succeeded?

**Output:** write `01_ideation/framing.md`. Record assumptions to
`_provenance/assumptions.md` (each flagged "to confirm"), terms to `glossary.md`, any
links the user shares to `links.md`.

Do **not** advance to Propose until the frame answers, at minimum: the idea in plain
language, the problem + stakeholder, the in/out scope, and the top assumptions.

### 1b. Propose

Now Claude may put **candidate directions** on the table — but only candidates *derived
from the framing* (plus, optionally, a light scouting search to avoid obviously-solved
directions). Produce **2–4** distinct candidates. Never produce one (that's deciding).

Each candidate uses the Proposal Canvas (mirrors the structure researchers defend):
- **Direction** (one line): what is explored.
- **Assumption**: what it takes as given.
- **Method sketch**: roughly how it would be investigated.
- **Expected evidence**: what observation would support it.
- **Nearest known prior work**: the closest thing that already exists (cite the source;
  if unknown, say "to be checked in lit review").

Present them as a comparison the researcher can weigh. Be explicit: *"These are options
derived from what you told me; I'm not recommending one — which fits the idea you
actually believe in, and what would you change?"*

**Output:** write `01_ideation/proposals.md` with all candidates and their canvases.

### 1c. Select — **Gate A**

The researcher selects one candidate and *refines* it. Capture **their** reasoning for
the choice in their own words. If they say "you choose," counter (SKILL.md Section 2).

**Output:** write `01_ideation/selection.md` (chosen direction, the researcher's
refinements, their reasoning). Log the decision to `_provenance/decisions.md`
("Decided by: researcher").

**Gate A passes when** a single direction is selected and committed by the researcher.
Do not start the literature review before this.

---

## Phase 2 — Literature review: Search -> Screen -> Select

This phase builds a reusable evidence base for the idea (a "literature-memory" of
evidence cards, citation links, and gap notes). It tells us the *scope* of the idea and
seeds the introduction's related work.

### 2a. Search

Turn the selected direction into queries. Use **multiple perspectives** and **query
reformulation** — different phrasings, synonyms, method-terms vs. problem-terms,
adjacent fields. Aim for breadth first, then narrow.

Run `scripts/search_papers.py` (arXiv + Semantic Scholar + OpenAlex) and/or `web_search`
for recency and coverage. Assemble a candidate pool.

**Log everything:** append *every query run* and *every result link* to
`02_literature/search_log.md` — including dead-end queries. The audit trail matters as
much as the hits. Save raw structured output under `02_literature/papers/`.

### 2b. Screen

Agree on inclusion/exclusion criteria *with the researcher* (e.g., recency window,
relevance to the direction, venue/credibility, empirical vs. position). Then screen the
pool: for each paper, an **include or exclude** decision **with a reason**.

**Output:** write `02_literature/screening.md` (each candidate: keep/drop + one-line
reason). This is the screen step — be willing to drop aggressively; a tight set beats a
bloated one.

### 2c. Select — **Gate B**

From the screened set, select the most relevant papers: the closest-to-idea work and any
paper that would plausibly be *cited in the introduction / related work*. For each
selected paper, write an **evidence card**:

```
### <Author Year> — <short title>
- Venue / year / DOI or URL:
- Relevant claim / method / result:
- Limitation (the crack your idea might exploit):
- Relation to our idea: [supports | contrasts | builds-on | same-dataset | competes]
- Gap note: what it leaves open
```

**Output:** write `02_literature/selected_papers.md` (the evidence cards). Add every DOI/
URL to `_provenance/links.md`; add any new terms to `glossary.md`.

**Gate B passes when** a justified selected set exists with evidence cards, and the
researcher agrees the scope of the idea is now visible.

---

## Phase 3 — Problem & novelty

Now run the discussion the researcher described: *what idea are we proposing, what
problem are we solving, what is the existing workaround.* Then the novelty test.

### 3a. Problem statement

Facilitate the researcher articulating (Claude scaffolds and questions; the researcher
supplies the substance):
1. **The idea we propose** — the committed direction, sharpened by what the literature taught us.
2. **The problem we solve** — concrete, and *whose* problem, and why it matters.
3. **Existing workarounds** — how the problem is handled today, grounded in the evidence
   cards, and where each falls short.

**Output:** write `03_problem/problem_statement.md`. Every claim about prior work must
point to an evidence card / link.

### 3b. Novelty memo — **Gate C (the Novelty Gate)**

The **researcher authors the novelty claim.** Claude's job is to make it defensible, not
to make it. Procedure:
1. Give the researcher the novelty-memo template (in `workspace-spec.md`).
2. **Stress-test against the selected papers.** For *every* paper that overlaps, ask the
   researcher to differentiate: "Lee 2023 already does X on the same dataset — what,
   exactly, is different about yours?" Surface overlaps proactively; do not let a
   collision slide.
3. If the novelty claim is unsupported by — or contradicted by — the literature, say so
   plainly and send it back to re-framing or more search.
4. **Claude never writes "this is novel."** Claude writes "this claim survives papers
   A,B,C; it collides with paper D until differentiated."

**Output:** write `03_problem/novelty_memo.md` (the researcher's claim + the
differentiation against each overlapping paper). Log the gate decision to
`_provenance/decisions.md`.

**Gate C passes — "move ahead" — when** the researcher can state idea + problem +
workarounds + a novelty claim that survives every overlapping selected paper. Then, and
only then, advance to Stage II (`stages-2-5-roadmap.md`). Otherwise loop back.

---

## Common failure modes to resist

- **Quietly inventing the idea.** If you find yourself supplying the research direction,
  the hypothesis, or the novelty rather than eliciting it — stop and counter.
- **Skipping the log.** If a link/term/assumption/decision exists in chat but not in the
  workspace, it doesn't exist. Write it.
- **Premature search.** No literature review before Gate A (a committed direction).
- **One proposal.** Proposing a single direction is deciding for the user. Always 2–4.
- **Declaring novelty.** Never. The researcher claims it; you only test it.
- **Bloated paper sets.** Screen hard. Closeness to the idea beats count.
