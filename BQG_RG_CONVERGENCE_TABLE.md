# Canonical BQG RG convergence table

This file defines the evidence discipline for the first continuum-RG table.

Closed directly from the serial multiplicity-master scan:

\[
j,\quad
m_{22}(j),\quad
\operatorname{spec}A_j,\quad
\gamma_j.
\]

Also recorded:

- exact-pair degeneracy defect;
- twirled \(S_4\) commutator;
- relative size of the boundary-frame twirl correction.

Two columns are intentionally **not** inferred from these data alone:

\[
\eta_j
\]

requires a defined cross-scale transport of the dynamically selected channel,
not subtraction of unrelated eigenvalue lists.

And

\[
\epsilon_j^{\rm sf}
\]

requires the full master comparison with off-channel leakage and positive
master gaps.  Restricting both scales to a single isolated irreducible copy
would leave only scalar operators and could make a relative-rescaling residual
trivially zero.

Therefore the canonical table is filled fail-closed:

| j | m22 | spec A_j | gamma_j | eta_j | epsilon_j^sf |
|---|---:|---|---:|---|---|
| scale | finite | finite | finite | OPEN until transport | OPEN until full master |

This prevents false evidence of continuum convergence.
