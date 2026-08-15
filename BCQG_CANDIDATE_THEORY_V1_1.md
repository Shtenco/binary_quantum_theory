# BCQG Candidate Theory v1.1

**Status:** mathematically/computationally specified candidate theory. Not experimentally established.

This document separates the **core candidate**, its **dimensionless predictions**, and extensions that still require scale setting or matter coupling.

---

## 1. Candidate postulates

### P1. Binary route kinematics

Microscopic local route homogeneity satisfies

\[
q+2=2^q,
\]

selecting

\[
\boxed{q=2}.
\]

The local route shell is the octahedral two-sphere

\[
\boxed{\Sigma Q_2\cong S^2}.
\]

### P2. Spatial globalization

BCQG v1.1 uses the minimal 8-vertex flag completion. The seed is the boundary of the 16-cell,

\[
(V,E,F,T)=(8,24,32,16),
\qquad
\beta=(1,0,0,1),
\]

a closed orientable PL `S^3`. Recursive PL refinements preserve the manifold class.

### P3. Quantum geometry

Geometry is carried by an SU(2) Peter-Weyl spin-network sector. The physical Euclidean ordering is

\[
\boxed{H_E^{sine}=(T-T^\dagger)/(2i)},
\qquad
\boxed{K=[V,H_E^{sine}]}.
\]

### P4. Signed Lorentzian completion

The nested Thiemann stack contains five Poisson brackets. With

\[
\{\ ,\ \}\to [\ ,\ ]/(i\hbar),
\]

the universal phase is

\[
\boxed{(1/i)^5=-i}.
\]

The upstream tetrahedral normalization gives

\[
H_E^{phys}=-\frac{2}{3\hbar}E_{raw}.
\]

At `beta=hbar=1`, the signed local geometry generator is frozen as

\[
\boxed{
G_v=-\frac23E_v+\frac{32i}{9}L_{raw,v}.
}
\]

No Lorentzian sign or relative magnitude is tuned against HDA data.

### P5. Quantum route-normal generator

The route normal is a linear positive operator, not a state-dependent expectation map:

\[
\boxed{
R_{op}[N]=\frac12\left\{N,
\sqrt{\hat Q^{ab}\hat P_a\hat P_b}
\right\}.
}
\]

Positivity follows from

\[
\hat Q^{ab}\hat P_a\hat P_b
=\sum_iB_i^\dagger B_i\ge0.
\]

### P6. Hamiltonian constraint

The core constraint is

\[
\boxed{H[N]=G[N]+R_{op}[N]},
\qquad
G[N]=\sum_vN_vG_v.
\]

The continuum target is

\[
\boxed{
[H[N],H[M]]
\longrightarrow
i\hbar D[\sharp_Q(NdM-MdN)].
}
\]

### P7. Continuum trajectory

At fixed safe cutoff the signed operator-first composition is conditionally

\[
\boxed{
\Delta_{full}
=\Delta_{R,op}+O(\epsilon)+O(\epsilon^2)
\to0.
}
\]

For the simultaneous-cutoff candidate trajectory

\[
\boxed{J_{max}\sim\epsilon^{-1/8}},
\]

with the separately frozen polynomial norm envelope,

\[
\boxed{C_{G\times R}/D=O(\epsilon^{3/16})},
\qquad
\boxed{C_{GG}/D=O(\epsilon^{3/8})}.
\]

---

## 2. Already measured candidate constants

```text
Hausdorff-like spatial exponent       d_H = 2.999229782
slice spectral dimension              d_s = 3.004393867
dynamical exponent                    z   = 0.998281156
history spectral dimension            ~ 4.004393867
```

Physical sine two-node HDA:

```text
p_cross = 1.0056948923496356
p_GG    = 2.007490390559045
p_joint = 1.0076444430189475
Delta_joint(1/64)=0.020030338775070305.
```

Operator-first route on the initial exact shared `4x4` sector:

```text
p_R = 0.9999594708960342
Delta_R(1/64)=8.205159710207802e-7.
```

Five genuine `H_E^sine`-reached higher-spin sectors give

```text
p_R in [0.9998813243, 0.9999820816]
endpoint defects in [9.37065e-7, 3.63658e-6].
```

Environment-unbiased raw Lorentzian logical one-body coefficient:

\[
\boxed{
L_{raw,1body}=i\,1.3389293521464034\,Y.
}
\]

At `beta=hbar=1`, the full signed correction on this one-body logical block is

\[
\boxed{H_{corr,1body}=-4.760637696520545\,Y}
\]

in repository structural units.

---

# 3. Core physical predictions

These predictions follow from the candidate core without inventing an absolute energy scale.

## Prediction A — 3+1-dimensional infrared geometry

The continuum/refinement flow must approach

\[
\boxed{d_{space}=3,\qquad z=1,\qquad d_{history}=4}.
\]

Persistent flow to a different limiting dimension or a nonunit dynamical exponent falsifies this branch of BCQG.

## Prediction B — two tensor gravitational degrees of freedom

Conditional on first-class continuum HDA and a nondegenerate three-metric, the DeWitt/HDA uniqueness and Dirac count give

\[
\boxed{2\ \text{local gravitational configuration modes}}.
\]

Thus the infrared sector predicts one massless spin-2 tensor field with two TT helicities and no additional non-decoupling scalar gravitational polarization.

## Prediction C — restoration of relativistic propagation in the infrared

The continuum requires

\[
\boxed{z\to1}.
\]

Therefore microscopic dispersion must disappear under refinement rather than survive as an unsuppressed low-energy tensor Lorentz violation. The present finite `z=0.998281156` is treated as a regulator/refinement value, not as an observed low-energy violation.

## Prediction D — regulator hierarchy of the full constraint algebra

On the declared WKB habitat at fixed safe cutoff,

\[
\boxed{C_{G\times R}/D=O(\epsilon)},
\qquad
\boxed{C_{GG}/D=O(\epsilon^2)}.
\]

The operator-first route-only residual has near-unit measured exponents both before and after genuine spin changes. A direct full finite calculation showing an `O(1)` relative mixed anomaly or an `O(epsilon)` relative pure-geometry anomaly would falsify the current assembly.

## Prediction E — first-order logical Euclidean silence

On the complete all-`j=1/2` logical sector,

\[
\boxed{P H_{E,v}^{sine}P=0}
\]

for both tested nodes separately. First-order logical dynamics in this sector is therefore not generated by the Euclidean block; Euclidean effects enter through leakage/return or higher order.

## Prediction F — signed microscopic orientation field

The phase-completed Lorentzian one-body block is proportional to `Y`. With exact 16-cell orientation

\[
\eta_v=(-1)^{popcount(v)},
\]

it assembles as

\[
\boxed{H_{L,1body}\propto\sum_v\eta_vY_v=16\Sigma}.
\]

At `beta=hbar=1`, the ideal full-correction fixed-orientation mirror-pair coefficient is

```text
-152.34040628865745
```

in structural units. This is not an energy in eV until a physical Hamiltonian/Newton scale is derived.

## Prediction G — global-orientation covariance

Under simultaneous reversal

\[
\eta_v\to-\eta_v,
\qquad
Y_v\to-Y_v,
\]

one has

\[
\boxed{\eta_vY_v\ \text{invariant}}.
\]

The orientation sector is therefore not an arbitrary absolute handedness selected by coordinates.

## Prediction H — operator-first route generates genuine two-node entangling channels

The exact shared two-node square root is not a direct sum of one-node square roots. In the symmetric logical `4x4` construction,

\[
\boxed{
\bar\Omega_2=A I+B(S_0+S_1)-B S_0S_1,
}
\]

where

\[
S=-\frac{\sqrt3}{2}X+\frac12Z.
\]

A representative signed Lorentzian-route cross contains

```text
XI = -0.09539104
ZI = -0.16522213
XX = -0.08261107
XZ = +0.04769552
ZX = -0.14308656
ZZ = +0.08261107.
```

The symmetric construction predicts

\[
\boxed{\|C_{local}\|=\|C_{entangling}\|}.
\]

Naively embedding a one-node cross into the two-node space misses an order-one correlated contribution.

## Prediction I — positivity of the route symbol on physical spin sectors

Five genuine spin-changed sectors pass the positive-semidefinite symbol test. The most negative checked eigenvalue is approximately

```text
-1.07e-14
```

and is consistent with floating-point zero. A robust negative eigenvalue in a correctly constructed physical block would invalidate the positive route-normal assembly.

## Prediction J — Lorentzian logical correlations survive before environment tracing

The successful exact MITM environment calculation was reassembled before the final partial trace. With source node `0`, nodes `3,4` fixed at `K=0`, and neighboring nodes `1,2` varied over `K=0/2`, the diagonal-environment raw Lorentzian operator has coefficient-vector norms

```text
source local             0.33709171624286727
source x node1           0.03631787483605024
source x node2           0.006983526478664483
source x node1 x node2   0.01396705295732858.
```

The dominant pseudoscalar pieces are

\[
\boxed{YI_1I_2=+i\,0.335901403339900},
\]

\[
\boxed{YZ_1I_2=-i\,0.007028617222480},
\]

\[
\boxed{YI_1Z_2=+i\,0.002338130606599},
\]

\[
\boxed{YZ_1Z_2=+i\,0.004676261213198}.
\]

Thus the very clean environment-unbiased one-body `Y` is **not** evidence that the microscopic Lorentzian sector is purely one-body before tracing. The checked diagonal matrix elements contain neighbor and three-body logical correlations.

Using the already frozen `beta=hbar=1` full-correction factor, the corresponding phase-compatible pseudoscalar structural coefficients would be

```text
YII    -> -1.1943161007640883
YZ1I   -> +0.02499063901326094
YIZ2   -> -0.008313353267907534
YZ1Z2  -> -0.016626706535814353
```

for these diagonal components.

**Scope restriction:** the historical workers measured `⟨e|L|e⟩`, not off-diagonal `⟨e'|L|e⟩`. Therefore Prediction J is a tested prediction for the diagonal-environment sector, not yet the complete multi-qubit Lorentzian Hamiltonian.

Evidence: `LORENTZIAN_MULTI_NODE_ENVIRONMENT_CORRELATION.md` and `verification_results/PETER_WEYL_LORENTZIAN_ENVTRACE_WALSH_NODE012.json`.

---

# 4. Conditional / extension predictions

These are not promoted to the gravity core.

## Foam spectrum

If the measured observer-smoothing exponent is identified with a genuine quantum RMS metric fluctuation exponent, the existing bridge gives approximately

\[
P_{\delta g}(k)\propto k^{1.003414}.
\]

This interpretation is conditional; it is not yet a core prediction.

## GW-driven microscopic route resonance

A route/information-mode resonance requires a derived nonzero TT microscopic coupling. The repository contains a candidate mechanism, but that coupling is not yet strong enough to call the resonance a confirmed BCQG prediction.

## Macroscopic mirror/orientation force

The microscopic `Y` field and multi-node correlations do **not** by themselves predict a fifth force, antigravity or a macroscopic mirror force. Such a claim additionally requires

1. a matter source operator;
2. a nonzero matter matrix element;
3. a propagation/range mechanism;
4. a physical scale and Newton normalization;
5. demonstration that the effect survives coarse graining.

---

# 5. Scale setting required for dimensional predictions

BCQG currently determines relative structural coefficients. To convert them to meters, seconds, joules or Newtons one additional physical calibration is required.

A valid scale-setting stage must simultaneously fix at least

```text
microscopic length / area scale;
Hamiltonian energy scale;
Newton coupling in the IR;
normalization of matter sources.
```

The preferred criterion is to match the recovered infrared Einstein-Hilbert/ADM coefficient to the observed Newton constant. Only after that match may structural Lorentzian splittings be converted into absolute physical energies.

---

# 6. Near-term falsifiers

The strongest remaining computational falsifiers are:

1. finish exact `EL`, `LE`, `LL` sparse states and assemble
   \[
   [G_0,G_1]
   =\frac49EE-\frac{64i}{27}(EL+LE)-\frac{1024}{81}LL;
   \]
2. compute the exact full spin-changing `G x R_op` cross on the same habitat;
3. run the frozen five-point final collector and require
   ```text
   p_cross in [0.75,1.25]
   p_GG    in [1.75,2.25]
   p_joint in [0.75,1.25]
   Delta_joint(1/64) < 0.05;
   ```
4. compute off-diagonal multi-node Lorentzian environment blocks and test whether the diagonal correlation hierarchy survives in the complete reduced operator;
5. repeat final HDA tests on independent habitats/WKB carriers;
6. strengthen `Jmax~epsilon^-1/8` toward a uniform joint-limit theorem;
7. perform physical scale setting and confront gravitational-wave/Newtonian observations.

No threshold or signed coefficient may be altered after finite channel results are observed.

---

# Candidate-theory statement

> **BCQG v1.1 is now a fully specified signed operator-first candidate architecture: binary `q=2` kinematics, recursive PL `S^3`, an SU(2) sine-Hermitian Euclidean constraint, a five-bracket signed Lorentzian completion, a positive operator-first route normal, and a conditional full HDA continuum theorem. It makes concrete dimensionless predictions for dimensional flow, tensor degree count, regulator hierarchy, first-order logical selection rules, microscopic orientation structure, two-node entangling route channels, and finite diagonal multi-node Lorentzian correlations. Absolute force/energy predictions are deliberately withheld until Newton/matter scale setting is derived.**
