---
name: engineering-discipline
description: Enforces a strict engineering-discipline workflow for any coding project — docs-first, modular code (100-LOC file ceiling), strict types, fail-loud errors, semantic logging, behavior-tests, dependency tracking, dated changelogs, and infra separation. Use this skill whenever the user types `/init-project` (bootstrap a new project) or `/existing-project` (onboard / audit a current repo), and also whenever the user asks to start a new codebase, scaffold a repo, set engineering standards, audit project structure, build a dependency map, write a FILE_TREE.md or DEPENDENCY.md, or work on a project under these rules. Trigger even when the slash commands aren't used verbatim — phrases like "start a new project", "set up a repo properly", "make this codebase clean", or "I want to add a feature to my project" should pull this skill in. The skill always interviews the user before producing code or docs; never assume tech stack, never skip the docs-before-code step.
---

# Engineering Discipline

A workflow skill that enforces docs-first, modular, type-strict engineering on every project the user touches.

The skill exposes two entry commands:

- **`/init-project`** — bootstrap a brand-new project with the full discipline scaffold (docs, infra, changelog, file-tree, dependency graph).
- **`/existing-project`** — onboard a current repo: read the file tree, build a dependency map, then start applying the discipline going forward.

If the user invokes either command, route immediately to the matching workflow file. If the user describes a project task without using a slash command but the intent matches (e.g. "let's start a Python service", "I want to add auth to my app, follow my rules"), confirm with one line which mode they want and proceed.

## Hard rules (apply in every turn after the skill triggers)

These are non-negotiable. Read `references/principles.md` for the full reasoning behind each one.

1. **Check docs before implementing.** Read `Docs/` first. If `Docs/` doesn't exist yet, that's the first thing to create.
2. **Update docs before adding features.** Doc edit lands in the same change as the code, never after.
3. **Append to `changelog/<YYYY-MM-DD>.md`** for every change. Format in `references/doc-conventions.md`.
4. **Never assume — ask.** Tech stack, scope, naming, deployment target. Ask via `ask_user_input_v0` when options are available.
5. **No file exceeds 100 LOC.** Split before you hit the ceiling. Function-per-concern, file-per-cohesive-unit.
6. **Every function has typed input/output and a docstring.** Strict casts. Document edge cases.
7. **Fail loud.** No silent excepts, no swallowed errors, no `if err != nil { /* ignore */ }`.
8. **Make impossible states impossible.** Use sum types / enums / discriminated unions instead of flag soup.
9. **Immutable by default.** Mutation only where measurably necessary.
10. **Logging is semantic and designed first.** Decide log events + fields before writing the logic that emits them.
11. **Tests cover behavior, not implementation.** Refactor must not break passing tests.
12. **Feature flags > branching logic** for anything that might toggle.
13. **Commits are meaningful**, prefixed: `feat:`, `fix:`, `refactor:`, `docs:`, `test:`, `chore:`, `perf:`, `ci:`, `revert:`. Commit message documents **why**, not what.
14. **Infra lives in `infra/`** with its own `README.md` and `Docs/` mapped 1:1 to that README.
15. **`Docs/FILE_TREE.md` and `Docs/DEPENDENCY.md` exist and are kept current.** See `assets/` for templates.
16. **Open for extension, closed for modification.** New behavior via new modules or strategies, not by editing stable interfaces.
17. **Aim for linear time and space.** Reach for the right data structure before reaching for a loop.
18. **Optimize for change**, not for today's requirements.

## Routing

| User input | Read next |
|---|---|
| `/init-project` or "start a new project" | `references/init-project-workflow.md` |
| `/existing-project` or "onboard this repo" | `references/existing-project-workflow.md` |
| Mid-project work (adding feature, fixing bug) | `references/principles.md` — apply rules above; also enforce changelog + doc updates in the same turn |
| User asks about the discipline itself | `references/principles.md` |
| Need to generate `FILE_TREE.md`, `DEPENDENCY.md`, or a changelog entry | `references/doc-conventions.md` + matching template in `assets/` |

## Style of interaction

The user prefers terse, directive communication and expects autonomous execution once intent is clear. Ask questions when something is genuinely ambiguous — and prefer `ask_user_input_v0` with concrete options over prose questions. Don't ask back-to-back rounds when one tightly-scoped batch will do. When you do execute, generate code, not summaries.
