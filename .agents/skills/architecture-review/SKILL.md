---
name: architecture-review
description: Critique an existing technical design or proposed architecture for complexity, interfaces, failure modes, and migration cost. Read-only design review; not an implementation request.
---

# Architecture review

Review decisions, not personalities or diagram aesthetics. This is **read-only**.

1. Establish the proposed change, present architecture, traffic/data assumptions, and decision deadline. Mark unknowns; never invent scale or SLO figures.
2. Follow one concrete request or data record through the proposed components. Identify ownership, side effects, dependency boundaries, and how failures surface.
3. Look for accidental complexity: extra services, frameworks, queues, caches, shared abstractions, duplicated state, and premature configurability.
4. Test the important edges: retries, idempotency, authorization, partial failure, observability, concurrency, schema versions, and recovery. Limit focus to actual risk.
5. Compare the proposal against a simpler viable alternative and the status quo. Describe what each option buys and costs.
6. Identify decisions that are easy to reverse versus expensive to reverse. Recommend a proof or spike only if it can resolve material uncertainty.

## Boundaries

Do not mutate source, schemas, infrastructure, or config. Do not claim performance or security guarantees without measurements or analysis of concrete controls.

## Output

**Recommendation**, **what works**, **blocking risks**, **simplifications**, **decisions to defer**, **missing evidence**. Prefer one decision table over an exhaustive catalog of patterns.
