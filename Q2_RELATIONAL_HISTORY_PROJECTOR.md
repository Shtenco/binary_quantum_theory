# q=2 relational history: combined constraint projector versus clock-only averaging

## Why this note exists

The history-character audit established a genuine no-go:

\[
P_0=\frac1N\sum_t U^t
\]

projects onto the trivial history character and kills nontrivial phase/current sectors if the history shift itself is treated as pure gauge.

That result remains correct.

The missing distinction is between:

1. **clock-only averaging**, and
2. **relational averaging of a combined clock + system constraint**.

The second is the finite-dimensional Page–Wootters/rigging-map mechanism.

This note implements it as an exact positive control on the already-derived C8 history carrier.

---

## 1. A separate clock and system step

Let the clock have eight orthonormal readings

\[
|t\rangle,\qquad t\in\mathbb Z_8,
\]

with shift

\[
S|t\rangle=|t+1\rangle.
\]

For the system positive control use the already-derived q=2 real complex structure

\[
R=J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
\qquad J^2=-I,
\qquad J^8=I.
\]

Define the combined constraint step

\[
\boxed{
G=S_{\rm clock}\otimes R_{\rm geom}.
}
\]

This does **not** assert that `R=J` is the physical gravitational evolution operator. It is a structural positive control chosen because it is already derived inside the q=2 carrier.

---

## 2. Relational history state

For a system seed `|psi0>` define

\[
\boxed{
|\Psi\rangle
=\frac1{\sqrt8}\sum_{t=0}^{7}
|t\rangle\otimes R^t|\psi_0\rangle.
}
\]

Then

\[
G|\Psi\rangle=|\Psi\rangle.
\]

So the global history is exactly invariant under the combined constraint.

Yet conditioning on clock reading `t` gives

\[
\boxed{
|\psi(t)\rangle=R^t|\psi_0\rangle,
}
\]

and therefore

\[
|\psi(t+1)\rangle=R|\psi(t)\rangle.
\]

Thus global gauge invariance and nontrivial relational evolution are not contradictory.

---

## 3. Combined rigging projector

The finite group average is

\[
\boxed{
P_{\rm rel}
=\frac18\sum_{\tau=0}^{7}G^\tau.
}
\]

It is exactly Hermitian and idempotent.

Starting from one gauge-orbit representative

\[
|0\rangle\otimes|\psi_0\rangle,
\]

its normalized projection is exactly the relational history state above.

So the history state does not need to be inserted independently once the combined constraint is specified.

---

## 4. Why clock-only averaging fails

Clock-only averaging is

\[
P_{\rm clock}
=\left(\frac18\sum_{\tau=0}^{7}S^\tau\right)\otimes I.
\]

For the nontrivial q=2 positive-control history,

\[
\boxed{
P_{\rm clock}|\Psi\rangle=0.
}
\]

This reproduces the earlier no-go exactly.

The conclusion is therefore not that group averaging is impossible. The conclusion is that **the object being averaged matters**:

- averaging the clock/history shift alone removes nontrivial phase;
- averaging the total relational constraint preserves clock-system correlations.

---

## 5. Character matching

For C8 let

\[
\zeta=e^{2\pi i/8}.
\]

The system step `J` has eigencharacters

\[
+i=\zeta^2,
\qquad
-i=\zeta^6.
\]

The combined constraint requires total character one, so clock and system characters obey

\[
m_{\rm clock}+r_{\rm system}=0\pmod8.
\]

The exact projector decomposes as

\[
\boxed{
P_{\rm rel}
=P^{\rm clock}_{6}\otimes Q_{+i}
+P^{\rm clock}_{2}\otimes Q_{-i}.
}
\]

For the chosen real seed the two matched sectors each carry weight `1/2`.

The clock trivial character `m=0` has zero weight in this history.

This is the precise mechanism by which a globally invariant state can retain nontrivial relational phase information.

---

## 6. What this resolves

It resolves a conceptual ambiguity in the previous phase/projector frontier.

The statements

```text
untwisted clock-only averaging kills nontrivial phase
```

and

```text
a gauge-invariant relational history can have nontrivial conditional phase evolution
```

are simultaneously true.

The correct relational object is a **combined constraint projector**, not the trivial-character projector of the clock alone.

---

## 7. What remains physically open

This is not yet the physical projector of the candidate gravity theory.

Still required:

1. derive a genuine clock or boundary-history degree of freedom from the microscopic q=2 construction;
2. derive the corresponding system step from the actual graph-changing Euclidean/Lorentzian constraint rather than choosing `R=J` as a positive control;
3. define the physical inner product / rigging map in the continuum or refinement limit;
4. insert metric sources and derive the connected generating functional;
5. obtain `Gamma[g]` and `Gamma^(2)_metric`;
6. only then identify a physical TT frequency/pole and compute the six Wilson coefficients;
7. only after a legitimate history-current coupling exists may one speak about `g_YC^gravity`.

The new exact architecture is therefore

\[
\boxed{
\text{constraint}
\to \text{combined relational projector}
\to \text{conditional history}
}
\]

rather than

\[
\text{clock shift}\to\text{untwisted clock-only average}.
\]
