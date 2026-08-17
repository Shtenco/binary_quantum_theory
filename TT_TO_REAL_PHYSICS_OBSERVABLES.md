# From microscopic TT Wilson coefficients to real observables

Status: **algebraically closed observable bridge; numerical prediction waits only for frozen `eta2_IR`, `zeta4_IR` and the one declared absolute scale calibration.**

This note turns the dimensionless infrared TT coefficients into quantities an experiment can constrain.  It does not insert an experimental number into the microscopic calculation.

---

## 1. Frozen infrared TT pole

After the microscopic six-edge kernel has been projected through the exact shape-to-metric Jacobian and the TT projector, write the low-energy pole as

\[
\omega^2
= c^2 k^2\left[
1+a_*^2 k^2 F(\hat n)+O(a_*^4k^4)
\right],
\]

where

\[
\boxed{
F(\hat n)
=\eta_2^{IR}
+\zeta_4^{IR}Q_4^{cub}(\hat n)
}
\]

and

\[
Q_4^{cub}(\hat n)
=\sum_{i=1}^{3}n_i^4-\frac35.
\]

The normalization is the one frozen in `C6_TO_TT_WILSON_COEFFICIENTS.md`.

For the three diagnostic directions,

\[
Q_{100}=\frac25,\qquad
Q_{110}=-\frac1{10},\qquad
Q_{111}=-\frac4{15}.
\]

Thus the directional coefficients are

\[
e_{100}=\eta_2+\frac25\zeta_4,
\]
\[
e_{110}=\eta_2-\frac1{10}\zeta_4,
\]
\[
e_{111}=\eta_2-\frac4{15}\zeta_4.
\]

The exact consistency relation is

\[
\boxed{e_{100}-4e_{110}+3e_{111}=0.}
\]

---

## 2. Phase and group velocity

For `a_* k << 1`, choose the positive-frequency branch:

\[
\omega
=ck\left[1+\frac12a_*^2k^2F(\hat n)+O(a_*^4k^4)\right].
\]

Therefore

\[
\boxed{
\frac{v_g-c}{c}
=\frac32a_*^2k^2F(\hat n)
+O(a_*^4k^4).
}
\]

At fixed angular frequency, inversion gives

\[
k(\omega)
=\frac{\omega}{c}
\left[1-\frac12a_*^2\left(\frac\omega c\right)^2F(\hat n)+\cdots\right].
\]

A wave propagating a physical distance `L` therefore accumulates the beyond-GR phase

\[
\boxed{
\delta\phi(\omega,\hat n)
=-\frac12La_*^2\left(\frac\omega c\right)^3F(\hat n)
+O(a_*^4\omega^5L/c^5).
}
\]

and the leading flight-time shift is

\[
\boxed{
\delta t
\simeq
-\frac32\frac{L}{c}a_*^2k^2F(\hat n).
}
\]

These formulas are observables after a convention for what reference signal is being compared is declared.  They should not be interpreted as a photon-vs-graviton delay unless the photon sector is independently shown to have the standard reference dispersion.

---

## 3. Insert the one-scale map

The repository scale map is

\[
\lambda_R^{eff}=\frac{a_*^2}{8\pi\ell_P^2},
\qquad
a_*^2=8\pi\lambda_R^{eff}\ell_P^2.
\]

With

\[
E_P=\frac{\hbar c}{\ell_P},
\qquad E=\hbar\omega,
\]

we obtain

\[
\boxed{
\frac{v_g-c}{c}
=12\pi\lambda_R^{eff}
F(\hat n)
\left(\frac{E}{E_P}\right)^2
+O(E^4/E_P^4).
}
\]

The propagation phase becomes

\[
\boxed{
\delta\phi
=-4\pi\lambda_R^{eff}
F(\hat n)
\frac{L}{\ell_P}
\left(\frac{E}{E_P}\right)^3
+O(E^5/E_P^5).
}
\]

and

\[
\boxed{
\delta t
=-12\pi\lambda_R^{eff}
F(\hat n)
\frac{L}{c}
\left(\frac{E}{E_P}\right)^2
+O(E^4/E_P^4).
}
\]

This exhibits the separation cleanly:

```text
microscopic dynamics -> eta2_IR, zeta4_IR       dimensionless, blind
one scale datum      -> lambda_R_eff or a_*/lP absolute normalization
experiment           -> phase / group delay / directional modulation
```

No second phenomenological fit is required.

---

## 4. Pure anisotropy observable that cancels the scalar coefficient

Take two propagation directions at the same frequency.  The isotropic `eta2` term cancels:

\[
\delta\phi(\hat n_1)-\delta\phi(\hat n_2)
=-\frac12La_*^2\left(\frac\omega c\right)^3
\zeta_4^{IR}
\left[Q_4(\hat n_1)-Q_4(\hat n_2)\right].
\]

In particular,

\[
Q_{100}-Q_{110}=\frac12,
\]

so

\[
\boxed{
\delta\phi_{100}-\delta\phi_{110}
=-\frac14La_*^2\left(\frac\omega c\right)^3\zeta_4^{IR}.
}
\]

Likewise

\[
Q_{110}-Q_{111}=\frac16,
\]

which supplies an independent ratio check.

This is the cleanest external target for a nonzero cubic/tetrahedral fixed point because it removes the scalar quartic correction at leading order.

---

## 5. Five-channel optical readout of the same traceless metric sector

The independent finite optical bridge gives, for five balanced channels,

\[
\Delta\Phi=\kappa R x,
\qquad
\kappa=\frac{k_\gamma\ell_*}{2},
\]

where `x` are the five orthonormal traceless metric coordinates and `R` is nonsingular on that five-dimensional sector.  Its exact singular-value spectrum is already derived in `BCQG_PHOTON_INTERFERENCE_BRIDGE.md` on the collective branch.

Therefore a TT two-point function/covariance `S_h` maps to an optical phase covariance by

\[
\boxed{
S_{\Phi}(\omega)
=\kappa^2 R\,S_h(\omega)\,R^T.
}
\]

Conversely,

\[
\boxed{
S_h(\omega)
=\kappa^{-2}R^{-1}S_{\Phi}(\omega)R^{-T}
}
\]

within the linear traceless sector.

Once the absolute TT residue and state prescription are fixed, the retarded kernel

\[
G^R_{TT}(\omega,\mathbf k)=K_{TT}^{-1}(\omega,\mathbf k)
\]

can be converted into the appropriate state-dependent symmetrized spectrum.  That final statistical step must state the vacuum/thermal/non-equilibrium state; the retarded pole alone does not determine a unique noise amplitude.

---

## 6. What is and is not calibrated

HDA fixes the GR tensor structure and relative kinetic/curvature normalization but leaves the familiar common gravitational normalization.  The microscopic composition law reduces that freedom to one overall action slope.

Accordingly the honest protocol is:

1. freeze `eta2_IR` and `zeta4_IR` from the microscopic theory;
2. freeze regulator sequence, momentum extraction and uncertainty;
3. use **one** declared absolute datum to set `lambda_R_eff` / `a_*` if it is not derived internally;
4. predict every other frequency, distance and direction dependence without retuning;
5. compare blind.

The anisotropy ratios and the three-direction consistency relation are dimensionless and do not require the absolute scale calibration.

---

## 7. Failure conditions

The physicalization gate fails if any of the following occurs:

- the microscopic `C6(omega,k)` has no stable low-momentum expansion;
- the TT pole is ghostlike/tachyonic;
- `eta2` or `zeta4` depends on arbitrary regulator choices after the declared extrapolation;
- the three-direction consistency relation fails beyond estimated higher-order/finite-size errors;
- the scale requires more than the one declared common normalization freedom;
- an external comparison is used to retune the already-frozen dimensionless coefficients.

This makes the bridge falsifiable rather than numerological.
