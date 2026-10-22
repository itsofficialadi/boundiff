# The skill map

The useful unit is a **decision**, not a role-playing persona. Call a skill when it changes how the task should be performed.

## The usual path

```text
Unclear request       $idea-to-scope
        ↓
Meaningful change     $implementation-plan (when needed)
        ↓
Implementation        $surgical-change / $bug-fix-verification
        ↓
Independent checking  $independent-review / $security-review / $test-gap-audit
        ↓
Real behavior         $acceptance-qa
        ↓
Handoff               $pull-request-handoff / $docs-sync
        ↓
Release boundary      $release-checkpoint
```

This is a map, not a mandatory conveyor belt. A typo needs none of it. A high-risk change may need only a short plan, an independent review, and a release checkpoint. Don't run three review skills if one focused pass covers the risk.

## Where skills differ

| Decision | Use | Avoid confusing it with |
| --- | --- | --- |
| “What should we build?” | `idea-to-scope` | `implementation-plan` assumes an outcome is already reasonably clear |
| “How would this fit our code?” | `implementation-plan` | `architecture-review` is a critique of the design, not a task list |
| “Why is it failing?” | `root-cause-investigation` | `bug-fix-verification` is allowed to implement the correction |
| “Did the user flow work?” | `acceptance-qa` | `test-gap-audit` inspects the effectiveness of existing tests |
| “Is this change correct?” | `independent-review` | `security-review` goes deeper on exploit paths and controls |
| “Is it fast enough?” | `performance-investigation` | `surgical-change` should not guess at bottlenecks |
| “Is it safe to change data?” | `migration-safety` | `release-checkpoint` handles Git/release integrity, not schema rollout design |
| “Can a reviewer pick this up?” | `pull-request-handoff` | `release-checkpoint` verifies staged and repository state |

## Common handoffs

- `root-cause-investigation` → `bug-fix-verification`: carry the reproduction, expected behavior, and rejected hypotheses. Do not carry an unverified fix claim.
- `implementation-plan` → `surgical-change`: carry acceptance criteria, non-goals, and a smallest-first sequence. The plan is not blanket authorization for deploys or destructive tasks.
- `independent-review` → `surgical-change`: carry findings, but begin a separate authorized implementation task. The original review target remains intact.
- `acceptance-qa` → `bug-fix-verification`: carry exact environment, actions, inputs, and observed results. “It felt wrong” is not reproducible evidence.
- `pull-request-handoff` → `release-checkpoint`: carry the tested diff and unresolved concerns. The checkpoint must still verify actual Git state.

## Evidence vocabulary

Use language that tells readers exactly what happened:

- **Observed:** output, source location, or runtime behavior actually inspected.
- **Reproduced:** the relevant failure was seen under stated conditions.
- **Verified locally:** checks ran against a specific local build or workspace.
- **Reviewed:** a bounded scope was inspected, with stated limits.
- **Prepared:** an artifact or plan exists, but was not necessarily run or published.
- **Unknown:** missing evidence that might change the conclusion.

Avoid broad claims like “fully secure”, “production ready”, or “all edge cases covered” unless the claim can be defined and independently checked.
