# BQG canonical selected-channel intertwiner theorem

Status: **PROVED finite representation theorem.**

Assume dynamics has selected one multiplicity channel at two consecutive
representation scales.  Each selected logical carrier is then an irreducible
copy of the same \(S_4[2,2]\) representation,

\[
\mathcal L_j\simeq V_{[2,2]},
\qquad
\mathcal L_{j'}\simeq V_{[2,2]}.
\]

Let their unitary group representations be \(U_j(g)\) and \(U_{j'}(g)\).

For any linear seed \(X:\mathcal L_j\to\mathcal L_{j'}\), define the group
average

\[
\boxed{
\mathcal P_{\rm Hom}(X)
=
\frac1{|S_4|}
\sum_{g\in S_4}
U_{j'}(g)\,X\,U_j(g)^\dagger.
}
\]

Then

\[
U_{j'}(h)\mathcal P_{\rm Hom}(X)
=
\mathcal P_{\rm Hom}(X)U_j(h)
\]

for every \(h\in S_4\).  Hence the averaged map lies in

\[
\mathrm{Hom}_{S_4}(\mathcal L_j,\mathcal L_{j'}).
\]

Because both carriers are equivalent irreducible \([2,2]\) representations,
Schur's lemma gives

\[
\dim \mathrm{Hom}_{S_4}(\mathcal L_j,\mathcal L_{j'})=1.
\]

Therefore every nonzero group-averaged seed is proportional to the unique
intertwiner.

Let

\[
Y=\mathcal P_{\rm Hom}(X)\ne0.
\]

Then \(Y^\dagger Y\) commutes with the irreducible source representation, so

\[
Y^\dagger Y=\alpha I,\qquad \alpha>0.
\]

Consequently

\[
\boxed{
\iota_{j\to j'}
=
\frac{Y}{\sqrt{\alpha}}
}
\]

is an isometric \(S_4\)-intertwiner,

\[
\boxed{
\iota^\dagger\iota=I,
\qquad
U_{j'}(g)\iota=\iota U_j(g).
}
\]

It is unique up to one overall phase.

Thus once the master multiplicity eigenchannel is nondegenerately selected,
the next refinement embedding contains no arbitrary basis rotation:

\[
\boxed{
A_j\ {\rm isolated\ channel}
\to
\mathcal L_j
\to
\iota_j\ {\rm unique\ up\ to\ phase}.
}
\]

The remaining phase drops out of projector-intertwining norms and can be fixed
by a deterministic overlap convention if matrix representatives are needed.

This theorem closes the logical arrow \(A_j\to\iota_j\) in the BQG fast-closure
programme.  It does not prove that the selected channels themselves converge;
that is controlled separately by \(\eta_j\).
