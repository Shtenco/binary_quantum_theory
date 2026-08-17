# Exact PL Euclidean 12-term / 24-term epsilon equivalence theorem

**Status:** exact operator-word theorem. This result retracts the hypothesis that merely restoring the omitted twelve anti-cyclic permutations can repair the finite 16-cell pairing-stabilizer covariance defect.

## 1. Question

The current PL Euclidean operator uses, for each omitted local slot `d`, the three cyclic orders of the remaining slots `(a,b,c)`. A natural covariance experiment was to replace this 12-term sum by the formally complete 24-term Levi-Civita sum

\[
E_{24}=\frac12\sum_{(d,a,b,c)\in S_4}\operatorname{sgn}(d,a,b,c)\,E_{abc}.
\]

The factor `1/2` was chosen so that the normalization would agree with the historical operator if the three missing anti-cyclic terms were exact negatives of the three cyclic terms.

That condition is not merely approximately true: it is an exact identity of the implemented operator words.

## 2. Exact ordered-word identity

For fixed source node `v` and fixed third slot `c`, the Peter-Weyl engine constructs

\[
T(v;a,b,c)
\]

from two base words and the oriented dual plaquette pair

\[
P_f=P(v;a,b),\qquad P_r=P(v;b,a).
\]

At sequence level the combination is

\[
T(v;a,b,c)
\propto
(B_1-B_2)(P_f-P_r).
\]

Swapping the first two local slots exchanges the forward and reverse dual loops while leaving the `c`-leg base word unchanged:

\[
P(v;b,a)=P_r,
\qquad
P(v;a,b)=P_f.
\]

Therefore

\[
\boxed{
T(v;b,a,c)=-T(v;a,b,c)
}
\]

exactly.

The repository's `adjoint_sequence` reverses each elementary sequence linearly without changing its external coefficient. Hence the same identity holds for the direct-adjoint ordered word:

\[
\boxed{
T^\dagger_{dir}(v;b,a,c)=-T^\dagger_{dir}(v;a,b,c).
}
\]

No cutoff, volume spectrum, CG coefficient, state, or continuum approximation enters this statement.

## 3. Exhaustive finite PL check

The executable gate compares the actual `T_sequences` multisets on the 16-cell dual complex.

For every

```text
16 source nodes
x 4 choices of first slot a
x 3 distinct choices of b
x 2 distinct choices of c
= 384 ordered cases
```

it verifies

\[
\mathcal T(v;b,a,c)=-\mathcal T(v;a,b,c)
\]

at the exact tuple/coefficient level.

Result:

```text
384 cases checked
0 failures
```

Because the proof uses only the way `T_sequences` is built, the identity is structural for this PL engine, not a numerical coincidence of one seed state.

## 4. Why the missing twelve terms are redundant

For fixed omitted slot `d`, write the sorted remaining slots as `(a,b,c)`. The historical operator contains the three cyclic orders

\[
(a,b,c),\quad(b,c,a),\quad(c,a,b).
\]

The three anti-cyclic orders can be paired as

\[
(b,a,c),\quad(c,b,a),\quad(a,c,b),
\]

which are obtained by swapping the first two entries of the corresponding cyclic term while keeping the third entry fixed.

Their permutation parity is opposite, and their ordered word is also opposite. Consequently the two minus signs cancel:

\[
\operatorname{sgn}(d,b,a,c)T_{bac}
=
\operatorname{sgn}(d,a,b,c)T_{abc}.
\]

Thus every anti-cyclic term duplicates one cyclic contribution in the fully alternating sum. With the normalization `1/2`,

\[
\boxed{E_{24}=E_{12}}
\]

as an operator identity.

The equality holds separately for the forward and direct-adjoint pieces and therefore also for the physical-sine Hermitian combination.

## 5. Consequence for the measured finite covariance defect

The first 16-cell source column previously gave full-H sign-irrep power

\[
\frac{\|P_{sign}E\|^2}{\|E\|^2}
=0.8860054496057664,
\]

so the finite symmetry-breaking power is

\[
\Delta_{tetra,E}=0.1139945503942336.
\]

Because `E_24=E_12`, adding the omitted anti-cyclic permutations cannot change this number at all.

Therefore the finite pairing-stabilizer defect is **not** caused by an incomplete 12-versus-24 Levi-Civita sum.

## 6. What the failed full-H assumption really means

The abstract group statement

\[
U_hE_{24}U_h^{-1}=\operatorname{sgn}(h)E_{24}
\]

would follow if every elementary ordered word transformed by pure slot relabelling,

\[
U_hT_pU_h^{-1}=T_{h\cdot p}.
\]

Since `E_24=E_12` but the measured source column is not a pure sign representation of the full order-eight pairing stabilizer, that elementary covariance hypothesis cannot hold for the complete implemented `T` word under all those `h`.

The defect must therefore live deeper than the cyclic/anti-cyclic bookkeeping. The structurally distinguished object is the third slot `c`, because it selects

\[
cnode=neighbor(v,c)
\]

and hence the open triad/holonomy leg entering the Thiemann word. Transformations that only exchange the first curvature-pair slots can survive exactly, while transformations moving the third slot need not act as a one-dimensional character on the finite regulator.

This matches the measured exact surviving subgroup

\[
\{e,(01)\}\cong C_2,
\]

where the passing nontrivial element swaps precisely the first curvature-pair slots and leaves the third-slot role intact for the relevant terms.

## 7. Scientific next step

Do **not** promote a 24-term replacement: it is exactly the same operator.

The correct next discriminator is instead to separate the local ordered word into its slot-role representation and determine whether the `c`-leg asymmetry is:

1. an irrelevant finite-regulator artifact whose non-sign irreps decay under refinement, or
2. a genuine regulator-ordering defect requiring a target-independent symmetrization over the distinguished triad leg / full tetrahedral orbit.

Any such operator modification must be justified by locality/covariance alone and must rerun the frozen Euclidean normalization, HDA, route, Lorentzian, and collective regressions before physical promotion.

## 8. Relation to the earlier full-epsilon experiment

`PL_EUCLIDEAN_FULL_EPSILON_COVARIANCE_THEOREM.md` remains mathematically correct as a conditional alternating-projection theorem, but its proposed practical repair route is superseded by this stronger identity: the current engine already makes the omitted anti-cyclic half redundant.

The heavy full-24 amplitude experiment is therefore unnecessary for deciding this question.
