# Mirror sigma range: symmetry-resolved finite gap and long-range falsifier

Status: **finite 16-cell mirror-odd spectral diagnostic + finite-block temporal susceptibility; continuum sigma mass remains open**.

The existence of two ordered mirror vacua does not imply a massless mediator. The staggered mirror order is `Z2`, not a continuous symmetry, so there is no automatic Goldstone mode.

A macroscopic mirror force therefore needs a sufficiently light **mirror-odd collective excitation**.

---

## 1. Why the raw third eigenvalue is not enough

Use the same 16-qubit `Q4` transverse-field Ising Hamiltonian as the microscopic mirror-order gate,

```text
H = -J sum_<vw> sigma_v sigma_w
    -h sum_v X_v.
```

The Hamiltonian commutes with global `Z2` flip. The order operator

```text
Sigma = (1/16) sum_v sigma_v
```

is `Z2` odd.

The finite ordered block has a nearly degenerate even/odd mirror doublet. Its tiny splitting is global tunnelling between the two vacua, not the propagating sigma mass.

A second subtlety is equally important: the raw state `E2` can be mirror even and therefore have zero matrix element with `Sigma`.

Thus the correct finite spectral diagnostic is not generically `E2-E0`.

Define instead

```text
Delta_sigma,odd
 = min(E_n-E0)
```

over states outside the tunnelling doublet satisfying

```text
|<0|Sigma|n>|^2 > 0.
```

This is the first additional mirror-odd state actually visible in the `Sigma` propagator.

---

## 2. Exact parity reduction

`scripts/mirror_sigma_range_gate.py` block-diagonalizes the full `2^16=65536` Hilbert space into exact global-parity sectors.

Each sector has dimension

```text
32768.
```

The even sector supplies the ground state. The lowest odd state is the tunnelling partner. Higher odd eigenstates are tested directly through their `Sigma` spectral weight.

This removes two false mass proxies at once:

```text
tiny E1-E0  -> tunnelling, not mediator mass
raw E2-E0   -> may have wrong Z2 parity.
```

---

## 3. Deep ordered result

At

```text
h/J = 0.2
```

the ground state remains strongly ordered,

```text
<Sigma^2> ~= 0.99765394737.
```

The mirror tunnelling gap is at machine scale, while its `Sigma` spectral weight carries almost the whole order parameter.

After excluding that tunnelling state, the first additional `Sigma`-coupled odd excitation has

```text
Delta_sigma,odd/J
 = 7.970087876964...
```

with nonzero spectral weight about

```text
1.5639e-4.
```

The computed low odd spectrum captures more than `99.9%` of the non-tunnelling `Sigma` weight at this point.

Thus the deep ordered 16-cell mirror mode is gapped at order `J`.

---

## 4. Crossover scan: the physical odd mode softens only modestly

The symmetry-resolved scan includes

```text
h/J = 0.2, 0.5, 1.0, 1.5,
      2.0, 2.1, 2.2, 2.25,
      2.4, 2.625, 2.75.
```

The softest checked `Sigma`-coupled odd excitation occurs near

```text
h/J = 2.2
```

with

```text
Delta_sigma,odd/J
 ~= 5.58410566853.
```

This corrects the earlier raw-eigenvalue diagnostic. For example, at `h/J=2.625` the raw `E2-E0` was about `3.39685 J`, but that state is not the first mirror-odd state coupled to `Sigma`. The actual `Sigma` spectral gap there is

```text
Delta_sigma,odd/J
 ~= 6.11072726933.
```

So the finite seed is **less** favorable to long-range propagation than the unprojected spectrum suggested.

---

## 5. Finite-block temporal response from the Lehmann expansion

After removing the global tunnelling partner, define the low-energy odd-sector susceptibility

```text
chi_*(i omega)
 = 2 sum_n
   Delta_n |<0|Sigma|n>|^2
   /(Delta_n^2 + omega^2).
```

At small frequency,

```text
chi_*(i omega)
 = A_* - B_* omega^2 + ...
```

and therefore

```text
chi_*^-1(i omega)
 ~= A_*^-1
  + (B_*/A_*^2) omega^2 + ...
```

The finite-block temporal coefficient is

```text
Z_t^(16) = B_*/A_*^2.
```

At `h/J=0.2`, the low odd spectrum is essentially single-mode after the tunnelling state is removed, giving approximately

```text
J Z_t^(16) ~= 401.15
omega_eff/J ~= 7.97009.
```

The equality of `omega_eff` with the odd spectral gap is expected in the single-mode-dominated limit.

This is real microscopic time-response information from the same 16-qubit Hamiltonian. It is **not yet the continuum kinetic coefficient**, because block volume, field normalization and refined dispersion still have to be matched.

---

## 6. Range formula

If the refined collective mode admits a relativistic low-energy dispersion with characteristic speed `c_sigma`, an energy gap `Delta_sigma` gives the Compton-like range

```text
lambda_sigma = hbar c_sigma / Delta_sigma.
```

Writing

```text
Delta_sigma = delta_sigma J
```

and defining

```text
j_sigma = J ell/(hbar c_sigma),
```

one gets

```text
lambda_sigma/ell
 = 1/(delta_sigma j_sigma).
```

For the deep ordered seed,

```text
delta_sigma ~= 7.97009,
```

and even the softest checked finite-Q4 mirror-odd mode has

```text
delta_sigma ~= 5.58411.
```

Therefore long range is not automatic.

---

## 7. What remains before calling this a physical m_sigma

The symmetry-resolved finite gap still cannot be identified directly with the physical continuum mass without deriving:

- the block-to-continuum normalization of `Sigma -> sigma(x)`;
- the temporal kinetic normalization in the refined theory;
- the physical length/time scale;
- the low-momentum dispersion on the refined PL complex;
- the scaling of the mirror-odd spectral gap under refinement.

The recursive PL gate already shows that staggered mirror order survives refinement. The next decisive computation is therefore a **refined mirror-odd propagator/susceptibility**, not another seed-level eigenvalue.

---

## 8. Long-range mirror-force killer condition

A physical repulsive branch requires all of

```text
beta_m != 0
m_sigma*r <= O(1)
alpha > exp(m_sigma*r)/(1+m_sigma*r)
stable positive-energy Hamiltonian
closed enlarged HDA.
```

The new parity-resolved range gate makes the second condition harder, not easier: the finite 16-cell order has no hidden light `Sigma` excitation once tunnelling and wrong-parity states are removed.

If the refined mirror-odd mode remains gapped at order microscopic `J`, macroscopic mirror repulsion is excluded even for nonzero matter charge.

---

## Reproduction

```bash
python scripts/mirror_sigma_range_gate.py \
  --output verification_results/MIRROR_SIGMA_RANGE.json
```
