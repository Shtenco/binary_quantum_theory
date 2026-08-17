# TT propagator first pass: exact reduced causal transfer

Status: **exact for the already-frozen reduced two-polarization causal transfer; not yet the final physical Peter--Weyl/history/RG propagator**.

## 1. Frozen transfer relation

`bcqg_unified_verification.py` uses

\[
\widehat k^2=\sum_i\left(2\sin\frac{k_i}{2}\right)^2,
\qquad
\lambda=r^2\widehat k^2,
\qquad
r=\frac1{\sqrt3},
\]

with symplectic one-step transfer matrix satisfying

\[
\cos\omega=1-\frac\lambda2.
\]

Therefore the pole equation is exactly

\[
\boxed{
4\sin^2\frac\omega2
=r^2\sum_i4\sin^2\frac{k_i}{2}.
}
\]

For the two reduced physical TT polarizations the free connected propagator is consequently fixed, up to the common residue/action normalization `Z_T`, by

\[
\boxed{
G^{TT}_{AB}(\omega,\mathbf k)
=\frac{\delta_{AB}}
{Z_T\left[
4\sin^2(\omega/2)
-r^2\sum_i4\sin^2(k_i/2)
+i0
\right]}.
}
\]

This is the first explicit connected `G_TT` object in the physicalization pass.  Its limitation is equally important: it belongs to the reduced causal TT transfer, not yet to the full constrained Peter--Weyl/history measure.

## 2. Exact quartic expansion

Expand

\[
4\sin^2(x/2)=x^2-\frac{x^4}{12}+O(x^6).
\]

Solving the pole equation gives

\[
\boxed{
\omega^2
=r^2k^2
+\frac{r^2}{12}
\left[r^2(k^2)^2-\sum_i k_i^4\right]
+O(k^6).
}
\]

For a unit direction `n_i=k_i/|k|`, write

\[
\omega^2=r^2k^2[1+\eta(\hat n)k^2+O(k^4)].
\]

Then

\[
\boxed{
\eta(\hat n)=\frac{r^2-\sum_i n_i^4}{12}.
}
\]

At the frozen `r^2=1/3`:

| direction | `sum n_i^4` | bare directional eta |
|---|---:|---:|
| axial `(1,0,0)` | 1 | `-1/18 = -0.0555555556` |
| face diagonal `(1,1,0)/sqrt(2)` | 1/2 | `-1/72 = -0.0138888889` |
| body diagonal `(1,1,1)/sqrt(3)` | 1/3 | `0` |

The executable numerical pole fit reproduces the analytic coefficients with maximum absolute error below

\[
\boxed{7.8\times10^{-10}}.
\]

## 3. Scalar versus cubic-lattice quartic invariant

In three spatial dimensions

\[
\left\langle\sum_i n_i^4\right\rangle_{S^2}=\frac35.
\]

Define

\[
Q_4^{cub}
=\sum_i k_i^4-\frac35(k^2)^2.
\]

Then

\[
\boxed{
\omega^2
=r^2k^2
+r^2\eta_{2,bare}^{iso}k^4
+r^2\zeta_{4,bare}Q_4^{cub}
+O(k^6)
}
\]

with

\[
\boxed{
\eta_{2,bare}^{iso}
=\frac{r^2-3/5}{12}
=-\frac1{45}
=-0.0222222222,
}
\]

and

\[
\boxed{
\zeta_{4,bare}=-\frac1{12}.
}
\]

This distinction is mandatory.  Treating a one-dimensional sine expansion `-1/12` as the final isotropic `eta_2` would be wrong.

## 4. Relation to the physicalization scale map

If the scalar coefficient `-1/45` survived the full constrained RG flow unchanged, the LVK-style scalar modified-dispersion coefficient would obey

\[
A_4E_P^2
=8\pi\lambda_R^{eff}\eta_2
=-\frac{8\pi}{45}\lambda_R^{eff}.
\]

Numerically,

\[
\boxed{
A_4E_P^2/\lambda_R^{eff}
=-0.5585053606.
}
\]

This is **not yet a physical prediction** because neither condition required for that promotion is closed:

1. `lambda_R_eff` still contains the one unresolved microscopic overall phase/action slope;
2. the bare scalar/cubic quartic coefficients have not yet been propagated through the same full Peter--Weyl/history/RG construction.

## 5. Independent Regge residue result obtained in the same pass

The full Regge edge Hessian, restricted through the existing edge-to-metric map and fit to the Fierz--Pauli tensor basis, has an extensive first coefficient `c1(L)`.  Dividing by the four-volume gives

\[
Z_L=c_1(L)/L^4.
\]

The sequence

```text
L=3  0.10211317
L=4  0.11146245
L=5  0.11613070
```

was used to preregister the independent `L=6` continuation with the fixed continuum target `1/8`.  The held-out result is documented in `TT_REGGE_ZT_L6_RESULT.md`:

\[
Z_6^{pred}=0.118769231939,
\qquad
Z_6^{obs}=0.118760754612,
\]

relative error `0.00714%`.

Thus the Regge branch supports

\[
\boxed{Z_{TT}^{(\sum A\delta)}\to1/8}.
\]

Consequently, after the common microscopic coefficient is fixed,

\[
\boxed{Z_T^{eff}\propto\lambda_R^{eff}/8}.
\]

The residue is therefore not evidence for a second arbitrary gravitational constant; it tracks the same remaining overall action normalization.

## 6. What is now actually open

The physicalization bottleneck has narrowed to two coupled calculations:

```text
P0: fix/derive the one remaining overall microscopic phase slope
P2: replace the reduced propagator by the full constrained Peter-Weyl/history/RG G_TT
```

The full propagator calculation must simultaneously fit

\[
Z_T,
\quad c_{TT},
\quad \eta_2^{iso},
\quad \zeta_4^{cub},
\]

and test whether

\[
\zeta_4^{cub}\to0
\]

in the physical IR.  If it does not, the first external prediction is anisotropic Lorentz violation rather than the scalar `alpha=4` LVK parameter alone.

## Reproduction

```bash
python scripts/tt_propagator_first_pass.py
```

## Scientific boundary

This file upgrades the project from a vague request for a propagator to an explicit exact reduced propagator plus a concrete quartic decomposition.  It does **not** claim that `eta_2=-1/45` is already a law of nature.  That promotion is allowed only after the same frozen microscopic theory fixes the common action normalization and carries the pole through the full constrained/RG construction.
