# Recursive TT RG physical-prediction preregistration

Status: **preregistered next killer gate**.

Purpose: freeze the interpretation, fit form and pass/fail logic **before** using any external gravitational-wave posterior and before declaring a physical Lorentz-violation coefficient.

## Frozen microscopic inputs

Use the canonical research branch containing:

- the fixed q=2 / PL / Peter–Weyl architecture;
- the regulator-safe Euclidean higher-shell observable `Lambda`;
- the exact higher-shell result in `PETER_WEYL_HIGHER_SHELL_LAMBDA_RESULT.md`;
- the fixed Lorentzian/HDA construction;
- the reduced TT transfer in `TT_PROPAGATOR_FIRST_PASS.md`.

No Standard-Model mass, electromagnetic coupling or gravitational-wave constraint may be used to choose the microscopic operator ordering, shell normalization or blocking map after this preregistration.

## 1. Quantity to compute

Construct one recursive spatial blocking map from the exact logical Peter–Weyl sector to a TT field on successive PL refinements.

For each blocking level `b`, derive the pole of the same connected TT propagator and fit

\[
\omega^2
=c_b^2 k^2
+c_b^2\eta_{2,b}^{iso} k^4
+c_b^2\zeta_{4,b}^{cub}
\left[\sum_i k_i^4-\frac35(k^2)^2\right]
+O(k^6).
\]

The scalar and cubic coefficients must be fitted simultaneously. A one-dimensional axis fit is not admissible as a substitute.

## 2. Bare reference values

The already-frozen reduced transfer gives

\[
\boxed{\eta_{2,bare}^{iso}=-1/45}
\]

and

\[
\boxed{\zeta_{4,bare}^{cub}=-1/12}.
\]

These are references, **not targets**. The RG calculation is allowed to move either value.

## 3. Required momentum directions

At minimum use independent low-momentum modes approaching the continuum along

```text
(100)
(110)
(111)
```

plus enough off-axis directions to separate the rotational scalar from the cubic invariant.

For the bare transfer the directional coefficients are

```text
eta(100) = -1/18
eta(110) = -1/72
eta(111) = 0
```

but the blocked theory is not required to preserve these numbers.

## 4. Continuum/RG hypotheses

The calculation will distinguish three outcomes.

### H_iso — rotational restoration

\[
\zeta_{4,b}^{cub}\to0,
\qquad
\eta_{2,b}^{iso}\to\eta_2^*\neq\text{undefined}.
\]

This produces a scalar modified-dispersion prediction.

### H_cub — anisotropic fixed point

\[
\zeta_{4,b}^{cub}\to\zeta_4^*\neq0
\]

with a regulator-independent directional tensor.

This produces an anisotropic Lorentz-violation prediction rather than a single LVK scalar coefficient.

### H_fail — no physical fixed coefficient

Any of the following is a failure of this physicalization gate:

- coefficients do not stabilize with refinement;
- the result depends materially on arbitrary regulator details after the declared continuum extrapolation;
- pole identification becomes nonunique;
- a ghost/tachyon pole enters the physical TT sector;
- the two TT polarizations split without a separately derived parity/chirality mechanism;
- post-hoc operator retuning is needed to obtain an acceptable continuum trend.

## 5. Scale normalization

The common Regge coefficient is

\[
\lambda_R^{eff}=rac{a_*^2}{8\pi\ell_P^2}.
\]

The one remaining overall microscopic action/phase slope may be fixed by **one declared gravitational normalization datum** if it cannot be derived internally.

No quartic coefficient may be used for scale calibration.

Once `lambda_R_eff` is frozen,

\[
\frac{a_*}{\ell_P}=\sqrt{8\pi\lambda_R^{eff}}.
\]

## 6. External observables after freezing

For a rotationally restored quartic correction,

\[
E^2=p^2c^2+A_4 p^4c^4+\cdots
\]

with

\[
\boxed{
A_4=rac{\eta_2^* a_*^2}{(\hbar c)^2}
=rac{8\pi\eta_2^*\lambda_R^{eff}}{E_P^2}.
}
\]

If `zeta_4^* != 0`, freeze the full directional tensor before comparing with any anisotropic propagation constraint.

## 7. Vacuum correlator cross-check

For the same blocked kernel compute the equal-time TT covariance

\[
C_{AB}(\mathbf k)
=\int\frac{d\omega}{2\pi}G^{TT}_{AB}(\omega,\mathbf k).
\]

The reduced Gaussian kernel already gives

\[
\boxed{P_{TT}(k)\propto k^{-1}}.
\]

Therefore the old smoothing-derived `k^{+1.003414}` interpretation is not an admissible target. Any different interacting IR exponent must emerge directly from the blocked quantum propagator.

## 8. Matter/constant firewall

This RG calculation is **not allowed** to claim predictions for

```text
alpha_EM
m_e, m_mu, m_tau
quark masses
m_W, m_Z, m_H
Yukawa matrices
```

unless a separately derived gauge/matter operator maps those observables to the same frozen microscopic theory.

Simple numerical coincidences between Peter–Weyl eigenvalues and known constants are not evidence.

## 9. Required frozen output before external comparison

Commit a machine-readable result containing at least

```text
microscopic commit SHA
blocking prescription
regulator sequence
momentum directions
fit window
c_TT(b)
eta2_iso(b)
zeta4_cub(b)
continuum extrapolation
uncertainty estimate
lambda_R_eff
A4 or anisotropic tensor
PASS / TENSION / FAIL criterion
```

Only after that commit may the chosen external posterior be opened for the blind comparison.

## Interpretation

This preregistration turns the next research step into a genuine falsification test:

```text
exact local Peter-Weyl higher shell
 -> recursive geometry
 -> TT pole
 -> frozen quartic tensor
 -> one scale calibration
 -> external blind comparison
```

No result is promoted to physical law merely because it resembles GR or a known constant.