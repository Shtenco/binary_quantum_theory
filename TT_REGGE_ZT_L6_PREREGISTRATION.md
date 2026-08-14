# Preregistration: intensive Regge TT normalization at L=6

Status: **frozen before computing the L=6 axial Hessian in the current physicalization pass**.

## Quantity

Use the existing `FlatRegge4D` Hessian and `gravity_bridge_scaling.py` edge-to-metric/Fierz--Pauli fit conventions.

For the lowest axial momentum

\[
k=(2\pi/L,0,0,0),
\]

let `c1(L)` be the first fitted Fierz--Pauli coefficient in

\[
H_{10}(k)=c_1 T_1+c_2 T_2+c_3 T_3+c_4 T_4+\text{residual}.
\]

Because the full periodic action is extensive, define the intensive coefficient

\[
\boxed{Z_L=c_1(L)/L^4}. 
\]

The already-open values from L=3,4,5 are

```text
L=3  Z_L = 0.10211317451806736
L=4  Z_L = 0.11146245302029784
L=5  Z_L = 0.11613069959122077
```

## Independent continuum target

`REGGE_EH_CUBIC_BRIDGE.md` independently fixes the smooth geometric normalization

\[
\sum_h A_h\delta_h \to \frac12\int\sqrt g R.
\]

With the repository TT Hessian/Fierz--Pauli conventions this gives the intensive target

\[
\boxed{Z_\infty=1/8=0.125}.
\]

This target is not fitted to the three values above.

## Frozen finite-size model

Fit only the two correction coefficients in

\[
\boxed{Z_L=\frac18+\frac{C}{L^2}+\frac{D}{L^4}}
\]

by least squares on L=3,4,5.

Frozen coefficients:

```text
C = -0.23041866
D = +0.21999650
```

Frozen held-out prediction:

\[
\boxed{Z_6^{pred}=0.11876923193907167}.
\]

## Acceptance rule

Define

\[
r_6=|Z_6^{obs}-Z_6^{pred}|/Z_6^{pred}.
\]

- PASS: `r6 <= 1%`
- TENSION: `1% < r6 <= 3%`
- FAIL: `r6 > 3%`

No fit coefficient or continuum target may be changed after the L=6 value is computed.

## Scope

This tests only the fixed-Regge intensive TT normalization and its finite-size correction. It does not determine the microscopic overall phase slope or `lambda_R_eff`; if the continuum result survives, the physical TT residue is proportional to `lambda_R_eff/8`, with the remaining common normalization still requiring microscopic derivation or one declared scale-setting datum.
