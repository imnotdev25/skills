# `/existing-project` Workflow

Onboard a current repo. The deliverable is a complete picture of what's there + a path forward under the discipline rules.

## Order of operations

### 1. Read the file tree first

Before asking anything, walk the repo:

```bash
# Use whichever tools are available in the environment
find . -type f -not -path '*/\.*' -not -path '*/node_modules/*' -not -path '*/__pycache__/*' -not -path '*/target/*' -not -path '*/dist/*' -not -path '*/build/*' | sort
```

Capture: every source file, every config file, every doc. Note file sizes and language.

### 2. Tech-stack interview — but pre-filled

Run `references/tech-stack-interview.md`, but for each question, **propose the answer** inferred from the tree (e.g. `pyproject.toml` → Python + uv/poetry; `package.json` with `"type": "module"` and a `pnpm-lock.yaml` → TS + pnpm). Present each inferred answer as the default-selected option in `ask_user_input_v0`. The user confirms or corrects.

Write the confirmed result to `Docs/STACK.md`. If `Docs/STACK.md` already exists, diff against it and surface conflicts.

### 3. Generate `Docs/FILE_TREE.md`

Use `assets/FILE_TREE.template.md`. For every file in the tree:

- One-line, present-tense description of its role.
- Read the file to write the description — don't guess from filename alone.
- Mark files over 100 LOC with `⚠️ over ceiling (N LOC)`.
- Mark files with no clear purpose (dead code, orphaned) with `⚠️ candidate for removal`.

If the repo is large (>200 files), batch the reads and ask the user whether to do a full pass or stop at the top three directory levels.

### 4. Generate `Docs/DEPENDENCY.md`

Use `assets/DEPENDENCY.template.md`. Two layers:

**Module-level graph:** for each module/file, list which other modules it imports and which import it. Use a Mermaid `flowchart` block.

**Function-level graph:** for each public function in each module, list:
- Inputs (with types if discoverable)
- Outputs (with types)
- Functions it calls
- Functions that call it

If function-level coverage of the whole repo is too large, scope it to the modules the user names. Ask which.

### 5. Audit pass

Generate `Docs/AUDIT-<YYYY-MM-DD>.md` with these sections, each a bullet list:

- **Files over 100 LOC** — path + line count.
- **Functions without typed signatures** — path + function name.
- **Silent error handling** — `except: pass`, `try { ... } catch {}`, ignored Go errors, `.unwrap()` chains in Rust.
- **Mutable globals / shared state.**
- **Missing `infra/`** — list what would go there if it existed.
- **Missing or stale `changelog/`.**
- **Missing tests** — modules with no matching test file.
- **TODO / FIXME / HACK comments** — path + line + text.
- **Cognitive-complexity hot spots** — functions with deeply nested control flow.

Each finding gets a severity tag: `[blocker]`, `[major]`, `[minor]`.

### 6. Plan, don't refactor yet

Write `Docs/REMEDIATION.md` with proposed changes grouped by theme (e.g. "split oversized files", "add types to module X", "introduce infra/", "wire up CI"). Order by `[blocker]` → `[major]` → `[minor]`.

Each item:
- What changes
- Why (link the principle from `references/principles.md`)
- Estimated blast radius (which files / tests are affected)
- A suggested feature-flag or branch name

### 7. Seed missing scaffolding

If any of these are missing, create them now:
- `Docs/` directory + the canonical files (`FILE_TREE.md`, `DEPENDENCY.md`, `STACK.md`, `ARCHITECTURE.md`, `CONVENTIONS.md`).
- `changelog/` directory + today's dated file with entry: `docs(onboard): generate file tree, dependency map, audit per engineering-discipline skill`.
- `infra/` directory + `README.md` + `Docs/DEPLOYMENT.md` skeletons (only if deployment artifacts exist in the repo today — Dockerfile, k8s manifests, terraform, etc.; move them in).

Do **not** rewrite source code in this pass. Only docs and structural moves.

### 8. Hand off

Present:
- `Docs/STACK.md`
- `Docs/FILE_TREE.md`
- `Docs/DEPENDENCY.md`
- `Docs/AUDIT-<date>.md`
- `Docs/REMEDIATION.md`

Ask: "Audit + remediation plan ready. Pick the first item to tackle, or want me to walk you through any section?"

## Anti-patterns specific to existing-project

- Don't start fixing code mid-audit. The audit is the deliverable.
- Don't auto-delete anything — `⚠️ candidate for removal` is a flag, not a command.
- Don't infer the stack silently — surface every inferred answer for confirmation.
- Don't generate function-level dependency for an entire monorepo without scoping. Ask.
