# Recursive TT RG physical-prediction preregistration

Status: **preregistered next killer gate**.

Purpose: freeze the representation map, fit form and pass/fail logic **before** using any external gravitational-wave posterior and before declaring a physical Lorentz-violation coefficient.

## Frozen microscopic inputs

Use the canonical research branch containing:

- the fixed q=2 / PL / Peter–Weyl architecture;
- the regulator-safe Euclidean higher-shell observable `Lambda`;
- the exact higher-shell result in `PETER_WEYL_HIGHER_SHELL_LAMBDA_RESULT.md`;
- the exact S4 reduction in `PETER_WEYL_HIGHER_SHELL_S4_RG_SEED.md`;
- the geometry-only no-flow control in `PL_GALERKIN_ANISOTROPY_NO_FLOW.md`;
- the logical-shape/TT separation in `LOGICAL_SHAPE_TO_TT_RG_BRIDGE.md`;
- the fixed Lorentzian/HDA construction;
- the reduced TT transfer in `TT_PROPAGATOR_FIRST_PASS.md`.

No Standard-Model mass, electromagnetic coupling or gravitational-wave constraint may be used to choose the microscopic operator ordering, shell normalization, logical projector, shape-to-metric map or blocking prescription after this preregistration.

## 0. Representation firewall: `R_aniso` is not `zeta4`

The logical qubit carries the S4 irrep `E=[2,2]`, and exact representation theory gives

\[
\operatorname{End}(E)=A_1(I)\oplus A_2(Y)\oplus E(X,Z).
\]

Thus

```text
(X,Z) = intrinsic shape / metric doublet
Y     = orientation pseudoscalar.
```

The internal pair observable

\[
R_{aniso}=\frac{J_{orient}-J_{shape}}{c_0}
\]

is a valid RG diagnostic, but it is **not** identified with the spatial cubic TT coefficient.

The physical TT kernel must instead be derived from the connected shape Hessian

\[
\Gamma_{shape}^{AB}(\omega,\mathbf k;b)
=\frac{\delta^2\Gamma_{eff}}
{\delta s_A(-\omega,-\mathbf k)\delta s_B(\omega,\mathbf k)},
\qquad s_A=(X,Z),
\]

together with the flux/tetrahedron shape-to-metric Jacobian `M` and the TT projector:

\[
\boxed{K_{TT}=\Pi_{TT}M\Gamma_{shape}M^T\Pi_{TT}.}
\]

No symmetry-only proportionality `zeta4 proportional to R_aniso` is admissible.

## 1. Quantity to compute

Construct one recursive spatial blocking map from the exact logical Peter–Weyl **shape doublet** to a TT metric field on successive PL refinements.

At each level derive:

1. the internal higher-shell coefficients `{c0,J_shape,J_orient}`;
2. the connected shape Hessian `Gamma_shape(omega,k;b)`;
3. the metric/TT kernel `K_TT(omega,k;b)`;
4. the physical pole.

Let `a_b` denote the derived physical/combinatorial length associated with that blocking level. Fit the same connected TT pole to

\[
\omega^2
=c_b^2 k^2
+c_b^2a_b^2\left[
\eta_{2,b}^{iso}(k^2)^2
+\zeta_{4,b}^{cub}
\left(\sum_i k_i^4-\frac35(k^2)^2\right)
\right]
+O(a_b^4k^6).
\]

`eta2_iso` and `zeta4_cub` are therefore dimensionless at each declared blocking scale. The scalar and cubic coefficients must be fitted simultaneously. A one-dimensional axis fit is not admissible as a substitute.

## 2. Internal RG control carried in parallel

The already-open `j=1/2` higher-shell gives

\[
R_{1/2}=0.0897532661805313.
\]

The first non-arbitrary representation growth is frozen separately in `PETER_WEYL_J1_INTERNAL_RG_PREREGISTRATION.md`:

\[
\frac12\to1,
\qquad
\mathcal H_{j=1}^{singlet}=[4]\oplus[2,2],
\]

with the multiplicity-one `[2,2]` coarse logical qubit.

Report `R_1`, `Delta R` and `R_1/R_1/2`, but do **not** convert that representation step to `dR/dlog(b)` until the common spatial block determines `b`.

This internal flow diagnoses whether the orientation sector becomes more or less separated from shape dynamics; it is not substituted for the TT quartic fit.

## 3. Bare TT reference values

The already-frozen reduced transfer gives

\[
\boxed{\eta_{2,bare}^{iso}=-1/45}
\]

and

\[
\boxed{\zeta_{4,bare}^{cub}=-1/12}.
\]

These are references, **not targets**. The RG calculation is allowed to move either value.

## 4. Required momentum directions

At minimum use independent low-momentum modes approaching the continuum along

```text
(100)
(110)
(111)
```

plus enough off-axis directions to separate the rotational scalar from the cubic invariant.

For the reduced bare transfer the directional coefficients are

```text
eta(100) = -1/18
eta(110) = -1/72
eta(111) = 0
```

but the blocked theory is not required to preserve these numbers.

## 5. Continuum/RG hypotheses

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

This produces an anisotropic Lorentz-violation prediction rather than a single scalar coefficient.

### H_fail — no physical fixed coefficient

Any of the following is a failure of this physicalization gate:

- coefficients do not stabilize with refinement;
- the result depends materially on arbitrary regulator details after the declared continuum extrapolation;
- the result requires identifying the orientation pseudoscalar with the TT metric by fiat;
- the shape-to-metric Jacobian or TT projector must be retuned after seeing the result;
- pole identification becomes nonunique;
- a ghost/tachyon pole enters the physical TT sector;
- the two TT polarizations split without a separately derived parity/chirality mechanism;
- post-hoc operator retuning is needed to obtain an acceptable continuum trend.

## 6. Scale normalization

The common Regge coefficient is

\[
\lambda_R^{eff}=\frac{a_*^2}{8\pi\ell_P^2}.
\]

The one remaining overall microscopic action/phase slope may be fixed by **one declared gravitational normalization datum** if it cannot be derived internally.

No quartic coefficient and no `R_aniso` value may be used for scale calibration.

Once `lambda_R_eff` is frozen,

\[
\frac{a_*}{\ell_P}=\sqrt{8\pi\lambda_R^{eff}}.
\]

## 7. External observables after freezing

For a rotationally restored quartic correction,

\[
E^2=p^2c^2+A_4p^4c^4+\cdots
\]

with

\[
\boxed{
A_4=\frac{\eta_2^* a_*^2}{(\hbar c)^2}
=\frac{8\pi\eta_2^*\lambda_R^{eff}}{E_P^2}.
}
\]

If `zeta_4^* != 0`, freeze the full directional tensor before comparing with any anisotropic propagation constraint.

## 8. Vacuum correlator cross-check

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

## 9. Matter/constant firewall

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

## 10. Required frozen output before external comparison

Commit a machine-readable result containing at least

```text
microscopic commit SHA
internal representation blocking rule
spatial PL blocking prescription
shape-to-metric Jacobian
regulator sequence
momentum directions
fit window
c_TT(b)
eta2_iso(b)
zeta4_cub(b)
R_aniso(b) as a separate internal diagnostic
continuum extrapolation
uncertainty estimate
lambda_R_eff
A4 or anisotropic tensor
PASS / TENSION / FAIL criterion
```

Only after that commit may the chosen external posterior be opened for the blind comparison.

## Interpretation

The corrected preregistered chain is

```text
exact Peter-Weyl higher shell
 -> S4 shape/orientation decomposition
 -> symmetry-selected internal representation blocking
 -> connected shape Hessian Gamma_shape(omega,k;b)
 -> shape-to-metric map + TT projection
 -> TT pole
 -> frozen {eta2_IR,zeta4_IR}
 -> one scale calibration
 -> external blind comparison.
```

`R_aniso` is carried in parallel as an internal RG observable and possible source of nonlinear orientation feedback, but is not numerically identified with `zeta4`.

No result is promoted to physical law merely because it resembles GR or a known constant.
