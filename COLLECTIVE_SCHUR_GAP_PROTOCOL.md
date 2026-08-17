# BCQG collective Schur-gap closure protocol

## Purpose

The homogeneous six-edge gravitational carrier has an exact direct-block selection rule

\[
PCP=0,
\]

so the first physical low-energy scalar is a return/self-energy effect.  This protocol fixes how that return is converted into an effective operator **without fitting an energy denominator**.

It implements C2 of `BCQG_INTERNAL_CLOSURE_FRONTIER.md`.

## 1. Canonical split

Let `P` contain every state already classified as low energy and let `Q=1-P`.  On a finite target-independent Krylov block write the Hermitian scalar constraint as

\[
C=\begin{pmatrix}A&B\\B^\dagger&D\end{pmatrix},
\qquad A=PCP,\ B=PCQ,\ D=QCQ.
\]

For a zero-constraint state, eliminating a gapped `Q` sector gives the unique zero-energy Schur complement

\[
\boxed{C_{eff}=A-BD^{-1}B^\dagger.}
\]

On the frozen homogeneous gravitational carrier `A=0` before any promoted low-energy states are added.

No constant denominator, fitted gap, GR target coefficient or post-hoc regularizer is permitted.

## 2. Low-energy modes are promoted/classified, never inverted away

Diagonalize the Hermitian `D=QCQ` and define the normalized gap ratios

\[
r_i=|d_i|/\max_j|d_j|.
\]

The executable gate scans the frozen relative thresholds

```text
1e-9, 1e-10, 1e-11
```

before any GR comparison.

For each candidate low-energy eigenvector `v_i`, also report its normalized coupling to the retained carrier

\[
g_i=\|Bv_i\|/\|B\|_2.
\]

Rules:

1. if low-energy counts change across the threshold scan, return `THRESHOLD_UNSTABLE`; increase precision/refinement or inspect the sector;
2. if a stable low-energy mode has nonzero coupling to `P`, return `PROMOTE_LOW_ENERGY_MODES` and enlarge `P` before recomputing;
3. if a stable low-energy mode is decoupled from `P`, return `CLASSIFY_DECOUPLED_LOW_ENERGY_MODES`; it must be identified as gauge/matter/superselection or retained before internal closure;
4. only a residual coupled `Q` sector with no low-energy eigenvalue at the loosest frozen threshold is called `GAPPED_Q_SECTOR` and may be inverted for a closure PASS.

This prevents a hidden scalar/vector mode from being removed numerically merely because it is inconvenient.

## 3. Required diagnostics

For a gapped sector report:

- Hermiticity defect of `C` and `C_eff`;
- `min |d_i|`, `max |d_i|`, normalized gap and condition number of `QCQ`;
- Schur elimination residual in both projected equations;
- `P` dimension, `Q` dimension and any retained non-metric directions;
- coupling norm `||PCQ||`;
- metric/nonmetric mixing inside retained `P` when `dim(P)>6`;
- S4 covariance defect of the first six metric directions;
- the three raw metric-channel eigenvalues `kappa_A1,kappa_E,kappa_T2`.

The measured first-block metric calibration is external to this producer.  The blind GR discriminator

\[
\kappa_{A_1}:\kappa_E:\kappa_{T_2}=-\frac12:1:2
\]

is reported only as a diagnostic after the three channel values have been produced; it is never used to choose support, thresholds, promotion or the inverse.

## 4. S4 reduction

Use the fixed coarse-edge order

```text
(01),(02),(03),(12),(13),(23).
```

Let `O_opp` exchange opposite edges.  Then

\[
P_{A_1}=\frac16\mathbf1\mathbf1^T,
\]

\[
P_E=\frac12(I+O_{opp})-P_{A_1},
\]

\[
P_{T_2}=\frac12(I-O_{opp}).
\]

Their ranks are `1,2,3`.  A homogeneous scalar must reduce to

\[
C_{metric}=\kappa_{A_1}P_{A_1}+\kappa_EP_E+\kappa_{T_2}P_{T_2}
\]

up to the separately reported covariance defect.

Thus no production calculation needs 36 independently fitted metric matrix elements.

## 5. Closure criterion for one scale

A scale is `SCHUR_GAP_STAGE_PASS` only if:

- input Hermiticity passes;
- the residual `Q` sector is gapped at all frozen thresholds;
- Schur elimination residual is below tolerance;
- `C_eff` is Hermitian;
- S4 covariance/mixing diagnostics are reported, not silently averaged;
- no low-energy state remains unclassified outside `P`.

This is a **one-scale C2 certificate**, not yet the continuum result.  Internal closure additionally requires stability of the gap, retained carrier and metric-map conditioning under the frozen refinement family.

## 6. Executable controls

`scripts/collective_schur_gap_closure_gate.py --self-test` contains three non-science controls:

1. gapped `Q` sector with a known Schur complement: must recover it;
2. exact zero mode coupled to `P`: must refuse inversion and request promotion;
3. exact zero mode decoupled from `P`: must refuse closure until the mode is classified.

A future production file supplies the actual corrected `E+S+R_op` Krylov matrix; no synthetic matrix is evidence for BCQG dynamics.
