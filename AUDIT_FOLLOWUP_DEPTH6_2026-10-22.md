# BQG follow-up audit — 2026-10-22

Repository: `Shtenco/binary_quantum_theory`
Related consolidated report: [AUDIT_REPORT_2026-10-22.md](https://github.com/Shtenco/binary_quantum_theory/blob/main/AUDIT_REPORT_2026-10-22.md)

## Recovery evidence availability

- The historical Stage-A run `36899125190` currently exposes no downloadable artifacts through the Actions artifacts endpoint. This does not prove no external backup exists; these artifacts are not available from the queried run endpoint now.
- The recovery ledger identifies 15 preserved shards: 15/112 shards, 15/2,755 blocks, and 7,749/130,903 columns (5.91965%). Its own claim boundary says this is not rank evidence.
- The multi-shard inventory test run `36938323927` is green historically, but the queried run currently exposes no downloadable artifacts. Treat its green conclusion as historical test evidence, not a present artifact bundle.
- `numerical-continuation` on audit commit `40428136` completed successfully. `core-regression` on that commit was cancelled; a subsequent core run at `34f4c642` was still pending when checked. No clean green full core-regression run has been confirmed.

## Code-level finding: replay authorization has an identity-integrity gap

Reviewed `scripts/depth6_32_replay_authorization.py` on `bqg/depth6-32-canonical-recovery`, blob `c3cf8e98e76c251cb9a2ce0277589fbaaa00abc2`.

The validator checks 2,755 records, unique orbit IDs, total column sum 130,903, all 112 shard IDs present, source-run/engine tags, and aggregate identity cross-check counts. However, record-level SHA-256 is verified only conditionally:

```python
if ledger.get('identity_sha256') is not None:
    _require(ledger['identity_sha256'] == _records_sha(records), ...)
```

Therefore an identity digest is not mandatory. The validator also does not compare each `(orbit_id, rep, m, coord_dim, source_shard)` tuple against a separately frozen trusted manifest. The values `persisted_identity_matches=15` and `historical_batch_matches=102` are counts, not a cryptographic proof that every record matches the frozen assignment.

Risk: a malformed or altered 2,755-record ledger could satisfy aggregate checks without proving it is the canonical frozen assignment. This is a provenance/integrity weakness, not evidence that the current ledger is corrupted.

### Required repair before expensive replay

1. Require `identity_sha256` and compare it with a pinned expected digest from an independently trusted commit/manifest.
2. Validate every record against the frozen assignment manifest: exact orbit IDs, reps, `m`, coordinate dimensions, shard mapping, and expected per-shard block/column totals.
3. Bind the authorization gate to the same expected manifest digest, not counts alone.
4. Add adversarial tests: missing digest; changed rep; changed shard; duplicate/omitted orbit with compensating column sum; altered `coord_dim`; incorrect per-shard totals. Each must fail closed.
5. Only then authorize numerical replay. This is a provenance prerequisite, not a rank result.

## Code-level finding: global peeling helper has good fail-closed boundaries

Reviewed `scripts/depth6_32_global_peeling.py` (blob `ca49027848a4c87e811f292b6d290e75315b4948`) and tests (blob `8f62d9aca3cfb085463c1d53fbbc99235c2c1ca7`).

Positive: exact KEYMETA block/column coverage is required before planning; a candidate is not called rank-certified; SVD is applied to the stack of supplied unique-q matrices; failed full-column rank does not authorize peeling.

Open limitation: correctness depends on the caller supplying complete, current `q_rows` and the actual matrices for precisely the q sectors globally unique in the current active set. The helper does not authenticate these matrices against frozen raw artifacts; that provenance must be guaranteed by orchestration and manifest validation.

## Depth-6 execution decision

Do not launch the 112-shard numerical replay from the currently preserved 15-shard KEYMETA inventory. First recover and verify the full frozen assignment identity and missing KEYMETA from existing raw evidence, or rerun only missing authorized numerical shards using the frozen ledger. Structural shell enumeration, multiplicity, Jucys selectors, and branch identity remain explicitly out of scope for recomputation.

## Priority branch comparison update

GitHub compare API confirms `audit/physicalization-truth-v3` is 234 commits behind `main` with no commits ahead. `bqg/depth6-32-canonical-recovery` is diverged: 92 commits ahead and 151 behind `main` at the latest comparison. It contains the frozen assignment ledger, recovery authorization, shard batching, and global-peeling helpers. These changes must be reviewed and selectively ported; do not merge the branch wholesale because it has a long diverged history.

## Reproduction boundary

No claim is made that the full repository test suite or the 112-shard calculation was executed in this chat environment. The findings above come from source inspection, recorded GitHub Actions metadata, and the recovery ledgers. The depth-6 numerical theorem remains open.
## Additional cross-check: gate digest is present but not bound during replay authorization

The rematerialization gate records SHA-256 `cc8c890d8b0c007195eda8e3ce8e9d109c6b1bab0c7db07b283a0dd10556c4dd`. The identity rematerialization function computes a digest of normalized records and compares persisted records and historical shard totals. However, `depth6_32_replay_authorization.py` checks the ledger digest only against the ledger's own records when that field is present; it does not compare `ledger.identity_sha256` to `gate.identity_sha256`. It also treats the ledger digest as optional. Therefore the authorization stage is not cryptographically bound to the identity digest accepted by the preceding rematerialization gate.

Recommended regression tests must specifically alter the ledger records and recompute the ledger's self-digest while leaving the accepted gate unchanged; authorization must reject the mismatch. Also reject a missing digest. This narrows the finding: the upstream rematerialization gate does compute a digest, but the downstream authorization does not enforce the cross-stage digest equality.

## Repair implemented and regression result

On `bqg/depth6-32-canonical-recovery`, the replay authorization now:
- requires the exact ledger checksum instead of accepting a missing digest;
- separately recomputes the normalized assignment digest used by the upstream rematerialization gate (these hashes cover different record representations and must not be conflated);
- checks that the gate's normalized digest matches the ledger's normalized frozen assignment;
- verifies each record's `source_shard` against the deterministic frozen cost-balancing algorithm, not merely that all 112 shard IDs appear.

Regression tests were added for missing digest, gate-digest mismatch, and tampered shard assignment. The first implementation exposed two downstream schema-8 fixtures that were using inconsistent digest conventions; those fixtures were corrected to preserve the raw ledger checksum separately from the normalized gate digest.

Latest canonical-recovery unit workflow: **PASS**, run [39708336418](https://github.com/Shtenco/binary_quantum_theory/actions/runs/39708336418), commit `a9d5fb911917fbf1b545ccbc5f4f9bc64406a96f`. The job ran the full canonical recovery unit suite and completed successfully.

The separate frozen-m numerical workflow on commit `05020073` was still in progress at the last poll; it is not reported as passed. These changes are confined to the recovery branch and have not been merged into `main`. They improve provenance validation only; they do not add any new numerical rank evidence and do not close the [3,2] sector.

## Branch comparison pass

All 138 non-main branch refs returned by GitHub were compared against the current `main` HEAD, in addition to recording all 139 branch names and HEAD SHAs in the consolidated report. The main report's original sentence saying only ten priority branches had been compared is now stale; the per-branch diff table itself has not yet been expanded to include every result, so this follow-up records the high-signal findings rather than pretending the ten-row sample is the complete table.

High-signal divergent branches requiring content-level triage (do not merge wholesale):
- `research/bcqg-core-candidate-v1`: 411 commits ahead / 274 behind; 300 changed files returned by compare API.
- `research/q2-history-gravity-orientation-current`: 422 ahead / 274 behind; 300 changed files returned.
- `research/physicalization-l1-depth2-metric`: 279 ahead / 274 behind; 218 changed files returned.
- `research/physical-scalar-kernel-dynamics`: 127 ahead / 233 behind; 102 changed files returned.
- `research/physical-pole-universality`: 118 ahead / 274 behind; 97 changed files returned.
- `recovery/bqg-physical-spectral-history-2026-09-06`: 132 ahead / 233 behind; 103 changed files returned.
- `research/physicalization-scale-observable-prediction`: 91 ahead / 274 behind; 70 changed files returned.
- `research/depth6-s4sign-proof`: 69 ahead / 221 behind; 53 changed files returned.
- `research/q2-oriented-flux-history-observable`: 52 ahead / 250 behind; 46 changed files returned.
- `research/q2-orientation-intrinsic-metric-nogo`: 49 ahead / 250 behind; 43 changed files returned.

Several aliases (for example `research/bqg-2t-algebra`, `research/bqg-2t-gate`, and their numbered variants) point to the same HEAD SHA and are all behind `main`; these are duplicate refs rather than independent lines of work. Multiple `codex-*`, NEXUS, and Sinergy refs are also stale or divergent and should not be merged into BQG based on their branch names alone.

Important: compare API `files` arrays can be truncated/capped for large divergences. Ahead/behind and commit counts are useful for prioritization, but content-level review of the large branches must inspect unique files and commits, not rely only on the returned file list.
