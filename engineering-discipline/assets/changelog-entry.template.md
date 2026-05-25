# <YYYY-MM-DD>

<!--
One file per calendar day. Multiple entries inside the file are fine.
Newest entry goes at the top of the file (after this comment).

Entry format below — copy the block, fill it in, drop unused lines.
-->

## <HH:MM> · <type>(<scope>): <subject>

**Why:** <the problem being solved; what alternatives were considered and rejected>

**What changed:**
- `<path/to/file>` — <one-line description>
- `<path/to/file>` — <one-line description>

**Breaks:** <no / yes — describe what callers must change>
**Migrations:** <none / link to migration steps>
**Flags:** <feature flag introduced or flipped, or "none">

---

<!--
Allowed <type> values (match commit prefixes):
  feat      — new user-visible behavior
  fix       — bug fix
  refactor  — internal change, no behavior delta
  docs      — docs-only change
  test      — test-only change
  chore     — tooling, dependencies, formatting
  perf      — measurable performance change
  ci        — CI / build pipeline change
  revert    — reverts a prior change

<scope> is the module or area: e.g. (auth), (api), (infra), (changelog), (init).

The subject is imperative, ≤ 72 chars, no trailing period.
Examples:
  feat(auth): add JWT refresh endpoint
  fix(api): handle empty query string in /search
  refactor(domain): split User into User + UserCredentials
  docs(architecture): record decision to use Postgres over Mongo
-->
