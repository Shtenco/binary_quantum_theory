# Collective route-ground / HDA-probe sector separation theorem

**Status:** exact consequence of the frozen operator-first route definition.  This theorem separates the constant-lapse vacuum/RG scalar calculation from the nonconstant-lapse WKB habitat used to test the hypersurface-deformation algebra.

## 1. Frozen route operator

The production route-normal constraint is

\[
R[N]=\frac12\{N,\Omega\},
\qquad
\Omega(k)=\frac1\epsilon\sqrt{Q^{ab}k_ak_b},
\]

with the positive operator-first symbol

\[
Q^{ab}k_ak_b\ge0.
\]

The sparse-Fourier implementation in `scripts/operator_route_sparse_fourier.py` uses exactly this definition.

## 2. Constant lapse

For the homogeneous scalar constraint use the constant lapse

\[
N=1.
\]

Since multiplication by a constant does not change Fourier mode,

\[
R[1]=\Omega.
\]

At the route-ground mode

\[
k=0
\]

we have identically

\[
Q^{ab}k_ak_b=0,
\]

and therefore

\[
\boxed{
\Omega(0)=0,
\qquad
R[1]|k=0\rangle=0.
}
\]

No expectation value, GR target or regulator fit is used.

Consequently, on the homogeneous six-metric carrier tensored with the route ground state,

\[
P_0=W_gW_g^\dagger\otimes|0\rangle\langle0|,
\]

the already proved geometry selection rule

\[
W_g^\dagger G W_g=0
\]

extends to the complete constant-lapse direct block:

\[
\boxed{
P_0H[1]P_0=0,
\qquad H[1]=G[1]+R[1].
}
\]

Thus the first nontrivial homogeneous vacuum metric scalar on this declared sector is a return/self-energy effect through states outside `P_0`.

## 3. This does NOT remove the route operator from HDA

For a nonconstant lapse

\[
N(x)=\sum_qN_qe^{iqx},
\]

multiplication shifts Fourier momentum.  Even if the input mode is `k=0`, the second half of the anticommutator contains

\[
\Omega(N|0\rangle),
\]

which samples the nonzero modes `q` present in the lapse.

For the frozen WKB HDA carrier the input itself has `k != 0`, so

\[
\Omega(k)\ne0
\]

on every non-null metric direction.

Therefore:

\[
\boxed{
\text{C2 constant-lapse route-ground block: }R[1]=0,
}
\]

but

\[
\boxed{
\text{C3 nonconstant-lapse/WKB HDA probe: route term retained in full.}
}
\]

Deleting `R_op` from C3 would destroy the operator-first structure-function mechanism and is forbidden.

## 4. Gap-theorem scope

Because

\[
\Omega(k)\sim |k|
\]

near `k=0`, the route momentum family is gapless in a continuum momentum limit.  It must therefore **not** be hidden inside the gapped eliminated geometry sector `Q` of the Schur-gap theorem.

The production C2 split is consequently sectorized:

1. fix the homogeneous route ground state `|k=0>` for the constant-lapse vacuum/RG scalar;
2. apply the `Q`-gap/quasilocality theorem only to the internal geometry/Krylov states being eliminated at that fixed route sector;
3. keep the WKB/path carrier as the separate C3 HDA habitat;
4. if a future theory promotes route momentum to a genuine physical propagating field, it must be counted explicitly among low-energy modes rather than removed by the gravitational `Q` gap.

## 5. Physical interpretation

This distinction prevents two opposite errors:

- **false direct metric dynamics:** adding a nonzero arbitrary route momentum to the homogeneous vacuum Hessian and mistaking `Omega(k)` for a gravitational DeWitt coefficient;
- **false HDA simplification:** setting route momentum to zero in the nonconstant-lapse commutator and thereby deleting the very term that generates the structure function.

The same operator is used in both calculations; only the declared physical/probe sector differs.
