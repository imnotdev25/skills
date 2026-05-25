# Doc Conventions

How to write the four canonical doc artifacts: `FILE_TREE.md`, `DEPENDENCY.md`, changelog entries, and `ARCHITECTURE.md`.

## `Docs/FILE_TREE.md`

See `assets/FILE_TREE.template.md` for the structure. Rules:

- Render the tree as a code block, using `├──`, `└──`, `│` characters.
- After the tree, list every file with a one-line description in a definition list or table.
- Descriptions are present-tense, single-sentence, end with a period.
- Update in the same commit that adds, removes, or moves a file.
- For oversized files, annotate the line count: `⚠️ over ceiling (147 LOC)`.

## `Docs/DEPENDENCY.md`

See `assets/DEPENDENCY.template.md`. Rules:

- Two sections: *Module graph* and *Function graph*.
- Module graph is a Mermaid `flowchart LR` block.
- Function graph is a table per module: function, inputs, outputs, calls-out, called-by.
- Generated automatically where possible (pydeps, madge, depgraph). Hand-curate the descriptions.
- Update when imports change or a public function appears/disappears.

## `changelog/<YYYY-MM-DD>.md`

One file per calendar day. Multiple entries per file are fine, newest at the top.

Template (also at `assets/changelog-entry.template.md`):

```markdown
# <YYYY-MM-DD>

## <HH:MM> · <type>(<scope>): <subject>

**Why:** <the problem this solves; what was considered>

**What changed:**
- <file or module> — <one line>
- <file or module> — <one line>

**Breaks:** <yes/no; if yes, what callers must change>
**Migrations:** <none / link to migration steps>
**Flags:** <feature flag introduced or flipped, if any>
```

`<type>` matches the commit prefix: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `perf`, `ci`, `revert`.

## `Docs/ARCHITECTURE.md`

Sections (in order):

1. **Problem** — what this system exists to solve, in plain language.
2. **Constraints** — non-negotiables (latency, cost, compliance, team size, runtime).
3. **Decisions** — each decision is a short block: *Context → Decision → Consequence*.
4. **Alternatives considered** — what we evaluated and why it lost. Keep the losers documented; they're the cheapest record of "we already thought about that".
5. **Open questions** — explicit list of things still undecided, with owners if known.

Architecture docs are written for the next engineer to land in the repo, not for the author. Assume they know the language but nothing about your specific design.

## `Docs/CONVENTIONS.md`

Pins repo-specific naming, log-field schema, branch model, commit prefixes (copy from `references/principles.md` §23), and any house style that isn't enforceable by linters. One page max.

## `Docs/STACK.md`

Format defined in `references/tech-stack-interview.md` §3. Single source of truth for tech choices.

## `infra/README.md`

Sections:

1. **What's here** — list of infra artifacts (Dockerfile, k8s manifests, terraform, GitHub Actions, secrets-rotation script, etc.).
2. **How to deploy** — concrete commands for the most common targets.
3. **Environments** — table of environments with their URLs/endpoints, owners, secrets locations.
4. **Required env vars** — table: name, purpose, example value (redacted), where it's set.
5. **Link to `infra/Docs/`** — for deeper docs.

Every section in `infra/README.md` corresponds to one file in `infra/Docs/`. Keep that mapping 1:1.
