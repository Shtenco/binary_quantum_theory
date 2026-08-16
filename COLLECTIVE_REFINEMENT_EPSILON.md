# Frozen collective refinement resolution epsilon

For every collective refinement level the power-law variable is the measured dimensionless intrinsic mesh resolution

\[
\boxed{\epsilon_l=\frac{h_l}{R_l}},
\]

where

- `h_l` is the median unique intrinsic PL edge length of the embedded barycentric tetrahedral complex;
- `R_l = V_l^(1/3)` with `V_l` the total intrinsic piecewise-flat 3-volume.

This replaces arbitrary choices such as `epsilon=2^-level` or using the refinement index itself.  It is frozen before the first collective HDA residual is computed.

For the canonical embedded 16-cell family the local reproduction gives

```text
level    V                  h                  R                  epsilon=h/R
0        5.333333333333332  1.4142135623730951 1.7471609294725976 0.8094352034302834
1        5.333333333333359  0.5                1.7471609294726005 0.2861785606383325
2        5.333333333332456  0.2357022603955158 1.7471609294725020 0.1349058672383880
3        5.333333333331203  0.0931694990624913 1.7471609294723651 0.0533262262742036
```

The total volume is conserved and `epsilon_l` decreases strictly.

## Use in the killer gate

Every direct collective science row must report this measured `epsilon`, or the exact same prescription applied to the **dynamically measured collective metric** if that metric differs from the static embedded precursor.

The production preference is:

1. use `h/R` from the direct dynamical collective metric when available;
2. report the static-background `h/R` beside it as a regulator control;
3. never choose between competing epsilon definitions after inspecting the HDA power.

No target value for `D_space`, `c_DeWitt`, constraint rank, `N_phys` or `Delta_HH` enters this resolution definition.
