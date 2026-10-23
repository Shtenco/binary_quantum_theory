# Depth-6 [3,2] KEYMETA artifact audit — 2026-10-22

## Scope

Audited durable GitHub Actions artifacts from authorized replay run [39708640090](https://github.com/Shtenco/binary_quantum_theory/actions/runs/39708640090), commit `3f44e5759385f91ec8c59530eaa3b96b00de65aa`.

This is an artifact-integrity audit, not a rank computation or proof of physical closure.

## Original source results

- Source run reported 21 artifacts: 20 shard artifacts plus the replay-authorization artifact.
- Downloaded and inspected all 20 shard artifacts.
- Durable shard IDs: `0, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 17, 18, 19, 20, 21, 22, 23, 24`.
- Each archive passed ZIP CRC validation and contained exactly one shard manifest.
- Each manifest's listed KEYMETA block was present and its SHA-256 matched the manifest.
- No duplicate shard IDs or orbit IDs were found among the audited artifacts.
- Durable blocks: 20.
- Manifest-declared columns: 11,169 of target 130,903 (8.53%).
- Compressed KEYMETA block payloads inspected: 303,385 bytes.
- Artifact integrity errors: 0.

## Recovery run snapshot — 2026-10-23 17:56 UTC

Recovery run: [39743112374](https://github.com/Shtenco/binary_quantum_theory/actions/runs/39743112374), branch `bqg/depth6-32-canonical-recovery`, commit `9f69eaf9a4bc9dac130745dd33e3e24a3ac454f5`.

- The recovery plan contains 2,735 missing orbit blocks in 195 chunks; the 20 durable source blocks are frozen and excluded from recomputation.
- 63 recovery chunk artifacts were available at the audit snapshot.
- All 63 downloaded recovery archives passed ZIP CRC checks; each had one successful chunk manifest, and all listed KEYMETA files matched their manifest SHA-256.
- Recovery artifacts contained 196 distinct orbit IDs, 23,531 manifest-declared columns, and no duplicate IDs within recovery outputs.
- Cross-check against the frozen source snapshot found no orbit-ID overlap.
- Combined source plus recovered partial output: 216 distinct blocks and 34,700 columns out of 2,755 blocks / 130,903 columns.
- Coverage by blocks: 7.84%; coverage by columns: 26.51%.
- Integrity errors in the 63 recovery artifacts: 0.
- At snapshot time, the workflow API reported 63 successful recovery jobs, 101 failed recovery jobs, 4 in progress, and 27 queued. The workflow had not produced a successful aggregate union gate.

The job-step summaries for representative failed jobs show the numerical replay step cancelled and the artifact-upload step skipped. Full logs could not be retrieved through the available GitHub log endpoint, so the precise failure cause is **not established**. Resource exhaustion is a hypothesis, not a verified diagnosis. The large discrepancy between block coverage and column coverage reflects the uneven multiplicity `m` of recovered orbit records; it is not evidence of rank or closure.

## Interpretation and limits

The original 20 durable blocks and the 63 recovered chunk artifacts are preserved and internally checksum-consistent. This does not independently validate the mathematical meaning of their contents, actual-q coverage, numerical rank, kernel dimension, or [3,2] closure.

Recovery must continue from the frozen assignment ledger, without altering frozen identities. Preserve successful artifacts, fill only missing orbit IDs, and fail closed on duplicate IDs or hash mismatches. Failed chunks should not be blindly treated as completed; investigate their execution failures and retry or subdivide only under the same frozen assignment contract.

The recovery workflow uses source run `39708640090`, bounded parallelism of 4, and a 360-minute per-chunk timeout. These are operational mitigations, not a guarantee that resource-related failures are resolved.

## Scientific claim boundary

`rank_certified = false`; `numerical_closure_claimed = false`.

No claim is made here about full 130,903-column coverage, global rank, Hamiltonian constraint closure, or the physical limit.
