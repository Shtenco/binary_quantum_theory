# Sharp-spin metric-response obstruction and coarse-graining bypass

## Status

Two statements are now simultaneously established and must not be conflated:

1. **microscopic selection theorem:** a spin-preserving fine-graph flux/metric operator has zero linear matrix element between the sharp all-`j=1/2` seed and the strict `q=4` changed-spin carrier;
2. **coarse-block result:** after exact internal-link contraction, the coarse total-face flux Gram observable has a full-rank linear response on the same six collective directions.

Thus the old obstruction remains correct in its microscopic domain, but it does **not** imply that the sharp seed is unusable for every coarse geometric observable.

## 1. Microscopic direct-sum selection rule

The fine spin-network Hilbert space decomposes as

\[
\mathcal H=\bigoplus_{\mathbf j}\mathcal H_{\mathbf j}.
\]

The homogeneous seed lies in one sharp sector `j0` with every microscopic edge at `j=1/2`. Every basis state entering the strict-interior `q=4` columns used to build the six-edge carrier changes exactly four microscopic doubled-spin labels. Therefore

\[
P_{\mathbf j_0}W_g=0,
\qquad
\langle\Omega_0|W_g=0.
\]

For a fine-graph spin-preserving observable `O_micro`, such as a polynomial in local flux generators at fixed microscopic edges,

\[
P_{\mathbf j}O_{micro}P_{\mathbf j'}=0
\qquad(\mathbf j\ne\mathbf j'),
\]

so

\[
\boxed{\langle\Omega_0|O_{micro}|w_A\rangle=0}.
\]

Hence the microscopic linear expectation-value Jacobian vanishes:

\[
\boxed{B_{micro}=0}.
\]

This remains an exact representation-selection theorem.

## 2. Why coarse flux is different

The canonical first barycentric block contains 24 fine tetrahedral chambers, 36 internal dual links and 24 open boundary links. The coarse observable is defined **after exact contraction of the internal block**, using total coarse-face fluxes

\[
X_f=\sum_{\ell\in f}J_\ell
\]

on the open boundary and the six gauge-invariant pair observables

\[
Z_{fg}=X_f\cdot X_g,
\qquad f<g.
\]

The effective coarse matrix element is therefore not the same object as a local fine-edge operator inserted between two different fixed-`\mathbf j` sectors. Internal contraction maps the changed-spin microscopic amplitudes into the common coarse boundary Hilbert space before `Z_fg` is read out.

The direct exact tensor contraction gives the regular background

\[
\langle X_f^2\rangle=\frac92,
\qquad
\langle X_f\cdot X_g\rangle=-\frac32\quad(f\ne g),
\]

and for the physically real Schrödinger tangent `|tau_e>=-i|w_e>`:

\[
(B_F)_{(fg),e}=2\,\mathrm{Re}\langle0|Z_{fg}|\tau_e\rangle.
\]

The three tetrahedral response classes are

```text
same      ~ 0
adjacent  ~ 0
opposite  = -1.7320508075688885
```

with the opposite class agreeing with `-sqrt(3)` to `1.13e-14` in the finite contraction.

Therefore

\[
\boxed{\operatorname{rank}B_F=6},
\qquad
\boxed{\operatorname{cond}B_F=1.0000000000000002}.
\]

This is a finite exact-coarse-graining bypass of the microscopic selection obstruction.

## 3. Consequence for metric calibration

The six pairwise coarse-face flux Gram observables have an independently derived invertible metric Jacobian

\[
\delta Z=J_Fh,
\qquad
\det J_F=\frac{128\sqrt2}{729}\ne0.
\]

Using the measured background scale gives

\[
J_F^{bg}=\frac92J_F,
\]

hence

\[
\boxed{h=(J_F^{bg})^{-1}B_Fq}.
\]

The direct finite `q -> h` map has rank six and condition number `sqrt(2)` to numerical precision. Therefore a coherent spin packet is **not mandatory merely to obtain the first finite coarse metric calibration**.

A coherent/refinement background remains valuable for semiclassicality, fluctuation suppression and refinement robustness, but it is now a separate physics question rather than a forced repair of a missing linear metric map.

## 4. Relation to gravitational dynamics

The existence of a direct coarse metric response does not imply a direct gravitational scalar block. The separate homogeneous phase/S4 theorem gives

\[
W_g^\dagger H_E^{sine}W_g=0,
\qquad
W_g^\dagger S W_g=0,
\]

for the Hermitian-completed Lorentzian `S`, so

\[
W_g^\dagger G W_g=0
\]

for `G=-2H_E/3-32S/9` at `beta=hbar=1`.

Thus the same six directions can be **linearly readable as coarse geometry** while their gravitational kinetic curvature first appears through depth-two leakage/return.

## 5. Photon consequence

The direct coarse map feeds the optical response without waiting for a coherent packet:

\[
\Delta\Phi=\kappa D J_{edge}(J_F^{bg})^{-1}B_Fq,
\qquad
\kappa=\frac{k\ell_*}{2}.
\]

The finite response has rank five and unique null vector proportional to

\[
(1,1,1,1,1,1),
\]

so balanced photon interferometry reads the complete five-dimensional traceless/shape sector while rejecting the common trace mode.

Absolute phase in radians still requires the physical block scale `ell_*`; visibility loss still requires the quantum geometry correlator.

## 6. Reproducibility

- `scripts/collective_l1_coarse_flux_response_gate.py`
- `verification_results/COLLECTIVE_L1_COARSE_FLUX_RESPONSE.json`
- `scripts/collective_flux_metric_coordinate_gate.py`
- `verification_results/COLLECTIVE_FLUX_METRIC_COORDINATE.json`
- `scripts/collective_gravitational_direct_block_gate.py`
- `verification_results/COLLECTIVE_GRAVITATIONAL_DIRECT_BLOCK.json`

## Final status

`PROVED_MICROSCOPIC_SELECTION_RULE + TESTED_FINITE_COARSE_BYPASS`.

Open: repeat the coarse response under refinement/coherent packets and compute the depth-two gravitational return channels needed for the DeWitt Hessian.
