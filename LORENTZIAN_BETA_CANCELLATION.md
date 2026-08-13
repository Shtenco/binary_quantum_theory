# Lorentzian β-cancellation gate

## Scope

This file records a **classical kinetic-sector identity** for the real Ashtekar--Barbero formulation. It is a convention/regression gate for the finite canonical programme. It does **not** prove quantum Immirzi independence, full off-shell HDA closure or the continuum limit of the Peter--Weyl model.

Let

$$
A_a^i=\Gamma_a^i+\beta K_a^i
$$

with real Barbero--Immirzi parameter $\beta$. Define the ADM/DeWitt kinetic density

$$
\boxed{
Q_{\rm DW}
=\sqrt q\left(K_{ab}K^{ab}-K^2\right)
}.
$$

Equivalently,

$$
C(E,K)
=\sqrt q\left(K^2-K_{ab}K^{ab}\right)
=-Q_{\rm DW}.
$$

## Derivative-free kinetic identity

In the curvature

$$
F(A)=F(\Gamma)+\beta D_\Gamma K+\beta^2 K\wedge K,
$$

the derivative-free kinetic contribution of the Euclidean constraint is

$$
\boxed{
H_E^{\rm kin}
=\beta^2 C(E,K)
=-\beta^2 Q_{\rm DW}.
}
$$

The Lorentzian correction contributes

$$
\boxed{
H_L^{\rm corr}
=-(1+\beta^2)C(E,K)
=(1+\beta^2)Q_{\rm DW}.
}
$$

Therefore

$$
\boxed{
H_E^{\rm kin}+H_L^{\rm corr}=Q_{\rm DW}
}
$$

for every real $\beta$ in this sector.

The cancellation is exact:

$$
-\beta^2+(1+\beta^2)=1.
$$

## Important qualification

The full $F(A)$ also contains the term

$$
\beta D_\Gamma K.
$$

It is therefore incorrect to demand raw pointwise $\beta$-independence of an unprojected Euclidean Hamiltonian. The finite quantum universality observable must be defined only after the appropriate Gauss/diffeomorphism/boundary treatment on the declared off-shell domain.

The intended IR gate is schematically

$$
\boxed{
\Delta_\beta
=
\frac{\|P_{G,D}[H^{(\beta_1)}-H^{(\beta_2)}]P_{G,D}\|}
{\|P_{G,D}HP_{G,D}\|}
\longrightarrow0,
}
$$

or its corresponding habitat/dual version when the Hamiltonian is graph-changing.

## Connection to the DeWitt signature gate

The target quadratic kinetic form is the same one whose flux pullback has inertia

$$
\boxed{(5+,1-,3\,0)}.
$$

Thus the Lorentzian programme must reproduce **both**:

1. the unique DeWitt trace/conformal structure;
2. cancellation of spurious real-$\beta$ dependence in the physical IR kinetic sector.

A model that reproduces only the Euclidean $EEF$ term is not enough for real-$SU(2)$ GR.

## Reproduction

```bash
python scripts/lorentzian_beta_cancellation_gate.py
```

The script samples random positive-definite spatial metrics and symmetric extrinsic-curvature tensors, computes $Q_{\rm DW}$ directly, evaluates the Euclidean and Lorentzian kinetic pieces for several real $\beta$, and verifies the cancellation to floating-point precision.

This script is a **regression of the stated classical identity**, not independent evidence for the quantum theory.
