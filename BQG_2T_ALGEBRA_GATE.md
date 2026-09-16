# BQG → 2T Algebra Gate

**Status: OPEN / falsification program.**

This document defines a strict test for whether the Binary Quantum Gravity (BQG) construction can contain a genuine two-time / 2T sector in the sense of Bars-style gauge-reduced two-time physics.

This is **not** a claim that BQG is already a 2T theory.

## 1. The central question

Can the BQG microscopic binary/history structure admit a parent constrained system with two time-like directions such that ordinary 3+1 physics appears after gauge reduction?

The target schematic chain is

```text
binary microstructure
      ↓
quantum geometry + relational history
      ↓
parent constrained phase space
      ↓
possible 2T sector
      ↓
constraint/gauge reduction
      ↓
ordinary 3+1 dynamics
      ↓
ADM/HDA → GR + physical spin-2 sector
```

The important distinction is between:

1. **two coordinates** — a literal signature `(d,2)`;
2. **two canonical history directions** — two evolution-like parameters;
3. **two-time gauge symmetry** — an enlarged constrained phase space whose redundant variables are removed by gauge constraints;
4. **a relational clock label** — the existing BQG history parameter;
5. **a genuine Bars 2T system** — a phase-space system with an `Sp(2,R)`-type constraint algebra.

Only item 5 would justify calling the construction a 2T theory in the standard Bars sense.

## 2. External 2T reference structure

In Bars' 2T framework, the parent theory has an `SO(d,2)` structure and an `Sp(2,R)` gauge symmetry in phase space. Different gauge choices can produce different one-time systems. See Bars, *Two-Time Physics* (1998), and subsequent work on 2T field theory.

A canonical particle-level fingerprint is the three-generator constraint set

```text
Q11 ~ X·X
Q12 ~ X·P
Q22 ~ P·P
```

whose Poisson/commutator algebra closes into `sp(2,R)` up to convention-dependent normalizations.

BQG must reproduce an equivalent algebraic structure rather than merely contain a variable called `clock` or a quantity with history dimension near four.

## 3. BQG starting point

The current BQG architecture already contains a relational-history construction and an explicit distinction between spatial scaling and history scaling.

The present controlled projector construction uses

```text
G = S_clock ⊗ R_geom
P_rel = (1/8) Σ_{τ=0}^{7} G^τ
```

with conditional evolution of the form

```text
|ψ(t)⟩ = R^t |ψ0⟩.
```

This is a useful relational-control structure, but it is **not yet** a 2T gauge symmetry.

In particular, the current positive-control choice `R=J` is not yet the physical graph-changing update. The physical projector, rigging map, partition function, effective action and interacting TT kernel remain open.

## 4. First hard gate: identify the actual BQG constraints

Do not introduce artificial `Q11,Q12,Q22` variables.

From the actual BQG microscopic/operator construction identify candidate constraints

```text
C_A
```

and classify them as:

- Gauss constraints;
- spatial diffeomorphism constraints;
- Hamiltonian constraint;
- graph-changing constraints;
- clock/history constraints;
- auxiliary/redundancy constraints.

For each candidate record whether it is exact, finite-cutoff, emergent, conditional, or only proposed.

## 5. Algebraic gate

Search for three independent combinations

```text
C1, C2, C3
```

such that their Poisson/commutator algebra closes:

```text
[C1,C2] =  a C1 + b C2 + c C3
[C1,C3] =  d C1 + e C2 + f C3
[C2,C3] =  g C1 + h C2 + i C3
```

with coefficients that are either constants or a controlled representation of the relevant structure functions.

The Bars target is, schematically,

```text
{Q11,Q22} ~ Q12
{Q12,Q11} ~ Q11
{Q12,Q22} ~ -Q22
```

after normalization conventions are fixed.

### Pass condition

A BQG `sp(2,R)` candidate passes only if:

1. the generators are independent;
2. the algebra closes without adding an unlimited tower of new generators;
3. Jacobi identities hold;
4. the constraint surface is preserved by the generated gauge flow;
5. the physical observables commute with the first-class generators modulo constraints.

A numerical resemblance of three matrices is not sufficient.

## 6. Canonical-variable gate

If an `sp(2,R)` subalgebra is found, construct an explicit local canonical dictionary

```text
(τ1, τ2, p1, p2)
```

or the corresponding field/graph variables.

Then verify that the candidate constraints can be written in a Bars-like form, possibly after a canonical transformation,

```text
Q11 = X^2 + corrections
Q12 = X·P + corrections
Q22 = P^2 + corrections.
```

The corrections must be classified rather than silently absorbed into notation.

## 7. Signature gate

A second canonical clock sector is not automatically a second timelike metric direction.

To establish a genuine `(d,2)` parent geometry one must derive a nondegenerate kinetic quadratic form with two negative directions before gauge reduction.

The signature must be shown from the action/Hessian/operator, not inferred from the number of labels.

If the extra history variable has no independent conjugate momentum or no second negative kinetic direction, the correct terminology remains **relational history sector**, not literal second time.

## 8. Gauge-reduction gate

The decisive test is whether one time direction can be removed by gauge fixing while preserving a nontrivial physical Hamiltonian.

Require

```text
parent variables
      ↓ gauge fixing
one physical time
      ↓
H_phys
```

with no negative-norm physical state surviving.

The reduced theory must reproduce the already required BQG continuum constraints rather than a new unrelated model.

## 9. Quantum gate

At the quantum level require a physical-state condition

```text
Ĉ_i |Ψ_phys⟩ = 0
```

or the appropriate rigging-map construction.

The physical inner product must be positive on the reduced Hilbert space.

The relational propagator must then admit a controlled one-time limit,

```text
R_BQG(Δτ)
 = I - i Δt H_phys / ħ + O(Δt²),
```

on the physical sector.

A finite cyclic projector by itself does not establish this result.

## 10. Gravity gate

After reduction, the constraint algebra must connect to the BQG ADM/HDA target:

```text
{H[N],H[M]}
   → D[q^{ab}(N∂_bM - M∂_bN)]
```

in the continuum habitat.

The resulting reduced theory must also satisfy the existing BQG requirements:

```text
b/a → -1
Δ_shape → 0
Δ_HDA → 0
m_unwanted / m_phys → ∞
z → 1
```

and ultimately yield a physical TT kernel with the frozen six-observable Wilson dictionary.

## 11. Black-hole gate

A successful parent 2T embedding should permit a controlled reduction to a known 3+1 gravitational solution.

The first target should be Schwarzschild, not Kerr.

Check:

1. the reduced metric solves the BQG/GR limit;
2. the horizon is a gauge-invariant observable or its gauge dependence is explicitly understood;
3. no second-time ghost survives;
4. the parent-to-shadow map remains regular on the exterior region.

Kerr and rotating sectors come only after the static test.

## 12. Falsification conditions

The hypothesis `BQG ⊃ 2T` must be rejected if any of the following occurs:

- no three-generator first-class subalgebra exists;
- the apparent algebra closes only after inserting fitted functions;
- the candidate second clock has no independent conjugate momentum;
- the parent kinetic form does not contain two timelike directions;
- gauge reduction leaves ghosts or negative-norm states;
- the reduced Hamiltonian fails to reproduce the BQG relational dynamics;
- the reduced constraint algebra fails the HDA target;
- the construction works only by changing the frozen microscopic rules after observing the result.

A clean no-go is a valid scientific result.

## 13. Minimal computational experiment

The first implementation should be deliberately small.

```text
Input:
  finite q=2 BQG graph
  finite history register
  existing SU(2) link/node operators

Step A:
  enumerate the independent microscopic constraints

Step B:
  build their finite matrices

Step C:
  search three-dimensional candidate subspaces

Step D:
  compute commutator closure residuals

Step E:
  solve for the best exact symbolic normalization

Step F:
  test Jacobi and first-class preservation

Step G:
  attempt canonical reconstruction of X,P

Step H:
  perform gauge reduction

Step I:
  compare the reduced evolution with P_rel
```

The search should be exact/rational or high-precision symbolic wherever possible. Floating-point proximity alone must never be declared an algebraic closure.

## 14. Interpretation matrix

| Outcome | Correct interpretation |
|---|---|
| Exact `sp(2,R)` + two-time signature + ghost-free reduction | strong evidence for a genuine BQG 2T embedding |
| `sp(2,R)` algebra but no second timelike kinetic direction | hidden phase-space duality / 2T-like algebra, not literal two-time spacetime |
| Relational history without independent canonical clock pair | one-time relational BQG, not 2T |
| Approximate algebra only at continuum limit | emergent/deformed 2T candidate; requires scaling proof |
| No closed three-generator algebra | BQG is not Bars-type 2T under the tested construction |

## 15. Current conclusion

The scientifically useful statement is therefore:

> **BQG currently has a relational-history sector that is structurally compatible with testing a 2T embedding, but it has not yet demonstrated an `Sp(2,R)` gauge algebra, a `(d,2)` parent metric, or a ghost-free 2T→1T reduction.**

The next decisive calculation is not another dimension fit. It is the **constraint-algebra gate**.

---

## References

- I. Bars, *Two-Time Physics*, arXiv:hep-th/9809034.
- I. Bars, *Hidden Symmetries, AdS_D × S^n, and the lifting of one-time-physics to two-time-physics*, arXiv:hep-th/9810025.
- I. Bars, *Constraints on Interacting Scalars in 2T Field Theory and No Scale Models in 1T Field Theory*, arXiv:1008.1540.

