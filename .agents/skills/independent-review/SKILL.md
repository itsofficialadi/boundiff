---
name: independent-review
description: Perform an independent, read-only review of a commit, branch, pull request, or code path and report reproducible findings. Use for review/audit requests; never silently remediate the target.
---

# Independent review

**Core invariant: review is not remediation.** Treat the review target as evidence that must not be modified by the reviewer.

## Establish the target

1. Confirm the repository and exact target (branch/commit/PR, base reference, or files). Record relevant HEAD, working-tree and staged state, and whether the review includes a dirty overlay.
2. Explicitly distinguish committed source, uncommitted changes, generated files, disposable test mutations, third-party evidence, and assumptions.
3. If the target cannot be identified reliably or unexpected state makes findings ambiguous, stop and report the provenance problem.

## Inspect and test

4. Review requested behavior, changed paths, callers, tests, error handling, trust boundaries, and potential regressions in proportion to risk.
5. Reproduce suspicious behavior with narrow, deterministic checks. For tests that may write caches, snapshots, build outputs, files, database state, or Git metadata, use a disposable copy or isolated environment. Do not change the reviewed working tree, index, refs, history, or project configuration.
6. Run negative or mutation testing only on disposable copies with an explicitly bounded target; never run destructive tests against live or production resources.
7. Classify findings by severity and likelihood. Support each with affected location, trigger, impact, and evidence. Separate confirmed defects from hypotheses.

## Prohibited during review

- No source edits, auto-fixes, dependency updates, lockfile changes, staging, commits, branch switches, rebases, pushes, or silent remediation.
- No opportunistic edits even when the fix appears trivial.
- Do not treat successful tests as proof that all defects or vulnerabilities are absent.

If a defect warrants remediation, report it and request a **new, explicitly authorized remediation task**. A later task may use `$surgical-change` or `$bug-fix-verification`; it does not retroactively change this review into a write-capable operation.

## Output

- **Target and provenance:** exact object/range and overlay state, if known.
- **Findings:** severity, location, reproduction/impact, and confidence, ordered by significance.
- **Verification:** checks performed, isolation method, and results.
- **Limitations:** unchecked areas, missing environment, and hypotheses.
- **Review state:** explicit confirmation that the reviewed target was left unchanged, or a disclosure if this could not be established.
