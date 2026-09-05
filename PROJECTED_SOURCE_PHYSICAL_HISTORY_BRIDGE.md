# Projected source dressing -> physical scalar history bridge

Status: **integration machinery frozen; theory-specific physical history remains open.**

This layer connects two already-existing parts of the repository without adding a new physical hypothesis:

1. enlarged-master projector/source dressing,
2. the scalar physical `W`-history measurement and Ward-response pipeline.

The legal order is

\[
\mathbb M
\to P_{phys}\text{ / controlled near-zero rigging limit}
\to B^\dagger P_{phys}B
\to \bar O_Q,\bar O_\zeta
\to Z_{phys}[J_Q,J_\zeta;\Delta t_{rel},\mathbf r]
\to W_{phys}
\to G_{QQ},G_{Q\zeta},G_{\zeta\zeta}
\to (A,B,C)
\to \Gamma^{(2)}_{scalar}.
\]

## Separation of regulator and physical time

The master heat depth

\[
\tau_{heat}
\quad\text{in}\quad e^{-\tau_{heat}\mathbb M}
\]

is a projector/rigging regulator only.

The physical history separation

\[
\Delta t_{rel}
\]

must be independently derived or frozen by the boundary/relational history construction. Only this quantity may be Fourier-conjugate to physical `omega`.

Therefore

\[
\boxed{\tau_{heat}\ne\Delta t_{rel},\qquad z_{constraint}\ne\omega_{physical}.}
\]

The integration gate explicitly feeds a converged projected-source Hessian into the downstream scalar history schema with physical-time flags disabled. The data contract is accepted, but physical interpretation is rejected. This is a required negative control.

## Reused upstream controls

The branch reuses three existing executable contracts from the earlier physical-scalar-kernel programme:

- `scripts/boundary_projector_source_dressing_gate.py` — enlarged projector before boundary compression and source whitening;
- `scripts/bqg_physical_history_adapter_gate.py` — finite constraint-family to existing source/history stack regression;
- `scripts/near_zero_rigging_limit_gate.py` — non-arbitrary asymptotic low-sector separation and negative controls.

All three remain controls. None is promoted to a BQG physical-history result.

## Integration gate

`scripts/projected_source_history_bridge_gate.py` verifies:

- projected source dressing remains reproducible;
- the finite history adapter remains reproducible;
- the near-zero rigging-limit theorem/control remains reproducible;
- static projected covariance cannot become a physical frequency response;
- an independently certified physical-history packet is accepted by the same downstream `BQG_PHYSICAL_SCALAR_W_HISTORY_V1` interface.

## What remains physically open

After this seam is frozen, the missing BQG object is no longer an algebraic consumer. It is the actual source-dressed connected physical history

\[
\boxed{
W_{BQG}[J_Q,J_\zeta;\Delta t_{rel},\mathbf r]
}
\]

on a certified exact or regulator/refinement-controlled physical projector/history sequence.

That production object must determine, from the same frozen history measure,

\[
G_{QQ},\quad G_{Q\zeta},\quad G_{\zeta\zeta}
\]

and the homogeneous restriction

\[
\Gamma_{FLRW}[a,N].
\]

The following gates therefore remain open until actual theory-specific data exist:

- `PHYSICAL_PROJECTOR_HISTORY`;
- `CONNECTED_INTERBLOCK_HISTORY`;
- `PHYSICAL_BQG_SCALAR_KERNEL`;
- physical `Phi`, `Psi`, `mu`, `Sigma`;
- physical `rho_hist`, `p_hist`, `w_hist`.

## Forbidden shortcuts

- master heat depth -> physical time;
- Feshbach/constraint `z` -> physical `omega`;
- maximally mixed projected positive control -> cosmological vacuum;
- equal-history symmetrized covariance -> separated-time propagator;
- background-by-background normalization of `Z[a;0]`;
- separate source renormalizations for dynamics and lensing.

A GREEN integration result freezes only the interface and no-shortcut logic. It is not a dark-matter or dark-energy prediction.
