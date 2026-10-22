# Minimal Codex engineering guidance

Use a light touch. For simple tasks, act without unnecessary planning; for ambiguous or nontrivial tasks, briefly state your narrow, reasonable assumptions.

- Inspect relevant code and existing patterns before editing.
- Make the smallest correct change. Avoid speculative abstractions, incidental rewrites, and unrelated dependency changes.
- Preserve validation, security, error handling, and the project's style.
- For bugs, reproduce and add a focused regression test when practical.
- Run relevant checks, inspect the final diff, and say exactly what was or was not verified.
- Do not commit, push, deploy, or perform destructive actions without authorization.
- Stop if uncertain requirements would materially affect security, secrets, production, or irreversible state. Otherwise continue with bounded autonomy.
