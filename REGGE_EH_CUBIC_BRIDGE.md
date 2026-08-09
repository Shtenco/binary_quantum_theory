# Regge -> Einstein-Hilbert cubic bridge

Status: **nonlinear finite-lattice evidence; full microscopic Einstein IR is not proved**.

## Purpose

The quadratic test in `GRAVITY_BRIDGE_SCALING.md` shows that the full unprojected metric Hessian approaches Fierz--Pauli.  That is still a free-field result.  This test asks a harder question: does a genuinely nonlinear coefficient of the finite Regge action approach the same coefficient obtained from the continuum Einstein--Hilbert functional for the **same smooth metric field**?

We use a deterministic generic traceless symmetric three-wave perturbation

\[
g_{\mu\nu}(x)=\delta_{\mu\nu}
+\varepsilon\left[
P^{(1)}_{\mu\nu}\cos(kx_1)
+P^{(2)}_{\mu\nu}\cos(kx_2)
+P^{(3)}_{\mu\nu}\cos(kx_1+kx_2)
\right],
\]

with fixed seed `260809`.  The three modes contain a momentum-conserving triad, so the cubic action does not vanish trivially.

For the Regge lattice the same field is mapped to squared edge lengths at edge midpoints.  Independently, the continuum reference is evaluated as

\[
S_{EH}=\int d^4x\,\sqrt g\,R
\]

using spectral derivatives on an auxiliary periodic grid.  Both actions are fitted as

\[
S(\varepsilon)=c_0+c_1\varepsilon+c_2\varepsilon^2+c_3\varepsilon^3+c_4\varepsilon^4+c_5\varepsilon^5.
\]

The standard smooth Regge normalization is

\[
\int\sqrt g\,R\;\longleftrightarrow\;2\sum_h A_h\delta_h,
\]

so the parameter-free smooth target is

\[
\boxed{\frac{c_n^{Regge}}{c_n^{EH}}\to\frac12}
\]

for both the quadratic and cubic coefficients.

## Main scan

The stable small-amplitude fit uses `eps_max=0.03`, 11 symmetric samples and continuum spectral grid 8.

| L | c2 Regge/EH | c3 Regge/EH | (c3/c2) Regge | (c3/c2) EH | relative nonlinear-ratio error |
|--:|--:|--:|--:|--:|--:|
| 3 | 0.392029 | 0.314255 | -0.122157 | -0.152389 | 0.1984 |
| 4 | 0.431849 | 0.314375 | -0.110936 | -0.152389 | 0.2720 |
| 5 | 0.453916 | 0.371737 | -0.124800 | -0.152389 | 0.1810 |
| 6 | 0.467013 | 0.407087 | -0.132835 | -0.152389 | 0.1283 |
| 7 | 0.475314 | 0.429964 | -0.137850 | -0.152389 | 0.09541 |
| 8 | 0.480872 | 0.445474 | -0.141172 | -0.152389 | 0.07361 |

`L=3,4` are visibly pre-asymptotic for the cubic observable.  On the cleaner `L=5..8` window:

\[
\left|\frac{c_2^{Regge}}{c_2^{EH}}-\frac12\right|
\sim L^{-1.87},
\]

\[
\left|\frac{c_3^{Regge}}{c_3^{EH}}-\frac12\right|
\sim L^{-1.82},
\]

and

\[
\left|
\frac{(c_3/c_2)_{Regge}}{(c_3/c_2)_{EH}}-1
\right|
\sim L^{-1.91}.
\]

All three are compatible, at the precision and sizes tested, with the expected leading `O(k^2) ~ O(L^-2)` discretization correction.

A linear extrapolation in `1/L^2` on `L=5..8` gives

\[
\boxed{(c_2^{Regge}/c_2^{EH})_{L\to\infty}=0.497924}
\]

and

\[
\boxed{(c_3^{Regge}/c_3^{EH})_{L\to\infty}=0.491859}.
\]

Thus the independent quadratic and cubic normalizations extrapolate to the expected `1/2` within about `0.42%` and `1.63%`, respectively, on this small four-size fit.

## Robustness checks

The continuum nonlinear ratio is numerically stable:

- spectral grid `8`, `10`, `12` changes `(c3/c2)_EH` only below the shown digits;
- `eps_max=0.03` gives approximately `-0.152389373`;
- `eps_max=0.05` gives approximately `-0.152389214`.

The Regge nonlinear ratio is also stable against the amplitude window.  Examples:

| L | eps_max=0.02 | eps_max=0.03 | eps_max=0.05 |
|--:|--:|--:|--:|
| 5 | -0.124800037 | -0.124800025 | -0.124799909 |
| 6 | -0.132835180 | -0.132835170 | -0.132835054 |
| 8 | -0.141171654 | -0.141171633 | -0.141171497 |

The fitted linear coefficient stays close to zero, as required around the flat stationary background.

## Interpretation

This result is stronger than a TT-only nonlinear stretch test:

1. the perturbation is a generic symmetric metric field, not a single TT polarization;
2. the cubic term is nonzero because the field contains a momentum-conserving triad;
3. the continuum reference is computed independently from Christoffels, Ricci tensor and `sqrt(g) R` rather than by inserting a known cubic coefficient;
4. both `c2` and `c3` approach the parameter-free Regge/EH normalization `1/2`;
5. the remaining error falls approximately quadratically with lattice spacing on the asymptotic window tested.

The correct current statement is therefore

\[
\boxed{\text{finite 4D Regge action shows direct quadratic + cubic convergence to the EH functional for the tested smooth field}.}
\]

This still does **not** establish:

- the cubic Ward identity `delta_0 S_3 + delta_1 S_2 = 0` from microscopic independent connection/frame variables;
- a regulator-independent blocked effective action of the binary edge-bit ensemble;
- Lorentzian unitarity or a selected quantum measure;
- dynamical emergence of four dimensions rather than use of a 4D scaffold;
- universal matter coupling, chirality and anomaly cancellation;
- experimental validation.

## Reproduction

```bash
python scripts/regge_eh_cubic_bridge.py \
  --sizes 5 6 7 8 \
  --grid 8 \
  --eps-max 0.03 \
  --samples 11 \
  --output verification_results/regge_eh_cubic_bridge.json
```

The next gravity calculation should contract a momentum-conserving cubic vertex with a gauge variation and test the nonlinear Ward combination rather than merely matching another scalar action coefficient.
