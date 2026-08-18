# Traceable Coding

`trace-code-work` is a Codex skill for keeping coding work understandable across long sessions. It records why changes were made, how execution travels through the codebase, which areas were explored, and whether the user completed the required session-recall quiz.

## What it maintains

For each active coding day, the skill creates:

```text
code-logs/YYYY-MM-DD/
├── DECISIONS.md  # Approaches, alternatives, libraries, and rationale
├── FLOW.md       # Entrypoints, call order, data flow, and changed paths
├── EXPLORE.md    # Files, modules, and functions already investigated
└── QUIZ.md       # Long-session recall gate and review results
```

Existing daily logs are preserved. The initializer only creates files that are missing.

## Core behavior

- Record material technical decisions and their tradeoffs.
- Explain why a library or implementation approach was selected.
- Trace relevant execution from entrypoint to caller and callee.
- Mark flow nodes as added, modified, removed, or unchanged.
- Track explored code surfaces to avoid unnecessary rediscovery.
- Reconcile documentation with the final diff and verification results.
- Quiz the user before further project changes when the newest completed session is marked long.

Read-only inspection is allowed before the quiz. Source, test, configuration, dependency, deployment, and log mutations wait until the quiz gate passes or the user explicitly waives it.

## Long-session rule

A session is long when any one of these conditions applies:

- 90 minutes of active work;
- five material decisions;
- ten distinct code, configuration, or test files inspected or changed;
- an execution path spanning at least three modules or services;
- the user explicitly marks it long.

The following coding session begins with three to five questions based on that session's decisions, execution flow, and changed behavior.

## Use the skill

Invoke it explicitly:

```text
Use $trace-code-work to implement this change and maintain the daily coding logs.
```

The skill also describes coding-related triggers in its metadata, allowing compatible Codex environments to select it automatically.

## Initialize logs manually

From any directory, run:

```bash
python3 /path/to/trace-code-work/scripts/init_code_logs.py --root /path/to/project
```

To initialize a specific date:

```bash
python3 /path/to/trace-code-work/scripts/init_code_logs.py \
  --root /path/to/project \
  --date 2026-08-18
```

## Skill contents

- `SKILL.md` — authoritative agent workflow and quality rules.
- `agents/openai.yaml` — user-facing Codex metadata.
- `assets/` — templates for the four daily log files.
- `scripts/init_code_logs.py` — non-overwriting daily log initializer.
