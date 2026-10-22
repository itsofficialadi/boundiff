---
name: security-review
description: Perform a bounded, read-only application security review of code, dependencies, or a change set. Use for threat and control analysis; not penetration testing of external targets or silent remediation.
---

# Security review

Report credible exploit paths and broken controls, not an inventory of every security buzzword. **Review is not remediation.**

1. Identify exact repository revision and review scope. Clarify trusted and untrusted inputs, assets, roles, and sensitive operations.
2. Trace relevant trust boundaries: authentication, authorization per object, parsing, injection surfaces, secrets, file/network access, persistence, logging, and unsafe defaults.
3. For each candidate risk, describe attacker prerequisites, entry point, violated invariant, impact, and the protective control expected.
4. Confirm findings with source-backed reasoning or safe, bounded local tests. Never use real secrets, production data, external scanning, exploitation, or disruptive traffic without explicit authority. Prefer a disposable workspace.
5. Rank by plausible impact and exploitability; distinguish confirmed flaws from defense-in-depth opportunities and unresolved questions.
6. Provide remediation direction and a regression test idea, but **do not edit the reviewed target**. A later authorized task can implement a fix and then seek a separate review.

## Output

For each finding: **severity**, **file/line or flow**, **preconditions**, **impact**, **evidence**, **proposed control**, **confidence**. Include scope and explicit non-coverage. No "secure" or "no vulnerabilities" conclusion from a bounded review.
