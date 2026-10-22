---
name: idea-to-scope
description: Turn a vague feature idea into a small, testable scope and explicit non-goals before code changes. Use for product discovery and unclear requests; not for a fully specified small fix.
---

# Idea to scope

Start with the user problem, not a screen or a package name. This is a **thinking workflow**; do not edit source or commit anything.

1. **Find the job.** Identify the user, the moment the problem occurs, and how they currently work around it. If the repository exists, inspect only enough to avoid proposing something it already does.
2. **Challenge the premise.** Name one smaller or simpler way to get the same result. Identify a plausible reason the requested feature might not help.
3. **Define a first slice.** Write the smallest behavior that delivers value; include a real example and a deliberate list of non-goals. Do not convert possibilities into requirements.
4. **Close consequential gaps.** Ask at most a few high-leverage questions when the answer materially changes the outcome. For ordinary decisions, propose a reversible default and mark it as an assumption.
5. **Set acceptance evidence.** Describe how a person could observe success. Include failure or edge cases that would make a superficial demo misleading.
6. **Hand off.** State scope, acceptance criteria, assumptions, rejected alternatives, and unresolved decisions. Invite `$implementation-plan` only after scope is coherent.

## Watch for

- Asking ten questions where a narrow assumption would suffice.
- Adding roles, dashboards, settings, and analytics before the first useful action works.
- Presenting invented user research as fact.
- Claiming agreement or approval that the user has not given.

## Output

A one-paragraph problem statement, **first slice**, **not now**, **acceptance evidence**, and **open decisions**. No code or project state changes.
