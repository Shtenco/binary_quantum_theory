# Frozen collective constraint-rank protocol

## Purpose

The collective GR killer requires

\[
(r_G,r_D,r_H,r_{extra})\to(3,3,1,0)
\]

and no surviving second-class sector.  Singular-value thresholds and class-overlap conventions must therefore be frozen **before** direct collective generator Jacobians are inspected.

## Common whitened tangent metric

All generator columns are represented in the same target-independent Gram-whitened effective block basis `W_l`.  If a raw state/operator image is `x`, its tangent coordinate is

\[
\xi=W_l^\dagger x.
\]

No class is given its own fitted norm.

## Generator classes

At one declared nondegenerate background construct raw tangent matrices

```text
G = [G_1, G_2, G_3]
D = [D_1, D_2, D_3]
H = [H_1]
X = [all additional candidate/null generator directions found by the frozen producer]
```

The columns may contain multiple spatial probes before local/block reduction, but the reduction prescription must be identical on every refinement level.

## Sequential independent ranks

To avoid counting the same tangent direction in two named classes:

1. `r_G = rank(G)`;
2. let `P_G` be the orthogonal projector onto `span(G)` and set `D_perp=(I-P_G)D`; then `r_D=rank(D_perp)`;
3. let `P_GD` project onto `span(G,D)` and set `H_perp=(I-P_GD)H`; then `r_H=rank(H_perp)`;
4. let `P_GDH` project onto `span(G,D,H)` and set `X_perp=(I-P_GDH)X`; then `r_extra=rank(X_perp)`.

The full independent first-class candidate rank is also reported directly from `[G,D,H,X]` as a consistency check.

A GR-like result must have

\[
\boxed{(r_G,r_D,r_H,r_{extra})=(3,3,1,0)}
\]

and full independent rank 7.

## Frozen SVD tolerance

For a matrix with singular values `sigma_1>=...`, define relative rank at

\[
\tau=10^{-8}
\]

by counting

\[
\sigma_i/\sigma_1>\tau.
\]

The primary science threshold is therefore

```text
relative_SVD_rank_tolerance = 1e-8
```

and may not be changed after viewing the refinement trend.

A mandatory robustness scan is performed at

```text
1e-7, 1e-8, 1e-9.
```

A rank component may count as a collective GR PASS only if the target rank is identical at all three thresholds on the two finest preregistered levels.  All raw singular values are stored.

## Reducibility and second-class guard

A rank-7 tangent span alone is insufficient.  The producer must separately report:

1. reducibility/null relations among named generators;
2. the projected commutator/Poisson matrix of the independent constraints on the same background;
3. any second-class rank `r_secondclass` after the first-class closure relations are removed using a prescription frozen before the result.

The collective GR killer requires

\[
\boxed{r_{secondclass}=0}.
\]

No numerically small direction may be deleted solely because removing it improves `N_phys`.

## Physical-mode count

In the canonical connection/flux phase-space count used by the killer,

\[
N_{phys}=\frac{18-2r_{FC}-r_{SC}}{2},
\]

where

\[
r_{FC}=r_G+r_D+r_H+r_{extra}.
\]

Thus the GR target

\[
(r_G,r_D,r_H,r_{extra},r_{SC})=(3,3,1,0,0)
\]

implies

\[
\boxed{N_{phys}=2}.
\]

This mode count is a derived check, not an independently fitted target.

## Failure policy

- target rank appears only at `1e-8` but not `1e-7/1e-9` -> **FAIL/UNSTABLE**, not PASS;
- extra independent null/gauge direction survives -> `r_extra>0`, FAIL;
- named Gauss/diffeomorphism/Hamiltonian columns overlap so sequential ranks are below `(3,3,1)` -> FAIL;
- second-class rank nonzero -> FAIL;
- insufficient effective-basis dimension or large projection leakage -> **INCOMPLETE**, not a rank result.
