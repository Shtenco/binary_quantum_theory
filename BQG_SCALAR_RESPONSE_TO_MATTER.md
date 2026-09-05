# BQG scalar response to a conserved matter probe

Status: **required physical-response interface identified; matter coupling not yet derived.**

The first q=2 scalar-effective-action calculation exposes an additional requirement that must be explicit before `mu_BQG` or `Sigma_BQG` can be called predictions.

A scalar metric Hessian by itself is a vacuum operator.  The functions conventionally called `mu(a,k)` and `Sigma(a,k)` are response coefficients: they compare metric potentials to a matter/energy source.  Therefore BQG must either derive a universal matter coupling or clearly declare a conserved external probe used only to define the gravitational response.

## 1. Required physical variational problem

After the theory-specific history has produced a physical metric effective action,

\[
\Gamma_{grav}[g],
\]

the linear response about a background `g_bar` requires a source term of the form

\[
\Gamma_{tot}[g;T]
=\Gamma_{grav}[g]
+S_{probe}[g;T].
\]

At linear order one may write schematically

\[
S_{probe}^{(1)}
=\frac12\int d^4x\sqrt{-\bar g}\,
 h_{\mu\nu}T^{\mu\nu},
\]

with the normalization and sign frozen consistently with the emergent Einstein sector.

The response equation is then

\[
\boxed{
\Gamma_{gg}^{(2)}\,h
=-J_T
}
\]

on the properly gauge-fixed or gauge-quotiented physical space.

Without `J_T` there is no operational definition of a modified Newtonian response.

## 2. Conservation and Ward consistency

A legal external probe must be conserved on the background,

\[
\bar\nabla_\mu T^{\mu\nu}=0.
\]

The metric kernel must satisfy the corresponding diffeomorphism/Ward identities before scalar gauge reduction.  Gauge artefacts must not be mistaken for extra dark modes.

This is especially important because the DeWitt conformal direction is negative in the unreduced canonical kinetic form while lapse and shift enforce constraints.  A negative conformal direction before Hamiltonian/diffeomorphism reduction is not by itself a propagating ghost, and a local conformal Hessian is not by itself a dark-matter degree of freedom.

## 3. Scalar response variables

For scalar perturbations in Newtonian gauge,

\[
ds^2=a^2(\eta)
\left[-(1+2\Psi)d\eta^2
+(1-2\Phi)d\mathbf x^2\right],
\]

the response to a conserved scalar matter perturbation can be summarized only after the physical kernel and coupling are derived.

A standard bookkeeping convention is

\[
-k^2\Psi
=4\pi G_{ref}a^2\,\mu_{BQG}(a,k)\,\rho\Delta,
\]

and

\[
-k^2(\Phi+\Psi)
=8\pi G_{ref}a^2\,\Sigma_{BQG}(a,k)\,\rho\Delta.
\]

The reference Newton coupling and source normalization must come from the same one-scale physicalization convention used elsewhere in the repository.  `mu` and `Sigma` are outputs, not independent fit functions.

The slip is then

\[
\eta_{slip}=\frac{\Phi}{\Psi}
=\frac{2\Sigma}{\mu}-1
\]

when the above definitions apply.

## 4. Lensing makes the source interface unavoidable

Massive nonrelativistic dynamics primarily probes `Psi`.

Weak/strong lensing and the gravitational Fermat/time-delay phase probe the Weyl combination

\[
\Phi_W=\frac{\Phi+\Psi}{2}.
\]

Therefore one derived response to the **same** conserved source must generate both sectors.  A theory that uses one coupling or effective mass for dynamics and another for lensing has not closed `LENSING_DYNAMICS_CLOSURE`.

## 5. Two physically distinct outcomes

The future BQG scalar calculation can produce at least two qualitatively different classes of result.

### A. Modified-constraint / modified-gravity response

After lapse/shift reduction there may be no new propagating scalar pole, but the constraint kernel can differ from Einstein gravity:

\[
\mu_{BQG}\ne1,
\qquad
\Sigma_{BQG}\ne1.
\]

This is a modified-gravity interpretation.  To mimic dark matter it must reproduce dynamics, lensing, growth, background consistency and all stability constraints with the same kernel.

### B. Emergent collective dark mode

The connected physical history may instead generate an additional scalar pole or collective excitation.  Before it can be called dark matter it must satisfy, at minimum:

- positive physical residue / no ghost;
- stable dispersion;
- sufficiently small effective sound speed on structure-forming scales if a cold component is claimed;
- controlled anisotropic stress;
- universal gravitational sourcing of `Phi/Psi`;
- a derived abundance/background history rather than a fitted density;
- the same lensing-dynamics response.

An additional pole is therefore a much stronger claim than a modified Poisson coefficient.

## 6. Dark energy is a separate zero-momentum/background question

A scalar response to `T_{mu nu}` does not by itself determine dark energy.

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

A zero-source normalization such as `W(0)=0` or `Gamma(p0)=0` is not a vacuum-energy prediction because normalized finite traces remove an additive free-energy normalization.

## 7. New physical gate

The scalar frontier therefore requires

```text
PHYSICAL_CONSERVED_MATTER_SOURCE_COUPLING = open_physical
```

until either:

1. the BQG microscopic construction derives the relevant matter/probe coupling and normalization, or
2. a conserved external test source is explicitly introduced only as a response probe, with its coupling fixed by the same emergent Einstein/one-scale convention and never refitted between dynamics and lensing.

Only after this interface and the physical scalar kernel are both frozen may `mu_BQG` and `Sigma_BQG` be promoted from symbols to predictions.
