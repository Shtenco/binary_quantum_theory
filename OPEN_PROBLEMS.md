# Open problems (post kinetic-sign fix)

## Done

- Numerology purged from README
- \(H_{\mathrm{kin}}=-H_{\mathrm{Regge}}\): TT>0 on tested k
- Gauge Ward intact
- TT/k² = O(1) > 0 (dispersion proxy)

## Small ka (L=3,4)

| L | min \(|k|\)=2π/L | TT/k² | ratio to continuum \(k^2/4\) |
|--:|--:|--:|--:|
| 3 | 2.09 | 1.80 | 7.2 |
| 4 | 1.57 | 6.72 | 26.9 |

TT stays positive. The continuum coefficient does **not** approach 1 when L increases in this window — lattice normalisation / edge-map artefacts dominate. More work needed (better continuum extrapolation, matching of field normalisation).

## Lorentzian / path integral

\(H_{\mathrm{kin}}\) fixes **Euclidean quadratic** tests only.

- Lorentzian spectrum, causal Regge histories, Wick rotation: **not computed**
- Weight \(e^{iS}\) vs \(e^{-S}\) vs CIMFIG quantum measure: **not selected** by the kinetic sign

## Coarse-graining → effective EH

**Map (architecture):**

1. Micro: \(q_e\) (and/or connection)
2. Block: \(B_b\) → continuum field \(g_{\mu\nu}(X)\)
3. \(S_{\mathrm{eff}}[g]=-\log\int_{B(q)=g}\!D\mu[q]\,e^{-S_{\mathrm{kin}}[q]}\)
4. Match 2-derivative sector to Einstein–Hilbert

**Exists:** micro Regge, H_kin TT pattern, gauge Ward, fork-2 philosophy.  
**Missing:** explicit ensemble, Wilson coefficients, \(b\to\infty\) limit.

## Bottom line

Linearised Euclidean graviton **pattern** is under control.  
**Nonlinear continuum Einstein IR is not proved.**
