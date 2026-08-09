# Held-out L=9,10 results

These values were computed **after** `HELDOUT_L9_L10_PREREGISTRATION.md` was committed at `4365df626bc8109a254a2ecc4bfe0f55f8c5f3a0`.

The frozen calibration model was

\[
e(L)=C/L^2+D/L^4
\]

fitted only on `L=5,6,7,8`.  `PASS` was preregistered as relative prediction error of each positive defect <= 5%.

## L=9

| observable | preregistered | observed | relative error of defect |
|:--|--:|--:|--:|
| `W3` | 0.009402664874 | 0.009430902016 | 0.3003% |
| `c2_Regge/c2_EH` | 0.4847745081 | 0.4847612143 | 0.08731% |
| `c3_Regge/c3_EH` | 0.4564879713 | 0.4564191036 | 0.1583% |
| nonlinear ratio defect | 0.05847722258 | 0.05846612710 | 0.01897% |

## L=10

| observable | preregistered | observed | relative error of defect |
|:--|--:|--:|--:|
| `W3` | 0.007531920710 | 0.007562453915 | 0.4054% |
| `c2_Regge/c2_EH` | 0.4875984288 | 0.4875833623 | 0.1215% |
| `c3_Regge/c3_EH` | 0.4644852172 | 0.4644071947 | 0.2197% |
| nonlinear ratio defect | 0.04754602831 | 0.04753272855 | 0.02797% |

All **8/8** preregistered held-out observables are inside the 5% PASS band.  In fact every relative defect-prediction error is below 0.5%.

## Direct L^2 coefficient check

For a true leading `1/L^2` correction, `C_eff(L)=L^2 e(L)` should approach a constant.  Including the held-out sizes:

| L | `L^2 W3` | `L^2 e2` | `L^2 e3` | `L^2 enl` |
|--:|--:|--:|--:|--:|
| 5 | 0.86112 | 1.15210 | 3.20658 | 4.52500 |
| 6 | 0.81621 | 1.18753 | 3.34487 | 4.61880 |
| 7 | 0.79064 | 1.20961 | 3.43176 | 4.67509 |
| 8 | 0.77460 | 1.22419 | 3.48966 | 4.71104 |
| 9 | 0.76390 | 1.23434 | 3.53005 | 4.73576 |
| 10 | 0.75625 | 1.24166 | 3.55928 | 4.75327 |

The held-out points continue the smooth approach to constant coefficients rather than merely continuing monotonic convergence.

Power fits over the enlarged `L=5..10` window give

\[
p_{W3}=2.1841,
\qquad
p_{e2}=1.8936,
\qquad
p_{e3}=1.8517,
\qquad
p_{enl}=1.9303.
\]

The residual drift is consistent with the preregistered `D/L^4` subleading term.

## Scientific interpretation

This is the first genuinely held-out numerical validation of the Regge continuum-scaling law in the repository.  It strengthens the statement that several independent fixed-scaffold gravity defects share a leading approximately `O(a^2)` irrelevant correction.

It still does **not** test the upstream microscopic quantum-link geometrogenesis, Lorentzian constraint closure, matter, or experiment.
