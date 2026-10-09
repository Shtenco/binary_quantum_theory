# BQG ancestry-consistent RG path

The local master spectrum alone does not identify the physical refinement
lineage.  The first multiplicity branch already shows that microscopic binary
blocking can preferentially enter a non-lowest master eigenchannel.

Given full channel-flow matrices

\[
\mathcal F_j^{ab}
=
\frac12\operatorname{Tr}
(P^{\rm block}_{j,a}P^{\rm master}_{j+1/2,b}),
\]

the finite ancestry path is selected *without fitting* by maximizing

\[
\boxed{
\prod_j\mathcal F_j^{a_j a_{j+1}}
}
\]

from the unique pre-branch source channel.

Equivalently maximize

\[
\boxed{
\sum_j\log\mathcal F_j^{a_j a_{j+1}}.
}
\]

A dynamic-programming gate computes this path exactly once all finite flow
matrices are available.

This criterion is not a physical-time probability principle.  It is a
representation-RG ancestry criterion: among discrete master eigenchannels, it
finds the lineage most compatible with the already-fixed microscopic binary
refinement tensor.

The resulting path can then be used as the candidate finite lineage on which
the graph-changing habitat residuals \(E_a,F_a\) and ultimately
\(\epsilon_j^{\rm sf}\) are evaluated.
