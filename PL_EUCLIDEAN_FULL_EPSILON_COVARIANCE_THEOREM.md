# Full-epsilon PL Euclidean covariance theorem

**Status:** exact finite group/representation theorem, conditional only on elementary ordered-term covariance. The theorem does not by itself promote a new production Hamiltonian.

## 1. Finite-regulator problem exposed by the 16-cell test

The current PL Euclidean implementation uses twelve cyclic representatives of the local four-slot epsilon contraction. On the first 16-cell regulator its source column is not a pure sign representation of the full order-eight K=0 pairing stabilizer: the measured sign-irrep power is about `0.88600545`, leaving about `0.11399455` finite-regulator breaking power.

The failure is highly structured: graph transport, dual-edge orientations, K-line recoupling, source-state invariance, sparse support and norm all remain exact. This points to the reduction of the full alternating tensor contraction to twelve cyclic representatives as a mathematically distinct finite-regulator assumption.

## 2. Full alternating operator

Let local slots be labelled `0,1,2,3`. For every ordered quadruple

\[
p=(d,a,b,c)\in S_4
\]

let \(T_p\) denote the physical-sine elementary ordered Euclidean word with omitted slot \(d\) and ordered curvature/triad slots \((a,b,c)\). Define

\[
\boxed{
E_{24}
=\frac12\sum_{p\in S_4}\operatorname{sgn}(p)T_p.
}
\]

The factor `1/2` is a normalization convention: whenever the twelve omitted anti-cyclic terms are exactly redundant by orientation reversal, `E_24` reduces to the historical twelve-term normalization.

## 3. Elementary covariance hypothesis

Let \(h\in S_4\) act by the exact oriented Peter-Weyl/unitary relabelling operator \(U_h\). Suppose the elementary ordered words satisfy

\[
\boxed{
U_hT_pU_h^{-1}=T_{h\cdot p},
}
\]

where

\[
h\cdot(d,a,b,c)=(h(d),h(a),h(b),h(c)).
\]

For the 16-cell regulator the repository already verifies the structural constituents needed by this statement:

1. the coordinate permutation maps every dual edge bijectively and preserves its canonical orientation;
2. for all nodes and local face pairs,
   \[
   h(\mathrm{plaquette}(v,r,s))
   =\mathrm{plaquette}(h(v),h(r),h(s));
   \]
3. the tetrahedral charged absolute volume is invariant under slot relabelling;
4. the oriented Peter-Weyl intertwiner/K-line action is unitary to machine precision.

The remaining numerical full-24 gate is therefore an implementation regression of these composed ingredients, not the source of the group theorem below.

## 4. Theorem: alternating projection is an exact pseudoscalar

Using elementary covariance,

\[
\begin{aligned}
U_hE_{24}U_h^{-1}
&=\frac12\sum_{p\in S_4}\operatorname{sgn}(p)T_{h\cdot p}.
\end{aligned}
\]

Set \(q=h\cdot p\), so \(p=h^{-1}\cdot q\). Since

\[
\operatorname{sgn}(h^{-1}q)
=\operatorname{sgn}(h)\operatorname{sgn}(q),
\]

we obtain

\[
\begin{aligned}
U_hE_{24}U_h^{-1}
&=\frac12\sum_{q\in S_4}
\operatorname{sgn}(h)\operatorname{sgn}(q)T_q\\
&=\boxed{\operatorname{sgn}(h)E_{24}}.
\end{aligned}
\]

Thus the fully antisymmetrized local operator transforms in the alternating one-dimensional irrep \(A_2\) of \(S_4\) **exactly at finite regulator**.

This is not an asymptotic argument and does not rely on GR, HDA, a continuum limit, or fitted coefficients.

## 5. Projector interpretation

Define the alternating projector on the 24-dimensional regular slot orbit,

\[
P_{A_2}=\frac1{24}\sum_{h\in S_4}\operatorname{sgn}(h)U_h.
\]

Then `E_24` is, up to normalization, precisely the alternating projection of any complete ordered-slot orbit. Consequently no component orthogonal to the sign irrep can survive in the fully antisymmetrized operator.

The previously measured finite-regulator breaking

\[
\Delta_{tetra,E}
=1-\frac{\|P_{sign}E_{12}\|^2}{\|E_{12}\|^2}
\simeq0.11399455
\]

therefore has a concrete interpretation: it measures how much the twelve-term cyclic shortcut differs from the exact alternating projection on the first 16-cell regulator.

## 6. Why this is not post-hoc fitting

The correction criterion is purely representation-theoretic:

\[
\epsilon^{abcd}\quad\Longleftrightarrow\quad A_2\text{ of }S_4.
\]

No target value from Einstein gravity, DeWitt kinetics, the HDA defect, a Lorentzian amplitude, or a physical prediction is used to choose the missing twelve terms or their signs. All coefficients are fixed uniquely by permutation parity.

Therefore testing `E_24` is a legitimate operator-covariance correction experiment, not parameter tuning.

## 7. Promotion requirements

Even if the implementation gate confirms machine-precision covariance, the current production operator must **not** be silently replaced. Promotion requires a separately frozen operator-correction addendum and rerunning at least:

1. K5 and 16-cell old-vs-new Euclidean comparison;
2. Euclidean normalization;
3. two-node physical-sine HDA;
4. operator-first route reached-sector tests;
5. tetrahedral charged-volume Lorentzian construction with \(K=[V,E_{24}]\);
6. collective first-order/direct-block symmetry statements;
7. depth-two and collective HDA regressions.

A particularly strong outcome would be

\[
E_{24}^{K5}=E_{12}^{K5}
\]

while

\[
E_{24}^{16cell}\ne E_{12}^{16cell},
\]

because that would preserve the microscopic triangular-regulator core while identifying the correction specifically with nontrivial higher-valence dual 2-cells.

## 8. Scientific consequence

There are now two clean, mutually exclusive routes for the finite symmetry frontier:

- if the full-24 implementation confirms exact covariance and passes the frozen regressions, promote the alternating regulator as the covariant PL continuation;
- if it does not, retain the existing operator and demand
  \[
  \Delta_{tetra,E}(\ell)\to0
  \]
  dynamically under refinement.

In neither route may the operator be selected by which one happens to produce a more GR-like coefficient.
