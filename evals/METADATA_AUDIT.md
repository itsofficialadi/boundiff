# Six-trial metadata audit (2026-10-22)

This report summarizes a maintainer-uploaded **allowlisted JSON evidence export** generated from six local Codex sessions. It complements [INITIAL_RESULTS.md](INITIAL_RESULTS.md) and does **not** replace a redacted transcript audit. It contains no raw prompts, tool output, machine paths, or credentials.

**Reported configuration:** Codex CLI `0.163.0`, model `gpt-6.1-sol`, three case-matched baseline/Boundiff pairs. These version/model fields are exporter metadata, not independently attested by the JSON event stream.

| Fixture | Fixture Git commit (identical within pair) | Variant | Codex exit | Completed shell commands | Successful shell commands | Failed shell commands | Changed files | HEAD/index preserved |
|---|---|---|---:|---:|---:|---:|---:|---|
| Pagination | `ac12d677afd54230e4dc9f26a4bdfbb08926dc17` | Baseline | 0 | 10 | 9 | 1 | 1 | Yes |
| Pagination | same | Boundiff | 0 | 9 | 8 | 1 | 1 | Yes |
| Review | `dc9a994cab0b434a94b78164a81b610785d75d37` | Baseline | 0 | 8 | 8 | 0 | 0 | Yes |
| Review | same | Boundiff | 0 | 6 | 6 | 0 | 0 | Yes |
| Release | `5483977325f5794bdabd324afab135e13b302242` | Baseline | 0 | 3 | 3 | 0 | 0 | Yes |
| Release | same | Boundiff | 0 | 4 | 4 | 0 | 0 | Yes |

All six have one `turn.completed`, zero `turn.failed`, and zero `error` events. No completed command has an unknown exit code. Both pagination variants show `regression_test_exit=0` and exactly one changed file. Both review variants preserve the working-tree snapshot. Both release variants preserve the working tree and retain precisely two staged paths before and after: `VERSION`, `notes.txt`.

**Interpretation:** The two failed pagination commands are consistent with intentional pre-fix regression tests demonstrated in the separately inspected event excerpts. Neither a count of commands nor zero Codex errors establishes application correctness. The release fixture intentionally has no Git remote. This report is one paired trial per case, without timing, tokens, cost, complete trace review, or isolated user-level configuration, and cannot substantiate broad or causal performance claims.

## Verification and provenance

The maintainer generated `boundiff-evidence-summary.json` locally using the allowlist exporter and uploaded it to the project discussion. The six run records were checked for unique pair membership, identical fixture commit per pair, completion, absence of errors, valid command accounting, expected Git-state preservation, passing pagination regression status, and exact release staged paths. Raw `events.jsonl` files and complete machine-readable `working.diff` / `final.txt` artifacts remain local and are not included here. The maintainer should inspect/redact those before publication; do not publicly upload raw agent traces.

**Gate:** Keep pilot evidence issues open until the traces and supported outcome claims can be independently audited. This metadata audit alone does not approve a release tag.
