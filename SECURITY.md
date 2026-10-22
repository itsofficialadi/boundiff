# Security policy

Boundiff is mostly Markdown instructions, but instructions can influence the actions a coding agent takes. Treat skill changes and installer changes as security-relevant during review.

## Reporting a vulnerability

If GitHub private vulnerability reporting is enabled for this repository, use the **Report a vulnerability** action under its Security tab. Do not publish exploit details, secrets, private source code, or personal data in a public issue.

If private reporting is not available, open a public issue requesting a private reporting channel **without including sensitive details**. A maintainer can then identify an appropriate channel. Do not assume a public issue is confidential.

Please include the affected file and revision, what the failure could cause, how to reproduce it safely, and any suggested mitigation. There is no promised response SLA.

## Boundaries

- This project is not a security scanner and does not guarantee that code created with Codex is safe.
- The installer is optional. Preview first and inspect it before `--apply`.
- Skills may recommend potentially risky commands for a particular task. Review commands against your own environment and permission boundaries before execution.
- Never run destructive tests, external probes, or production mutations just to demonstrate a vulnerability.

There is no hosted service, credential collection, or telemetry in this repository.
