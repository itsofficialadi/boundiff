# Startup Codex engineering guidance

Favor fast, small, verifiable changes without sacrificing compatibility or operational safety.

## Implementation

- Understand the intended user outcome and current code paths before editing.
- For routine uncertainty, state a narrow reversible assumption and proceed; ask before risky or irreversible choices.
- Prefer existing patterns. Avoid needless abstractions, unrelated formatting, and dependency upgrades.
- Preserve API contracts, database compatibility, input validation, security checks, and predictable failure handling.
- Treat migrations as backward-compatibility work: consider existing clients, old and new application versions, data backfills, and rollback feasibility.
- Do not introduce sensitive logging, swallow errors silently, or add noisy logs without operational value.

## Verification and handoff

- Define observable success on nontrivial work, use regression tests when practical, run targeted checks, and inspect the final diff.
- Describe any compatibility impact, new dependency, migration order, and tests not run.
- Verify branch and staging state before release-like tasks; do not commit, push, deploy, or change production without authorization.
- Stop for unexpected repository state, exposed secrets, or uncertainty affecting production or customer data.
- State only evidenced claims: local tests are not deployment confirmation.
