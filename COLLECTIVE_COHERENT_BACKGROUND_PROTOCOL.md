# BCQG collective coherent/refinement background protocol

## Motivation

The sharp all-`j=1/2` seed is an excellent exact algebraic reference state but fails as a **linear expectation-value metric background** for the six-edge `P4` carrier: spin-preserving flux/metric observables have zero cross matrix elements between the sharp seed and changed-spin `W_g` states.

The GR-universality science run therefore needs a background with overlapping representation support. The choice must be frozen without looking at `c_eff`, constraint ranks or photon data.

## 1. Minimal S4-homogeneous finite precursor

Let the six orthonormal microscopic edge columns be `|w_e>` and define the uniform intrinsic mode

\[
|u\rangle=\frac1{\sqrt6}\sum_{e=1}^6|w_e\rangle.
\]

Since the six-edge representation decomposes as `A1+E+T2`, `|u>` is the unique `A1` direction.

Define

\[
\boxed{|\Omega_\alpha\rangle=\frac{|0\rangle+\alpha|u\rangle}{\sqrt{1+\alpha^2}}}.
\]

This state is target-independent, preserves tetrahedral homogeneity and mixes the original sharp spin sector with the first intrinsic dynamical sector.

Primary finite precursor:

```text
alpha = 1
```

Mandatory robustness scan:

```text
alpha = 1/4, 1/2, 1, 2
```

No value may be selected or discarded because it makes `c_eff` closer to `1/2`.

## 2. Tangent frame about the mixed background

The normalized trace/radial tangent is

\[
|t_{A1}\rangle=\frac{|u\rangle-\alpha|0\rangle}{\sqrt{1+\alpha^2}}.
\]

The five shape tangents are any frozen orthonormal `E(2)+T2(3)` combinations of the six edge vectors orthogonal to `|u>`. They remain orthogonal to `|Omega_alpha>`.

This yields a six-dimensional orthonormal tangent frame with no use of GR target data.

## 3. Direct metric-response requirement

For six coarse geometric observables `y_e` constructed from BCQG flux/metric data, measure

\[
B_{eA}(\alpha)=2\,\mathrm{Re}\langle\Omega_\alpha|\hat y_e|t_A\rangle.
\]

The background qualifies for the metric Hessian only if:

1. `rank B = 6` at the frozen numerical tolerance;
2. the rank is stable over `1e-7,1e-8,1e-9` SVD thresholds;
3. the `A1`, `E`, `T2` channel singular values are finite and reported separately;
4. the condition number is acceptable and improves/stabilizes under refinement;
5. no `alpha` is tuned using the DeWitt result.

At finite tetrahedral symmetry `B` is allowed three channel scales `b_A1,b_E,b_T2`. Continuum rotational isotropy requires the `E` and `T2` calibrations to merge.

## 4. Beyond the minimal two-sector precursor

`Omega_alpha` is a finite diagnostic, not asserted to be the final semiclassical vacuum. If it fails nondegeneracy/semiclassicality, the extension order is frozen as:

1. enlarge with target-independent depth-2 `E,S,R_op` Krylov sectors;
2. construct a Gauss-projected representation packet using only BCQG geometric/dynamical observables;
3. determine its parameters by a background stationarity/minimum-uncertainty criterion, never by the GR target values.

Every extension must retain the sharp-spin state as a reproducible control.

## 5. Photon interpretation

The distinction between sharp and coherent backgrounds is experimentally meaningful in the optical bridge.

- Sharp spin reference: first-order mean metric response to `W_g` excitations vanishes for spin-preserving metric/Hodge observables; leading optical effects can instead enter through phase variance/path-geometry entanglement.
- Mixed/coherent background: nonzero `B` permits the conventional linear eikonal phase `Delta Phi=(k ell_*/2) D J h`.

Thus phase shift and visibility are separate observables of the same collective geometry rather than interchangeable claims.

## Status

`PREREGISTERED_BACKGROUND_PRECURSOR`. The next direct calculation is the six-by-six metric-response matrix `B(alpha)` followed by the three representative S4 channels of the effective scalar constraint.
