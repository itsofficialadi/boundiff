---
name: release-checkpoint
description: Inspect or create a high-integrity Git commit/release checkpoint with exact repository provenance and staged-diff verification. Use for checkpoint, commit, push-readiness, or release preparation; writes require explicit authorization.
---

# Release checkpoint

## Modes and authority

Default to **inspection mode**: collect evidence and report readiness without modifying repository state. Enter **write mode** only when the user explicitly authorizes the particular commit, tag, push, or release action and its scope. A request to inspect readiness does not authorize publishing.

## Before any write

1. **Establish identity.** Confirm repository root and remote(s), current branch, `HEAD`, parent relationship where relevant, expected base, and target environment. Do not guess the intended repository or branch.
2. **Record all state.** Inspect staged changes, unstaged tracked changes, unexpected untracked files, conflicts, and ignored outputs where relevant. Use commands such as `git status --porcelain=v1 -uall`, `git diff --name-status`, `git diff --cached --name-status`, and `git diff --cached --check`.
3. **Resolve provenance.** Compare against the expected branch/commit/remote if that evidence is available. Remote-tracking refs can be stale; fetching changes local refs and should not be done silently where the task is strictly read-only. Mark remote state *unverified* if it was not checked.
4. **Enforce scope.** Enumerate exact intended files and examine the entire staged patch. Stop if the stage includes unexpected paths, the worktree contains unreconciled changes relevant to the operation, or the target differs from expectations.
5. **Verify.** Run appropriate tests, lint, build or artifact validation. Record command, observed result, skipped checks, and any output/hash used as a release input.

## Authorized local checkpoint

6. If explicitly asked to stage files, stage only an enumerated allowlist of paths. Never use `git add .` or `git add -A` by default. Recheck `git diff --cached --name-status` and `git diff --cached` afterward.
7. If a commit was explicitly authorized, create it only after checking the staged diff and verification status. Record the resulting commit SHA and parent SHA. Stop if a hook or tool altered the staged content unexpectedly; re-inspect rather than bypass checks.
8. Confirm `HEAD`, staged/unstaged/untracked state, and any expected artifact hash after the operation. Do not claim a clean worktree unless it is observed.

## Push, release, and deployment boundaries

- Push, tag, publish, deploy, rollback, force-push, history rewrite, and destructive cleanup each require explicit authority and a known target. No force push by default.
- Before an authorized push, establish the expected remote destination and relationship to its current tip. Stop if divergent or uncertain; do not silently reconcile by rebasing or resetting.
- A successful local commit is not a confirmed push. A successful push is not a deployed release. A successful deploy command is not proof that production is healthy.
- If high-risk integrity checks fail, report the mismatch. Never disable the checks just to pass.

## Output

Provide a compact checkpoint ledger: **repo/branch/HEAD (before)**, **staged file list**, **verification evidence**, **actions performed or withheld**, **commit and parent (if created)**, **remote/deployment state (confirmed or unknown)**, **repo/HEAD/worktree (after)**, and **unresolved risks**.
