# Directional Regge residue: absolute normalization control

Status: **completed finite-lattice consistency result; not a microscopic six-Wilson prediction.**

Workflow `physicalization-regge-directional-quartic` run `32037899460` completed successfully and stored the absolute Fierz-Pauli fit coefficients for the three frozen momentum directions `(100)`, `(110)`, `(111)` at `L=3,4,5`.

The underlying mode amplitude is not normalized by `1/sqrt(volume)` and the Regge action is summed over the full `L^4` lattice.  Consequently the leading Fierz-Pauli coefficient scales extensively.  The corresponding intensive residue diagnostic is

\[
\boxed{Z_{dir}(L)=c_0^{dir}(L)/L^4.}
\]

## Raw and intensive values

| direction | L=3 c0 | L=4 c0 | L=5 c0 |
|---|---:|---:|---:|
| 100 | 8.271112330189368 | 28.534034458911265 | 72.58033779183708 |
| 110 | 7.309364618125481 | 26.475075900287145 | 69.07749760413965 |
| 111 | 5.642319400435426 | 22.727749318201795 | 62.54882166237611 |

After division by `L^4`:

| direction | Z(3) | Z(4) | Z(5) |
|---|---:|---:|---:|
| 100 | 0.102112498 | 0.111461072 | 0.116128540 |
| 110 | 0.090239069 | 0.103418265 | 0.110523996 |
| 111 | 0.069658264 | 0.088780271 | 0.100078115 |

All three sequences rise toward the independently frozen continuum normalization `1/8=0.125`.

A three-point diagnostic fit

\[
Z(L)=Z_\infty+C/L^2+D/L^4
\]

returns

```text
100: Z_inf = 0.1249581589
110: Z_inf = 0.1247277286
111: Z_inf = 0.1239867432
```

whose relative offsets from `1/8` are approximately

```text
100: -0.0335 %
110: -0.2178 %
111: -0.8106 %
```

Because three points determine the three fit parameters exactly, these intercepts are **diagnostics**, not independent continuum predictions.

## Tensor-structure convergence

The same successful run fits the full unprojected metric Hessian to the four two-derivative Fierz-Pauli tensors.

For the axial direction the linear `1/L^2` continuum ratios are

```text
[1,
 -2.0003174076410657,
  2.0011994209614445,
 -1.0006796220631886]
```

with relative ratio error `4.4735270225317535e-4`.

The finite-size Fierz-Pauli matrix residual and ratio error scale approximately as

```text
matrix residual ~ L^-2.0959
ratio error     ~ L^-2.0205
```

for the axial sequence.

For diagonal directions the finite gauge-to-metric leakage is larger, but decreases approximately as

```text
110 leakage ~ L^-2.2925
111 leakage ~ L^-2.2376.
```

The corresponding three-point continuum ratio errors are about `1.52%` and `5.95%`, respectively, so these directions are not yet as asymptotic as `(100)`.

## Important non-overclaim

The directional differences of the intensive residues themselves over only `L=3,4,5` do **not** yet show a clean `L^-2` power law.  Effective powers from these three points are only about `1.46` for `|Z110-Z100|` and `1.37` for `|Z111-Z100|`.

Therefore the completed result supports, but does not by itself prove, restoration of a common leading two-derivative residue.

A directional `L=6` (and preferably `L=7`) extension is the correct next held-out control.

## Physical meaning

This Regge calculation is an independent downstream geometric scaffold.  It supports the required hierarchy

```text
leading derivative order <=2 -> Einstein/Fierz-Pauli and increasingly isotropic
subleading derivative order 4 -> allowed location for lattice/tetrahedral memory
```

but its finite Regge coefficients are **not** the microscopic BCQG values `c1...c6`, `eta2`, `zeta4` or `gamma4`.

Those require the physical projector/history kernel and microscopic multi-block TT calculation.
