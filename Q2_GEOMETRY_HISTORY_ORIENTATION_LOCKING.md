# q=2 geometry orientation ↔ history current: the first symmetry-allowed locking channel

**Status:** exact symmetry/representation theorem; the microscopic gravitational coefficient remains uncomputed and may be zero.

Two exact sign structures have now been derived from the same q=2 carrier:

1. geometry orientation is carried by the logical pseudoscalar
   \[
   Q=\frac{\sqrt3}{4}Y_L,
   \qquad Y_L\mapsto-Y_L
   \]
   under orientation reversal;
2. the minimal reversible history dilation has an oriented `C8` shift `U` with
   \[
   R_h U R_h^{-1}=U^{-1}.
   \]

The next question is whether there is a natural operator that can dynamically **lock the sign of geometry orientation to the direction of history phase motion** without explicitly breaking the overall reflection symmetry.

There is exactly such a channel.

---

## 1. The orientation-even history kernel cannot choose a direction

The ordinary nearest-neighbor cyclic kernel is

\[
H_{even}=U+U^\dagger.
\]

For the history character `m`,

\[
U|m\rangle=e^{2\pi i m/8}|m\rangle,
\]

so

\[
H_{even}|m\rangle
=2\cos\left(\frac{2\pi m}{8}\right)|m\rangle.
\]

But

\[
\cos\left(\frac{2\pi(8-m)}8\right)
=\cos\left(\frac{2\pi m}8\right).
\]

Therefore

\[
\boxed{E_m=E_{8-m}.}
\]

The conjugate clockwise/counterclockwise character sectors are exactly degenerate.

This includes the q=2 Hamming/adjacency philosophy: an orientation-even real adjacency can see the cosine of phase, but it cannot select its sign.

So

\[
\boxed{
\text{orientation-even Hamming dynamics alone cannot lock a preferred phase direction.}
}
\]

---

## 2. The history current is the reflection-odd partner

Define

\[
\boxed{
C_h=\frac{U-U^\dagger}{2i}.
}
\]

This operator is Hermitian:

\[
C_h^\dagger=C_h.
\]

Under history reflection,

\[
U\leftrightarrow U^{-1},
\]

so

\[
\boxed{R_h C_h R_h^{-1}=-C_h.}
\]

Its character eigenvalues are

\[
\boxed{
c_m=\sin\left(\frac{2\pi m}{8}\right).}
\]

Hence

\[
\boxed{c_{8-m}=-c_m.}
\]

Unlike `U+U^-1`, the current distinguishes the two orientations.

Within the nearest-neighbor span of `U` and `U^-1`, Hermiticity plus reflection oddness leaves this channel unique up to one real overall coefficient.

---

## 3. Geometry has exactly the same sign behavior

The established geometry-qubit pseudoscalar satisfies

\[
\boxed{Y_L\mapsto-Y_L.}
\]

Thus we have two odd objects:

```text
geometry orientation:  Y_L       -> -Y_L
history direction:      C_h       -> -C_h
```

Their product is even.

Define

\[
\boxed{
H_{lock}=g\,Y_L\otimes C_h.
}
\]

Because both factors are Hermitian,

\[
H_{lock}^\dagger=H_{lock}.
\]

Under the combined orientation reversal,

\[
(Y_L,C_h)\mapsto(-Y_L,-C_h),
\]

so

\[
\boxed{H_{lock}\mapsto H_{lock}.}
\]

Therefore this term can correlate the two orientations **without explicitly breaking the total reflection symmetry**.

---

## 4. What the locking term does to the spectrum

Let

\[
Y_L|y\rangle=y|y\rangle,
\qquad y=\pm1.
\]

For a history character `m`,

\[
C_h|m\rangle=c_m|m\rangle.
\]

Then

\[
H_{lock}|y,m\rangle
=g\,y\,c_m|y,m\rangle.
\]

Thus

\[
\boxed{E_{lock}(y,m)=g\,y\sin(2\pi m/8).}
\]

At fixed geometry orientation `y`, conjugate history sectors split:

\[
E(y,8-m)=-E(y,m)
\]

whenever the sine is nonzero.

But the **combined-reflection partner** remains degenerate:

\[
\boxed{
E(y,m)=E(-y,8-m).
}
\]

So a nonzero `g` can dynamically favor a correlation

```text
one geometry orientation <-> one history direction
opposite geometry orientation <-> opposite history direction
```

while preserving the symmetry that reverses both together.

This is exactly the type of locking needed to turn the earlier common sign covariance

```text
J -> -J
Y_L -> -Y_L
```

into a possible dynamical relation rather than a mere representation coincidence.

---

## 5. A second no-go: pure gauge averaging kills the locking channel

The projector audit proved that ordinary group averaging over the complete history shift gives

\[
P_0=\frac18\sum_{t=0}^{7}U^t,
\]

the trivial character projector.

But the history current vanishes in that sector:

\[
\boxed{P_0C_hP_0=0.}
\]

Therefore

\[
\boxed{
(I\otimes P_0)H_{lock}(I\otimes P_0)=0.
}
\]

So even though `Y_L C_h` is symmetry-allowed, it **cannot survive ordinary untwisted averaging if the entire history shift U is declared pure gauge**.

This sharply narrows the physical possibilities.

A nonzero surviving lock requires the history direction to appear as one of:

- relational/boundary data;
- a nontrivial character/superselection sector;
- a distributional rigging-map spectral variable;
- another physical history degree of freedom not completely quotiented away.

---

## 6. What must now be computed microscopically

Symmetry has reduced the question to one concrete coefficient.

The next genuine physical calculation is to take the **actual graph-changing gravitational constraint/history amplitude** and project it onto

\[
\boxed{Y_L\otimes C_h.}
\]

Call the coefficient

\[
g_{Y\!C}.
\]

Then there are three logically clean outcomes:

### A. `g_YC != 0`

The microscopic operator dynamically couples geometry orientation to history direction. This would close a major part of the phase/geometry locking bridge, subject still to the physical-projector interpretation.

### B. `g_YC = 0` by a deeper symmetry

Then the beautiful common sign covariance does **not** become a physical locking force in the current model. The theory must accept the no-go rather than manufacture a coefficient.

### C. the coefficient is basis/regularization dependent

Then it is not yet a physical prediction and must be tested under the same regulator/refinement universality discipline as the gravity sector.

No numerical `g_YC` is claimed in this note.

---

## 7. Relation to the existing Peter-Weyl parity theorem

The repository already proves a separate doubled-spin parity grading:

```text
H_E   odd
V     even
K     odd
H_L   even
```

This grading is **not the same symmetry** as the q=2 orientation reflection discussed here.

They must not be conflated.

The new task is therefore not to infer `g_YC` from the old parity signs, but to evaluate the actual orientation-sensitive matrix elements of the microscopic history/constraint operator.

This distinction prevents another false shortcut.

---

## 8. Updated status

| result | status |
|---|---|
| `H_even=U+U^-1` conjugate degeneracy | EXACT |
| history current `C_h=(U-U†)/(2i)` Hermitian | EXACT |
| `C_h` reflection odd | EXACT |
| `Y_L` geometry reflection odd | EXACT from existing geometry bridge |
| `Y_L C_h` combined-reflection even | EXACT |
| locking term splits conjugates at fixed `Y_L` | EXACT |
| simultaneous `(Y,m)->(-Y,8-m)` degeneracy | EXACT |
| ordinary group average kills `C_h` | EXACT / NO-GO |
| ordinary group average kills `Y_L C_h` | EXACT / NO-GO |
| microscopic gravitational coefficient `g_YC` | OPEN_PHYSICAL |
| nonzero physical orientation-history locking | NOT YET CLAIMED |

---

## 9. Reproduction

```bash
python scripts/q2_geometry_history_orientation_lock_gate.py \
  --output verification_results/Q2_GEOMETRY_HISTORY_ORIENTATION_LOCK.json
```

The gate performs the full finite `C8` character algebra symbolically and checks the combined reflection symmetry and group-average no-go exactly.
