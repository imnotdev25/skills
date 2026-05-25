# Principles

The full ruleset. Each rule has a one-line statement and a short reasoning paragraph. Apply all of them in every turn after the skill triggers.

---

## Docs & process

### 1. Docs before code

Read `Docs/` before implementing. If a feature isn't in the docs, the docs change first — same turn, same review. **Why:** docs that lag the code are worse than no docs; they actively mislead.

### 2. Update docs before adding features

The doc edit lands with the code, not after it. If you find yourself thinking "I'll document it later", stop and document now. **Why:** "later" is when reviewers can't catch design errors cheaply.

### 3. Dated changelog

Every change appends an entry to `changelog/<YYYY-MM-DD>.md`. One file per calendar day; multiple entries inside the file are fine. Format in `references/doc-conventions.md`. **Why:** dated changelogs are robust to merges and let you reconstruct what shipped without git archaeology.

### 4. Docs reflect design decisions

`Docs/ARCHITECTURE.md` records *why* and *what was rejected*, not just what exists. **Why:** decisions are valuable; the artifact alone doesn't capture them.

### 5. Never assume — ask

Tech stack, scope, naming, integration points, deployment target. Use `ask_user_input_v0` when discrete options exist. Asking pulls the user into the design and surfaces hidden constraints. **Why:** assumed-into-code mistakes cost 10× to remove.

---

## Code shape

### 6. 100-LOC file ceiling

No source file exceeds 100 lines. Split before the ceiling, not at it. Test files and generated files are exempt; configs should also try to stay under. **Why:** the ceiling forces decomposition into named units, which forces naming, which forces clarity.

### 7. Break down functions

Function-per-concern. If a function does X *and* Y, it's two functions. **Why:** small functions are testable in isolation and review fast.

### 8. Clean architecture, OOP/composition patterns where they fit

Layers: domain → use cases → adapters → infrastructure. Dependencies point inward. Use composition over inheritance; classes when state has identity, modules of functions otherwise. **Why:** lets you change the database or the framework without rewriting the business logic.

### 9. Structured repo

No stray files in the root or inside `<src>/`. Everything in a labeled folder. **Why:** root noise hides intent.

### 10. `infra/` is separate

All deployment, IaC, Docker, k8s, terraform, CI helpers live in `infra/`. It has its own `README.md` and its own `Docs/` mapped 1:1 to that README. **Why:** infra changes have different review needs and different blast radius than app code.

---

## Functions

### 11. Typed input and output

Every function declares its parameter types and return type. Strict mode on (`mypy --strict`, `tsconfig.strict: true`, etc.). **Why:** types are the cheapest spec you'll ever write.

### 12. Docstrings document the function

Each function has a docstring covering: purpose, params, return, raises, edge cases. **Why:** the docstring is where future-you finds the answer to "what does this do".

### 13. Aggressive casting at boundaries

Validate and cast at every system boundary (HTTP input, file read, DB row, external API response). Inside the system, types are guaranteed. **Why:** trust no input; trust everything you've validated.

### 14. Think about edge cases

Empty input, single-item input, huge input, unicode, timezones, null/None, negative, zero, off-by-one. Write the edge-case list in the docstring before writing the body. **Why:** edge cases listed are edge cases handled.

### 15. Right data structure first

Linear time and linear space are the goal. Reach for the right structure (set, dict, deque, trie) before reaching for nested loops. **Why:** algorithmic cost compounds; structural choice is essentially free.

---

## Error handling & state

### 16. Fail loud

No silent `except`, no swallowed errors, no ignored return values. If you catch, you log + re-raise or you convert to a domain error and propagate. **Why:** silent failures cause the worst on-call nights.

### 17. Make impossible states impossible

Use sum types / enums / discriminated unions / smart constructors. A `User` should not be able to hold `email=None` and `email_verified=True` simultaneously. **Why:** if the type system says it can't happen, you don't write code to handle it.

### 18. Immutable by default

Default to `const`/`readonly`/frozen dataclasses/`@dataclass(frozen=True)`/owned values. Reach for mutation only when measured. **Why:** immutable state is easier to reason about and parallelize.

---

## Observability & testing

### 19. Semantic logging, designed first

Before writing the logic, list the events you'll log and the fields you'll attach. Logs are structured (JSON), event-named, and include a correlation ID. No `print`, no `console.log`, no `log.info("here")`. **Why:** logs designed after the fact become noise; logs designed first become a usable narrative.

### 20. Tests around behavior

Tests assert observable behavior, not internal calls. Refactors must not break passing tests. Aim for: one test per behavior, not one test per function. **Why:** implementation tests rot on the first refactor; behavior tests survive.

### 21. Feature flags > branching logic

For anything toggleable, conditional, experimental, or rollout-gated, use a feature flag (a config key, env var, or a flag service). No `if user.is_in_beta:` sprinkled across the code. **Why:** flags concentrate the conditional in one place and make rollback a config change.

---

## Reviewability & change

### 22. Review-friendly code

Each PR/commit does one thing. Diffs are small. Variable names are full words. No clever one-liners. **Why:** review quality drops sharply with diff size.

### 23. Meaningful conventional commits

Prefix with: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `perf`, `ci`, `revert`. Optional scope. Subject ≤ 72 chars, imperative. Body explains **why**, not what (the diff shows what). **Why:** the prefix turns `git log` into a release-note generator and makes bisecting honest.

### 24. Code versioning

Semantic versions (or calendar versions) tagged in git. Breaking changes bump major. Deprecations land before removals. **Why:** consumers need to know whether to read the changelog.

### 25. Optimize for change

Today's requirements are the worst possible thing to optimize for — they're a snapshot. Optimize for the next likely change. **Why:** software's only constant is more requirements.

### 26. Open for extension, closed for modification

New behavior arrives by adding code (new strategy, new adapter, new module), not by editing stable interfaces. **Why:** stable code earns trust; trusted code shouldn't be edited carelessly.

### 27. Reduce cognitive complexity

Nesting depth ≤ 3. Cyclomatic complexity ≤ 10 per function. Prefer early returns. **Why:** the reader's brain is your most expensive resource.

### 28. Commit messages document WHY

The diff already shows what changed. The message should tell future-you what problem you were solving and what you considered. **Why:** six months later, only the why is recoverable.

---

## Dependency tracking

### 29. `Docs/FILE_TREE.md` exists and is current

Every file in the repo has a one-line entry. Updated in the same commit that adds/removes files. Template: `assets/FILE_TREE.template.md`.

### 30. `Docs/DEPENDENCY.md` exists and is current

Module-level and function-level dependency graph. Updated when imports change or a public function is added/removed. Template: `assets/DEPENDENCY.template.md`.

---

## Quick checklist before claiming a change is done

- [ ] Docs updated (architecture, file tree, dependency, conventions if affected)
- [ ] `changelog/<YYYY-MM-DD>.md` has an entry
- [ ] No file > 100 LOC
- [ ] All new functions typed + docstring'd with edge cases
- [ ] No silent error handling introduced
- [ ] Tests added for new behavior
- [ ] Commit message is conventional + explains why
- [ ] No new branching logic that should have been a feature flag
