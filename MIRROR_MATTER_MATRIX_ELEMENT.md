# Mirror matter matrix element: static-source gate

Status: **exact free-Dirac source-selection result + finite positive-mass mirror-doublet construction; numerical microscopic coupling still open**.

The mirror branch had reached

```text
Y_L/Q -> Sigma -> sigma(x) -> Z_sigma -> beta_m -> alpha -> F_mirror.
```

This note attacks the remaining matter coefficient `beta_m` rather than assigning it by hand.

---

## 1. The old axial bridge is not a universal static mass source

The mirror/chirality construction naturally allows the parity-even product

```text
sigma * J5^0,
```

because both `sigma` and the axial density are parity odd.

That remains a legitimate chirality/spin-sensitive coupling. But for a free on-shell massive Dirac state the exact bilinear identity gives

```text
J5^0/J^0 = h |p|/E,
```

with helicity `h=+/-1`.

Therefore in the rest frame

```text
p=0 -> J5^0=0.
```

For an unpolarized ensemble the two helicities cancel at every momentum:

```text
<J5^0>_unpolarized = 0.
```

The diagonal pseudoscalar bilinear also vanishes for the same on-shell state:

```text
ubar i gamma5 u = 0.
```

`scripts/mirror_matter_matrix_element_gate.py` verifies these identities directly with explicit Dirac gamma matrices and normalized positive-energy spinors.

### Consequence

The earlier `sigma J5^0` bridge survives as a candidate for

```text
chirality / spin / velocity dependent physics,
```

but it cannot by itself generate the universal static mirror charge required for a long-range force between cold unpolarized massive bodies.

This is a genuine negative result.

---

## 2. The static source is an energy derivative

Let a matter Hamiltonian depend on the coarse mirror order `sigma`.

For a normalized stationary matter state, Hellmann--Feynman gives

```text
dE/dsigma = < dH_m/dsigma >.
```

For a rest state with physical mass `m=E_rest`, define the dimensionless mirror charge-to-mass coefficient by

```text
beta_m
 = (1/(chi*m)) < dH_m/dsigma >_rest.
```

Equivalently,

```text
Q_sigma = chi beta_m m.
```

This is now the operational definition of the missing microscopic coefficient.

It supplies a direct falsifier:

```text
if <dH_m/dsigma>_rest = 0
for every physical matter state,
then beta_m=0
```

and the static mirror-force branch dies even if the geometry has a perfectly robust `Sigma=+/-1` order.

---

## 3. Minimal positive mirror doublet

Introduce an internal mirror label

```text
q=+/-1
```

with mirror operation

```text
(sigma,q) -> (-sigma,-q).
```

Require simultaneously:

1. positive rest mass;
2. equal masses for exact mirror partners;
3. a constant universal logarithmic response to `sigma`:

```text
d ln m_q / d sigma = q beta.
```

This first-order equation has the unique solution for fixed normalization `m_*`:

```text
m_q(sigma) = m_* exp(q beta sigma).
```

It is positive for every real `sigma`.

Take the two aligned mirror branches

```text
(sigma,q) = (chi v, chi).
```

Their physical mass is

```text
m_phys = m_* exp(beta v),
```

which is identical for `chi=+1` and `chi=-1`.

But their static source is

```text
dm/dsigma
 = q beta m
 = chi beta m_phys.
```

Hence

```text
Q_sigma = chi beta m_phys
```

and therefore

```text
beta_m = beta.
```

The sign of the **charge** reverses; the rest energy stays positive.

This is exactly the structure needed by the healthy mirror-force construction without negative mass or a ghost graviton.

---

## 4. Dirac Hellmann--Feynman control

For

```text
H_D = alpha.p + beta_D m_q(sigma),
```

we have

```text
dH_D/dsigma = beta_D dm_q/dsigma.
```

For a positive-energy Dirac state,

```text
<beta_D> = m/E.
```

Therefore

```text
dE/dsigma
 = q beta m^2/E.
```

At rest `E=m`, so

```text
dE_rest/dsigma = q beta m.
```

The executable gate verifies both the rest and moving identities to machine precision.

---

## 5. beta can be read directly from a mirror-resolved mass spectrum

At any nonzero probe value `sigma`, the exponential doublet obeys

```text
m_+(sigma)/m_-(sigma) = exp(2 beta sigma).
```

Thus

```text
beta
 = [ln m_+(sigma) - ln m_-(sigma)]/(2 sigma).
```

This gives a concrete future microscopic calculation:

```text
construct H_m(sigma)
 -> diagonalize mirror-resolved rest spectrum
 -> extract m_+(sigma), m_-(sigma)
 -> compute beta
 -> compute alpha.
```

No fifth-force strength needs to be fitted in that calculation.

---

## 6. Force strength after the matter gate

The continuum normalization already gives

```text
alpha = beta_m^2/(4*pi*G*Z_sigma).
```

For the minimal mirror doublet `beta_m=beta`, so

```text
alpha = beta^2/(4*pi*G*Z_sigma).
```

Using the regular-seed Hodge stiffness

```text
Z_sigma = (2*sqrt(2)/3) J/ell,
```

one gets

```text
alpha
 = 3 beta^2 ell
   /(8*sqrt(2)*pi*G*J).
```

The repulsion criterion remains

```text
alpha > exp(m_sigma r)/(1+m_sigma r).
```

Thus the matter problem is no longer “choose alpha”. It is

```text
compute beta from the microscopic rest spectrum.
```

---

## 7. Important remaining selection problem

The finite construction demonstrates a consistent mirror doublet, but the present repository has not yet derived why low-energy physical matter should select the aligned sector

```text
q=chi
```

rather than another combination of `q` and the background mirror order.

A realistic matter theory must derive:

- the microscopic matter Hilbert space;
- its gauge/chiral representations;
- the `sigma`-dependent mass operator;
- which mirror branch is low energy;
- anomaly cancellation and the fate of any hidden mirror partner.

So `beta_m=beta` is an exact extraction rule **within the positive mirror-doublet candidate**, not yet a numerical Standard-Model prediction.

---

## Reproduction

```bash
python scripts/mirror_matter_matrix_element_gate.py \
  --output verification_results/MIRROR_MATTER_MATRIX_ELEMENT.json
```
