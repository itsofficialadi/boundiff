---
name: test-gap-audit
description: Review existing test coverage for important behavior, missing assertions, and false confidence without changing code. Use to assess a test suite; not to implement new tests.
---

# Test-gap audit

Coverage percentages are a map, not the destination. This is a **read-only audit**.

1. Identify the behavior and regression surface. Read tests alongside the production paths they claim to exercise.
2. Trace meaningful boundaries: validation, authorization, failure handling, persistence, concurrency, and public contracts where relevant.
3. Inspect assertions, test doubles, fixtures, and setup. Ask whether the test fails for the relevant defect or merely proves the mock was configured.
4. Look for gaps: a successful path without failure checks, missing negative cases, brittle snapshots, shared test pollution, unverifiable external assumptions, and tests that cannot detect regressions.
5. If running tests might write snapshots, fixtures, caches, or project files, use a disposable copy. Do not run auto-fix or coverage instrumentation that mutates the reviewed target.
6. Rank a short list by **impact × likelihood × detectability**. Suggest the narrowest high-value addition without implementing it.

## Output

| Gap | Why existing tests miss it | Suggested assertion or scenario | Priority |
| --- | --- | --- | --- |

Include target/version, checks actually run, and limitations. Do not infer all behaviors are covered because a test run is green.
