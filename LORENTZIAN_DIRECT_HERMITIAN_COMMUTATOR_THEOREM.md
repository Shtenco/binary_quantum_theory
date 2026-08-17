# Exact direct-Hermitian Lorentzian commutator theorem

**Status:** exact operator identity for the frozen v1.3 Lorentzian word.  It changes no operator, cutoff, charged-volume definition, normalization, orientation coefficient or science threshold.

## 1. Starting point

For one omitted local slot `d`, let `(a,b,c)` denote one of the three cyclic orders of the remaining slots.  Write

\[
A_a=C_a(K),\qquad B_b=C_b(K),\qquad V_c=C_c(V_{tet}).
\]

The frozen raw Lorentzian sum contains all six permutations with Levi-Civita parity,

\[
L_d
=\eta_d\sum_{\pi\in S_3}\operatorname{sgn}(\pi)
\operatorname{Tr}_{aux}
\big(A_{\pi_1}A_{\pi_2}V_{\pi_3}\big),
\]

with the same local PL orientation coefficient `eta_d` already used by V2.

The production component adjoint identities are

\[
C_a(K)_{ij}^\dagger=-C_a(K)_{ji},
\qquad
C_c(V)_{ij}^\dagger=C_c(V)_{ji},
\]

because `K=[V,E]` is anti-Hermitian and `V` is Hermitian.

No tetrahedral covariance assumption is used below.

## 2. Exact six-to-three raw reduction

Pair every cyclic order `(a,b,c)` with its first-two swap `(b,a,c)`.  Their epsilon signs are opposite, hence

\[
\begin{aligned}
&\operatorname{Tr}_{aux}(A_aA_bV_c)
-
\operatorname{Tr}_{aux}(A_bA_aV_c)\\
&\qquad=
\boxed{\operatorname{Tr}_{aux}([A_a,A_b]V_c)}.
\end{aligned}
\]

Therefore the complete six-term raw orbit for fixed omitted slot is **exactly**

\[
\boxed{
L_d
=\eta_d\sum_{(a,b,c)\in cyclic}
\operatorname{Tr}_{aux}([C_a(K),C_b(K)]C_c(V)).
}
\]

This is an algebraic identity and does not rely on the failed order-eight pairing-stabilizer pseudoscalar hypothesis.

## 3. Direct Hermitian completion

For

\[
X_{abc}=\operatorname{Tr}_{aux}([A_a,A_b]V_c),
\]

the component adjoint identities give

\[
[A_a,A_b]^\dagger=-[A_a,A_b]
\]

and hence

\[
X_{abc}^\dagger
=-\operatorname{Tr}_{aux}(V_c[A_a,A_b]).
\]

The physical v1.3 Hermitian Lorentzian block is

\[
S=-\frac{i}{2}(L_{raw}-L_{raw}^\dagger).
\]

Substitution yields the exact direct form

\[
\boxed{
S
=-\frac{i}{2}
\sum_d\eta_d
\sum_{(a,b,c)\in cyclic}
\operatorname{Tr}_{aux}
\left(
\{[C_a(K),C_b(K)],C_c(V)\}
\right).
}
\]

Thus physical `S` can be produced directly as twelve Hermitian commutator--anticommutator words (`4 omitted slots x 3 cyclic orders`) instead of first materializing a 24-term forward raw column and a separate 24-term direct-adjoint raw column.

## 4. Hermiticity is built in before projection

Let

\[
Y_{abc}=\{[A_a,A_b],V_c\}.
\]

Since `[A_a,A_b]` is anti-Hermitian and `V_c` Hermitian,

\[
Y_{abc}^\dagger=-Y_{abc}.
\]

Therefore

\[
\boxed{-\frac i2Y_{abc}}
\]

is Hermitian term by term, before sparse state assembly, scalar Gauss projection, or summation over omitted slots.

This is stronger numerically than subtracting two independently accumulated large raw columns after the fact: cancellations required by Hermiticity can occur inside each physical pair.

## 5. Why this is not the blocked V3 symmetry reduction

The failed V3 shortcut attempted to reconstruct different slot words using a finite-regulator tetrahedral stabilizer.  This theorem does nothing of the kind.

It uses only:

1. the epsilon antisymmetry already present in the definition;
2. the exact algebraic identity `AB-BA=[A,B]`;
3. the already frozen adjoint properties of `C(K)` and `C(V)`.

Therefore it remains valid even when the finite 16-cell Euclidean column has nonzero tetrahedral symmetry-breaking power.

## 6. Production promotion contract

Before replacing the 48-term V2 execution path, a direct-Hermitian implementation must pass all of the following without changing thresholds after seeing amplitudes:

1. exact symbolic/random-matrix identity against the original 24-forward + 24-adjoint formula;
2. K5 finite Peter--Weyl comparison against the historical full collector where that result is already reproducible;
3. at least one direct 16-cell cyclic physical pair compared against the sum of its two V2 forward and two V2 adjoint ordered terms;
4. same `V_tet`, `Jmax2=7`, zero-aware spectrum, scalar projection and leakage guards as V2;
5. no lower bound on `||S||`;
6. provenance must state `direct-hermitian-commutator-v4`.

Only then may the direct twelve-word producer replace the cancelled V2 48-term execution as C1.

## 7. Computational significance

The theorem does not claim a formal reduction in the number of primitive noncommuting operator products from 48 to 12; each anticommutator/commutator contains four orderings.  Its advantage is structural:

- the four orderings of one physical word share the same local caches;
- opposite epsilon partners are combined before scalar projection;
- forward/adjoint cancellation is local to one physical word;
- Hermiticity is exact by construction;
- no global slot-symmetry assumption is required.

This is the shortest scientifically safe route to the corrected finite Lorentzian C1 result currently available in the repository.
