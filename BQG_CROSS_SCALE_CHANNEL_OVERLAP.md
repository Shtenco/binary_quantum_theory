# BQG microscopic/master cross-scale channel overlap

For consecutive representation scales \(j\to j+\frac12\), define:

1. \(P_j^{\rm master}\): the isolated lowest \([2,2]\) channel selected by the
   S4-twirled local Euclidean constraint master;
2. \(T_j\): the exact microscopic bilinear q=2 refinement tensor obtained by
   adding a fresh four-qubit Gauss-singlet ancilla and symmetrically blocking
   each edge;
3. \(P_{j+1/2}^{\rm block}\): the \([2,2]\) copy generated at the target scale
   by applying \(T_j\) to
   \(P_j^{\rm master}\otimes[2,2]_{\rm anc}\).

The canonical channel overlap is

\[
\boxed{
\mathcal F_j
=
\frac12
\operatorname{Tr}
\left(
P_{j+1/2}^{\rm block}
P_{j+1/2}^{\rm master}
\right).
}
\]

It lies in \([0,1]\).

Also define the principal-angle mismatch

\[
\boxed{
\chi_j
=
\|P_{j+1/2}^{\rm block}-P_{j+1/2}^{\rm master}\|_2.
}
\]

Interpretation:

- \(\mathcal F_j=1\): microscopic binary refinement flows exactly into the
  channel preferred by next-scale constraint dynamics;
- \(\mathcal F_j=0\): the blocking-generated and master-selected copies are
  orthogonal;
- intermediate values quantify genuine representation-RG channel rotation.

This is a well-defined cross-scale quantity and replaces ambiguous comparisons
of raw eigenvectors in multiplicity spaces of changing dimension.

It still does not equal the full physical-projector refinement error
\(\epsilon_j^{\rm sf}\), which additionally requires refinement of the
graph-changing one-hit habitat and full master gaps.
