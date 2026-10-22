---
name: pull-request-handoff
description: Prepare a concise, evidence-backed pull request description and reviewer handoff from a known diff. Use after implementation; do not create or publish a PR unless explicitly requested.
---

# Pull request handoff

Make review easy. A PR summary should explain *why this diff exists*, not narrate every line.

1. Identify the intended base and exact change range. Check branch, HEAD, staged/unstaged state, and whether uncommitted changes are included. If the base is uncertain, do not invent it.
2. Read the patch, commit intent, tests, and affected contracts. Separate changes shown in the diff from related work that is merely proposed.
3. Write a plain-English summary with user impact, key implementation decisions, compatibility or migration notes, and non-goals.
4. Report tests/checks by exact observed result. Mark skipped, blocked, or not-run checks explicitly. Do not convert "test command documented" into "tests passed".
5. Give reviewers 2 to 4 concrete places to focus: a fragile assumption, API contract, migration boundary, concurrency path, error behavior, or risk-sensitive diff.
6. Draft the PR description; do not stage, commit, push, open a PR, assign people, or publish release notes unless explicitly authorized.

## Output

```md
## Why
...
## What changed
...
## Evidence
- Ran: `<command>` (result)
- Not run: ... (reason)
## Review focus
...
## Rollout / rollback
... (when relevant)
```

If provenance cannot be established, present a draft labeled **unverified diff** instead of a final PR-ready claim.
