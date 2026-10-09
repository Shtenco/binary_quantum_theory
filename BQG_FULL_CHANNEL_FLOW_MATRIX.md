# BQG full multiplicity-channel flow matrix

The previous low-to-low overlap test temporarily assumed that the physically
relevant local master channel is always the lowest eigenchannel.  The first
multiplicity branching \(j=3/2\to2\) falsifies that shortcut: binary
microscopic refinement overlaps only about \(5.4\%\) with the lowest \(j=2\)
master channel and therefore about \(94.6\%\) with the other channel.

The correct finite representation-RG object is therefore the **full channel
flow matrix**

\[
\boxed{
\mathcal F_j^{ab}
=
\frac12
\operatorname{Tr}
\left(
P_{j\to j+1/2,a}^{\rm block}
P_{j+1/2,b}^{\rm master}
\right).
}
\]

Here:

- \(a\) labels every isolated source master multiplicity channel;
- \(b\) labels every target master multiplicity channel;
- \(P^{\rm block}_{a}\) is the target \([2,2]\) copy generated from source
  channel \(a\) by the exact binary-ancilla symmetric blocking tensor.

For each fixed source channel \(a\),

\[
\boxed{
\sum_b \mathcal F_j^{ab}=1
}
\]

within numerical precision, because the target master channels form an
orthogonal resolution of the full target \([2,2]\)-isotypic sector.

This matrix is **not** a physical Markov transition probability.  It is an
RG-compatibility/fidelity matrix.

Its purpose is to identify ancestry-consistent channel trajectories without
the unsupported rule "always choose the lowest local master eigenvalue".

The next canonical finite question is whether the sequence of flow matrices
contains a high-overlap lineage across increasing \(j\), and whether that
lineage stabilizes.
