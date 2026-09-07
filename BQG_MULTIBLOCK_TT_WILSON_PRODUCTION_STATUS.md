# BQG multi-block TT Wilson production status

Status: **the signed microscopic five-block downstream bridge is executable; the actual five-block operator columns and the physical IR six-vector remain open.**

This note separates two calculations that must not be collapsed:

```text
microscopic signed gravitational spatial precursor
    G_frozen -> C_5block -> Schur -> K_h(k) -> TT -> c_micro_spatial_BQG

physical quantum-gravity response
    {C_A} -> projector/history -> Z_phys -> W_phys -> Gamma_phys
          -> Gamma_TT^(2)(omega,k) -> c_BQG_IR
```

The first chain is now fail-closed in code downstream of a completed five-block operator bundle. The second chain is still required before any six-vector is called a physical BQG prediction.

## 1. Frozen gravitational operator

No new microscopic operator is introduced here. The gravitational operator used by the five-block TT precursor is the already frozen Hermitian signed combination

\[
\boxed{
G_{\rm frozen}
=-\frac23 H_E^{\rm sine}-\frac{32}{9}S,
\qquad
S=-\frac{i}{2}(L_{raw}-L_{raw}^\dagger).
}
\]

The route operator `R_op` is **not** part of this gravitational TT precursor. Historical combined HDA/route constraints may contain a separately declared route block, but a direct route contribution may not be renamed the gravitational DeWitt/TT dynamics.

The exact coefficients above are enforced by provenance guards. No fitted transfer coefficient is accepted.

## 2. New executable seam: component columns -> signed G

`scripts/bqg_signed_5block_operator_assembler.py` consumes exact action-column matrices for `H_E^sine` and `S` on one common closed finite basis and forms only the signed operator above.

Required source bundle:

```text
E_columns       NxN, column j = H_E^sine |j>
S_columns       NxN, column j = S |j>
p_indices       30 retained metric-carrier vectors
p_block         five block ids x six q coordinates
p_coord         coordinate ids 0..5
block_positions center + four actual neighboring coarse-cell positions
central_block
C00_E
C00_S
metadata_json
```

Optional:

```text
basis_ids
metric_map
```

The source metadata must declare:

```text
synthetic=false
target_fitting_used=false
basis_closure_complete=true
source_commit=<exact commit>
regulator=<complete cutoff/support declaration>
operator_components=[H_E_sine,S]
route_operator_included=false
component_definitions.H_E_sine=H_E_sine
component_definitions.S=-i/2(L_raw-L_raw_dagger)
```

The assembler rejects route mixing, incomplete basis closure, non-Hermitian component matrices, non-tetrahedral five-block geometry and missing provenance. It records SHA256 hashes of the source bundle and the E/S/G matrices.

Its output metadata freezes

```text
operator_family=frozen_signed_gravitational_constraint
operator_coefficients_exact:
    H_E_sine = -2/3
    S        = -32/9
provenance_level=microscopic_constraint
physical_history_1pi=false
```

## 3. Downstream Schur -> metric -> TT chain

`scripts/bqg_multiblock_tt_wilson_extractor.py` then performs:

1. supplied metric carrier `P` and complement `Q`;
2. exact audit of `QCQ`;
3. rejection of every zero/gapless `Q` mode still coupled to `P`;
4. zero-constraint-energy Schur/Feshbach reduction on the remaining gapped range,

\[
\boxed{
C_{eff}=PCP-PCQ(QCQ)^{+}QCP,
}
\]

where the Moore-Penrose zero on a null subspace is allowed only for exactly uncoupled zero modes;

5. normalized-state Hessian

\[
\boxed{
K_q=2\,\operatorname{Re}C_{eff}-2C_{00}I;
}
\]

6. independently measured q-to-metric map

\[
\boxed{
K_h=M_{hq}^{-T}K_qM_{hq}^{-1};
}
\]

7. actual center plus four-neighbor tetrahedral shell;
8. spatial Fourier/Taylor symbol;
9. deterministic two-polarization TT projection;
10. zero-TT-mass, positive/isotropic leading `k^2`, reciprocity/parity and six-basis closure guards;
11. exact six-observable extraction of the parity-even tetrahedral spatial quartic vector.

## 4. Frozen metric map

The default metric calibration remains the measured L1 map

\[
M_{hq}=\begin{pmatrix}
1/\sqrt{12}&0&0&0&0&1/\sqrt{12}\\
0&1/\sqrt{12}&0&0&1/\sqrt{12}&0\\
0&0&1/\sqrt{12}&1/\sqrt{12}&0&0\\
0&0&1/\sqrt6&-1/\sqrt6&0&0\\
0&1/\sqrt6&0&0&-1/\sqrt6&0\\
1/\sqrt6&0&0&0&0&-1/\sqrt6
\end{pmatrix},
\]

with

\[
\boxed{\operatorname{cond}(M_{hq})=\sqrt2}.
\]

An identity coordinate map is forbidden.

## 5. Exact status of the six-vector

The raw signed-constraint calculation may now emit only

\[
\boxed{
\mathbf c_{\rm micro,spatial}^{BQG}
=(c_1,\ldots,c_6)_{\rm micro,spatial}.
}
\]

The code field is

```text
c_micro_spatial_BQG
```

and the physical field remains

```text
c_BQG_IR = null
```

by construction.

This is intentional. A constraint Schur kernel is not automatically the connected physical 1PI graviton kernel.

The physical vector may be frozen only after

\[
\boxed{
\{C_A\}
\to P_{phys}/\eta
\to Z_{phys}[J_g]
\to W_{phys}[J_g]
\to\Gamma_{phys}[g]
\to\Gamma^{(2)}_{TT}(\omega,\mathbf k).
}
\]

Only the quartic pole data read from that final object may be called

\[
\mathbf c_{BQG}^{IR}.
\]

## 6. What old calculations already supply

The recovered collective/16-cell research line contains several reusable exact primitives:

- the measured six-dimensional metric carrier and `M_hq` calibration;
- the theorem `P G_frozen P = 0` for one homogeneous six-edge gravitational block;
- exact L1 full-E depth-two action `H_B u_e` on a parent block;
- exact 16-cell physical-sine Euclidean source columns;
- direct Hermitian Lorentzian pair workers implementing
  `S=-i/2(L_raw-L_raw^dagger)`;
- target-independent collective boundary/Krylov and Schur-gap protocols;
- exact shared-face `S3` symmetry reduction and tetrahedral neighbor geometry.

These are upstream operator primitives, not free parameters.

## 7. What is still missing upstream

The existing archive does **not** contain the completed common-basis matrices

```text
E_columns
S_columns
```

for all retained and reachable basis vectors of the actual centered spatial patch

```text
one coarse block + its four shared-face neighbors.
```

In particular:

- the local L1 depth-two result is full Euclidean but only one parent block;
- the old 16-cell Euclidean/Lorentzian source workers act on background/source columns, not the complete 30-column five-block metric carrier plus Q closure;
- the nearest-block `S3` theorem fixes the allowed six transfer amplitudes but does not compute their microscopic values;
- no symmetry value or fitted stencil is allowed to fill those amplitudes.

Therefore the remaining expensive producer is concrete:

```text
construct centered five-block glued boundary carrier
 -> globally orthonormalize the 30 metric P vectors
 -> apply H_E^sine and S to every P vector
 -> collect every reachable Q state at the frozen support wall
 -> apply H_E^sine and S to the Q basis until the declared finite closure is complete
 -> serialize complete Hermitian E_columns and S_columns on one common basis
 -> run bqg_signed_5block_operator_assembler.py
 -> run bqg_multiblock_tt_wilson_extractor.py
```

No GR, TT, observed-dispersion or Wilson target may be used to prune this basis.

## 8. Gapless-mode rule

If `QCQ` has a zero mode `u_0` with

\[
PCQ u_0\ne0,
\]

the calculation stops with

```text
GAPLESS_COUPLED_Q_MODE_REQUIRES_PROMOTION
```

and that mode must be promoted to the retained low-energy carrier. The code does not add `i eta`, a mass shift, denominator clipping or a fitted scalar resolvent.

## 9. Infrastructure selftests

The signed-G assembler selftest checks:

- exact coefficients `-2/3` and `-32/9`;
- route-operator rejection;
- Hermiticity detection;
- complete five-block x six-coordinate layout;
- tetrahedral neighbor geometry.

The downstream extractor synthetic known-answer test still recovers its planted six-vector with machine-precision errors. Those planted numbers remain explicitly labelled

```text
INFRASTRUCTURE_SELFTEST_NOT_BQG_EVIDENCE
```

and are not BQG Wilson coefficients.

## 10. Scientific frontier

The shortest honest path is now

```text
UPSTREAM HEAVY CALCULATION
actual closed five-block E/S action-column basis

ALREADY EXECUTABLE
 -> exact signed G
 -> Q-gap audit
 -> zero-energy Schur
 -> normalized K_q
 -> measured M_hq
 -> K_h(k)
 -> TT
 -> c_micro_spatial_BQG

STILL PHYSICALIZATION-OPEN
 -> physical projector/history
 -> connected Z_phys/W_phys
 -> Gamma_phys
 -> physical Gamma_TT^(2)(omega,k)
 -> c_BQG_IR
 -> one common scale
 -> blind external test
```

This is the current bridge. No new microscopic degree of freedom, clock, fitted route amplitude or phenomenological Wilson coefficient has been added.