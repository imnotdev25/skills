# AI Prompt Templates for Three-Pass Reading

Copy-paste these into your AI assistant (Hermes, Claude, ChatGPT, etc.) at each pass.

---

## PASS 1 PROMPT — The 5Cs Scan

```
You are a research assistant helping with Pass 1 of Keshav's three-pass method.
Paper text provided below. Extract and present the 5Cs:

1. CATEGORY: What type of paper? (survey, novel method, benchmark, position, theory, system, empirical study)
2. CONTEXT: Which field/subfield? Key prior works cited? Who is the audience?
3. CORRECTNESS: Do assumptions seem reasonable? Any red flags in claims?
4. CONTRIBUTIONS: What are the authors' stated contributions (usually in Introduction)?
5. CLARITY: How well-written? Accessible to non-specialists?

Output as a structured brief. DO NOT DECIDE for the user — just present the 5Cs.

Paper:
[paste_paper_text_here_first_2000_chars_or_full_if_short]
```

**Expected Output Format:**
```markdown
## Pass 1: 5Cs Assessment

**CATEGORY:** [one line]
**CONTEXT:** [2-3 sentences]
**CORRECTNESS:** [2-3 sentences, flag any concerns]
**CONTRIBUTIONS:** [bullet list of 3-5 stated contributions]
**CLARITY:** [1-2 sentences]

---
*Decision needed: Continue to Pass 2? (Yes / No / Defer)*
```

---

## PASS 2 PROMPT — Structured Comprehension

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
[paste_full_paper_text_here]
```

**Expected Output Format:** Four separate markdown blocks for summary.md, problem.md, method.md, results.md

---

## PASS 3 PROMPT — Reviewer Mode

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

**Expected Output Format:**
```markdown
## Pass 3: Reviewer Questions

### ASSUMPTIONS
1. ...
2. ...

### EXPERIMENTAL DESIGN
1. ...
...

### CLAIMS VS EVIDENCE
...

### REPRODUCIBILITY
...

### EXTENSIONS & FOLLOW-UPS
...
```

---

## TEACHING MODE PROMPT — Worked Example

```
You are teaching Keshav's three-pass method. Use the sample paper provided.
Walk through each pass showing:
1. What you read / skip
2. The AI prompt you'd use
3. The expected output (annotated with teaching notes)
4. Common mistakes at this pass

Sample paper: [sample_paper_text]
```