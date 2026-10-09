# BQG two-sided habitat refinement theorem

Status: **PROVED finite operator theorem.**

A selected logical-channel embedding is not by itself enough to compare
graph-changing constraints, because a constraint maps the base carrier into a
larger graph/spin-changed image habitat.

Let

\[
C_{f,a}:\mathcal H_f^{(0)}\to\mathcal H_f^{(1)},
\qquad
C_{c,a}:\mathcal H_c^{(0)}\to\mathcal H_c^{(1)}.
\]

Choose isometric refinement maps

\[
\iota_0:\mathcal H_f^{(0)}\to\mathcal H_c^{(0)},
\qquad
\iota_1:\mathcal H_f^{(1)}\to\mathcal H_c^{(1)}.
\]

Define the forward one-hit residual

\[
\boxed{
E_a
=
C_{c,a}\iota_0-\iota_1C_{f,a}.
}
\]

For the adjoint/return map define

\[
\boxed{
F_a
=
C_{c,a}^\dagger\iota_1-\iota_0C_{f,a}^\dagger.
}
\]

The fine and coarse master operators are

\[
M_f=\sum_a C_{f,a}^\dagger C_{f,a},
\qquad
M_c=\sum_a C_{c,a}^\dagger C_{c,a}.
\]

Then

\[
\begin{aligned}
M_c\iota_0-\iota_0M_f
&=
\sum_a
\left(
C_{c,a}^\dagger C_{c,a}\iota_0
-
\iota_0C_{f,a}^\dagger C_{f,a}
\right)\\
&=
\sum_a
\left[
C_{c,a}^\dagger
(C_{c,a}\iota_0-\iota_1C_{f,a})
+
(C_{c,a}^\dagger\iota_1-\iota_0C_{f,a}^\dagger)
C_{f,a}
\right].
\end{aligned}
\]

Therefore the exact identity is

\[
\boxed{
R
=
M_c\iota_0-\iota_0M_f
=
\sum_a
\left(
C_{c,a}^\dagger E_a+F_a C_{f,a}
\right).
}
\]

Hence

\[
\boxed{
\|R\|
\le
\sum_a
\left(
\|C_{c,a}\|\|E_a\|
+
\|F_a\|\|C_{f,a}\|
\right).
}
\]

This is the correct graph-changing refinement criterion.

It exposes the real next BQG task:

1. dynamically select the base logical carrier and construct \(\iota_0\);
2. construct a representation/refinement map \(\iota_1\) on the one-hit
   Peter-Weyl graph-changing habitat;
3. measure forward residuals \(E_a\);
4. measure adjoint/return residuals \(F_a\);
5. use the theorem to bound the full master residual and therefore
   \(\epsilon_j^{\rm sf}\).

## Pullback master mismatch from forward residual alone

Even before the return map is controlled, the fine-space pullback of the
coarse master obeys a useful identity.

Using

\[
C_{c,a}\iota_0=\iota_1C_{f,a}+E_a,
\]

and \(\iota_1^\dagger\iota_1=I\),

\[
\boxed{
\iota_0^\dagger M_c\iota_0-M_f
=
\sum_a
\left(
C_{f,a}^\dagger\iota_1^\dagger E_a
+
E_a^\dagger\iota_1C_{f,a}
+
E_a^\dagger E_a
\right).
}
\]

Thus

\[
\boxed{
\|\iota_0^\dagger M_c\iota_0-M_f\|
\le
\sum_a
\left(
2\|C_{f,a}\|\|E_a\|
+
\|E_a\|^2
\right).
}
\]

So one-hit forward refinement already controls the internal dynamical mismatch,
while the additional return residual \(F_a\) is what is needed to control the
full off-carrier master leakage.

This theorem sharpens the fast-closure programme from a single-carrier map to
a compatible refinement of the actual graph-changing constraint habitat.
