# Depth-6 [3,2] recovery audit — 2026-10-24

## Scope and method

Audited the frozen source artifacts from replay run [39708640090](https://github.com/Shtenco/binary_quantum_theory/actions/runs/39708640090) and the durable recovery artifacts from run [39743112374](https://github.com/Shtenco/binary_quantum_theory/actions/runs/39743112374), branch `bqg/depth6-32-canonical-recovery`.

The audit checks ZIP CRCs, manifest presence and totals, decodability of compressed KEYMETA payloads, unique orbit IDs, and recovery payload SHA-256 values against each chunk manifest. It is not a numerical-rank computation or proof of physical closure.

## Verified durable data

| Set | Archives | Distinct blocks | Manifest-declared columns |
|---|---:|---:|---:|
| Original frozen source | 20 | 20 | 11,169 |
| Recovery chunks | 63 | 196 | 23,531 |
| Combined partial union | 83 | 216 | 34,700 |
| Target | — | 2,755 | 130,903 |
| Still missing | — | 2,539 | 96,203 |

- Recovery artifacts downloaded and inspected: 63.
- Recovery ZIP CRC failures: 0.
- Missing or mismatched recovery manifest records: 0.
- Recovery payload SHA-256 mismatches: 0.
- Duplicate orbit IDs inside recovery artifacts: 0.
- Orbit IDs overlapping the original source set: 0.
- Total detected integrity errors across the inspected source and recovery archives: 0.
- Coverage: 7.84% of target blocks and 26.51% of target columns.

The block and column coverage percentages differ because orbit multiplicities are uneven. Neither percentage indicates numerical rank or constraint closure.

## Workflow state

The recovery run finished with overall conclusion `failure`; its aggregate job was skipped because the recovery matrix did not succeed. The planner had generated 195 chunks. Only 63 chunk artifacts are durable in this audit, so 132 planned chunk results remain unaccounted for in the durable output set.

Representative job-step summaries show the replay step cancelled and artifact upload skipped for some failed jobs. The available job-log endpoint returned a missing-blob response, so the precise cause of the cancellations is not established. Resource exhaustion or runner cancellation remains a hypothesis, not a verified root cause.

## Next action

Retry failed jobs from the existing run while preserving successful artifacts and the frozen ledger. After the retry, re-audit the complete artifact set and require exact coverage of all 2,755 frozen orbit blocks and 130,903 columns before permitting global peeling/SVD. Any union with duplicate IDs, missing records, or hash mismatches must fail closed.

## Scientific claim boundary

`rank_certified = false`; `numerical_closure_claimed = false`.

No claim is made here about full [3,2] rank, kernel dimension, Hamiltonian constraint closure, or the physical limit.
