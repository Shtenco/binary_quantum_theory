# ADM family selected by HDA closure

Status: **classical local-ansatz identity + finite spectral regression**.

Take

\[
H_{A,B,c,\Lambda}[N]
=\int d^3x\,N\left[
A\frac{\pi_{ab}\pi^{ab}-c\pi^2}{\sqrt q}
-B\sqrt q(R-2\Lambda)
\right].
\]

Within this local ADM ansatz the bracket is

\[
\boxed{
\{H[N],H[M]\}
=AB\left[D[\beta]+4\left(c-\frac12\right)I[N,M]\right],
}
\]

where

\[
\beta^a=q^{ab}(N\partial_bM-M\partial_bN),
\]

\[
I[N,M]=\int d^3x\,\pi\left(N\nabla^2M-M\nabla^2N\right).
\]

Thus the standard hypersurface-deformation algebra selects

\[
\boxed{c=\frac12,\qquad AB=1.}
\]

The cosmological constant cancels from the bracket, and the ratio `A/B` remains free.  Writing

\[
A=16\pi G,
\qquad
B=(16\pi G)^{-1}
\]

gives the usual GR normalization and automatically satisfies `AB=1`.

## Finite regression

`scripts/adm_hda_parameter_selection_gate.py` uses the independently implemented spectral ADM bracket from `HDA_SAFE_WINDOW_GATE.md`.

Representative results at `L=7`:

- `(A,B)=(2,1/2),(4,1/4),(1/2,2),(3,1/3)` all reproduce the same standard HDA bracket to the underlying `~10^-8` spectral error because `AB=1`;
- `(A,B)=(2,1)` and `(1,2)` give twice the standard structure function;
- `c=0.4` and `c=0.6` give explicit scalar anomalies at the few-percent level on the same state;
- varying `Lambda` from `-10` to `+10` leaves the bracket unchanged at the numerical noise level.

## Interpretation

Within the stated assumptions, closure leaves precisely the familiar classical GR freedoms:

\[
\boxed{G\quad\text{and}\quad\Lambda.}
\]

It does **not** leave a free DeWitt trace coefficient or a free relative kinetic/curvature normalization.

This is the finite-program analogue of the geometrodynamical uniqueness logic: reproducing the hypersurface-deformation algebra strongly constrains the Hamiltonian representation.  It is not a replacement for the full Hojman--Kuchar--Teitelboim theorem, whose hypotheses are broader and must be stated separately.

## Microscopic target

The Peter--Weyl quantum-link theory should not fit Einstein coefficients individually.  In the double regulator-safe window it should instead demonstrate simultaneously

\[
\Delta_{HH}^{Q}\to0,
\qquad
c_{eff}\to\frac12,
\qquad
A_{eff}B_{eff}\to1,
\qquad
\partial_\beta H_{phys}\to0.
\]

If these hold, the leading two-derivative classical Hamiltonian is already forced into the ADM/GR family up to `G` and `Lambda`; the independent Regge--EH--Ward branch then serves as a nontrivial cross-check rather than a coefficient-fitting procedure.
