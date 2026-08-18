# Physical scale and observable map

Status: **canonical scale/units bridge for the closed candidate package; external data validation remains separate.**

The internal theory produces dimensionless geometric and TT quantities. A physical comparison additionally needs one common normalization that converts the microscopic length/time units into SI or particle-physics units. That normalization is not allowed to vary independently by observable.

## 1. Regge normalization

With the Einstein-Hilbert convention

```text
S_EH = c^3/(16*pi*G) int d^4x sqrt(-g) R
```

and the smooth Regge correspondence

```text
int sqrt(|g|) R d^4x  <->  2 sum_h A_h delta_h,
```

write

```text
A_h = a_*^2 Atilde_h
```

and define `lambda_R_eff` as the dimensionless coefficient multiplying
`sum_h Atilde_h delta_h` in `S_eff/hbar`. Then

```text
lambda_R_eff = a_*^2/(8*pi*l_P^2)
```

so

```text
a_*/l_P = sqrt(8*pi*lambda_R_eff).
```

This is an exact unit-conversion relation in the declared convention. If `lambda_R_eff` is not independently derived, exactly one declared calibration datum may set the common scale.

## 2. Time normalization

For a dimensionless low-momentum tensor dispersion

```text
omega_tilde = v0 |k_tilde| + ...
```

and microscopic units `a_*`, `tau_*`,

```text
c_TT = v0 a_*/tau_*.
```

The internal result `z approximately 1` establishes compatible space/time scaling but is not itself an SI conversion factor.

## 3. Complete TT observable input

The generic quartic parity-even S4 TT response is six-dimensional:

```text
c_IR = (c1,c2,c3,c4,c5,c6).
```

For direction `n`, `scripts/s4_tt_six_wilson_predictor.py` constructs the real symmetric 2x2 quartic TT matrix and its two eigenvalues

```text
e4_1(n), e4_2(n).
```

A frozen branch may be written as

```text
omega_sigma^2 = c^2 k^2 [1 + a_*^2 k^2 e4_sigma(n) + ...].
```

## 4. Modified-dispersion units

In the standard alpha=4 convention

```text
E^2 = (pc)^2 + A4 (pc)^4 + ...,
```

the algebraic map is

```text
A4_sigma(n) = a_*^2 e4_sigma(n)/(hbar*c)^2
            = 8*pi*lambda_R_eff*e4_sigma(n)/E_P^2.
```

The same frozen eigenvalues determine the leading group-velocity and accumulated-phase corrections. A real cosmological catalog comparison must use the appropriate redshift/proper-distance propagation integral rather than a flat-space distance shortcut.

## 5. No-fit rule

Allowed:

```text
freeze dimensionless six-vector
freeze conventions
set or derive one common scale
predict all remaining directions/polarizations/observables
open held-out external data
```

Forbidden:

```text
separate scale per observable
separate scale per sky direction
retuning the six-vector after holdout inspection
promoting construction selectors or oracle controls to blind predictions
```

## 6. External validation

This document closes the algebraic scale/units dictionary. It does not claim that any external dataset has confirmed the candidate. The preregistered observational protocol is in `PREDICTIONS_AND_EXPERIMENTAL_TESTS.md`.

Reproduction of the pure unit translator:

```bash
python scripts/physical_scale_prediction_bridge.py \
  --lambda-r-eff 1.0 \
  --eta2 -0.022222222222222222 \
  --frequency-hz 100 \
  --distance-mpc 1000
```

The translator performs no fitting.
