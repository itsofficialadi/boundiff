---
name: implementation-plan
description: Produce an executable, repository-grounded implementation plan with bounded steps and verification gates. Use for multi-file features or risky changes before coding; not for trivial edits.
---

# Implementation plan

A plan should lower implementation risk, not become a second specification. **Plan-only mode:** do not edit code, stage, or commit.

1. Read task scope, relevant `AGENTS.md` files, entry points, tests, and existing architecture. Verify referenced files actually exist.
2. Write the target outcome and 2 to 5 checkable acceptance criteria. Mark missing facts, defaults, and decisions requiring authority.
3. Choose the smallest viable change path. Mention alternatives only where a tradeoff affects correctness, operational risk, or future compatibility.
4. Divide work into bounded steps. For each step: likely paths, change intent, verification command or manual check, and an observable completion signal. Do not invent commands; label suggested commands not yet verified.
5. Include contracts and failure paths: API consumers, validation, concurrency, data persistence, backwards compatibility, and rollback if relevant.
6. Identify the first stop boundary, such as destructive migration, production credentials, externally visible behavior, or unreconciled Git state.
7. Recommend the next execution skill: `$surgical-change`, `$bug-fix-verification`, `$migration-safety`, or `$dependency-upgrade`.

## Quality bar

- Prefer 3 credible steps over 15 microtasks.
- No broad rewrite unless the current design actually blocks the goal.
- Do not add tests that merely restate the implementation.
- If critical requirements are unresolved, provide a conditional plan and identify the blocked step rather than pretending the plan is approved.

## Output

**Target**, **current evidence**, **steps with checks**, **risks/stops**, **assumptions**, **explicit non-goals**. State that no implementation was performed.
