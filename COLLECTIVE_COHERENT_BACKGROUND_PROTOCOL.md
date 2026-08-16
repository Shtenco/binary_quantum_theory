# BCQG collective coherent/refinement background protocol

## Updated motivation

The sharp all-`j=1/2` seed has an exact **microscopic** selection obstruction: a fine-graph spin-preserving local flux/metric operator cannot have a linear cross matrix element into the strict changed-spin `q=4` carrier.

However the exact first barycentric coarse block now supplies a stronger finite result. After contracting the 36 internal links and reading total coarse-face flux Gram observables on the open boundary, the direct response matrix is full rank:

\[
\boxed{rank(B_F)=6},
\qquad
\boxed{cond(B_F)\simeq1}.
\]

Therefore a coherent spin packet is **no longer required merely to rescue the first finite metric calibration**. The role of coherent/refinement backgrounds is now cleaner: test semiclassicality, suppress fluctuations, verify stability of the coarse map and follow the carrier toward the continuum.

No background parameter may be selected using `c_eff`, constraint ranks or photon data.

## 1. Sharp coarse-block control

The canonical finite control is the exact contracted sharp-seed block used by

- `collective_l1_background_orthogonal_metric_tangent_gate.py`;
- `collective_l1_coarse_flux_response_gate.py`.

It already provides six orthonormal collective directions and the BCQG-native map

\[
h=(J_F^{bg})^{-1}B_Fq.
\]

This sharp coarse block is now the primary **finite calibration control**.

It is not automatically the final semiclassical vacuum: volume fluctuations, refinement stability and long-wavelength correlations remain separate tests.

## 2. Minimal S4-homogeneous coherent precursor

Let the six orthonormal microscopic/coarse edge columns be `|w_e>` and define

\[
|u\rangle=\frac1{\sqrt6}\sum_{e=1}^6|w_e\rangle.
\]

Since

\[
6=A_1\oplus E\oplus T_2,
\]

`|u>` is the unique `A1` direction.

Define the optional homogeneous packet

\[
\boxed{|\Omega_\alpha\rangle=\frac{|0\rangle+\alpha|u\rangle}{\sqrt{1+\alpha^2}}}.
\]

Frozen finite diagnostic values:

```text
alpha = 1/4, 1/2, 1, 2
```

with `alpha=1` retained as the nominal central diagnostic. No value may be selected or discarded because it moves `c_eff` toward `1/2` or improves an optical signal.

## 3. Tangent frame

For the mixed packet the normalized `A1` tangent is

\[
|t_{A1}\rangle=\frac{|u\rangle-\alpha|0\rangle}{\sqrt{1+\alpha^2}},
\]

and the five shape tangents are the frozen orthonormal `E(2)+T2(3)` combinations orthogonal to `|u>`.

The sharp coarse control and every coherent packet must use the **same irrep labelling and the same BCQG flux-metric observable** so channel trends are comparable.

## 4. Direct metric-response requirement

Use the six coarse face-flux Gram observables

\[
Z_{fg}=X_f\cdot X_g,
\qquad f<g.
\]

For any tested background `Omega`, measure

\[
(B_F)_{(fg),A}=2\,\mathrm{Re}\langle\Omega|Z_{fg}|t_A\rangle.
\]

A background qualifies for metric-Hessian use only if:

1. `rank B_F = 6` at the frozen tolerance;
2. the rank is stable under the declared SVD thresholds;
3. `A1`, `E`, `T2` channel scales are finite and separately reported;
4. conditioning is acceptable;
5. the response is converted to the same physical metric coordinates through the independently derived `J_F`;
6. no state parameter is tuned using the GR or photon target.

At finite tetrahedral symmetry three calibration scales are allowed. Continuum rotational isotropy requires the `E` and `T2` calibrations to merge under refinement.

## 5. Dynamical selection theorem

A nonzero coarse metric response does not imply a nonzero direct gravitational scalar matrix. Under the frozen real recoupling convention and exact homogeneous `S4` covariance,

\[
W_g^\dagger H_E^{sine}W_g=0,
\qquad
W_g^\dagger S W_g=0,
\]

so the signed gravitational block `G=-2H_E/3-32S/9` also has zero direct `6x6` projection.

Therefore the DeWitt question is fundamentally a **depth-two return/backreaction** question. The coherent packet may change finite response and leakage, but it may not be used to manufacture a direct first-order gravitational Hessian forbidden by the symmetry theorem.

## 6. Refinement extension order

If the sharp finite block or the minimal packet is not sufficiently semiclassical, enlarge in this target-independent order:

1. include depth-2 `E,S,R_op` Krylov sectors;
2. construct Gauss-projected representation packets from BCQG geometric/dynamical observables;
3. determine packet parameters by stationarity/minimum-uncertainty or refinement criteria;
4. retain all tested parameter values and bad levels in the published ledger.

The sharp-spin block remains a reproducible control at every stage.

## 7. Photon interpretation

The updated optical picture has two layers:

- **coarse mean phase:** already nonzero at the first sharp contracted block because `B_F` is full rank;
- **quantum visibility/covariance:** depends on the geometry state and therefore remains a major use of coherent/refinement packets.

For the first finite block

\[
\Delta\Phi=\kappa D J_{edge}(J_F^{bg})^{-1}B_Fq
\]

has rank five on the traceless sector. Coherent packets should therefore be tested primarily for the refinement and covariance of this response, not introduced merely to make the mean phase exist.

## Status

`PREREGISTERED_SEMICLASSICAL_ROBUSTNESS_PATH`.

The immediate dynamics bottleneck is no longer `B(alpha)`: the sharp coarse block already has a direct invertible metric map. The next calculation is the three-channel depth-two gravitational return on the same six directions, followed by the normalized-state metric Hessian and constraint-rank experiment.
