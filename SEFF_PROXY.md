# Blocked S_eff proxy (v14)

## Setup

- Micro: Metropolis on edge lengths of `FlatRegge4D` (L=3)
- Weight: Euclidean \(\exp(-\beta S_{\mathrm{kin}})\), \(S_{\mathrm{kin}}=-S_{\mathrm{Regge}}\)
- Block: index-bin average of log-length fluctuations (\(B=8\)) — **not** geometric block-spin
- Fit: \(G^{-1}\approx \alpha\,\mathrm{Lap}+m^2\)

## Result

- \(\alpha>0\) (kinetic-like term present in the proxy)
- residual \(\sim 0.77\) — **poor** fit; statistics small; blocking non-geometric
- **Does not** match continuum Einstein–Hilbert

## Lorentzian

Not computed. Euclidean weight only. Causal/Wick structure open.

## Measure Q1–Q2

Axioms exist in the verification suite; multiway lift of a unique path-space measure remains open.

## Scoreboard

| layer | status |
|---|---|
| Linearised P1–P3 + G_eff | yes |
| Local nonlinear a2>0 | yes |
| Blocked S_eff proxy ran | yes |
| S_eff = EH | **no** |
| Lorentzian | **no** |
| IR Einstein | **no** |

## One line

Proxy demonstrates a workflow toward S_eff; it does not establish continuum Einstein gravity.
