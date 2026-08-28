# Reducing the 24-term Lorentzian epsilon node to one logical ordered triple

The genuine-amplitude frontier should not pay for 24 expensive Peter-Weyl
ordered triples if representation theory already fixes their orbit.

For one four-neighbor frame, the Lorentzian oriented assembler contains four
choices of omitted neighbor and all six orders of the remaining three:

\[
4\times 3!=24.
\]

Write a permutation of the full frame as

\[
p=(a,b,c,d),
\]

where `d` is omitted and `(a,b,c)` is the ordered triple.  With the repository's
current tetrahedral face convention `(-1)^r`, the exact combinatorial
coefficient is

\[
\boxed{\epsilon(p)=-\operatorname{sgn}(p).}
\]

The overall minus sign is only the chosen global frame orientation.

If the genuine microscopic ordered-triple operator is covariant under neighbor
permutations,

\[
T_{p(a)p(b)p(c)}=U_p O U_p^\dagger,
\]

then the complete logical epsilon operator is

\[
L_\epsilon
=-\sum_{p\in S_4}\operatorname{sgn}(p)U_pOU_p^\dagger
=-24\,\mathcal T_{\rm sgn}(O).
\]

On the two-dimensional logical `[2,2]` carrier,

\[
\operatorname{End}(E)=A_1(I)\oplus A_2(Y)\oplus E(X,Z),
\]

so the sign sector is one-dimensional.  Therefore

\[
\mathcal T_{\rm sgn}(O)
=\frac{\operatorname{Tr}(YO)}{2}Y,
\]

and hence

\[
\boxed{
L_\epsilon=-12\operatorname{Tr}(YO)\,Y.
}
\]

This gives a major computational reduction: after genuine Peter-Weyl covariance
is validated on a generating set of neighbor permutations, the full logical
24-term epsilon node can be reconstructed from one canonical `2x2` logical
ordered-triple matrix `O`.

The result is exact group theory and combinatorics.  It does **not** assume that
the microscopic sine-ordered Peter-Weyl triple is already proven covariant, and
it does not identify the resulting local `Y` coefficient with the later
relational/history coefficient `g_YC^gravity`.
