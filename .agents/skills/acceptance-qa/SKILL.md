---
name: acceptance-qa
description: Check user-visible behavior against acceptance criteria using an available local app, staging system, API, or CLI. Prefer read-only smoke tests; never mutate production or external data without authorization.
---

# Acceptance QA

Tests can pass while the workflow is broken. Exercise the behavior as a user would, with evidence from the environment actually available.

1. Confirm the build/version, target URL or local process, environment, credentials policy, and acceptance criteria. If the target is unclear, do not guess a production endpoint.
2. Map the shortest **happy path**, one meaningful **failure path**, and a **recovery or retry path** when applicable. Prefer high-signal cases to broad click tours.
3. Select available tools: browser automation, HTTP client, CLI, or a manual checklist. Do not claim a browser test was performed if no browser is available.
4. Use disposable accounts and test data where possible. Navigation and observation are safe defaults; writes, emails, payments, account creation, destructive actions, and production interactions require appropriate authorization.
5. For each case record **action**, **expected outcome**, **observed result**, **environment**, and **evidence** (log, response, screenshot, or exact output when available).
6. Classify failures as reproduced defects, environment blockers, or unverified assumptions. Do not silently repair during QA; hand off reproducible findings to `$bug-fix-verification`.

## Output

A short pass/fail/not-run matrix, build identity, environment, findings with reproduction steps, and untested paths. A local pass is not production validation.
