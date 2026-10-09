# Actual j=2 multiplicity master target

Status: **implemented calculation target; numerical execution pending.**

At \(j=2\), the local four-valent singlet space contains two copies of \(S_4[2,2]\).

The existing volume operator already resolves them geometrically. The next question is whether the **actual Peter-Weyl Euclidean constraint dynamics** resolves the same multiplicity channels.

Freeze the symmetric K5 background:

- all ten links carry \(j=2\);
- nodes \(1,2,3,4\) are fixed in \(K=0\);
- node \(0\) spans doubled labels \(K_2=0,2,4,6,8\).

Use the production sine-Hermitian Euclidean constraint

\[
\boxed{C_0=H_{E,0}^{\rm sine}.}
\]

Define the positive local master block

\[
\boxed{M_0=C_0^\dagger C_0.}
\]

Project to the exact \([2,2]\)-isotypic sector:

\[
M_{22}=P_{22}^{(2)}M_0P_{22}^{(2)}.
\]

If the construction is \(S_4\)-equivariant, Schur's lemma requires

\[
\boxed{M_{22}=A_2^{(M)}\otimes I_2.}
\]

The calculation reports the two multiplicity eigenvalues of \(A_2^{(M)}\), their gap, the doubled-degeneracy defect, \([M_{22},V_{22}]\), and the overlap between low-master and low-volume multiplicity channels.

Scope: local Euclidean constraint master only. The full global master \(M=C_A^\dagger G^{AB}C_B\) and its refinement residual remain later steps.
