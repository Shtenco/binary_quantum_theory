# Frozen conserved scalar test-probe convention

Status: **external conserved gravitational-response probe convention frozen; microscopic matter sector and common physical scale calibration remain open.**

This closes option 2 of `BQG_SCALAR_RESPONSE_TO_MATTER.md`: BQG may define its gravitational response using a conserved external test source provided the coupling is universal, inherited from the same Einstein/one-scale convention, and is never independently refitted between dynamics and lensing.

The frozen linear interface is

\[
\boxed{
S_{\rm probe}^{(1)}
=\frac12\int d^4x\sqrt{-\bar g}\,h_{\mu\nu}T^{\mu\nu}
}
\]

with

\[
\boxed{\bar\nabla_\mu T^{\mu\nu}=0.}
\]

There is no additional scalar coupling parameter in this definition.

## 1. Ward consistency

For a linearized diffeomorphism

\[
\delta h_{\mu\nu}=\nabla_\mu\xi_\nu+\nabla_\nu\xi_\mu,
\]

integration by parts gives

\[
\delta S_{\rm probe}^{(1)}
=-\int d^4x\sqrt{-\bar g}\,\xi_\nu\bar\nabla_\mu T^{\mu\nu},
\]

up to the boundary term.  Hence a conserved test probe has zero overlap with pure-gauge metric directions.

The CI gate also verifies this identity exactly in a flat Fourier scalar control.

## 2. One source for both dynamics and lensing

In Newtonian gauge,

\[
ds^2=a^2\left[-(1+2\Psi)d\eta^2+(1-2\Phi)d\mathbf x^2\right],
\]

the source components are contractions of the same `T^{mu nu}`.  In the flat reference convention,

\[
J_\Psi=-T^{00},
\qquad
J_\Phi=-\sum_iT^{ii}.
\]

Therefore massive-body dynamics and the Weyl/lensing combination cannot be assigned independent source normalizations.

The frozen rule is

\[
\boxed{\alpha_{\rm dyn}=\alpha_{\rm lens}}
\]

not because the two observables are numerically equal, but because they are responses of the same metric to the same conserved tensor source.

## 3. Scale rule

This interface does not calibrate Newton's constant or the microscopic length scale.  The absolute normalization is inherited from the one common Einstein/physicalization scale used elsewhere in the repository.  If that scale is not internally derived, the existing one-calibration rule applies.

Forbidden:

```text
one source normalization for growth
another source normalization for weak/strong lensing
another source normalization for time delay
retuning source normalization after inspecting data
```

Allowed:

```text
one conserved external probe
one metric coupling convention
one common scale
all scalar observables derived from the same reduced physical kernel
```

## 4. Scientific boundary

This frozen convention does **not** derive:

- Standard-Model matter;
- a microscopic BQG matter Hilbert space;
- a physical dark-matter density;
- the BQG scalar kernel;
- the common scale in SI units.

It does close the response-interface ambiguity.  Once a theory-specific reduced metric kernel exists, `mu_BQG` and `Sigma_BQG` no longer require an extra phenomenological coupling choice.
