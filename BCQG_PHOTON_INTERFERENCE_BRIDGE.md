# BCQG collective metric -> photon/interference bridge

## Status

`STRUCTURAL_OPTICAL_BRIDGE` — exact at linearized coarse-tetrahedron kinematics. It is **not** yet a calibrated experimental prediction.

The purpose is to connect the independently derived six-edge collective metric carrier to a standard optical observable without inserting the GR DeWitt target, an experimental length scale, or a fitted signal amplitude.

## 1. Matter coupling to be used

The minimal continuum target is Maxwell theory on the emergent metric,

\[
S_{EM}=-\frac14\int d^4x\sqrt{-g}\,g^{\mu\alpha}g^{\nu\beta}F_{\mu\nu}F_{\alpha\beta}.
\]

On a simplicial/PL carrier the structure-preserving version is formulated with discrete forms and a metric-dependent Hodge star,

\[
F=dA,\qquad S_{EM}^{PL}\propto -\frac12\langle F,*_gF\rangle.
\]

The present gate does not fix the missing overall matter normalization. Its role is to identify the metric response seen by a photon once the Maxwell sector is attached.

## 2. Exact six-edge metric map

For a regular coarse tetrahedron with unit edge directions `n_e`, define the orthonormal symmetric-tensor coordinates

\[
h=(h_{xx},h_{yy},h_{zz},\sqrt2h_{xy},\sqrt2h_{xz},\sqrt2h_{yz}).
\]

The fractional squared-edge response is

\[
y_e\equiv\frac{\delta \ell_e^2}{\ell_*^2}=n_e^in_e^j h_{ij}\equiv(Jh)_e.
\]

The exact gate gives

\[
\det J=-\frac{\sqrt2}{2}\ne0,
\qquad \operatorname{rank}J=6.
\]

Further,

\[
\sum_e n_en_e^T=2I_3,
\]

so the uniform six-edge direction is exactly the trace/conformal metric direction and the five-dimensional sum-zero edge subspace is exactly the traceless symmetric metric space.

## 3. Photon phase

For a weak static spatial perturbation and an optical segment of baseline physical length `ell_*`,

\[
\delta\ell_e=\frac{\ell_*}{2}y_e+O(h^2),
\]

hence an eikonal photon of wave number `k` acquires

\[
\boxed{\delta\phi_e=\frac{k\ell_*}{2}(Jh)_e.}
\]

For two paths the observable is the relative phase. Choose five independent balanced differences relative to one reference edge and collect them into a `5x6` matrix `D`. Then

\[
\boxed{\Delta\Phi=\frac{k\ell_*}{2}DJh.}
\]

## 4. Exact interferometric theorem

The executable gate proves

\[
\operatorname{rank}D=5,\qquad D\mathbf1=0,
\]

and therefore

\[
(DJ)h_{trace}=0.
\]

On the frozen orthonormal traceless basis `T`,

\[
\boxed{\det[(DJ)T]=\frac{\sqrt6}{2}\ne0},
\]

so

\[
\boxed{\operatorname{rank}[(DJ)T]=5.}
\]

Thus balanced equal-arm edge interferometry is exactly blind to the common trace mode while being informationally complete on all five traceless collective metric directions.

This is particularly useful for the GR killer: the same five-dimensional sector whose kinetic eigenvalue must become the DeWitt traceless eigenvalue is independently addressable by differential photon phases.

## 5. Single-photon statement

For an ideal path superposition

\[
|\psi_\gamma\rangle=\frac{|\gamma_1\rangle+|\gamma_2\rangle}{\sqrt2},
\]

a classical/semi-classical geometry produces a relative phase `Delta phi`; an ideal recombiner gives

\[
P_\pm=\frac12[1\pm\cos(\Delta\phi)]
\]

(up to the chosen beam-splitter phase convention and visibility).

For a quantum geometry the paths can become entangled with the BCQG state. The natural coherence functional is

\[
\mathcal C_{12}=\langle\Psi_g|U_{\gamma_2}^\dagger U_{\gamma_1}|\Psi_g\rangle,
\]

with

\[
V=|\mathcal C_{12}|,\qquad \Delta\phi=\arg\mathcal C_{12}.
\]

This equation defines the next genuinely quantum optical observable: BCQG may affect not only phase but visibility if the two photon paths leave distinguishable geometry states.

## 6. What is and is not predicted now

Already fixed structurally:

- the collective intrinsic metric carrier has six edge-labelled directions;
- its trace/traceless split is exactly `1+5`;
- five balanced phase differences kill the trace common mode;
- those five differences are injective on the whole traceless metric sector.

Still required before quoting an absolute BCQG fringe shift:

1. the direct collective metric-response Jacobian `B=dy/dq` relating microscopic `W_g` coordinates to physical edge observables;
2. the physical block scale `ell_*` / scale-setting branch;
3. the explicit Maxwell/photon Hamiltonian on the BCQG PL complex and its normalization;
4. for visibility/decoherence, the geometry state/correlator entering `C_12`.

Therefore no present coefficient is to be advertised as a measured photon anomaly, photon mass, refractive index, or experimental exclusion.

## 7. Reproducibility

- `scripts/collective_photon_interference_metric_gate.py`
- `verification_results/COLLECTIVE_PHOTON_INTERFERENCE_METRIC.json`

The gate uses exact SymPy algebra and no GR target values.
