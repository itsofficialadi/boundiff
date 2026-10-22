---
name: migration-safety
description: Plan or implement a backward-compatible schema or data migration with rollout, validation, and recovery gates. Use for persistent-state changes; never run against production without explicit authorization.
---

# Migration safety

A migration is a compatibility transition, not only a SQL file.

1. Identify source and destination schemas, data owners, writers/readers, deploy topology, retention obligations, and expected data volumes when known.
2. State invariants: no lost records, compatibility with old and new application versions, stable identifiers, constraints, and permitted downtime or dual-write periods.
3. Design a staged sequence where appropriate: **expand**, deploy compatible readers/writers, **backfill**, verify, then **contract** in a later authorized window. Do not force this pattern when a simpler transaction is genuinely safe.
4. Specify replayability, batch size, lock exposure, idempotency, validation queries, monitoring, and failure/rollback semantics. A reversible schema change does not automatically reverse changed data.
5. For authorized local implementation, edit only scoped migration code and tests. Test on disposable or sanitized representative data, including old/new version combinations if practical.
6. Stop before production execution, irreversible backfill, table drop, or deletion unless scope, environment, backup/recovery posture, and authority are explicit. Do not silently perform production operations.

## Output

**Invariants**, **ordered rollout**, **compatibility window**, **verification queries/checks**, **stop/rollback plan**, **unverified assumptions**, and exactly **what was executed where**.
