# q=2 history -> winding and phase refinement

**Status:** exact history/topology theorems + one exact first refinement + two no-go results; the infinite `C4 -> C8 -> C16 -> ...` physical tower remains conditional on recursive carry locking in the physical history/projector.

This note attacks the next bottleneck after the modular-complex arithmetic bridge:

\[
\boxed{
\text{can the q=2 microscopic/history structure itself supply}
\quad
C_4\to\mu_8\to\mu_{16}\to\cdots
\quad\text{and}
\quad
\text{history}\to\mathbb Z\text{ winding?}
}
\]

The answer splits cleanly:

1. **history -> winding is exact** once the full ordered path is retained;
2. **the first phase refinement `C4 -> C8` has an exact history lift** because every selected q=2 Hamming edge already factorizes through a two-stage graph-change channel;
3. the **instantaneous five-state active+no-link Hilbert is too small** to be that `C8` and loses edge-channel information;
4. an independent binary clock also fails: `Z4 x Z2` is not `Z8`;
5. the infinite dyadic tower follows exactly **if** the same ordered edge-subdivision/carry rule is recursively selected by the physical history dynamics, but that all-level locking is still an open physical gate.

The point of this separation is to avoid hiding a new assumption inside the attractive formula

```text
C4 -> C8 -> C16 -> ... -> U(1).
```

---

## 1. Frozen q=2 phase skeleton

The four q=2 route labels in Gray order are

```text
00 -> 01 -> 11 -> 10 -> 00.
```

Each adjacent pair differs in one bit. Therefore the selected oriented phase skeleton is the same `C4` already used in the arithmetic bridge.

Let

\[
S_4|k\rangle=|k+1\pmod4\rangle.
\]

On the real Fourier plane this contains

\[
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
\qquad
J^2=-I,
\]

so the coarse phase spectrum contains the fourth roots of unity.

---

## 2. Existing microscopic fact: one q=2 edge is already two-stage

The previously committed graph-link gate proves, for the active q=2 basis states, that every matrix unit factors through the rank-one graph-absence state:

\[
\boxed{
|a\rangle\langle b|
=P_g U_a P_0 U_b P_g.
}
\]

Therefore each chosen oriented Hamming edge of the Gray `C4` has a two-stage graph-change history:

```text
active source
-> no-link transition event
-> active target.
```

This does **not** mean that the instantaneous no-link state itself remembers which edge is being traversed. It means the **history channel** does: the path contains a source label, a transition event, and a target label.

That distinction becomes crucial immediately.

---

## 3. Canonical history edge subdivision gives `C8`

For each coarse oriented edge

\[
k\to k+1,
\]

insert one transition-event position `m_k`:

\[
k\to m_k\to k+1.
\]

The history graph is then

```text
0 -> m0 -> 1 -> m1 -> 2 -> m2 -> 3 -> m3 -> 0,
```

which is exactly

\[
\boxed{C_8}.
\]

Equivalently represent a history position by `(k,s)` with

\[
k\in\mathbb Z_4,
\qquad
s\in\{0,1\},
\]

but **do not** use independent product dynamics. Use the carry update

\[
T(k,0)=(k,1),
\]

\[
T(k,1)=(k+1,0).
\]

Then

\[
\boxed{T^8=I}
\]

and no smaller positive power is the identity, so `T` has exact order eight.

Two refined ticks equal one coarse tick after projection:

\[
\boxed{
\pi\,T_8^2=S_4\,\pi.
}
\]

Thus the first history refinement is not merely a denser sampling of the same four phases. It has a genuine order-eight cyclic generator and therefore admits

\[
\mu_8.
\]

---

## 4. First no-go: the instantaneous five-state Hilbert is not `C8`

The graph-link carrier has

```text
4 active q=2 states + 1 no-link state = 5 states.
```

But the history subdivision requires

```text
4 active positions + 4 edge-event positions = 8 history positions.
```

All four event histories

```text
m0, m1, m2, m3
```

project onto the **same** instantaneous rank-one no-link state.

Therefore

\[
\boxed{
\text{instantaneous physical-state projection}
\quad
m_0,m_1,m_2,m_3\mapsto|0_{link}\rangle
}
\]

forgets the channel.

This is an exact obstruction:

\[
\boxed{
\text{the five-state instantaneous Hilbert alone cannot carry a bijective }C_8\text{ shift.}
}
\]

A transition/history label, or an equivalent dynamically retained channel degree of freedom, is required.

This fits the broader physicalization lesson already present in the repository:

> a constraint/state space and a physical history space are not the same object.

---

## 5. Second no-go: an independent time bit does not refine the phase

It is tempting to write

\[
\mathbb Z_4\times\mathbb Z_2
\]

and call the result `Z8`.

That is false.

For an element `(a,b)` of the product, its order divides

\[
\operatorname{lcm}(4,2)=4.
\]

Therefore the product contains **no element of order eight**:

\[
\boxed{
\mathbb Z_4\times\mathbb Z_2\not\cong\mathbb Z_8.
}
\]

So

```text
phase register + independent binary clock
```

cannot produce `mu8`.

What produces order eight is the **carry coupling**:

```text
(k,0) -> (k,1) -> (k+1,0).
```

The half-step and phase advance are not independent.

This is a useful microscopic falsifier: if the eventual physical history factorizes into independent phase and clock sectors with no carry relation, the proposed phase-refinement mechanism fails.

---

## 6. History gives integer winding exactly

Take any oriented cycle

\[
C_N=\mathbb Z/N\mathbb Z.
\]

Its universal cover is the integer line:

\[
\boxed{\mathbb Z\to C_N}.
\]

Suppose a full nearest-neighbor history is

\[
k_0,k_1,\ldots,k_T,
\qquad
k_{t+1}-k_t=\pm1\pmod N.
\]

Choose one initial lift

\[
n_0\in\mathbb Z,
\qquad
n_0\equiv k_0\pmod N.
\]

Then every next lifted point is forced uniquely:

\[
n_{t+1}=n_t\pm1
\]

with the sign fixed by the oriented edge actually traversed.

Therefore the complete history determines an ordinary integer path

\[
\boxed{n_t\in\mathbb Z}.
\]

If the residue history closes,

\[
k_T=k_0,
\]

then

\[
n_T-n_0=Nw
\]

for a unique

\[
\boxed{w\in\mathbb Z}.
\]

Hence

\[
\boxed{
w=\frac{n_T-n_0}{N}
}
\]

is the winding number.

Changing the initial sheet

\[
n_0\to n_0+qN
\]

shifts the entire lift by `qN` but leaves `w` unchanged.

So **history -> winding does not require an extra ad hoc counter**. The integer appears because the universal cover of a circle/cycle is an unbounded line.

This is precisely the structure needed by the previous arithmetic bridge:

\[
\boxed{
\text{compact residue}
+\text{complete history}
\to
\text{ordinary integer lift}.
}
\]

---

## 7. Winding survives phase refinement

A coarse `+1` edge of `C_N` becomes two `+1` refined edges of `C_{2N}`.
Likewise for `-1`.

For a closed coarse history with winding `w`,

\[
\sum_t\delta_t=Nw.
\]

After subdivision,

\[
\sum_t\delta_t^{fine}=2Nw.
\]

Since the refined cycle has length `2N`,

\[
\boxed{w_{fine}=w_{coarse}}.
\]

Thus the integer topological sector is stable under canonical edge subdivision.

This matters conceptually:

```text
phase resolution changes
winding sector does not.
```

The compact phase becomes finer while the universal-cover integer remains the same topological charge.

---

## 8. What recursive edge subdivision would imply

Suppose the same ordered two-stage history refinement is physically selected at every level.

After `g` refinements, one original `C4` edge contains

\[
2^g
\]

ordered history substeps, and the connected carry cycle has

\[
\boxed{N_g=4\cdot2^g}
\]

positions.

Hence

\[
\boxed{
C_4\to C_8\to C_{16}\to\cdots\to C_{4\cdot2^g}.
}
\]

The root groups obey

\[
\mu_4\subset\mu_8\subset\mu_{16}\subset\cdots
\]

because every old root is an even-index root at the next level:

\[
e^{2\pi ik/N_g}=e^{2\pi i(2k)/(2N_g)}.
\]

The angular mesh is

\[
\Delta\theta_g=\frac{2\pi}{N_g}
=\frac{\pi}{2^{g+1}},
\]

so the maximum distance to the nearest root is at most

\[
\boxed{
\frac{\pi}{N_g}\to0.
}
\]

Therefore the union is dense in the unit circle:

\[
\boxed{
\overline{\bigcup_{g\ge0}\mu_{4\cdot2^g}}=U(1).
}
\]

This mathematical implication is exact.

The physical premise is **not yet exact**.

---

## 9. Why recursive phase locking is not yet proved

The repository does prove a separate recursive causal fact for the frozen q=2 route family:

- every active causal edge is replaced by two-step routes;
- causal length doubles per generation.

Thus

\[
\boxed{L_g\propto2^g}
\]

is already exact in that family.

However two statements are different:

```text
causal history has dyadic resolution
```

and

```text
that dyadic resolution is the carry variable of the q=2 phase cycle.
```

The first is established.
The second requires a microscopic/history operator that locks the phase edge channel to the causal substep at every refinement level.

Without that operator, writing

\[
C_{4\cdot2^g}
\]

for all `g` would be an assumption, not a derivation.

Therefore the correct status is:

| statement | status |
|---|---|
| q=2 Gray `C4` | EXACT |
| each selected Hamming matrix unit factors through no-link | EXACT |
| history edge subdivision `C4 -> C8` | EXACT_HISTORY_LIFT |
| five-state instantaneous Hilbert itself is `C8` | NO-GO |
| independent `Z4 x Z2` clock gives `Z8` | NO-GO |
| complete cycle history -> integer winding | EXACT_TOPOLOGICAL |
| winding preserved by subdivision | EXACT |
| q=2 causal length doubles each generation | EXACT |
| all-level phase carry locking | OPEN_PHYSICAL |
| `C8 -> C16 -> ... -> U(1)` | CONDITIONAL on that locking |

---

## 10. A sharper candidate architecture

The arithmetic branch can now be refined to

\[
\boxed{
\begin{aligned}
q=2\text{ labels}
&\to C_4\text{ phase skeleton}\\
&\to\text{two-stage graph-change edge histories}\\
&\to C_8\text{ history lift}\\
&\to\text{universal-cover lift }\mathbb Z\\
&\to\text{winding }w\in\mathbb Z.
\end{aligned}
}
\]

Then, **if recursive physical carry locking is proved**,

\[
\boxed{
C_8\to C_{16}\to C_{32}\to\cdots\to U(1).
}
\]

This yields a very concrete interpretation of the previous integer arithmetic bridge:

> the ordinary integer need not be pasted onto a compact phase from outside; it can be the universal-cover coordinate of the complete phase history.

At refinement level `g`, the compact observable sees only

\[
n\pmod{N_g},
\]

while the complete history lift retains

\[
\boxed{n\in\mathbb Z}.
\]

---

## 11. New physical killer gate

The next computation is now sharply defined.

We need a real microscopic/history operator `U_hist` or projector measure such that, on the selected q=2 phase channel,

1. it distinguishes the four edge-history channels before they are projected to the common no-link state;
2. it implements the carry relation coherently;
3. under one refinement it intertwines
   \[
   \pi U_{g+1}^2=U_g\pi;
   \]
4. the same construction repeats without retuning for `g=0,1,2,...`;
5. history weights remain compatible with the existing Gauss/graph-changing dynamics and eventually the physical-projector construction.

Only after this passes may the project upgrade

```text
C4 -> C8 -> C16 -> ... -> U(1)
```

from `CONDITIONAL` to `DERIVED_PHYSICAL_HISTORY`.

---

## 12. Reproduction

The new executable gate is

```bash
python scripts/q2_history_phase_refinement_winding_gate.py \
  --graphlink-json verification_results/Q2_GRAPHLINK_PETER_WEYL.json \
  --dimension-json verification_results/Q2_DIMENSION3_FIXED_POINT.json \
  --max-generation 10 \
  --output verification_results/Q2_HISTORY_PHASE_REFINEMENT_WINDING.json
```

It checks:

- the Gray `C4` Hamming edges;
- the committed graph-link factorization certificate;
- the committed causal length-doubling certificate;
- exact `C4 -> C8` carry/history subdivision;
- the five-state/no-link information-loss no-go;
- the `Z4 x Z2 != Z8` no-go;
- exhaustive path-lift/winding identities;
- refinement-invariance of winding;
- the conditional recursive `C_(4*2^g)` algebra and density bound.

The executable deliberately reports

```text
phase_causal_locking = OPEN_PHYSICAL
```

even when all exact/conditional algebraic checks are green.
