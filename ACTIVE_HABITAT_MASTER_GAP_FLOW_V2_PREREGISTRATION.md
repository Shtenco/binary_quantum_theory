# Active-habitat master-gap flow v2 — preregistration

Status: **preregistered before reading the v1 active-habitat numerical result.**

This document freezes the next finite-regulator test independently of whatever leakage, zero-mode count or spectral distortion is returned by `active-habitat-master-research #1`.

## Frozen constraint family

Use exactly the same finite Euclidean three-node graph-changing Peter-Weyl family as v1:

- nodes `v = 0,1,2`;
- seed = first state of `basis_full_jhalf()`;
- doubled-spin cutoff `JMAX2 = 5` (`Jmax=5/2`);
- sparse pruning `1e-8`;
- Hamiltonian action = `k5_peter_weyl_safe_hda_column.apply_H_cached_state`.

No result from v1 may alter these choices.

## Nested deterministic active domains

Let

\[
P_0=\operatorname{span}\{\psi_0\}.
\]

Define the one-hit space

\[
P_1=\operatorname{span}\{\psi_0,H_v\psi_0:v=0,1,2\}.
\]

After orthonormalizing `P1`, define the full depth-two cone without selecting directions by amplitude:

\[
\boxed{
P_2=\operatorname{span}\left(P_1\cup\{H_v q_i:q_i\in\operatorname{ONB}(P_1),\ v=0,1,2\}\right).
}
\]

All nonzero linearly independent directions are retained.  There is no SVD truncation chosen from the observed master spectrum and no target-dependent promotion rule.

The orthonormalization algorithm is frozen as two-pass modified Gram-Schmidt with dependence test

```text
residual_norm <= 1e-11 * max(1, input_norm)
```

matching v1.

## Safe master quadratic forms

For `d=0,1,2`, the master matrix on the finite domain is **not** formed from `P_d H_v P_d`.  Instead use the complete images:

\[
\boxed{
[M_d]_{ij}
=\sum_{v=0}^{2}\langle H_vq_i,H_vq_j\rangle.
}
\]

Equivalently,

\[
M_d=P_d\left(\sum_v H_v^\dagger H_v\right)P_d
\]

as a quadratic form, while retaining graph/spin-changing norm outside `P_d`.

For each depth also compute

\[
L_d=\sum_v[(1-P_d)H_vP_d]^\dagger[(1-P_d)H_vP_d]
\]

and the projected shortcut

\[
M_d^{proj}=\sum_v(P_dH_vP_d)^\dagger(P_dH_vP_d),
\]

with the exact identity

\[
M_d-M_d^{proj}=L_d\succeq0.
\]

## Preregistered questions

The outputs, **not PASS targets**, are:

1. dimensions `dim P0`, `dim P1`, `dim P2`;
2. complete spectra of `M0`, `M1`, `M2`;
3. complete spectra of `L0`, `L1`, `L2`;
4. maximum leakage ratio at each depth;
5. apparent kernel counts under the same relative thresholds `1e-8`, `1e-10`, `1e-12`;
6. whether `M_d^proj` creates extra apparent zero modes at any depth;
7. minimum eigenvalue / lowest positive spectral scale as a function of depth;
8. overlap of the lowest Ritz subspaces between nested depths;
9. residual constraint norm of every low-Ritz vector evaluated with the complete `H_v` images;
10. cost diagnostics: sparse support sizes, number of Hamiltonian applications and wall-clock time.

## Exact/variational checks required for PASS

PASS means only that the diagnostic was implemented correctly.  It requires:

1. `P0 subset P1 subset P2` numerically, with orthonormality defect <= `2e-9`;
2. all full master matrices Hermitian and PSD within the v1 numerical tolerances;
3. all leakage matrices Hermitian and PSD;
4. at each depth,

   \[
   M_d-M_d^{proj}=L_d
   \]

   within relative operator-norm error `5e-8`;
5. the Cauchy/Rayleigh-Ritz interlacing appropriate to nested principal restrictions is respected within numerical tolerance;
6. in particular,

   \[
   \lambda_{min}(M_2)\le\lambda_{min}(M_1)\le\lambda_{min}(M_0)
   \]

   up to an absolute numerical allowance `5e-8 * max(||M_2||_2,1)`;
7. all JSON values are native serializable Python types and all computed arrays are finite.

No PASS criterion requires leakage to decrease, a kernel to appear, GR to emerge, or a desired gap value.

## Interpretation rules frozen before result

### Case A — leakage decreases materially
This is evidence that the deterministic Krylov cone is approaching an invariant domain.  It is not yet continuum closure.

### Case B — leakage stays large or grows
The finite cone is dynamically expanding faster than depth two captures.  The correct response is deeper/adaptive sparse Krylov work, not projection.

### Case C — the safe master develops a stable near-zero Ritz sector
Only then may that sector be promoted to a **candidate finite constraint kernel**, after independent checks under larger depth, additional nodes, Lorentzian completion and refinement.

### Case D — only the projected master develops zero modes
Those modes are classified as projection artifacts, not physical states.

### Case E — no low mode appears
This is a valid negative finite-regulator result.  Thresholds must not be loosened to manufacture a kernel.

## Stronger follow-up required before physical projector language

Even a stable finite kernel at depth two is insufficient.  A theory-specific physical projector requires at minimum:

- extension from three Euclidean nodes to the full intended constraint family;
- Lorentzian completion;
- covariance under the full graph/recoupling symmetry action;
- depth/refinement stability of normalized matrix elements;
- control of boundary/history data and the continuum rigging-map limit.

Only after those gates may the chain

\[
P_{phys}\to Z[J]\to W[J]\to\Gamma^{(2)}\to K_{TT}(\omega,k)
\]

be promoted from positive-control formalism to a theory-specific physical construction.

## Claim boundary

This preregistration freezes a finite three-node Euclidean numerical experiment.  It does not assert in advance that the master gap closes, that a physical state exists, that `z` is physical frequency, or that BCQG has derived a graviton propagator.
