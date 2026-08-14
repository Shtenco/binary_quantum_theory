# Lattice field normalisation

> **Canonical status note.** The old target `c_eff -> 1` in this diagnostic is superseded by `RESOLUTION.md`.  The continuum reference `k^2/4` already assumes a chosen Newton/wave-function normalization.  Therefore the overall finite positive `c_eff` is a coupling normalization to be fixed by the physical scale map, while tensor structure, gauge nulls, sign and momentum dependence remain the relevant structural tests.  The numerical values below are preserved as historical diagnostics; they are not a failed-GR criterion.

## Two Rayleigh quotients

Continuum (unit Frobenius \(||h||_F=1\)):

\[
S_{\mathrm{cont}} = \frac{k^2}{4}.
\]

Regge mode embedding \(v = \mathrm{embed}(h)\) via \(M\colon h_{\mu\nu}\mapsto n^\mu n^\nu h_{\mu\nu}\) on 15 edge types.

| quotient | definition | typical value (L=3, \(|k|=2\pi/3\)) |
|---|---|--:|
| edge-norm | \(v^T H_{\mathrm{kin}} v / \|v\|^2\) | ~7 |
| field-norm | \(v^T H_{\mathrm{kin}} v / \|h\|_F^2\) | ~35 |
| continuum | \(k^2/4\) | ~1.1 |

Singular values of \(M\) span ~1–8 (condition ~8). Stretch \(\|Mh\|/\|h\|_F\sim 2.5\).

## Effective coefficient

\[
c_{\mathrm{eff}} = \frac{Q_{\mathrm{field}}(h)}{k^2/4} \sim 20\text{–}34
\]

on tested momenta.  These values diagnose the overall lattice coupling/wave-function normalization plus finite-lattice effects; the canonical theory no longer demands that this raw number approach one before scale matching.

## Implications

- Old “Regge/continuum ratio ~5” mixed **kinetic coefficient** with **edge-space normalisation**.
- Field-norm comparison remains the right way to expose the overall coefficient without mixing it with the edge embedding.
- TT **sign** under \(H_{\mathrm{kin}}\) remains healthy.
- The absolute coefficient must be carried into the physical scale/Newton normalization rather than normalized away after seeing data.

## Regge alternatives (position)

| approach | note |
|---|---|
| area–deficit (this repo) | keep + \(H_{\mathrm{kin}}\) convention |
| Palatini / first-order | Gate C2 frame gauge; full torsion-free e.o.m. open |
| CDT / spin foams | different ensembles; continuum not assumed here |

Do **not** switch frameworks to hide a normalisation issue.

## Status

Historical normalization diagnostic preserved.  The `c_eff -> 1` falsifier is retracted by `RESOLUTION.md`.  Absolute physical scale setting is now handled by `PHYSICALIZATION_SCALE_OBSERVABLE_PREDICTION.md`; nonlinear/quantum microscopic Einstein IR remains a separate question.
