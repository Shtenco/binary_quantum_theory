# Held-out result: intensive Regge TT normalization at L=6

This value was computed **after** `TT_REGGE_ZT_L6_PREREGISTRATION.md` was committed at `00220ae7fad55e572aed20109d1306a3c3c5b908`.

The frozen prediction was

\[
Z_6^{pred}=0.11876923193907167
\]

for

\[
Z_L=c_1(L)/L^4,
\qquad
Z_L=\frac18+\frac{C}{L^2}+\frac{D}{L^4}.
\]

The held-out direct metric-Hessian calculation gives

\[
\boxed{Z_6^{obs}=0.11876075461190198}.
\]

Therefore

\[
\boxed{
\frac{|Z_6^{obs}-Z_6^{pred}|}{Z_6^{pred}}
=7.13765\times10^{-5}
=0.00714\%.
}
\]

The preregistered PASS threshold was `1%`, so this is a strong **PASS**.

The same L=6 fit gives

```text
Fierz-Pauli ratios = (1, -1.9885082262, 1.9540514832, -0.9741541752)
full FP matrix residual = 0.02611716074
```

The intensive sequence is now

| L | c1/L^4 |
|--:|--:|
| 3 | 0.1021131745 |
| 4 | 0.1114624530 |
| 5 | 0.1161306996 |
| 6 | 0.1187607546 |
| continuum target | 0.125 = 1/8 |

## Interpretation

This resolves the old extensive-normalization confusion much more cleanly than raw field-norm numbers of order 20--30.  In the declared Regge convention, the unit geometric action

\[
S_R=\sum_h A_h\delta_h
\]

has an intensive TT/Fierz--Pauli coefficient approaching

\[
\boxed{Z_{TT}^{(R)}=1/8}.
\]

If the renormalized microscopic effective action contains

\[
(S_{eff}/\hbar)\supset
\lambda_R^{eff}\sum_h\widetilde A_h\delta_h,
\]

then the corresponding dimensionless TT residue normalization is proportional to

\[
\boxed{Z_T^{eff}=\lambda_R^{eff}/8}
\]

up to the common Lorentzian/time-field convention fixed by the final physical propagator.

This does **not** determine `lambda_R_eff`; it instead proves that `Z_T` is not a second unrelated free constant once the common microscopic action normalization is fixed.

## Computation note

The held-out result used the same edge-to-metric and Fierz--Pauli conventions as `gravity_bridge_scaling.py`, but evaluated the projected 20-dimensional metric Hessian directly rather than first constructing the full 30-dimensional edge Hessian. Algebraically this computes the same `A^T H A` object while avoiding ten unused edge-space directions.
