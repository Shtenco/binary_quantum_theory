# Exact finite S4 spectrum of the BCQG coarse metric calibration

The direct first-block coarse face-flux calculation fixes the BCQG-native metric map

\[
h=M_{hq}q.
\]

In the frozen edge ordering `(01,02,03,12,13,23)` and orthonormal metric ordering `(xx,yy,zz,sqrt(2)xy,sqrt(2)xz,sqrt(2)yz)`, the measured matrix closes to

\[
M_{hq}=\begin{pmatrix}
1/\sqrt{12}&0&0&0&0&1/\sqrt{12}\\
0&1/\sqrt{12}&0&0&1/\sqrt{12}&0\\
0&0&1/\sqrt{12}&1/\sqrt{12}&0&0\\
0&0&1/\sqrt6&-1/\sqrt6&0&0\\
0&1/\sqrt6&0&0&-1/\sqrt6&0\\
1/\sqrt6&0&0&0&0&-1/\sqrt6
\end{pmatrix}
\]

to the exact-gate tolerance.

Let `O_opp` exchange each coarse edge with its opposite edge. Then

\[
\boxed{M_{hq}^TM_{hq}=\frac14I-\frac1{12}O_{opp}}.
\]

Since the six-edge representation is

\[
6=A_1\oplus E\oplus T_2,
\]

`O_opp` has eigenvalue `+1` on `A1+E` and `-1` on `T2`. Therefore

\[
\boxed{s_{A_1}^2=s_E^2=\frac16},
\qquad
\boxed{s_{T_2}^2=\frac13},
\]

or

\[
\boxed{s_{A_1}=s_E=\frac1{\sqrt6}},
\qquad
\boxed{s_{T_2}=\frac1{\sqrt3}}.
\]

Also

\[
\det M_{hq}=-\frac{\sqrt2}{108},
\qquad
cond(M_{hq})=\sqrt2.
\]

## Consequence for the kinetic Hessian

For an `S4`-diagonal raw Hilbert-space Hessian `K_q`, the physical metric Hessian is

\[
K_h=M_{hq}^{-T}K_qM_{hq}^{-1}.
\]

Hence the channel eigenvalues rescale as

\[
\lambda_{A_1}^{(h)}=6\lambda_{A_1}^{(q)},
\qquad
\lambda_E^{(h)}=6\lambda_E^{(q)},
\qquad
\lambda_{T_2}^{(h)}=3\lambda_{T_2}^{(q)}.
\]

Therefore finite physical traceless isotropy

\[
\lambda_E^{(h)}=\lambda_{T_2}^{(h)}
\]

requires

\[
\boxed{\lambda_{T_2}^{(q)}=2\lambda_E^{(q)}}.
\]

Equal raw Hilbert-space `E` and `T2` eigenvalues would **not** be an isotropic metric result; they would generate a factor-two physical split after the measured coordinate transport.

## Blind DeWitt ratio

For the ADM/DeWitt kinetic form

\[
K_h\sim \pi^{ij}\pi_{ij}-\frac12\pi^2,
\]

the trace eigenvalue is `-1/2` of the common traceless eigenvalue. Because `A1` and `E` share the same calibration scale while `T2` has twice the squared scale, the corresponding raw `q`-space blind target is

\[
\boxed{
\lambda_{A_1}^{(q)}:\lambda_E^{(q)}:\lambda_{T_2}^{(q)}
=-\frac12:1:2.
}
\]

This ratio is **not** an input to the depth-two producer. It is an external discriminator derived only after the metric calibration was measured. The producer must emit the raw depth-two channels without consulting this ratio.

## Reproducibility

- `scripts/collective_metric_calibration_irrep_gate.py`
- `verification_results/COLLECTIVE_METRIC_CALIBRATION_IRREP.json`
- `scripts/collective_l1_coarse_flux_response_gate.py`
- `verification_results/COLLECTIVE_L1_COARSE_FLUX_RESPONSE.json`
- `scripts/collective_metric_hessian_extractor.py`

## Status

`PROVED_FINITE_CALIBRATION_THEOREM` for the first canonical barycentric coarse block.

Continuum refinement must still test whether the transported physical `E` and `T2` kinetic channels merge and whether the trace ratio tends to DeWitt `c=1/2`.
