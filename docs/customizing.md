# Fit Boundiff to your repository

The baseline is short on purpose. Keep the root `AGENTS.md` focused on behavior you expect in almost every task. Put project facts and commands in that file and specialized procedures in skills.

## Make the guidance local

Choose the root `AGENTS.md` or **one** of the [minimal](../templates/minimal/AGENTS.md), [startup](../templates/startup/AGENTS.md), or [security-sensitive](../templates/security-sensitive/AGENTS.md) alternatives. These are starting points, not layered files.

A useful project-specific section looks like this:

```md
## Project notes
- Run `python -m pytest tests/orders -q` for order service changes.
- API clients are generated from `api/openapi.yaml`; don't hand-edit them.
- Schema changes require compatibility with the previous deployed application version.
- Production database access is never authorized by ordinary feature requests.
```

Replace those details with facts about your actual repository. Don't paste example commands into your live policy and assume they apply.

## Install or update safely

The checkout contains an **optional**, no-network installer to reduce copy mistakes. Python 3 is needed only to run this helper, not to use the skills.

```sh
# Inspect a full install (read-only preview).
python3 scripts/install.py --target ../your-project --skills all

# Install only three selected skills and the startup policy.
python3 scripts/install.py --target ../your-project --preset startup \
  --skills surgical-change,bug-fix-verification,independent-review --apply

# Install all skills, but no AGENTS.md, into a repo with an existing policy.
python3 scripts/install.py --target ../your-project --policy none --skills all --apply
```

The helper will **not overwrite** an existing `AGENTS.md` or skill directory. If any selected path conflicts, it stops before copying any file, so you can inspect and merge manually. It does not run skill contents, install dependencies, edit Git metadata, or push. It does not fetch updates. Inspect the installer before choosing `--apply`.

Manual installation is equally supported: copy `SKILL.md` directories to `.agents/skills/` in the target project and preserve existing folders.

## Selective installs are expected

There is no requirement to install all 16 skills. Developers working on an API may want `surgical-change`, `bug-fix-verification`, `security-review`, and `pull-request-handoff`. A data team may use `migration-safety`, `root-cause-investigation`, and `release-checkpoint`.

Skills are selected explicitly with `$skill-name` or matched by their descriptions. See [skill map](skill-map.md) to avoid overlapping workflows.

## User-wide skills

Codex also scans `$HOME/.agents/skills` for user-wide skills. If you want Boundiff in many projects, copy the chosen skill directories there. Keep each repository's own constraints in its `AGENTS.md`. Avoid copying a generic project policy over a carefully maintained local one.

Codex may pick up new skills automatically; if not, restart your Codex session. Verify available skills with your installed Codex version.

## Maintenance

Treat behavior changes as code review: why is a rule needed, when is it safe to skip, and does it collide with a higher-priority instruction or another skill? Don't add a new skill merely to get a longer feature list.
