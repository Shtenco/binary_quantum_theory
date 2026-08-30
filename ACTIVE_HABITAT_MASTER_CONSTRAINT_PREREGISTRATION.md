# Leakage-aware active-habitat master constraint — preregistration

Status: **finite Euclidean three-node research diagnostic; not a physical projector or continuum rigging map.**

## Purpose

The current graph-changing Peter-Weyl Hamiltonian deliberately retains outputs outside the original all-`j=1/2` sector.  A physicalization calculation must therefore not replace the full action `H_v P` by `P H_v P` before the lost norm has been measured.

For the frozen three-node Euclidean family `v in {0,1,2}`, define the one-hit active habitat

\[
\mathcal H_{P_1}=\operatorname{span}\{\psi_0,H_0\psi_0,H_1\psi_0,H_2\psi_0\},
\]

with orthogonal projector `P1` obtained numerically from the actual sparse Peter-Weyl states by reorthogonalized modified Gram-Schmidt.

For every retained node constraint define

\[
C_v=P_1H_vP_1,
\qquad
L_v=(1-P_1)H_vP_1.
\]

The **safe restricted master quadratic form** is

\[
\boxed{
M_{P_1}^{full}=\sum_v (H_vP_1)^\dagger(H_vP_1).
}
\]

The projected shortcut is

\[
M_{P_1}^{proj}=\sum_v C_v^\dagger C_v.
\]

Because `P1` is orthogonal, the exact finite identity is

\[
\boxed{
M_{P_1}^{full}-M_{P_1}^{proj}
=\sum_v L_v^\dagger L_v\succeq0.
}
\]

This identity is the central preregistered gate.  It quantifies exactly how much information is discarded by projecting graph-changing outputs back into the one-hit habitat.

## Frozen construction

- initial state: first state returned by `basis_full_jhalf()`;
- nodes: `0,1,2`;
- Euclidean Hamiltonian implementation: `k5_peter_weyl_safe_hda_column.apply_H_cached_state`;
- doubled-spin cutoff: `JMAX2=5` (`Jmax=5/2`), matching the existing three-node graph-changing HDA control;
- sparse pruning threshold: `1e-8`;
- active basis: seed plus the three actual one-hit states, no target-dependent basis enlargement;
- no GR ratio, TT coefficient or experimental datum enters basis construction, thresholds or PASS criteria.

## Required numerical checks

A PASS of the diagnostic requires only implementation identities and conditioning checks:

1. the active basis is nonempty and orthonormal to the frozen tolerance;
2. all three single-node actions on the seed are nonzero;
3. all constructed matrices are finite;
4. each full image Gram matrix and the full master matrix are positive semidefinite up to numerical roundoff;
5. the decomposition

   `M_full - M_projected = sum_v L_v^dagger L_v`

   holds to the frozen relative tolerance;
6. `M_full - M_projected` agrees with the independently accumulated leakage Gram matrix;
7. the master and leakage matrices are Hermitian to tolerance.

The amount of leakage, the kernel rank and the spectral distortion are **results**, not acceptance targets.

## Mandatory diagnostics

The result must report:

- active-habitat dimension and orthonormality defect;
- one-hit supports and norms;
- for every node, full action norm, projected action norm, leakage operator norm and leakage ratio;
- `M_full`, `M_projected` and `M_leak` spectra;
- threshold scans of apparent zero-mode counts;
- whether the projected shortcut creates additional apparent zero modes;
- relative spectral distortion between `M_full` and `M_projected`;
- decomposition residual;
- a fail-closed `science_status` distinguishing leakage present from an actually closed one-hit habitat.

## Interpretation

If leakage is nonzero, this does **not** fail the physics.  It proves that the one-hit habitat is not invariant and that a master constraint must be built from full images or on an enlarged active cone.

If a projected master has a larger apparent kernel than `M_full`, that is direct evidence that `P H P` would manufacture spurious physical states.

Even if the one-hit habitat happens to close, this finite result does not establish the theory-specific physical projector.  Full five-node/Lorentzian constraints, refinement stability, boundary/history data and the continuum rigging-map problem remain separate gates.

## Claim boundary

This research gate may establish only:

```text
finite three-node Euclidean one-hit habitat
+ exact leakage accounting
+ safe restricted master quadratic form.
```

It may not be cited as a derivation of physical time, a continuum physical Hilbert space, the graviton propagator, the six Wilson coefficients or experimental quantum gravity.
