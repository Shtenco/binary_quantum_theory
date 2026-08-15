# BCQG v1.2 deep-closure certificate

Date: 2026-08-15

Status: **closed candidate architecture on the frozen finite-depth two-node habitat; collective/physical realization remains conditional**.

This certificate is a compact logical boundary around the current gravity core.  It does not supersede the detailed derivations in `BCQG_CANDIDATE_THEORY_V1_2.md`; it records exactly which arrows are now theorem/finite-evidence complete and which arrows still require new physics or a larger habitat.

## 1. Production constraint

At `beta=hbar=1`:

\[
E_v=\frac{T_v-T_v^\dagger}{2i},
\]

\[
S_v=-\frac{i}{2}(L_{raw,v}-L_{raw,v}^\dagger),
\]

\[
G_v=-\frac23E_v-\frac{32}{9}S_v,
\]

\[
R_{op}[N]=\frac12\left\{N,\sqrt{\hat Q^{ab}\hat P_a\hat P_b}\right\},
\]

and

\[
\boxed{H[N]=G[N]+R_{op}[N].}
\]

The Hermitian projection of the already-defined raw Lorentzian phase is unique as a real-linear projection with Hermitian range and anti-Hermitian kernel, and is the Hilbert-Schmidt closest Hermitian operator.

## 2. Exact finite support

The all-`j=1/2` finite-depth HH habitat has at most 12 fundamental holonomy hits per physical link.  Therefore

\[
\boxed{J_{max}\ge13/2}
\]

is a sufficient exact support wall.  Above it, the spin-truncation remainder for the declared finite-depth calculation is exactly zero.

This removes the former need for an assumed `Jmax(epsilon)` trajectory from the **core frozen-habitat closure**.  Such trajectories remain relevant only when spin, blocking depth or operator depth themselves grow with refinement.

## 3. Operator-first route completeness on the one-step physical support

One physical Euclidean action produces 41 nonzero basis outputs and 33 distinct fixed-spin route sectors.  All 33 have been finite-regressed.  Thirty have measurable residual scaling with

\[
p_R\in[0.999794406814,0.999983093445],
\]

while three close at numerical zero on the five-point epsilon family.

The positive route symbol has also been audited at its singular points.  Across 33 sectors and 25 momentum modes, 24 singular PSD cases occur, yet

\[
P_0(\partial A)P_0\simeq0
\]

and the required Sylvester equation remains solvable to numerical precision.  Hence route zero modes do not introduce a hidden principal-symbol anomaly on the tested support.

## 4. Full HDA composition

For

\[
N=\bar N+\epsilon n,\qquad M=\bar M+\epsilon m,
\]

the pure geometry antisymmetric smear has no zeroth-order term.  In the geometry-route cross the apparent inverse-epsilon piece cancels identically before matrix elements are taken.

Since local `G` is a bounded finite-dimensional operator at the exact support wall and the WKB diffeomorphism target is `O(epsilon^-1)`,

\[
\frac{C_{G\times R}}{D}=O(\epsilon),
\qquad
\frac{C_{GG}}{D}=O(\epsilon^2).
\]

Together with the exhaustive route scaling,

\[
\boxed{\Delta_{full}=O(\epsilon^{\min(p_R,1)})\to0}
\]

on the frozen preregistered habitat.

Doubled-spin parity further splits the residual into orthogonal even/odd sectors, so the convergence cannot be manufactured by cancellation of an odd anomaly against the even diffeomorphism target.

## 5. What the remaining finite ES/SE/SS calculation means

The Hermitian geometry commutator remains preregistered as

\[
[G_0,G_1]
=\frac49EE+\frac{64}{27}(ES+SE)+\frac{1024}{81}SS.
\]

A completed channel-resolved evaluation is still a strong implementation and finite-amplitude falsifier.  It can expose a coding, projection or habitat-specific obstruction.  It is no longer a missing logical arrow in the fixed-habitat asymptotic composition theorem.

## 6. Boundary to general relativity

The step from this controlled quantum habitat to physical GR remains conditional.  A genuine collective continuum must still show, in one common scaling window:

\[
D_{space}\to3,
\qquad c_{DW}\to1/2,
\qquad (r_G,r_D,r_H,r_{extra})\to(3,3,1,0),
\]

\[
A_{eff}B_{eff}\to1,
\qquad N_{phys}^{config}\to2,
\qquad \Delta_{HH}\to0.
\]

This rejects a topological BF fixed point even if its constraints close.

## 7. Scientific verdict

The core can now be called a **closed candidate architecture on its declared frozen habitat** in the precise sense that its operator definition is Hermitian and linear, its finite spin support is exact, its route sector is exhaustively checked on the one-step Euclidean-reached support including singular symbols, and its HDA asymptotic composition follows without tuning a Lorentzian sign or an epsilon-dependent spin cutoff.

It cannot honestly be called a proved theory of nature.  The uniform collective continuum, GR first-class rank, matter/Newton scale setting and experimental tests are separate falsifiable requirements.
