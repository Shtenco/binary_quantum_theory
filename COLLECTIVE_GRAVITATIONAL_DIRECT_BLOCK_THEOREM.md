# Collective homogeneous gravitational direct-block theorem

## Result

On the frozen real Peter-Weyl convention and the homogeneous six-edge coarse carrier `W_g`, the direct Euclidean **and** Hermitian-completed Lorentzian gravitational matrices vanish:

\[
\boxed{W_g^\dagger H_E^{\rm sine}W_g=0},
\]

\[
\boxed{W_g^\dagger S W_g=0},
\qquad
S=-\frac{i}{2}(L_{raw}-L_{raw}^\dagger),
\]

and therefore, at `beta=hbar=1`,

\[
\boxed{W_g^\dagger G W_g=0},
\qquad
G=-\frac23H_E^{\rm sine}-\frac{32}{9}S.
\]

This is a direct-projection theorem. It does **not** say that the gravitational operators vanish, nor that their leakage or depth-two return vanishes.

## 1. Phase chain

The real recoupling/absolute-volume convention gives

\[
V=V^T\in\mathbb R,
\qquad
H_E^{\rm sine}=iA_E,
\qquad
A_E^T=-A_E\in\mathbb R.
\]

Hence

\[
K=[V,H_E^{\rm sine}]
=i(VA_E-A_EV)
\equiv iB_K,
\]

and

\[
B_K^T=B_K.
\]

Thus `K` is pure-imaginary and anti-Hermitian, with a real-symmetric core.

The raw Lorentzian structural stack contains two `K` legs and one `V` leg. All Clebsch-Gordan coefficients, epsilon intertwiners and auxiliary contractions are real in the frozen convention. The two `K` phases give

\[
i^2=-1,
\]

so the unsymmetrized raw Lorentzian matrix is real:

\[
L_{raw}\in\mathbb R.
\]

The production Hermitian completion therefore becomes

\[
S=-\frac{i}{2}(L_{raw}-L_{raw}^T)
=iA_S,
\qquad A_S^T=-A_S\in\mathbb R.
\]

So both `H_E^sine` and `S` lie in the same pure-imaginary Hermitian / real-antisymmetric matrix class on a real coarse basis.

## 2. S4 obstruction

The six coarse tetrahedral edges carry the real multiplicity-free representation

\[
6=A_1\oplus E\oplus T_2=1\oplus2\oplus3.
\]

The orientation phase convention may twist this representation by the sign character, but the exact gate checks both cases.

For both the ordinary edge representation and its sign twist, the space of `S4`-invariant real antisymmetric `6x6` matrices has nullity zero:

```text
ordinary antisymmetric commutant nullity = 0
sign-twisted antisymmetric commutant nullity = 0
```

Therefore any exactly homogeneous `S4` scalar in the pure-imaginary Hermitian class has zero direct six-edge matrix.

## 3. Consequence for the DeWitt calculation

This prevents a false shortcut. A nonzero Einstein/DeWitt kinetic tensor cannot be obtained by fitting the direct homogeneous gravitational projection, because that projection is structurally zero.

The first nontrivial gravitational metric dynamics must instead be extracted from excursions outside the six-edge carrier and their return, schematically

\[
W_g
\xrightarrow{\;G\;}
Q_\perp\mathcal H
\xrightarrow{\;G\;}
W_g.
\]

A target-independent denominator-free precursor is the positive return/leakage Gram

\[
\boxed{
L_G=(Q_\perp G W_g)^\dagger(Q_\perp G W_g),
}
\]

which is itself `S4` invariant and therefore determined by only three representative channels: diagonal, adjacent and opposite edge. A physical Feshbach/Schrieffer-Wolff effective Hamiltonian may be introduced only after its energy/resolvent prescription is frozen independently of the GR target.

## 4. Route operator

The theorem does not force the operator-first route block to zero. A homogeneous route operator built from a positive flux-metric symbol is real-symmetric and may carry the three allowed `A1/E/T2` channels.

Therefore, if a temporary combined effective operator is written as

\[
C=H_E+(1+\beta^2)H_L+R_{op},
\]

the direct homogeneous `6x6` matrix can receive a route contribution even though the gravitational `H_E+H_L` part vanishes. That route contribution must not be misidentified with the gravitational DeWitt tensor; the latter is a depth-two gravitational return question.

## 5. Relation to photon interference

The direct coarse metric response is already nonzero:

\[
rank(B_F)=6,
\qquad cond(B_F)\simeq1,
\]

while the direct gravitational scalar projection is zero.

Thus BCQG predicts a concrete operator-depth separation on this finite block:

- coarse geometry is linearly readable by flux observables and therefore by photon phase;
- homogeneous gravitational curvature of those same six directions first appears through a higher dynamical depth.

Balanced photon interferometry still has rank five on the traceless sector. Consequently optical readout can in principle diagnose the five shape directions whose **depth-two** gravitational return eigenvalues must later merge into the continuum DeWitt traceless sector.

## 6. Reproducibility

- `scripts/collective_gravitational_direct_block_gate.py`
- `verification_results/COLLECTIVE_GRAVITATIONAL_DIRECT_BLOCK.json`
- `scripts/collective_euclidean_first_order_projection_gate.py`
- `verification_results/COLLECTIVE_EUCLIDEAN_FIRST_ORDER_PROJECTION.json`
- `LORENTZIAN_HERMITIAN_COMPLETION.md`
- `BCQG_PHOTON_INTERFERENCE_BRIDGE.md`

## Status

`PROVED_FINITE_SELECTION_THEOREM` under the frozen real recoupling convention and exact homogeneous `S4` covariance.

Open: direct computation of the three `A1/E/T2` depth-two gravitational return channels, followed by the preregistered normalized-state metric Hessian and collective constraint ranks.
