# Mirror-force normalization and source selection

Status: **exact continuum normalization identity + Hodge-weighted spatial stiffness + finite matter-source extraction rule; numerical microscopic matter coupling and absolute scale remain open**.

The mirror branch now has the chain

```text
Y_L/Q
 -> staggered Sigma
 -> coarse sigma(x)
 -> Z_sigma
 -> beta_m
 -> alpha
 -> F_mirror.
```

The force strength is no longer treated as a free phenomenological sign. The remaining matter coefficient is an explicit rest-energy matrix element.

---

## 1. Canonical normalization

Let `sigma` be dimensionless and write

```text
L_sigma = Z_sigma/2 * (partial sigma)^2 - ...,
Z_sigma > 0.
```

A static source with orientation label `chi=+/-1` is parameterized by

```text
Q_sigma = chi beta_m m.
```

After canonical normalization

```text
phi_c = sqrt(Z_sigma) sigma,
```

the source charge is

```text
g_m = chi beta_m m/sqrt(Z_sigma).
```

Tree-level exchange gives

```text
V_sigma(r)
 = - beta_1 beta_2 m1 m2 chi1 chi2
   * exp(-m_sigma r)
   /(4*pi*Z_sigma*r).
```

Relative to

```text
V_G(r) = -G m1 m2/r,
```

the exact strength ratio is

```text
alpha = beta_m^2/(4*pi*G*Z_sigma)
```

for equal source normalization.

---

## 2. Existing Hodge geometry fixes the spatial stiffness

For a tetrahedral face `f`, the repository already uses the circumcentric Hodge factor

```text
A_f/d_f.
```

For the coarse mirror order,

```text
H_grad
 = (Z_sigma/2)
   sum_f (A_f/d_f)(sigma_L-sigma_R)^2.
```

The microscopic staggered gluing energy near uniform order is

```text
H_micro
 = (1/2) sum_f J_f (sigma_L-sigma_R)^2 + const.
```

Matching the quadratic mode gives

```text
J_f = Z_sigma A_f/d_f
```

and hence

```text
Z_sigma = J_f d_f/A_f.
```

`scripts/mirror_hodge_stiffness_gate.py` verifies this matching on irregular shared-face controls. A common continuum `Z_sigma` requires the microscopic coupling to carry the corresponding Hodge weight, or an RG flow to generate it.

For a regular tetrahedral seed of edge length `ell`,

```text
A = sqrt(3) ell^2/4,
d = ell/sqrt(6),
```

so

```text
Z_sigma = (2*sqrt(2)/3) J/ell.
```

Therefore, in natural units,

```text
alpha
 = 3 beta_m^2 ell
   /(8*sqrt(2)*pi*G*J).
```

The spatial stiffness is therefore tied to the same microscopic gluing energy and dual metric data already present in the geometry sector.

---

## 3. Pure geometry does not automatically carry mirror charge

The 16-cell gate gives one local orientation defect the same energy in both mirror vacua:

```text
E_defect(Sigma=+1)=E_defect(Sigma=-1).
```

Thus the mirror-odd splitting of the geometry-only defect is zero and

```text
beta_geometry = 0.
```

The existence of `Sigma=+/-1` therefore does not make ordinary positive rest energy automatically source the mirror force.

---

## 4. Correction: the axial density is not a universal static source

The earlier chirality bridge

```text
sigma J5^0
```

is parity allowed and remains useful for chirality/spin-sensitive physics.

However the explicit Dirac gate now shows

```text
J5^0/J^0 = h |p|/E.
```

Hence

```text
J5^0 = 0
```

for a massive particle at rest, and the unpolarized average vanishes at every momentum. The diagonal pseudoscalar bilinear `ubar i gamma5 u` also vanishes on the same free on-shell state.

Therefore `sigma J5^0` cannot by itself supply a universal static charge for cold unpolarized massive matter.

This is a source-selection no-go, not a failure of the chirality bridge.

---

## 5. Operational definition of beta_m

Let the microscopic matter Hamiltonian depend on the coarse mirror field `sigma`.

Hellmann--Feynman gives

```text
dE/dsigma = <dH_m/dsigma>.
```

For a rest state with `E=m`, define

```text
beta_m
 = (1/(chi*m))
   <dH_m/dsigma>_rest.
```

Equivalently,

```text
Q_sigma = <dH_m/dsigma>_rest
        = chi beta_m m.
```

This is now the exact quantity that a future microscopic matter Hamiltonian must calculate.

If it vanishes for every physical state, then

```text
beta_m = 0
alpha  = 0
```

and the static mirror-force branch fails.

---

## 6. Minimal positive mirror-doublet candidate

Introduce an internal mirror label `q=+/-1` with

```text
(sigma,q) -> (-sigma,-q).
```

Demand positive mass and a constant universal logarithmic response

```text
d ln m_q/dsigma = q beta.
```

The unique solution at fixed normalization is

```text
m_q(sigma)=m_* exp(q beta sigma).
```

For aligned mirror states

```text
(sigma,q)=(chi v,chi),
```

the two mirror partners have the same positive physical mass

```text
m_phys=m_* exp(beta v),
```

but opposite static source

```text
dm/dsigma = chi beta m_phys.
```

Thus, within this minimal positive-mass candidate,

```text
beta_m = beta.
```

For a Dirac Hamiltonian

```text
H_D = alpha.p + beta_D m_q(sigma),
```

the finite matrix-element gate verifies

```text
dE/dsigma = q beta m^2/E,
```

which reduces at rest to `q beta m`.

The same coefficient can be extracted from a mirror-resolved rest spectrum:

```text
beta
 = [ln m_+(sigma)-ln m_-(sigma)]/(2 sigma).
```

This gives a direct microscopic program rather than a fitted force strength.

---

## 7. Exact screening threshold in terms of the matter matrix element

The force gate gives

```text
alpha_crit(x)=exp(x)/(1+x),
x=m_sigma r.
```

Therefore

```text
beta_crit(x)
 = sqrt(4*pi*G*Z_sigma * exp(x)/(1+x)).
```

For the regular-seed stiffness,

```text
beta_crit(x)
 = sqrt(
     (8*sqrt(2)*pi*G*J/(3*ell))
     * exp(x)/(1+x)
   ).
```

A proposed microscopic matter spectrum can therefore be tested directly:

```text
|beta_m| < beta_crit -> attraction remains
|beta_m| = beta_crit -> screening
|beta_m| > beta_crit -> opposite-chi repulsion.
```

---

## 8. Range is an independent killer gate

The mirror order is `Z2`, so its existence does not imply a Goldstone mode.

`scripts/mirror_sigma_range_gate.py` shows that the deep ordered 16-cell block has a non-tunnelling excitation gap of order `8J`; the finite crossover softens it but does not close it.

Thus a macroscopic force requires independently

```text
m_sigma r <= O(1).
```

A physical long-range branch needs a parametrically light refined collective mode or a separate light mediator, together with the correct temporal normalization.

---

## 9. Current falsifiers

A macroscopic repulsive branch now requires simultaneously

```text
beta_m != 0
m_sigma r <= O(1)
alpha > exp(m_sigma r)/(1+m_sigma r)
stable positive-energy Hamiltonian
closed enlarged HDA.
```

Failure of any one condition kills macroscopic mirror repulsion.

The remaining microscopic matter problem is therefore sharply defined:

```text
construct H_m(sigma)
 -> compute <dH_m/dsigma>_rest
 -> extract beta_m
 -> combine with Z_sigma
 -> predict alpha
 -> test the range and enlarged HDA.
```

---

## Reproduction

```bash
python scripts/mirror_force_normalization_gate.py \
  --output verification_results/MIRROR_FORCE_NORMALIZATION.json

python scripts/mirror_hodge_stiffness_gate.py \
  --output verification_results/MIRROR_HODGE_STIFFNESS.json

python scripts/mirror_matter_matrix_element_gate.py \
  --output verification_results/MIRROR_MATTER_MATRIX_ELEMENT.json

python scripts/mirror_sigma_range_gate.py \
  --output verification_results/MIRROR_SIGMA_RANGE.json
```
