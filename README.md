# Boundiff

**Small changes. Strong evidence.**

Boundiff combines *bounded autonomy* with disciplined *diffs* for everyday Codex work.

Created by [Aditya Shekhar](https://github.com/itsofficialadi).

A practical `AGENTS.md` and a set of 16 focused skills for [OpenAI Codex](https://developers.openai.com/codex/). Use them to turn a rough idea into a scoped change, investigate a failure, review a risky patch, verify real behavior, and prepare a clean handoff.

No services to sign up for. No telemetry. No runtime needed to use the skills. Just Markdown that lives with your code.

> **Example:** “The export endpoint times out on large accounts.”
>
> Use `$root-cause-investigation` to isolate the bottleneck without making changes, `$bug-fix-verification` to land a regression-backed fix, and `$pull-request-handoff` to explain exactly what changed and what was tested.

The point is not to make Codex follow a ceremony for every typo. It's to make the important boundaries hard to miss on work where mistakes are expensive.

## Start here

If you're adding Boundiff to an **existing repository**, check whether it already has an `AGENTS.md` and `.agents/skills/` first. Preserve the project's existing instructions.

### Install in a project

**From a local checkout** (recommended when trying it for the first time):

```sh
git clone https://github.com/itsofficialadi/boundiff.git
cd boundiff
python3 scripts/install.py --target ../your-project
```

This **previews** the installation. It changes nothing. If the paths look right, run:

```sh
python3 scripts/install.py --target ../your-project --skills all --apply
```

By default this installs only `surgical-change`, `bug-fix-verification`, and `independent-review`. Add more skills when you need them (`--skills all` is available). The optional installer uses only Python's standard library. It refuses to overwrite existing files and won't stage, commit, or contact a network service. If your project already has an `AGENTS.md`, merge the policies manually rather than replacing it. [Installation notes](docs/customizing.md#install-or-update-safely).

**No Python? No installer needed.** Copy [`AGENTS.md`](AGENTS.md) into a new project, or merge it with your existing policy. Then copy the desired directories from [`.agents/skills/`](.agents/skills/) into `<your-project>/.agents/skills/`. Keep each `SKILL.md` at its original path. No script is executed by a skill merely because the skill was installed.

**Just want the policy?** Once this repository is published, download it to a safe name for review:

```sh
curl --fail --location --silent --show-error \
  https://raw.githubusercontent.com/itsofficialadi/boundiff/main/AGENTS.md \
  --output AGENTS.boundiff.example.md
```

Don't replace an existing `AGENTS.md` without reading and merging it.

**Personal Codex setup:** Codex also discovers skills under `~/.agents/skills`. Copy the selected skill directories there if you want them available across projects. Project rules belong in each project's `AGENTS.md`, not in your global skill instructions. See [Codex skill locations](https://learn.chatgpt.com/docs/build-skills).

## Pick a skill

You don't need to memorize all 16. Ask Codex naturally, or explicitly mention `$skill-name` in Codex CLI or the IDE extension. Codex can also match skills to tasks using their descriptions.

| When you're trying to… | Skill | Changes files? |
| --- | --- | --- |
| Turn a fuzzy request into a first useful slice | [`$idea-to-scope`](.agents/skills/idea-to-scope/SKILL.md) | No |
| Plan a multi-file change before writing code | [`$implementation-plan`](.agents/skills/implementation-plan/SKILL.md) | No |
| Challenge a design before committing to it | [`$architecture-review`](.agents/skills/architecture-review/SKILL.md) | No |
| Implement a contained feature or fix | [`$surgical-change`](.agents/skills/surgical-change/SKILL.md) | Yes |
| Fix a bug with credible regression evidence | [`$bug-fix-verification`](.agents/skills/bug-fix-verification/SKILL.md) | Yes |
| Explain an intermittent bug or CI failure | [`$root-cause-investigation`](.agents/skills/root-cause-investigation/SKILL.md) | No |
| Find the important holes in a test suite | [`$test-gap-audit`](.agents/skills/test-gap-audit/SKILL.md) | No |
| Exercise real user flows in local/staging | [`$acceptance-qa`](.agents/skills/acceptance-qa/SKILL.md) | No by default |
| Review a change without modifying it | [`$independent-review`](.agents/skills/independent-review/SKILL.md) | No |
| Evaluate a trust boundary or risky patch | [`$security-review`](.agents/skills/security-review/SKILL.md) | No |
| Investigate a measured slowdown | [`$performance-investigation`](.agents/skills/performance-investigation/SKILL.md) | No by default |
| Update a package without dependency churn | [`$dependency-upgrade`](.agents/skills/dependency-upgrade/SKILL.md) | Yes |
| Handle a schema change or backfill | [`$migration-safety`](.agents/skills/migration-safety/SKILL.md) | Yes locally, with boundaries |
| Keep docs aligned with working behavior | [`$docs-sync`](.agents/skills/docs-sync/SKILL.md) | Yes, docs only |
| Hand reviewers a clear diff and evidence | [`$pull-request-handoff`](.agents/skills/pull-request-handoff/SKILL.md) | No |
| Verify a commit, release, or push boundary | [`$release-checkpoint`](.agents/skills/release-checkpoint/SKILL.md) | Inspection by default |

If you only install three to start with, try `surgical-change`, `independent-review`, and `bug-fix-verification`. Add the others when the corresponding work appears. [Skill selection guide](docs/skill-map.md).

## Three common workflows

**A bug that doesn't reproduce locally**

```text
Use $root-cause-investigation for this intermittent webhook failure.
Don't edit code. Show the hypotheses you ruled out and what evidence is missing.
```

Then, when there is a reproducible fix path:

```text
Use $bug-fix-verification to fix the webhook race. Keep changes to the
retry path and its tests. Show the failing and passing evidence if available.
```

**A feature with unclear scope**

```text
Use $idea-to-scope to narrow the CSV import request to a first release.
Then use $implementation-plan. Do not implement anything yet.
```

**A release you need to trust**

```text
Use $independent-review on the diff against main. Do not edit files.
After we resolve the findings, use $release-checkpoint in inspection mode.
List the exact staged paths, checks run, and anything still unverified.
```

More examples, including migration and QA handoffs, are in [workflow recipes](docs/recipes.md).

## What is ours, and what isn't

The engineering ideas in this repository are not new in isolation. Small changes, regression testing, independent review, and careful releases were established practices before coding agents existed. Skill catalogs for Codex and other agents already cover much of this territory.

**Our product hypothesis** is that a small persistent policy and deliberately separated workflows can keep one consistent boundary across the job: implement narrowly, review without silent remediation, verify the right evidence, and confirm source and target state before consequential release actions. That is a *design position*, not a demonstrated advantage over other tools. The pack is Codex-oriented and uses its supported skill conventions, but the workflow prose is largely portable rather than uniquely tied to Codex internals.

`AGENTS.md` carries persistent expectations. Task-specific skills supply procedures only when relevant. A planner doesn't quietly implement. A reviewer doesn't change its review target. A local test doesn't turn into a deployment claim. A release inspection doesn't authorize a push.

We have not published Codex behavior benchmarks yet. We will not claim this pack improves outcomes until comparable real task runs support that conclusion. Read [the overlap and originality assessment](docs/originality.md), [evaluation criteria](docs/evaluation.md), and [how skills are written](docs/skill-authoring.md).

## Choose your baseline policy

The default [root `AGENTS.md`](AGENTS.md) works for most repositories. These alternatives are starting points, **not** policies to concatenate:

- [`minimal`](templates/minimal/AGENTS.md): everyday projects, minimal overhead.
- [`startup`](templates/startup/AGENTS.md): public APIs, customer-facing reliability, migrations.
- [`security-sensitive`](templates/security-sensitive/AGENTS.md): high-impact systems with stricter provenance and stop rules.

Merge one into your actual project instructions, including its real commands, constraints, protected state, and approval boundaries. [Customization guide](docs/customizing.md).

## Quality and contribution

Every skill must have a distinct reason to exist and a realistic failure mode it prevents. We prefer a short skill that earns its place over a hundred steps no one reads.

The pack includes a dependency-free validator:

```sh
python3 scripts/check_pack.py
```

It checks skill metadata, local Markdown links, and other packaging invariants. That is **structural validation**, not evidence that Codex reliably follows the behaviors. The latter needs real tasks and comparison trials. Our [contribution guide](CONTRIBUTING.md) explains the bar for additions and examples. See the [security policy](SECURITY.md) for responsible reporting and the [maintainer publishing checklist](docs/publishing.md) before creating a public release.

## Attribution and licensing

**Created by [Aditya Shekhar](https://github.com/itsofficialadi).** Boundiff is independently maintained, **not official OpenAI guidance**, and is not endorsed by OpenAI or the referenced authors and maintainers.

We want the influences to be easy to find, not buried in a footnote:

| Source | What we learned or referenced |
| --- | --- |
| [`multica-ai/andrej-karpathy-skills`](https://github.com/multica-ai/andrej-karpathy-skills) | The four foundational themes: thinking before changing, simplicity, surgical diffs, and verification. The source is the **multica-ai repository**, not an endorsement by Andrej Karpathy. |
| [`garrytan/gstack`](https://github.com/garrytan/gstack) | Distinct engineering workflows and practical onboarding. |
| [`obra/superpowers`](https://github.com/obra/superpowers) | Composable workflows across planning, implementation, and testing. |
| [Agent Skills specification](https://agentskills.io/) | Open `SKILL.md` format, originally developed by Anthropic. |
| [Codex skills documentation](https://learn.chatgpt.com/docs/build-skills) | Codex skill conventions and discovery locations. |

The files in this repository were drafted for Boundiff rather than vendored from those projects. Concepts, workflow categories, and common engineering advice are shared across the field. That statement is not a substitute for a line-by-line plagiarism or legal review. If upstream wording or code is added in the future, its license and required notices must be preserved.

For exact inspected commits, file hashes, license observations, and reference roles, see [provenance](docs/provenance.md). For overlap and limitations, see [originality assessment](docs/originality.md).

Boundiff itself is licensed under [MIT](LICENSE). Copyright © 2026 Aditya Shekhar.
