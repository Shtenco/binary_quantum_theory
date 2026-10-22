# Depth-6 [3,2] KEYMETA artifact audit — 2026-10-22

## Scope

Audited durable GitHub Actions artifacts from authorized replay run [39708640090](https://github.com/Shtenco/binary_quantum_theory/actions/runs/39708640090), commit `3f44e5759385f91ec8c59530eaa3b96b00de65aa`.

This is an artifact-integrity audit, not a rank computation or proof of physical closure.

## Results

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

## Interpretation and limits

The 20 durable blocks are preserved and internally checksum-consistent. This does not independently validate the mathematical meaning of their contents, actual-q coverage, numerical rank, kernel dimension, or [3,2] closure.

The failed source workflow has no successful 112-shard aggregate. Remaining orbit records must be recovered from the frozen assignment ledger, without altering frozen identities. Recovery must retain these artifacts as a frozen source snapshot, fill only missing orbit IDs, and fail closed on duplicate IDs or hash mismatches.

The recovery workflow was adjusted to use source run `39708640090`, bounded parallelism of 4, and a 360-minute per-chunk timeout to reduce the risk of repeating the same high-concurrency failure pattern. These settings are operational mitigations, not a guarantee that resource-related failures are resolved.

## Scientific claim boundary

`rank_certified = false`; `numerical_closure_claimed = false`.

No claim is made here about full 130,903-column coverage, global rank, Hamiltonian constraint closure, or the physical limit.
