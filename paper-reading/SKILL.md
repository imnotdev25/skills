---
name: keshav-three-pass-reading
version: 1.0.0
description: S. Keshav's three-pass paper reading method with AI-assisted passes and structured outputs (Summary, Problem, Method, Results, Takeaways). Teaches when to skim, when to dig deep, and how to use AI as a reading companion without outsourcing judgment.
trigger: User wants to read a paper effectively using the three-pass method, or wants structured comprehension outputs from a paper they're reading.
context: paper_path, paper_text (optional), pass_number (1|2|3|all)
modes: [read, analyze, teach]
---

# Keshav Three-Pass Paper Reading Skill

**Based on:** S. Keshav, "How to Read a Paper" (ACM SIGCOMM 2007, updated 2013)

**Purpose:** Guide researchers through effective paper reading using three progressive passes, with AI assistance at each stage while preserving human judgment. Produces structured comprehension artifacts.

## The Three-Pass Method

| Pass | Time | Focus | AI Role | Human Judgment Required |
|------|------|-------|---------|------------------------|
| **Pass 1** | 5–10 min | 5Cs: Category, Context, Correctness, Contributions, Clarity | Summarize RQ, contributions, conclusions | **Decide: worth reading further?** |
| **Pass 2** | 30–60 min | Main thread, figures, experimental setup, key citations | Explain methods, figures, concepts | **Cross-check: do numbers/claims match text?** |
| **Pass 3** | 1–2+ hrs | Deep reconstruction, assumptions, flaws, reproducibility | Play reviewer: probe assumptions, baselines, leaks | **Decide: what to adopt/cite/build on?** |

---

## Structured Outputs (Generated After Pass 2 or 3)

The skill produces **five standardized artifacts** capturing comprehension:

| Artifact | Purpose | When Generated |
|----------|---------|----------------|
| `summary.md` | 3–5 sentence executive summary | After Pass 2 |
| `problem.md` | Problem statement, motivation, gap | After Pass 2 |
| `method.md` | Core approach, algorithm, architecture | After Pass 2 |
| `results.md` | Key findings, numbers, tables, figures | After Pass 2 |
| `takeaways.md` | Actionable insights, limitations, future work | After Pass 3 |

---

## Workflow

### Prerequisites
- Paper accessible as text (`.txt`, `.md`) or PDF (use `pdftotext` first)
- Paper path or content provided

### Pass 1: The 5Cs Scan (5–10 minutes)

**Goal:** Answer the 5Cs to decide *whether to continue*.

**Read:** Title, Abstract, Introduction, Section Headings, Conclusion, References.

**AI Assistance Prompt:**
```
You are a research assistant helping with Pass 1 of Keshav's three-pass method.
Paper text provided below. Extract and present:

1. CATEGORY: What type of paper? (survey, novel method, benchmark, position, theory, system, empirical study)
2. CONTEXT: Which field/subfield? Key prior works cited? Who is the audience?
3. CORRECTNESS: Do assumptions seem reasonable? Any red flags in claims?
4. CONTRIBUTIONS: What are the authors' stated contributions (usually in Introduction)?
5. CLARITY: How well-written? Accessible to non-specialists?

Output as a structured brief. DO NOT DECIDE for the user — just present the 5Cs.
Paper:
[paper_text_first_2000_chars_or_full_if_short]
```

**Human Decision Point:** Based on 5Cs, decide: **Skip / Defer / Continue to Pass 2**.

**Record Decision:** Save to `pass1_decision.md` with rationale.

---

### Pass 2: The Main Thread (30–60 minutes)

**Goal:** Understand the paper's argument and evidence without getting lost in proofs.

**Read:** Full paper linearly, but **skip proof details** (appendices, derivations). Focus on:
- Figures and tables (what they show, trends, surprises)
- Experimental setup (datasets, baselines, metrics, hardware)
- Which key works are cited and how they're positioned
- The "story arc": problem → insight → method → results → implications

**AI Assistance Prompt:**
```
You are a research assistant helping with Pass 2 of Keshav's three-pass method.
Paper text provided below. Produce structured comprehension:

## SUMMARY (3-5 sentences)
Executive summary of the paper's core argument and findings.

## PROBLEM
- Core problem addressed
- Motivation / real-world impact
- Gap in prior work this paper fills
- Research questions or hypotheses

## METHOD
- Core insight / innovation (1-2 paragraphs)
- Algorithm / architecture / approach description
- Key design choices and why they matter
- Theoretical claims (if any)

## RESULTS
- Headline numbers (exact metrics from paper)
- Key figures/tables described with takeaways
- Baselines compared and outcomes
- Ablation studies (if any)
- Surprising or counterintuitive findings

## CITATIONS OF NOTE
- 3-5 most important prior works cited and how this paper relates to each

IMPORTANT: Cross-reference every number/claim against the provided text. Flag any discrepancies.
Paper:
[full_paper_text]
```

**Human Verification:** For each key number in Results, **verify against original text**. Do not trust AI extraction blindly.

**Output Files Created:**
- `summary.md` — from SUMMARY section
- `problem.md` — from PROBLEM section
- `method.md` — from METHOD section
- `results.md` — from RESULTS section (with verified numbers)

---

### Pass 3: Deep Reconstruction (1–2+ hours)

**Goal:** Reconstruct the author's thinking; scrutinize validity.

**Activities:**
- Could you reproduce the method from the description alone?
- Are assumptions valid? (data distribution, compute budget, task formulation)
- Do experiments support conclusions? (missing baselines, cherry-picked metrics, data leaks)
- Evaluation biases? (oracle choice, prompt sensitivity, seed variance)
- Overclaims? (generalization beyond evidence, "solves X" when only shows improvement on Y)
- What would you change / extend / challenge?

**AI Assistance Prompt (Reviewer Mode):**
```
You are a rigorous peer reviewer for this paper. Paper text and Pass 2 outputs provided.
Generate probing questions organized by category:

## ASSUMPTIONS
- What assumptions underlie the method? Are they explicit?
- What would break if assumption X is violated?

## EXPERIMENTAL DESIGN
- Are baselines appropriate and strong? Any missing?
- Is the evaluation metric aligned with the claimed contribution?
- Any data leakage risks (train/test overlap, oracle contamination)?
- Statistical rigor: seeds, variance, significance testing?

## CLAIMS VS EVIDENCE
- Which claims are well-supported? Which overreach?
- Does "we solve X" actually mean "we improve on benchmark Y by Z%"?
- External validity: do results generalize beyond the experimental setup?

## REPRODUCIBILITY
- Sufficient detail to reimplement? Missing hyperparameters?
- Compute requirements stated? Code/data availability?

## EXTENSIONS & FOLLOW-UPS
- What's the most natural next experiment?
- What would a strong ablation look like?
- How might this method fail in deployment?

Output as structured questions. Do NOT answer them — the human researcher answers.
Paper: [full_paper_text]
Pass 2 outputs: [summary.md, problem.md, method.md, results.md]
```

**Human Synthesis:** Answer the reviewer questions. Write `takeaways.md` with:

```markdown
# Takeaways: [Paper Title]

## What I'll Use / Cite
- [Specific technique, insight, dataset, baseline]

## Limitations Noted
- [Assumption fragility, eval gap, scope restriction]

## Open Questions / Extensions
- [Concrete follow-up experiments or analyses]

## Verdict
- [Skip / Reference / Build Upon / Reproduce]
```

---

## Usage Examples

### Quick Start (All Passes)
```
User: "Read this paper with the three-pass method: /path/to/paper.txt"
Agent: Runs Pass 1 → presents 5Cs → user decides → Pass 2 → structured outputs → Pass 3 → takeaways
```

### Specific Pass
```
User: "Just do Pass 1 on this paper"
Agent: Runs 5Cs scan only, saves pass1_decision.md
```

### AI-Assisted Pass 2 on Existing Paper
```
User: "I've read the paper. Generate the 4 structured outputs from Pass 2."
Agent: Uses AI prompt with full paper text → produces summary.md, problem.md, method.md, results.md
```

### Reviewer Mode (Pass 3 Only)
```
User: "Act as reviewer on this paper I've already read. Here are my Pass 2 notes."
Agent: Runs reviewer prompt → generates probing questions → user answers → takeaways.md
```

---

## File Output Structure

```
paper_reading/
├── pass1_decision.md        # 5Cs + continue/skip decision
├── summary.md               # 3-5 sentence executive summary
├── problem.md               # Problem, motivation, gap, RQs
├── method.md                # Core approach, algorithm, design choices
├── results.md               # Verified headline numbers, figures, ablations
└── takeaways.md             # Personal synthesis: use, limits, extensions, verdict
```

---

## Quality Standards

- **Never fabricate numbers.** Every metric in `results.md` must trace to paper text.
- **Flag uncertainty.** If paper is vague on a detail, state: "Paper does not specify X."
- **Separate summary from judgment.** `summary.md`/`problem.md`/`method.md`/`results.md` = what the paper *says*. `takeaways.md` = what *you* think.
- **Cross-check Pass 2 extractions** against original text before saving.
- **Pass 3 questions are probes, not answers.** The human provides answers in `takeaways.md`.

---

## Common Pitfalls

❌ **Skipping Pass 1** — leads to wasting time on irrelevant papers
❌ **Trusting AI extraction without verification** — hallucinated numbers propagate
❌ **Conflating summary with critique** — keep `results.md` descriptive; save critique for `takeaways.md`
❌ **Reading proofs in Pass 2** — saves them for Pass 3 (or skip entirely if not reproducing)
❌ **Not making a Pass 1 decision** — the 5Cs are useless without the continue/skip call

---

## Integration Notes

- Works with any paper source: arXiv PDF, local `.txt`, conference PDF
- Pair with `arxiv` skill to fetch paper, `pdftotext` to convert
- Complements `academic-paper-review` skill: this is for *your* reading; that skill produces *review deliverables* for a collection
- Can be used in batch: run Pass 1 on 20 papers, continue only on 3–5

---

## Teaching Mode

When `mode=teach`, the skill explains the method and runs a **worked example** on a short sample paper (provided in `references/sample-paper.txt`), showing:
- Annotated Pass 1 5Cs output
- Annotated Pass 2 structured outputs
- Annotated Pass 3 reviewer questions and takeaways
- Common mistakes highlighted

Use when onboarding new researchers to the method.

---

## Reference Files

- `references/keshav-original-article.md` — Full text of Keshav's "How to Read a Paper"
- `references/sample-paper.txt` — Short ML paper for teaching mode
- `references/ai-prompts.md` — Full prompt templates for each pass (copy-paste ready)
- `templates/output-structure.md` — Markdown templates for the 5 output files

---

## Success Checklist

- [ ] Pass 1: 5Cs extracted, decision recorded with rationale
- [ ] Pass 2: 4 structured files created, all numbers verified against paper
- [ ] Pass 3: Reviewer questions generated, human answers synthesized into takeaways.md
- [ ] No fabricated metrics in any output
- [ ] Clear separation: descriptive (what paper says) vs. evaluative (what I think)
- [ ] Decision recorded: Skip / Reference / Build Upon / Reproduce