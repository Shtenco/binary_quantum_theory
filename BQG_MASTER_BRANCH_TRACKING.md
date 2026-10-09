# BQG master-branch tracking diagnostic

The previous cross-scale overlap compared microscopic binary refinement only
with the *lowest* target master \([2,2]\) channel.

The observed sequence

\[
\mathcal F =
0.0540,\ 0.9656,\ 0.8398,\ 0.00108,\ 0.9920
\]

is therefore not yet a no-go for microscopic/master compatibility.  It may
instead indicate that the physical RG trajectory moves between different
multiplicity eigenbranches.

This diagnostic resolves the blocking-generated rank-two \([2,2]\) copy
against **all** target master eigenchannels:

\[
\mathcal F_{j\to j+1/2}^{(r)}
=
\frac12
\operatorname{Tr}
\left(
P_{\rm block}
P_{\rm master}^{(r)}
\right).
\]

Because the master channels form an orthogonal resolution of the full
\([2,2]\) isotypic sector,

\[
\sum_r\mathcal F^{(r)}=1.
\]

If a low-channel failure is accompanied by

\[
\max_r \mathcal F^{(r)}\approx1
\]

for \(r\neq0\), then the correct interpretation is **branch switching**, not
failure of the microscopic refinement map.

That would replace the naive rule "always follow the lowest local master
eigenvalue" by the dynamically continuous rule "follow the master branch with
maximal microscopic refinement overlap".
