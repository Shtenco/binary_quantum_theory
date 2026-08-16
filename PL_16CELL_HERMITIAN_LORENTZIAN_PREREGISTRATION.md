# Exact 16-cell PL-S3 Hermitian Lorentzian amplitude — preregistration

## Purpose

Lift the already validated K5 Thiemann Lorentzian operator to the independent canonical 16-cell PL-S3 regulator without fitting a GR target, sign, amplitude or truncation after seeing the result.

The production Euclidean and Hermitian Lorentzian definitions are

\[
E_v=H_{E,v}^{sine}=\frac{T_v-T_v^\dagger}{2i},
\qquad
K_v=[V_v,E_v],
\]

\[
L_{raw,v}=\sum_{r=0}^{3}\sum_{\pi\in S_3}
\eta_{r,\pi}\;\mathrm{Tr}_{aux}
\left[C_{a}(K)C_{b}(K)C_{c}(V)\right],
\]

where `(a,b,c)` are the three non-omitted local face slots in the order `pi`, and

\[
\boxed{\eta_{r,\pi}=\mathrm{localSign}(v,r)\,\mathrm{sgn}(\pi)}.
\]

For the boundary of a 4-simplex this becomes the historical K5 epsilon orbit multiplied by the independently fixed tetrahedron orientation. No new orientation parameter is introduced.

The physical v1.2 structural Lorentzian block is

\[
\boxed{S_v=-\frac{i}{2}\left(L_{raw,v}-L_{raw,v}^\dagger\right)}.
\]

## Exact adjoint ordering

The component identities are

\[
C(K)_{ij}^\dagger=-C(K)_{ji},
\qquad
C(V)_{ij}^\dagger=C(V)_{ji}.
\]

The two minus signs from the two K legs cancel. Therefore for one ordered raw term

\[
A_{abc}=\sum_{ijk}C_a(K)_{ij}C_b(K)_{jk}C_c(V)_{ki},
\]

its adjoint column is computed directly as

\[
\boxed{
A_{abc}^\dagger=\sum_{ijk}C_c(V)_{ik}C_b(K)_{kj}C_a(K)_{ji}
}.
\]

No numerical matrix inversion is used to construct the dagger.

## Regulator and cutoff

- spatial carrier: boundary of the 16-cell, a closed orientable PL-S3 triangulation;
- source node: `0` for the first amplitude column;
- initial state: all 32 dual links `j=1/2`, all 16 Gauss recoupling labels `K=0`;
- dual plaquettes: complete dual 2-cells from `DualComplex`;
- volume convention: production zero-aware `sqrt(abs(Q))` with the frozen backward-error nullspace threshold;
- single raw Lorentzian edge-spin cutoff: doubled `Jmax2=7`, i.e. `j<=7/2`, inherited from the single-H_L hit-depth wall;
- all 24 forward and all 24 adjoint ordered terms are computed independently;
- exact-zero ordered terms are allowed.

The separate coarse-face support theorem `collective_hda_depth2_support_wall_gate.py` remains the target-independent representation wall for the later block-space calculation. This finite microscopic dual-edge cutoff is only for the exact node-amplitude engine.

## Hard worker acceptance

Every one of 48 workers must satisfy:

1. finite covariant norm and amplitudes;
2. finite scalar-Gauss norm and amplitudes;
3. complete-basis/volume leakage `<1e-8`;
4. scalar closure fraction `>1-1e-10`, with exact zero defined as fraction 1;
5. nonscalar rejected norm `<1e-8`;
6. output dual-edge spin `<=7/2`;
7. frozen PL orientation coefficient is exactly `+1` or `-1`.

No lower bound on the ordered-term norm is imposed.

## Collector

The collector exact-sums the frozen PL coefficients separately:

\[
L=\sum_t\eta_t L_t,
\qquad
L^\dagger=\sum_t\eta_t L_t^\dagger,
\]

and then forms

\[
S=-\frac i2(L-L^\dagger).
\]

Hard collector acceptance requires only:

- exactly 24 passed forward plus 24 passed adjoint workers;
- one unique `(omitted slot, permutation)` orbit in each mode;
- finite combined amplitudes;
- the same expected collective doubled-spin parity as the even-valence 16-cell seed;
- diagonal matrix element `<Omega|S|Omega>` real to numerical tolerance;
- no output beyond the frozen `j<=7/2` engine wall.

`S` is **not required to be nonzero**. Its support, norm, overlap with the E-only Krylov span and later contribution to the collective effective basis are science outputs.

## Non-circularity

Forbidden after the first result:

- changing the 24 orientation signs;
- deleting exact nonzero ordered terms;
- replacing `S` by raw `L` because it gives a more attractive collective result;
- widening leakage/scalar-closure tolerances;
- imposing K5 parity-flip logic on the even-valence 16-cell;
- fitting a Lorentzian normalization to `c_DeWitt=1/2`, rank `(3,3,1,0)`, two TT modes or a desired HDA residual.

The later physical geometry coefficient remains the already frozen v1.2 value

\[
G_v=-\frac23 E_v-\frac{32}{9}S_v.
\]
