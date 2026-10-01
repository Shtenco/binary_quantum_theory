# Depth-6 proof frontier closure and [3,2] master-rank pipeline

Date: 2026-10-01
Repository: `Shtenco/binary_quantum_theory`
Canonical base commit at design time: `9de8df36c34f0a39305f28bd09ec6496ad954473`

## 1. Purpose

This change moves the finite corrected K5 depth-6 programme from the now-closed S4-sign sector `[2,1,1,1]` to the first remaining mixed irrep `[3,2]`, while repairing repository truth/provenance so that machine-readable status, documentation, CI and proof artifacts all describe the same theorem boundary.

The design is intentionally fail-closed. It must never turn a structural or matching failure into a claimed operator kernel, and it must never reopen the historical H2/null-lift route unless a residual vector survives an independent application of the complete declared master map.

The target sequence is

```text
preserve [2,1,1,1] evidence
  -> synchronize canonical depth6 truth
  -> freeze [2,1,1,1] as CLOSED_FINITE_NUMERICAL
  -> build [3,2] branch-q rank map
  -> robust capacitated matching
  -> quarantine weak/conflicting columns
  -> assemble small residual master Gram
  -> independent true-kernel check only if needed
  -> close [3,2] or report a verified residual kernel
```

## 2. Scientific claim boundaries

### 2.1 `[2,1,1,1]`

The canonical finite statement is

```text
scope: corrected K5 depth-6 S4-sign multiplicity space
status: CLOSED_FINITE_NUMERICAL
```

with the certified decomposition

```text
ker H0 = K16
dim K16 = 16
rank H0 | K16^perp = 130096 / 130096
rank H1 | K16 = 16 / 16
sigma_min(H1 | K16) = 1.1304521906426825
```

and therefore

```text
ker M | S4-sign = 0
[2,1,1,1] dimension 103318 -> rank 103318 -> empty kernel
```

This is a finite numerical rank certificate with a large conditioning margin. It is not promoted to an all-depth, continuum, rigging-map, physical-propagator or experimental theorem.

### 2.2 `[3,2]`

The next target is

```text
irrep: [3,2]
multiplicity-space dimension: 130903
active S5 orbit blocks: 2755
```

The S5 -> S4 branching identity is frozen as

```text
[3,2] -> [3,1] + [2,2]
B32 = 3 A31 + 2 A22
```

Equivalently the positive stacked map is

```text
C32 = [sqrt(3) H31 ; sqrt(2) H22]
B32 = C32^dagger C32
ker B32 = ker H31 intersect ker H22
```

The existing vertex/S3 reduction

```text
B = A0 + A1 + 3 A2
```

is a compatible decomposition of the same positive master object and remains available as an implementation-level route. It must not be confused with the S4 branch identity.

## 3. P0 provenance and artifact preservation

The `[2,1,1,1]` master certificate references source workflow run `36527314863`, source head SHA `5cefb20906e1d0a95d9abc06c038fcdae026235c`, and 128 `bqg-s4sign-v2-shard-*` Actions artifacts. Those artifacts are temporary and must not remain the sole carrier of the source maps.

The repository already contains `.github/workflows/bqg-depth6-s4sign-aggregate-existing.yml`, which downloads all 128 canonical shards and verifies their count. The preservation change should reuse that exact ingestion path rather than introduce a second downloader.

Required preservation output:

```text
BQG_DEPTH6_S4SIGN_SOURCE_RUN_36527314863/
  artifacts.tsv
  sha256_manifest.txt
  source_run.json
  shard_bundle.tar.gz (or tar.zst if runner/tooling is frozen)
```

`source_run.json` must record at least:

```text
repository
source_run_id
source_head_sha
source_branch
expected_shards = 128
artifact names
artifact ids
GitHub artifact digest when available
bundle digest
creation timestamp
```

The bundle must be copied to a storage location whose lifetime is independent of the original 2-3 day Actions retention. The preservation operation is evidence handling only; it must not change any theorem status.

## 4. Canonical truth synchronization

After evidence preservation, the following surfaces must agree:

- `BQG_DEPTH6_2111_MASTER_CLOSED_2026-10-01.json`
- `depth6_frontier.json`
- `scripts/verify_depth6_frontier.py`
- `THEORY_STATUS.md`
- `OPEN_PROBLEMS.md`
- `CANONICAL_THEORY_PACKAGE.md`
- `.github/workflows/bqg-depth6-s4sign-aggregate.yml`
- `.github/workflows/bqg-depth6-mixed-stage-b-final.yml`
- any README status block that still names the obsolete 130007 x 130007 minor as the active blocker

The old giant-minor route remains historical evidence but is no longer the canonical blocker.

The canonical depth-6 status after synchronization must be

```text
CLOSED:
  [1^5]
  [5]
  [4,1]
  [2,1,1,1]

OPEN:
  [3,2]
  [3,1,1]
  [2,2,1]

finite_depth6_full_theorem_status = NOT_YET_PROVED
next_frontier = [3,2]
```

The verifier must fail if any public/canonical surface attempts to restore `[2,1,1,1]` to `ACTIVE_NOT_CLOSED` without explicitly superseding the 2026-10-01 certificate.

## 5. `[3,2]` proof architecture

### 5.1 Input map

Reuse the current generic selector/master machinery and exact coverage ledger:

```text
shell states = 264962
S5 orbits = 2757
active [3,2] blocks = 2755
columns = 130903
```

Each active orbit block produces domain columns and an output map keyed by symmetry-resolved output channels. The new aggregator must preserve enough branch metadata to distinguish `[3,1]` and `[2,2]` contributions when constructing local capacities and certificates.

### 5.2 Local branch-q ranks

For each `(branch, q, orbit-block)` contribution compute a local rank certificate. The certificate must include:

```text
rows
columns
rank
rank tolerance
sigma_min on the certified local image
source block id
branch id
q id
```

Row count alone is not a capacity certificate. Matching capacity is bounded by certified numerical rank.

A local block with weak conditioning is not discarded; it is tagged for quarantine/residual handling.

### 5.3 Robust capacitated matching

Construct a bipartite capacity problem:

```text
left: domain rank units / columns grouped by S5 orbit block
right: symmetry-resolved (branch,q) output channels
right capacity: certified local independent row/rank capacity
```

The primary objective is full coverage. The secondary objective is conditioning: among full/near-full feasible assignments, prefer assignments whose bottleneck local singular value is largest and that reduce collision pressure on channels needed by difficult blocks.

A matching certificate is only a sufficient injectivity witness for the selected main subspace. Failure to find a full matching is not evidence of an operator kernel.

### 5.4 Main witness and quarantine

Split the 130903-dimensional domain as

```text
V32 = V_main direct-sum V_residual
```

with exact coverage guards:

```text
main_columns + residual_columns = 130903
missing_columns = 0
duplicate_columns = 0
```

`V_main` contains columns covered by a robust, row-disjoint/rank-certified witness. `V_residual` contains weak, colliding, unmatched or deliberately quarantined columns.

The main certificate must record at least:

```text
blocks
columns
selected output channels
minimum selected sigma
median selected sigma
1% quantile selected sigma
row/channel disjointness or the exact generalized independence condition used
```

### 5.5 Residual full master map

For the residual subspace build the complete declared stacked master map, not only the channels selected by matching:

```text
C_residual
G_residual = C_residual^dagger C_residual
```

The residual certificate must record

```text
residual blocks
residual columns
rows
nnz
smallest several Gram eigenvalues
relative eigen residuals
sigma_min = sqrt(lambda_min)
rank tolerance
condition estimate when meaningful
```

If `lambda_min` is safely positive compared with numerical error and tolerance, `[3,2]` closes.

## 6. True-kernel gate and H2 rule

If the residual calculation produces `lambda_min` compatible with zero, the system must not immediately launch H2/null-lift logic.

First extract candidate null vectors and apply the complete independently reconstructed `[3,2]` master map to them. The independent check must use a separately assembled path where practical and must report normalized residuals for every required branch/vertex component.

Only if a candidate survives this check as a genuine operator kernel may the workflow set

```text
true_residual_kernel = true
h2_null_lift_allowed = true
```

Otherwise the failure is classified as a certificate/matching/numerical failure, not a physical or algebraic kernel.

Canonical rule:

```text
TRUE residual kernel -> null-lift/H2 allowed
anything weaker       -> null-lift/H2 forbidden
```

## 7. `[3,2]` decision states

The new aggregator must have explicit fail-closed states:

```text
PASS_CLOSED_FINITE_NUMERICAL
RESIDUAL_POSITIVE_BUT_UNVERIFIED
RESIDUAL_NEAR_NULL_REQUIRES_INDEPENDENT_CHECK
TRUE_KERNEL_CONFIRMED
CERTIFICATE_INCOMPLETE
INPUT_COVERAGE_FAILURE
NUMERICAL_INCONCLUSIVE
```

Only `PASS_CLOSED_FINITE_NUMERICAL` may update the canonical frontier to `[3,2] = CLOSED`.

## 8. Output certificate

The final file should be named along the lines of

```text
BQG_DEPTH6_32_MASTER_CLOSED_2026-10-XX.json
```

and contain:

```text
schema_version
status_date
status
scope
source_commit
proof_engine_commit
artifact manifest hash
input dimension
active block count
branch identity
local-rank protocol
main witness summary
residual sparse certificate
independent recompute result
kernel dimension
irrep consequence
remaining depth6 irreps
full depth6 theorem status
claim boundary
```

All large intermediate artifacts must have hashes in the certificate even when they are stored outside git.

## 9. CI architecture

The current mixed Stage A requires the streaming peeler to certify all 130903 columns directly. That requirement should be replaced for `[3,2]` by the new two-level certificate:

```text
main robust witness + residual Gram + independent near-null gate
```

CI must separately check:

1. exact input coverage;
2. branch-reduction regression;
3. local-rank certificate integrity;
4. main/residual partition integrity;
5. residual spectral residuals;
6. final status semantics;
7. no H2 path unless `true_residual_kernel == true`.

The existing generic shard generation can remain unchanged unless branch metadata cannot be reconstructed losslessly at aggregation time.

## 10. Numerical reproducibility

Proof runs must record the numerical environment. A dedicated proof environment manifest should freeze or record:

```text
Python version
numpy version
scipy version
sympy version
BLAS/LAPACK implementation
platform/architecture
OMP_NUM_THREADS
OPENBLAS_NUM_THREADS
MKL_NUM_THREADS
```

The general repository `requirements.txt` may remain broad for ordinary development, but depth-6 proof certificates must not rely only on unbounded future dependency upgrades.

## 11. Testing strategy

Before accepting any truth update:

- run the existing branch/master-row regression;
- verify the old `[2,1,1,1]` certificate is still accepted;
- add negative tests showing that malformed coverage, duplicated columns, missing channels and a fake near-null residual fail closed;
- test that matching failure without an operator null vector does not set `TRUE_KERNEL_CONFIRMED`;
- test that H2 entry is rejected unless the independent true-kernel flag is present;
- compile all changed Python sources;
- run `scripts/verify_depth6_frontier.py` against the synchronized ledger;
- run the canonical status/documentation validation touched by the change.

A green generic core regression is not by itself sufficient to certify `[3,2]`; the dedicated depth-6 certificate must pass.

## 12. Execution order

Implementation order is frozen as:

```text
P0. preserve source evidence
P0. synchronize canonical `[2,1,1,1]` truth
P1. add tests/status enums for new `[3,2]` pipeline
P2. implement branch-q local-rank extraction
P3. implement robust capacitated matching
P4. implement quarantine/main-residual partition
P5. implement residual sparse Gram + spectral certificate
P6. implement independent true-kernel gate
P7. wire dedicated `[3,2]` CI
P8. run `[3,2]`
P9. if PASS, update frontier; otherwise preserve exact failure state
```

No work on `[3,1,1]`, `[2,2,1]`, continuum physicalization or 2T is part of this implementation until `[3,2]` reaches a stable decision state.

## 13. Success criteria

The change is successful when all of the following are true:

1. the 2026-10-01 `[2,1,1,1]` proof evidence cannot disappear solely because the original Actions artifacts expire;
2. every canonical status surface agrees that `[2,1,1,1]` is closed only in its finite numerical scope;
3. the old 130007 x 130007 minor is historical rather than an active blocker;
4. `[3,2]` has a deterministic fail-closed pipeline with exact 130903-column coverage;
5. certificate failure cannot be misreported as an operator kernel;
6. H2/null-lift cannot run without a separately confirmed true residual kernel;
7. a future PASS certificate contains enough provenance, numerical environment and artifact hashes for independent reproduction.
