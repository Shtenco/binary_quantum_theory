# Exact 16-cell PL-S3 Hermitian Lorentzian amplitude — preregistration V2

## Why V1 is superseded before a science result

The first distributed PL Lorentzian run was launched with the historical charged-state extension of the four-valent volume based on a fixed local `q_123`.  Before any complete 24+24 Lorentzian amplitude was obtained, an independent covariance audit found a preferred-leg obstruction:

- on Gauss `J=0`, the normalized full four-leg oriented grasping is equivalent in absolute volume to `q_123`;
- after one fundamental holonomy, on charged `J=1/2` sectors, that equivalence fails;
- on the 16-cell homogeneous seed the historical covariant volume legs had unequal Frobenius norms and one local slot was identically zero;
- replacing `q_123` by the normalized four-leg tetrahedral operator restores equal nonzero `C_r(V)` norms for all four local slots;
- the same replacement leaves the gauge-invariant `H_E^sine` column unchanged on both the boundary-4-simplex and independent 16-cell regulators.

Therefore V1 jobs/results are retained only as **SUPERSEDED_PRE_RESULT diagnostics**.  The change is forced by a target-independent local tetrahedral covariance test, not by `D_space`, `c_DeWitt`, constraint ranks, TT counting or an HDA residual.

## Correct charged volume

In canonical local-slot orientation define

\[
Q_{\rm tet}
=\frac14\sum_{r=0}^{3}(-1)^r
\,q_{\widehat r},
\]

where `q_hat{r}` is the epsilon-contracted triple of flux generators on the three local legs other than `r`.

The common orientation of the tetrahedral vertex multiplies `Q_tet` by an overall sign and hence drops from

\[
\boxed{V_{\rm tet}=\sqrt{|Q_{\rm tet}|}}.
\]

The factor `1/4` is fixed by Gauss-sector continuity, not fitted: on `J=0` it preserves the already frozen absolute-volume normalization of the previous `q_123` representation.

The same backward-error zero-eigenspace rule as v1.2 is used before `sqrt(abs(.))`.

## Everything else remains frozen

The Euclidean, K and Lorentzian definitions remain

\[
E_v=H_{E,v}^{sine}=\frac{T_v-T_v^\dagger}{2i},
\qquad K_v=[V_{\rm tet,v},E_v],
\]

\[
L_{raw,v}=\sum_{r=0}^{3}\sum_{\pi\in S_3}
\eta_{r,\pi}\;\mathrm{Tr}_{aux}
[C_a(K)C_b(K)C_c(V_{\rm tet})],
\]

\[
\eta_{r,\pi}=\mathrm{localSign}(v,r)\,\mathrm{sgn}(\pi),
\]

and the physical v1.2/v1.3-compatible Hermitian structural block is

\[
\boxed{S_v=-\frac i2(L_{raw,v}-L_{raw,v}^\dagger)}.
\]

No V1 sign, cutoff or acceptance threshold is changed:

- source node `0` first;
- all-j=1/2, all-K=0 16-cell seed;
- `Jmax2=7` for one raw Lorentzian column;
- 24 forward + 24 direct-adjoint ordered terms;
- exact-zero terms allowed;
- physical complete-basis/internal-volume leakage `<1e-8`;
- scalar closure `>1-1e-10`, with exact zero assigned 1;
- nonscalar rejected norm `<1e-8`;
- output spin `j<=7/2`;
- no lower bound on `||S||`.

The primitive fixed-index charge-projection diagnostic is retained for visibility but is not a hard criterion, matching the already validated acceptance-correct Lorentzian wrapper.

## Required preflight

Before a V2 Lorentzian result is promoted, `tetrahedral_charged_volume_audit_gate.py` must pass and show simultaneously:

1. old charged `q_123` preferred-leg negative control;
2. Gauss absolute-volume normalization preservation;
3. exact `H_E^sine` preservation on K5 and 16-cell;
4. four nonzero, equal 16-cell `C_r(V_tet)` matrix norms;
5. complete charged basis reconstruction below `1e-10`.

## Node transport

The independently frozen XOR gate predicts

\[
S_m|\Omega\rangle
=(-1)^{\mathrm{popcount}(m)}U_mS_0|\Omega\rangle.
\]

This may reduce the production cost of all 16 node columns only **after** one direct held-out nonzero-mask `S_m` calculation agrees in exact sparse support and relative amplitude error `<1e-8`.  Until then, XOR transport is a preregistered prediction, not substituted science data.
