# K5 / tetrahedral off-shell habitat preregistration

Status: **targets frozen before the quantum dual-habitat calculation; symmetric/reference-simplex benchmark, not yet the generic dual-K5 algebra.**

The purpose of this file is to prevent post-hoc selection of a vertex-smooth
functional after seeing the quantum HH output.

## Geometry

Use the positively oriented unit regular tetrahedron

$$
x_0=(0,0,0),
$$

$$
x_1=(1,0,0),
$$

$$
x_2=\left(\frac12,\frac{\sqrt3}{2},0\right),
$$

$$
x_3=\left(\frac12,\frac{\sqrt3}{6},\sqrt{\frac23}\right).
$$

Its oriented volume is

$$
\boxed{V=\frac{\sqrt2}{12}}.
$$

With the inward/toward-vertex flux convention

$$
E_l=3V\nabla\lambda_l,
$$

the four face fluxes are

$$
E_0=
\left(-\frac{\sqrt2}{4},-\frac{\sqrt6}{12},-\frac{\sqrt3}{12}\right),
$$

$$
E_1=
\left(\frac{\sqrt2}{4},-\frac{\sqrt6}{12},-\frac{\sqrt3}{12}\right),
$$

$$
E_2=
\left(0,\frac{\sqrt6}{6},-\frac{\sqrt3}{12}\right),
$$

$$
E_3=
\left(0,0,\frac{\sqrt3}{4}\right),
$$

and `sum_l E_l = 0`.

## HDA pair and sign convention

Freeze the pair `(H_1,H_2)` and define the classical off-shell RHS on a
vertex-smooth functional by

$$
\boxed{
R_{12}f
=\frac{-E_1\cdot\partial_{x_2}f
+E_2\cdot\partial_{x_1}f}{3V}.
}
$$

Changing the global orientation convention flips all nonzero signs together;
the quantum implementation must choose the same convention **before** the
comparison.

## Preregistered test functionals

The first quantum habitat calculation must report all five channels below.
It may add diagnostics, but it may not drop a failing channel.

| ID | functional | exact target |
|---|---|---:|
| F1 | $x_2^x$ | $-1$ |
| F2 | $x_1^y$ | $2\sqrt3/3$ |
| F3 | $x_1^z$ | $-\sqrt6/6$ |
| F4 | $x_2^y$ | $\sqrt3/3$ |
| F5 | $x_1\cdot x_2$ | $0$ |

Numerically,

$$
\boxed{
(-1,
1.1547005383792515,
-0.4082482904638630,
0.5773502691896257,
0).
}
$$

`F5` is a null-control. A quantum prescription that returns zero on every
functional cannot pass simply because `F5` vanishes: it must reproduce the four
nonzero channels too.

## Quantum comparison rule

For each functional `F_a`, compute the declared dual/habitat action of the
quantum graph-changing commutator and a common normalization `C_Q` fixed by one
physical convention, not separately per channel. The shape test is

$$
\Delta_a
=\frac{|C_Q\,Q_a-R_a|}{|C_Q\,Q_a|+|R_a|+\epsilon}.
$$

A single freely fitted `C_Q` may be allowed only if it represents the overall
Newton/time normalization and is fitted **jointly** across the four nonzero
channels. Independent per-functional rescalings are forbidden.

The first structural gate is more stringent than a fit: the vector

$$
(Q_{F1},Q_{F2},Q_{F3},Q_{F4})
$$

must be collinear with

$$
\boxed{
\left(-1,\frac{2\sqrt3}{3},-\frac{\sqrt6}{6},\frac{\sqrt3}{3}\right)
}
$$

while the `F5` response remains compatible with zero.

## Critical scope note: primal simplex versus dual K5

The Bonzom--Dittrich boundary formula used here fixes one reference spatial
simplex `sigma(0)` and its `H(k)` translate the four **primal vertices** of that
simplex.  Our canonical K5 implementation labels Hamiltonians by **dual
four-valent tetrahedral nodes** and uses a local node volume.

The boundary of a regular 4-simplex is self-dual at the combinatorial level, so
the distinction is hidden in the maximally symmetric benchmark.  It is not
legitimate to assume that the same `1/(3V)` formula with one common reference
volume is automatically the generic algebra of the node-local K5
regularization.

Therefore the frozen targets in this file are deliberately classified as a

$$
\boxed{\text{symmetric/reference-simplex benchmark}}
$$

and **not** yet as the universal generic-geometry target of all five node-local
Hamiltonians.  Before a generic off-shell claim is made, the dual-cell
classical algebra matching the actual node-local volume/normalization must be
derived separately.

## Interpretation boundary

These are classical off-shell targets, not predictions of the microscopic
theory. Their role is to test a declared symmetric/reference-simplex channel
and to detect the trivial zero-commutator pathology. A generic dual-K5 HDA claim
requires the additional primal-to-dual derivation stated above.
