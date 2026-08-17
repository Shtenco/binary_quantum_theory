# From microscopic TT Wilson coefficients to real observables

Status: **algebraically closed observable bridge.**  The generic parity-even tetrahedral quartic prediction is a six-dimensional TT Wilson vector.  The familiar `eta2/zeta4` and single-`Q_tet` formulas below are retained as exact nested submodels, not assumed as the most general answer.

No experimental number is inserted into the microscopic calculation.

---

## 1. General frozen infrared TT poles

After the full interblock kernel has been projected through the metric and TT bridges, the two physical pole branches are written

\[
\boxed{
\omega_\sigma^2
=c^2k^2\left[
1+a_*^2k^2e_{4,\sigma}(\hat n)
+O(a_*^4k^4)
\right],
\qquad \sigma=1,2.
}
\]

The pair of real functions

\[
\boxed{
\mathcal E_4(\hat n)
=\{e_{4,1}(\hat n),e_{4,2}(\hat n)\}
}
\]

is the direct physical quartic prediction.

`S4_TT_QUARTIC_COMPLETE_BASIS.md` proves that, for the stated parity-even spatial tetrahedral symmetry, the complete TT quartic response is determined by six dimensionless Wilson coefficients

\[
\boxed{
\mathbf c=(c_1,c_2,c_3,c_4,c_5,c_6).
}
\]

A frozen six-vector therefore predicts the complete sky-direction and polarization dependence of `mathcal E_4(n)` with no further tensor fit.

---

## 2. Phase velocity, group velocity and propagation phase

For `a_*k << 1`,

\[
\omega_\sigma
=ck\left[
1+\frac12a_*^2k^2e_{4,\sigma}(\hat n)
+O(a_*^4k^4)
\right].
\]

Hence

\[
\boxed{
\frac{v_{g,\sigma}-c}{c}
=\frac32a_*^2k^2e_{4,\sigma}(\hat n)
+O(a_*^4k^4).
}
\]

At fixed angular frequency,

\[
k_\sigma(\omega)
=\frac\omega c\left[
1-\frac12a_*^2\left(\frac\omega c\right)^2e_{4,\sigma}(\hat n)
+\cdots
\right],
\]

so a baseline `L` gives

\[
\boxed{
\delta\phi_\sigma
=-\frac12La_*^2\left(\frac\omega c\right)^3e_{4,\sigma}(\hat n)
+O(a_*^4\omega^5L/c^5).
}
\]

and, relative to the leading Einstein light cone,

\[
\boxed{
\delta t_\sigma
\simeq
-\frac32\frac{L}{c}a_*^2k^2e_{4,\sigma}(\hat n).
}
\]

A photon-vs-graviton interpretation requires the photon reference dispersion to be independently fixed.  The equations themselves are intrinsic gravitational propagation observables.

---

## 3. One absolute scale map

The repository scale bridge is

\[
\lambda_R^{eff}=\frac{a_*^2}{8\pi\ell_P^2},
\qquad
a_*^2=8\pi\lambda_R^{eff}\ell_P^2.
\]

Using

\[
E=\hbar\omega,
\qquad
E_P=\frac{\hbar c}{\ell_P},
\]

we obtain for each polarization branch

\[
\boxed{
\frac{v_{g,\sigma}-c}{c}
=12\pi\lambda_R^{eff}
e_{4,\sigma}(\hat n)
\left(\frac E{E_P}\right)^2
+O(E^4/E_P^4),
}
\]

\[
\boxed{
\delta\phi_\sigma
=-4\pi\lambda_R^{eff}
e_{4,\sigma}(\hat n)
\frac L{\ell_P}
\left(\frac E{E_P}\right)^3
+O(E^5/E_P^5),
}
\]

\[
\boxed{
\delta t_\sigma
=-12\pi\lambda_R^{eff}
e_{4,\sigma}(\hat n)
\frac Lc
\left(\frac E{E_P}\right)^2
+O(E^4/E_P^4).
}
\]

Thus the data flow is

```text
microscopic dynamics -> c1...c6                    dimensionless, blind
one common scale      -> lambda_R_eff or a_*/lP    absolute normalization
algebra               -> e4_1(n), e4_2(n)
experiment            -> phase, delay, sky pattern, polarization splitting
```

No second phenomenological scale fit is required.

---

## 4. Polarization-average and birefringent observables

Define

\[
\bar e_4(\hat n)
=\frac12[e_{4,1}(\hat n)+e_{4,2}(\hat n)],
\]

\[
\Delta e_4(\hat n)
=e_{4,1}(\hat n)-e_{4,2}(\hat n).
\]

Then

\[
\boxed{
\frac{\bar v_g-c}{c}
=\frac32a_*^2k^2\bar e_4(\hat n),
}
\]

while the polarization group-velocity splitting is

\[
\boxed{
\frac{v_{g,1}-v_{g,2}}{c}
=\frac32a_*^2k^2\Delta e_4(\hat n).
}
\]

The accumulated polarization phase difference is

\[
\boxed{
\Delta\phi_{pol}
=-\frac12La_*^2\left(\frac\omega c\right)^3\Delta e_4(\hat n).
}
\]

These are basis-independent because they are functions of the two TT eigenvalues.

---

## 5. Nested eta2/zeta4 scalar model

If and only if the complete six-coefficient result passes the restricted scalar-cubic hypothesis,

\[
\boxed{
\bar e_4(\hat n)
=\eta_2+\zeta_4Q_4^{cub}(\hat n),
}
\]

with

\[
Q_4^{cub}=\sum_i n_i^4-\frac35,
\]

then the compact two-number description is valid.

For `(100),(110),(111)`:

\[
Q=\left(\frac25,-\frac1{10},-\frac4{15}\right),
\]

and

\[
\zeta_4=2(e_{100}-e_{110}),
\qquad
\eta_2=\frac15e_{100}+\frac45e_{110},
\]

with held-out relation

\[
\boxed{e_{100}-4e_{110}+3e_{111}=0.}
\]

The general six-coefficient result is **not required** to obey this identity unless it lies in that nested subspace.

---

## 6. Nested single-Qtet birefringence model

If the anisotropic quartic tensor is dominated by the single spin-2 splitter

\[
Q_{tet}=\frac35P_E-\frac25P_{T_2},
\]

then `TETRAHEDRAL_TT_BIREFRINGENCE_THEOREM.md` gives

\[
\zeta_4=\gamma_4/4
\]

for the polarization average and the parameter-free splitting pattern

\[
\boxed{
\Delta e_{100}:\Delta e_{110}:\Delta e_{111}=4:3:0.
}
\]

This is a strong blind nested test.  A future microscopic result that violates it has not “failed tetrahedral physics”; it has shown that more than one of the six allowed quartic TT Wilson structures is active.

---

## 7. Angular fingerprint of the scalar cubic nested model

The scalar cubic harmonic has the exact complex spherical-harmonic decomposition

\[
\boxed{
Q_4^{cub}(\hat n)
=\frac{4\sqrt\pi}{15}
\left[
Y_{40}(\hat n)
+\sqrt{\frac5{14}}
\left(Y_{44}(\hat n)+Y_{4,-4}(\hat n)\right)
\right]
}
\]

in the intrinsic microscopic frame.

Therefore the nested scalar-cubic model is a pure `l=4` sky pattern with a fixed `m=0` versus `m=±4` ratio.  An arbitrary rotation to the astronomical frame changes only the Euler orientation of the multiplet, not its internal harmonic ratios.

This gives a zero-fit angular fingerprint once the microscopic frame/transport is defined globally.

---

## 8. Mapping to the common modified-dispersion notation

For either TT pole branch, multiply

\[
\omega_\sigma^2
=c^2k^2+c^2a_*^2k^4e_{4,\sigma}
\]

by `hbar^2` and use `p=hbar k`, `E=hbar omega`:

\[
\boxed{
E^2
=(pc)^2+A_{4,\sigma}(\hat n)(pc)^4+\cdots,
}
\]

where

\[
\boxed{
A_{4,\sigma}(\hat n)
=\frac{a_*^2}{(\hbar c)^2}
e_{4,\sigma}(\hat n)
=\frac{8\pi\lambda_R^{eff}}{E_P^2}
e_{4,\sigma}(\hat n).
}
\]

Thus the candidate theory lands directly in the `alpha=4` / quartic modified-dispersion observational class once its microscopic six-vector and one absolute scale are frozen.

The anisotropic/polarization-resolved prediction is stronger than an isotropic `A4`: it supplies a correlated sky and polarization pattern rather than one free coefficient per event.

---

## 9. Five-channel optical readout of the same traceless metric sector

The independent collective optical bridge gives

\[
\Delta\Phi=\kappa R x,
\qquad
\kappa=\frac{k_\gamma\ell_*}{2},
\]

for five balanced phase channels and five traceless metric coordinates.

The response is invertible on that sector, and its exact finite-condition-number sensitivity spectrum is derived in `BCQG_PHOTON_INTERFERENCE_BRIDGE.md` on the collective branch.

For a metric covariance/spectrum `S_h`,

\[
\boxed{
S_\Phi(\omega)
=\kappa^2RS_h(\omega)R^T,
}
\]

\[
\boxed{
S_h(\omega)
=\kappa^{-2}R^{-1}S_\Phi(\omega)R^{-T}.
}
\]

The retarded TT kernel determines poles/response; a unique noise spectrum additionally requires a declared quantum/statistical state.  The bridge does not confuse those two objects.

---

## 10. Calibration and anti-overfitting protocol

The correct order is now:

1. freeze the microscopic commit, ordering, regulator and block prescription;
2. compute onsite and interblock dynamics;
3. verify the leading Einstein/HDA cone and absence of anisotropy at derivative order `<=2`;
4. extract all six quartic TT Wilson coefficients using the frozen full-rank protocol;
5. freeze their uncertainties and continuum/blocking extrapolation;
6. test the `eta/zeta` and single-`Q_tet` nested hypotheses **without changing the six-vector**;
7. derive or calibrate the single common absolute scale `lambda_R_eff`;
8. convert to `A4`, group delay, phase and polarization patterns;
9. only then open the chosen external posterior / dataset.

If a nested hypothesis fails, the six-coefficient prediction is reported rather than retuned into the simpler model.

---

## 11. Failure conditions

The physicalization branch fails if:

- no stable low-momentum TT expansion emerges;
- a mass, ghost, tachyon, negative kinetic residue, or non-Einstein leading `k^2` cone survives;
- quartic coefficients remain materially regulator/blocking dependent after the frozen extrapolation;
- the six-observable extraction is internally inconsistent;
- more than the one already-known common absolute normalization must be fitted;
- external data are used to modify a previously frozen microscopic Wilson vector.

A failure of the two-parameter `eta/zeta` nested model alone is **not** a failure of the full theory; it simply means the more general six-coefficient tetrahedral prediction is active.
