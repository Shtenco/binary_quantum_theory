# Held-out L=9,10 preregistration

**Frozen before computing L=9 or L=10.**

Purpose: turn the observed approximately quadratic Regge -> GR convergence into a genuine held-out falsification test.

## Calibration data

Only the already-published `L=5,6,7,8` values are used.  For each positive defect `e(L)` we fit

\[
\boxed{e(L)=\frac{C}{L^2}+\frac{D}{L^4}}
\]

with zero continuum intercept.  No `L=9` or `L=10` value is used in the fit.

The four preregistered observables are:

1. cubic Ward defect `W3`;
2. quadratic normalization defect `e2=0.5-c2_Regge/c2_EH`;
3. cubic normalization defect `e3=0.5-c3_Regge/c3_EH`;
4. nonlinear ratio defect `enl=|(c3/c2)_R/(c3/c2)_EH-1|`.

## Frozen coefficients

| observable | C | D |
|:--|--:|--:|
| `W3` | 0.7172801505768301 | 3.5911920401322224 |
| `e2` | 1.269539999333847 | -2.938287751390221 |
| `e3` | 3.6666004056415966 | -11.512212617371636 |
| `enl` | 4.8311171464184754 | -7.651431498697587 |

## Frozen predictions

### L=9

\[
\boxed{W_3=0.00940266487}
\]

\[
\boxed{c_2^{R}/c_2^{EH}=0.48477450812}
\]

\[
\boxed{c_3^{R}/c_3^{EH}=0.45648797131}
\]

\[
\boxed{e_{nl}=0.05847722258}
\]

### L=10

\[
\boxed{W_3=0.00753192071}
\]

\[
\boxed{c_2^{R}/c_2^{EH}=0.48759842878}
\]

\[
\boxed{c_3^{R}/c_3^{EH}=0.46448521721}
\]

\[
\boxed{e_{nl}=0.04754602831}
\]

## Falsification rule

For each defect separately define

\[
r=\frac{|e_{obs}-e_{pred}|}{e_{pred}}.
\]

- `PASS`: `r <= 5%`;
- `TENSION`: `5% < r <= 10%`;
- `FAIL`: `r > 10%`.

The joint quadratic-universality prediction is called a strong PASS only if **all four observables at both held-out sizes** are within 5%.  No coefficient, amplitude window, seed, continuum grid or fit formula may be changed after inspecting held-out values.

This test concerns only the fixed-4D Regge cross-validation branch.  Passing it does not close microscopic geometrogenesis or Lorentzian quantum dynamics.
