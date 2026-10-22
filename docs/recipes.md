# Practical recipes

These prompts are deliberately short. You can use natural language instead of quoting the skill names, but explicit names help when you want a particular mode.

## 1. The failing CI job

```text
Use $root-cause-investigation on the flaky integration test in CI.
Compare the local and CI runtime, fixture ordering, and shared state.
Don't change any source files. Tell me what you can reproduce.
```

**Good handoff:** one plausible cause supported by a trace or experiment, the alternatives considered, and the next safe reproduction step. Not “probably a race condition” without evidence.

## 2. An endpoint returning duplicate results

```text
Use $bug-fix-verification. The cursor endpoint duplicates an item
when two records have the same created_at timestamp. Reproduce it,
add a regression if practical, implement the narrowest fix, and show
what was tested. Do not change unrelated pagination endpoints.
```

**Good handoff:** a before-fix duplicate case and after-fix behavior, including whether nearby pagination tests passed. A test written only after the fix may be useful, but it is not evidence that it failed beforehand.

## 3. A risky permissions change

```text
Use $security-review to inspect the change to organization membership
checks. Trace whether a user can access another organization's data.
Review only. Do not modify the current tree or run against production.
```

**Good handoff:** relevant access path, actor preconditions, object-level authorization invariant, actual evidence, and a limited conclusion. Remediation should be requested separately.

## 4. A database column rename

```text
Use $migration-safety to propose a rollout for renaming account_id
in the event table. Two app versions may run during deployment.
Plan only. Include compatibility, backfill, validation, and stops
before any destructive or production operation.
```

**Good handoff:** expand/contract steps if appropriate, both-version compatibility, how to validate data, and which operations would be irreversible.

## 5. Testing the shipped flow

```text
Use $acceptance-qa on the locally running CLI import flow.
Test one valid CSV, one invalid row, and repeated import behavior.
Record exact command output. Don't send data to external endpoints.
```

**Good handoff:** pass/fail/not-run results tied to a specific build and inputs. No fictional screenshots if there is no browser.

## 6. Handing off a change for review

```text
Use $pull-request-handoff to draft the PR description from the
current diff against main. Show exact tests you observed, the
migration risk, and two concrete review hotspots. Don't push or
open the PR.
```

**Good handoff:** the real changed behavior, not a commit-by-commit narrative. Don't call a dirty diff committed or a commit deployed.

## When not to use a skill

If you ask Codex to fix a typo, change a label, or update an obvious constant, the root `AGENTS.md` is probably enough. Choosing no workflow is part of using this pack well.
