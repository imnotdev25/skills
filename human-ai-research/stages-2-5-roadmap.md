# Stages II–V — roadmap (scaffolds, co-develop)

These stages are **architected, not authored.** Their substance — which hypothesis,
which experiment, how to validate, what to claim — belongs to the researcher and depends
on the specific project. When you reach one, say so plainly: *"This stage is a scaffold;
let's build it together,"* then co-develop it. Do **not** silently auto-fill it.

The same operating contract applies throughout: human owns commitments, Claude
implements; counter when thinking is offloaded; log everything to `_provenance/`; pass
each gate explicitly. Each stage writes into `_stages/`.

Each scaffold names the **regimes** it should eventually support (from the project's
framework figures) so we know the design space when we flesh it out.

---

## Stage II — Hypothesis formation & planning

**Purpose:** convert the grounded, novel problem into testable hypotheses and an
executable plan.

**Sub-steps (to detail together):** question generation -> hypothesis formulation ->
feasibility analysis -> experiment design.

**Regimes to support (design space):**
- *Proposal-centered* — proposal canvas, local refinement, ranked set.
- *Deliberative multi-agent* — generate / debate / rank / evolve hypotheses (optional, heavy).
- *Structure-guided* — relation-constrained reasoning over a concept/method/result graph.
- *Search-based / evolutionary* — branch, score, prune candidate plans.

**Gate (the full selection gate):** evidence support, **novelty** (carried from Gate C),
**feasibility**, **resource cost**, **risk/safety**. This is where feasibility/cost/risk
finally get weighed. Researcher decides go/no-go.

**Workspace:** `_stages/02_hypothesis_planning.md` (hypotheses, feasibility notes,
experiment design, the selection-gate scorecard).

**Counter-question themes:** what exactly would falsify this? what's the minimal
experiment? what resource do you actually have? what's the riskiest assumption?

---

## Stage III — Experimentation & tool use

**Purpose:** realize the plan as concrete actions and produce execution artifacts.

**Sub-steps:** tool selection -> protocol generation -> execution -> data processing.

**Regimes to support:**
- *Code-native* — repository edit / run / patch loop (most relevant for ML/SW research).
- *Tool-orchestrated* — planner-mediated tool calls (search, DB, code, APIs) + observations.
- *Laboratory-robotic* — protocol-to-instrument (mostly N/A unless wet-lab).
- *Human-gated* — bounded actions behind validity/safety/resource/ethics checkpoints.

**Important:** every execution writes an artifact + a log. Side-effectful or irreversible
actions go behind a human checkpoint — Claude proposes, the researcher approves.

**Workspace:** `_stages/03_experimentation.md` + an artifacts/log area to be defined.

**Counter-question themes:** which baseline are we beating? what does a null result look
like? what could silently corrupt the data?

---

## Stage IV — Validation & review

**Purpose:** apply rejection pressure before believing a result. Output: keep / revise /
reject.

**Sub-steps:** result analysis -> validation & verification -> error debug/detection ->
peer-like review.

**Regimes to support:**
- *Execution-coupled* — reruns, ablations, baseline compare, consistency signal.
- *Critique-mediated* — critic review / comparative judgment / revision signal.
- *Expert-grounded* — claim package -> expert/temporal scrutiny -> adequacy signal.

**Workspace:** `_stages/04_validation.md` (what was tested, what survived, the keep/
revise/reject decision with the researcher's reasoning).

**Counter-question themes:** would this replicate? is the metric the right one? what's the
strongest objection a reviewer raises, and is it answered?

---

## Stage V — Reporting & knowledge communication

**Purpose:** communicate claims while keeping them aligned with the evidence.

**Sub-steps:** outline & argumentation -> figure/table generation -> manuscript drafting
-> formatting & citation.

**Regimes to support:**
- *Draft-centered* — fluent section/manuscript drafting (watch: narrative outrunning evidence).
- *Review-centered* — review / response / revision dialogue.
- *Artifact-linked* — claim<->figure<->table<->code<->provenance alignment checklist.

**Important:** every claim in the manuscript must trace to a workspace artifact (an
evidence card, a result, a provenance entry). Reuse the provenance log built since Stage I.
Follow copyright limits when quoting sources.

**Workspace:** `_stages/05_reporting.md` (outline, claim->evidence map, draft sections).

**Counter-question themes:** does every claim have backing? does any sentence over-state
what the data shows? is each figure honestly captioned?

---

## When we co-develop these

For each stage, decide together: which regime(s) fit this project, which sub-steps we
actually need, what the workspace files and gate scorecard look like, and which actions
require a human checkpoint. Then I'll write that stage's full reference the way Stage I is
written — but only after you've made those calls.
