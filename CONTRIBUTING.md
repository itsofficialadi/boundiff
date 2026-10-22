# Contributing

Start with a bug in the *workflow*, not an idea for a new persona.

Useful contributions include a skill that stops a repeatable failure, a smaller decision rule, an installation edge case, or a realistic task where the current advice produces the wrong behavior.

## Before proposing a skill

- Point to the task and failure mode it addresses. “Developers might like this” is not enough on its own.
- Search the current 16 skills and [skill map](docs/skill-map.md) for overlap. A better example in an existing skill is often the right change.
- State whether the workflow is read-only, write-capable, or inspection-first with a separate action boundary.
- Include one realistic prompt, a useful expected output, and at least one “should not trigger” case.
- Keep the instructions executable with ordinary Codex tools. No new dependency without a reason.

## Pull request checklist

1. Use the smallest set of changed files. Don't reformat unrelated files.
2. Run `python3 scripts/check_pack.py` (Python 3 standard library only).
3. Check every new Markdown link and every command you put in the README.
4. Check for copied phrases or third-party artifacts. Add upstream links, pinned revisions, and license notices when appropriate.
5. State what you actually tried with Codex versus what you only reviewed on paper.

We particularly value **before/after task transcripts or reproducible tests** that show a guideline catching a real failure. Redacted examples are welcome. Never include credentials or private repository content.

## Small changes welcome

Typo fixes, trigger wording, clearer safety boundaries, and better examples are welcome. Not every change needs an issue or an elaborate proposal. Keep the conversation grounded in developer experience, not benchmark theater.

By contributing, you agree that your contribution may be distributed under this repository's MIT license. Do not submit material you do not have rights to share.
