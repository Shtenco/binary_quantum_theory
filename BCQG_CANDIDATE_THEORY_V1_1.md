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

BCQG v1.1 uses the minimal flag completion of the local shell. The seed is the boundary of the 16-cell,

\[
(V,E,F,T)=(8,24,32,16),
\]

with

\[
\beta=(1,0,0,1),
\]

so the microscopic spatial seed is a closed orientable PL `S^3`. Recursive PL refinements preserve the manifold class.

### P3. Quantum geometry

Geometry is carried by an SU(2) Peter-Weyl spin-network sector with flux, volume and holonomy operations. The physical Euclidean ordering is

\[
\boxed{H_E^{sine}=(T-T^\dagger)/(2i)}.
\]

The covariant extrinsic-curvature generator is

\[
\boxed{K=[V,H_E^{sine}]}.
\]

### P4. Signed Lorentzian completion

The exact nested Thiemann stack has five Poisson brackets. With

\[
\{\ ,\ \}\to [\ ,\ ]/(i\hbar),
\]

the universal phase is `(1/i)^5=-i`.

The upstream tetrahedral normalization gives

\[
H_E^{phys}=-\frac{2}{3\hbar}E_{raw}.
\]

At `beta=hbar=1`, the signed local geometry generator is therefore frozen as

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

The frozen two-node/core form is

\[
\boxed{
H[N]=G[N]+R_{op}[N]
}
\]

with

\[
G[N]=\sum_vN_vG_v.
\]

The continuum target is the hypersurface-deformation algebra

\[
\boxed{
[H[N],H[M]]
\longrightarrow
i\hbar D[\sharp_Q(NdM-MdN)].
}
\]

### P7. Continuum trajectory

At fixed safe cutoff the signed operator-first HDA has the conditional asymptotic composition

\[
\Delta_{full}
=\Delta_{R,op}+O(\epsilon)+O(\epsilon^2)
\to0.
\]

For the simultaneous-cutoff candidate trajectory,

\[
\boxed{
J_{max}\sim\epsilon^{-1/8},
}
\]

with the declared norm envelope,

\[
C_{G\times R}/D=O(\epsilon^{3/16}),
\qquad
C_{GG}/D=O(\epsilon^{3/8}).
\]

---

## 2. Already measured candidate constants

The present frozen calculations give

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

Operator-first route on the initial exact 4x4 sector:

```text
p_R = 0.9999594708960342
Delta_R(1/64)=8.205159710207802e-7.
```

On five genuine `H_E^sine`-reached higher-spin sectors:

```text
p_R in [0.9998813243, 0.9999820816]
endpoint defects in [9.37065e-7, 3.63658e-6].
```

Raw Lorentzian logical one-body coefficient:

\[
\boxed{
L_{raw,1body}=i\,1.3389293521464034\,Y.
}
\]

At `beta=hbar=1`, the full signed Lorentzian correction on this logical block is

\[
\boxed{
H_{corr,1body}=-4.760637696520545\,Y
}
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

The current finite estimates are already close to those values. Persistent flow to a different limiting dimension or a nonunit dynamical exponent falsifies this branch of BCQG.

## Prediction B — two tensor gravitational degrees of freedom

Conditional on first-class continuum HDA and a nondegenerate three-metric, the DeWitt/HDA uniqueness and Dirac count give

\[
\boxed{2\ \text{local gravitational configuration modes}}.
\]

Thus the infrared gravitational sector predicts one massless spin-2 tensor field with two TT helicities and **no additional non-decoupling scalar gravitational polarization**.

A robust extra scalar gravitational wave mode in the same infrared sector would falsify the minimal core.

## Prediction C — restoration of relativistic propagation in the infrared

The candidate continuum requires

\[
\boxed{z\to1}.
\]

Therefore the minimal core predicts no finite infrared Lorentz-violating tensor dispersion once the continuum limit is reached. Any microscopic dispersion must vanish under the refinement/continuum flow rather than survive as an unsuppressed low-energy effect.

This is a null prediction; the current finite `z=0.998281156` is treated as a regulator/refinement value, not a claim of measured low-energy Lorentz violation.

## Prediction D — regulator hierarchy of the full constraint algebra

On the declared WKB habitat at fixed safe cutoff,

\[
\boxed{
C_{G\times R}/D=O(\epsilon),
\qquad
C_{GG}/D=O(\epsilon^2).
}
\]

The operator-first route-only residual has near-unit measured exponents both before and after genuine spin changes.

Therefore a direct full finite calculation that exhibits an `O(1)` relative mixed anomaly or an `O(epsilon)` relative pure-geometry anomaly would falsify the present ordering/assembly even if individual one-body amplitudes look correct.

## Prediction E — first-order logical Euclidean silence

On the complete all-`j=1/2` logical sector,

\[
\boxed{P H_{E,v}^{sine}P=0}
\]

for both tested nodes separately.

Consequently first-order dynamics internal to this logical sector is not generated by the Euclidean block. Euclidean effects enter through leakage/return or higher order, while the nonzero first-order logical chirality channel is Lorentzian.

## Prediction F — a signed microscopic orientation field

The phase-completed Lorentzian one-body block is proportional to `Y`. With exact 16-cell orientation

\[
\eta_v=(-1)^{popcount(v)},
\]

it assembles as

\[
\boxed{
H_{L,1body}\propto\sum_v\eta_vY_v=16\Sigma.
}
\]

Thus at fixed global orientation the core predicts a microscopic field conjugate to staggered orientation/chirality.

For `beta=hbar=1`, the ideal full-correction mirror-pair coefficient is

```text
-152.34040628865745
```

in structural units.

This number is **not an energy in eV** until the microscopic Hamiltonian scale is fixed.

## Prediction G — global-orientation covariance

Under simultaneous reversal of the global cell orientation and the local chirality variable,

\[
\eta_v\to-\eta_v,
\qquad
Y_v\to-Y_v,
\]

so

\[
\boxed{\eta_vY_v\ \text{is invariant}}.
\]

The orientation term therefore does not represent an arbitrary absolute handedness chosen by coordinates. A calculation that changes the physical spectrum merely by relabelling/reversing the entire frame would violate the candidate covariance.

## Prediction H — operator-first route generates genuine two-node entangling geometry channels

The exact shared two-node route square root is not equal to a direct sum of one-node square roots. In the logical `4x4` block its angular average factorizes as

\[
\boxed{
\bar\Omega_2=A I+B(S_0+S_1)-B S_0S_1,
}
\]

where

\[
S=-\frac{\sqrt3}{2}X+\frac12Z.
\]

For the signed Lorentzian node-0 cross this produces local and entangling components. Numerically the representative coefficients are approximately

```text
XI = -0.09539104
ZI = -0.16522213
XX = -0.08261107
XZ = +0.04769552
ZX = -0.14308656
ZZ = +0.08261107.
```

The model predicts

\[
\boxed{
\|C_{local}\|=\|C_{entangling}\|
}

for this symmetric two-node logical construction. Naively embedding the one-node cross into the two-node space misses an order-one correlated contribution.

This is one of the sharpest microscopic dimensionless predictions currently available.

## Prediction I — positivity of the route symbol on physical spin sectors

Because `R_op` is defined from a positive spectral square root, checked physical sectors must have nonnegative route symbols up to numerical roundoff. Five genuine spin-changed sectors pass this test; the most negative measured eigenvalue is approximately

```text
-1.07e-14
```

and is consistent with zero numerical error.

A robust negative eigenvalue on a correctly constructed physical block would invalidate the positive route-normal definition or the flux-metric assembly.

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

A route/information-mode resonance requires a derived nonzero TT microscopic coupling. The repository contains a candidate mechanism, but the coupling has not been derived strongly enough for this to be called a confirmed BCQG prediction.

## Macroscopic mirror/orientation force

The nonzero microscopic `Y` field does **not** by itself predict a fifth force, antigravity or a macroscopic mirror force. Such a prediction additionally requires

1. a matter source operator;
2. a nonzero matter matrix element;
3. a propagation/range mechanism;
4. a physical scale and Newton normalization;
5. demonstration that the effect survives coarse graining.

Until those are derived, the candidate predicts only the microscopic signed orientation field above.

---

# 5. Scale setting required for dimensional predictions

BCQG currently determines relative structural coefficients. To convert them to meters, seconds, joules or Newtons one additional physical calibration is required.

A valid scale-setting stage must simultaneously fix at least:

```text
microscopic length / area scale;
Hamiltonian energy scale;
Newton coupling in the IR;
normalization of matter sources.
```

The preferred criterion is not to choose these independently: match the coefficient of the recovered infrared Einstein-Hilbert/ADM Hamiltonian to the observed Newton constant. Only after that match may the structural Lorentzian splitting be converted into an absolute physical energy.

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
4. repeat the final PASS/FAIL on independent habitats and WKB carriers;
5. strengthen the conditional `Jmax~epsilon^-1/8` path toward a uniform joint-limit theorem;
6. perform physical scale setting and then confront gravitational-wave/Newtonian observations.

No threshold or signed coefficient may be altered after the finite channel results are observed.

---

# Candidate-theory statement

> **BCQG v1.1 is now a fully specified signed operator-first candidate architecture: binary `q=2` kinematics, recursive PL `S^3`, an SU(2) sine-Hermitian Euclidean constraint, a five-bracket signed Lorentzian completion, a positive operator-first route normal, and a conditional full HDA continuum theorem. It makes concrete dimensionless predictions for dimensional flow, tensor degree count, regulator hierarchy, first-order logical selection rules, microscopic orientation structure and two-node entangling route channels. Absolute force/energy predictions are deliberately withheld until Newton/matter scale setting is derived.**
