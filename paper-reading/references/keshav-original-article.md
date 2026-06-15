# How to Read a Paper — S. Keshav (Full Text)

*Originally published in ACM SIGCOMM Computer Communication Review, 2007; updated 2013*
*Source: https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf*

---

## Abstract

Researchers spend a great deal of time reading research papers. However, this skill is rarely taught, leading to much wasted effort. This article outlines a practical and efficient three-pass method for reading research papers. I also describe how to use this method to do a literature survey.

---

## 1. Introduction

Reading a research paper is a skill that can be acquired. Many researchers learn it the hard way — by trial and error — which wastes time and leads to frustration. This article describes a three-pass method for reading research papers that I have developed over years of reading and reviewing papers. The key insight is that you should *not* read a paper linearly from start to finish. Instead, you should read it in up to three passes, each with a specific goal.

---

## 2. The Three-Pass Approach

### 2.1 First Pass: The 5Cs (5–10 minutes)

The goal of the first pass is to get a bird's-eye view of the paper. Read the title, abstract, introduction, section headings, conclusion, and references. **Do not read the body text.** Answer the 5Cs:

1. **Category**: What type of paper? (Measurement, analysis, prototype, survey, etc.)
2. **Context**: Which field? What are the related papers? What theoretical bases?
3. **Correctness**: Do the assumptions seem valid? Are there obvious flaws?
4. **Contributions**: What are the paper's main contributions (usually in intro)?
5. **Clarity**: Is the paper well-written?

At the end of the first pass, you should be able to decide: **Is this paper worth reading further?** If not, stop here. If yes, proceed to the second pass.

**Time**: 5–10 minutes for a typical conference paper.

### 2.2 Second Pass: The Main Thread (30–60 minutes)

Read the paper more carefully, but **ignore details like proofs and derivations**. Focus on:

- The figures, graphs, and illustrations
- The experimental setup and methodology
- Whether the results are clearly presented
- Which references are the key ones (not yet read)

Mark up the paper with questions and comments. At the end of this pass, you should be able to **summarize the paper's main thread** to someone else.

**Time**: Up to an hour for a conference paper.

### 2.3 Third Pass: Deep Understanding (1–2+ hours)

This is where you **reconstruct the paper's intellectual structure** as if you were the author. Goals:

- Understand the assumptions, both explicit and implicit
- Scrutinize the methodology and experimental design
- Identify innovations and potential flaws
- Think of alternative approaches or extensions

You should be able to **re-implement the paper** (at least conceptually) after this pass. This is the pass you do for papers that are directly relevant to your research.

**Time**: Several hours.

---

## 3. Doing a Literature Survey

The three-pass method also works for literature surveys:

1. **Search**: Find 30–50 recent papers in the area (Google Scholar, DBLP, conference proceedings)
2. **First pass on all**: Filter to 10–15 relevant papers
3. **Second pass on relevant**: Understand each paper's contributions
4. **Cluster**: Group papers by theme/approach
5. **Third pass on key papers**: Deep dive on 3–5 most important
6. **Synthesize**: Write the survey organized by themes, not paper-by-paper

---

## 4. Practical Advice

- **Don't read linearly.** The three-pass method saves enormous time.
- **Know when to stop.** Most papers don't deserve a third pass.
- **Take notes.** Write summaries in your own words; don't just highlight.
- **Use a reference manager** (Zotero, Mendeley, etc.)
- **Read the references** of important papers — they lead to the foundational work.
- **Discuss with others.** Explaining a paper tests your understanding.

---

## 5. Summary

| Pass | Time | Goal | Read |
|------|------|------|------|
| 1 | 5–10 min | Decide whether to continue | Title, abstract, intro, headings, conclusion, refs |
| 2 | 30–60 min | Grasp the main argument | All text, skip proofs; focus on figures, experiments |
| 3 | 1–2+ hr | Deep reconstruction | Everything; question every assumption |

The first pass is a filter. The second pass builds comprehension. The third pass builds expertise. Use them wisely.