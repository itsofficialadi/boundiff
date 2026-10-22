# Philosophy

Boundiff aims to make everyday coding-agent work more dependable without replacing engineering judgment with a checklist.

## Bounded autonomy

Small, reversible, local choices should not generate a queue of clarification questions. The agent should inspect the code, explain a narrow assumption when material, act within scope, and verify. As potential impact rises, autonomy narrows. Credentials, financial consequences, data loss, production systems, unverified provenance, and security-critical assumptions require explicit boundaries and, where necessary, a stop.

## Smallest correct change

Minimize changed surface area, not correctness. A smaller diff is valuable because it is easier to review and revert. It is not an excuse to omit error handling, input validation, or security protections.

## Independent evaluation

An independent reviewer is useful only when review evidence remains distinguishable from remediation. Keep inspected code unchanged; place experiments in disposable environments; preserve a clear target and scope; describe what was checked and what remains uncertain.

## Provenance and checkpointing

At high-impact boundaries, know which repository, branch, commit, staged diff, artifact, target, and authorizing party are involved. A reproducible handoff is worth more than an assertion that a release 'looks good'. The level of ceremony should scale with real risk.

## Calibrated claims

Evidence has domains. Unit tests validate specific behavior under local assumptions. Static review can identify defects but cannot exhaustively establish safety. A commit identifies a version, not deployment. Hash equality establishes byte equality, not business correctness. Describe precisely which domain the evidence covers.

## Measuring value

Future evaluations can compare the same tasks with and without the guidelines, using metrics such as unrelated changed lines, additional touched files, first-pass task success, regression verification, and unsupported completion claims. Avoid claiming improvement until results are reproducible.
