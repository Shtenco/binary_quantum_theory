# Preregistration — Hermitian-completed full BCQG finite HDA

Status: **frozen before ES/SE/SS results**.

This replaces the unsymmetrized raw-Lorentzian finite channel calculation as the physical falsifier. The earlier `EE/EL/LE/LL` run remains a historical raw-ordering diagnostic and its timeout/result history is retained.

## 1. Physical finite operators

At `beta=hbar=1`:

\[
E_v=H_{E,v}^{sine},
\]

\[
\boxed{
S_v=-\frac{i}{2}(L_{raw,v}-L_{raw,v}^\dagger)
}
\]

is the minimal Hermitian completion of the already declared Lorentzian raw ordering, and

\[
\boxed{
G_v=-\frac23E_v-\frac{32}{9}S_v.
}
\]

No coefficient is fitted to the HDA calculation.

## 2. Exact channel decomposition

Define

\[
EE=E_0E_1-E_1E_0,
\]

\[
ES=E_0S_1-E_1S_0,
\]

\[
SE=S_0E_1-S_1E_0,
\]

\[
SS=S_0S_1-S_1S_0.
\]

Then

\[
\boxed{
[G_0,G_1]
=\frac49EE
+\frac{64}{27}(ES+SE)
+\frac{1024}{81}SS.
}
\]

The weights are fixed algebraically from `a=-2/3`, `c=-32/9`:

```text
EE  = a^2  = 4/9
ES  = ac   = 64/27
SE  = ac   = 64/27
SS  = c^2  = 1024/81.
```

They may not be changed after observing finite results.

## 3. Cutoff walls

Use the already audited hit-depth walls:

```text
EE : Jmax = 5/2
ES : Jmax = 9/2
SE : Jmax = 9/2
SS : Jmax = 13/2.
```

The Hermitian projection does not increase spin support relative to raw `L`/`L^dagger`.

## 4. Route sector

Use only the positive operator-first route normal

\[
R_{op}[N]=\frac12\{N,\sqrt{\hat Q^{ab}\hat P_a\hat P_b}\}.
\]

No expectation-valued metric is allowed in the production finite falsifier.

The generic route block must be completed on every fixed-spin sector reached by `E` or `S`; no diagonal expectation replacement is allowed after geometry change.

## 5. Habitat and regulator sequence

Retain the same frozen nonconstant-lapse/WKB family as the physical sine HDA:

```text
L=48
carrier=8
epsilon = 1/4, 1/8, 1/16, 1/32, 1/64
initial all ten links j=1/2
initial all five K=0.
```

## 6. Acceptance criteria

The final full Hermitian operator is

\[
H_{full}[N]=G[N]+R_{op}[N].
\]

The same pre-existing five-point HDA acceptance bands remain frozen:

```text
p_cross in [0.75,1.25]
p_GG    in [1.75,2.25]
p_joint in [0.75,1.25]
all relative residual sequences strictly decreasing
Delta_joint(1/64) < 0.05.
```

No post-result:

```text
sign flip
coefficient refit
channel subtraction
channel deletion
threshold widening
expectation-first route replacement
```

is allowed.

## 7. Required diagnostics

The finite result must save:

- exact sparse `EE`, `ES`, `SE`, `SS` states;
- signed channel Gram/interference matrix;
- total `[G0,G1]` support/norm/max spin;
- Hermiticity checks for `S0,S1,G0,G1` on every explicitly represented finite block;
- physical basis/volume leakage;
- route-symbol positivity on reached sectors;
- five epsilon values of route-only, mixed, pure-geometry and joint residuals.

## 8. Interpretation rule

A numerical timeout is not a physics failure.

A completed finite FAIL is retained as a falsification of the current ordering/habitat candidate. A PASS strengthens the conditional asymptotic theorem but does not turn the model into an experimentally established theory.
