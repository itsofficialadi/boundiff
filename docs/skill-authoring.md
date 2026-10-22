# Writing a useful skill

A skill earns its own directory when a task needs a repeatable workflow that would clutter `AGENTS.md`.

Codex reads the `name` and `description` first, then loads a skill's instructions when it selects the skill. Be precise about triggers so users don't get a full security review when they asked for a README typo.

```md
---
name: example-skill
description: Do one specific job; state when it applies and the nearby job it does not replace.
---

# Example skill

1. Verify relevant context and inputs.
2. Perform the bounded workflow.
3. Check the result and report the evidence.
```

## A reviewable skill has five properties

1. **An unmistakable trigger.** The description says what task activates it, not merely that it's “helpful for coding”.
2. **One job.** Separate plan, investigation, review, remediation, and release rather than quietly changing modes mid-task.
3. **A useful default.** Make progress on ordinary uncertainty; name the cases that truly require a stop.
4. **Evidence discipline.** The output distinguishes what was observed, what was inferred, and what could not be tested.
5. **Negative space.** Name the tempting but wrong actions, such as editing a review target or running a migration on production.

Instruction-only is the default. Add scripts only when there is a deterministic task that prompts handle poorly, and test those scripts independently. Do not require browser tooling for skills that can operate on API/CLI evidence.

## Test the skill itself

Review at least these cases before proposing it:

- **Correct trigger:** a prompt where this skill should clearly activate.
- **Neighbor trigger:** a prompt better handled by a different skill.
- **Trivial work:** a task where no skill is needed.
- **Risk boundary:** an operation that should stop before changing dangerous state.
- **Evidence limitation:** a blocked check that the skill must report without inventing success.

Run `python3 scripts/check_pack.py` to validate the repository's structure. It does **not** test whether Codex follows the instructions. That requires observed agent runs and human evaluation.

Reference: [official Codex skill guide](https://learn.chatgpt.com/docs/build-skills).
