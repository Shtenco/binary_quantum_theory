# BQG S4 logical-carrier multiplicity theorem and uniqueness NO-GO

Status:
- **PROVED**: exact multiplicity formula for the \(S_4[2,2]\) sector in the equal-spin four-valent singlet space.
- **NO-GO / PROVED**: \(S_4\) symmetry alone does not select a unique two-dimensional logical geometry carrier at all Peter-Weyl scales.

## 1. Equal-spin four-valent singlet space

Let

\[
\mathcal H_j^{\rm sing}
=
\mathrm{Inv}_{SU(2)}(V_j^{\otimes4}).
\]

Using the standard pair-coupling basis \(K=0,1,\dots,2j\),

\[
\boxed{
\dim \mathcal H_j^{\rm sing}=2j+1.
}
\]

Write

\[
n=2j\in\mathbb Z_{\ge1}.
\]

The permutation group \(S_4\) acts by permuting the four equal-spin legs.

We ask for the multiplicity of the two-dimensional irrep \([2,2]\).

---

## 2. Character formula

For a permutation \(\pi\in S_4\), the trace on the invariant subspace can be written as the group integral

\[
\chi_j^{\rm sing}(\pi)
=
\int_{SU(2)} dg\;
\prod_{c\in{\rm cycles}(\pi)}
\chi_j(g^{|c|}).
\]

For the three conjugacy classes that enter the \([2,2]\) character projection one obtains

\[
\boxed{
\chi_j^{\rm sing}(1^4)=n+1,
}
\]

\[
\boxed{
\chi_j^{\rm sing}(2^2)=n+1,
}
\]

and

\[
\boxed{
\chi_j^{\rm sing}(3,1)=
\begin{cases}
+1,& n\equiv0\pmod3,\\
-1,& n\equiv1\pmod3,\\
0,& n\equiv2\pmod3.
\end{cases}
}
\]

The double-transposition identity is also immediate in the pair basis: both pair swaps carry the same exchange parity and their product is \(+1\) on every singlet basis vector.

The periodic three-cycle trace follows by inserting the finite SU(2) character series into the class integral and extracting the Haar-singlet coefficient.

---

## 3. Exact multiplicity of \([2,2]\)

The \(S_4\) character of \([2,2]\) is

\[
\chi_{[2,2]}
=
(2,0,2,-1,0)
\]

on the classes

\[
(1^4),(2,1,1),(2^2),(3,1),(4).
\]

Hence character orthogonality gives

\[
m_{[2,2]}
=
\frac1{24}
\left[
2\chi(1^4)
+
3\cdot2\chi(2^2)
-
8\chi(3,1)
\right].
\]

Substituting the exact traces,

\[
m_{[2,2]}
=
\frac{n+1-\chi(3,1)}{3}.
\]

Evaluating the three congruence classes of \(n\) gives

\[
\boxed{
m_{[2,2]}(j)
=
\left\lceil\frac{n}{3}\right\rceil
=
\left\lceil\frac{2j}{3}\right\rceil.
}
\]

This is the exact multiplicity theorem.

---

## 4. Immediate consequence

The first scales are

\[
\begin{array}{c|c}
j & m_{[2,2]}\\
\hline
1/2 & 1\\
1 & 1\\
3/2 & 1\\
2 & 2\\
5/2 & 2\\
3 & 2\\
7/2 & 3\\
4 & 3
\end{array}
\]

Therefore

\[
\boxed{
m_{[2,2]}=1
\quad\Longleftrightarrow\quad
j\in\left\{\frac12,1,\frac32\right\}
}
\]

within the positive equal-spin tower.

Already at

\[
\boxed{j=2}
\]

there are two symmetry-equivalent \([2,2]\) copies.

---

## 5. NO-GO for the naive all-scale logical-qubit tower

The \(j=\frac12\to1\) canonical intertwiner is unique up to phase because both scales contain a multiplicity-one \([2,2]\) irrep.

The same remains true for \(j=1\to\frac32\).

But for \(j\ge2\),

\[
\boxed{
S_4\text{ symmetry alone cannot select one unique }[2,2]\text{ copy}.
}
\]

Therefore the naive proposal

\[
\boxed{
\text{one symmetry-selected logical qubit at every }j
}
\]

is false.

**Status: NO-GO / PROVED.**

---

## 6. Physical meaning

This is not a failure of refinement.

It says that from \(j=2\) onward the coarse geometry contains an additional **multiplicity space**.

Schematically,

\[
\mathcal H_j^{\rm sing}
\supset
\mathbb C^{m_{22}(j)}
\otimes
V_{[2,2]}.
\]

The two-dimensional \(V_{[2,2]}\) factor is the familiar logical shape qubit.

The new factor

\[
\boxed{
\mathbb C^{m_{22}(j)}
}
\]

contains genuinely new coarse-scale information not fixed by tetrahedral permutation symmetry.

Thus the correct refinement carrier is not merely a qubit, but

\[
\boxed{
\text{multiplicity channel}
\otimes
\text{logical shape qubit}.
}
\]

---

## 7. New fast-closure problem

From \(j=2\) onward the dynamics must select or evolve the multiplicity channel.

The correct next object is the coarse master/return operator restricted to the full \([2,2]\)-isotypic sector,

\[
P_{22}^{(j)} M_j P_{22}^{(j)}.
\]

Because \(M_j\) is \(S_4\)-equivariant, Schur's lemma implies

\[
\boxed{
P_{22}^{(j)}M_jP_{22}^{(j)}
=
A_j\otimes I_2,
}
\]

where

\[
A_j
\]

acts only on the multiplicity space.

Therefore the all-scale RG problem collapses to the much smaller matrix sequence

\[
\boxed{
A_{1/2},A_1,A_{3/2},A_2,A_{5/2},\dots
}
\]

rather than the full four-valent Hilbert spaces.

At the first three scales \(A_j\) is scalar because \(m_{22}=1\).

At \(j=2\), \(A_2\) is the first nontrivial \(2\times2\) multiplicity-space operator.

This is the new minimal dynamical selection test.

---

## 8. Revised fast-closure route

The refinement programme is therefore sharpened to

\[
\boxed{
\text{exact }S_4\text{ isotypic decomposition}
\to
A_j
\to
\text{selected low-energy multiplicity channel}
\to
\iota_j
\to
R_j
\to
\epsilon_j
\to
P_\infty.
}
\]

This is stronger than assuming a fixed qubit carrier by hand.

---

## 9. Numerical regression

The companion gate independently builds the exact permutation matrices from the repository recoupling tensors for

\[
j=\frac12,1,\frac32,\dots
\]

and verifies

\[
\boxed{
m_{[2,2]}(j)=\left\lceil\frac{2j}{3}\right\rceil.
}
\]

It also constructs the central \([2,2]\) projector and checks

\[
\operatorname{rank}P_{22}^{(j)}
=
2m_{[2,2]}(j).
\]

The finite scan is a regression of the analytic theorem, not its proof.
