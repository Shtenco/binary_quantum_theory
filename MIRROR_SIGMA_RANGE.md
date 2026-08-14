# Mirror sigma range: finite gap and long-range falsifier

Status: **finite 16-cell spectral range diagnostic; continuum sigma mass and temporal normalization remain open**.

The existence of two ordered mirror vacua does not imply a massless mediator. The staggered mirror order is `Z2`, not a continuous symmetry, so there is no automatic Goldstone mode.

A macroscopic mirror force therefore needs a sufficiently light collective excitation.

---

## 1. The relevant finite gap

Use the same 16-qubit `Q4` transverse-field Ising Hamiltonian as the microscopic mirror-order gate,

```text
H = -J sum_<vw> sigma_v sigma_w
    -h sum_v X_v.
```

The lowest two states form the finite mirror doublet. To avoid identifying the exponentially small finite-size tunnelling splitting with the mediator mass, define the two-level-excluded gap

```text
Delta_sigma^(16)(h) = E2-E0.
```

At `h=0`, one local orientation error has the exact classical cost

```text
Delta_local = 8J.
```

At the strongly ordered control point `h/J=0.2`, the sparse finite calculation gives

```text
Delta_sigma^(16)/J = 7.9700878769645...
Sigma^2             > 0.99.
```

Thus the ordered seed is gapped at order `J`; the robust mirror order itself is not a long-range mediator.

---

## 2. Finite crossover softens the mode but does not close it

`scripts/mirror_sigma_range_gate.py` scans

```text
h/J = 0.2, 0.5, 1.0, 1.5,
      2.0, 2.25, 2.5, 2.625,
      2.75, 3.0, 3.5, 4.0.
```

The softest scanned finite-Q4 point is near

```text
h/J = 2.625
```

with approximately

```text
E0/J = -46.5558916475
E1/J = -46.1944809892
E2/J = -43.1590390553
```

so

```text
E2-E0 = 3.39685259213 J
```

while

```text
Sigma^2 ~= 0.45837.
```

The finite crossover therefore softens the excitation substantially, but the checked 16-cell block does not exhibit a vanishing non-tunnelling gap.

This is exactly the behaviour that must be resolved in the refined/continuum theory rather than hidden by the nearly degenerate mirror doublet.

---

## 3. Range formula

If a refined collective mode admits a relativistic low-energy dispersion with characteristic speed `c_sigma`, then an energy gap `Delta_sigma` corresponds to the Compton-like range

```text
lambda_sigma = hbar c_sigma / Delta_sigma.
```

If

```text
Delta_sigma = delta J,
```

then relative to a microscopic length `ell`,

```text
lambda_sigma/ell
 = 1/(delta*j_sigma),
```

where

```text
j_sigma = J ell/(hbar c_sigma).
```

For the deep ordered 16-cell point,

```text
delta ~= 7.97009.
```

Therefore a force acting at a macroscopic separation `r` requires, after the full physical normalization,

```text
m_sigma r <= O(1)
```

or equivalently

```text
Delta_sigma <= O(hbar c_sigma/r).
```

---

## 4. What the finite seed does NOT establish

The quantity `E2-E0` is a finite spectral diagnostic. It cannot yet be called the physical continuum `m_sigma` without deriving:

- which refined eigenmode becomes the continuum scalar/pseudoscalar field;
- the temporal kinetic normalization;
- the physical lattice length/time relation;
- the refined low-momentum dispersion;
- the thermodynamic/continuum scaling of the gap.

The recursive PL gate already shows that the staggered order survives refinement and that the first combinatorial dual-Laplacian eigenvalue decreases strongly with refinement. That is compatible with growing long-wavelength structure, but it is not by itself a proof of a massless or parametrically light sigma particle.

---

## 5. Long-range mirror-force killer condition

A physical repulsive branch requires all of

```text
beta_m != 0
m_sigma*r <= O(1)
alpha > exp(m_sigma*r)/(1+m_sigma*r)
stable positive-energy Hamiltonian
closed enlarged HDA.
```

The new range gate makes the second condition independent and explicit.

If the refined mirror mode remains gapped at order the microscopic `J`, and the resulting physical range is microscopic, then macroscopic mirror repulsion is excluded even when the matter matrix element `beta_m` is nonzero.

---

## Reproduction

```bash
python scripts/mirror_sigma_range_gate.py \
  --output verification_results/MIRROR_SIGMA_RANGE.json
```
