# Physicalization frontier: scale -> observable -> blind prediction

Status: **new canonical research priority beyond the fixed-cutoff mathematical core**.

The project remains a **candidate theory**.  Internal finite gates are not a substitute for physical scale setting or experiment.

This certificate changes the project-wide priority.  Mirror-sector quantities such as a local logical Lorentzian return remain useful internal consistency tests, but they are not the main bottleneck for turning the architecture into physics.

The physicalization chain is

```text
frozen microscopic rule
 -> absolute dimensionless action/phase normalization
 -> one scale-setting observable
 -> physical length/time normalization
 -> Lorentzian TT propagator
 -> coefficient not used in calibration
 -> preregistered prediction
 -> comparison with external data.
```

---

## 1. Repository-wide diagnosis

The repository already contains strong structural evidence:

- q=2 gives the frozen 3D/4D-like scaling chain;
- the Regge quadratic metric kernel approaches Fierz--Pauli;
- the tested Regge cubic coefficient approaches the Einstein--Hilbert cubic functional;
- held-out L=9,10 Regge defects follow the preregistered approximately `O(a^2)` law;
- the canonical Peter--Weyl/route architecture has a fixed-cutoff HDA composition certificate.

None of those facts fixes meters, seconds or joules by itself.

The current microscopic Hamiltonian is specified only up to an overall coefficient in `CANONICAL_MICRO_ARCHITECTURE_V1.md`, and the executable finite Thiemann gate intentionally omits `G`, `hbar`, `c` and the final absolute prefactor.  `CIMFIG_V18_CANDIDATE_THEORY.md` likewise leaves the microscopic history weights/phases to be derived.

The growth-axiom calculation is important here: composition fixes the primitive phase to be **linear**, but the null space is one-dimensional.  Therefore it fixes the functional dependence, not the overall phase slope.  That remaining scalar is precisely an absolute normalization freedom.

This is the first physical bottleneck.

---

## 2. Why `c_eff != 1` is not the bottleneck

`NORMALIZATION.md` and `FIELD_NORM.md` preserve an older wording in which `c_eff != 1` was treated as a failed absolute continuum match.

`RESOLUTION.md` correctly retracts that target.  The overall coefficient of a correctly shaped Fierz--Pauli kernel is the gravitational wave-function/Newton normalization.  The true structural tests are the tensor ratios, gauge null directions, sign and low-momentum scaling.

Therefore

```text
c_eff != 1
```

is not by itself a contradiction.

But this does **not** mean that Newton's constant has already been predicted.  The microscopic overall phase/coupling is still not fixed.  Once it is fixed, the TT residue can be used for scale matching or an independent consistency test.

---

## 3. Minimal exact scale map

Use coordinates with dimensions of length.  The Einstein--Hilbert action is

\[
S_{EH}=\frac{c^3}{16\pi G}\int d^4x\sqrt{-g}\,R.
\]

The standard smooth Regge relation is

\[
\int d^4x\sqrt{|g|}\,R
\longleftrightarrow
2\sum_h A_h\,\delta_h.
\]

Hence

\[
\frac{S_R}{\hbar}
=\frac{1}{8\pi\ell_P^2}\sum_h A_h\delta_h,
\qquad
\ell_P^2=\frac{\hbar G}{c^3}.
\]

Let the physical lattice length be `a_*`, write

\[
A_h=a_*^2\widetilde A_h,
\]

and define **without convention ambiguity**

\[
\lambda_R^{eff}
\equiv
\text{the renormalized dimensionless coefficient multiplying }
\sum_h\widetilde A_h\delta_h
\text{ in }S_{eff}/\hbar.
\]

Then matching gives

\[
\boxed{
\lambda_R^{eff}=\frac{a_*^2}{8\pi\ell_P^2}
}
\]

or equivalently

\[
\boxed{
\frac{a_*}{\ell_P}=\sqrt{8\pi\lambda_R^{eff}}.
}
\]

This is the correct scale-setting equation for the declared Regge convention.

It is **not yet a numerical prediction**, because the current microscopic rule has not produced a unique `lambda_R^eff`.

A value inserted by hand in an old toy finite-RG script is not admissible evidence for this purpose.

---

## 4. Time scale and the speed of the massless spin-2 mode

Let `tau_*` be one microscopic physical time unit and let the dimensionless low-momentum TT dispersion be

\[
\widetilde\omega(\widetilde k)
=v_0|\widetilde k|+O(|\widetilde k|^3).
\]

With

\[
k=\widetilde k/a_*,
\qquad
\omega=\widetilde\omega/\tau_*,
\]

the physical limiting speed is

\[
\boxed{
c_{TT}=v_0\frac{a_*}{\tau_*}.}
\]

The existing result `z approximately 1` establishes compatible scaling of space and time.  It does not by itself fix the conversion factor `a_*/tau_*` in SI units.

After one physical scale calibration, matching the observed luminal tensor speed fixes the remaining time-unit conversion unless the microscopic theory predicts it independently.

---

## 5. The first clean observable must be the Lorentzian TT propagator

The next project-wide calculation is not another local mirror matrix element.  It is

\[
\boxed{
G^{TT}_{AB}(\omega,\mathbf k)
=\langle h_A^{TT}h_B^{TT}\rangle_{\omega,\mathbf k}
}
\]

from the **same frozen microscopic Hamiltonian/history measure** used for the scale map.

At low momentum it must be fitted before looking at external constraints to

\[
[G^{TT}]^{-1}
=Z_T\left[
\omega^2-c_{TT}^2k^2
-\eta_2 c_{TT}^2a_*^2k^4
+O(a_*^4k^6)
\right].
\]

This single object supplies three physically distinct quantities:

1. pole residue `Z_T` -- Newton/wave-function normalization;
2. pole slope `c_TT` -- physical tensor propagation speed;
3. `eta_2` -- the leading dispersive correction not removable by an overall field normalization.

The first two may participate in calibration.  **`eta_2` must not.**  It is the natural first blind prediction coefficient.

---

## 6. Direct map to an existing gravitational-wave observable

Write the predicted dispersion as

\[
E^2=p^2c^2\left[1+\eta_2(k a_*)^2+O((ka_*)^4)\right],
\qquad k=p/\hbar.
\]

Then

\[
E^2=p^2c^2
+\frac{\eta_2a_*^2}{\hbar^2c^2}\,p^4c^4+\cdots.
\]

The LIGO--Virgo--KAGRA modified-dispersion convention

\[
E^2=p^2c^2+A_\alpha p^\alpha c^\alpha
\]

therefore gives the exact identification for the leading lattice-type correction

\[
\boxed{
\alpha=4,
\qquad
A_4=\frac{\eta_2a_*^2}{(\hbar c)^2}.
}
\]

Combining with the scale equation,

\[
\boxed{
A_4
=\frac{8\pi\eta_2\lambda_R^{eff}}{E_P^2},
\qquad
E_P=\frac{\hbar c}{\ell_P}.
}
\]

Thus a frozen pair

```text
(lambda_R_eff, eta_2)
```

becomes a completely numerical modified-dispersion prediction after one scale calibration.

No new fit to gravitational-wave data is allowed after these coefficients are frozen.

For flat propagation the low-energy expansion also gives

\[
\frac{v_g-c}{c}
=\frac32\eta_2(ka_*)^2+O((ka_*)^4),
\]

and at fixed observed angular frequency, ignoring cosmological redshift only for this local formula,

\[
\Delta\phi(D,\omega)
\simeq
-\frac{\eta_2}{2}
\frac{D\,\omega^3a_*^2}{c^3}.
\]

A real catalog comparison must use the cosmological propagation integral employed in the LVK modified-dispersion analysis rather than this flat-space approximation.

---

## 7. Detectability warning

If `lambda_R_eff` and `eta_2` are both order unity, then `a_*` is of order the Planck length and

\[
A_4\sim\frac{8\pi}{E_P^2}\sim1.7\times10^{-55}\;\mathrm{eV}^{-2}.
\]

This estimate is an **illustration**, not the theory prediction, because neither coefficient has yet been derived.

It also teaches an important strategic lesson: an ordinary `O(a_*^2 k^4)` Planck-scale dispersion correction is likely far too small for current ground-based GW observations.  The modified-dispersion channel is still a clean falsifier, but may not be the most sensitive first experiment.

Therefore a second observable branch should be pursued in parallel: a dimensionless or IR-enhanced prediction whose leading signature is not suppressed by `(k ell_P)^2`.

---

## 8. Best second observable: true quantum metric two-point spectrum

The existing smoothing law

\[
\delta g\sim b^{-2.001707}
\]

was obtained for a coarse-graining defect.  Interpreting it as a vacuum RMS fluctuation gives the conditional exponent

\[
P_{\delta g}(k)\sim k^{1.003414}.
\]

That interpretation is **not yet licensed**.

The correct next vacuum calculation is to construct the physical ground/history state and measure

\[
C_{AB}(x-y)
=\langle0|h_A^{TT}(x)h_B^{TT}(y)|0\rangle
\]

or its spectral density directly.  Only if that independent calculation yields the same exponent may the number

\[
\boxed{n_{foam}=1.003414}
\]

be promoted from a conditional inference to a physical prediction.

This route is especially valuable because a spectral exponent is dimensionless.  Its shape can be falsifiable even before an absolute amplitude is measured, while the amplitude can later be fixed by the same `Z_T/G` normalization.

---

## 9. Why the mirror and infoton branches are not first

### Mirror force

The current mirror-force normalization still depends on independent microscopic quantities such as

```text
beta_m,
g_*,
j_sigma,
delta_sigma
```

and on whether a light one-particle pole survives the full constrained/RG dynamics.  It is therefore not yet a parameter-free first prediction.

### GW-driven information-mode resonance

The resonance location is a clean conditional signature, but its physical rate requires the microscopic TT coupling `xi`, which is not yet derived.

Both branches remain useful **after** the common gravitational scale/propagator is fixed.

---

## 10. Preregistered physical falsification protocol

The repository already demonstrated the right anti-overfitting method in the held-out L=9,10 Regge test: freeze formula and acceptance interval first, then compute held-out values.

Use exactly the same discipline for external physics.

### Calibration set

May determine only quantities explicitly designated as scale setters, for example:

```text
one Newton/Planck normalization datum
and, if necessary, the unit conversion of the causal time step.
```

### Frozen prediction file

Before reading the selected experimental posterior, commit:

```text
microscopic commit SHA
operator ordering
regulator sequence
lambda_R_eff
Z_T
c_TT
eta_2
uncertainty from finite-size/RG extrapolation
predicted external parameter A_4
PASS/TENSION/FAIL rule.
```

### External test

Then compare against a dataset not used anywhere in calibration.

For gravitational-wave propagation the natural present target is the LVK modified-dispersion posterior, in particular its `alpha=4` sector.

No coefficient may be retuned after opening that posterior.

---

# New project-wide frontier

The project-wide priority is now

```text
P0  freeze absolute microscopic phase/coupling and quantum measure
P1  derive lambda_R_eff and a_*/ell_P
P2  derive the Lorentzian TT propagator from the same frozen rule
P3  extract eta_2 and the true vacuum two-point spectrum
P4  preregister one external prediction before opening the comparison dataset
P5  test against real observations
```

Internal mirror, Lorentzian-return and matter gates continue as supporting branches, not as the definition of project completion.

The candidate becomes a physical theory only when this chain produces at least one quantitative observable that survives an external blind comparison without post-hoc retuning.
