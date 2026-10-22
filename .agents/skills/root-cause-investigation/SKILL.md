---
name: root-cause-investigation
description: Investigate intermittent bugs, regressions, errors, or failing CI to isolate a defensible root cause before changing code. Diagnosis-only; use bug-fix-verification for remediation.
---

# Root-cause investigation

Do not jump from the first error message to a patch. This skill investigates; it does not remediate.

1. Establish symptoms with timestamps, affected versions, inputs, expected behavior, and the **earliest reliable failure signal**. Separate the user's report from observed evidence.
2. Form no more than three competing explanations. State what observation would discriminate between them.
3. Trace the relevant path: caller, state transitions, data shape, exceptions, retries, configuration, and recent changes. Search narrowly before searching everywhere.
4. Run small, controlled experiments when the environment permits. Start with deterministic local reproductions; avoid writing to production or external systems. Record command, input, and outcome.
5. Update hypotheses as evidence arrives. Do not label correlation as root cause. If no explanation survives testing, explicitly report a bounded unknown.
6. Hand off the smallest candidate correction and a proposed regression check to `$bug-fix-verification`. Do not edit the reviewed code during diagnosis.

## Special cases

- CI-only failure: compare runtime versions, environment, time, ordering, data, and resource constraints rather than immediately retrying.
- Flaky test: check shared state, parallelism, nondeterministic order, leaked timers, and dependencies before increasing timeouts.
- Incident: treat secrets, live customer data, and deployment actions as separate authorization boundaries.

## Output

**Symptom**, **evidence timeline**, **hypotheses tested**, **most likely cause with confidence**, **reproduction**, **next safe action**. Say clearly when the cause remains unconfirmed.
