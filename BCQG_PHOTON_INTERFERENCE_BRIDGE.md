# BCQG collective metric -> photon/interference bridge

## Status

This bridge now has three distinct layers:

- `MATTER_KINEMATIC_PRECURSOR`: exact U(1) gauge kinematics on the BCQG PL carrier;
- `STRUCTURAL_OPTICAL_BRIDGE`: exact metric-to-balanced-phase and covariance tomography maps;
- `DIRECT_L1_METRIC_RESPONSE_PRECURSOR`: the first finite BCQG coarse block directly supplies a full-rank flux-metric response and therefore a dimensionless BCQG-to-fringe response.

It is **not yet an absolute experimental prediction** because the physical block scale and full Lorentzian Maxwell normalization are not fixed.

## 1. Maxwell/Hodge coupling

Use the minimal metric coupling

\[
S_{EM}=-\frac14\int d^4x\sqrt{-g}\,g^{\mu\alpha}g^{\nu\beta}F_{\mu\nu}F_{\alpha\beta}.
\]

On the PL carrier the kinematic discretization is

\[
A\in C^1,\qquad F=dA,\qquad S_{EM}^{PL}=\frac12 F^T *_2(g)F.
\]

The executable 16-cell gate verifies exactly

\[
d_1d_0=0,
\]

so `A -> A+d_0 lambda` leaves both `F` and the weighted action invariant for arbitrary positive nonuniform face-Hodge weights. On `(V,E,F,T)=(8,24,32,16)` it finds

\[
rank(d_0)=7,\quad rank(d_1)=17,\quad rank(d_1^T*_2d_1)=17,
\]

with Maxwell nullity seven, equal to the gradient/gauge dimension.

Thus BCQG metric information may enter the photon sector through the discrete Hodge operator without sacrificing U(1) gauge invariance.

## 2. Two exact geometric coordinate maps

For a regular coarse tetrahedron use orthonormal metric coordinates

\[
h=(h_{xx},h_{yy},h_{zz},\sqrt2h_{xy},\sqrt2h_{xz},\sqrt2h_{yz}).
\]

### Edge-length optical map

For six unit edge directions `n_e`,

\[
y_e=\delta\ell_e^2/\ell_*^2=n_e^in_e^jh_{ij}\equiv(J_{edge}h)_e,
\]

with

\[
\det J_{edge}=-\frac{\sqrt2}{2}\ne0.
\]

### BCQG-native face-flux metric map

For four coarse face fluxes `X_f` define the six gauge-invariant Gram observables

\[
Z_{fg}=X_f\cdot X_g,\qquad f<g.
\]

At a regular isotropic background their linearized metric Jacobian is

\[
\delta Z=J_Fh,
\]

and the exact gate gives

\[
\boxed{\det J_F=\frac{128\sqrt2}{729}\ne0},\qquad rank(J_F)=6.
\]

Therefore the six coarse flux-pair observables themselves are complete linear coordinates on `Sym^2(R^3)`; no separate quantum edge-length operator is required to calibrate the metric.

## 3. Direct L1 BCQG metric response

The first barycentric block has 24 fine chambers and 36 internal dual links. Contracting the strict-interior `q=4` Euclidean image and projecting out the static boundary state gives six equal-norm coarse-edge directions.

The physically real state tangent associated with the Hermitian Euclidean image is the Schrödinger tangent

\[
|\tau_e\rangle=-i|w_e\rangle.
\]

Insert the coarse face-flux operators after internal contraction. The direct finite calculation gives the static background

\[
\boxed{\langle X_f^2\rangle=\frac92},\qquad
\boxed{\langle X_f\cdot X_g\rangle=-\frac32\quad(f\ne g)},
\]

with exact closure at the reported precision.

For the response

\[
(B_F)_{(fg),e}=2\,Re\langle0|Z_{fg}|\tau_e\rangle,
\]

the three `S4` classes are

```text
same      ~ 0
adjacent  ~ 0
opposite  = -1.7320508075688885
```

and the opposite coefficient agrees with `-sqrt(3)` to `1.13e-14` in the numerical tensor contraction. The closed form is therefore a strong finite identity candidate, but the hard PASS uses only zero/nonzero structure, covariance and rank.

The reconstructed matrix obeys

\[
\boxed{rank(B_F)=6},\qquad
\boxed{cond(B_F)=1.0000000000000002}.
\]

Combining it with the background-scaled flux Jacobian,

\[
J_F^{bg}=\frac92J_F,
\]

gives the direct finite map

\[
\boxed{h=(J_F^{bg})^{-1}B_Fq}.
\]

Its rank is six and its condition number is `sqrt(2)` to numerical precision.

This result is important conceptually: the microscopic sharp-spin selection rule forbids a local spin-preserving metric cross matrix element before RG contraction, but exact internal-link contraction maps the changed-spin dynamics into the same coarse boundary Hilbert space, where a full-rank coarse metric response exists.

## 4. Photon phase

For a weak static spatial perturbation and optical segment of baseline physical length `ell_*`,

\[
\delta\ell_e=\frac{\ell_*}{2}(J_{edge}h)_e+O(h^2).
\]

With wave number `k`, define

\[
\kappa=\frac{k\ell_*}{2}.
\]

Five balanced path differences are collected in a `5x6` matrix `D`, giving

\[
\Delta\Phi=\kappa D J_{edge}h.
\]

For the direct L1 BCQG tangent this becomes

\[
\boxed{
\Delta\Phi=\kappa R_q q,
\qquad
R_q=D J_{edge}(J_F^{bg})^{-1}B_F.
}
\]

The measured finite response has

\[
\boxed{rank(R_q)=5},
\]

and its unique null vector is, to roundoff,

\[
\boxed{(1,1,1,1,1,1)}.
\]

Thus the L1 dimensionless BCQG-to-interference map is already complete on the five shape/traceless directions. Only the common trace mode is removed by balanced interferometry.

The remaining unknown overall experimental factor is `kappa`; it requires the physical coarse length scale.

## 5. Exact five-channel interferometric theorem

Independently of the finite BCQG response coefficient,

\[
rank(D)=5,\qquad D\mathbf1=0.
\]

On the fixed orthonormal traceless metric basis `T`,

\[
\boxed{\det[(DJ_{edge})T]=\frac{\sqrt6}{2}\ne0},
\]

hence all five traceless metric components are observable in principle through five independent balanced phase channels.

This gives an optical readout of the same five-dimensional sector whose kinetic eigenvalues must merge into the rotationally invariant DeWitt traceless sector in the collective GR killer.

## 6. Single photon and quantum visibility

For an ideal path superposition

\[
|\psi_\gamma\rangle=\frac{|\gamma_1\rangle+|\gamma_2\rangle}{\sqrt2},
\]

a classical/semi-classical geometry supplies a relative phase. For a quantum geometry define

\[
\mathcal C_{12}=\langle\Psi_g|U_{\gamma_2}^\dagger U_{\gamma_1}|\Psi_g\rangle,
\]

with

\[
V=|\mathcal C_{12}|,\qquad \Delta\phi=arg\,\mathcal C_{12}.
\]

The phase and visibility are therefore distinct observables. Geometry-path entanglement may reduce visibility even when the mean first-order phase vanishes in a particular microscopic basis.

## 7. Five-channel covariance tomography

Let `x` denote the five traceless metric coordinates and

\[
R=(DJ_{edge})T,
\qquad \det R=\frac{\sqrt6}{2}.
\]

In the linear regime,

\[
\boxed{\Sigma_\Phi=\kappa^2R\Sigma_gR^T}.
\]

Because `R` is invertible,

\[
\boxed{\Sigma_g=\kappa^{-2}R^{-1}\Sigma_\Phi R^{-T}},
\]

and

\[
\boxed{\det\Sigma_\Phi=\frac32\kappa^{10}\det\Sigma_g}.
\]

Thus five balanced photon phase channels can reconstruct the complete `5x5` covariance matrix of traceless collective geometry in the linear regime once the physical scale is known.

For a zero-mean commuting/Gaussian phase fluctuation the usual characteristic-function reduction gives

\[
V=\exp[-Var(\Delta\phi)/2].
\]

This is a future route from BCQG geometry correlators to an interference-visibility prediction; the required BCQG correlator has not yet been derived.

## 8. What remains before an experimental BCQG claim

Already fixed or measured:

- exact U(1) gauge kinematics on the simplicial carrier;
- exact `6 = 1+5` metric geometry;
- invertible BCQG-native face-flux metric coordinates;
- direct finite L1 full-rank coarse metric response;
- direct rank-five BCQG-to-balanced-phase response up to `kappa`;
- exact five-channel traceless covariance tomography map.

Still required:

1. physical scale setting for `ell_*` and therefore `kappa`;
2. Lorentzian/history Maxwell dynamics and overall electromagnetic normalization;
3. full `E+S+R_op` depth-two collective dynamics and its geometry correlators;
4. refinement scaling and continuum isotropy;
5. an experimental protocol only after the above quantities are frozen.

No present coefficient is to be advertised as a measured photon anomaly, photon mass, refractive index shift or experimental exclusion.

## 9. Reproducibility

- `scripts/bcqg_u1_maxwell_kinematic_gate.py`
- `verification_results/BCQG_U1_MAXWELL_KINEMATIC.json`
- `scripts/collective_flux_metric_coordinate_gate.py`
- `verification_results/COLLECTIVE_FLUX_METRIC_COORDINATE.json`
- `scripts/collective_photon_interference_metric_gate.py`
- `verification_results/COLLECTIVE_PHOTON_INTERFERENCE_METRIC.json`
- `scripts/collective_photon_covariance_tomography_gate.py`
- `verification_results/COLLECTIVE_PHOTON_COVARIANCE_TOMOGRAPHY.json`
- `scripts/collective_l1_coarse_flux_response_gate.py`
- `verification_results/COLLECTIVE_L1_COARSE_FLUX_RESPONSE.json`
