# q=2 history winding, phase characters and orientation conjugation

**Status:** exact group/representation theorem once the complete history supplies integer winding; the physical character parameter and physical-projector weighting remain open.

The history-refinement calculation gives a stronger object than a finer phase label:

\[
\boxed{w\in\mathbb Z}
\]

for every closed oriented history, with

\[
w(\gamma_1\circ\gamma_2)=w(\gamma_1)+w(\gamma_2).
\]

This immediately raises a physical composition question:

> If a topological history sector carries a unit-norm phase weight and sequential histories compose multiplicatively, what functional form can that weight have?

The answer is exact.

---

## 1. Composition forces a character of the winding group

Let

\[
\Omega:\mathbb Z\to U(1)
\]

satisfy

\[
\Omega(0)=1
\]

and

\[
\boxed{
\Omega(w_1+w_2)=\Omega(w_1)\Omega(w_2).
}
\]

Set

\[
u=\Omega(1).
\]

Then for positive integer `w`, repeated composition gives

\[
\Omega(w)=u^w.
\]

For negative winding,

\[
\Omega(-w)=\Omega(w)^{-1}.
\]

Therefore

\[
\boxed{
\Omega(w)=u^w,
\qquad u\in U(1).
}
\]

So every unit-norm multiplicative winding weight is a one-dimensional unitary character of the additive group `Z`.

This is the elementary content behind the standard duality

\[
\boxed{\widehat{\mathbb Z}\cong U(1).}
\]

---

## 2. Real q=2 form: no primitive complex number is required

The q=2 phase carrier already supplies

\[
J^2=-I.
\]

Write the character generator as

\[
U=aI+bJ,
\]

with

\[
a^2+b^2=1.
\]

Then

\[
U\in SO(2)
\]

and

\[
\boxed{
\Omega_U(w)=U^w.
}
\]

The character law is just

\[
U^{w_1+w_2}=U^{w_1}U^{w_2}.
\]

Thus the history phase can be formulated entirely with real matrices:

```text
integer winding
-> powers of one real 2x2 rotation
-> phase character.
```

Complex notation

\[
e^{iw\theta}
\]

is the spectral shorthand for the same real rotation character.

---

## 3. Orientation reversal becomes complex conjugation again

Reverse a closed oriented history:

\[
w\mapsto-w.
\]

Then

\[
\Omega(-w)
=\Omega(w)^{-1}.
\]

For an orthogonal rotation,

\[
U^{-1}=U^T.
\]

Therefore

\[
\boxed{
\Omega(-w)=\Omega(w)^T.
}
\]

In complex notation this is

\[
\boxed{
\Omega(-w)=\overline{\Omega(w)}.
}
\]

This now aligns three exact orientation rules:

```text
q=2 label reflection:     J -> -J
geometry orientation:     Y_L -> -Y_L
history reversal:         w -> -w
phase weight:             Omega -> conjugate(Omega)
```

The repository still must derive whether one physical history operator dynamically locks all four sectors, but their covariance is now mutually consistent.

---

## 4. Finite C4 is the finite character seed

For the original q=2 phase cycle

\[
C_4\cong\mathbb Z_4,
\]

the four characters are

\[
\chi_m(k)=i^{mk},
\qquad m=0,1,2,3.
\]

They obey exact orthogonality

\[
\sum_{k=0}^{3}\chi_m(k)\overline{\chi_n(k)}
=4\delta_{mn}.
\]

So the same `mu4` that appeared as the q=2 phase spectrum is also the exact character group of the finite cycle.

The universal-cover lift replaces the finite residue group by

\[
\mathbb Z,
\]

and the corresponding character space becomes continuous after ordinary coefficient completion.

Schematically:

\[
\boxed{
\widehat{\mathbb Z_4}=\mu_4,
\qquad
\widehat{\mathbb Z}=U(1).
}
\]

This is a cleaner way to understand why unwrapping a compact history and retaining winding naturally introduces a continuous conjugate phase variable.

---

## 5. A special Gaussian arithmetic fact: `mu4` is the complete finite torsion seed

The arithmetic branch gives

\[
\mathbb Q[J]\cong\mathbb Q(i).
\]

Ask which exact roots of unity already live in this field.

Any root of unity is an algebraic integer. The algebraic integers of `Q(i)` are the Gaussian integers

\[
\mathbb Z[i].
\]

A Gaussian-integer unit has norm one:

\[
a^2+b^2=1,
\qquad a,b\in\mathbb Z.
\]

The only solutions are

\[
(\pm1,0),\qquad(0,\pm1).
\]

Hence the complete root-of-unity subgroup of `Q(i)` is

\[
\boxed{\mu_4=\{1,i,-1,-i\}.}
\]

This is a useful structural fact:

> once the q=2 quarter-turn `J` is fixed, `mu4` is exactly the full finite torsion already available over Gaussian rational arithmetic.

Exact `mu8` requires more structure, for example adjoining

\[
\sqrt2
\]

through Archimedean completion, or using the separate eight-dimensional reversible history spectrum.

So the appearance of `C4` is not in conflict with a continuous final `U(1)`: finite torsion can remain `mu4` while non-torsion rational/real characters become dense/continuous.

---

## 6. Rational winding characters are already dense

The direct rational-phase theorem supplies exact unit rotations

\[
U_{p,q}
=
\begin{pmatrix}
a&-b\\b&a\end{pmatrix},
\]

with

\[
a=\frac{q^2-p^2}{p^2+q^2},
\qquad
b=\frac{2pq}{p^2+q^2}.
\]

Each one defines an exact winding character

\[
\boxed{
\Omega_{p,q}(w)=U_{p,q}^{\,w}.
}
\]

Because the rational unit rotations are dense in the circle, these rational characters form a dense subset of all `SO(2)` winding characters.

Then Archimedean completion closes the parameter space to all

\[
U\in SO(2)\cong U(1).
\]

Thus the chain can be written without an infinite finite-order root tower:

\[
\boxed{
\text{history winding }\mathbb Z
\xrightarrow{\text{characters over }\mathbb Q[J]}
\text{dense phase group}
\xrightarrow{\text{Archimedean completion}}
U(1).
}
\]

---

## 7. What the theorem does and does not derive physically

The form

\[
\Omega(w)=U^w
\]

is forced if all of the following are true:

1. closed histories are classified by integer winding `w`;
2. the weight depends only on that topological sector;
3. sequential composition adds winding;
4. sequential amplitude composition multiplies the sector weights;
5. the sector factor is unit norm.

Under those assumptions the weight is necessarily a character.

But the theorem does **not** yet determine

\[
U
\]

or equivalently the angle/phase parameter.

That remaining number is analogous to a `theta` or action parameter:

\[
U=\exp(\theta J).
\]

The microscopic physical history/projector must derive it from the actual action/operator, not fit it after the fact.

The theorem also does not yet prove that the full gravitational history weight depends *only* on winding; local geometry and constraint data can contribute additional non-topological amplitudes.

So the new status is:

| statement | status |
|---|---|
| full q=2 phase history -> integer winding | EXACT |
| winding addition under concatenation | EXACT |
| unit multiplicative sector weight -> character `U^w` | EXACT |
| reversal -> inverse/conjugate character | EXACT |
| rational character generators dense after q2 `J` + `Q` | EXACT ARITHMETIC |
| Archimedean closure -> all `U(1)` characters | EXACT MATHEMATICS |
| physical projector weight depends only on winding | OPEN_PHYSICAL |
| physical generator `U` / angle derived from microscopic action | OPEN_PHYSICAL |

---

## 8. Reproduction

```bash
python scripts/q2_winding_phase_character_gate.py \
  --history-json verification_results/Q2_HISTORY_PHASE_REFINEMENT_WINDING.json \
  --output verification_results/Q2_WINDING_PHASE_CHARACTER.json
```

The gate checks the exact finite `C4` character table, exact rational `SO(2)` characters of integer winding, the composition law for positive and negative windings, orientation-reversal/conjugation, and the Gaussian `mu4` finite-torsion seed.
