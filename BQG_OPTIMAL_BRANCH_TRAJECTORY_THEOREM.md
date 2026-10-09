# BQG optimal branch-trajectory theorem

Status: **PROVED finite combinatorial theorem.**

Let the microscopic/master branch-transfer matrix at refinement step \(j\) be

\[
F_j^{rs}\in[0,1],
\]

where \(r\) labels source master multiplicity branches and \(s\) labels target
branches.  For every source branch,

\[
\sum_s F_j^{rs}=1.
\]

For a branch path

\[
\pi=(r_0,r_1,\dots,r_N),
\]

define the cumulative overlap score

\[
\boxed{
\mathcal P(\pi)
=
\prod_{k=0}^{N-1}F_k^{r_k r_{k+1}}.
}
\]

Equivalently define the additive action

\[
\boxed{
S(\pi)
=
-\log\mathcal P(\pi)
=
-\sum_k\log F_k^{r_k r_{k+1}}.
}
\]

Then the globally optimal path is obtained exactly by the recurrence

\[
\boxed{
D_{k+1}(s)
=
\max_r
\left[
D_k(r)\,F_k^{rs}
\right].
}
\]

No exponential path enumeration is required.

For robustness against one catastrophic RG step, define the bottleneck score

\[
\boxed{
B(\pi)
=
\min_kF_k^{r_k r_{k+1}}.
}
\]

Its globally optimal trajectory is given by

\[
\boxed{
B_{k+1}(s)
=
\max_r
\min\left(B_k(r),F_k^{rs}\right).
}
\]

Therefore the finite BQG branch-selection problem has two exact canonical
diagnostics:

1. **maximum-product trajectory**
   \[
   \pi_{\rm prod}
   =
   \arg\max_\pi\prod_kF_k^{r_kr_{k+1}};
   \]

2. **maximum-bottleneck trajectory**
   \[
   \pi_{\rm bott}
   =
   \arg\max_\pi\min_kF_k^{r_kr_{k+1}}.
   \]

If both select the same branch sequence, the trajectory is particularly
robust.

For the selected trajectory define

\[
\boxed{
\chi_k
=
\sqrt{1-F_k^{r_kr_{k+1}}}.
}
\]

A necessary finite precursor of an asymptotically smooth microscopic/master RG
trajectory is that the optimal-path mismatches become small rather than merely
the overlaps with the locally lowest master branch.

This theorem changes no physics and introduces no fitted parameter.  It only
extracts the globally most continuous branch sequence from the already defined
microscopic/master overlap matrices.
