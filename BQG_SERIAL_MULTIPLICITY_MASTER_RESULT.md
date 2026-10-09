# BQG serial multiplicity-master RG result, j=2..4

Status: **FINITE PASS on five consecutive Peter-Weyl representation scales.**

The same local production constraint is used at every scale,

\[
C_0=H_{E,0}^{\rm sine},
\]

with raw positive master

\[
M_j^{\rm raw}=C_0^\dagger C_0
\]

and exact boundary-frame \(S_4\) twirl

\[
M_j^{\rm tw}
=
\frac1{24}
\sum_{p\in S_4}
U_j(p)^\dagger M_j^{\rm raw}U_j(p).
\]

On the full \([2,2]\)-isotypic sector,

\[
P_{22}^{(j)}M_j^{\rm tw}P_{22}^{(j)}
=
A_j\otimes I_2.
\]

All five independently sharded CI calculations pass.

| \(j\) | \(m_{22}\) | \(\operatorname{spec}A_j\) | lowest isolation gap \(\gamma_j\) | \(\gamma_j/a_{j,0}\) |
|---:|---:|---|---:|---:|
| 2 | 2 | 5.067680982954, 5.807713077901 | 0.740032094948 | 0.1460297318 |
| 5/2 | 2 | 5.769201915254, 22.499018693032 | 16.729816777778 | 2.8998494113 |
| 3 | 2 | 9.001223358412, 10.264684071156 | 1.263460712743 | 0.1403654439 |
| 7/2 | 3 | 7.140843485222, 9.459669912782, 36.381268968404 | 2.318826427560 | 0.3247272444 |
| 4 | 3 | 7.819342874141, 14.040428696350, 16.140265919741 | 6.221085822210 | 0.7956021270 |

The paired Schur degeneracy defects remain at approximately

\[
10^{-14}
\]

or below, and twirled \(S_4\) commutators remain at approximately

\[
10^{-14}
\]

or below.

The relative size of the exact twirl correction stays modest over the scan:

\[
0.0485\lesssim
\frac{\|M_j^{\rm tw}-M_j^{\rm raw}\|}{\|M_j^{\rm raw}\|}
\lesssim0.0617.
\]

## Main result

The lowest master-selected multiplicity channel is nondegenerate in
multiplicity space at every tested scale:

\[
\boxed{
\gamma_j>0
\qquad
j=2,\frac52,3,\frac72,4.
}
\]

Thus there is no observed loss of dynamical channel selection through the
first five scales where multiplicity is nontrivial.

The gap is strongly nonmonotonic:

\[
0.7400,\quad
16.7298,\quad
1.2635,\quad
2.3188,\quad
6.2211.
\]

Therefore no monotone convergence law is inferred from the current data.

In particular, the large \(j=5/2\) gap is not repeated at \(j=7/2\), so a
simple integer/half-integer staggering hypothesis is rejected by the finite
sequence.

## What this closes

The finite sequence

\[
\boxed{
\{A_j,\gamma_j\}_{j=2}^{4}
}
\]

now exists on five consecutive representation scales.

This closes the first column block of the planned continuum-RG table:

- \(j\);
- \(m_{22}(j)\);
- \(\operatorname{spec}A_j\);
- \(\gamma_j\).

## What remains open

This result does **not** yet establish convergence of the physical projector.

The following are still separate calculations:

1. microscopic cross-scale channel overlap from the bilinear q=2 refinement
   tensor;
2. compatible refinement of the graph-changing one-hit habitat;
3. forward/return constraint residuals \(E_a,F_a\);
4. scale-free master residual \(\epsilon_j^{\rm sf}\);
5. asymptotic/summability analysis beyond the first finite representation
   window.

Thus

\[
\boxed{
\gamma_j>0
}
\]

is necessary for stable dynamical channel selection, but it is not by itself a
continuum theorem.
