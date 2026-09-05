# Unified physical cosmology, light interference and gravitational lensing frontier

**Status:** proposed fail-closed physicalization extension.  This document freezes the architecture and consistency requirements; it does **not** claim that dark matter, dark energy, the Maxwell kernel or observed lensing have already been derived from BQG.

## 1. One generating functional, not four fitted models

The target physical chain is

```text
binary microhistory
 -> theory-specific regulated constraints
 -> physical projector / rigging or boundary-history amplitude
 -> Z[J_g,J_A]
 -> W[J_g,J_A] = log Z
 -> Gamma[g,A]
```

Only after the same `Gamma[g,A]` is defined may it be projected into different observable sectors:

```text
Gamma_AA^(2)       -> photon / Maxwell propagation / interference
Gamma_gg,TT^(2)    -> gravitational waves
Gamma_scalar^(2)   -> Phi, Psi, growth, dynamics and lensing
Gamma_FLRW         -> H(a), rho_hist(a), p_hist(a), w_hist(a)
```

No sector may introduce an independent post-hoc history measure or an independently fitted gravitational potential.

---

## 2. Binary-history interference target

The existing q=2/C4/C8 arithmetic-history layer supplies a real complex structure

```text
J^2 = -I
```

and a phase representation

```text
W(theta) = exp(-theta J) <-> exp(i theta).
```

For alternatives `h` connecting preparation and detection, the target physical amplitude is

```math
A(x) = sum_h A_h(x).
```

For two coherent classes,

```math
A = a_1 e^{i phi_1} + a_2 e^{i phi_2},
```

and a future physical probability rule must recover the observed quadratic interference structure

```math
I = |A|^2
  = a_1^2 + a_2^2 + 2 a_1 a_2 cos(phi_1-phi_2).
```

This equation is currently a **reference target**, not a derivation of the Born rule from BQG.

### Which-path decoherence

If the alternatives correlate with environment/history records `|E_1>, |E_2>`, then

```math
I = |A_1|^2 + |A_2|^2
  + 2 Re[A_1 A_2^* <E_2|E_1>].
```

Thus distinguishability suppresses the same interference term when

```math
<E_2|E_1> -> 0.
```

### Sorkin gate

For ordinary linear amplitude composition plus a quadratic probability rule, third-order interference must vanish:

```math
I_3(A,B,C)=0.
```

A future BQG physical-history output must therefore either recover `I3=0` in the tested regime or explicitly predict a nonzero deviation before comparison with data.

---

## 3. Gravitational lensing is the strongest light-phase consistency bridge

Use scalar perturbations in Newtonian gauge,

```math
ds^2 = a^2(eta) [-(1+2 Psi)d eta^2 + (1-2 Phi)d x^2].
```

Nonrelativistic dynamics primarily responds to `Psi`.  Weak/strong lensing responds to the Weyl combination

```math
Phi_W = (Phi + Psi)/2.
```

Therefore any BQG explanation of an apparent dark component must simultaneously predict both potentials from the **same physical scalar kernel**.

Define the phenomenological bookkeeping functions only after the physical kernel exists:

```math
-k^2 Psi = 4 pi G a^2 mu(a,k) rho Delta,
```

```math
-k^2 (Phi+Psi) = 8 pi G a^2 Sigma(a,k) rho Delta.
```

Then

```math
eta_slip = Phi/Psi = 2 Sigma/mu - 1,
```

and the ratio of lensing-inferred to dynamics-inferred mass enhancement is

```math
M_lens/M_dyn = Sigma/mu.
```

These are not extra fitting functions allowed in the final theory. They are a diagnostic language for the derived scalar response.

### Hard lensing-dynamics closure

If BQG mimics cold dark matter by an effective geometric/history stress tensor with negligible anisotropic stress, a natural no-slip target is

```math
Phi ~= Psi,
mu ~= Sigma,
M_lens ~= M_dyn.
```

A model that produces flat rotation curves by changing `Psi` but fails to generate the corresponding Weyl curvature is rejected.

Likewise, a model that bends light by introducing an independent optical potential while leaving the dynamical metric unchanged is rejected.

---

## 4. Why lensing and interference meet at the phase

In gravitational wave optics the amplification amplitude is schematically

```math
F(omega) ~ integral d^2 theta exp[i omega tau(theta,beta)],
```

where the Fermat/time-delay surface has the structure

```math
tau(theta,beta)
 = geometric_delay(theta,beta)
 - gravitational_delay[Phi_W(theta)].
```

Geometric-optics images satisfy

```math
grad_theta tau = 0.
```

The **same** `tau` also controls the relative phase between multiple coherent images:

```math
Delta phi = omega Delta tau.
```

Hence lensing and interference are not identical phenomena, but they are two limits of the same phase geometry:

```text
same physical Weyl potential
 -> Fermat phase
 -> stationary paths = lensing images/deflection
 -> phase differences = wave-optics interference
```

This creates a direct bridge to BQG's microscopic oriented-history phase.  The future derivation must show that the coarse history phase reduces to the same `Phi_W` that appears in the scalar metric response.

The finite reference script `scripts/binary_history_interference_lensing_gate.py` includes a point-lens control and a negative control in which phase and deflection potentials are artificially split. The split control must not pass.

---

## 5. Dark matter target from the connected history effective action

Do **not** identify current TT higher-derivative coefficients, higher-shell constraint eigenvalues or the finite E/T2 anisotropy with dark matter.

The intended route is instead

```text
physical connected histories
 -> Gamma_hist[g]
 -> T_hist^{mu nu}
 -> background + scalar response
 -> growth + dynamics + lensing.
```

Define

```math
T_hist^{mu nu}
 = -2/sqrt(-g) * delta Gamma_hist / delta g_{mu nu}.
```

A dark-matter-like branch must demonstrate, over the relevant regime and without per-observable retuning,

```math
rho_hist > 0,
p_hist/rho_hist ~= 0,
c_s^2 ~= 0,
```

small enough anisotropic stress for the claimed no-slip regime, stable clustering, and the correct sign/magnitude of the scalar gravitational response.

It must then survive the joint observable set rather than only galaxy rotation curves:

```text
galaxy/cluster dynamics
weak and strong lensing
CMB lensing
matter power spectrum / growth
merging-cluster morphology
```

The current repository does not yet satisfy this gate.

---

## 6. Dark energy target from the homogeneous history sector

The background projection of the same connected effective action defines

```math
rho_hist(a), p_hist(a).
```

Covariant conservation gives

```math
d rho_hist/d ln a + 3(rho_hist+p_hist)=0,
```

so for positive density

```math
w_hist(a)
 = p_hist/rho_hist
 = -1 - (1/3) d ln rho_hist / d ln a.
```

This is an **inference from a derived density**, not permission to choose a desired `w(a)` and reconstruct a convenient density.

Reference limits are

```text
rho_hist ~ a^-3  -> w_hist = 0     (pressureless matter-like)
rho_hist = const -> w_hist = -1    (cosmological-constant-like)
rho_hist ~ a^-4  -> w_hist = 1/3   (radiation-like)
```

The scientifically preferred order is therefore

```text
microscopic physical history
 -> Gamma_FLRW
 -> rho_hist(a)
 -> p_hist(a)
 -> w_hist(a)
 -> only then compare with cosmological data.
```

No evolving-dark-energy form is built in.  A constant output predicts `w=-1`; a genuine slow microscopic evolution predicts an evolving `w(a)`.

---

## 7. Current observational discipline

The July 30, 2026 DESI DR2 Lyman-alpha full-shape release tightened the high-redshift Alcock-Paczynski constraints and shifted its central value toward Planck-LambdaCDM relative to the previous Ly-alpha BAO-only result.  Therefore this project must not hard-code evolving dark energy as a target.

The comparison protocol is:

```text
1. freeze theory commit and physical history prescription
2. derive rho_hist(a), scalar kernels and photon kernel
3. freeze all dimensionless functions/coefficient outputs
4. apply the existing one-common-scale rule
5. preregister external data/likelihood selections
6. compare to DESI/CMB/lensing/growth data without retuning
```

Reference: DESI DR2 Results IV (2026) and the DESI July 30, 2026 Lyman-alpha full-shape release.

---

## 8. Required physical gates

The unified extension adds four physical blockers to the existing physicalization frontier:

```text
DYNAMICAL_MAXWELL_KERNEL
PHYSICAL_BACKGROUND_COSMOLOGY
PHYSICAL_SCALAR_COSMOLOGY
LENSING_DYNAMICS_CLOSURE
```

They remain `open_physical` until theory-specific evidence exists.

### DYNAMICAL_MAXWELL_KERNEL

Required:

```text
Gamma_AA^(2)
transverse gauge-invariant kernel
massless deconfined photon pole
positive physical residue
Maxwell stiffness Z_A
IR common causal cone with gravity
```

### PHYSICAL_BACKGROUND_COSMOLOGY

Required:

```text
Gamma_FLRW from the same physical history measure
rho_hist(a), p_hist(a)
continuity/Bianchi consistency
stable H(a)
w_hist(a) inferred after derivation
```

### PHYSICAL_SCALAR_COSMOLOGY

Required:

```text
physical scalar Hessian/kernel
Phi and Psi
no ghost/gradient instability in claimed regime
growth response
sound speed and anisotropic stress of effective history sector
```

### LENSING_DYNAMICS_CLOSURE

Required:

```text
same physical Phi/Psi for massive dynamics and lensing
same Weyl potential for deflection/time delay and optical phase
joint dynamics+lensing prediction without an independent lensing fit
```

---

## 9. Falsification conditions

The extension is rejected or narrowed if, after freezing the physical output, any of the following occurs:

```text
photon phase and lensing deflection require different gravitational potentials
M_lens and M_dyn cannot be reconciled with the derived gravitational slip
history component clusters incorrectly or has unacceptable pressure/sound speed
background rho_hist(a) fails expansion-history constraints
scalar response fails CMB/lensing/growth jointly
photon and gravitational IR causal cones disagree beyond allowed limits
Sorkin I3 is predicted nonzero but excluded, or predicted zero and robustly violated
one common scale cannot describe the different sectors
```

No failed gate may be repaired by choosing a new potential, scale or history measure only for the failed observable.

---

## 10. Current claim boundary

At the time this document is introduced:

```text
binary-history interference identities             = finite reference control
point-lens Fermat phase/stationarity bridge         = finite reference control
background rho -> w conservation map                = finite reference control
scalar mu/Sigma/slip bookkeeping                    = finite reference control
BQG physical Maxwell kernel                         = OPEN PHYSICAL
BQG dark-matter-like scalar history response        = OPEN PHYSICAL
BQG dark-energy-like background history response    = OPEN PHYSICAL
BQG joint lensing-dynamics closure                   = OPEN PHYSICAL
external cosmological/lensing confirmation          = NO
```

The purpose of the layer is to make the next calculations harder to fake, not easier to claim.
