# TT dispersion under H_kin = −H_Regge

Linearised tests on `FlatRegge4D` (L=3), kinetic Hessian

\[
H_{\mathrm{kin}} = -H[S_{\mathrm{Regge}}].
\]

## Results (representative momenta)

| \(|k|\) | TT mean | TT/k² | TT>0 | Bianchi |
|--:|--:|--:|---|--:|
| 2.09 | 7.5 | 1.71 | yes | ~1e-8 |
| 2.96 | 13.1 | 1.50 | yes | ~1e-8 |
| 3.63 | 22.1 | 1.68 | yes | ~1e-8 |
| 4.19 | 14–33 | 0.8–1.9 | yes | ~1e-8 |
| 5.92 | 25.5 | 0.73 | yes | ~1e-8 |

- **TT > 0** on all tested k
- **TT/k² ≈ 1.34 ± 0.43** (dispersion proxy; order-one, positive)
- **Regge/continuum ratio** (vs \(k^2/4\)) ≈ 5.4 ± 1.7 (lattice normalisation, not 1)
- Gauge nulls / Bianchi **unchanged** under overall sign flip

Pure-trace embedding via edge map is only approximate (overcomplete \(n^\mu n^\nu\)); do not over-interpret trace Rayleigh on the lattice.

## Claim boundary

This establishes a **linearised Euclidean kinetic pattern** (TT positive, gauge clean, rough \(\omega^2 \propto k^2\) proxy).

It does **not** prove the nonlinear continuum limit is Einstein–Hilbert.
