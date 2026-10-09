# First BQG symmetry-matched dynamical RG datum: j=1/2 -> j=1

Status: **IMPLEMENTED calculation target; numerical result pending execution of the committed gate.**

The first nontrivial BQG refinement carrier is already fixed exactly by symmetry:

\[
W:\ [2,2]_{j=1/2}\to[2,2]_{j=1}.
\]

This allows the same 32-dimensional five-node logical space to be represented at two Peter-Weyl scales without changing its logical dimension.

## Fine carrier

At every K5 node:

\[
j=\frac12,
\qquad
K\in\{0,2\}.
\]

The global logical dimension is

\[
2^5=32.
\]

## Coarse carrier

At every K5 node:

\[
j=1,
\qquad
K\in\{0,2,4\},
\]

but only the symmetry-selected \([2,2]\) doublet is retained:

\[
|0_L\rangle=|K=2\rangle,
\]

\[
|1_L\rangle
=
\frac23|K=0\rangle
-
\frac{\sqrt5}{3}|K=4\rangle.
\]

Thus the coarse logical carrier is again exactly

\[
2^5=32.
\]

No basis fitting is permitted.

## Same dynamical operator at both scales

Use the existing regulator-safe Euclidean sine-Hermitian action

\[
H_{01}=H_{E,0}^{\rm sine}+H_{E,1}^{\rm sine}.
\]

For each logical state compute its one-hit image and form the positive return kernel

\[
\boxed{
K=P H_{01}^2P=A^\dagger A.
}
\]

This produces

\[
K_{1/2}
\]

and

\[
K_1
\]

in exactly the same logical coordinates.

The first theory-specific dynamical RG mismatch is therefore

\[
\boxed{
D_{1/2\to1}^{\rm return}
=
K_1-K_{1/2}.
}
\]

The gate reports both operator and Frobenius relative mismatches, spectra, ranks, gaps-on-support and spin-support controls.

## Why this matters

This is not yet the full master residual

\[
M_1W-WM_{1/2}.
\]

But it is the first nontrivial calculation in which:

- the embedding is derived rather than fitted;
- the microscopic Peter-Weyl dynamics is identical at both scales;
- the logical observable space is identical;
- the comparison is performed before any phenomenological fit.

It therefore gives the first direct answer to:

\[
\boxed{
\text{does BQG dynamics approach a representation-RG fixed point?}
}
\]

The next extension is to replace the return-control \(K\) by the full graph-changing master \(M=C^\dagger G C\), then evaluate the exact leakage/mismatch decomposition

\[
R=L+WD
\]

and the canonical refinement control parameter

\[
\epsilon
=
\frac{\|R\|}{\Delta_{\min}}.
\]
