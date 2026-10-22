---
name: surgical-change
description: Implement a small feature or bounded bug fix with minimal files and a focused diff. Use for scoped implementation; not for broad redesigns, read-only reviews, or release operations.
---

# Surgical change

## Objective

Deliver the requested behavior with the narrowest correct modification and explicit verification. This workflow implements code; it is not an independent review.

## Steps

1. **Inspect.** Read the entry point, affected implementation, nearby tests, and project-specific instructions. Confirm what is already working.
2. **Bound the task.** State a one-sentence outcome and a small set of observable acceptance criteria. Identify in-scope files and explicit exclusions when useful.
3. **Handle uncertainty.** Choose and disclose a narrow reversible assumption for harmless ambiguity. Stop before a decision affecting security, production, external authority, credentials, data loss, or irreversible state.
4. **Implement.** Follow existing conventions. Prefer direct changes over additional layers, configuration, or dependencies. Keep unrelated code untouched.
5. **Verify.** Run the smallest useful checks first, then nearby checks if practical. For a bug, prefer evidence of prior failure and subsequent success when available.
6. **Inspect.** Review changed paths and full diff for incidental changes, weakened validation, or unexplained formatting. Check worktree state.
7. **Report.** Summarize behavior changed, verification evidence, test gaps, assumptions, and unrelated observations without fixing them opportunistically.

## Boundaries

- Do not stage, commit, push, release, deploy, or mutate external systems unless explicitly authorized.
- Do not update dependencies or regenerate large artifacts just because a tool suggests it; explain necessity before expanding scope.
- Remove only dead code/imports caused by this change unless broader cleanup was requested.
- Do not claim an outcome is verified when checks were skipped, failed, or only simulated.

## Output

A concise handoff with **scope**, **change**, **evidence**, and **limitations**. Cite actual commands/results where available; never invent passing tests.
