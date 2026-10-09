# BQG canonical refinement residual decomposition

Status:
- **PROVED** exact operator identity.
- **PROVED** canonical first BQG carrier embedding \(j=\tfrac12\to j=1\) on the unique \(S_4[2,2]\) doublet.
- **OPEN** theory-specific master residual values for the full graph-changing Hamiltonian/master operator.

## 1. Canonical first BQG refinement embedding

The repository already contains the unique \(S_4\)-intertwiner

\[
W:\mathcal H_{j=1/2}^{[2,2]}
\to
\mathcal H_{j=1}^{[2,2]}
\]

between:

- the full two-dimensional four-spin-\(\tfrac12\) singlet geometry carrier;
- the unique multiplicity-one \(S_4[2,2]\) doublet inside the three-dimensional four-spin-1 singlet space.

In the frozen bases the map is

\[
\boxed{
W=
\begin{pmatrix}
0 & 2/3\\
1 & 0\\
0 & -\sqrt5/3
\end{pmatrix}.
}
\]

It satisfies

\[
\boxed{
W^\dagger W=I_2,
}
\]

and

\[
\boxed{
U_{j=1}(p)W
=
WU_{j=1/2}(p)
\qquad
\forall p\in S_4.
}
\]

The range projector is

\[
\boxed{
P_{22}=WW^\dagger.
}
\]

Thus the first nontrivial representation-RG embedding is symmetry-selected rather than fitted.

---

## 2. Exact residual decomposition

Let

\[
M_f
\]

be the fine operator on the \(j=\tfrac12\) logical carrier and

\[
M_c
\]

the coarse operator on the \(j=1\) carrier.

Define

\[
\boxed{
R=M_cW-WM_f.
}
\]

Insert

\[
I=P_{22}+(I-P_{22}),
\qquad
P_{22}=WW^\dagger.
\]

Then

\[
M_cW
=
(I-P_{22})M_cW
+
WW^\dagger M_cW.
\]

Therefore

\[
\boxed{
R
=
\underbrace{(I-WW^\dagger)M_cW}_{L\;\text{(carrier leakage)}}
+
\underbrace{
W(W^\dagger M_cW-M_f)
}_{W D\;\text{(internal dynamical mismatch)}}.
}
\]

Define

\[
\boxed{
L=(I-WW^\dagger)M_cW,
}
\]

\[
\boxed{
D=W^\dagger M_cW-M_f.
}
\]

Then

\[
\boxed{
R=L+WD.
}
\]

---

## 3. Orthogonality and exact norm reduction

Because

\[
W^\dagger L
=
W^\dagger(I-WW^\dagger)M_cW
=0,
\]

the two residual pieces have orthogonal codomain ranges.

Hence for every vector \(x\),

\[
\|Rx\|^2
=
\|Lx\|^2+\|Dx\|^2.
\]

Equivalently,

\[
\boxed{
R^\dagger R
=
L^\dagger L+D^\dagger D.
}
\]

Therefore

\[
\boxed{
\|R\|^2
=
\lambda_{\max}(L^\dagger L+D^\dagger D).
}
\]

Useful bounds are

\[
\boxed{
\max(\|L\|,\|D\|)
\le
\|R\|
\le
\sqrt{\|L\|^2+\|D\|^2}.
}
\]

Thus the full operator-refinement problem splits exactly into two smaller diagnostics.

---

## 4. Galerkin pullback special case

If the fine effective operator is defined by the canonical pullback

\[
\boxed{
M_f^{\rm Gal}
=
W^\dagger M_cW,
}
\]

then

\[
D=0,
\]

and

\[
\boxed{
R=(I-WW^\dagger)M_cW.
}
\]

So the entire refinement defect is exactly the leakage of coarse dynamics out of the symmetry-selected logical carrier.

This is especially useful computationally because it reduces a potentially huge coarse/fine comparison to a thin off-carrier block.

---

## 5. Exact closure criterion

Exact operator intertwining is equivalent to the simultaneous conditions

\[
\boxed{
L=0,
\qquad
D=0.
}
\]

That is,

\[
\boxed{
(I-WW^\dagger)M_cW=0
}
\]

and

\[
\boxed{
W^\dagger M_cW=M_f.
}
\]

Interpretation:

1. the coarse dynamics preserves the selected logical geometry carrier;
2. once restricted to that carrier, it reproduces the fine dynamics.

This is a much sharper target than comparing full spectra.

---

## 6. Combination with the projector-stability theorem

The companion theorem gives

\[
\|P_cW-WP_f\|
\le
\frac{\|R\|}
{\min(\Delta_f,\Delta_c)}.
\]

Using the exact residual decomposition,

\[
\boxed{
\|P_cW-WP_f\|
\le
\frac{
\sqrt{\lambda_{\max}(L^\dagger L+D^\dagger D)}
}{
\min(\Delta_f,\Delta_c)
}.
}
\]

Therefore the BQG continuum/refinement problem reduces to proving that both

\[
\boxed{
\frac{\|L_d\|}{\Delta_{\min,d}}\to0
}
\]

and

\[
\boxed{
\frac{\|D_d\|}{\Delta_{\min,d}}\to0.
}
\]

A sufficient summability condition is

\[
\boxed{
\sum_d
\frac{
\sqrt{\|L_d\|^2+\|D_d\|^2}
}{
\Delta_{\min,d}
}
<\infty.
}
\]

---

## 7. Immediate BQG consequence

For the first registered \(j=\tfrac12\to1\) step, the embedding \(W\) is already fixed uniquely by \(S_4\) symmetry.

Therefore there is no remaining projector-choice ambiguity at this RG step.

The next calculation is now completely specified:

### Fine operator

Use the frozen \(j=\tfrac12\) Peter-Weyl logical master/Hamiltonian block.

### Coarse operator

Recompute the same declared operator with all four incident face spins \(j=1\), then project to the full three-dimensional singlet carrier.

### Measure

Compute

\[
L_{1/2\to1}
=
(I-WW^\dagger)M_{j=1}W,
\]

\[
D_{1/2\to1}
=
W^\dagger M_{j=1}W-M_{j=1/2},
\]

and

\[
\boxed{
\epsilon_{1/2\to1}
=
\frac{\|R\|}
{\min(\Delta_{1/2},\Delta_1)}.
}
\]

This is the first genuine BQG refinement datum required by the fast-closure programme.

---

## 8. Symmetry-protected observable sector

For any coarse operator \(O_c\) that commutes with the full \(S_4\) action, Schur's lemma implies that its restriction to the multiplicity-one \([2,2]\) carrier is scalar:

\[
\boxed{
W^\dagger O_cW=\lambda_c I_2.
}
\]

The existing \(j=1\) absolute-volume calculation is an example:

\[
W^\dagger V_{j=1}W
=
3^{1/4}I_2
\]

within the registered numerical spectral tolerance.

Thus the embedding already intertwines the symmetry class of isotropic scalar observables up to their scale normalization.

Nontrivial RG information necessarily first appears in operators that resolve shape/orientation/dynamical structure rather than pure \(S_4\)-scalar observables.

---

## 9. Scientific consequence

The shortest continuum programme is now not

\[
\text{depth }4\to6\to8\to10\text{ brute force}.
\]

It is

\[
\boxed{
W_d
\to
(L_d,D_d)
\to
R_d
\to
\epsilon_d
\to
P_\infty.
}
\]

The huge matrices matter only insofar as they determine the thin refinement residual blocks and the master gaps.

This is the computational compression needed for the BQG fast-closure route.
