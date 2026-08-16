# BCQG collective/refinement GR-universality killer gate — preregistration

**Purpose.** This is the next gate after the cutoff-saturated microscopic BCQG v1.2 core. The gate asks whether the same first-class structure survives blocking/refinement and enters a nondegenerate GR phase. It is an AND gate: no single spectral-dimension, HDA, or mode-count result can pass it alone.

## 1. Science target

A complete PASS requires, on the **same direct BCQG refinement family**,

\[
D_{space}\to3,\qquad c_{DW}\to\frac12,
\]

\[
(r_G,r_D,r_H,r_{extra})\to(3,3,1,0),
\]

\[
N_{phys}\to2,
\]

and

\[
\Delta^{collective}_{HH}\to0.
\]

The frozen local phase-space convention is the SU(2)-connection count `18` real canonical dimensions per generic bulk point/block. With no second-class constraints,

\[
N_{phys}^{config}=\frac{18-2(r_G+r_D+r_H+r_{extra})}{2}.
\]

Thus `(3,3,1,0)` gives exactly two local configuration modes.

## 2. Direct data requirement

A science verdict requires at least **four increasing refinement/block levels**. Every level must provide:

- `epsilon` — declared physical/block resolution parameter;
- `D_space_metric` — metric/volume-growth dimension measured from the collective geometry, not bare PL topology;
- either `c_DeWitt_eff` or a raw `6x6` kinetic Hessian in the frozen orthonormal symmetric-tensor basis;
- measured ranks `r_G,r_D,r_H,r_extra,r_secondclass`;
- `delta_HH_collective` from the collective Hamiltonian-constraint commutator against its collective diffeomorphism target.

Missing fields produce `INCOMPLETE`, never an inferred PASS.

## 3. DeWitt coefficient: non-circular extractor

Use the orthonormal symmetric-tensor basis

```text
xx, yy, zz, sqrt(2)xy, sqrt(2)xz, sqrt(2)yz.
```

For a local isotropic kinetic quadratic form

\[
K=A(\pi_{ab}\pi^{ab}-c\pi^2),
\]

the Hessian eigenvalues are

\[
\lambda_{TL}=2A\quad(5\;traceless\;directions),
\]

\[
\lambda_{tr}=2A(1-3c).
\]

Therefore the measured coefficient is extracted without fixing the GR target:

\[
\boxed{c_{eff}=\frac{1-\lambda_{tr}/\bar\lambda_{TL}}{3}}.
\]

The two finest levels must also have traceless-Hessian anisotropy and trace/traceless mixing below `0.05`; otherwise a single DeWitt parameter is not yet a valid effective description.

The existing ADM/DeWitt scripts establish that **if** a local ADM metric phase closes the standard HDA, its target is `c=1/2` and `AB=1`. Those controls are not substituted for the BCQG measurement above.

## 4. Frozen acceptance criteria

These thresholds are fixed before the direct collective data producer is run:

```text
minimum complete levels                  4
|D_space(finest)-3|                   <= 0.10
D target error: last-two mean <= first-two mean
|c_eff(finest)-1/2|                  <= 0.05
c target error: last-two mean <= first-two mean
traceless Hessian anisotropy          <= 0.05  (when Hessian supplied)
trace/traceless kinetic mixing        <= 0.05  (when Hessian supplied)
ranks on two finest levels              exactly (3,3,1,0)
second-class rank on two finest levels   exactly 0
N_phys on two finest levels              exactly 2
Delta_HH(finest)                        < 0.05
Delta_HH ~ epsilon^p                     p >= 0.50
```

The `p>=0.50` threshold tests actual decay while allowing collective corrections different from the microscopic leading `p~1`. It must not be widened after seeing results.

## 5. Controls that do NOT count as science data

The following are required protocol/target controls but cannot fill direct collective fields:

1. `collective_16cell_refinement_gate.py`: verifies the growing PL-S3 refinement carrier and local topological dimension 3.
2. `collective_volume_rg_gate.py` / extended ladder: verifies that representation blocking beyond `j=1/2` creates persistent nontrivial volume branches.
3. `collective_j1_block_isometry_gate.py`: exact two-carrier-per-face SU(2)/Gauss/volume fusion control. It is a minimal representation-blocking check, **not** the first canonical barycentric spatial block.
4. `collective_barycentric_tetra_block_gate.py`: finite tensor-network gate for the first canonical barycentric spatial tetra block.
5. `dewitt_hda_uniqueness_gate.py`: verifies the classical target `c=1/2` in its safe spectral window.
6. `adm_hda_parameter_selection_gate.py`: verifies standard HDA selects `c=1/2, AB=1` but not Newton normalization `A/B` or `Lambda`.
7. `dimension_emergence_gate.py`: minimal binary-diamond model is a negative dimension control and must not be promoted to the BCQG continuum geometry.
8. oracle-encoded Einstein reconstruction scripts are positive reconstruction controls only.

## 6. Canonical first spatial block and representation ladder

For any set of `n` parallel boundary spin-1/2 carriers, the fully symmetric SU(2) channel is

\[
(\tfrac12)^{\otimes n}_{sym}\longrightarrow j=n/2.
\]

The minimal `n=2 -> j=1` gate is useful because `j=1` is the first equal-spin four-valent representation where the absolute-volume operator is non-scalar. That is a representation-RG prerequisite only.

For the **canonical first barycentric subdivision of one coarse tetrahedron**, however, the combinatorics are fixed:

```text
24 fine tetrahedral chambers
36 internal dual links
24 boundary dual links
6 fine boundary triangles per coarse triangular face
```

Therefore the fully symmetric boundary channel of the canonical first spatial block is

\[
\boxed{(\tfrac12)^{\otimes6}_{sym}\to j=3}
\]

on each of four coarse faces, with a seven-dimensional four-`j=3` coarse Gauss intertwiner space.

The finite gate `collective_barycentric_tetra_block_gate.py` finds that the **static all-j=1/2 block projected to maximal symmetric j=3 on every face has rank-one image** in that seven-dimensional coarse singlet space. Its selected normalized intertwiner is

\[
\boxed{
\frac{1}{\sqrt{3241}}(7\sqrt5,0,-24,0,22\sqrt5,0,0)
}
\]

in the ordered coarse basis `K2=0,2,4,6,8,10,12`.

This finite rank-one result is a selection/obstruction, not a failure of the enlarged theory: the direct collective producer must retain production spin-changing sectors and/or non-maximal face irreps before attempting a generic GR tangent-space/Hessian/rank analysis. The static maximal-symmetric state alone is not allowed to stand in for six metric perturbation directions.

## 7. Required direct collective producer

For each refinement/block level `l`, construct a boundary collective isometry/effective embedding `W_l` from microscopic Peter-Weyl states to a collective block space. The operator-first compression is

\[
C_A^{(l)}=W_l^\dagger C_A W_l,
\]

with a separately reported leakage

\[
\eta_A^{(l)}=\|(1-W_lW_l^\dagger)C_AW_l\|.
\]

If leakage is not small, a Feshbach/Schrieffer-Wolff correction may be evaluated, but its prescription must be frozen before the science run.

The block space must be large enough that its measured kinetic tangent rank is not artificially fixed by the static rank-one maximal-symmetric sector. In particular, spin sectors reached by the frozen production `E`, Hermitian `S`, and route operator must be included according to a target-independent support rule.

On each level, the producer must then output:

1. a collective flux/metric observable and metric ball-volume dimension;
2. the kinetic Hessian of the effective scalar constraint about a declared nondegenerate homogeneous background;
3. the independent constraint-generator ranks from a singular-value decomposition with a preregistered relative rank tolerance;
4. the collective `[H[N],H[M]]` action and diffeomorphism target for the same smooth lapse family;
5. leakage and conditioning diagnostics.

No target value (`3`, `1/2`, rank tuple, `2`) may be used inside the construction or fit of those observables.

## 8. Failure semantics

- `PASS`: all five science targets pass simultaneously on the direct BCQG family.
- `FAIL`: a complete direct data set exists and at least one frozen criterion fails.
- `INCOMPLETE`: direct measurements are missing. Green topology/ADM controls do not upgrade this state.

A collective `FAIL` is scientifically meaningful and must not be repaired by deleting levels, changing the blocking map after looking at the target, fitting the DeWitt coefficient to `1/2`, removing extra constraints, or widening thresholds.

## 9. Current status

Already green prerequisites/controls:

- microscopic BCQG v1.2 core and HDA certificate;
- canonical PL-S3 refinement carrier;
- onset and persistence of nontrivial collective volume branches;
- exact minimal `j=1` representation fusion;
- explicit first barycentric tetra block geometry and its static rank-one maximal-symmetric selection rule;
- classical DeWitt/ADM target controls in the safe window (when run with their required Torch dependency).

**Science verdict remains `INCOMPLETE` until the direct dynamical collective effective-constraint producer supplies four-or-more complete levels.**
