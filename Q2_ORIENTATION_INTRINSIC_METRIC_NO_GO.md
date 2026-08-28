# q=2 orientation is invisible to the linear intrinsic metric

## Result

The frozen q=2 local geometry map reconstructs the intrinsic tetrahedral metric from the logical shape coordinates `X,Z` at fixed face-spin norm. The orientation pseudoscalar `Y_L` distinguishes the two mirror/orientation branches but does not enter the intrinsic face Gram matrix.

Therefore

\[
\boxed{\frac{\partial g}{\partial Y}=0}
\]

exactly within this local intrinsic geometry map.

At the two regular branches

\[
(X,Z,Y)=(0,0,+1),\qquad(0,0,-1),
\]

the intrinsic metric is identical.

---

## Full logical-to-metric Jacobian

Using the logical source order `(X,Y,Z)`, the linear metric Jacobian is

\[
B_{XYZ}=(\operatorname{vec}M_X,\;0,\;\operatorname{vec}M_Z).
\]

Hence

\[
\boxed{\operatorname{rank}B_{XYZ}=2.}
\]

With full Frobenius vectorization,

\[
\boxed{
B_{XYZ}^TB_{XYZ}
=\operatorname{diag}\left(\frac92,0,\frac92\right).
}
\]

With the background-covariant tracefree/DeWitt normalization used by the original shape gate,

\[
\boxed{
\langle M_A,M_B\rangle
=\operatorname{diag}\left(\frac32,0,\frac32\right)_{AB}.
}
\]

So the orientation direction is an exact null direction of the intrinsic metric tangent, independently of which of these two normalizations is used.

---

## Relation to the relational source construction

The finite relational projector positive control admits gauge-invariant operators

\[
X_{\rm rel},\quad Y_{\rm rel},\quad Z_{\rm rel}.
\]

Thus `Y` is not absent from the physical-history operator algebra of the positive control.

But when the logical source response is pushed into **intrinsic metric components**, the `Y` column is zero.

Even if the logical connected covariance were isotropic,

\[
\Sigma_{XYZ}=I_3,
\]

the intrinsic metric response is

\[
C_{\rm metric}=B_{XYZ}\Sigma_{XYZ}B_{XYZ}^T
\]

and still has rank two.

Therefore

\[
\boxed{
B_{XYZ}\,e_Y=0.
}
\]

---

## Consequence for the orientation-history coupling

The symmetry-allowed history coupling

\[
g_{YC}\,Y_L\otimes C_h
\]

cannot be identified with a **linear intrinsic-metric** source coefficient.

If a genuine microscopic Peter–Weyl Lorentzian calculation produces a nonzero orientation-odd channel, the correct physical observable must retain information discarded by the intrinsic metric.

Candidate places to look are:

- oriented triad/frame variables;
- connection or holonomy variables;
- extrinsic curvature;
- parity-odd/history-current observables;
- nonlinear metric response where orientation-sensitive data can re-enter through additional structure.

This conclusion is important for the six-Wilson programme: the standard parity-even TT metric `Gamma^(2)` should not be forced to carry a linear `Y_L` coefficient that the exact local geometry map cannot see.

---

## What this does not prove

This no-go is deliberately narrow.

It does **not** prove that:

- physical orientation is pure gauge;
- the Lorentzian orientation-odd amplitude vanishes;
- connection/extrinsic-curvature observables are orientation blind;
- nonlinear metric observables are orientation blind;
- `g_YC^gravity=0`.

It proves only that the **linear intrinsic tetrahedral metric map** has an exact orientation null direction.
