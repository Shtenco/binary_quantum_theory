# Depth-6 proof frontier recovery and [3,2] independent numerical witness

Date: 2026-10-01
Repository: `Shtenco/binary_quantum_theory`
Supersedes the mistaken frontier wording introduced by commit `36aa2cd48a7ae3b912cb729a2cfbe1618382e75a`.
Canonical finite-depth inputs include the 2026-09-29 branch-sum checkpoints and the 2026-10-01 `[2,1,1,1]` master certificate.

## 1. Purpose

This document restores the correct depth-6 theorem boundary.

`[3,2]` is **not** a new structural target. Its corrected K5 depth-6 structural/branch-sum proof was already closed on 2026-09-29:

```text
irrep                         = [3,2]
active blocks                 = 2755 / 2755
multiplicity-space columns    = 130903 / 130903
remaining blocks              = 0
remaining columns             = 0
structural status             = CLOSED
```

The only unfinished `[3,2]` task is the **independent numerical master-rank witness**. Therefore all already-certified shell, orbit, Jucys, branching, support/capacity and structural peeling work is immutable input and MUST NOT be recomputed merely to continue the proof.

The corrected target sequence is:

```text
preserve already-closed evidence
  -> synchronize canonical depth6 truth
  -> freeze [2,1,1,1] as CLOSED_FINITE_NUMERICAL
  -> freeze [3,2] structural certificate as CLOSED
  -> recover all surviving [3,2] numerical checkpoints / Actions artifacts
  -> validate recovered evidence against immutable 130903-column ledger
  -> compute only missing numerical master witness pieces
  -> quarantine genuinely unresolved numerical subspace
  -> assemble residual full master Gram only where needed
  -> independent true-kernel check only if a near-null vector survives
  -> close [3,2] numerically or report the exact unresolved numerical state
```

## 2. Scientific claim boundaries

### 2.1 `[2,1,1,1]`

The canonical finite statement is:

```text
scope: corrected K5 depth-6 S4-sign multiplicity space
status: CLOSED_FINITE_NUMERICAL
```

with:

```text
ker H0 = K16
dim K16 = 16
rank H0 | K16^perp = 130096 / 130096
rank H1 | K16 = 16 / 16
sigma_min(H1 | K16) = 1.1304521906426825
```

and hence:

```text
ker M | S4-sign = 0
[2,1,1,1] multiplicity dimension 103318 -> empty kernel
```

This is a finite numerical rank certificate, not an all-depth, continuum, rigging-map, physical-propagator or experimental theorem.

### 2.2 `[3,2]`

The canonical structural statement is already:

```text
multiplicity-space dimension = 130903
active S5 orbit blocks       = 2755
structural blocks            = 2755 / 2755
structural columns           = 130903 / 130903
structural remainder         = 0
structural status            = CLOSED
```

The exact S5 -> S4 branch identity is frozen:

```text
[3,2] -> [3,1] + [2,2]
B32 = 3 A31 + 2 A22
```

Equivalently:

```text
C32 = [sqrt(3) H31 ; sqrt(2) H22]
B32 = C32^dagger C32
ker B32 = ker H31 intersect ker H22
```

The existing vertex/S3 master-row identity

```text
B = A0 + A1 + 3 A2
```

is a compatible implementation-level decomposition of the same positive master object. It is not a replacement for the S4 branching statement and is not a reason to reopen structural proof.

The historical 2026-09-29 numerical checkpoint was **partial**, not negative. H0-only probes found local rank deficits on some blocks; this established only that H0 by itself was an insufficient certificate. It did not establish a master-constraint kernel. The numerical continuation must therefore use the complete declared positive master map or an equivalent independently verified stacked map.

## 3. Immutable depth-6 structural ledger

The mixed-sector branch-sum structural certificates are frozen inputs:

```text
[3,2]       2755/2755 blocks   130903/130903 columns   remaining 0
[3,1,1]     2719/2719 blocks   153455/153455 columns   remaining 0
[2,2,1]     2749/2749 blocks   130503/130503 columns   remaining 0
[2,1,1,1]   2712/2712 blocks   103318/103318 columns   remaining 0
```

Thus structural/combinatorial capacity is already closed for all seven depth-6 S5 irreps.

This means the following are **DO_NOT_RECOMPUTE** for `[3,2]` unless an explicit integrity check detects corruption:

```text
depth-6 shell enumeration
264962 spin assignments
2757 S5 orbit enumeration
[3,2] multiplicity 130903
2755 active [3,2] blocks
S3/J4/J5 Jucys selector construction
S5 -> S4 branching identity
structural support graph
structural capacity ledger
structural peeling / matching proving 130903/130903 coverage
universal branch transporter regressions already certified
```

Integrity verification of hashes/counts is allowed. Recomputing the mathematical search is not the default continuation path.

## 4. Canonical status after correction

Canonical status must distinguish structural closure from numerical master closure.

```text
NUMERICALLY CLOSED / finite master witness:
  [1^5]
  [5]          (non-vacuum sector; zero-spin vacuum line treated separately)
  [4,1]
  [2,1,1,1]

STRUCTURALLY CLOSED, independent numerical master witness still to recover/finish:
  [3,2]
  [3,1,1]
  [2,2,1]

STRUCTURAL DEPTH-6 STATUS:
  CLOSED_FOR_ALL_7_S5_IRREPS

FULL FINITE DEPTH-6 MASTER THEOREM:
  NOT_YET_PROVED

CURRENT NUMERICAL WITNESS TARGET:
  [3,2]
```

The phrase `next_frontier = [3,2]` is forbidden when it can be read as reopening structural work. Use instead:

```text
next_numeric_witness = [3,2]
[3,2].structural_status = CLOSED
[3,2].numerical_master_status = RECOVER_OR_FINISH
```

## 5. Recovery-first rule for `[3,2]`

Before launching any new expensive calculation, recover existing evidence in this order:

1. GitHub Actions runs for the mixed Stage-A workflow, including failed/cancelled runs.
2. Per-shard artifacts and aggregate artifacts from those runs.
3. Repository checkpoints on historical/research branches.
4. Canonical Library/project checkpoints already produced during the 2026-09-29 calculation.
5. Only after deduplication and validation, recompute numerical pieces that are genuinely absent.

Every recovered artifact must be checked against:

```text
irrep = [3,2]
input dimension = 130903
active blocks = 2755
source/proof-engine commit
block ids / column ranges
hash or deterministic content identity when available
```

Recovered numerical evidence may be reused only if its operator convention matches the frozen master definition.

## 6. Known partial numerical checkpoint

The 2026-09-29 `[3,2]` numerical checkpoint is retained as historical evidence:

```text
runner = PROBE_SELECTOR_V1
processed blocks = 825
H0-only pass blocks = 500
H0-only unresolved blocks = 325
H0-only certified columns = 3293
```

Representative H0-only deficits included:

```text
block 705   rank 6/10
block 1018  rank 2/6
block 2145  rank 2/6
block 2150  rank 2/6
block 2182  rank 12/20
block 2183  rank 12/20
block 2205  rank 9/23
block 2480  rank 9/23
```

Interpretation is frozen:

```text
H0-only rank deficiency != master-constraint kernel
```

Any continuation which treats those deficits as a physical/algebraic nullspace without applying the missing master components is invalid.

A later live checkpoint also recorded a dynamic master numerical run with committed progress. That progress must be recovered and merged before new work is scheduled.

## 7. Numerical witness architecture

### 7.1 Reuse before recompute

The numerical pipeline starts from a recovery manifest, not from shell/orbit generation.

Create a coverage ledger over the immutable 130903 domain columns:

```text
RECOVERED_STRONG
RECOVERED_UNRESOLVED
MISSING_NUMERICAL_EVIDENCE
```

No column may appear in more than one final class. The ledger must satisfy:

```text
recovered_strong
+ recovered_unresolved
+ missing_numerical_evidence
= 130903
missing_or_duplicate_domain_columns = 0
```

### 7.2 Full positive master map

For columns not already covered by a valid recovered numerical witness, use either the exact branch-stacked map

```text
C32 = [sqrt(3) H31 ; sqrt(2) H22]
```

or the independently regression-tested equivalent generic master map. Preserve sufficient branch/vertex metadata to verify equivalence.

### 7.3 Robust main witness

Recovered and newly calculated well-conditioned pieces may form a main injectivity witness. Record:

```text
blocks
columns
operator convention
selected output channels
rank tolerance
minimum selected sigma
median selected sigma
1% quantile selected sigma
independence/disjointness condition
provenance per chunk
```

Matching or peeling is only a sufficient certificate mechanism. A failure of that mechanism is not evidence of an operator kernel.

### 7.4 Residual/quarantine only for unresolved numerical columns

Construct:

```text
V32 = V_main direct-sum V_residual
```

with:

```text
main_columns + residual_columns = 130903
missing_columns = 0
duplicate_columns = 0
```

`V_residual` contains only columns whose independent numerical injectivity has not already been certified.

Do **not** rebuild a residual merely because a structural matcher once encountered a weak edge. Structural coverage is already closed.

### 7.5 Residual full master Gram

For the genuinely unresolved residual subspace construct the complete declared master map:

```text
C_residual
G_residual = C_residual^dagger C_residual
```

Record:

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

If `lambda_min` is safely positive relative to numerical uncertainty, the residual is injective and `[3,2]` closes numerically.

## 8. True-kernel gate and H2 rule

A small singular value, failed local selector or failed matching is not a true kernel.

If a residual vector is compatible with null numerically:

1. extract the candidate vector;
2. reconstruct the full `[3,2]` master action independently;
3. apply every required branch/vertex component;
4. report normalized component residuals;
5. repeat the weakest calculation with an independent numerical route where practical.

Only if the candidate survives the complete independent check may the workflow set:

```text
true_residual_kernel = true
h2_null_lift_allowed = true
```

Otherwise:

```text
true_residual_kernel = false
h2_null_lift_allowed = false
```

Canonical rule:

```text
TRUE independently verified master kernel -> H2/null-lift allowed
anything weaker                           -> H2/null-lift forbidden
```

## 9. Decision states

The numerical continuation must be fail-closed:

```text
PASS_CLOSED_FINITE_NUMERICAL
RECOVERED_PARTIAL_NUMERICAL_EVIDENCE
RESIDUAL_POSITIVE_BUT_UNVERIFIED
RESIDUAL_NEAR_NULL_REQUIRES_INDEPENDENT_CHECK
TRUE_KERNEL_CONFIRMED
CERTIFICATE_INCOMPLETE
INPUT_COVERAGE_FAILURE
NUMERICAL_INCONCLUSIVE
```

Only `PASS_CLOSED_FINITE_NUMERICAL` changes `[3,2].numerical_master_status` to `CLOSED_FINITE_NUMERICAL`.

`[3,2].structural_status` remains `CLOSED` regardless of a numerical-certificate failure unless the immutable structural certificate itself is separately falsified.

## 10. Output certificate

A successful final numerical certificate should be named:

```text
BQG_DEPTH6_32_MASTER_CLOSED_2026-10-XX.json
```

and include:

```text
schema_version
status_date
status
scope
source structural checkpoint(s)
source numerical runs / artifacts
source commit(s)
proof-engine commit
artifact hashes / manifest
input dimension = 130903
active blocks = 2755
structural_status = CLOSED
branch identity B32 = 3 A31 + 2 A22
recovered evidence summary
newly computed evidence summary
main witness summary
residual sparse certificate
independent recompute result
kernel dimension
irrep consequence
remaining numerical depth6 irreps
full depth6 theorem status
claim boundary
```

The certificate must make it impossible to mistake structural recomputation for new numerical evidence.

## 11. CI architecture

The current mixed Stage-A workflow must not force a fresh structural proof before numerical continuation.

CI for `[3,2]` should check separately:

1. immutable structural checkpoint integrity;
2. exact `2755` block / `130903` column ledger;
3. recovered artifact provenance and non-overlap;
4. master-map convention regression;
5. main/residual partition integrity;
6. residual spectral residuals;
7. final numerical status semantics;
8. no H2 path unless `true_residual_kernel == true`.

Existing generic numerical shard generation may be reused for missing chunks, but orchestration should be recovery-aware: schedule only absent or invalid numerical chunks whenever the previous artifacts provide valid reusable evidence.

## 12. Numerical reproducibility

Every proof run must record:

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

The general repository `requirements.txt` may remain broad for development, but final numerical proof artifacts require a frozen or fully recorded environment.

## 13. Testing strategy

Before accepting `[3,2]` numerical closure:

- verify the immutable structural `2755/2755`, `130903/130903`, remainder `0` checkpoint;
- verify branch/master-row regression;
- verify recovered artifact hashes and coverage;
- reject duplicated or missing domain columns;
- reject operator-convention mismatches;
- test that H0-only deficiency is not promoted to a master kernel;
- test that matching failure is not promoted to a master kernel;
- test the true-kernel/H2 gate;
- compile all changed Python sources;
- validate canonical frontier semantics;
- require the dedicated `[3,2]` numerical certificate, not merely generic core CI.

## 14. Corrected execution order

```text
P0. correct the erroneous 36aa2cd frontier wording                         DONE by superseding commit
P0. preserve [2,1,1,1] numerical evidence                                 ACTIVE
P0. synchronize [2,1,1,1] canonical truth                                 ACTIVE
P0. freeze [3,2] structural 2755/2755, 130903/130903 as immutable          DONE historically
P1. inventory old [3,2] Actions runs/checkpoints/artifacts                 CURRENT
P2. build recovery manifest and exact numerical coverage ledger            NEXT
P3. validate/reuse surviving numerical chunks                              NEXT
P4. schedule only genuinely missing numerical chunks                       NEXT
P5. build main/residual numerical witness                                  NEXT
P6. residual Gram and independent near-null gate if needed                 NEXT
P7. issue [3,2] finite numerical master certificate                        NEXT
P8. then continue independent numerical witnesses for [2,2,1]/[3,1,1]     LATER
```

No structural `[3,2]` shell/orbit/Jucys/matching/capacity rerun is part of this continuation.

## 15. Success criteria

The correction/continuation succeeds when:

1. no canonical document calls `[3,2]` structurally open;
2. `[3,2]` structural status remains `CLOSED` with `2755/2755`, `130903/130903`, remainder `0`;
3. the numerical continuation begins from recovered evidence rather than zero;
4. every reused chunk has explicit provenance and coverage;
5. only genuinely missing numerical work is recomputed;
6. certificate failure cannot be misreported as an operator kernel;
7. H2/null-lift cannot run without a separately confirmed true residual kernel;
8. a future numerical PASS contains sufficient provenance/environment/hash data for independent reproduction;
9. the repository continues to distinguish finite depth-6 closure from continuum/refinement physicalization.
