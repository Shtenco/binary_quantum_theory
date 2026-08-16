# BCQG Candidate Theory v1.3 — operator-correction draft

**Status:** research draft; not experimentally established.  This document does not replace the reproducible v1.2 microscopic certificate until the corrected Lorentzian finite rerun and canonical ledger sync are complete.

## 1. What survives unchanged from v1.2

The following parts of the candidate are unchanged by the 2026-08-16 charged-volume audit:

\[
q=2\to \text{chosen closed orientable PL }S^3,
\]

\[
E_v=H_{E,v}^{sine}=\frac{T_v-T_v^\dagger}{2i},
\]

operator-first

\[
R_{op}[N]=\frac12\{N,\sqrt{\hat Q^{ab}\hat P_a\hat P_b}\},
\]

and the finite-depth representation wall / HDA composition architecture on the declared microscopic habitat.

The exact audit verifies that replacing the historical charged-state volume continuation by the tetrahedral completion leaves both `H_E^sine` and the Gauss-state `K=[V,E]` columns unchanged on the K5 control and the independent 16-cell PL-S3 carrier to machine precision.

Thus v1.3 is **not** a new Euclidean theory and does not reopen the already tested operator-first route construction.

## 2. The defect found by the collective audit

The historical magnetic/covariant Lorentzian implementation represented the four-valent volume using one fixed triple grasping `q_123` even after holonomy hits had moved the source node into a charged total-spin sector.

For a Gauss `J=0` four-valent intertwiner this is harmless: closure relates the four triple graspings and the absolute volume is unchanged up to the common orientation normalization.

For charged `J!=0` intermediate states closure no longer permits selecting one triple as a tetrahedrally symmetric continuation.

The independent negative control gives, for example,

```text
charged spins       ||q123||       ||Q_tet||    best scalar residual
(0,1,1,1), J=1/2      0             0.6123724        1
(2,1,1,1), J=1/2      1             3.0618622        0.5773503
```

and on the 16-cell homogeneous seed the old covariant volume-leg norms were

```text
0.6453707252, 0.6453707252, 0.5163939349, 0
```

so one local slot was artificially preferred/null.

This is a target-independent tetrahedral-covariance failure, discovered before any complete collective PL Lorentzian science result.

## 3. v1.3 charged-volume completion

In canonical local-slot orientation define

\[
\boxed{
Q_{tet}=\frac14\sum_{r=0}^{3}(-1)^r q_{\widehat r}
}
\]

and

\[
\boxed{V_{tet}=\sqrt{|Q_{tet}|}}.
\]

The common vertex orientation multiplies `Q_tet` by a sign and therefore drops from the absolute volume.

The factor `1/4` is fixed by Gauss-sector continuity, not GR fitting.  On all tested nontrivial `J=0` blocks it reproduces the old absolute volume with worst relative error at roundoff scale.

The production zero-aware spectral convention is retained unchanged.

On the same 16-cell charged seed the corrected four `C_r(V_tet)` Frobenius norms are

```text
0.2513477706186925
0.25134777061869257
0.25134777061869235
0.25134777061869235
```

with slot spread about `2.2e-16` and complete-basis leakage about `4.4e-16`.

## 4. Euclidean invariance under the correction

The corrected charged continuation is invisible to the fully contracted gauge-invariant Euclidean operator at the tested anchors:

```text
K5 H_E^sine:
  support 37 -> 37
  norm 2.1712581763270546 -> 2.1712581763270546
  relative error 0

16-cell H_E^sine:
  support 82 -> 82
  norm 2.144278042516496 -> 2.144278042516496
  relative error ~1.8e-16

K5 K=[V,E] on Gauss seed:
  support 37 -> 37
  relative error ~1.2e-15

16-cell K=[V,E] on Gauss seed:
  support 82 -> 82
  relative error ~1.5e-15
```

Therefore the correction is localized to charged/intermediate volume and generalized Lorentzian composition.

## 5. Lorentzian definition

The operator word is unchanged except that every intermediate volume uses `V_tet`:

\[
K_v=[V_{tet,v},E_v],
\]

\[
L_{raw,v}=\sum_{r,\pi}\eta_{r,\pi}
\operatorname{Tr}_{aux}[C_a(K)C_b(K)C_c(V_{tet})],
\]

\[
\eta_{r,\pi}=localSign(v,r)\,sgn(\pi).
\]

The unique Hermitian projection remains

\[
\boxed{S_v=-\frac i2(L_{raw,v}-L_{raw,v}^\dagger)}.
\]

At `beta=hbar=1` the structural geometry normalization remains

\[
\boxed{G_v=-\frac23E_v-\frac{32}{9}S_v}.
\]

The coefficient is not refitted to any collective or GR observable.

## 6. Historical finite Lorentzian numbers

Until the corrected 24-forward + 24-adjoint calculation passes its preregistration, the following are **historical regression anchors, not v1.3 predictions**:

```text
L_raw,1body = i 1.3389293521464034 Y
H_corr,1body = -4.760637696520545 Y
old diagonal-environment Walsh coefficients
old finite Lorentzian-route coefficients derived from that raw block
```

A corrected result is allowed to agree or disagree.  No threshold, orientation sign, normalization or exact-zero rule may be changed after the new result is inspected.

## 7. Corrected finite experiment

The preregistration is

`PL_16CELL_HERMITIAN_LORENTZIAN_PREREGISTRATION_V2.md`.

It requires:

- 24 forward and 24 direct-adjoint terms;
- exact-zero ordered terms allowed;
- one-L spin wall `j<=7/2`;
- physical complete-basis/internal-volume leakage `<1e-8`;
- scalar closure `>1-1e-10` unless exact zero;
- nonscalar rejection `<1e-8`;
- no lower bound on `||S||`.

The V2 collector rejects any old-q123 artifact by provenance.

## 8. Collective progress already independent of this rerun

The collective GR AND gate remains `INCOMPLETE`, but direct non-Lorentzian progress is now substantial:

\[
\dim span\{E_v|\Omega_0\rangle\}_{v=0}^{15}=16,
\]

with a positive-definite Gram matrix and condition number about `1.55362`.

The sparse reached union has 552 Peter-Weyl states and gives a preliminary exact `seed+E` embedding dimension 17.

The 16-cell XOR subgroup is node-transitive and the exact Euclidean amplitudes satisfy

\[
E_m|\Omega_0\rangle=(-1)^{popcount(m)}U_mE_0|\Omega_0\rangle
\]

with exact support equality and maximum direct amplitude defect below `1e-8`.

The operator-first route test passes all 26 fixed-spin sectors reached by the exact production Euclidean column on the first collective habitat.

The collective lapse family and refinement scale are frozen before any collective HDA measurement:

\[
N_\mu(x)=x_\mu,\qquad
\epsilon_l=h_l/R_l.
\]

## 9. Current science frontier

The next mandatory chain is

```text
corrected tetrahedral charged-volume audit
-> corrected S_0|Omega_0>
-> direct held-out S_m XOR covariance test
-> W_{E+S+R}
-> target-independent depth-2 closure/leakage
-> direct D_space_metric
-> raw 6x6 kinetic Hessian -> c_DeWitt_eff
-> direct constraint rank/reducibility
-> collective [H,H] on >=4 refinement levels
-> GR universality AND-gate verdict.
```

No target control may populate a missing direct BCQG science field.

## 10. Status statement

> **v1.3 is a narrowly scoped operator-correction draft: the microscopic Euclidean/operator-first HDA architecture survives, while the finite Lorentzian amplitudes are being recomputed with the unique target-independent four-leg tetrahedral volume continuation required by charged-sector covariance.  The collective GR verdict remains INCOMPLETE until direct refinement data satisfy the preregistered AND gate.**
