# Agent Skills

A collection of reusable skills that give coding and research agents focused workflows, persistent project context, and repeatable operating rules.

## Skills

| Directory | Skill | Purpose |
|---|---|---|
| [`trace-code-work/`](trace-code-work/) | Traceable Coding | Maintains dated decision, execution-flow, exploration, and recall-quiz logs during coding work. |
| [`engineering-discipline/`](engineering-discipline/) | Engineering Discipline | Applies docs-first development, modularity, strict typing, testing, dependency mapping, and dated changelogs. |
| [`file-management/`](file-management/) | Workspace Hygiene | Enforces consistent workspace layout, dated filenames, script placement, and recoverable archiving. |
| [`human-ai-research/`](human-ai-research/) | Research Pipeline | Guides a human-led research process from ideation and literature review through validation and reporting. |
| [`paper-reading/`](paper-reading/) | Keshav Three-Pass Reading | Applies S. Keshav's three-pass method to structured academic-paper reading and analysis. |

## Traceable coding workflow

The [`trace-code-work`](trace-code-work/README.md) skill creates a daily audit trail inside the project being changed:

```text
code-logs/YYYY-MM-DD/
├── DECISIONS.md
├── FLOW.md
├── EXPLORE.md
└── QUIZ.md
```

It records why approaches and libraries were selected, how execution moves between modules and functions, what the agent has already explored, and which parts of the path changed. After a completed long session, the next coding session begins with a user recall quiz before project mutations continue.

## Repository structure

Each modern skill generally follows this layout:

```text
skill-name/
├── SKILL.md            # Trigger metadata and agent instructions
├── agents/
│   └── openai.yaml     # Codex interface metadata
├── scripts/            # Optional deterministic utilities
├── references/         # Optional detailed guidance
└── assets/             # Optional templates and reusable artifacts
```

`SKILL.md` is the authoritative entrypoint. Optional resources should exist only when they directly support the workflow.

## Use a skill

In a compatible Codex environment, invoke a skill by name:

```text
Use $trace-code-work to implement this feature with dated traceability logs.
```

Skills may also activate automatically when their `SKILL.md` description matches the task.

## Install locally

Copy or link the required skill directory into your Codex skills directory:

```bash
cp -R trace-code-work "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Restart or refresh the Codex environment if it does not detect the newly installed skill immediately.

## Create or update a skill

When adding a skill:

1. Use a lowercase, hyphenated directory name.
2. Add a concise `SKILL.md` with accurate trigger conditions.
3. Keep instructions imperative and focused on non-obvious workflow requirements.
4. Put reusable automation in `scripts/` and output templates in `assets/`.
5. Add `agents/openai.yaml` for user-facing metadata when supported.
6. Validate the skill with the official skill validator before handoff.
7. Update the skill table in this README.
