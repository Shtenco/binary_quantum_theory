# BCQG collective metric -> photon/interference bridge

## Status

The photon bridge now contains four separate statements:

- `MATTER_KINEMATIC_PRECURSOR`: exact U(1) gauge kinematics on the BCQG PL carrier;
- `STRUCTURAL_OPTICAL_BRIDGE`: exact metric-to-balanced-phase map;
- `DIRECT_L1_METRIC_RESPONSE_PRECURSOR`: direct finite BCQG coarse metric response;
- `EXACT_RELATIVE_SENSITIVITY_SPECTRUM`: closed-form conditioning of the five balanced phase channels.

It is **not yet an absolute experimental prediction** because the physical block length `ell_*`, Lorentzian/history Maxwell normalization and BCQG geometry correlator are not yet fixed.

## 1. Maxwell/Hodge coupling

Use minimal metric coupling

\[
S_{EM}=-\frac14\int d^4x\sqrt{-g}\,g^{\mu\alpha}g^{\nu\beta}F_{\mu\nu}F_{\alpha\beta}.
\]

On the PL carrier,

\[
A\in C^1,\qquad F=dA,\qquad S_{EM}^{PL}=\frac12F^T*_2(g)F.
\]

The executable 16-cell gate verifies

\[
d_1d_0=0,
\]

so `A -> A+d_0 lambda` leaves `F` and the weighted action invariant for arbitrary positive nonuniform face-Hodge weights. On `(V,E,F,T)=(8,24,32,16)`:

\[
rank(d_0)=7,\quad rank(d_1)=17,\quad rank(d_1^T*_2d_1)=17,
\]

and Maxwell nullity is seven, exactly the gradient/gauge dimension. Therefore BCQG metric information may enter photon propagation through `*_g` without breaking U(1) gauge symmetry.

## 2. Geometric coordinate maps

Use orthonormal metric coordinates

\[
h=(h_{xx},h_{yy},h_{zz},\sqrt2h_{xy},\sqrt2h_{xz},\sqrt2h_{yz}).
\]

For six regular-tetrahedron edge directions,

\[
y=J_{edge}h,
\qquad
\det J_{edge}=-\frac{\sqrt2}{2}\ne0.
\]

For four coarse face fluxes define six gauge-invariant Gram observables

\[
Z_{fg}=X_f\cdot X_g,
\qquad f<g.
\]

Their regular-background metric Jacobian obeys

\[
\delta Z=J_Fh,
\qquad
\boxed{\det J_F=\frac{128\sqrt2}{729}\ne0},
\qquad
rank(J_F)=6.
\]

Thus coarse face-flux Gram data are complete local coordinates on `Sym^2(R^3)`; no separate quantum edge-length operator is required.

## 3. Direct finite BCQG metric response

The first barycentric block contains 24 fine chambers, 36 internal dual links and 24 open boundary links. After exact internal contraction and projection of the static boundary state, the strict `q=4` Euclidean image supplies six equal-norm coarse-edge directions.

For the physically real Schrödinger tangent

\[
|\tau_e\rangle=-i|w_e\rangle,
\]

the coarse background is

\[
\boxed{\langle X_f^2\rangle=\frac92},
\qquad
\boxed{\langle X_f\cdot X_g\rangle=-\frac32\quad(f\ne g)}.
\]

The response

\[
(B_F)_{(fg),e}=2\,Re\langle0|Z_{fg}|\tau_e\rangle
\]

has tetrahedral classes

```text
same      ~ 0
adjacent  ~ 0
opposite  = -1.7320508075688885
```

with the opposite coefficient equal to `-sqrt(3)` to `1.13e-14` in the exact numerical contraction. The hard gate uses rank/covariance rather than fitting this closed form.

The measured matrix has

\[
\boxed{rank(B_F)=6},
\qquad
\boxed{cond(B_F)=1.0000000000000002}.
\]

With

\[
J_F^{bg}=\frac92J_F,
\]

the direct BCQG-native metric calibration is

\[
\boxed{h=M_{hq}q},
\qquad
\boxed{M_{hq}=(J_F^{bg})^{-1}B_F},
\]

with rank six and condition number `sqrt(2)` to numerical precision.

This resolves the earlier apparent sharp-spin paradox: a local fine-graph spin-preserving flux operator has a representation-sector selection zero, while exact internal contraction maps the changed-spin dynamics into a common coarse boundary Hilbert space where the coarse total-face observable has nonzero full-rank response.

## 4. Mean photon phase

For a weak spatial perturbation and optical baseline `ell_*`,

\[
\delta\ell_e=\frac{\ell_*}{2}(J_{edge}h)_e+O(h^2).
\]

Let

\[
\kappa=\frac{k\ell_*}{2}.
\]

Five balanced path differences are collected by a `5x6` matrix `D`:

\[
\Delta\Phi=\kappa D J_{edge}h.
\]

Using the measured native metric map,

\[
\boxed{
\Delta\Phi=\kappa R_q q,
\qquad
R_q=D J_{edge}M_{hq}.
}
\]

The direct finite response has

\[
\boxed{rank(R_q)=5}
\]

and unique null direction

\[
\boxed{(1,1,1,1,1,1)}.
\]

Thus balanced interferometry removes the common trace mode and reads the complete five-dimensional shape/traceless sector.

## 5. Exact five-channel theorem

Independently of the finite BCQG coefficient,

\[
rank(D)=5,
\qquad
D\mathbf1=0.
\]

For the fixed orthonormal traceless basis `T`,

\[
\boxed{\det[(DJ_{edge})T]=\frac{\sqrt6}{2}\ne0}.
\]

Therefore all five traceless metric components are observable in principle by five independent balanced phase channels.

## 6. Exact relative sensitivity spectrum

The measured first-block matrix `R_q/kappa` matches the closed form

\[
R_q/\kappa=
\begin{pmatrix}
1/\sqrt3&0&0&0&0&-1/\sqrt3\\
\sqrt3/4&\sqrt3/12&0&0&-\sqrt3/4&-\sqrt3/12\\
\sqrt3/4&0&\sqrt3/12&-\sqrt3/4&0&-\sqrt3/12\\
\sqrt3/4&0&-\sqrt3/4&\sqrt3/12&0&-\sqrt3/12\\
\sqrt3/4&-\sqrt3/4&0&0&\sqrt3/12&-\sqrt3/12
\end{pmatrix}
\]

to the frozen numerical tolerance.

The five nonzero eigenvalues of

\[
(R_q/\kappa)(R_q/\kappa)^T
\]

are exactly

\[
\boxed{
\left\{
\frac1{12},\frac13,\frac13,
\frac{19-\sqrt{265}}{24},
\frac{19+\sqrt{265}}{24}
\right\}.
}
\]

Hence the singular values, descending, are

\[
\boxed{
\left(
\sqrt{\frac{19+\sqrt{265}}{24}},
\frac1{\sqrt3},
\frac1{\sqrt3},
\sqrt{\frac{19-\sqrt{265}}{24}},
\frac1{\sqrt{12}}
\right)\kappa.
}
\]

Numerically, per unit `kappa`,

```text
1.21241529938
0.57735026919
0.57735026919
0.33672314319
0.28867513459
```

and the nonzero optical condition number is

\[
\boxed{
\kappa_{opt}=\sqrt{\frac{19+\sqrt{265}}{2}}
=4.1999297968\ldots
}
\]

This is important because it is independent of the unknown absolute scale `ell_*`: the five-mode tomography is not merely invertible but has a finite, moderate relative conditioning already fixed by the finite BCQG geometry.

## 7. Single photon, entanglement and visibility

For an ideal path state

\[
|\psi_\gamma\rangle=\frac{|\gamma_1\rangle+|\gamma_2\rangle}{\sqrt2},
\]

a quantum geometry gives the path coherence

\[
\mathcal C_{12}=\langle\Psi_g|U_{\gamma_2}^\dagger U_{\gamma_1}|\Psi_g\rangle,
\]

with

\[
V=|\mathcal C_{12}|,
\qquad
\Delta\phi=arg\,\mathcal C_{12}.
\]

Thus mean phase and visibility are distinct observables. Path-geometry entanglement can reduce visibility even when a particular mean phase channel vanishes.

For zero-mean commuting/Gaussian phase noise,

\[
\boxed{V=\exp[-Var(\Delta\phi)/2]}.
\]

## 8. Five-channel covariance tomography

Let `x` be the five traceless metric coordinates and

\[
R=(DJ_{edge})T,
\qquad
\det R=\frac{\sqrt6}{2}.
\]

Then

\[
\boxed{\Sigma_\Phi=\kappa^2R\Sigma_gR^T},
\]

so

\[
\boxed{\Sigma_g=\kappa^{-2}R^{-1}\Sigma_\Phi R^{-T}},
\]

and

\[
\boxed{\det\Sigma_\Phi=\frac32\kappa^{10}\det\Sigma_g}.
\]

Once the scale and BCQG correlator are fixed, five balanced photon channels can reconstruct the complete `5x5` covariance matrix of traceless collective geometry in the linear regime.

## 9. Relation to gravitational dynamics

The same six metric directions obey a separate homogeneous gravitational selection theorem:

\[
W_g^\dagger H_E^{sine}W_g=0,
\qquad
W_g^\dagger S W_g=0,
\qquad
W_g^\dagger G W_g=0.
\]

Therefore the finite block displays an operator-depth separation:

- **optical/geometric readout is linear and full rank** at the coarse level;
- **homogeneous gravitational kinetic curvature is depth-two**, entering through leakage/return.

The five balanced optical shape channels are therefore a natural observational basis for the same traceless sector whose depth-two gravitational `E` and `T2` eigenvalues must merge if the continuum theory is Einstein/DeWitt.

## 10. What remains before an experimental BCQG claim

Already fixed or measured:

- exact U(1) gauge kinematics;
- exact six-component coarse metric coordinates;
- direct finite rank-six BCQG metric response;
- direct rank-five BCQG-to-balanced-phase response;
- exact five-channel sensitivity spectrum and finite condition number;
- exact traceless covariance tomography map;
- direct homogeneous gravitational projection zero theorem.

Still required:

1. physical scale setting for `ell_*` and therefore `kappa`;
2. Lorentzian/history Maxwell dynamics and electromagnetic normalization;
3. full depth-two gravitational `E/S` return and `R_op` bookkeeping;
4. BCQG geometry two-point correlators for visibility/noise;
5. refinement scaling and restoration of continuum `SO(3)` isotropy;
6. experimental protocol only after these are frozen.

No present coefficient is to be advertised as a measured photon anomaly, photon mass, refractive-index shift or experimental exclusion.

## 11. Reproducibility

- `scripts/bcqg_u1_maxwell_kinematic_gate.py`
- `verification_results/BCQG_U1_MAXWELL_KINEMATIC.json`
- `scripts/collective_flux_metric_coordinate_gate.py`
- `verification_results/COLLECTIVE_FLUX_METRIC_COORDINATE.json`
- `scripts/collective_l1_coarse_flux_response_gate.py`
- `verification_results/COLLECTIVE_L1_COARSE_FLUX_RESPONSE.json`
- `scripts/collective_photon_interference_metric_gate.py`
- `verification_results/COLLECTIVE_PHOTON_INTERFERENCE_METRIC.json`
- `scripts/collective_photon_covariance_tomography_gate.py`
- `scripts/collective_photon_sensitivity_spectrum_gate.py`
- `verification_results/COLLECTIVE_PHOTON_SENSITIVITY_SPECTRUM.json`
- `scripts/collective_gravitational_direct_block_gate.py`
- `verification_results/COLLECTIVE_GRAVITATIONAL_DIRECT_BLOCK.json`
