---
name: trace-code-work
description: Maintain auditable, dated coding-session records for implementation, debugging, refactoring, and code review. Use whenever Codex changes source code, tests, configuration, schemas, dependencies, build or deployment code, or resumes a coding project that has prior session logs. Create and update code-logs/YYYY-MM-DD/DECISIONS.md, FLOW.md, EXPLORE.md, and QUIZ.md; record why approaches and libraries were chosen, trace caller-to-callee execution paths and modified segments, remember explored files/functions, and enforce a user recall quiz before further project changes after a long completed session.
---

# Trace Code Work

Keep a compact audit trail beside the project so a later agent or developer can recover both the reasoning and the runtime path without rediscovering the codebase.

## Non-negotiable rules

1. Treat `<project-root>/code-logs/YYYY-MM-DD/` as the canonical daily log directory. Use the project's local calendar date.
2. Maintain exactly these core files in each active daily directory: `DECISIONS.md`, `FLOW.md`, `EXPLORE.md`, and `QUIZ.md`.
3. Append or edit the current day's files. Never overwrite earlier dated logs.
4. Record evidence and concise rationale, not hidden chain-of-thought. Explain constraints, alternatives, tradeoffs, and verification in user-auditable terms.
5. Update logs during the work, not only at handoff. Log a fact as soon as it becomes relevant.
6. Do not claim a call path is verified unless it was established from code, tests, runtime traces, or documentation. Label inferred paths.
7. Do not duplicate secrets, tokens, personal data, or large code blocks in logs.

## Start-of-task gate

Perform this sequence before editing source, tests, configuration, schemas, dependencies, generated artifacts, or deployment files.

1. Locate the project root and inspect `code-logs/` read-only.
2. Find the newest completed session before today. Read its four core files.
3. If that session is marked `Length: long`, quiz the user before any project mutation. Read-only exploration is allowed; project and log writes are not.
4. Ask three to five concrete questions drawn from the recorded changes. Cover at least:
   - one rationale or tradeoff;
   - one execution-flow or call-order fact;
   - one changed module, behavior, or test.
5. Wait for the user's answers. Then give concise corrections and ask whether to proceed if their response does not already authorize continuation.
6. After the gate passes, initialize today's logs and record the questions, answers, corrections, source-session date, and gate result in `QUIZ.md`.
7. If no prior completed long session exists, initialize today's logs and record why the quiz was not required.

The gate applies once per coding session. A user may explicitly waive it; record the waiver in `QUIZ.md`. Never invent answers for the user.

## Define a long session

Mark a session `Length: long` when any one condition is met:

- active work reaches 90 minutes;
- at least five material decisions are logged;
- at least ten distinct code/config/test files are inspected or changed;
- at least three modules or services participate in a traced execution path;
- the user explicitly calls the session long.

At handoff, set each log's `Status` to `completed` and its `Length` to `short` or `long`. A session still marked `active` is not a completed session for the next quiz gate.

## Initialize daily logs

Run:

```bash
python3 <skill-dir>/scripts/init_code_logs.py --root <project-root>
```

Pass `--date YYYY-MM-DD` only to reproduce or test a specific date. The script creates missing files from `assets/` and preserves existing content.

If script execution is unavailable, copy the four templates from `assets/` manually and replace `{{DATE}}`.

## Maintain `DECISIONS.md`

Create one decision entry for every material choice, including:

- architecture, algorithm, API, data model, or error-handling approach;
- library or dependency selection, rejection, upgrade, or removal;
- behavior-changing interpretation of an ambiguous requirement;
- important testing, compatibility, performance, or security tradeoff.

Give every entry a stable daily ID such as `D-001`. Include context, considered alternatives, chosen option, concise rationale, consequences, affected paths, and supporting evidence. Do not log trivial syntax choices.

## Maintain `FLOW.md`

Document the actual execution path relevant to the task:

- identify external and internal entry points;
- show call order with qualified symbols such as `module.function()`;
- record important inputs, outputs, state changes, branches, asynchronous boundaries, and external calls;
- mark each node as `unchanged`, `modified`, `added`, or `removed`;
- include before and after paths when the change alters control or data flow;
- cite file paths and line numbers or symbols, refreshing stale line numbers before handoff.

Prefer a compact ordered path plus a caller/callee table. Restrict the map to paths relevant to the current task.

## Maintain `EXPLORE.md`

Log each materially inspected file, module, class, function, schema, or configuration surface. Record why it was inspected, what was learned, whether it is in scope, and whether it must be revisited. Search this file before reopening previously explored areas, but re-check any observation that may be stale after edits.

## Maintain `QUIZ.md`

Record whether the start gate was required, passed, waived, or skipped. When required, preserve the questions, a short summary of the user's answers, corrections, and the prior session date used as the source. Do not store an invented score; use `passed` when the review occurred and the user authorized work to continue.

## Work cycle

For each coding task:

1. Complete the start-of-task gate.
2. Initialize or reuse today's log directory.
3. Explore read-only and update `EXPLORE.md` after each meaningful discovery.
4. Establish the relevant current call path in `FLOW.md` before modifying it.
5. Record a decision before or alongside each material implementation choice.
6. Make the code change and mark the exact changed nodes and paths in `FLOW.md`.
7. Run proportionate verification and attach results to the relevant decision and flow entries.
8. Reconcile logs against the final diff; remove stale claims while retaining superseded decisions with status `superseded`.
9. Complete the session headers and add a concise changed-this-cycle summary to every core log.

## Quality check before handoff

Confirm that:

- every changed path appears in at least one decision or flow entry;
- every modified runtime path has an entry point and ordered caller/callee chain;
- every significant inspected symbol appears in `EXPLORE.md`;
- every new dependency has a selection rationale and rejected alternatives;
- quiz status and session length are explicit;
- the logs describe the final implementation and verification, not an abandoned plan.
