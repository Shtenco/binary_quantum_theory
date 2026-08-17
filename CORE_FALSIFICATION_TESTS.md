# Core falsification tests — discrete quantum geometry → continuum GR

Status: **research test register**. A test becomes evidence only when its protocol, parameters, tolerances and held-out data are frozen before the evaluated result is inspected.

The purpose of this file is to keep the project focused on one question:

```text
Can the same discrete quantum microscopic model produce a stable smooth geometry
whose continuum dynamics is general relativity?
```

## 1. Dimension without using the target dimension in the score

Freeze the microscopic binary rule on a training range and evaluate larger held-out generations.

Required observables include Hausdorff/volume-growth dimension, spectral dimension and dynamical exponent. A failure to approach a common macroscopic spatial dimension near three, together with `z -> 1`, falsifies the current route to a 3+1-dimensional continuum.

## 2. Local manifold-link test

For every relevant coarse vertex, compute the link complex and its homology/PL diagnostics.

A persistent non-manifold link, wrong local dimension or unstable topology under refinement falsifies the interpretation of the coarse state as a smooth spatial slice.

## 3. Global completion independence

Repeat continuum observables under more than one admissible microscopic completion/refinement scheme.

If large-scale observables depend strongly on an arbitrary completion choice, the claimed continuum geometry is not universal.

## 4. Qubit-to-geometry reconstruction without oracle geometry

Derive the face-qubit/two-form sector from the microscopic quantum dynamics itself, then reconstruct

$$
\rho_f\to B^i\to g_U.
$$

The target metric, tetrad, connection or curvature must not be encoded into the microscopic state-selection score. Failure to reconstruct a nondegenerate stable metric closes the present bridge.

## 5. Einstein versus non-Einstein negative control

The same reconstruction pipeline must accept a controlled Einstein geometry and reject a smooth non-Einstein geometry at the curvature stage.

A gate that accepts both is not an Einstein-dynamics test; a gate that rejects both is not a working bridge.

## 6. Regge-to-Einstein-Hilbert refinement

For a declared refinement family, test

$$
S_{discrete}[\Gamma_n]\longrightarrow S_{EH}[g]
$$

with no retuning of couplings after each refinement level.

The continuum error must decrease with a preregistered scaling law or bound. A plateau/divergence falsifies the current action bridge.

## 7. Connection/Ward consistency

Test the discrete connection variation and the corresponding Ward/constraint identity on off-shell controls.

The target must be defined independently of the measured residual. A residual that does not decrease under refinement is evidence of a broken gauge/diffeomorphism structure.

## 8. Lorentzian isotropy and dynamical exponent

Measure the long-wavelength dispersion relation in inequivalent lattice directions.

Required continuum behaviour:

```text
z -> 1
angular dispersion spread -> 0
```

A preferred-frame effect that survives refinement falsifies a Lorentz-invariant GR continuum for the tested phase.

## 9. Two physical tensor polarizations in the GR limit

After constraints/gauge reduction, the weak-field continuum sector must contain the two local tensor polarizations of 3+1 GR and no propagating negative-norm mode.

The binary character of microscopic degrees of freedom is not counted as evidence for this result; the polarization count must follow from the constrained continuum dynamics.

## 10. HDA structure function, not only closure to zero

The decisive canonical target is

$$
\frac{1}{i\hbar}[\hat H[N],\hat H[M]]
\longrightarrow
\hat D\!\left[q^{ab}(N\partial_bM-M\partial_bN)\right].
$$

It is not enough for a projected or averaged commutator to vanish. The calculation must reproduce the independently defined diffeomorphism target and its geometry-dependent structure function.

## 11. Multi-node graph-changing off-shell HDA

Freeze several nonconstant lapses and a graph-changing habitat with more than two interacting nodes.

Required result: the normalized defect decreases along a regulator/refinement sequence without channel-by-channel post-hoc normalization. Failure here falsifies the strongest current quantum-GR claim even if all two-node tests pass.

## 12. Joint regulator removal

Test a declared sequence

$$
\epsilon\to0,
\qquad
J_{max}\to\infty,
$$

and bound the route, cross, pure-geometry and truncation contributions separately.

A fixed-cutoff proof cannot substitute for this test.

## 13. Coarse-graining universality

Repeat the continuum extrapolation with at least two reasonable coarse-graining maps and several microscopic perturbations that were not used in model selection.

Universal dimensionless observables should agree within frozen uncertainties. Strong scheme dependence is a falsifier.

## 14. Common physical scale setting

If the model is eventually compared with dimensional observables, use one declared map from microscopic units to physical length/time/action scales.

Do not fit a separate conversion factor to every observable. Failure of one common scale map across held-out observables falsifies that physical calibration.

## 15. Blind external prediction

Before consulting the held-out physical value, commit a preregistration containing:

```text
observable definition
all frozen parameters
allowed inputs
forbidden fitting operations
solver/version
uncertainty calculation
accept/reject threshold
hash of the prediction artifact
```

Only then compare with an independent measurement or dataset.

An internal control that reconstructs a quantity already encoded in its input is not a blind prediction.

---

## Priority order

The highest-value sequence is:

```text
microscopic dynamics -> geometric qubit sector
-> Regge/EH refinement
-> multi-node graph-changing HDA
-> joint regulator removal
-> common scale setting
-> blind external prediction.
```

This register intentionally excludes unrelated matter-spectrum, anomaly, tunnelling and extra-interaction programmes. They may be studied elsewhere only after the gravity core survives its own falsification tests.
