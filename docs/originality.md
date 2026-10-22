# What is original here?

**Short answer:** the ingredients are established engineering practices. The contribution we are attempting is a specific way to combine those practices for Codex: bounded autonomy, separate review and remediation, risk-proportionate provenance, and claims that match evidence. That combination is a design choice, not a proven invention or performance improvement.

There are mature tools in this space. It would be misleading to describe Boundiff as the first coding-agent skill collection, the first Codex skill pack, the inventor of `SKILL.md`, or a substitute for agent/tool security controls.

## Where the ideas overlap

| Public project or standard | Existing work relevant to us | Our relationship to it |
| --- | --- | --- |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Think before coding, simplicity, surgical changes, verification | The clear starting influence on the four foundational principles. Credit the repository and maintainers; don't present it as Karpathy's own repo or imply endorsement. |
| [garrytan/gstack](https://github.com/garrytan/gstack) | Specialized workflows for planning, review, QA, debugging, and shipping, including Codex support | Strong overlap in skill categories and onboarding. We studied the value of a navigable workflow catalog, not its implementation. |
| [obra/superpowers](https://github.com/obra/superpowers) | A composable skills methodology spanning planning, execution, tests, and review, also usable with Codex | Strong overlap in workflow composition. Our goal is a smaller policy layer and more explicit boundaries, not to claim we invented multi-stage workflows. |
| [Agent Skills specification](https://agentskills.io/) | Portable `SKILL.md` packaging with name, description, and progressive disclosure | We use a public standard, originally developed by Anthropic. This format is not proprietary to Boundiff or Codex. |
| [OpenAI's Codex skills documentation](https://learn.chatgpt.com/docs/build-skills) | Where skills live, how Codex discovers them, how to write descriptions | Implementation reference for supported Codex discovery and invocation, not an endorsement. |

These references serve different purposes. The first three influenced the product framing or structure. The specification and Codex docs are compatibility references. See [pinned sources and license notes](provenance.md). This is a comparison of documented features, not an exhaustive text-similarity or license audit of every file in those projects.

## What we are proposing, rather than claiming to have invented

1. **Risk-proportionate autonomy.** Keep moving on bounded, reversible engineering tasks while making high-impact decisions explicit. Avoid both constant questioning and reckless execution.
2. **Review is not remediation.** A reviewer may inspect and safely test in a disposable environment, but must not silently change the target it is supposed to assess.
3. **A chain of evidence.** A local regression, a code review, a commit, a push, a deployed artifact, and production behavior establish different things. Preserve the distinctions in handoffs.
4. **Provenance at boundaries.** Verify the relevant source state, staged paths, artifact identity, destination, and authority before consequential Git or deployment actions, without imposing release ceremony on a typo fix.
5. **A small default with optional workflows.** `AGENTS.md` holds persistent expectations. Skills activate when the task needs a distinct procedure. The suggested installation starts with three skills rather than all sixteen.

**Codex positioning check:** The current pack is oriented toward Codex and follows its documented local skill conventions, but most of its workflow content would also make sense in another agent. That is not proof of deep Codex-specific differentiation. We should earn the phrase "Codex-native" through documented Codex trials, invocation behavior, and integration choices rather than merely the directory name.

These ideas are not unique in isolation. Our product hypothesis is that making them **consistent across a whole task lifecycle** will reduce scope drift, unsupported completion claims, and risky changes without slowing down ordinary development.

## What we do not yet have evidence to claim

- We have **not** established that Boundiff produces better code, fewer unrelated edits, or more reliable review findings than competing packs or an unmodified Codex setup.
- We have **not** run a published, controlled benchmark of these policies against gstack, Superpowers, or Codex alone.
- Local packaging tests validate directory structure and installer behavior. They **do not** demonstrate agent compliance.
- The drafted instructions draw on the project's design brief and public engineering ideas. Until real work examples are documented, do **not** market every rule as a lesson personally measured in production.
- Separately written text is not the same as a certified originality clearance. Before publication, reread anything closely adapted from another author's expression and retain required notices where applicable.

## How to turn experience into an actual contribution

For each proposed rule or new skill, record an evidence-backed engineering case with:

- **Problem:** what happened in a real, shareable task, with sensitive details removed.
- **Baseline:** the request and Codex behavior without the rule, using the same code revision and tools when feasible.
- **Intervention:** the exact `AGENTS.md` or skill change introduced.
- **Result:** what happened afterward, including regressions and extra time/questions.
- **Decision:** keep, narrow, revise, or remove the rule based on observed value.

The [evaluation guide](evaluation.md) outlines comparisons. Publish the failures alongside successful examples. We should prefer a tested six-skill toolkit over an untested sixty-skill collection.

## What the repository can actually demonstrate today

The optional installer previews changes, refuses to overwrite existing policies or skills, and rejects symlinked skill destinations. Its tests exercise those boundaries in disposable temporary directories ([test file](../tests/test_packaging.py)); the package validator checks skill metadata and local links ([source](../scripts/check_pack.py)). These are concrete implementation details and tested behaviors of **the packaging tools**, not proof that the prompts improve Codex's engineering results.

This distinction matters. We can claim the installer has local tests; we cannot yet claim that Codex using these skills is safer or more effective in production.
