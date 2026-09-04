# Preregistration — BQG physical cosmology, interference and lensing

**Status:** architecture preregistration before theory-specific physical outputs exist.

## Frozen dependency order

No observational comparison is eligible until the following order is respected:

```text
actual graph-changing constraints
 -> physical projector / rigging or boundary history
 -> connected Z[J_g,J_A]
 -> W=log Z
 -> Gamma[g,A]
 -> background/scalar/TT/photon projections
 -> frozen dimensionless outputs
 -> one common scale
 -> external comparison
```

## Forbidden shortcuts

The following invalidate a blind claim:

```text
rename a constraint spectral variable as physical frequency
choose rho_hist(a) from a desired w(a)
fit mu(a,k) and Sigma(a,k) independently to dynamics and lensing
use one gravitational potential for deflection and another for optical phase
interpret TT/higher-shell eigenvalues as dark matter particles
interpret the S4 oracle curvature Lambda~3 as the observed cosmological constant
fit a different scale to GW, photon, lensing or cosmology sectors
select evolving dark energy because a current dataset prefers it
```

## Reference gates frozen before physical calculation

1. Two-path amplitude identity.
2. Environment-overlap decoherence identity.
3. `I3=0` for linear amplitudes plus a quadratic Born rule.
4. Point-lens Fermat stationary-path and wave-phase identity.
5. Split phase/deflection potential negative control.
6. `rho~a^-3 -> w=0`, `rho=const -> w=-1`, `rho~a^-4 -> w=1/3`.
7. Scalar `mu/Sigma/eta` algebra.
8. No-slip reference `mu=Sigma -> Phi=Psi` and `M_lens=M_dyn`.
9. Split lensing/dynamics negative control.

These tests validate the measurement dictionary only. They cannot close a physical BQG gate.

## First theory-specific outputs to freeze

```text
hash/commit of physical-history operator family
physical projector/history prescription
boundary/vacuum state prescription
Gamma_FLRW or equivalent connected background amplitude
rho_hist(a), p_hist(a)
physical scalar 2-point/1PI kernel
Phi(a,k), Psi(a,k) or an equivalent gauge-invariant response
Gamma_AA^(2) and Z_A
photon limiting cone
GW TT limiting cone
regulator/refinement uncertainty
one common scale rule
```

## Dark-sector acceptance requirements

A DM-like claim is not accepted from rotation curves alone. The same frozen scalar output must be confronted with dynamics, weak/strong lensing, CMB lensing, growth/matter power and merging-cluster constraints.

A DE-like claim is not accepted from a chosen equation-of-state ansatz. `w_hist(a)` must be computed from a previously derived `rho_hist(a)` and the conservation equation.

## DESI rule

The theory must not choose LambdaCDM, `w0waCDM`, or any evolving-DE parameterization based on the current DESI preference. DESI DR2 and future releases are comparison data, not microscopic route selectors.

## Lensing/interference rule

The same coarse gravitational phase geometry must control:

```text
stationary optical paths
image deflection
Shapiro/Fermat time delay
coherent phase differences between multiple paths/images.
```

A future theory output that requires an independent lensing or interference potential is a preregistered failure of the unified mechanism.
