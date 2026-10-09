# BQG S4 refinement-carrier scan

Status: **implemented exact finite representation scan; numerical execution tracked by CI.**

The first canonical BQG embedding

\[
j=\frac12\to j=1
\]

works because the four-valent singlet spaces contain a unique multiplicity-one
\(S_4[2,2]\) logical geometry doublet.

The natural fast-closure question is whether this persists for

\[
j=\frac32,2,\frac52,\ldots
\]

so that the same logical qubit has a unique symmetry-selected continuation through the Peter-Weyl tower.

For each equal-spin four-valent singlet space

\[
\mathcal H_j^{\rm sing}
=
\mathrm{Inv}_{SU(2)}(V_j^{\otimes4}),
\qquad
\dim=2j+1,
\]

the gate constructs the full \(S_4\) permutation representation from the same recoupling tensors used by the canonical \(j=\tfrac12\to1\) gate, computes its character, and decomposes it into the five \(S_4\) irreps.

The \([2,2]\) central projector is

\[
\boxed{
P_{22}^{(j)}
=
\frac{2}{24}
\sum_{p\in S_4}
\chi_{22}(p)\,U_j(p).
}
\]

If

\[
\operatorname{rank}P_{22}^{(j)}=2
\]

and its multiplicity remains one, then the logical geometry carrier is uniquely selected by symmetry at that scale.

A persistent multiplicity-one result would define a canonical tower

\[
\boxed{
\mathcal L_{1/2}
\to
\mathcal L_1
\to
\mathcal L_{3/2}
\to
\mathcal L_2
\to\cdots
}
\]

without fitted projectors.

That would reduce the continuum problem to dynamics on a fixed two-dimensional logical carrier per node plus the leakage/mismatch diagnostics \(L_j,D_j\).
