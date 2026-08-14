# Open problems — post integration-certificate

The core fixed-cutoff architecture is not reopened here. Peter--Weyl geometry, topology, route HDA and the fixed-cutoff Lorentzian composition certificate remain frozen.

## Project-wide priority: physicalization

The main frontier is no longer another internal logical/mirror matrix element.

The candidate becomes a physical theory only after the common gravitational sector closes the chain

```text
frozen microscopic rule
 -> absolute dimensionless phase/coupling
 -> physical scale setting
 -> Lorentzian TT propagator
 -> observable coefficient not used in calibration
 -> preregistered external prediction
 -> blind comparison with real data.
```

The executable target is now described in

```text
PHYSICALIZATION_SCALE_OBSERVABLE_PREDICTION.md
scripts/physical_scale_prediction_bridge.py
```

The two immediate quantities to derive from one frozen microscopic commit are

```text
lambda_R_eff
eta_2
```

where

```text
lambda_R_eff = a_*^2/(8*pi*l_P^2)
```

sets the lattice/Planck scale relation, while `eta_2` is the leading TT dispersion coefficient in

```text
omega^2 = c^2 k^2 [1 + eta_2 (k a_*)^2 + ...].
```

The corresponding LVK modified-dispersion observable is

```text
alpha = 4
A_4 = eta_2 a_*^2/(hbar*c)^2.
```

No external GW posterior may be used to tune `eta_2` after it is derived.  The repository's held-out L=9,10 preregistration workflow is the model for the external falsification protocol.

In parallel, compute the **true quantum TT two-point function**.  The existing `P_delta_g(k)~k^1.003414` statement remains conditional until that independent quantum correlator reproduces the exponent.

Mirror force and information-mode resonance remain supporting phenomenology branches because they still require additional microscopic quantities (`beta_m`, light-pole data or `xi`).

## New graviton / information-mode result

`GRAVITON_INFOTON_FOAM_BRIDGE.md` adds one exact finite bridge and one conditional physical extension.

Exact finite result:

```text
(1/2)^4 = 2 x j=0 + 3 x j=1 + 1 x j=2,
```

with the `m=+2/-2` extremal states forming an exact two-state code inside the unique `j=2` sector. This gives a microscopic route from four spin-1/2 constituents to a spin-2 collective channel. For a massless spin-2 excitation, the physical helicity `+/-2` polarization space is therefore naturally a logical qubit.

Conditional vacuum result: if the frozen `delta g ~ b^-2.001707` law is interpreted as a quantum RMS coarse-graining law in 3D, then

```text
P_delta_g(k) ~ k^1.003414
```

at low k. This is a hyperuniform-like rather than white-noise vacuum prediction.

Conditional GW-response result: if a bosonic route/information mode has a nonzero TT quadratic metric coupling, a coherent gravitational wave gives a Mathieu-type vacuum-squeezing channel centered at

```text
Omega_GW ~= 2 omega_I,
mu ~= |xi*h| omega_I / 4.
```

The finite Floquet gate reproduces this leading growth law and off-resonance negative controls.

## Genuine research beyond the certificate

The remaining higher-level questions are now more sharply separated:

- freeze the absolute microscopic phase/coupling and selected quantum/history measure;
- derive `lambda_R_eff` and the physical lattice/Planck scale relation;
- derive the Lorentzian TT propagator and its low-energy `eta_2` coefficient;
- compute the true vacuum TT two-point function and test the conditional `P(k) ~ k^1.003414` inference;
- preregister and perform at least one external blind comparison;
- prove a **uniform** bound if `Jmax -> infinity` jointly with `epsilon -> 0`;
- derive rather than freeze the unique global q=2 face pairing from the bare causal rewrite, if uniqueness is demanded;
- derive a Lorentzian quantum measure and establish unitarity/reflection or causal consistency;
- derive the route/information-mode action and its TT coupling `xi` rather than introducing `xi` as a placeholder;
- incorporate matter, chirality and anomaly cancellation;
- obtain independent external replication.

A direct 11.3M-state Lorentzian HH enumeration remains optional regression work. It is not a logical bottleneck for the fixed-cutoff regulator-limit HDA statement and is not the project-wide physicalization bottleneck.
