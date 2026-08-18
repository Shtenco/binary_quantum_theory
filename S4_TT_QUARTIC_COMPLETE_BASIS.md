# Complete parity-even S4 quartic TT basis

Status: **exact finite representation/constraint quotient.**  This document corrects the too-restrictive idea that a generic directed momentum kernel can always be written as three fixed S4 orbit functions `a I+b A+c O`.

The correct covariance law at nonzero momentum is

\[
\boxed{
C(g\mathbf k)=U_g\,C(\mathbf k)\,U_g^{-1},
\qquad g\in S_4,
}
\]

not `C(g k)=C(k)` at a fixed generic direction.  A direction therefore carries its own `S4` representation data.

At `k=0`, for an onsite kernel, for an angular average, or at a momentum fixed by the full stabilizer, the familiar three-orbit reduction remains exact.  At generic nonzero `k`, additional covariant tensor structures are allowed.

---

## 1. Why the unrestricted quartic metric sector has 13 traceless-spin-2 invariants

The five traceless metric components transform as

\[
H_5=E\oplus T_2.
\]

Their symmetric quadratic products decompose as

\[
\boxed{
\mathrm{Sym}^2(H_5)
=2A_1\oplus2E\oplus T_1\oplus2T_2.
}
\]

The spatial vector transforms as the three-dimensional `T2` irrep.  Homogeneous quartic momentum polynomials have

\[
\boxed{
\mathrm{Sym}^4(T_2)
=2A_1\oplus2E\oplus T_1\oplus2T_2.
}
\]

Therefore the number of `S4` singlets before imposing physical TT constraints is

\[
2^2+2^2+1^2+2^2
=\boxed{13}.
\]

This is the correct general representation count.  A single `Q_tet` operator is a useful restricted subfamily, not the most general quartic kernel.

---

## 2. Exact TT quotient: 13 collapses to six physical quartic structures

Write a real symmetric spatial perturbation as

\[
h=
\begin{pmatrix}
h_{xx}&h_{xy}&h_{xz}\\
h_{xy}&h_{yy}&h_{yz}\\
h_{xz}&h_{yz}&h_{zz}
\end{pmatrix}.
\]

The physical tensor sector obeys

\[
\boxed{
\operatorname{tr}h=0,
\qquad
h_{ij}k_j=0.
}
\]

The executable gate constructs the complete degree-`h^2 k^4` monomial space and the exact signed-permutation realization of the 24-element tetrahedral `S4` action.

For the full six-component symmetric metric carrier it finds 19 nonzero Reynolds-orbit invariants at bidegree `(2,4)`.  The linear ideal generated at that bidegree by

```text
tr(h)=0
h.k=0
```

has exact rank

\[
222.
\]

Appending the 19 invariant orbit vectors raises the exact rank to

\[
228.
\]

Hence the dimension of their restriction to the physical TT quotient is

\[
\boxed{
228-222=6.
}
\]

Therefore

\[
\boxed{
\dim \mathcal W^{(4)}_{TT,S_4}=6.
}
\]

This is the complete parity-even quartic TT response space for the stated spatial `S4` symmetry and no extra dynamical assumptions.

---

## 3. A simple canonical Reynolds basis

Define the group average

\[
\mathcal R[f]
=\frac1{24}\sum_{g\in S_4}f(g\cdot h,g\cdot k).
\]

A particularly sparse six-element basis of the TT quotient is

\[
\boxed{
W_1=\mathcal R[h_{xx}^2k_z^4],
}
\]

\[
\boxed{
W_2=\mathcal R[h_{xx}^2k_x^4],
}
\]

\[
\boxed{
W_3=\mathcal R[h_{xy}^2k_z^4],
}
\]

\[
\boxed{
W_4=\mathcal R[h_{xy}^2k_y^4],
}
\]

\[
\boxed{
W_5=\mathcal R[h_{xx}^2k_y^2k_z^2],
}
\]

\[
\boxed{
W_6=\mathcal R[h_{xx}^2k_x^2k_z^2].
}
\]

Because all seed powers are even, these can be written transparently as

\[
W_1=\frac16\sum_{i\ne j}h_{ii}^2k_j^4,
\]

\[
W_2=\frac13\sum_i h_{ii}^2k_i^4,
\]

\[
W_3=\frac13\left(
h_{xy}^2k_z^4+h_{xz}^2k_y^4+h_{yz}^2k_x^4
\right),
\]

\[
W_4=\frac16\left[
h_{xy}^2(k_x^4+k_y^4)
+h_{xz}^2(k_x^4+k_z^4)
+h_{yz}^2(k_y^4+k_z^4)
\right],
\]

\[
W_5=\frac13\left(
h_{xx}^2k_y^2k_z^2
+h_{yy}^2k_x^2k_z^2
+h_{zz}^2k_x^2k_y^2
\right),
\]

\[
W_6=\frac16\sum_{i\ne j}h_{ii}^2k_i^2k_j^2.
\]

Every parity-even quartic physical TT kernel with the stated tetrahedral symmetry can therefore be represented, modulo the TT constraints, as

\[
\boxed{
\delta K_{TT}^{(4)}
=a_*^2\sum_{r=1}^{6}c_r W_r.
}
\]

The six `c_r` are the general quartic TT Wilson coefficients in this basis.

---

## 4. Familiar restricted structures are fixed linear combinations

The rotationally invariant TT operator

\[
(h_{ij}h_{ij})(k^2)^2
\]

has the exact TT-quotient representation

\[
\boxed{
I_{iso}
=6W_1+24W_2+6W_3+36W_4-9W_5+18W_6.
}
\]

The old scalar cubic-harmonic ansatz

\[
Q_4^{cub}(\hat k)\,(h_{ij}h_{ij})k^4,
\qquad
Q_4^{cub}=\sum_i\hat k_i^4-\frac35,
\]

is another one-dimensional direction in the six-dimensional space:

\[
\boxed{
I_{Q4}
=\frac15\left(
12W_1-57W_2+12W_3-48W_4+27W_5-54W_6
\right).
}
\]

Likewise the momentum-scalar tetrahedral spin-2 splitter

\[
k^4\,h:Q_{tet}h
\]

is

\[
\boxed{
I_{Q_{tet}}
=\frac15\left(
18W_1-33W_2-12W_3-72W_4+48W_5+24W_6
\right).
}
\]

Thus the earlier `eta2 + zeta4 Q4` and single-`Q_tet` models remain valid **restricted hypotheses**, but neither spans the complete general `S4` quartic TT sector.

---

## 5. Three high-symmetry directions are one equation short

A complete blind extraction should not choose a tensor ansatz after opening microscopic data.

Choose deterministic TT plus/cross frames tied to the microscopic cubic axes.  The three high-symmetry propagation directions

```text
(100), (110), (111)
```

provide only rank five for the general six-coefficient quartic TT basis.

This explains why a three-direction scalar extractor can look complete while silently missing one allowed TT structure.

Add one preregistered generic direction

\[
\boxed{(120)}
\]

and the extraction becomes full rank.

---

## 6. Exact six-observable extractor

Let the six quartic TT observables be

\[
y=
\begin{pmatrix}
K_{++}^{(4)}(100)\\
K_{\times\times}^{(4)}(100)\\
K_{++}^{(4)}(110)\\
K_{\times\times}^{(4)}(110)\\
K_{++}^{(4)}(111)\\
K_{++}^{(4)}(120)
\end{pmatrix},
\]

where lower derivative pieces have already been subtracted and a common normalization convention has been frozen.

For the ordered Wilson vector

\[
c=(c_1,c_2,c_3,c_4,c_5,c_6)^T,
\]

\[
\boxed{y=A c}
\]

with

\[
A=
\begin{pmatrix}
1/6&0&0&0&0&0\\
0&0&1/6&0&0&0\\
5/96&1/48&0&1/96&1/24&1/96\\
0&0&1/24&1/48&0&0\\
1/81&1/81&1/81&1/81&1/81&1/81\\
341/3750&16/1875&0&17/1875&2/75&17/1875
\end{pmatrix}.
\]

Its determinant is exactly

\[
\boxed{
\det A=\frac1{699840000}\ne0.
}
\]

Therefore the six Wilson coefficients are uniquely reconstructible with no tensor fit ambiguity.

The exact inverse is

\[
\boxed{
A^{-1}=\begin{pmatrix}
6&0&0&0&0&0\\
219/4&-3&88&0&81/2&-625/4\\
0&6&0&0&0&0\\
0&-12&0&48&0&0\\
-105/4&3&8/3&0&-81/2&625/12\\
-69/2&6&-272/3&-48&81&625/6
\end{pmatrix}.
}
\]

This matrix should be frozen before the production momentum kernel is opened.

---

## 7. What becomes of eta2 and zeta4

The general theory should first report the full six-vector

\[
\boxed{c^{IR}=(c_1,\ldots,c_6)^{IR}}.
\]

Only after that may one project it onto declared subspaces such as

- the rotationally invariant direction `I_iso`;
- the scalar cubic harmonic `I_Q4`;
- the single tetrahedral spin-2 splitter `I_Qtet`.

If the five anisotropic combinations orthogonal to the isotropic direction are statistically compatible with the one-dimensional `I_Q4` hypothesis, then the older two-number notation

\[
\{\eta_2,\zeta_4\}
\]

is sufficient.

If not, the theory has made a **stronger six-coefficient prediction**, and it is scientifically wrong to compress that result into a post-hoc `zeta4`.

---

## 8. Corrected physicalization chain

The fully general chain is now

\[
\boxed{
\text{Peter--Weyl interblock dynamics}
\to C_{6,PQ}(\omega)
\to C_6(\omega,\mathbf k)
\to K_{TT}
\to c_1,\ldots,c_6
\to \text{restricted projections only if passed}
\to \text{real propagation / polarization observables}.
}
\]

The old three-orbit `a,b,c` onsite kernel remains an essential local input.  It is not, by itself, the complete generic momentum-dependent tensor kernel.

This correction makes the blind test harder and therefore more meaningful.
