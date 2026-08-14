# Mirror-force normalization and source selection

Status: **exact continuum normalization identity + finite source-selection control; physical coupling still open**.

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

Thus the problem of predicting `alpha` factorizes cleanly into two microscopic questions:

```text
1. derive Z_sigma
2. derive beta_m.
```

## 2. Pure geometry does not automatically source the force

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

## 3. Matter must provide the charge

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

This is not yet a numerical prediction because neither the physical normalization `Z_sigma` nor the microscopic low-energy value of `lambda_5 Q5/m` has been derived.

It does, however, sharpen the physical statement:

> the mirror force is composition/chirality sensitive unless the microscopic theory generates a universal charge proportional to mass.

## 4. Exact relation to the screening threshold

The healthy-force gate derived

```text
alpha_crit(x) = exp(x)/(1+x)
x = m_sigma*r.
```

Combining the two results gives the required matter coupling

```text
beta_crit(x)
 = sqrt(4*pi*G*Z_sigma * exp(x)/(1+x)).
```

Thus every proposed microscopic matter sector can now be tested directly:

```text
beta_m < beta_crit  -> attraction remains
beta_m = beta_crit  -> screening
beta_m > beta_crit  -> opposite-chi repulsion.
```

## 5. Why the remaining normalization cannot be guessed away

The HDA fixes the form of the first-class constraint algebra. It does not by itself determine the overall physical value of Newton's constant or the continuum normalization of a new collective field.

Therefore inserting an arbitrary `alpha>1` would not count as a derivation.

The next legitimate calculation is

```text
16-cell Sigma spectrum
 -> block-to-block propagation
 -> continuum Z_sigma
 -> microscopic matter matrix element beta_m
 -> alpha
```

followed by the enlarged Peter-Weyl x route x mirror HDA gate.

## 6. Falsifier

The branch now has a very sharp failure condition:

```text
if beta_m = 0
for every admissible microscopic matter operator,
then alpha = 0
```

and the derived mirror order cannot generate a matter fifth force, regardless of how robust the `Sigma=+/-1` order itself is.

## Reproduction

```bash
python scripts/mirror_force_normalization_gate.py \
  --output verification_results/MIRROR_FORCE_NORMALIZATION.json
```
