# Logical shape sector -> physical TT kernel: the missing RG bridge

Status: **exact representation-theory separation + physicalization target definition**.

This document corrects a tempting shortcut in the physicalization chain.

The completed higher-shell pair kernel has the S4-invariant form

\[
\Lambda_{pair}^{S4}
=c_0II+J_{shape}(XX+ZZ)+J_{orient}YY.
\]

It is useful to define

\[
R_{aniso}=\frac{J_{orient}-J_{shape}}{c_0}.
\]

However, `R_aniso` is **not** by itself the spatial cubic TT dispersion coefficient `zeta4`.

## 1. Exact operator representation content

The logical geometry qubit carries the two-dimensional tetrahedral irrep

\[
E=[2,2].
\]

The exact S4 sign-character gate proves

\[
\boxed{\operatorname{End}(E)=A_1(I)\oplus A_2(Y)\oplus E(X,Z).}
\]

Equivalently:

```text
I     = ordinary scalar
Y     = orientation/sign pseudoscalar
(X,Z) = intrinsic shape doublet
```

This matches the independent geometric identities

\[
J_1\!\cdot J_2=-\frac14I-\frac12Z,
\]

\[
J_1\!\cdot J_3=-\frac14I+\frac14Z-\frac{\sqrt3}{4}X,
\]

\[
Q=J_1\!\cdot(J_2\times J_3)=\frac{\sqrt3}{4}Y.
\]

Thus `X,Z` change intrinsic tetrahedral shape/metric data, while `Y` carries oriented volume.

## 2. Mirror parity forbids the naive linear identification

Under mirror conjugation,

```text
X -> +X
Z -> +Z
Y -> -Y.
```

The physical metric is mirror even. Therefore its linearized local logical perturbation belongs to the shape doublet `E(X,Z)`, not to the orientation pseudoscalar `Y`.

At a parity/mirror-symmetric quadratic fixed point there is no linear `Y <-> h_TT` mixing.

Consequently

\[
\boxed{R_{aniso}\not\equiv\zeta_4^{cub}.}
\]

Both `YY` and `XX+ZZ` are two-cell S4 scalars, so tetrahedral symmetry alone cannot determine a numerical map from their coefficient difference to a spatial momentum-space cubic invariant.

## 3. Correct quadratic observable

Let

\[
s_A=(X,Z),\qquad A=1,2
\]

denote the local shape doublet.

The quantity that must be coarse-grained is its connected inverse susceptibility / Hessian,

\[
\Gamma_{shape}^{AB}(\omega,\mathbf k;b)
=\frac{\delta^2\Gamma_{eff}}
{\delta s_A(-\omega,-\mathbf k)\,\delta s_B(\omega,\mathbf k)}.
\]

The exact flux/tetrahedron reconstruction supplies a local Jacobian from shape variables to metric perturbations around a chosen nondegenerate background,

\[
h_{ab}=M_{ab}^{\ A}s_A+O(s^2).
\]

After the usual transverse-traceless projector `Pi_TT`, the physical kernel is

\[
\boxed{
K_{TT}=\Pi_{TT}\,M\,\Gamma_{shape}\,M^T\Pi_{TT}.
}
\]

This is the object whose pole must be fitted simultaneously to

\[
\omega^2
=c_T^2k^2
+c_T^2a_*^2\left[
\eta_2^{iso}(k^2)^2
+\zeta_4^{cub}Q_4^{cub}(\mathbf k)
\right]
+O(k^6),
\]

where

\[
Q_4^{cub}=\sum_i k_i^4-\frac35(k^2)^2.
\]

## 4. Where the orientation channel can enter

`J_orient` remains physical information. It controls the propagation/gap of the orientation sector and can feed back into the TT shape kernel if the microscopic dynamics generates symmetry-allowed nonlinear couplings.

Examples schematically include

\[
y^2s_As_A,
\]

or derivative interactions whose total S4/mirror character is scalar.

But such corrections must be **derived and integrated out**. They cannot be replaced by the postulate

```text
zeta4 proportional to J_orient-J_shape.
```

Therefore the j=1 calculation of `R_aniso` remains a valuable internal RG diagnostic, but it is not the external gravitational-wave coefficient.

## 5. Corrected physicalization chain

The shortest honest chain is now

```text
higher-shell Lambda(j=1/2)
 -> S4 pair coefficients {c0,J_shape,J_orient}
 -> symmetry-selected j=1 coarse logical doublet
 -> higher-shell Lambda(j=1)
 -> internal flow of {J_shape,J_orient,R_aniso}

AND

recursive PL geometry
 + shape-to-metric Jacobian M
 + connected shape Hessian Gamma_shape(omega,k;b)
 -> K_TT(omega,k;b)
 -> eta2_iso(b), zeta4_cub(b)
 -> eta2_IR, zeta4_IR.
```

The two lines meet because the same microscopic Peter-Weyl dynamics determines the shape Hessian. They are not identified by symmetry alone.

## 6. New bottleneck

The next physical calculation is therefore not merely

```text
R_aniso(b) -> zeta4(b).
```

It is

\[
\boxed{
\text{Peter-Weyl shape doublet}
\to
\Gamma_{shape}(\omega,\mathbf k;b)
\to
K_{TT}(\omega,\mathbf k;b).
}
\]

The current j=1 higher-shell pilot is the first internal step needed to construct this susceptibility without an arbitrary projector.

## Existing exact gates used by this argument

```text
SPATIAL_QUBIT_GEOMETRY_BRIDGE.md
scripts/logical_s4_twirl_gate.py
scripts/logical_s4_sign_twirl_gate.py
PETER_WEYL_HIGHER_SHELL_S4_RG_SEED.md
PL_GALERKIN_ANISOTROPY_NO_FLOW.md
PETER_WEYL_J1_INTERNAL_RG_PREREGISTRATION.md
```

## Scope

This is a representation-theory and effective-kernel separation statement. It does not yet compute the full interacting `Gamma_shape`, `eta2_IR` or `zeta4_IR`.
