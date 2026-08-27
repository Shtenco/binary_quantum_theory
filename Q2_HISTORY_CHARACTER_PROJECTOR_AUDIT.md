# q=2 history character projectors: what group averaging preserves and what it destroys

**Status:** exact finite character-projector theorem + exact no-go for naive untwisted group averaging; universal-cover continuous characters require generalized/spectral history machinery. No physical time is inferred from a constraint spectrum.

The q=2 history branch has now established three separate facts:

1. complete oriented histories lift to integer winding `w in Z`;
2. the minimal reversible first history dilation is an eight-state `C8`;
3. additive winding supports unitary characters `Omega(w)=u^w`.

That is still **not** enough to say that a gravitational physical projector preserves those phases.

This note asks the next question:

> If the cyclic/history motion is averaged as a gauge orbit, what happens to the phase characters?

The answer gives an important no-go.

---

## 1. Exact C8 character projectors

Let `U` be the exact order-eight history permutation,

\[
U^8=I.
\]

Let

\[
\zeta=e^{2\pi i/8}.
\]

For `m=0,...,7` define

\[
\boxed{
P_m=\frac18\sum_{t=0}^{7}\zeta^{-mt}U^t.
}
\]

Standard finite Fourier algebra gives exactly

\[
\boxed{P_m^2=P_m,}
\]

\[
\boxed{P_mP_n=0\quad(m\ne n),}
\]

\[
\boxed{\sum_{m=0}^{7}P_m=I,}
\]

and

\[
\boxed{UP_m=\zeta^mP_m.}
\]

On the regular `C8` history carrier every `P_m` has rank one.

Therefore the eight history characters give a complete exact spectral decomposition of the minimal reversible history update.

This is finite representation theory, not yet a physical constraint projection.

---

## 2. The ordinary group average selects only the trivial character

The usual untwisted finite group average is

\[
\boxed{
P_{avg}=\frac18\sum_{t=0}^{7}U^t.
}
\]

But this is exactly

\[
\boxed{P_{avg}=P_0.}
\]

Hence, for every nontrivial character,

\[
\boxed{P_{avg}P_m=0\qquad m=1,\ldots,7.}
\]

This is the first major physical lesson.

If the entire q=2 history shift `U` is declared to be a **pure gauge redundancy**, and physical states are obtained by ordinary group averaging over that orbit, then all nontrivial phase sectors disappear.

So one cannot simultaneously say

```text
U is pure gauge
```

and

```text
its nontrivial character phase is a surviving physical observable
```

under ordinary untwisted averaging.

This is an exact no-go, not an interpretation preference.

---

## 3. Character-twisted averages do preserve a selected sector

One can instead use

\[
\boxed{
P_m=\frac18\sum_t\zeta^{-mt}U^t.
}
\]

This keeps exactly the `m`-th character sector.

But the label `m` did not come from ordinary group averaging. It was supplied to the projector.

Therefore a twisted projector is legitimate only when there is independent physics telling us what the character label means, for example:

- a boundary charge;
- a topological superselection sector;
- a relational clock/boundary condition;
- a history action supplying the character;
- another constraint/boundary observable whose eigenvalue fixes the sector.

Without such a derivation, choosing `m` is merely choosing the answer.

So the correct statement is

\[
\boxed{
\text{twisted projectors exist exactly}
\not\Rightarrow
\text{the physical theory selects one of them}.
}
\]

---

## 4. Real form: conjugate characters make real two-dimensional planes

The complex sectors `m` and `8-m` are conjugates.

Their sum

\[
Q_m=P_m+P_{8-m}
\]

is a real projector.

For

\[
m=1,2,3,
\]

the corresponding real subspace has dimension two.

Thus the real history carrier decomposes into

```text
m=0      one real line
m=4      one real line
m=1/7    one real rotation plane
m=2/6    one real rotation plane
m=3/5    one real rotation plane
```

with dimensions

\[
1+1+2+2+2=8.
\]

Again, primitive complex arithmetic is unnecessary: the complex conjugate character pairs are ordinary real invariant rotation planes.

---

## 5. The universal-cover Z changes the mathematical category

The exact winding theorem lifts complete histories from the compact cycle to

\[
\mathbb Z.
\]

Let `T` be the bilateral shift on the history cover:

\[
T|n\rangle=|n+1\rangle.
\]

A character with phase `u`, `|u|=1`, formally satisfies

\[
T\psi=u\psi.
\]

The recurrence implies that all components have the same modulus.

Therefore a nonzero exact unit-circle character has

\[
|\psi_n|=\text{constant}.
\]

Its squared norm would be

\[
\sum_{n\in\mathbb Z}|\psi_n|^2=\infty.
\]

Hence

\[
\boxed{
\text{the bilateral shift has no nonzero normalizable }\ell^2(\mathbb Z)
\text{ eigenvector with }|u|=1.
}
\]

This is crucial.

The continuous characters

\[
e^{in\theta}
\]

are **generalized spectral states**, analogous to momentum plane waves, not ordinary normalizable vectors on the integer cover.

Therefore the formal continuous twisted average

\[
\sum_{w\in\mathbb Z}e^{-iw\theta}T^w
\]

is distributional.

It cannot simply be inserted as a bounded rank-one Hilbert-space projector.

---

## 6. Abel regularization exposes the distributional limit cleanly

Introduce

\[
0<r<1
\]

and damp the winding sum:

\[
K_r(\phi)
=
\sum_{w\in\mathbb Z}r^{|w|}e^{iw\phi}.
\]

The geometric series gives exactly

\[
\boxed{
K_r(\phi)
=\frac{1-r^2}{1-2r\cos\phi+r^2}.
}
\]

This is the Poisson kernel.

For fixed

\[
\phi\not\equiv0\pmod{2\pi},
\]

we have

\[
K_r(\phi)\to0
\qquad(r\to1^-),
\]

while the total circle mass stays fixed.

Thus the limit is delta-like/distributional on the character circle.

This is exactly the behavior expected from a rigging-map or generalized spectral projector rather than an ordinary normalizable state.

---

## 7. New no-go for the physical interpretation

We can now state a sharper falsifier:

\[
\boxed{
\text{If q=2 phase/history motion is fully averaged as gauge,}
\text{ its nontrivial phase characters are removed.}
}
\]

Therefore a surviving physical complex phase requires at least one of the following:

### Route A — relational/boundary symmetry

The phase/history shift is not pure gauge; it describes a relational or boundary degree of freedom that survives reduction.

### Route B — superselection/boundary sector

A physical boundary/topological datum fixes a character sector before or during group averaging.

### Route C — rigging-map/history amplitude

The true generally covariant physical inner product is built as a distributional history/constraint amplitude whose spectral measure contains the character parameter.

In all cases the character must be **derived** from physical structure.

One may not simply pick a twisted character because it gives the desired complex phase.

---

## 8. Relation to the Hamiltonian-constraint warning

This result reinforces an earlier conceptual boundary of the project.

A canonical Hamiltonian constraint is not automatically a physical time Hamiltonian.

Likewise:

```text
spectral decomposition of a history permutation
```

is not automatically

```text
physical frequency spectrum.
```

The correct route still requires a physical projector/history amplitude or a derived relational/boundary clock.

The new character algebra tells us what such a construction **could act on** and what ordinary group averaging would do, but it does not supply the missing physical measure by itself.

---

## 9. Updated status

| statement | status |
|---|---|
| finite C8 character projectors `P_m` | EXACT |
| projector orthogonality/completeness | EXACT |
| ordinary group averaging = `P_0` | EXACT |
| ordinary averaging kills nontrivial characters | NEGATIVE / NO-GO |
| finite twisted `P_m` | EXACT MATHEMATICS |
| physical selection of `m` | OPEN_PHYSICAL |
| real conjugate character planes | EXACT |
| Z-cover unit characters normalizable in `l2(Z)` | NEGATIVE |
| continuous character states as generalized spectrum | EXACT FUNCTIONAL-ANALYTIC STATEMENT |
| Abel regularization -> Poisson kernel | EXACT |
| gravitational rigging map / physical inner product | OPEN_PHYSICAL |
| constraint spectrum = physical frequency | NOT CLAIMED |

---

## 10. Next physical computation

The next useful gate is now narrower than before.

We should not try to invent another phase refinement.

We should take a **small actual q=2 graph-changing constraint/history kernel** already present in the repository and ask:

1. does it commute with or resolve the new history-character operator?
2. does its group-averaged / boundary amplitude collapse to the trivial sector?
3. do orientation-dependent matrix elements generate a nontrivial character weight before averaging?
4. if a nontrivial character appears, is its parameter fixed by the microscopic operator coefficients rather than inserted by hand?
5. can that construction be written as a legitimate rigging-map/boundary amplitude without renaming a constraint eigenvalue `omega`?

That is the real physical test for the new arithmetic/history line.

---

## 11. Reproduction

```bash
python scripts/q2_history_character_projector_audit_gate.py \
  --output verification_results/Q2_HISTORY_CHARACTER_PROJECTOR_AUDIT.json
```

The gate uses exact symbolic algebra for the C8 projectors and the Abel/Poisson identity, plus exact finite-window controls for the non-normalizability of universal-cover character states.
