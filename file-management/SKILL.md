---
name: workspace-hygiene
description: Enforce strict file management discipline for autonomous agent workflows. Use this skill ALWAYS when creating, naming, moving, or retiring files during any task — coding, data processing, scripting, document generation, scratch work, anything. Triggers on any request that produces files or scripts: "build/create/generate/write a script", "save this", "make a file", "run an analysis", "set up a project", "clean up", "archive these", "I don't need X anymore". Enforces: single workspace root (never /tmp or scattered paths), `BaseName_DD_MM_YYYY.ext` naming, all scripts under `scripts/`, all retired files moved into `archive/` (never deleted). Consult this skill at the start of any task that touches the filesystem.
---

# Workspace Hygiene

Rules for where files go, how they're named, and what happens when they're no longer needed. Apply on every filesystem-touching task without being asked.

## The 5 Rules

1. **One root per task.** Pick a single workspace directory (the current working directory, or a named project folder under it). Create everything for the task inside that root. Never write to `/tmp`, `~`, `/var`, or scattered absolute paths. If no root is obvious, ask the user once, then commit to it.
2. **Scripts live in `scripts/`.** Every executable file (`.py`, `.sh`, `.js`, `.ts`, `.zig`, `.applescript`, etc.) goes under `<root>/scripts/`. Never at the root, never beside outputs.
3. **Date-suffix every file.** Format: `BaseName_DD_MM_YYYY.ext`. `BaseName` is snake_case, meaningful (describes content, not type). Today is `26_05_2026`. Example: `compensation_eval_runner_26_05_2026.py`, not `script.py` or `run.py`.
4. **Retire to `archive/`, never delete.** When a file is superseded, unused, or replaced, move it to `<root>/archive/` (preserving the dated name). `rm` is forbidden on user/task files. Only auto-generated caches (`__pycache__`, `node_modules`, `.venv`) may be deleted.
5. **Outputs are dated too.** Result files (`.csv`, `.json`, `.jsonl`, `.png`, `.md`, `.parquet`) follow the same `BaseName_DD_MM_YYYY.ext` rule so runs are distinguishable across days.

## Canonical Layout

```
<workspace_root>/
├── scripts/                          # all executable code
│   ├── retry_runner_26_05_2026.py
│   └── oai_batch_26_05_2026.py
├── data/                             # inputs (read-only by convention)
│   └── prompts_26_05_2026.jsonl
├── outputs/                          # generated artifacts
│   └── eval_results_26_05_2026.jsonl
├── archive/                          # retired files, never deleted
│   ├── scripts/
│   │   └── retry_runner_24_05_2026.py
│   └── outputs/
│       └── eval_results_24_05_2026.jsonl
└── notes_26_05_2026.md
```

`data/`, `outputs/`, and intermediate folders are optional — create them only when the task has clear input/output separation. `scripts/` and `archive/` are mandatory the moment they're needed.

## Decision Flow

Before any file operation, run this check:

```
Creating a file?
  ├─ Is it a script?            → <root>/scripts/<base>_DD_MM_YYYY.<ext>
  ├─ Is it data/output?         → <root>/[data|outputs]/<base>_DD_MM_YYYY.<ext>
  └─ Else                       → <root>/<base>_DD_MM_YYYY.<ext>

Removing a file?
  ├─ User/task file             → mv to <root>/archive/<same_subpath>/  (NEVER rm)
  └─ Build cache/dep folder     → rm -rf is fine

Replacing a file with a new version?
  └─ Move old to archive/ first, then write the new dated file
```

## Naming — Good vs Bad

| Bad                  | Good                                       |
|----------------------|--------------------------------------------|
| `script.py`          | `salary_bias_analysis_26_05_2026.py`       |
| `run.sh`             | `modal_deploy_26_05_2026.sh`               |
| `test.py`            | `retry_smoke_test_26_05_2026.py`           |
| `output.json`        | `compensation_eval_results_26_05_2026.json`|
| `final_v2_NEW.py`    | `cortex_router_26_05_2026.py`              |
| `tmp.csv`            | `unpivoted_patient_scenarios_26_05_2026.csv`|

Rules: snake_case, no spaces, no version suffixes (`_v2`, `_final`, `_NEW`) — the date *is* the version. No generic words alone (`script`, `test`, `output`, `data`, `file`, `tmp`).

## Helper Script

`scripts/wsh.py` (workspace hygiene) — a small CLI that does the right thing automatically. Use it instead of raw `mv`/`touch` when convenient:

- `python scripts/wsh.py new <base> <ext> [--kind script|data|output|root]` → creates a properly-dated empty file in the right folder and prints its path.
- `python scripts/wsh.py archive <path>` → moves a file into `archive/` mirroring its subpath.
- `python scripts/wsh.py rename <path> <new_base>` → renames keeping the date suffix and folder.
- `python scripts/wsh.py audit` → lists all files violating the rules (missing date suffix, scripts outside `scripts/`, untracked files at root).

See `scripts/wsh.py` for the implementation. Copy it into any new workspace root on first use.

## When the User Says "Delete"

Treat "delete", "remove", "get rid of", "drop", "clean up" as "archive". Move the file(s) under `<root>/archive/` preserving subpath, then tell the user where it went. Only ask for confirmation to actually `rm` if the user pushes back ("no I mean really delete it") AND the file is genuinely disposable.

## When No Workspace Root Exists

If you're starting fresh and there's no obvious root (e.g. `cwd` is `/` or `$HOME`), create one:
- Pick a snake_case name from the task (`compensation_eval/`, `radxa_debug/`, `homeassistant_dashboard/`).
- `mkdir -p <name>/{scripts,archive}` and `cd` into it.
- Everything else flows from there.

## Self-Check Before Finishing a Task

At the end of any task that produced files, scan for violations:
- Any script outside `scripts/`? → move it.
- Any file without `_DD_MM_YYYY` suffix? → rename it.
- Any superseded file still sitting next to its replacement? → archive it.
- Any file written to `/tmp` or outside the root? → move it in.

`python scripts/wsh.py audit` does this automatically. Run it before reporting "done".
