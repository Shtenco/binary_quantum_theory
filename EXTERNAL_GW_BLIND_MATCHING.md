# Blind matching to real gravitational-wave propagation tests

Status: **observable dictionary fixed before the microscopic IR Wilson vector is known.  No external posterior is used as a calibration of the dimensionless coefficients.**

The purpose of this document is to define how the future frozen BCQG TT prediction is compared with existing gravitational-wave propagation analyses.

Primary observational languages already exist:

- generic modified-dispersion tests used by LIGO–Virgo–KAGRA;
- anisotropic / birefringent gauge-invariant gravity-sector SME analyses.

Relevant references include:

- T. Baka et al., *Testing general relativity with gravitational waves—improving and extending Modified Dispersion Relation tests*, arXiv:2511.00497 (updated 2026);
- V. A. Kostelecký and M. Mewes, *Testing local Lorentz invariance with gravitational waves*, arXiv:1602.04782;
- M. Mewes, *Signals for Lorentz violation in gravitational waves*, arXiv:1905.00409;
- C. Gong et al., *Gravitational wave constraints on non-birefringent dispersions ... with GWTC-3*, arXiv:2302.05077.

These references are used only to define the external observable basis.  Their posterior values do not enter the microscopic calculation.

---

## 1. Exact modified-dispersion dictionary

The common phenomenological MDR convention is

\[
E^2=(pc)^2+A_\alpha(pc)^\alpha.
\]

BCQG predicts for each TT pole branch

\[
\omega_\sigma^2
=c^2k^2\left[1+a_*^2k^2e_{4,\sigma}(\hat n)+\cdots\right].
\]

Using

\[
E=\hbar\omega,
\qquad p=\hbar k,
\]

we obtain

\[
E^2
=(pc)^2
+\frac{a_*^2}{(\hbar c)^2}
e_{4,\sigma}(\hat n)(pc)^4
+\cdots.
\]

Therefore BCQG lands exactly in the `alpha=4` MDR class:

\[
\boxed{
A_{4,\sigma}(\hat n)
=\frac{a_*^2}{(\hbar c)^2}
e_{4,\sigma}(\hat n).
}
\]

With the repository scale map

\[
a_*^2=8\pi\lambda_R^{eff}\ell_P^2,
\qquad
E_P=\hbar c/\ell_P,
\]

\[
\boxed{
A_{4,\sigma}(\hat n)
=\frac{8\pi\lambda_R^{eff}}{E_P^2}
e_{4,\sigma}(\hat n).
}
\]

The frequency-domain propagation correction therefore has the characteristic `f^3` scaling of the `alpha=4` MDR class.

---

## 2. BCQG predicts correlated A4 values, not one free A4 per event

A generic isotropic MDR analysis samples one common amplitude.

The BCQG prediction is stronger:

\[
\boxed{
A_{4,\sigma}
=A_{4,\sigma}(\hat n;\mathbf c^{IR},\mathcal R_{micro}),
}
\]

where

- `sigma=1,2` labels the two TT poles;
- `n` is the source propagation direction expressed in the microscopic/coarse geometric frame;
- `c_IR=(c1,...,c6)` is the frozen six-Wilson vector;
- `R_micro` denotes at most the global orientation of the microscopic tetrahedral frame relative to the astronomical frame if that orientation is not dynamically averaged away.

Thus many GW events at different sky positions are **not independent theory coefficients**.  They sample one correlated sky pattern.

This sharply reduces overfitting and creates cross-event falsifiers.

---

## 3. Cosmological propagation

For a cosmological source the flat-space baseline `L` is replaced by the standard MDR redshift-weighted propagation integral used by the external analysis.

The microscopic theory supplies `A4_sigma(n)`; the data-analysis convention supplies the cosmological distance functional.

This separation is deliberate:

```text
BCQG:       microscopic coefficient and angular/polarization law
cosmology:  background expansion / redshift integral
likelihood: detector noise + waveform inference
```

Changing the cosmological convention must not change the previously frozen dimensionless Wilson vector.

---

## 4. Anisotropic and birefringent matching

Gauge-invariant Lorentz-violating gravity frameworks already organize propagation signatures into

- dispersion;
- anisotropy;
- birefringence / polarization splitting.

BCQG should therefore be matched in one of two preregistered ways.

### Route A — direct theory waveform

Insert the two predicted functions

\[
A_{4,1}(\hat n),
\qquad
A_{4,2}(\hat n)
\]

directly into a propagation waveform model.

This preserves the exact BCQG six-coefficient correlations and is the preferred route if practical.

### Route B — SME coefficient map

Before opening the target posterior, derive a linear transformation from the six BCQG quartic TT Wilson coefficients to the chosen dimension-6 anisotropic/birefringent SME basis.

Then compare the resulting fixed six-dimensional submanifold with the external coefficient likelihood.

The map itself must be committed before looking at the numerical posterior.

---

## 5. Scalar-cubic nested sky fingerprint

If the full six-vector happens to satisfy the smaller scalar-cubic hypothesis,

\[
\bar e_4(\hat n)
=\eta_2+\zeta_4Q_4^{cub}(\hat n),
\]

then

\[
Q_4^{cub}
=n_x^4+n_y^4+n_z^4-\frac35
\]

has the exact spherical-harmonic form

\[
\boxed{
Q_4^{cub}
=\frac{4\sqrt\pi}{15}
\left[
Y_{40}
+\sqrt{\frac5{14}}(Y_{44}+Y_{4,-4})
\right]
}
\]

in its intrinsic frame.

So this nested model predicts a **pure `l=4` cubic multiplet with fixed internal harmonic ratios**.  Only an overall amplitude and a possible global frame rotation remain; the `m=0` versus `m=±4` ratio is not fitted.

---

## 6. Single-Qtet nested polarization fingerprint

If the full six-vector also lies in the single-`Q_tet` polarization subspace, the TT splitting obeys

\[
\boxed{
\Delta e_{100}:\Delta e_{110}:\Delta e_{111}=4:3:0.
}
\]

This is independent of the absolute scale and of the magnitude of the anisotropic coefficient.

A multi-event birefringence analysis can therefore test not only whether splitting exists, but whether its direction dependence follows this fixed ratio/pattern.

Failure of this nested fingerprint does not justify retuning it; one returns to the already-frozen full six-coefficient prediction.

---

## 7. Absolute scale versus dimensionless shape

The six Wilson coefficients determine the dimensionless angular/polarization shape.

The known single common normalization freedom enters through

\[
\lambda_R^{eff}
\]

or equivalently `a_*/ell_P`.

The allowed protocol is:

1. freeze `c1...c6` and their RG/finite-size uncertainty;
2. derive the common scale internally **or use one declared scale datum**;
3. predict all other events, frequencies, directions and polarization combinations;
4. never use a second event-dependent scale calibration.

The angular ratios, nested-hypothesis residuals and many polarization ratios can be tested without knowing the absolute scale.

---

## 8. Blind PASS / TENSION / FAIL logic

Before the target posterior is opened, commit:

```text
microscopic SHA
six Wilson coefficients + covariance
absolute-scale rule
sky-frame convention / marginalization rule
waveform propagation convention
cosmology convention
external event/catalog selection
likelihood or posterior-reuse method
PASS / TENSION / FAIL thresholds
```

A valid external comparison must preserve the microscopic six-vector.

Possible outcomes:

- **PASS:** correlated BCQG propagation pattern is compatible with the external likelihood within preregistered uncertainty;
- **TENSION:** discrepancy exceeds the declared soft threshold but not the rejection threshold;
- **FAIL:** the frozen prediction is excluded according to the preregistered criterion.

The theory is not repaired after `FAIL` by deleting allowed Wilson structures or refitting the microscopic coefficient to the same data.

---

## 9. What is already closed and what is not

Closed:

\[
\boxed{
\mathbf c^{IR}
\to e_{4,1/2}(\hat n)
\to A_{4,1/2}(\hat n)
\to \text{frequency-dependent GW propagation likelihood}.
}
\]

Still open numerically:

```text
full-E onsite depth-two result
nearest-block transfer amplitudes
refinement/locality extrapolation
actual frozen c1...c6 values
one absolute scale if not derived internally
blind posterior comparison
```

This is the real-physics end of the project: the remaining unknowns are microscopic numbers, not an undefined observable dictionary.
