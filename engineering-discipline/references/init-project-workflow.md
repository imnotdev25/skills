# `/init-project` Workflow

Bootstrap a new project from zero with the full discipline scaffold.

## Order of operations (do not reorder)

### 1. Interview

Run `references/tech-stack-interview.md` end-to-end. Don't generate a single line of code or docs before this is complete and `Docs/STACK.md` is written.

### 2. Scope ask

After the stack is locked, ask the user in one `ask_user_input_v0` batch:

1. **What is this project?** — free text, one sentence.
2. **Public or private repo?** — affects license file generation.
3. **Versioning scheme?** — `SemVer`, `CalVer`, `none yet`.

Skip questions whose answer is already obvious from chat context.

### 3. Scaffold the tree

Create exactly this structure. Every entry below is mandatory. Use the language-conventional source folder name (e.g. `src/`, `pkg/`, `app/`) but keep the rest identical.

```
<project-root>/
├── README.md                         # one-paragraph what + how to run
├── Docs/
│   ├── FILE_TREE.md                  # see assets/FILE_TREE.template.md
│   ├── DEPENDENCY.md                 # see assets/DEPENDENCY.template.md
│   ├── STACK.md                      # written in step 1
│   ├── ARCHITECTURE.md               # design decisions, WHY not WHAT
│   └── CONVENTIONS.md                # commit prefixes, naming, log fields
├── changelog/
│   └── <YYYY-MM-DD>.md               # today's date, "project initialized"
├── infra/
│   ├── README.md                     # how to deploy, env vars, secrets policy
│   └── Docs/
│       └── DEPLOYMENT.md
├── <src>/
│   └── <one starter module>/
├── tests/
│   └── <mirror of src tree>
├── .gitignore
├── .editorconfig
└── <lockfile + manifest for chosen package manager>
```

For each file generated, the description in `Docs/FILE_TREE.md` must be one line, present-tense, ending in a period. Templates live in `assets/`.

### 4. Configure tooling

Based on stack answers:

- **Linter + formatter config files** at the root (e.g. `ruff.toml`, `.eslintrc.json`, `rustfmt.toml`).
- **Type-checker config** (strict mode on by default — `mypy --strict`, `tsconfig` with `"strict": true`, etc.).
- **Test runner config** with one passing smoke test.
- **CI workflow file** that runs: lint → typecheck → test, in that order, on push and PR.

Keep each config file under 100 LOC.

### 5. Seed the docs

- `README.md`: one paragraph describing the project; a "Run locally" code block; a link to `Docs/`.
- `Docs/ARCHITECTURE.md`: skeleton with these sections — *Problem*, *Constraints*, *Decisions*, *Alternatives considered*, *Open questions*. Fill *Problem* and *Constraints* from the scope ask. Leave the rest as `<TBD>` with a comment block explaining what should go there.
- `Docs/CONVENTIONS.md`: copy the commit-prefix table and logging-field conventions from `references/principles.md`.
- `infra/README.md` + `infra/Docs/DEPLOYMENT.md`: skeleton tied to the chosen deployment target.

### 6. Seed the changelog

Create `changelog/<YYYY-MM-DD>.md` with one entry: `feat(init): scaffold project per engineering-discipline skill`. Use the template at `assets/changelog-entry.template.md`.

### 7. First commit

Stage everything and produce a single conventional commit message. Do not run `git commit` unless the user explicitly asks — just print the suggested message.

```
feat(init): bootstrap project scaffold

- Stack pinned in Docs/STACK.md per interview.
- Docs, infra, tests, and CI scaffolded.
- See changelog/<YYYY-MM-DD>.md for entry.
```

### 8. Hand off

Present the file tree and ask: "Scaffold ready. Want me to start on the first feature, or adjust anything?" Do not start coding features without an explicit go-ahead.

## Anti-patterns specific to init

- Don't generate code for features the user hasn't asked for. The scaffold is the deliverable.
- Don't write a 300-line README. One paragraph + run instructions.
- Don't pick a stack on the user's behalf if they said "Other" — ask.
- Don't skip `infra/` even for "local only" projects. A two-line `infra/README.md` is fine.
