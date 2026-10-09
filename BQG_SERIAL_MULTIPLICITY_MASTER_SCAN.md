# BQG serial multiplicity-master RG scan

Status: **implemented serial finite calculation.**

The next fast-closure datum is the sequence

\[
A_j,\qquad \gamma_j
\]

for several consecutive representation scales, using exactly the same
Peter-Weyl Euclidean constraint at every scale.

For each

\[
j=2,\frac52,3,\frac72,4
\]

the calculation builds

\[
C_0=H^{\rm sine}_{E,0},
\qquad
M_j^{\rm raw}=C_0^\dagger C_0,
\]

then removes the frozen local-frame bias by the exact group average

\[
M_j^{\rm tw}
=
\frac1{24}\sum_{p\in S_4}U_j(p)^\dagger M_j^{\rm raw}U_j(p).
\]

On the full \([2,2]\)-isotypic sector,

\[
P_{22}^{(j)}M_j^{\rm tw}P_{22}^{(j)}
=
A_j\otimes I_2.
\]

Thus every eigenvalue of \(A_j\) must appear twice in the restricted spectrum.

The gate records:

- \(m_{22}(j)=\lceil2j/3\rceil\);
- all eigenvalues of \(A_j\);
- adjacent multiplicity-channel gaps;
- the isolation gap \(\gamma_j\) of the lowest channel;
- exact-pair degeneracy defects;
- raw and twirled \(S_4\) covariance diagnostics;
- the size of the twirl correction.

This is the first serial dataset needed before a non-arbitrary inter-scale
embedding \(\iota_j\) can be derived.

It does **not** yet claim \(\eta_j\) or \(\epsilon_j\): those require an
actual consecutive-scale channel map rather than comparing eigenvalue lists.
