# BQG constraint-level refinement bound

Status: **PROVED finite operator theorem.**

This theorem reduces the expensive master-refinement problem to one-hit
constraint intertwiners.

Let the fine and coarse regulated theories have matching Hermitian constraint
families

\[
C_{f,a}=C_{f,a}^\dagger,
\qquad
C_{c,a}=C_{c,a}^\dagger,
\]

and identity constraint metric for clarity,

\[
M_f=\sum_a C_{f,a}^2,
\qquad
M_c=\sum_a C_{c,a}^2.
\]

Let

\[
\iota:\mathcal H_f\to\mathcal H_c
\]

be an isometric refinement embedding.

For any \(s>0\), define the constraint-level residuals

\[
\boxed{
E_a(s)
=
C_{c,a}\iota-s\,\iota C_{f,a}.
}
\]

Then

\[
\begin{aligned}
M_c\iota-s^2\iota M_f
&=
\sum_a
\left(C_{c,a}^2\iota-s^2\iota C_{f,a}^2\right)\\
&=
\sum_a
\left[
C_{c,a}(C_{c,a}\iota-s\iota C_{f,a})
+s(C_{c,a}\iota-s\iota C_{f,a})C_{f,a}
\right].
\end{aligned}
\]

Therefore the exact identity is

\[
\boxed{
R_{s^2}
=
M_c\iota-s^2\iota M_f
=
\sum_a
\big(
C_{c,a}E_a(s)
+
sE_a(s)C_{f,a}
\big).
}
\]

By the operator-norm triangle inequality,

\[
\boxed{
\|R_{s^2}\|
\le
\sum_a
\left(
\|C_{c,a}\|
+s\|C_{f,a}\|
\right)
\|E_a(s)\|.
}
\]

Thus the scale-free projector-control parameter satisfies

\[
\boxed{
\epsilon^{\rm sf}
\le
\inf_{s>0}
\frac{
\sum_a
(\|C_{c,a}\|+s\|C_{f,a}\|)\|E_a(s)\|
}{
\min(\Delta_c,s^2\Delta_f)
}.
}
\]

The major computational consequence is that each \(E_a(s)\) requires only
**one application of the graph-changing constraint** at each scale.

One does not need to explicitly assemble \(C_a^\dagger C_a\), nor apply every
constraint twice, to obtain a rigorous upper bound on the master residual.

For the current sine-Hermitian Peter-Weyl node constraints,

\[
C_a=H_{E,a}^{\rm sine},
\]

the assumptions hold directly.

If the bound tends to zero (or is summable) along the dynamically selected
refinement channel, then the previously proved projector-stability theorem
immediately gives controlled convergence of the physical projectors.

The theorem extends to a positive nontrivial constraint metric \(G\) after
absorbing \(G^{1/2}\) into a stacked constraint operator; the present identity
metric form is the canonical first BQG implementation target.
