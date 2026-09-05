# BQG scalar response to a conserved matter probe

Status: **universal conserved external TEST-PROBE interface frozen; realistic microscopic matter sector and physical scalar kernel remain open.**

The first q=2 scalar-effective-action calculation exposed a requirement that must be explicit before `mu_BQG` or `Sigma_BQG` can be called predictions: a scalar metric Hessian by itself is a vacuum operator, while `mu` and `Sigma` are response coefficients to matter/energy.

The repository now closes the allowed **option-2 response interface** without inventing a matter model: one conserved external test tensor is coupled universally to the metric, with the same normalization convention for dynamics, lensing and time delay.  This removes an otherwise free phenomenological source-coupling ambiguity while leaving realistic matter dynamics open.

## 1. Frozen physical response interface

After the theory-specific history has produced a physical metric effective action,

\[
\Gamma_{grav}[g],
\]

the linear response about a background `g_bar` is defined by

\[
\Gamma_{tot}[g;T]
=\Gamma_{grav}[g]+S_{probe}[g;T],
\]

with the frozen linear source term

\[
\boxed{
S_{probe}^{(1)}
=\frac12\int d^4x\sqrt{-\bar g}\,
 h_{\mu\nu}T^{\mu\nu}.
}
\]

No additional `alpha_dyn`, `alpha_lens` or dark-sector source normalization is introduced.

The response equation is

\[
\boxed{
\Gamma_{gg}^{(2)}h=-J_T
}
\]

on the correctly constrained/gauge-quotiented physical space.

The absolute Newton/length normalization is inherited from the one common Einstein/physicalization scale.  This document does not calibrate that scale.

## 2. Conservation and Ward consistency

The external probe is required to satisfy

\[
\boxed{
\bar\nabla_\mu T^{\mu\nu}=0.
}
\]

For

\[
\delta h_{\mu\nu}
=\bar\nabla_\mu\xi_\nu+\bar\nabla_\nu\xi_\mu,
\]

one obtains, up to a boundary term,

\[
\delta S_{probe}^{(1)}
=-\int d^4x\sqrt{-\bar g}\,\xi_\nu\bar\nabla_\mu T^{\mu\nu}=0.
\]

Thus the frozen probe has zero overlap with linearized pure-gauge metric directions.  `scripts/conserved_scalar_probe_convention_gate.py` verifies the same statement exactly in a flat Fourier scalar control.

This does **not** prove that the future BQG metric kernel itself satisfies all required Ward identities; that remains a property of the theory-specific reduced kernel.

## 3. Scalar response variables

For scalar perturbations in Newtonian gauge,

\[
ds^2=a^2(\eta)
\left[-(1+2\Psi)d\eta^2
+(1-2\Phi)d\mathbf x^2\right],
\]

the same conserved `T^{mu nu}` supplies both source components.  In the flat reference convention,

\[
J_\Psi=-T^{00},
\qquad
J_\Phi=-\sum_iT^{ii}.
\]

Only after the physical reduced scalar kernel exists may the response be summarized as

\[
-k^2\Psi
=4\pi G_{ref}a^2\,\mu_{BQG}(a,k)\,\rho\Delta,
\]

\[
-k^2(\Phi+\Psi)
=8\pi G_{ref}a^2\,\Sigma_{BQG}(a,k)\,\rho\Delta.
\]

The same `G_ref` / one-scale convention enters both equations.  `mu` and `Sigma` are outputs of one reduced kernel, not independent fit functions.

The slip is then

\[
\eta_{slip}=\frac{\Phi}{\Psi}
=\frac{2\Sigma}{\mu}-1
\]

when these definitions apply.

## 4. Lensing and dynamics use one source

Massive nonrelativistic dynamics primarily probes `Psi`.

Weak/strong lensing and the gravitational Fermat/time-delay phase probe

\[
\Phi_W=\frac{\Phi+\Psi}{2}.
\]

Because both are contractions of the response to the same `T^{mu nu}`, the source interface enforces

\[
\boxed{\alpha_{dyn}=\alpha_{lens}}
\]

at the level of coupling convention.  This does not assert `Phi=Psi`; it forbids independent source renormalization between observables.

A future failure of one derived kernel to fit both dynamics and lensing is therefore a falsification signal, not something repaired by introducing another coupling.

## 5. Two physically distinct future outcomes

### A. Modified-constraint / modified-gravity response

After lapse/shift reduction there may be no new propagating scalar pole, but

\[
\mu_{BQG}\ne1,
\qquad
\Sigma_{BQG}\ne1.
\]

This is a modified-gravity interpretation.  To mimic dark matter it must reproduce dynamics, lensing, growth and background consistency with the same kernel and frozen source interface.

### B. Emergent collective dark mode

The connected physical history may instead generate an additional scalar pole or collective excitation.  Before it can be called dark matter it must satisfy at minimum:

- positive physical residue / no ghost;
- stable dispersion / no tachyon;
- acceptable effective sound speed and clustering;
- controlled anisotropic stress;
- universal sourcing of `Phi/Psi` through the frozen probe interface;
- a derived abundance/background history rather than a fitted density;
- the same lensing-dynamics response.

An additional pole is therefore a much stronger claim than a modified Poisson coefficient.

## 6. Dark energy remains a separate background question

A scalar response to `T_{mu nu}` does not determine dark energy.

The homogeneous physical history must independently determine

\[
\rho_{hist}(a),
\qquad
p_{hist}(a),
\]

and only then

\[
w_{hist}(a)
=-1-\frac13\frac{d\ln\rho_{hist}}{d\ln a}
\]

when the effective component is separately conserved in that description.

A normalized finite trace with `W(0)=0` or a local `Gamma(p0)=0` is not a vacuum-energy prediction.

## 7. Updated gate status

The permitted response interface is now frozen through

- `CONSERVED_SCALAR_PROBE_CONVENTION.md`;
- `scripts/conserved_scalar_probe_convention_gate.py`;
- the exact conservation/Ward reference control;
- the one-scale/no-independent-lensing-coupling rule.

Therefore the scalar frontier records

```text
PHYSICAL_CONSERVED_MATTER_SOURCE_COUPLING = frozen
```

with the precise meaning:

```text
frozen external conserved TEST-PROBE convention
!= microscopic realistic matter sector derived
!= common physical scale calibrated
!= physical BQG scalar kernel derived
```

The remaining route is now narrower:

```text
physical volume-history source
+ lapse/shift response block
+ connected scalar interblock history
+ Ward-certified Dirac reduction
+ frozen conserved probe
-> Gamma_scalar^(2)(omega,k)
-> Phi/Psi -> mu_BQG/Sigma_BQG.
```
