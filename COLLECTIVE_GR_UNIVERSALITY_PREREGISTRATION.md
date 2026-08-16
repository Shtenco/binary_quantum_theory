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
2. `collective_volume_rg_gate.py` / extended ladder: verifies that blocking beyond `j=1/2` creates persistent nontrivial volume branches.
3. `dewitt_hda_uniqueness_gate.py`: verifies the classical target `c=1/2` in its safe spectral window.
4. `adm_hda_parameter_selection_gate.py`: verifies standard HDA selects `c=1/2, AB=1` but not Newton normalization `A/B` or `Lambda`.
5. `dimension_emergence_gate.py`: minimal binary-diamond model is a negative dimension control and must not be promoted to the BCQG continuum geometry.
6. oracle-encoded Einstein reconstruction scripts are positive reconstruction controls only.

## 6. First blocking ladder already fixed

For each face, the first symmetric collective map is

\[
(\tfrac12)^{\otimes n}_{sym}\longrightarrow j=n/2.
\]

At a four-valent node the singlet intertwiner dimension is `2j+1`. The microscopic `j=1/2` absolute-volume operator is scalar, while `j=1` is the first representation with nontrivial volume spectrum. The extended finite ladder through `j=5/2` is a prerequisite/control for the effective-geometry producer; it is not itself GR emergence.

## 7. Required direct collective producer

For each refinement/block level `l`, construct a boundary collective isometry `W_l` from microscopic Peter-Weyl states to a collective block space. The recommended operator-first compression is

\[
C_A^{(l)}=W_l^\dagger C_A W_l,
\]

with a separately reported leakage

\[
\eta_A^{(l)}=\|(1-W_lW_l^\dagger)C_AW_l\|.
\]

If leakage is not small, a Feshbach/Schrieffer-Wolff correction may be evaluated, but its prescription must be frozen before the science run.

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

## 9. Current status at preregistration

Already green prerequisites/controls:

- microscopic BCQG v1.2 core and HDA certificate;
- canonical PL-S3 refinement carrier;
- onset and persistence of nontrivial collective volume branches;
- classical DeWitt/ADM target controls in the safe window.

**Science verdict remains `INCOMPLETE` until the direct collective effective-constraint producer supplies four-or-more complete levels.**
