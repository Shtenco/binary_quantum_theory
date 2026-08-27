# Minimal reversible q=2 history dilation

**Status:** exact finite-dimensional history/unitarity theorem; not yet a derivation of the gravitational physical-projector measure.

The q=2 graph-link carrier has four orthogonal active states

\[
|0\rangle,|1\rangle,|2\rangle,|3\rangle
\]

and one rank-one physical no-link state

\[
|\varnothing\rangle.
\]

The existing matrix-unit theorem shows that active transitions factor through this no-link sector. A new question then becomes unavoidable:

> If the microscopic/history dynamics is reversible or unitary, where is the information about which active channel entered the same rank-one no-link state stored?

The answer is exact: **it must survive in a transition/history channel of dimension at least four.**

---

## 1. Rank-one no-link cannot erase four orthogonal sources reversibly

Suppose a reversible first half-step has the form

\[
|k\rangle
\longmapsto
|\varnothing\rangle\otimes|e_k\rangle.
\]

Because the four source states are orthonormal,

\[
\langle k|l\rangle=\delta_{kl}.
\]

An isometry preserves inner products, therefore

\[
\delta_{kl}
=
\langle\varnothing|\varnothing\rangle
\langle e_k|e_l\rangle
=
\langle e_k|e_l\rangle.
\]

Hence

\[
\boxed{
\langle e_k|e_l\rangle=\delta_{kl}.
}
\]

So the transition/history carrier contains at least four mutually orthogonal states:

\[
\boxed{\dim\mathcal H_{channel}\ge4.}
\]

This is not an optional memory trick. It follows from reversibility.

---

## 2. Minimal history space has dimension eight

The smallest reversible history sector therefore contains

```text
4 active states
+ 4 transition-channel states
= 8 states.
```

Write the transition states as

\[
|m_0\rangle,|m_1\rangle,|m_2\rangle,|m_3\rangle.
\]

For the oriented q=2 Gray cycle define

\[
S_4|k\rangle=|k+1\pmod4\rangle.
\]

Use the basis decomposition

\[
\mathcal H_{hist}=\mathcal H_A\oplus\mathcal H_M.
\]

The minimal carry unitary is

\[
\boxed{
U=
\begin{pmatrix}
0&S_4\\
I_4&0
\end{pmatrix}.
}
\]

Its action is

\[
|k\rangle_A\to|m_k\rangle,
\]

\[
|m_k\rangle\to|k+1\rangle_A.
\]

Therefore

\[
U^2=
\begin{pmatrix}
S_4&0\\
0&S_4
\end{pmatrix}.
\]

In particular, on active states,

\[
\boxed{U^2|k\rangle=|k+1\rangle.}
\]

The full history update has order eight:

\[
\boxed{U^8=I,}
\]

with no smaller positive power equal to the identity.

So the minimal reversible dilation is exactly the connected history cycle

\[
\boxed{C_8.}
\]

---

## 3. Why the physical five-state projection is allowed to look irreversible

Define a forgetting map from history states to instantaneous physical labels:

\[
|k\rangle_A\mapsto|k\rangle_{phys},
\]

\[
|m_k\rangle\mapsto|\varnothing\rangle.
\]

All four orthogonal transition histories project to the same physical no-link state.

Thus the physical snapshot has only

\[
4+1=5
\]

basis labels, while the reversible history carrier has eight.

The projection is necessarily noninvertible:

\[
\boxed{
\text{history}\to\text{instantaneous physical snapshot}
}
\]

forgets transition-channel information.

This is not a contradiction with reversible microscopic/history evolution. It says that **a snapshot is a quotient of the full history description**.

That distinction is potentially important for the repository's separate constraint/projector problem: a state-space object and a physical-history object need not have the same dimension or retain the same information.

---

## 4. `C8` is not `C4 x C2`

The eight history states can be labelled by a pair `(k,s)`, but the dynamics is not the direct-product update.

The actual rule is

```text
(k,0) -> (k,1)
(k,1) -> (k+1,0).
```

The second line is the carry.

Without it one only has

\[
\mathbb Z_4\times\mathbb Z_2,
\]

whose maximum element order is four.

With carry, the update has order eight.

Thus

\[
\boxed{
\text{phase refinement requires a nontrivial history extension, not an independent clock bit.}
}
\]

---

## 5. Relation to complex phase

The coarse `C4` shift contains the real quarter-turn block

\[
J^2=-I.
\]

The minimal reversible history lift has order eight. Its Fourier spectrum contains

\[
\mu_8
=
\left\{
\exp\left(\frac{2\pi i m}{8}\right)
\right\}_{m=0}^{7}.
\]

Therefore the first eighth-root phase resolution does not require inserting a square root of `i` as a new primitive number. It appears as the spectral notation of an ordinary real/integer permutation on the minimal reversible history carrier.

Schematically:

\[
\boxed{
C_4\text{ snapshot phase}
+\text{rank-one no-link bottleneck}
+\text{reversibility}
\to
C_8\text{ history phase}.
}
\]

This is stronger than merely subdividing an edge by hand, because the four distinct midpoint channels are forced by preservation of orthogonality.

---

## 6. What this still does not prove

This theorem closes the **first reversible dilation** only.

It does not prove that:

1. the gravitational physical-projector measure selects this minimal history dilation rather than a larger one;
2. the same rank-one bottleneck/carry structure repeats recursively on every refined phase edge;
3. the resulting all-level tower is dynamically selected rather than kinematically available;
4. the history update is the physical time-evolution operator of generally covariant gravity.

Therefore

```text
C4 -> C8
```

is now supported by an exact minimal reversible history theorem, while

```text
C8 -> C16 -> C32 -> ...
```

remains conditional on recursive physical self-similarity.

---

## 7. Reproduction

```bash
python scripts/q2_minimal_reversible_history_dilation_gate.py \
  --output verification_results/Q2_MINIMAL_REVERSIBLE_HISTORY_DILATION.json
```

The gate checks:

- exact 8x8 integer permutation form;
- orthogonality/unitarity;
- `U^2` equals two copies of the coarse `C4` shift;
- order `U=8`;
- channel Gram rank `4`;
- instantaneous transition projection rank `1`;
- noninvertibility of the 8-to-5 forgetting map.
