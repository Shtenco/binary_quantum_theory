# Observer-scale smoothing of binary Planck spacetime

Checks: **16/16**

$$\ell_{obs}=\sqrt{\ell_P^2+(\theta r)^2},\qquad b=2^{\lfloor\log_2(\ell_{obs}/\ell_P)\rfloor}.$$

This is an observer-resolution map, not a claim that distance itself dynamically changes spacetime.

## Measured finite scaling

- metric noise exponent: **1.995138**
- gradient roughness exponent: **2.992908**
- linear curvature-noise exponent: **3.957407**
- simplicity exponent: **1.973708**
- Urbantke metric-error exponent: **2.052015**
- visible dispersion-error exponent: **1.920692**
- far conditional 4D spectral dimension: **4.00187656**
- dimension-blind binary diamond spectral dimension: **2.06975151**

## Interpretation

In a 4D block, $N=b^4$ independent zero-mean bits give RMS fluctuations $N^{-1/2}=b^{-2}$. Physical derivatives add inverse block lengths, giving the observed $b^{-3}$ gradient and $b^{-4}$ linear-curvature laws. The separate dimension-blind null remains near 2D, so this is a continuumisation mechanism, not a derivation of 3+1 dimensions.

| check | value | target | status |
|---|---:|---|---|
| metric noise exponent | `1.995137671661402` | 2 +/- .15 | PASS |
| gradient roughness exponent | `2.992907594471482` | 3 +/- .20 | PASS |
| curvature noise exponent | `3.957407067304873` | 4 +/- .35 | PASS |
| far/near SNR gain | `49.66873860754732` | >20 | PASS |
| dispersion error exponent | `1.920692422271939` | ~2 | PASS |
| far dispersion mean error | `0.0003199521303427612` | <5e-4 | PASS |
| far z | `0.9998470951176417` | 1 +/- .01 | PASS |
| far conditional spectral dimension | `4.001876560449994` | 4 +/- .02 | PASS |
| spectral UV correction decreases | `0.0018765604499941801` | < block1 error | PASS |
| binary diamond fails 4D | `2.0084122398161997` | null fail | PASS |
| binary diamond near 2D | `2.0697515090185665` | 1.8..2.3 | PASS |
| simplicity smoothing exponent | `1.9737078127751904` | ~2 | PASS |
| Urbantke smoothing exponent | `2.0520148892745613` | ~2 | PASS |
| far simplicity | `0.009397290792127939` | <.02 | PASS |
| far Urbantke error | `0.011154524246036123` | <.02 | PASS |
| Lorentzian beta cancellation | `1.9012454751867332e-12` | <2e-11 | PASS |

## Scope

The positive result is conditional: on a 4D effective scaffold, unresolved binary Planck-scale fluctuations self-average into a smooth observer-accessible IR sector. It does **not** derive four dimensions from the microscopic rule and it does **not** close the full graph-changing quantum HDA gate. The dimension-blind binary reconvergence control remains approximately two-dimensional and is preserved as a negative control.