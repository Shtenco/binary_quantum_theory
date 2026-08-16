# Exact first-refinement Euclidean tangent-rank theorem

This note records a computationally exact lower-bound construction that avoids evaluating the expensive q=6 and q=8 barycentric plaquettes.

## Setup

Take the first barycentric subdivision of the 16-cell PL-S3.  One declared coarse tetrahedron contains 24 fine tetrahedral chambers.  The full closed refinement has 384 fine tetrahedra and 768 dual links.

For each fine source chamber `u` in the selected coarse block, define

\[
c_u=E_u^{sine}|\Omega_{L1}\rangle,
\]

with the frozen zero-aware physical-sine Euclidean operator and the homogeneous all-`j=1/2`, `K=0` seed.

Every fine chamber has the same regulator-length census over its 12 oriented Euclidean specs:

```text
q=4 : 6 specs
q=6 : 4 specs
q=8 : 2 specs
```

## Exact four-edge projector

Let `P4` project onto final Gauss-basis states for which exactly four microscopic doubled-spin labels differ from the seed value `2j=1`.

For one oriented Euclidean term, every edge of the curvature plaquette is hit exactly once by a fundamental holonomy.  Therefore

\[
2j=1\longrightarrow 0\;\text{or}\;2
\]

on every plaquette edge: every such edge necessarily changes its spin label.

The separate source link is disjoint from the plaquette and receives two hits.  It may return to the seed spin or reach another allowed spin, but it cannot remove any of the q changed plaquette edges.

Hence

\[
P_4 E_u^{sine}|\Omega_{L1}\rangle
\]

receives contributions from `q=4` plaquettes only.  Terms with `q=6` or `q=8` are exactly annihilated by `P4`.  This is a representation-support theorem, not a numerical truncation.

Define

\[
d_u=P_4c_u.
\]

The q=4 amplitudes are evaluated with the same Peter-Weyl/CG/volume primitives as the full graph-independent operator.  The active-cone backend merely factors untouched-node overlaps equal to one and has a separate full-backend equivalence gate.

## Exact rank implication

The 24 projected columns have a 24x24 Gram matrix

\[
G^{(4)}_{uv}=\langle d_u|d_v\rangle.
\]

The direct calculation gives full rank 24.  Since a linear projector cannot increase rank,

\[
24=\operatorname{rank}\{P_4c_u\}
\le \operatorname{rank}\{c_u\}
\le24.
\]

Therefore

\[
\boxed{\operatorname{rank}\{E_u^{sine}|\Omega_{L1}\rangle\}_{u=1}^{24}=24}.
\]

This conclusion is exact even though the q=6 and q=8 amplitudes are never evaluated.

## Independent local calculation before CI reproduction

The local exact run that motivated the distributed regression found:

```text
projected support per source       60
projected union support            768
unique states per source           12
support multiplicity 1             288 states
support multiplicity 2             384 states
support multiplicity 4              96 states
Gram minimum eigenvalue     0.8436999771224867
Gram maximum eigenvalue     1.855322144931527
minimum singular value      0.9185314241344641
maximum singular value      1.3621021051784359
projected rank                         24 / 24
column norm                 1.1616845789744337
```

These numbers are now regression targets for reproducibility, not post-hoc acceptance thresholds for GR universality.  The scientific content is the exact projector isolation and the observed positive-definite rank-24 Gram.

## What this closes — and what it does not

It closes a major obstruction: the static maximal-symmetric barycentric block has rank-one image, but the production Euclidean dynamics immediately generates the full 24-dimensional fine-chamber tangent span at L1.

It does **not** yet identify those 24 fine-Hilbert directions with physical coarse metric modes.  The next mandatory operation is an explicit internal-link contraction / boundary isometry `W_block`, followed by the frozen target-independent Krylov compression, Lorentzian and route completion, kinetic Hessian, constraint-rank SVD, and collective HDA residual.
