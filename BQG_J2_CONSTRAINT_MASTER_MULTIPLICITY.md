# Actual j=2 constraint-master multiplicity result

Status: **FINITE PASS for exact S4-twirled local Euclidean constraint master; raw boundary-conditioned block is a NONCOVARIANT CONTROL.**

At \(j=2\), the local four-valent singlet space contains two copies of \(S_4[2,2]\).

The existing volume operator resolves them geometrically. The present calculation asks whether the actual Peter-Weyl Euclidean constraint dynamics also resolves the multiplicity space.

## Raw local master

On the symmetric all-\(j=2\) K5 background, use

\[
C_0=H_{E,0}^{\rm sine},
\qquad
M_0=C_0^\dagger C_0.
\]

With neighbours frozen in \(K=0\), the raw boundary-conditioned local master is not invariant under a permutation acting only on the node-0 recoupling basis:

\[
\max_{p\in S_4}\|[M_0,U(p)]\|
=
1.304251618607578.
\]

Therefore the raw block is retained only as a **NONCOVARIANT CONTROL** and its apparent pair averages are not interpreted as Schur multiplicity eigenvalues.

## Exact S4 twirl

Define

\[
\boxed{
M_0^{\rm tw}
=
\frac1{24}
\sum_{p\in S_4}
U(p)^\dagger M_0U(p).
}
\]

This removes the arbitrary local boundary-frame orientation without fitting any operator coefficient.

The twirled commutator is

\[
\boxed{
\max_{p\in S_4}
\|[M_0^{\rm tw},U(p)]\|
=
5.88\times10^{-15}.
}
\]

Its five-dimensional spectrum is

\[
\{5.067680982953854,\,
5.067680982953856,\,
5.807713077901409,\,
5.807713077901410,\,
8.857799903329834\}.
\]

Restricted to the \([2,2]\) isotypic sector:

\[
\boxed{
\operatorname{spec}
\left(P_{22}M_0^{\rm tw}P_{22}\right)
=
\{
5.06768098295385,
5.067680982953855,
5.807713077901405,
5.807713077901409
\}.
}
\]

Thus

\[
\boxed{
P_{22}M_0^{\rm tw}P_{22}
=
A_2^{(M)}\otimes I_2
}
\]

within numerical precision, with multiplicity eigenvalues

\[
\boxed{
a_-^{(M)}=5.067680982953853,
\qquad
a_+^{(M)}=5.807713077901408.
}
\]

The multiplicity gap is

\[
\boxed{
\gamma_2^{(M)}
=
0.740032094947555.
}
\]

The paired-degeneracy defect is only

\[
\boxed{
5.33\times10^{-15}.
}
\]

## Geometry versus dynamics

The volume-selected \([2,2]\) channels are

\[
V_-\approx1.985011890130056,
\qquad
V_+\approx3.022651919534289.
\]

But

\[
\boxed{
\|[M_{22}^{\rm tw},V_{22}]\|
=
0.4376577461914789,
}
\]

with relative commutator

\[
\boxed{
7.8509543313\times10^{-3}.
}
\]

The overlap of the low-master and low-volume rank-two channel projectors is

\[
\boxed{
0.08916057985397588.
}
\]

Therefore the actual constraint dynamics and the geometric volume operator do **not** select the same multiplicity direction.

This is a positive and physically important result:

\[
\boxed{
\text{geometry provides coordinates in multiplicity space,}
\quad
\text{dynamics selects the RG channel.}
}
\]

The lower-volume channel must not be assumed to be the physical refinement trajectory.

## Scope

This is a finite local Euclidean constraint-master result after exact \(S_4\) twirling of the boundary-conditioned node-0 block.

It is not yet:

- the full global master sum over all constraint labels;
- the Lorentzian-completed master;
- a refinement residual \(R_j\);
- a continuum physical-projector theorem.

The next required step is to construct the same \(S_4\)-equivariant/global master prescription at consecutive \(j\), select the isolated master channel, build \(\iota_j\), and compute

\[
\epsilon_j=\|R_j\|/\Delta_{\min,j}.
\]
