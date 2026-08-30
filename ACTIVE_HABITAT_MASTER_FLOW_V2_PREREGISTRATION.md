# Active-habitat master-gap flow v2 — preregistration

Status: **finite Euclidean three-node research diagnostic; not a physical projector, rigging map, continuum limit, graviton theorem or phenomenological prediction.**

## Motivation fixed before v2 is run

The preregistered v1 one-hit calculation found material graph-changing leakage while preserving the exact positive decomposition

\[
M^{\rm full}_{P_1}-M^{\rm proj}_{P_1}
=\sum_v[(1-P_1)H_vP_1]^\dagger[(1-P_1)H_vP_1]\succeq0.
\]

The numerical amount of v1 leakage is already known, but **no v2 result is known at the time this document is committed**.  Therefore the depth-2 basis construction and the acceptance criteria below are frozen now and will not depend on the eventual v2 spectrum, gap or leakage.

## Frozen nested habitats

Use exactly the same initial state, Hamiltonian implementation, node set, spin cutoff and sparse pruning convention as v1:

- seed `psi0`: first state returned by `basis_full_jhalf()`;
- nodes `v in {0,1,2}`;
- Hamiltonian: `k5_peter_weyl_safe_hda_column.apply_H_cached_state`;
- `JMAX2=5` (`Jmax=5/2`);
- sparse pruning threshold `1e-8`;
- reorthogonalized modified Gram-Schmidt with the v1 frozen linear-dependence tolerance.

Define

\[
P_0=\operatorname{span}\{\psi_0\},
\]

\[
P_1=\operatorname{span}\{\psi_0,H_0\psi_0,H_1\psi_0,H_2\psi_0\}.
\]

Let `q_i^(1)` be the ordered orthonormal basis produced for `P1`, with the seed first and then the one-hit directions in node order.  Define the deterministic depth-2 cone

\[
\boxed{
P_2=\operatorname{span}\left(
P_1\cup\{H_vq_i^{(1)}:\ q_i^{(1)}\in P_1,\ v=0,1,2\}
\right).
}
\]

No singular-vector selection, eigenvector selection, leakage-direction selection, spectral threshold tuning or target observable is allowed in the construction of `P2`.

## Safe master quadratic forms

For each depth `d in {0,1,2}` and orthonormal basis `q_i^(d)`, define the finite restricted **full-image** master matrix by

\[
\boxed{
[M_d]_{ij}=\sum_{v=0}^2
\langle H_vq_i^{(d)},H_vq_j^{(d)}\rangle.
}
\]

This is equivalent to

\[
M_d=P_d\left(\sum_vH_v^\dagger H_v\right)P_d
\]

as a quadratic form, without replacing `H_v P_d` by `P_d H_v P_d` before the norm is evaluated.

The projected shortcut and leakage matrix may also be computed diagnostically:

\[
M_d^{proj}=\sum_v(P_dH_vP_d)^\dagger(P_dH_vP_d),
\]

\[
M_d^{leak}=\sum_v[(1-P_d)H_vP_d]^\dagger[(1-P_d)H_vP_d].
\]

They must satisfy

\[
M_d-M_d^{proj}=M_d^{leak}\succeq0
\]

within the already frozen numerical tolerances.

## Preregistered theorem checks

A GREEN v2 diagnostic certifies implementation and variational structure only.  It requires:

1. `P0`, `P1` and `P2` are nonempty and orthonormal to the frozen tolerance;
2. the ordered `P1` basis is exactly retained as the leading block of the `P2` basis up to numerical tolerance;
3. all full master matrices are finite, Hermitian and positive semidefinite up to roundoff;
4. all leakage matrices are Hermitian and positive semidefinite up to roundoff;
5. the exact full/projected/leakage decomposition holds independently at `P1` and `P2`;
6. the leading `P1 x P1` principal block of `M2` agrees with `M1`, because the same full images `H_v q_i^(1)` define both quadratic forms;
7. the Rayleigh-Ritz inequality

   \[
   \boxed{\lambda_{\min}(M_2)\le\lambda_{\min}(M_1)}
   \]

   holds up to numerical tolerance;
8. the already generated one-step images of the `P1` basis lie in `P2` by construction, verified directly as a construction self-check.

## Quantities that are deliberately NOT PASS criteria

The following are scientific outputs and must not be used to tune the gate after seeing them:

- `dim(P2)`;
- `lambda_min(M2)`;
- whether an exact or apparent zero mode appears;
- the ratio `lambda_min(M2)/lambda_min(M1)`;
- the `P2` leakage magnitude under one further Hamiltonian hit;
- whether `P2` leakage is smaller or larger than v1 leakage;
- projected-vs-full spectral distortion at depth 2;
- any candidate eigenvector's overlap with historical TT, Wilson, GR-ratio or phenomenological sectors.

In particular, **v2 is allowed to remain strongly leaky and gapped and still pass** if all preregistered mathematical identities are correct.

## Mandatory diagnostics

The v2 artifact must report for each depth:

- habitat dimension and basis labels;
- orthonormality defect;
- full, projected and leakage master spectra;
- minimum and maximum eigenvalues;
- apparent zero-mode scans at the same relative thresholds as v1;
- maximum node leakage ratio;
- projected-vs-full spectral distortion;
- exact decomposition residual.

It must additionally report:

- the P1->P2 retained-basis overlap defect;
- the P1 master principal-block consistency defect;
- the Rayleigh-Ritz gap-flow `lambda_min(P0), lambda_min(P1), lambda_min(P2)`;
- ratios between successive minimum eigenvalues when denominators are nonzero;
- maximum residual of every construction image `H_v q_i^(1)` against `P2`;
- a fail-closed `science_status` that states whether depth-2 remains leaky and whether a finite zero-mode candidate is observed, without promoting such a candidate to a physical state.

## Interpretation boundary

Even if `lambda_min(M2)` is numerically zero, this is only a finite Euclidean three-node Ritz candidate.  It is not sufficient to set any physicalization gate to closed.  A theory-specific physical projector requires, at minimum, stability under deeper active-cone enlargement, inclusion of the full intended constraint family (including Lorentzian terms where applicable), refinement/cutoff stability, and a controlled relation to boundary/history observables.

This preregistration explicitly forbids identifying a Hamiltonian-constraint eigenvalue with a physical frequency `omega`.
