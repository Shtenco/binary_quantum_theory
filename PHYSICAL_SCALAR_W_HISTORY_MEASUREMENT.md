# Physical scalar W-history cumulant measurement

Status: **production measurement interface closed; theory-specific source-dressed BQG history data still open.**

The scalar algebraic consumer pipeline is already closed from the three physical Ward-source cumulants

\[
G_{QQ},\quad G_{Q\zeta},\quad G_{\zeta\zeta}
\]
through the Legendre inverse, scalar response and pole/stability classifier.

This note fixes the immediately preceding measurement layer: how a source-dressed **physical connected generating functional** is converted into exactly those three cumulants in physical frequency and momentum.

## 1. Legal input

The input is the theory-specific physical connected functional

\[
W_{phys}[J_Q,J_\zeta;\tau,\mathbf r],
\]

where

- `Q` and `zeta` are the certified scalar Ward-source coordinates;
- `tau` is geometric boundary/history time, not heat-flow time and not a constraint spectral variable;
- `r` is a certified physical/coarse geometric separation;
- every source evaluation uses the same history measure, normalization and boundary convention.

The gate explicitly rejects physical promotion if the input is merely raw `Z`, a constraint resolvent, Feshbach data or an uncertified time coordinate.

## 2. Connected derivatives

At each physical separation the target is

\[
G_{ab}^{conn}(\tau,\mathbf r)
=
\frac{\delta^2 W_{phys}}
{\delta J_a\delta J_b}\bigg|_{J=0},
\qquad a,b\in\{Q,\zeta\}.
\]

Two executable routes are supported.

### A. Direct history Hessian

If the history engine already differentiates the connected functional, it supplies

```text
G_QQ
G_Qzeta
G_zetazeta
```

directly at each `(tau,r)`.

### B. Centered source differences

For source steps `h_Q,h_zeta`, the production gate can form

\[
G_{QQ}
\simeq
\frac{W(h_Q,0)-2W(0,0)+W(-h_Q,0)}{h_Q^2},
\]

\[
G_{\zeta\zeta}
\simeq
\frac{W(0,h_\zeta)-2W(0,0)+W(0,-h_\zeta)}{h_\zeta^2},
\]

and

\[
G_{Q\zeta}
\simeq
\frac{
W(h_Q,h_\zeta)-W(h_Q,-h_\zeta)
-W(-h_Q,h_\zeta)+W(-h_Q,-h_\zeta)
}{4h_Qh_\zeta}.
\]

These formulas are exact for a quadratic source dependence and otherwise carry finite-source `O(h^2)` error. Therefore a finite-difference production packet cannot be promoted to physical status until a source-step convergence scan is certified.

## 3. Physical Fourier transform

For an explicitly weighted finite history/geometry sample the frozen discrete convention is

\[
\boxed{
G_{ab}(\omega,\mathbf k)
=
\sum_p w_p
\exp\left(i\omega\tau_p-i\mathbf k\cdot\mathbf r_p\right)
G_{ab}(\tau_p,\mathbf r_p).
}
\]

The quadrature weights are input data. The gate does not silently invent a continuum-volume factor or a lattice normalization.

This is the first place in the scalar production chain where the symbol `omega` may appear, and only when the packet explicitly certifies that `tau` is physical history/boundary time.

## 4. Downstream handoff

Every Fourier mode is emitted with a `BQG_CONNECTED_SCALAR_HISTORY_V1` packet compatible with

```text
scripts/scalar_connected_history_extractor_gate.py
```

and therefore with the already-frozen chain

```text
G_conn
 -> A,B,C
 -> Delta
 -> Psi,Phi
 -> poles/residues/stability.
```

A numeric finite mode grid by itself is not silently fitted to a dispersion law. Pole inference still requires a controlled functional/momentum representation or a preregistered interpolation/continuum analysis.

## 5. Fail-closed requirements

Physical promotion requires all of:

- theory-specific physical history certified;
- input is connected `W`, not raw `Z`;
- physical `tau` certified;
- physical spatial separation certified;
- Ward source insertions certified;
- same history normalization across all source evaluations;
- Legendre-Hessian convention certified;
- frozen conserved probe convention;
- background/common-scale convention frozen for the requested response;
- complete provenance hashes;
- if finite source differences are used, a source-step convergence scan certified.

## 6. Exact boundary

This layer closes

\[
\boxed{
W_{phys}[J_Q,J_\zeta;\tau,\mathbf r]
\longrightarrow
\{G_{QQ},G_{Q\zeta},G_{\zeta\zeta}\}(\omega,\mathbf k)
}
\]

**as an executable measurement contract.**

It does not generate the theory-specific source-dressed BQG history itself. Therefore the remaining physical input is now even sharper:

\[
\boxed{
\text{actual BQG }W_{phys}[J_Q,J_\zeta;\tau,\mathbf r]
}
\]

with its theory-derived boundary/history measure and normalization.

Constraint spectral `z`, Euclidean restricted habitats, local normalized traces and Feshbach resolvents remain forbidden substitutes.
