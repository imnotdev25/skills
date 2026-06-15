# Output File Templates

Copy these templates when creating the structured output files.

---

## summary.md

```markdown
# Summary: [Paper Title]

**Paper:** [Title] — [Authors] — [Venue/arXiv] — [Year]
**Domain:** [e.g., LLM alignment, efficient attention, benchmark]

---

## Executive Summary (3–5 sentences)

[One paragraph capturing: problem → insight → method → key result → implication]

---

## One-Sentence Takeaway

[Single sentence you'd use to describe this paper to a colleague]
```

---

## problem.md

```markdown
# Problem: [Paper Title]

**Paper:** [Title] — [Authors] — [Venue/arXiv] — [Year]

---

## Core Problem

[What specific problem does this paper address? 2–3 sentences]

---

## Motivation & Real-World Impact

[Why does this problem matter? Who cares? What happens if unsolved?]

---

## Gap in Prior Work

[What did previous approaches miss? What limitation does this paper overcome?]

---

## Research Questions / Hypotheses

- RQ1: [Explicit or implicit research question]
- RQ2: [...]
- H1: [Hypothesis if stated]

---

## Problem Type Classification

- [ ] Novel method for existing problem
- [ ] New problem formulation
- [ ] New benchmark / dataset
- [ ] Theoretical analysis of known method
- [ ] System / implementation paper
- [ ] Survey / position paper
```

---

## method.md

```markdown
# Method: [Paper Title]

**Paper:** [Title] — [Authors] — [Venue/arXiv] — [Year]

---

## Core Insight / Innovation (1–2 paragraphs)

[In your own words: what is the key idea? What's the "aha!" moment?]

---

## Algorithm / Architecture / Approach

[Step-by-step description. Pseudocode-level detail if applicable.]

### Key Components

| Component | Description | Why It Matters |
|-----------|-------------|----------------|
| [Name] | [What it does] | [Design rationale] |
| [Name] | [What it does] | [Design rationale] |

---

## Key Design Choices

| Choice | Alternative Considered | Rationale Given |
|--------|------------------------|-----------------|
| [e.g., loss function] | [e.g., cross-entropy] | [e.g., handles class imbalance] |
| ... | ... | ... |

---

## Theoretical Claims (if any)

- Claim 1: [Statement] — [Proof sketch / reference]
- Claim 2: [...]

---

## Complexity / Requirements

- **Time complexity:** [e.g., O(n²) per layer]
- **Memory complexity:** [e.g., O(n) activations]
- **Compute budget:** [e.g., 8×A100 for 3 days]
- **Data requirements:** [e.g., 1M samples, 10B tokens]

---

## Reproducibility Checklist

- [ ] Hyperparameters fully specified
- [ ] Random seeds reported
- [ ] Code available (link: [URL])
- [ ] Data available (link: [URL])
- [ ] Hardware specified
```

---

## results.md

```markdown
# Results: [Paper Title]

**Paper:** [Title] — [Authors] — [Venue/arXiv] — [Year]

---

## Headline Numbers (Verified Against Paper)

| Metric | Our Method | Best Baseline | Δ | Dataset / Setting |
|--------|------------|---------------|---|-------------------|
| [Metric] | [X%] | [Y%] | [+Z%] | [e.g., MMLU 5-shot] |
| ... | ... | ... | ... | ... |

> **Verification:** All numbers above traced to Table [N] / Figure [N] / page [N] of paper.

---

## Key Figures & Tables

### Figure [N]: [Title]
**What it shows:** [Description]
**Key takeaway:** [What you learn from it]
**Surprises:** [Anything counterintuitive?]

### Table [N]: [Title]
**Full table reproduced:** [Markdown table with exact numbers]
**Key takeaway:** [...]

---

## Baseline Comparison

| Baseline | Type | Result | Notes |
|----------|------|--------|-------|
| [Name] | [SOTA / ablation / classical] | [Metric] | [Why included] |

---

## Ablation Studies

| Component Removed | Metric Change | Interpretation |
|-------------------|---------------|----------------|
| [e.g., positional encoding] | [−2.3%] | [Critical for long context] |

---

## Surprising / Counterintuitive Findings

1. [Finding that contradicts conventional wisdom]
2. [Unexpected scaling behavior]
3. [Negative result that's informative]

---

## Limitations Acknowledged by Authors

- [Quote or paraphrase from paper's limitations section]
- ...

---

## Missing Evaluations (Not in Paper)

- [ ] Statistical significance / variance across seeds
- [ ] Human evaluation
- [ ] Out-of-distribution generalization
- [ ] Compute / latency tradeoffs
- [ ] Ablation of [specific component]
```

---

## takeaways.md

```markdown
# Takeaways: [Paper Title]

**Paper:** [Title] — [Authors] — [Venue/arXiv] — [Year]
**Date read:** [YYYY-MM-DD]
**Passes completed:** [1, 2, 3]

---

## What I'll Use / Cite

- **Technique:** [Specific method component worth adopting]
- **Insight:** [Conceptual framing that shifts how I think about X]
- **Baseline:** [Strong baseline to compare against in my work]
- **Dataset:** [Benchmark/dataset to evaluate on]
- **Citation:** [Prior work this paper surfaced that I should read]

---

## Limitations Noted

| Limitation | Severity | Impact on My Use Case |
|------------|----------|----------------------|
| [e.g., assumes IID data] | High / Med / Low | [Blocks / Caution / Fine] |
| [e.g., eval only on English] | ... | ... |

---

## Open Questions / Extensions

1. **Natural next experiment:** [Concrete experiment]
2. **Strongest ablation missing:** [What would convince you more?]
3. **Scaling question:** [How does this behave at 10× scale?]
4. **Failure mode:** [Where would this break in deployment?]
5. **Combination opportunity:** [Could this combine with X from paper Y?]

---

## Verdict

**Decision:** [Skip / Reference / Build Upon / Reproduce]

**Rationale:** [2–3 sentences explaining your decision]

---

## Follow-Up Actions

- [ ] Read cited paper: [Title]
- [ ] Implement [component] in [my project]
- [ ] Run experiment: [description]
- [ ] Discuss with [colleague] about [aspect]
```

---

## pass1_decision.md

```markdown
# Pass 1 Decision: [Paper Title]

**Paper:** [Title] — [Authors] — [Venue/arXiv] — [Year]
**Date:** [YYYY-MM-DD]

---

## 5Cs Assessment

**CATEGORY:** [Type]
**CONTEXT:** [Field, audience, key prior work]
**CORRECTNESS:** [Assumptions reasonable? Red flags?]
**CONTRIBUTIONS:** [Stated contributions]
**CLARITY:** [Writing quality]

---

## Decision

- [ ] **CONTINUE to Pass 2** — Worth deep reading
- [ ] **DEFER** — Relevant but not urgent; add to reading list
- [ ] **SKIP** — Not relevant / low quality / superseded

**Rationale:** [2–3 sentences explaining decision]

---

## Next Steps (if Continue)

- [ ] Schedule Pass 2 reading session
- [ ] Fetch full paper PDF if only had abstract
- [ ] Identify key figures to focus on
```