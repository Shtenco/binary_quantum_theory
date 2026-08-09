# Lattice field normalisation

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

on tested momenta — **not** 1. Decreases mildly with \(|k|\) but does not extrapolate to continuum matching in the L=3 window.

## Implications

- Old “Regge/continuum ratio ~5” mixed **kinetic coefficient** with **edge-space normalisation**.
- Field-norm comparison is the right test; it still fails \(c_{\mathrm{eff}}\to 1\).
- TT **sign** under \(H_{\mathrm{kin}}\) remains healthy; only the **absolute coefficient** is off.

## Regge alternatives (position)

| approach | note |
|---|---|
| area–deficit (this repo) | keep + \(H_{\mathrm{kin}}\) convention |
| Palatini / first-order | Gate C2 frame gauge; full torsion-free e.o.m. open |
| CDT / spin foams | different ensembles; continuum not assumed here |

Do **not** switch frameworks to hide a normalisation mismatch.

## Status

Normalisation **diagnosed**. Continuum kinetic coefficient **not matched**. IR Einstein **open**.
