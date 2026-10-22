---
name: bug-fix-verification
description: Reproduce a reported bug, establish meaningful regression coverage when feasible, apply a minimal fix, and verify it. Use for debugging and regression work; not for general features or read-only audit.
---

# Bug-fix verification

## Objective

Convert a bug report into a small, demonstrably improved behavior without mistaking green tests for universal correctness.

## Steps

1. **Frame.** Record observed symptom, expected behavior, relevant inputs, and scope. Distinguish user report from directly reproduced evidence.
2. **Inspect.** Locate responsible code, relevant configuration, and nearby tests. Look for alternative explanations before editing.
3. **Reproduce.** Attempt the smallest repeatable reproduction in a safe environment. Capture exact failing command, assertion, or observable result.
4. **Regression.** When practical, add or adapt a test that fails for the reported bug before the fix. Avoid contrived tests that only encode the implementation.
5. **Fix narrowly.** Change the minimum necessary behavior. Preserve public contracts, validation, security checks, and unrelated behavior.
6. **Verify.** Run the reproduction or regression again, then relevant adjacent checks. Record outcomes and whether the pre-fix failure was confirmed.
7. **Inspect the diff.** Check that tests meaningfully cover the defect and that no incidental files or abstractions were introduced.
8. **Report.** State reproduction status, evidence before and after, remaining coverage gaps, and any unreproduced conditions.

## Decision rules

- If reproduction is impossible due to missing data or environment, do not fabricate a failure. Document the blocker, use a reasoned alternative check if available, and qualify the result.
- If a new test is artificial or disproportionately costly, explain why and use the most credible available verification instead.
- For destructive, production, credential, or security-sensitive reproduction, stop or use a disposable/authorized environment.
- Do not silently fix a separate issue discovered while debugging.

## Output

Provide **symptom**, **reproduction**, **fix**, **tests/checks**, and **residual uncertainty**. Distinguish not reproduced, failed before/passed after, and merely passed after.
