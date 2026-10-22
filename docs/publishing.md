# Maintainer publishing checklist

Boundiff is an independent engineering toolkit. Make the repository useful before trying to make it popular. This is a release checklist, not an automated publish procedure.

## Before making the repository public

- [ ] Read the entire root policy and all changed skill instructions. Check for contradictory permissions or accidental requirements to execute unsafe commands.
- [ ] Run `python3 scripts/check_pack.py` and `python3 -m unittest discover -s tests -v` from the repository root.
- [ ] Run an installation preview against a disposable target, and confirm `--apply` copies only the intended paths. Confirm conflicts do not overwrite existing policies.
- [ ] Try at least three skills in an actual Codex environment: a narrow implementation, an independent read-only review, and a release inspection with unexpected staged content. Inspect the actual result, not just the agent's summary.
- [ ] Review README commands and repository links after publishing. Confirm that the default branch matches the raw-file URL.
- [ ] Recheck upstream links, reference commits, license observations, and originality. Preserve notices for any future copied or adapted files.
- [ ] Confirm that `SECURITY.md` offers a real private reporting route if GitHub private vulnerability reporting is enabled.
- [ ] Ensure there are no secrets, local logs, private paths, generated caches, or unrelated files in the public commit.
- [ ] Inspect the exact staged diff and Git status before committing. Do not blindly stage all files.

## GitHub listing

Suggested description: **Engineering guidelines and reusable skills for OpenAI Codex.**

Suggested topics: `codex`, `agents-md`, `agent-skills`, `coding-agents`, `developer-tools`, `software-engineering`, `code-review`, `testing`, `openai`.

Pin the **three-skill starting point** from the README instead of selling a long catalog. The 16 workflows are there when users need them.

## Credible launch demonstrations

Use actual examples with a public, reproducible repository snapshot:

1. **Small fix:** show the task, exact diff, and regression result. Count unrelated edits.
2. **Independent review:** show a finding and establish that the reviewed tree stayed unchanged.
3. **Release checkpoint:** intentionally stage an unexpected file in a disposable repo and show that the workflow stops before committing.

Record the Codex version, inputs, environment, reference commit, selected skills, and observed outputs. Do not claim these examples prove general effectiveness. Publish misses and inconvenient results alongside successes.

## After publishing

Start with user reports and workflow failures, not a large feature roadmap. Collect repeatable problems, add minimal reproductions, and distinguish structural test coverage from real-world behavior. Tag a release when the public documentation, installation path, and first Codex trials have been checked.

## Product and attribution truthfulness

- [ ] Read [the overlap and originality assessment](originality.md); ensure no README, listing, or launch post claims that ordinary skills, Codex compatibility, `SKILL.md`, or review workflows were invented here.
- [ ] Keep upstream project and maintainer credits visible in the README. Preserve exact copyright/license notices for any third-party code or text intentionally copied or adapted in future revisions.
- [ ] Do not market hypothetical failure modes as personally observed production incidents without a real, shareable source and supporting evidence.
- [ ] Lead with the three-skill starter pack. Make installing all 16 an explicit choice; assess skill selection and conflicts before adding more.
- [ ] Revisit `AGENTS.md` and descriptions with actual Codex trials, especially to catch excessive caution or unintended implicit skill triggers.

## Creating the first public repository

**Owner:** `itsofficialadi`. The repository must be created under this account, not the creator's historical GitHub URL.

If the [GitHub CLI](https://cli.github.com/) is installed and authenticated as `itsofficialadi`, you can create and push directly after the local validation, staging review, and commit shown below. Replace the final `git remote add` and `git push` commands with:

```sh
gh auth status
gh repo create itsofficialadi/boundiff --public --source=. --remote=origin --push
```

Alternatively, create an empty public repository at `https://github.com/new` and use the `git remote add`/`git push` commands below. Never use `--force` to bypass unexpected remote contents.

These commands are **for the repository owner**, after they have confirmed the contents and created an **empty public** repository named `boundiff` in the intended GitHub account. In the GitHub creation form, do not generate an additional README, license, or `.gitignore` because this package already contains them.

```sh
# From the root of the extracted Boundiff package
git init -b main
python3 scripts/check_pack.py
python3 -m unittest discover -s tests -v
git add .agents .github .gitignore AGENTS.md CHANGELOG.md CONTRIBUTING.md \
  LICENSE README.md SECURITY.md docs scripts templates tests
git diff --cached --check
git diff --cached --stat
git status --short
# Review the staged content; then, if correct:
git commit -m "Initial public Boundiff toolkit"
git remote add origin https://github.com/itsofficialadi/boundiff.git
git push -u origin main
```

Confirm you are authenticated as `itsofficialadi` before creating the repository or pushing. If the repository or remote already has content, inspect the state and do not overwrite it. **Never force-push** to resolve unexpected remote content. These steps do not run automatically.
