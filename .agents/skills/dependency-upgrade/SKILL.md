---
name: dependency-upgrade
description: Safely upgrade a specified package or small dependency group, inspect supply-chain changes, and verify compatibility. Use for targeted version updates; not automatic bulk maintenance.
---

# Dependency upgrade

Upgrade for a reason. Avoid turning one package bump into a lockfile rewrite of the world.

1. Confirm requested packages, target version policy, package manager, supported runtimes, and the real dependency manifest and lockfile.
2. Read official changelog/release notes and security advisories when available. If sources are unavailable, state the limitation and avoid invented migration instructions.
3. Compare compatibility: major-version breaks, transitive movement, peer requirements, native toolchains, license changes, build scripts, and package provenance when relevant.
4. Establish baseline verification. Update only scoped manifests and the required lockfile using the project's existing tooling; do not disable checks or ignore unrelated lockfile churn.
5. Run targeted build, tests, and critical integration checks. Inspect exact manifest/lockfile changes and unexpected new packages or install scripts.
6. Report observed version changes, residual risks, and any follow-up migration. Stop for suspicious provenance, unexpected script execution requirements, or a broad unexplained dependency graph rewrite.

## Boundaries

Package installation may run third-party scripts or contact a registry. Honor the sandbox and authorization rules; explain when verification cannot be done safely. Never publish packages or change CI credentials as part of a version bump.

## Output

**Before/after versions**, **reason**, **scope**, **compatibility changes**, **checks**, **unexpected transitive changes**, **remaining risks**.
