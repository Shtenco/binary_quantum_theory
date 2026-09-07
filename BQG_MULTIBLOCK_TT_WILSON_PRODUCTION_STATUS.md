# BQG multi-block TT Wilson production status

Status: **the downstream microscopic five-block bridge is executable on a true coarse subspace; the heavy five-block E/S amplitude producer and the physical connected 1PI bridge remain open.**

No new microscopic dynamics is introduced here.

## 1. Two chains that must remain distinct

```text
microscopic signed gravitational spatial precursor
    G_frozen -> true 5-block P subspace -> Schur -> K_h(k) -> TT
             -> c_micro_spatial_BQG

physical quantum-gravity response
    {C_A} -> projector/history -> Z_phys -> W_phys -> Gamma_phys
          -> Gamma_TT^(2)(omega,k) -> c_BQG_IR
```

The first chain is a constraint-dynamics precursor. It is not automatically the second chain.

## 2. Frozen signed gravitational operator

The spatial precursor uses only the already frozen Hermitian combination

\[
\boxed{
G_{\rm frozen}
=-\frac23 H_E^{\rm sine}-\frac{32}{9}S,
\qquad
S=-\frac{i}{2}(L_{raw}-L_{raw}^\dagger).
}
\]

`R_op` is forbidden in this TT gravitational precursor. No fitted transfer coefficient, mass shift, denominator clipping or phenomenological Wilson term is accepted.

## 3. Important correction: P is a subspace, not 30 basis indices

The actual coarse metric tangents are microscopic **superpositions**. Existing collective production already uses states such as

\[
|u_e\rangle=\frac12\sum_{c\to e}H_c|\Omega\rangle,
\]

so replacing them by 30 coordinate-basis indices changes the retained subspace.

Production therefore now requires

```text
P_vectors : N x 30 complex matrix
```

with one labelled coarse q tangent per column.

The assembler removes only the background component of each column and normalizes it by a positive scalar; it does not rotate the labelled q coordinates. The full overlap matrix is retained:

\[
\boxed{K_P=V^\dagger V.}
\]

`K_P` is allowed to be non-diagonal and is required to have rank 30.

## 4. Correct non-orthogonal Schur/Feshbach map

Let

\[
Q_0=V K_P^{-1/2}
\]

be an orthonormal basis for the retained subspace and let `Q1` span its orthogonal complement. The zero-energy Schur reduction is performed in the orthonormal decomposition:

\[
C_{eff}^{(0)}
=Q_0^\dagger C Q_0
-Q_0^\dagger C Q_1
(Q_1^\dagger C Q_1)^+
Q_1^\dagger C Q_0.
\]

The result is then transformed back to the original labelled q coordinates:

\[
\boxed{
C_{eff}^{(q)}
=K_P^{1/2}C_{eff}^{(0)}K_P^{1/2}.
}
\]

Therefore the normalized-state quadratic Hessian is

\[
\boxed{
K_q=2\,\Re C_{eff}^{(q)}-2C_{00}\,\Re K_P,
}
\]

not `2 Re Ceff - 2 C00 I` unless the retained carrier is orthonormal.

A non-orthogonal known-answer regression recovers the planted raw-q Schur form at relative error

```text
8.84e-15
```

and the planted six-Wilson vector at relative error

```text
1.60e-14.
```

These are infrastructure tests only, not BQG physical coefficients.

## 5. Production input contract

`scripts/bqg_signed_5block_operator_assembler.py` now requires

```text
E_columns         NxN, H_E^sine action columns
S_columns         NxN, Hermitian S action columns
P_vectors         Nx30 true coarse tangent superpositions
background_vector N amplitudes for |Omega>
p_block           30 block labels
p_coord           six q labels per block
block_positions   center + four actual neighboring coarse-cell positions
central_block
metadata_json
```

Optional `C00_E/C00_S` are cross-checks only. The assembler computes

\[
C_{00,E}=\langle\Omega|H_E|\Omega\rangle,
\qquad
C_{00,S}=\langle\Omega|S|\Omega\rangle
\]

directly from the supplied background.

The output records SHA256 hashes of E, S, G, P and `K_P`.

## 6. What the recovered research line already gives us

The frozen `research/bcqg-core-candidate-v1` line contains reusable operator primitives rather than new physics:

- the full L1 barycentric 16-cell habitat: 384 fine tetrahedra / 768 dual links;
- 16 coarse tetrahedral parent blocks, each with four shared-face neighbors;
- exact physical-sine `H_E` active-cone action;
- exact full-E parent-block depth-two workers;
- a six-dimensional intrinsic coarse-edge carrier inside the q4 boundary decomposition;
- complete six-link SU(2) shared-face recoupling bases;
- conservative one-S support wall through coarse-face `j<=6`;
- exact Hermitian Lorentzian primitives implementing `S=-i/2(L_raw-L_raw^dagger)`;
- measured full-rank q-to-metric map `M_hq` with condition number `sqrt(2)`.

The static maximal-symmetric `j=3` coarse-face block is rank one and therefore is **not** used as the production metric carrier.

## 7. Canonical centered five-block patch

The coarse geometry is not fitted to a tetrahedral stencil. It is read from the existing 16-cell boundary. For canonical parent block `0`, the four face-sharing parents are the four one-bit-flip neighbors.

The production carrier is therefore

```text
center parent 0
+ its four actual shared-face parent neighbors
x six labelled q tangents per parent
= 30 retained coarse columns.
```

The existing tetrahedral geometry gate remains only a consistency check on those actual positions.

## 8. Remaining heavy calculation

The real upstream task is now concrete:

```text
construct the five actual L1 parent blocks on one common global basis
 -> construct all 30 labelled coarse tangent superpositions V
 -> keep complete shared-face recoupling sectors
 -> apply full H_E^sine and Hermitian S to every retained vector
 -> collect every target-independent reachable state into Q
 -> continue E/S action on Q until the declared finite support/cutoff closure is complete
 -> serialize complete Hermitian E_columns and S_columns on that common basis
 -> run bqg_signed_5block_operator_assembler.py
 -> run bqg_multiblock_tt_wilson_extractor.py
 -> report c_micro_spatial_BQG or a fail-closed obstruction.
```

No GR, TT, observed-dispersion or Wilson target may be used to prune Q.

## 9. Gapless-mode rule

If a zero mode of the Q block remains coupled to P,

\[
Q_0^\dagger C Q_1u_0\ne0,
\]

the run stops with

```text
GAPLESS_COUPLED_Q_MODE_REQUIRES_PROMOTION
```

and that mode must be promoted to the retained low-energy carrier. No `i eta` regulator is inserted.

## 10. Physical frontier after the microscopic run

Even a successful microscopic six-vector is only

\[
\boxed{\mathbf c_{micro,spatial}^{BQG}}.
\]

The physical prediction remains null until the existing theory supplies

\[
\boxed{
\{C_A\}
\to P_{phys}/\eta
\to Z_{phys}[J_g]
\to W_{phys}[J_g]
\to\Gamma_{phys}[g]
\to\Gamma^{(2)}_{TT}(\omega,\mathbf k)
\to\mathbf c_{BQG}^{IR}.
}
\]

That distinction is now enforced in code rather than left to interpretation.