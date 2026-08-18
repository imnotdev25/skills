# Execution Flow — {{DATE}}

- Status: active
- Length: short
- Changed this cycle: None yet.

## Scope

- Task:
- Relevant entry point(s):
- Flow evidence: verified | inferred | mixed

## Before

1. `entrypoint()` — unchanged — `path/to/file:line`
2. `module.function()` — unchanged — called by `entrypoint()`

## After

1. `entrypoint()` — unchanged — `path/to/file:line`
2. `module.function()` — modified — changed behavior and reason

## Caller/callee trace

| Order | Caller | Callee | Condition/data passed | Change | Evidence |
|---:|---|---|---|---|---|

## Side effects and boundaries

- State writes:
- I/O or network calls:
- Async/event boundaries:
- Error paths:

## Verification

- Command/test:
- Observed result:
