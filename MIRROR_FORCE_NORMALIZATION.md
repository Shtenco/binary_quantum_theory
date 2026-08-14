# Mirror-force normalization and source selection

Status: **exact continuum normalization identity + Hodge-weighted spatial stiffness matching + finite source-selection control; physical matter coupling and absolute scale still open**.

The microscopic 16-cell gate derives a real mirror order parameter

```text
Y_L/Q -> staggered Sigma -> coarse sigma(x).
```

The healthy continuum force gate shows that a positive-kinetic mirror sector can produce opposite-`chi` repulsion. The remaining question is whether the force strength `alpha` can be derived rather than chosen.

## 1. Canonical normalization

Let `sigma` be dimensionless at coarse scale and write

```text
L_sigma = Z_sigma/2 * (partial sigma)^2 - ...
```

with `Z_sigma > 0`.

For a massive source with mirror charge `chi=+/-1`, use the most general leading linear coupling

```text
L_int = - beta_m * m * chi * sigma.
```

The canonically normalized field is

```text
phi_c = sqrt(Z_sigma) * sigma
```

so the source charge seen by `phi_c` is

```text
g_m = beta_m * m * chi / sqrt(Z_sigma).
```

Tree-level exchange gives

```text
V_sigma(r)
 = - beta_1 beta_2 m1 m2 chi1 chi2
   * exp(-m_sigma r)
   / (4*pi*Z_sigma*r).
```

Comparing its long-range magnitude with

```text
V_G(r) = -G*m1*m2/r
```

gives the exact strength ratio

```text
alpha = beta_m^2 / (4*pi*G*Z_sigma)
```

for equal source normalizations.

Thus predicting `alpha` factorizes into the mirror-mode normalization and the matter source matrix element.

## 2. The existing Hodge geometry fixes the spatial stiffness matching

The repository already has the circumcentric dual/Hodge factor for a tetrahedral face `f`:

```text
A_f / d_f
```

where `A_f` is the shared triangular area and `d_f` is the circumcenter-to-circumcenter dual length.

For a dimensionless scalar order parameter on neighboring tetrahedra, the DEC Dirichlet energy is

```text
H_grad
 = (Z_sigma/2)
   * sum_f (A_f/d_f) (sigma_L-sigma_R)^2.
```

Near uniform staggered order, the microscopic face coupling can be written

```text
H_micro
 = (1/2) sum_f J_f (sigma_L-sigma_R)^2 + const.
```

Matching the same quadratic mode gives, face by face,

```text
J_f = Z_sigma * A_f/d_f
```

or

```text
Z_sigma = J_f * d_f/A_f.
```

This is the direct microscopic-to-continuum **spatial stiffness law**.

It also gives a new universality requirement: on an irregular mesh, one constant `J` generally does not represent one metric-covariant continuum `Z_sigma`. Either the microscopic coupling must acquire the Hodge weight

```text
J_f proportional to A_f/d_f
```

or RG must drive the coarse theory to that weighted form.

`scripts/mirror_hodge_stiffness_gate.py` verifies the matching on deterministic random shared-face tetrahedron pairs. Hodge-weighted `J_f` recovers the chosen common `Z_sigma` to machine precision, whereas constant `J` on the irregular control ensemble gives a strongly varying effective stiffness.

## 3. Closed form on the regular tetrahedral seed

For two regular tetrahedra of edge length `ell` glued across an equilateral face,

```text
A = sqrt(3)*ell^2/4
```

and the distance between their circumcenters is

```text
d = ell/sqrt(6).
```

Therefore constant microscopic coupling `J` gives

```text
Z_sigma
 = J*d/A
 = (2*sqrt(2)/3) * J/ell.
```

In natural units `hbar=c=1`, the force ratio becomes

```text
alpha
 = beta_m^2/(4*pi*G*Z_sigma)
 = 3*beta_m^2*ell/(8*sqrt(2)*pi*G*J).
```

So `Z_sigma` is no longer a completely abstract parameter: its **spatial part is fixed in terms of microscopic gluing energy and metric geometry**.

What is still needed for a physical prediction is the absolute/temporal normalization of the collective mode and the matter coupling `beta_m`.

## 4. Pure geometry does not automatically source the force

The 16-cell mirror-order gate found that one local orientation defect costs

```text
Delta E = 8J
```

in either mirror vacuum.

Therefore

```text
E_defect(Sigma=+1) = E_defect(Sigma=-1)
```

and the mirror-odd energy splitting is exactly zero:

```text
Delta E_odd = 0.
```

Consequently the minimal geometry-only defect has

```text
beta_geometry = 0.
```

This is an important source-selection result. Existence of the mirror order parameter does **not** imply that ordinary positive rest energy automatically carries mirror charge.

## 5. Matter must provide the charge

The earlier chirality bridge gives a natural candidate operator

```text
H_chi-psi ~ lambda_5 * sigma * J5^0.
```

For a localized matter state with integrated axial charge `Q5`, the effective source coefficient has the schematic form

```text
beta_m = lambda_5 * (Q5/m).
```

Then

```text
alpha
 = lambda_5^2 * (Q5/m)^2
   / (4*pi*G*Z_sigma).
```

Using the regular-seed stiffness gives

```text
alpha
 = 3*lambda_5^2*(Q5/m)^2*ell
   / (8*sqrt(2)*pi*G*J).
```

This is not yet a numerical physical prediction because the low-energy matter matrix element and the absolute scale `ell,J,G` relation are not derived.

It does, however, sharpen the physical statement:

> the mirror force is composition/chirality sensitive unless the microscopic theory generates a universal orientation charge proportional to mass.

This is consistent with the known possibility of promoting the Barbero-Immirzi variable to a dynamical pseudoscalar in first-order gravity, where fermionic current couplings arise naturally. It does not imply that the specific CIMFIG coupling above has already been derived.

## 6. Exact relation to the screening threshold

The healthy-force gate derived

```text
alpha_crit(x) = exp(x)/(1+x)
x = m_sigma*r.
```

Combining the normalization with the threshold gives

```text
beta_crit(x)
 = sqrt(4*pi*G*Z_sigma * exp(x)/(1+x)).
```

On the regular tetrahedral normalization:

```text
beta_crit(x)
 = sqrt(
     (8*sqrt(2)*pi*G*J/(3*ell))
     * exp(x)/(1+x)
   ).
```

Thus every proposed microscopic matter sector can now be tested directly:

```text
beta_m < beta_crit  -> attraction remains
beta_m = beta_crit  -> screening
beta_m > beta_crit  -> opposite-chi repulsion.
```

## 7. Why the remaining normalization cannot be guessed away

The HDA fixes the form of the first-class constraint algebra. It does not by itself determine the overall physical value of Newton's constant, the absolute length scale or the temporal normalization of a new collective field.

Therefore inserting an arbitrary `alpha>1` would not count as a derivation.

The chain is now

```text
16-cell / recursive Sigma order
 -> Hodge spatial stiffness J_f d_f/A_f
 -> physical length/time scale
 -> microscopic matter matrix element beta_m
 -> alpha
```

followed by the enlarged Peter-Weyl x route x mirror HDA gate.

## 8. Falsifier

The branch now has a very sharp failure condition:

```text
if beta_m = 0
for every admissible microscopic matter operator,
then alpha = 0
```

and the derived mirror order cannot generate a matter fifth force, regardless of how robust the `Sigma=+/-1` order itself is.

A second failure condition is range:

```text
m_sigma*r >> 1
```

exponentially suppresses the force even when `beta_m` is nonzero.

Therefore a macroscopic repulsive branch requires simultaneously

```text
beta_m != 0
m_sigma*r <= O(1)
alpha > alpha_crit(m_sigma*r)
stable Hamiltonian
closed enlarged HDA.
```

## Reproduction

Source normalization:

```bash
python scripts/mirror_force_normalization_gate.py \
  --output verification_results/MIRROR_FORCE_NORMALIZATION.json
```

Hodge stiffness matching:

```bash
python scripts/mirror_hodge_stiffness_gate.py \
  --output verification_results/MIRROR_HODGE_STIFFNESS.json
```
