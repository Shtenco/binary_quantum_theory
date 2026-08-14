# Longitudinal mirror charge in the conditional Goldstone branch

Status: **conditional nonlinear-sigma-model EFT control; does not establish that the pseudospin symmetry survives the full gravity dynamics**.

The exact Bell-gluing Hamiltonian has a bipartite Heisenberg parent. If that continuous pseudospin symmetry survives the full low-energy projected theory and the refined phase develops Neel order, one might be tempted to identify the resulting Goldstones with a massless mirror-force mediator.

That conclusion is too fast.

The physical mirror observable is the **orientation component** of the Neel vector. In a vacuum aligned with that component, it is longitudinal, while the Goldstones are transverse.

---

## 1. Expand around a mirror-oriented Neel vacuum

Let

```text
N_0 = v e_y
```

and parameterize the fixed-length order field as

```text
N = (pi_x,
     sqrt(v^2-pi_x^2-pi_z^2),
     pi_z).
```

The two fields `pi_x,pi_z` are the transverse Goldstone coordinates.

The physical mirror scalar is

```text
Sigma_Y = N_y.
```

Expanding,

```text
Sigma_Y
 = v
 - (pi_x^2+pi_z^2)/(2v)
 + O(pi^4).
```

There is no term linear in a Goldstone field.

Therefore

```text
<one Goldstone | Sigma_Y | vacuum> = 0
```

at this order.

So an exact Heisenberg/Goldstone limit does **not** automatically restore the previous one-particle `1/r` mirror potential.

---

## 2. Static longitudinal source

Let a static object carry longitudinal mirror charge `Q` through

```text
H_source = -Q Sigma_Y.
```

After dropping the constant vacuum energy,

```text
H_source
 = Q/(2v)
   (pi_x^2+pi_z^2)
 + O(pi^4).
```

Thus the leading massless interaction is a **two-Goldstone vertex**.

---

## 3. Leading free-Goldstone static potential in 3+1 dimensions

For canonically normalized massless Goldstones with Euclidean propagator

```text
D(tau,r)
 = 1/[4*pi^2*(tau^2+r^2)],
```

we need

```text
int d tau D(tau,r)^2.
```

The exact integral is

```text
int_{-infinity}^{infinity} d tau D^2
 = 1/(32*pi^3*r^3).
```

There are two Goldstone species. The connected Wick contraction gives the leading static interaction

```text
V_2G(r)
 = - Q1 Q2
   /(32*pi^3*v^2*r^3).
```

Therefore

```text
Q1 Q2 > 0 -> attraction
Q1 Q2 < 0 -> repulsion.
```

Opposite mirror charges still repel in this conditional EFT control.

But the radial law is different:

```text
V_2G ~ r^-3
F_2G ~ r^-4.
```

It falls much faster than Newtonian gravity.

`scripts/mirror_goldstone_source_gate.py` verifies the absence of the linear Goldstone vertex, the exact Euclidean integral numerically, the charge sign and the `r^-3` scaling.

---

## 4. Why this is a useful negative result

The Bell-gluing Heisenberg parent can provide a continuous low-energy sector without giving the physical longitudinal mirror scalar a one-particle massless pole.

Thus two logically different possibilities must remain separate.

### A. Light longitudinal mirror-odd particle

```text
<sigma particle|Sigma_Y|0> != 0
```

and

```text
V(r) ~ exp(-m_sigma r)/r.
```

This is the branch described by `MIRROR_MASTER_CRITERION.md`.

### B. Only transverse Goldstones are gapless

```text
<Goldstone|Sigma_Y|0> = 0
```

but the quadratic vertex survives, giving

```text
V_2G(r) ~ r^-3.
```

This can give opposite-charge repulsion but cannot imitate a Newtonian `1/r` potential over arbitrarily large distances.

---

## 5. What could restore one-Goldstone exchange

A one-Goldstone pole can appear only if the microscopic matter source couples **linearly to a transverse order component** or if the full projected dynamics mixes the physical mirror orientation with a transverse mode.

Schematically,

```text
H_source
 ~ -Q_a N_a
```

with a source vector containing a component perpendicular to the selected vacuum can have a linear Goldstone vertex.

But that is a different matter coupling from a purely longitudinal scalar mirror charge and must be derived, not assumed.

---

## 6. Experimental fingerprint

The two branches predict qualitatively different distance dependence:

```text
one-particle light mirror mode:
  V ~ 1/r       (massless limit)
  F ~ 1/r^2

longitudinal two-Goldstone channel:
  V ~ 1/r^3
  F ~ 1/r^4.
```

So a future physical-scale theory would have a direct radial-law discriminator rather than merely a sign prediction.

---

## Reproduction

```bash
python scripts/mirror_goldstone_source_gate.py \
  --output verification_results/MIRROR_GOLDSTONE_SOURCE.json
```
