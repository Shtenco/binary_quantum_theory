# START HERE — canonical BCQG research map

**Current date of the working frontier: 2026-08-16.**

BCQG is a computable candidate quantum-gravity architecture. It is **not experimentally established**.

The repository now has two deliberately separated layers:

```text
v1.2 stable microscopic architecture
        +
v1.3 charged-volume operator-correction addendum
```

The v1.2 Euclidean/operator-first HDA architecture remains reproducible. A collective audit subsequently falsified one narrower finite implementation detail: the historical fixed `q_123` continuation of the four-valent volume to **charged intermediate states** inside the Lorentzian Thiemann word. The corrected finite Lorentzian sector is being recomputed before any new Lorentzian coefficient is promoted.

`README.md` is historical/explanatory and is not the canonical status surface.

## Read these first

1. `THEORY_STATUS.md` — current human status ledger;
2. `BCQG_CANDIDATE_THEORY_V1_3_DRAFT.md` — exact scope of the charged-volume correction;
3. `theory_gates_v13.json` — authoritative addendum for claims changed by the 2026-08-16 audit;
4. `BCQG_CANDIDATE_THEORY_V1_2.md` — reproducible stable microscopic architecture before the addendum;
5. `BCQG_V12_DEEP_CLOSURE_CERTIFICATE.md` — boundary of the frozen-habitat HDA result;
6. `PL_16CELL_HERMITIAN_LORENTZIAN_PREREGISTRATION_V2.md` — corrected 24+24 finite Lorentzian experiment;
7. `COLLECTIVE_GR_UNIVERSALITY_PREREGISTRATION.md` — final collective GR AND-gate protocol;
8. `COLLECTIVE_EFFECTIVE_CONSTRAINT_PRODUCER.md` — direct-data producer contract.

`theory_gates.json` is retained as the v1.2 historical machine ledger. If a Lorentzian/collective status conflicts with `theory_gates_v13.json`, the v1.3 addendum wins.

## Stable production structure

The structural chain remains

```text
binary routes
-> q=2
-> octahedral S2 local link
-> chosen closed orientable PL S3 completion
-> E = H_E^sine
-> K = [V,E]
-> raw Lorentzian Thiemann stack
-> S = -i/2 (L_raw-L_raw^dagger)
-> G = -2/3 E -32/9 S        (beta=hbar=1)
-> positive operator-first R_op
-> H = G + R_op
-> microscopic HDA architecture
-> collective/refinement GR-universality killer.
```

The production route operator is

\[
R_{op}[N]=\frac12\{N,\sqrt{\hat Q^{ab}\hat P_a\hat P_b}\}.
\]

The unique Hermitian projection remains

\[
\boxed{S=-\frac i2(L_{raw}-L_{raw}^\dagger)}.
\]

## 2026-08-16 charged-volume correction

The historical charged covariant implementation extended the local volume using a fixed triple grasping `q_123`. On Gauss `J=0` this represents the same absolute four-valent volume, but on charged intermediate states it selects a preferred local leg.

The negative control found, on the 16-cell homogeneous seed,

```text
old fixed-q123 C_r(V) Frobenius norms:
0.6453707252, 0.6453707252, 0.5163939349, 0
```

The target-independent correction is

\[
\boxed{
Q_{tet}=\frac14\sum_{r=0}^{3}(-1)^r q_{\widehat r},
\qquad
V_{tet}=\sqrt{|Q_{tet}|}
}
\]

with the already frozen zero-aware spectral convention.

The corrected charged volume gives

```text
C_r(V_tet) norms:
0.2513477706186925
0.25134777061869257
0.25134777061869235
0.25134777061869235
```

with slot spread at roundoff scale.

This correction is not fitted to GR. It was forced by local tetrahedral covariance before a complete collective Lorentzian result existed.

## What the correction does NOT change

It leaves the gauge-invariant Euclidean columns unchanged:

```text
K5 H_E^sine:      support 37 -> 37, relative error 0
16-cell H_E^sine: support 82 -> 82, relative error ~1.8e-16
```

and leaves Gauss-state `K=[V,E]` unchanged to about `1e-15`.

Therefore the stable anchors remain:

### Physical Euclidean two-node HDA

```text
p_cross = 1.0056948923496356
p_GG    = 2.007490390559045
p_joint = 1.0076444430189475
Delta_joint(1/64)=0.020030338775070305
```

### Microscopic exhaustive route

```text
reached fixed-spin sectors  33
nonzero power-law sectors   30
numerical-zero sectors       3
p range 0.9997944068141106 .. 0.9999830934452917
max endpoint 1.405841033798129e-05
```

### Strict finite-depth spin wall

\[
\boxed{J_{max}^{safe}=13/2}.
\]

The charged-volume correction changes amplitudes, not the number of fundamental holonomy hits.

## Historical Lorentzian finite numbers — do not promote yet

The following are now **historical regression anchors only**:

```text
L_raw,1body = i 1.3389293521464034 Y
H_corr,1body = -4.760637696520545 Y
historical diagonal-environment Walsh coefficients
historical Lorentzian-route finite coefficients derived from them
```

They were obtained with the old charged `q_123` continuation. The corrected V2 24-forward + 24-adjoint calculation is allowed to agree or disagree. No sign, normalization, cutoff or threshold may be changed after seeing it.

## Direct collective progress

The collective GR verdict is still **INCOMPLETE**, but the producer is no longer only a protocol.

Exact first 16-cell Euclidean Krylov layer:

\[
\boxed{\dim span\{E_v|\Omega_0\rangle\}_{v=0}^{15}=16}.
\]

Measured data:

```text
raw E-column rank              16
sparse reached union          552 states
Gram minimum eigenvalue       3.6545545582254197
Gram condition number         1.5536226967002744
whitened orthogonality defect 4.83e-15
reconstruction error          1.23e-15
seed + E span dimension       17
```

The exact 16-cell XOR translation subgroup is node-transitive:

\[
\boxed{
E_m|\Omega_0\rangle=(-1)^{popcount(m)}U_mE_0|\Omega_0\rangle
}
\]

with exact sparse-support equality and maximum direct amplitude error below `1e-8`.

On every one of the 26 local fixed-spin sectors reached by the production 16-cell Euclidean column, the operator-first route test also passes:

```text
54 intertwiner carriers
3 numerical-zero carriers
p_min=0.99979440681411
p_max=0.9999830934452917
max endpoint=1.405841033797955e-05
min symbol eig=-1.39e-15
```

## Frozen collective probes

Before the first collective `[H,H]` result the lapse family is frozen to the four lowest nonconstant unit-S3 harmonics

\[
N_\mu(x)=x_\mu.
\]

Primary pair: `(0,1)`.
Held-out pairs: `(0,2),(0,3),(1,2),(1,3),(2,3)`.

The refinement fit variable is not a hand-assigned `2^-level`. It is

\[
\boxed{\epsilon_l=h_l/R_l}
\]

from the intrinsic collective metric/regulator.

Static regulator control values are

```text
0.8094352034302834
0.2861785606383325
0.1349058672383880
0.0533262262742036
```

through L0-L3.

## Collective GR killer

A science PASS remains the simultaneous direct result

\[
D_{space}\to3,
\qquad c_{DeWitt}\to\frac12,
\]

\[
(r_G,r_D,r_H,r_{extra})\to(3,3,1,0),
\]

\[
N_{phys}\to2,
\qquad \Delta_{HH}^{collective}\to0.
\]

The AND gate requires at least four direct refinement levels. Classical ADM/DeWitt targets, topology and static metric precursors **cannot fill missing BCQG fields**.

## Immediate production sequence

```text
1. tetrahedral charged-volume audit
2. corrected S_0|Omega_0> from 24 forward + 24 adjoint terms
3. direct held-out S_m XOR covariance check
4. W_E -> W_{E+S+R}
5. depth-2 image/leakage closure
6. direct dynamical D_space
7. raw 6x6 kinetic Hessian -> c_DeWitt_eff
8. direct constraint rank/reducibility
9. collective [H,H] on the frozen S3 harmonic lapses across >=4 levels
10. final GR-universality AND-gate verdict.
```

**Nothing in steps 2-10 may be tuned to make the final GR targets pass.**
