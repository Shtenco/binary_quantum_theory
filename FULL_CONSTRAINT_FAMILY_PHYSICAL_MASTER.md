# Full constraint family required by the BQG physical master

Status: **physicalization scope correction. The current five-node Euclidean master remains a normal-constraint diagnostic, not the full physical projector.**

## 1. Constraint hierarchy

The Peter-Weyl spin-network basis used by the current K5 calculations is already Gauss reduced at every four-valent node. Thus the local SU(2) Gauss constraint is implemented kinematically in the declared basis.

The remaining gravitational constraint structure contains at least

- normal/Hamiltonian constraints;
- tangential/diffeomorphism constraints or their graph/route/habitat realization.

A full finite-regulator master should therefore be understood schematically as

\[
\boxed{
\mathbb M_{full}
=
C_H^\dagger G_H C_H
+
C_D^\dagger G_D C_D
}
\]

on the Gauss-reduced habitat, with positive-definite master metrics on the declared independent constraint labels.

If additional regulator/boundary constraints are retained in the production habitat they must be listed explicitly rather than hidden inside a generic symbol.

## 2. Why the Hamiltonian-only master is not automatically physical at finite regulator

In an exact first-class continuum algebra,

\[
[H[N],H[M]]\sim D[\vec\beta(N,M)],
\]

so a state annihilated by all exact Hamiltonian constraints is also annihilated by their commutators on the appropriate domain.

The finite BQG regulator, however, currently has measured nonzero HDA defects that decrease along a declared scaling family rather than vanishing identically at every finite level.

Therefore it is not legitimate to assume at finite regulator that

\[
\bigcap_v\ker H_v
\]

is already identical to the full physical Dirac sector.

The current five-node master

\[
M_H^{(B)}
=B^\dagger\left(\sum_vH_v^\dagger H_v\right)B
\]

is consequently a **normal-constraint boundary diagnostic**.

## 3. Existing finite Dirac control

`K5_FINITE_DIRAC_REDUCTION.md` provides an exact but regulator-unsafe `Jmax=1/2` control in which the commutator-derived tangential operators first reduce the 32-dimensional fully-active logical carrier to a two-dimensional common scalar sector, after which the normal constraints select one branch.

This establishes an important ordering lesson:

\[
\boxed{
\text{Gauss reduction}
\to \text{tangential/diffeomorphism reduction}
\to \text{normal constraint}
}
\]

can be nontrivial even when all ingredients originate from the same node Hamiltonians.

The old finite result cannot be promoted to the production projector because it lies below the safe Peter-Weyl wall.

## 4. Two legal production strategies

### Strategy A — explicit full master

Construct independent regulator-safe tangential/diffeomorphism operators `D_I` on the same graph-changing habitat and use

\[
\boxed{
\mathbb M_{full}
=
\sum_{v,w}H_v^\dagger G_H^{vw}H_w
+
\sum_{I,J}D_I^\dagger G_D^{IJ}D_J.
}
\]

Then the finite master theorem gives

\[
\ker\mathbb M_{full}
=
\bigcap_v\ker H_v
\cap
\bigcap_I\ker D_I
\]

for positive-definite `G_H,G_D`.

### Strategy B — derived tangential kernel in the joint limit

One may omit an explicit `D` block only if a separate theorem/control proves on the same regulator/refinement family that the asymptotic Hamiltonian zero sector automatically lies in the tangential kernel, with the HDA anomaly vanishing sufficiently fast.

That proof must compare the low projector of the Hamiltonian master to the tangential residual, e.g.

\[
\boxed{
\|D_I P_{low}^{H}\|
\to0
}
\]

for every declared independent tangential generator.

Without such a limit, Hamiltonian-only `P_low^H` must not be called the final physical projector.

## 5. Suggested block-Krylov organization

Keep constraint labels explicit. Starting from the q=2 boundary block `B`, generate

\[
\mathcal K_1
=\operatorname{span}
\{B,H_vB,D_IB\}
\]

or, if the tangential operators are derived from Hamiltonian commutators,

\[
\mathcal K_2
\supset
\operatorname{span}
\{B,H_vB,H_wH_vB\}.
\]

The latter is attractive because the same two-H data used for HDA closure can also measure tangential residuals and the master Ritz spectrum.

The constraints should remain separately labelled when constructing Gram matrices. Summing them into one operator before forming a master can create accidental cancellations that are absent from

\[
\sum_A\|C_A\psi\|^2.
\]

## 6. Lorentzian extension

For

\[
H_v=H^E_v+\lambda H^L_v,
\]

the full normal master is a matrix pencil in `lambda` on a parity-complete habitat:

\[
M_H(\lambda)
=M_{EE}+\lambda M_{EL}+\lambda^2M_{LL}.
\]

On the pure even q=2 boundary the mixed term is removed by doubled-spin parity, but on an enlarged even+odd physical candidate it can be nonzero and must be retained.

Therefore `beta`/relative Lorentzian normalization may not be fixed by the boundary parity simplification.

## 7. Physical-projector decision tree

At each regulator/refinement level:

1. construct the separately labelled normal and tangential constraint images;
2. form the positive master or justified Hamiltonian-only precursor;
3. inspect exact/near-zero spectral separation using `PHYSICAL_PROJECTOR_NEAR_ZERO_RIGGING_LIMIT.md`;
4. test the tangential residual of every low-mode candidate;
5. compare low-subspace projectors under refinement embeddings;
6. compute the q=2 boundary overlap;
7. only after these pass, source-dress the resulting physical/history sector.

## 8. Consequence for scalar cosmology

This distinction is directly relevant to dark-sector claims. A scalar zero of an unreduced normal-constraint master can be

- a tangential/gauge mode;
- a regulator anomaly;
- a genuine additional physical scalar.

Only the third survives the full Dirac/master reduction. Therefore no low Hamiltonian-master eigenvalue is to be labelled dark matter before the tangential residual is shown to vanish and the physical residue/stability tests are passed.

## 9. Claim boundary

The five-node Euclidean boundary master and the K1 outgoing-span calculation remain valuable because they measure the true normal-constraint geometry and the minimal generated habitat. This document only prevents those precursors from being overstated as the complete physical projector before the regulator-safe tangential sector is included or proved redundant in the joint limit.
