# Preregistration — signed full Peter-Weyl geometry commutator

Status: **frozen before the first exact `LL` result**.

This is the geometry-only precursor to the final two-node

```text
H_E^sine + (1+beta^2) H_L + R_op
```

HDA. Its purpose is to construct and audit the complete signed geometry commutator before route coupling is added.

No result from the full `LL` channel has been inspected at the time this protocol is committed.

---

## 1. Frozen input

```text
K5 graph
nodes: 0 and 1
all ten links: j=1/2
all five Gauss intertwiners: K=0
beta=1
hbar=1 structural units
zero-aware exact-Q-nullspace volume convention
physical Euclidean ordering H_E^sine=(T-T^dagger)/(2i)
```

---

## 2. Frozen signed geometry operator

The upstream normalization/sign certificates give

\[
H_E^{phys}=-\frac23 H_E^{sine,raw}
\]

and, for the full beta=1 Lorentzian correction,

\[
H^{corr}=\frac{32i}{9}L_{raw}.
\]

Therefore the node geometry operator used in this calculation is

\[
\boxed{
G_v=-\frac23 E_v+\frac{32i}{9}L_v
}
\]

where

```text
E_v = H_E^{sine,raw}_v
L_v = full 24-term epsilon-oriented raw K_sine-K_sine-V node operator.
```

The coefficient/sign is **not** a fit parameter.

---

## 3. Frozen pair-channel decomposition

The exact commutator is decomposed before summation:

\[
[G_0,G_1]
=a^2 C_{EE}+ab C_{EL}+ab C_{LE}+b^2 C_{LL},
\]

with

```text
a=-2/3
b=32 i/9
```

and

\[
C_{EE}=E_0E_1-E_1E_0,
\]

\[
C_{EL}=E_0L_1-E_1L_0,
\]

\[
C_{LE}=L_0E_1-L_1E_0,
\]

\[
C_{LL}=L_0L_1-L_1L_0.
\]

No channel may be removed because it is numerically inconvenient or increases the residual.

---

## 4. Frozen cutoff walls

The cutoffs are selected from operator hit depth before amplitude evaluation.

### EE

The existing physical sine Euclidean two-node gate remains exact at

```text
Jmax=5/2.
```

### EL / LE

Starting from all `j=1/2`, one Euclidean move can add at most two fundamental hits on a link, while one Lorentzian move can add at most six. A sufficient mixed pair wall is therefore

```text
j_in + (2+6)/2 = 1/2 + 4 = 9/2.
```

Freeze

```text
Jmax_mixed=9/2.
```

### LL

The independent `lorentzian_hit_depth_bound.py` gate proves the sufficient full two-node Lorentzian HH wall

```text
Jmax_LL=13/2.
```

This is frozen before evaluation.

No cutoff will be reduced because a smaller one gives a more favorable result.

---

## 5. Frozen sparse thresholds

Reuse the established operator thresholds:

```text
internal Lorentzian structural tolerance = 1e-11
reported/final Gauss sparse prune        = 1e-10
physical basis/volume leakage maximum    = 1e-8
channel recombination relative error     = 1e-9
```

A diagnostic threshold ladder may be reported, but the PASS criteria above will not be changed after result inspection.

---

## 6. Required outputs

The calculation must report separately:

```text
E0, E1 support/norm/max spin
L0, L1 support/norm/max spin
C_EE support/norm
C_EL support/norm
C_LE support/norm
C_LL support/norm
signed weighted channel norms
full [G0,G1] support/norm
max physical leakage
max spin reached in every channel
cache/runtime statistics
```

It must also construct the same final commutator in two ways:

1. weighted sum of the four frozen channels;
2. direct application of `G0G1-G1G0` using the same cached basis actions, if computationally feasible.

If the direct second construction is too expensive, the exact algebraic channel sum remains the production definition and the absence of the duplicate direct computation must be reported rather than silently replaced by an approximation.

---

## 7. PASS / FAIL for this construction gate

This is **not yet the full HDA PASS** because route coupling and the diffeomorphism target are added in the next gate.

Construction PASS requires:

```text
1. E0,E1,L0,L1 are nonzero;
2. all four pair channels are evaluated without cutoff/basis exceptions;
3. all reported coefficients are finite;
4. physical basis/volume leakage < 1e-8;
5. measured max spin does not exceed its preregistered sufficient wall;
6. if direct and channel-summed constructions are both evaluated, their relative difference < 1e-9;
7. no post-hoc sign, relative coefficient, channel subtraction or threshold change.
```

A mathematically exact zero in any individual pair channel is allowed and must be retained. The gate must not require a channel to be nonzero merely for aesthetic reasons.

---

## 8. Next HDA use

After this construction gate, the antisymmetric lapse factor

\[
a_Nd_M-b_Nc_M
\]

and the operator-first route sector are inserted with the already frozen lapse/WKB family.

The full HDA acceptance remains a regulator-scaling statement, not a demand that `[G0,G1]` itself vanish at finite cutoff.

---

## 9. Falsification discipline

If the computation exceeds practical resources, that is recorded as a computational frontier. It is not converted into a PASS.

If a channel fails basis closure, cutoff safety or finite arithmetic, the failure remains in the evidence. No weaker proxy may be relabelled as the exact full geometry commutator.
