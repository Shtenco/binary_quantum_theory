# BCQG v1.3 — collective metric and photon-interference addendum

**Status:** finite exact/structural results plus preregistered open dynamical tests. This addendum does not promote BCQG to an experimentally established theory and does not replace the pending corrected Lorentzian/refinement certificates.

## 1. What is now established at the first canonical coarse block

The first barycentric coarse tetrahedral block carries six background-orthogonal collective edge directions

\[
W_g=(|w_{01}\rangle,|w_{02}\rangle,|w_{03}\rangle,|w_{12}\rangle,|w_{13}\rangle,|w_{23}\rangle),
\qquad W_g^\dagger W_g=I_6.
\]

Under tetrahedral symmetry

\[
\boxed{6=A_1\oplus E\oplus T_2=1\oplus2\oplus3}.
\]

This is the finite carrier on which the first direct collective metric, optical response and dynamical return tests are defined.

## 2. BCQG-native metric calibration

Let the four coarse face fluxes be `X_f` and define the six gauge-invariant observables

\[
Z_{fg}=X_f\cdot X_g,\qquad f<g.
\]

The exact contracted background obeys

\[
\boxed{\langle X_f^2\rangle=\frac92},
\qquad
\boxed{\langle X_f\cdot X_g\rangle=-\frac32\quad(f\ne g)}.
\]

For the real Schrödinger tangents

\[
|\tau_e\rangle=-i|w_e\rangle,
\]

the response

\[
(B_F)_{(fg),e}=2\,Re\langle0|Z_{fg}|\tau_e\rangle
\]

has three tetrahedral classes

```text
same      = 0      (within numerical tolerance)
adjacent  = 0      (within numerical tolerance)
opposite  = -sqrt(3)  (numerically to ~1e-14)
```

and

\[
\boxed{rank(B_F)=6},
\qquad
\boxed{cond(B_F)=1}.
\]

With the independently derived flux-to-metric Jacobian `J_F`, scaled at the measured background,

\[
J_F^{bg}=\frac92J_F,
\]

the native metric map is

\[
\boxed{h=M_{hq}q},
\qquad
\boxed{M_{hq}=(J_F^{bg})^{-1}B_F}.
\]

It is invertible and has

\[
\boxed{cond(M_{hq})=\sqrt2}.
\]

Thus six coarse BCQG state directions already carry six independent components of a symmetric three-metric at the first finite block.

## 3. Exact finite calibration spectrum

The measured map closes to

\[
\boxed{M_{hq}^TM_{hq}=\frac14I-\frac1{12}O_{opp}},
\]

where `O_opp` exchanges the three pairs of opposite tetrahedral edges.

Hence the squared metric-calibration scales are

\[
\boxed{s_{A_1}^2=s_E^2=\frac16},
\qquad
\boxed{s_{T_2}^2=\frac13}.
\]

This is essential for the GR test. A raw Hilbert-space kinetic matrix must be transported to metric coordinates before testing isotropy.

For an `S4`-diagonal raw Hessian,

\[
\lambda_{A_1}^{(h)}=6\lambda_{A_1}^{(q)},
\quad
\lambda_E^{(h)}=6\lambda_E^{(q)},
\quad
\lambda_{T_2}^{(h)}=3\lambda_{T_2}^{(q)}.
\]

Therefore physical finite traceless isotropy requires

\[
\boxed{\lambda_{T_2}^{(q)}=2\lambda_E^{(q)}}.
\]

If the eventual physical metric Hessian is the ADM/DeWitt form with `c=1/2`, then the corresponding **external blind raw-q discriminator** is

\[
\boxed{
\lambda_{A_1}^{(q)}:\lambda_E^{(q)}:\lambda_{T_2}^{(q)}
=-\frac12:1:2.
}
\]

This ratio is not allowed inside the producer, cutoff choice, basis construction or resolvent selection.

## 4. Direct homogeneous gravitational projection vanishes

In the frozen real Peter-Weyl convention

\[
H_E^{sine}=iA_E,\qquad A_E^T=-A_E,
\]

while the Hermitian-completed Lorentzian term has

\[
S=-\frac i2(L_{raw}-L_{raw}^\dagger)=iA_S,
\qquad A_S^T=-A_S.
\]

The six-edge representation and its orientation sign twist admit no nonzero `S4`-invariant real antisymmetric matrix. Therefore

\[
\boxed{W_g^\dagger H_E^{sine}W_g=0},
\qquad
\boxed{W_g^\dagger S W_g=0}.
\]

At `beta=hbar=1`, with

\[
G=-\frac23H_E^{sine}-\frac{32}{9}S,
\]

this gives

\[
\boxed{W_g^\dagger G W_g=0}.
\]

This result is not a failure of gravity. It fixes the operator depth at which nontrivial collective gravitational curvature can first appear: **outside-carrier excursion and return**.

## 5. The true next gravitational observable

Let

\[
P_g=W_gW_g^\dagger,
\qquad Q_\perp=1-P_0-P_g.
\]

Define

\[
X_E=Q_\perp EW_g,
\qquad
X_S=Q_\perp SW_g,
\]

and

\[
L_{EE}=X_E^\dagger X_E,
\quad
L_{SS}=X_S^\dagger X_S,
\quad
L_{ES}=X_E^\dagger X_S+X_S^\dagger X_E.
\]

For the signed geometry

\[
G=-\frac23E-\frac{32}{9}S,
\]

the denominator-free return Gram is frozen as

\[
\boxed{
L_G=\frac49L_{EE}+\frac{1024}{81}L_{SS}+\frac{64}{27}L_{ES}.
}
\]

Each homogeneous matrix is determined by three representatives `(same, adjacent, opposite)`, hence by its `A1`, `E`, `T2` eigenvalues.

`L_G` is a dynamical return diagnostic, not yet the physical effective Hamiltonian. A DeWitt coefficient may be reported only after a target-independent Feshbach/Schrieffer-Wolff resolvent is frozen and the physical effective scalar is constructed.

## 6. Maxwell/photon coupling uses the same metric

The electromagnetic field is introduced minimally through

\[
S_{EM}=-\frac14\int d^4x\sqrt{-g}\,g^{\mu\alpha}g^{\nu\beta}F_{\mu\nu}F_{\alpha\beta}.
\]

On the PL carrier

\[
A\in C^1,
\qquad F=dA,
\qquad S_{EM}^{PL}=\frac12F^T*_2(g)F.
\]

The finite 16-cell gate verifies exact gauge kinematics

\[
d_1d_0=0,
\qquad F[A+d\lambda]=F[A],
\]

for arbitrary positive nonuniform metric/Hodge weights.

Thus the same metric `h` calibrated from the BCQG face-flux Gram controls the electromagnetic Hodge star and therefore photon propagation.

The structural chain is

\[
\boxed{
W_g
\to Z_{fg}=X_f\cdot X_g
\to h_{ij}
\to *_g
\to \text{Maxwell}
\to (\Delta\phi,V).
}
\]

## 7. Balanced photon interference

For an optical wave number `k` and physical coarse baseline `ell_*`, define

\[
\kappa=\frac{k\ell_*}{2}.
\]

Five balanced path differences give

\[
\boxed{
\Delta\Phi=\kappa R_q q,
\qquad
R_q=D J_{edge}M_{hq}.
}
\]

At the first canonical block

\[
\boxed{rank(R_q)=5},
\]

and the unique null direction is the uniform edge mode

\[
\boxed{(1,1,1,1,1,1)}.
\]

Hence balanced optical interferometry removes the common trace mode and is complete on the five-dimensional shape/traceless sector.

## 8. Exact relative photon sensitivity spectrum

The five nonzero eigenvalues of

\[
(R_q/\kappa)(R_q/\kappa)^T
\]

are

\[
\boxed{
\left\{
\frac1{12},\frac13,\frac13,
\frac{19-\sqrt{265}}{24},
\frac{19+\sqrt{265}}{24}
\right\}.
}
\]

Thus the relative singular values are

\[
\boxed{
\left(
\sqrt{\frac{19+\sqrt{265}}{24}},
\frac1{\sqrt3},
\frac1{\sqrt3},
\sqrt{\frac{19-\sqrt{265}}{24}},
\frac1{\sqrt{12}}
\right),
}
\]

and the nonzero tomography condition number is

\[
\boxed{
\kappa_{opt}=\sqrt{\frac{19+\sqrt{265}}2}
=4.1999297968\ldots
}
\]

independent of the unknown overall physical scale.

Thus the five-mode optical readout is not merely algebraically invertible; its relative conditioning is already finite and moderate on the first block.

## 9. Quantum photon visibility

For a path-superposed photon

\[
|\psi_\gamma\rangle=\frac{|\gamma_1\rangle+|\gamma_2\rangle}{\sqrt2},
\]

the geometry-induced coherence is

\[
\mathcal C_{12}=\langle\Psi_g|U_{\gamma_2}^\dagger U_{\gamma_1}|\Psi_g\rangle,
\]

with

\[
V=|\mathcal C_{12}|,
\qquad
\Delta\phi=arg\mathcal C_{12}.
\]

For linearized traceless geometry covariance `Sigma_g`, five balanced phase channels obey

\[
\boxed{\Sigma_\Phi=\kappa^2R\Sigma_gR^T},
\]

and, because the traceless response is invertible,

\[
\boxed{\Sigma_g=\kappa^{-2}R^{-1}\Sigma_\Phi R^{-T}}.
\]

For commuting Gaussian phase fluctuations,

\[
\boxed{V=\exp[-Var(\Delta\phi)/2]}.
\]

Therefore BCQG geometry two-point functions can in principle be mapped to a single-photon fringe-visibility prediction. The required BCQG correlator is not yet computed.

## 10. Operator-depth separation is a concrete BCQG prediction

The first canonical block simultaneously has

\[
rank\left(\frac{d\langle Z\rangle}{dq}\right)=6
\]

and

\[
W_g^\dagger G W_g=0.
\]

So the finite candidate predicts a nontrivial separation:

1. collective geometry is **linearly readable** by coarse flux observables and photon phase;
2. homogeneous gravitational kinetic curvature of those same metric directions first enters at **depth two**.

This is stronger than a qualitative statement that “light follows the emergent metric”: the optical and gravitational calculations share the same independently measured `M_hq` coordinate map.

## 11. Current falsification chain

The next decisive chain is

```text
measured W_g and M_hq
-> exact L_EE, L_SS, L_ES
-> L_G with frozen signed coefficients
-> target-independent physical resolvent
-> physical C_eff and normalized-state K_h
-> c_DeWitt_eff + E/T2 physical degeneracy
-> r_G, r_D, r_H, r_extra
-> collective [H,H] under refinement
-> GR universality verdict
```

The independent blind finite raw-q discriminator for the DeWitt step is

```text
A1 : E : T2 = -1/2 : 1 : 2
```

and is consulted only after the producer output is frozen.

The photon continuation is

```text
same M_hq
-> Lorentzian/history Maxwell operator
-> BCQG geometry correlator Sigma_g
-> phase covariance Sigma_Phi
-> visibility V
-> absolute radians only after ell_* scale setting
```

## 12. Reproducibility map

Core new files:

- `scripts/collective_l1_coarse_flux_response_gate.py`
- `verification_results/COLLECTIVE_L1_COARSE_FLUX_RESPONSE.json`
- `scripts/collective_metric_calibration_irrep_gate.py`
- `verification_results/COLLECTIVE_METRIC_CALIBRATION_IRREP.json`
- `COLLECTIVE_METRIC_CALIBRATION_IRREP_THEOREM.md`
- `scripts/collective_gravitational_direct_block_gate.py`
- `verification_results/COLLECTIVE_GRAVITATIONAL_DIRECT_BLOCK.json`
- `COLLECTIVE_GRAVITATIONAL_DIRECT_BLOCK_THEOREM.md`
- `COLLECTIVE_DEPTH2_RETURN_PREREGISTRATION.md`
- `scripts/collective_metric_hessian_extractor.py`
- `verification_results/COLLECTIVE_METRIC_HESSIAN_EXTRACTOR_SELFTEST.json`
- `scripts/bcqg_u1_maxwell_kinematic_gate.py`
- `scripts/collective_photon_sensitivity_spectrum_gate.py`
- `verification_results/COLLECTIVE_PHOTON_SENSITIVITY_SPECTRUM.json`
- `BCQG_PHOTON_INTERFERENCE_BRIDGE.md`

## 13. Scientific status

**Established finite/structural:** six-component coarse metric carrier; full-rank BCQG-native metric calibration; exact finite S4 calibration spectrum; homogeneous direct gravitational projection zero; exact U(1) PL kinematics; rank-five balanced photon shape readout; exact relative optical sensitivity spectrum.

**Open:** complete depth-two `E/S` return; physical effective resolvent; corrected full Lorentzian collective amplitudes; refinement flow; constraint ranks; collective HDA; geometry correlator; absolute length/energy scale; experimental photon signal.

No absolute phase anomaly, photon mass, refractive-index anomaly or observed deviation from GR is claimed at this stage.
