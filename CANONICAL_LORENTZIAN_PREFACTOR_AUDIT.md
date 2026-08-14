# Canonical Lorentzian prefactor audit

Status: **algebraic normalization audit for the existing Peter--Weyl raw operators; no new coupling is introduced**.

## Purpose

The finite Peter--Weyl Lorentzian gates deliberately compute the structural raw object

\[
L_{\rm raw}
=\sum_{abc}\epsilon_{abc}\operatorname{Tr}_{aux}
\left[C_a(K_{\rm raw})C_b(K_{\rm raw})C_c(V_{\rm raw})\right],
\]

with

\[
K_{\rm raw}=[V_{\rm raw},H_{E,\rm raw}],
\qquad
C_e(O)=h_e[h_e^{-1},O].
\]

They omit the canonical Poisson-to-commutator factors, the physical volume/action units and the final Lorentzian real coefficient. This file tracks those factors symbolically so the raw Lorentzian amplitude is not mistaken for a second independent gravitational coupling.

## 1. Already-existing physical normalizations

Write

\[
\hat V=v_*V_{\rm raw},
\qquad
\hat H_E=h_*H_{E,\rm raw}.
\]

`v_*` is fixed once the microscopic flux/area unit is fixed, because volume is homogeneous of degree `3/2` in the fluxes. `h_*` is fixed by the same action/time normalization that determines the effective gravitational coupling. They are not new Lorentzian parameters.

Keep convention-dependent real constants explicit:

- `c_K`: coefficient in the classical Thiemann identity defining the integrated extrinsic-curvature generator from `{V,H_E}`;
- `c_C`: regulator/holonomy coefficient converting a connection Poisson bracket into the finite covariant leg;
- `c_L`: real classical coefficient of the structural Lorentzian triple before the already-separated factor `(1+beta^2)`.

These constants are fixed once the canonical and regulator conventions are frozen.

## 2. Extrinsic-curvature generator

Poisson-to-commutator replacement gives

\[
\hat K_{phys}
=c_K\frac{1}{i\hbar}[\hat V,\hat H_E]
=c_K\frac{v_*h_*}{i\hbar}K_{\rm raw}.
\]

Because `V_raw` and the sine-ordered `H_E,raw` are Hermitian, `K_raw` is anti-Hermitian and `(1/i)K_raw` is Hermitian, as required for the physical generator.

## 3. Three covariant legs

For each connection Poisson bracket write schematically

\[
\{A,O\}\longrightarrow
c_C\frac{1}{i\hbar}C(O).
\]

Linearity gives

\[
C(K_{phys})
=c_K\frac{v_*h_*}{i\hbar}C(K_{raw}),
\qquad
C(V_{phys})=v_*C(V_{raw}).
\]

Therefore, with all convention/regulator constants displayed rather than silently set to one, the conversion factor multiplying the raw `K-K-V` triple has the structure

\[
\boxed{
\mathcal N_L
=c_Lc_C^3c_K^2
\frac{v_*^3h_*^2}{(i\hbar)^5}.
}
\]

Since

\[
1/i^5=-i,
\]

we obtain the structural phase

\[
\boxed{
\mathcal N_L
=-i\,
\left(c_Lc_C^3c_K^2\frac{v_*^3h_*^2}{\hbar^5}\right).
}
\]

Thus, in the declared commutator conventions, the phase that converts the present anti-Hermitian raw epsilon sum to a Hermitian structural Lorentzian operator is

\[
\boxed{H_L^{Herm}\propto -iL_{raw}.}
\]

The exact real magnitude still requires the frozen canonical/regulator coefficients; it is not fitted from the raw matrix element.

## 4. Environment-unbiased one-body result

The completed exact `S4` orbit environment trace at `Jmax=7/2` gives

\[
L_{1body}^{raw}
=(1.3389293521464034\,i)Y
\]

with

\[
\Delta_{S4,cov}=1.3976239359266602\times10^{-15},
\]

and

\[
\Delta_{volume\ leakage}=6.532094795930893\times10^{-16}.
\]

The non-`Y` Pauli coefficients after the exact sign twirl vanish at roundoff.

Therefore the Hermitian structural one-body term has the form

\[
\boxed{
H_{L,1body}^{Herm}
=g_L\,1.3389293521464034\,Y,
}
\]

where

\[
g_L=c_Lc_C^3c_K^2\frac{v_*^3h_*^2}{\hbar^5}\in\mathbb R
\]

within the convention bookkeeping above. The full declared constraint contributes

\[
A_{0,1body}
=(1+\beta^2)H_{L,1body}^{Herm}.
\]

This is the one-body component of `P H_L P`, not the complete 32-dimensional logical Lorentzian matrix.

## 5. Exact local shape dynamics implied by the Y structure

The logical tetrahedral metric/shape coordinates live in the `X/Z` plane, while oriented volume is proportional to `Y`. For

\[
H=a_LY,
\]

Pauli algebra gives

\[
[Y,X]=-2iZ,
\qquad
[Y,Z]=2iX,
\]

hence

\[
\dot X=\frac{2a_L}{\hbar}Z,
\qquad
\dot Z=-\frac{2a_L}{\hbar}X,
\]

and

\[
\boxed{
\ddot X+\Omega_L^2X=0,
\qquad
\Omega_L=2|a_L|/\hbar.
}
\]

The nonzero environment-unbiased Lorentzian one-body return therefore acts structurally as a local rotation of the two metric-shape coordinates. This is not by itself a graviton mass: the physical pole requires the full constrained spatial coupling and continued-fraction resolvent.

## 6. One-coupling conclusion

The finite code intentionally stripped units from `V`, `H_E` and the Lorentzian triple. Restoring them does **not** justify introducing a new fitted Lorentzian coupling. Once

1. the microscopic area/length conversion is fixed;
2. the Euclidean/action normalization is fixed;
3. the canonical `c_K,c_C,c_L,beta` convention is frozen;

then the Lorentzian normalization is algebraically determined by the same data.

The physicalization problem therefore remains one common gravitational scale/action normalization plus regulator/universality control, not independent Euclidean and Lorentzian Newton constants.

## Boundary

The numerical one-body coefficient is a finite safe-cutoff structural result. The environment-unbiased full `32 x 32` `P H_L P`, its multi-body Pauli components, the full Lorentzian block-Lanczos chain, continuum/RG limit and experimental comparison remain separate calculations.
