# File Tree

_Generated: <YYYY-MM-DD>. Update on every file add / remove / move._

## Tree

```
<project-root>/
├── README.md
├── Docs/
│   ├── FILE_TREE.md
│   ├── DEPENDENCY.md
│   ├── STACK.md
│   ├── ARCHITECTURE.md
│   └── CONVENTIONS.md
├── changelog/
│   └── <YYYY-MM-DD>.md
├── infra/
│   ├── README.md
│   └── Docs/
│       └── DEPLOYMENT.md
├── <src>/
│   └── <module>/
│       └── <file>.<ext>
├── tests/
│   └── <module>/
│       └── test_<file>.<ext>
├── .gitignore
├── .editorconfig
└── <manifest>
```

## File index

| Path | Description | Notes |
|---|---|---|
| `README.md` | One-paragraph project summary plus run instructions. | |
| `Docs/FILE_TREE.md` | This file. The current shape of the repo. | |
| `Docs/DEPENDENCY.md` | Module-level and function-level dependency graph. | |
| `Docs/STACK.md` | Pinned tech-stack choices. | |
| `Docs/ARCHITECTURE.md` | Design decisions and rejected alternatives. | |
| `Docs/CONVENTIONS.md` | Naming, commits, log schema, branch model. | |
| `changelog/<YYYY-MM-DD>.md` | Dated changelog entries for that day. | |
| `infra/README.md` | Deployment overview, environments, env vars. | |
| `infra/Docs/DEPLOYMENT.md` | How-to deploy in detail. | |
| `<src>/<module>/<file>.<ext>` | <one-line role>. | ⚠️ over ceiling (N LOC) if applicable |
| `tests/<module>/test_<file>.<ext>` | Behavior tests for `<module>/<file>`. | |
| `.gitignore` | Ignored paths for git. | |
| `.editorconfig` | Editor-agnostic whitespace settings. | |
| `<manifest>` | Package manifest (pyproject.toml / package.json / Cargo.toml / go.mod). | |

## Conventions

- Description is one sentence, present tense, ends with a period.
- For directories, describe the directory's purpose; individual files get their own row.
- Mark files exceeding the 100-LOC ceiling: `⚠️ over ceiling (<N> LOC)`.
- Mark orphaned or unused files: `⚠️ candidate for removal`.
