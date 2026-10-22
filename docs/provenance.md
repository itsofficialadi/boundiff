# Provenance and attribution

Reference notes for the Boundiff expanded draft, checked **2026-10-22**. This records what informed the *design* of the toolkit. It is not a claim of endorsement, partnership, or automated code import.

| Reference | Revision inspected | File / blob | Observed licensing |
| --- | --- | --- | --- |
| [`multica-ai/andrej-karpathy-skills`](https://github.com/multica-ai/andrej-karpathy-skills) | [`2c606141936f1eeef17fa3043a72095b4765b9c2`](https://github.com/multica-ai/andrej-karpathy-skills/commit/2c606141936f1eeef17fa3043a72095b4765b9c2) | `CLAUDE.md` blob `daced9bd64f25908ebedeb4701fb406985dc8366`; README blob `7cf07a786532bebe01c65179c8e2c3a98cc0a09b` | README license section says **MIT**; a separate top-level LICENSE was not confirmed in the original inspection |
| [`garrytan/gstack`](https://github.com/garrytan/gstack) | [`514fbfdc9799376edfd2536f60659501a48ead64`](https://github.com/garrytan/gstack/commit/514fbfdc9799376edfd2536f60659501a48ead64) | README blob `e44cf94ae71167f0768575ad3b5a47b4da129774`; LICENSE blob `35029511144443297cad2d26e4bac17d0e352f93` | MIT LICENSE at pinned revision |
| [`obra/superpowers`](https://github.com/obra/superpowers) | [`2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`](https://github.com/obra/superpowers/commit/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b) | README blob `c5bb59fdaf17ba154e803c549cd71a73ef36c24b`; LICENSE blob `abf0390320aa14406af7a520b9b0739fdda9bf08` | MIT LICENSE at pinned revision |

## What we took from the references

- **The first project:** the problem framing of overcomplication, unexamined assumptions, and unnecessary code churn.
- **gstack:** the product lesson that distinct development activities deserve distinct workflows, and that first-time users need clear examples of how to start.
- **Superpowers:** the idea that skills can be composed across planning, implementation, and evaluation without making a monolithic prompt.
- **Codex documentation:** `AGENTS.md` for durable instructions, `.agents/skills/<name>/SKILL.md` for task-specific guidance, and concise `name` and `description` front matter.

All Boundiff skill instructions in this draft were newly authored. We did not vendor upstream source, installer code, skill text, or browser tooling. Familiar engineering terms and categories do not imply copied implementation.

If later work copies or materially adapts an upstream file, review the exact applicable license, preserve required notices, and record the pinned file and original authorship. **MIT in an upstream README is not a substitute for review of actual copied content.**

## Current product and compatibility references

- [Codex skill building and local discovery](https://learn.chatgpt.com/docs/build-skills)
- [Codex repository instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

These are documentation references, not project endorsements. Recheck Codex paths and invocation behavior when publishing a tagged version; product behavior can change.

## Standards and platform documentation

- [Agent Skills specification](https://agentskills.io/), an open format originally developed by Anthropic: explains the `SKILL.md` package shape and progressive disclosure. This is **format provenance**, not an upstream repository whose implementation was copied.
- [OpenAI Codex skills documentation](https://learn.chatgpt.com/docs/build-skills): confirms supported paths, metadata, and activation behavior. This is a **compatibility reference**, not an endorsement.
- [OpenAI, *Rethinking skills and prompts for GPT-6 Astra* (2026-09-11)](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): cautions against oversized catalogs, overlapping descriptions, and unnecessary workflow overhead. We favor a selective three-skill starter installation because of that tradeoff.

For a distinction between established ideas, our design synthesis, and results not yet demonstrated, read the [originality assessment](originality.md).
