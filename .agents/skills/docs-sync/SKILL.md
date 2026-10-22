---
name: docs-sync
description: Update user or maintainer documentation to match observed software behavior and commands. Use for documentation drift and feature handoffs; avoid speculative or unrelated rewriting.
---

# Documentation sync

Documentation should describe the software that exists, not the feature as originally imagined.

1. Identify the change, intended reader, relevant entry points, actual config/CLI/API behavior, and current documentation.
2. Verify names, flags, environment variables, examples, version requirements, and error cases against source or a runnable command where practical.
3. Edit only impacted sections. Prefer a working example with realistic input and output over vague adjectives. Preserve the project's voice and established formatting.
4. Ensure installation examples do not overwrite existing files without warning, pipe unreviewed remote scripts into a shell, or require unnecessary privileges.
5. Check local links, code fences, command examples, and the diff. If code and docs disagree, report the mismatch rather than fabricating intended behavior.
6. Distinguish commands **executed** from commands **documented but not run** in the final handoff.

## Output

**Readers affected**, **documentation paths**, **behavioral evidence**, **example checks**, and **known gaps**. Never claim an integration works because its README says so.
