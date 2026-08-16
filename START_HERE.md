# START HERE — canonical BCQG v1.2 research map

The repository contains several historical generations. **Current production definitions live in v1.2; older raw-Lorentzian and joint-cutoff files are retained as provenance/extension controls, not competing canonical Hamiltonians.**

Current integrated theory:

```text
BCQG Candidate Theory v1.2
```

Status: **candidate quantum-gravity architecture with a cutoff-saturated two-node HDA theorem on the frozen habitat; not experimentally established.**

`README.md` is an explanatory/historical tutorial and contains older extension language. It is **not** the canonical status surface. Where README and the v1.2 files disagree, v1.2 wins.

## Canonical files

Read in this order:

1. `BCQG_CANDIDATE_THEORY_V1_2.md` — detailed canonical theory and scope;
2. `BCQG_CORE_CANDIDATE_V1_2.md` — compact production definition;
3. `BCQG_V12_DEEP_CLOSURE_CERTIFICATE.md` — exact boundary between frozen-habitat closure and remaining continuum physics;
4. `BCQG_V12_PREDICTIONS.md` — falsifiable structural/conditional prediction ledger;
5. `COLLECTIVE_GR_UNIVERSALITY_PREREGISTRATION.md` — frozen next-stage AND gate for collective GR emergence;
6. `COLLECTIVE_EFFECTIVE_CONSTRAINT_PRODUCER.md` — non-circular direct-data producer contract;
7. `collective_gr_measurement_template.json` — direct collective measurement schema;
8. `THEORY_STATUS.md` — human status ledger;
9. `theory_gates.json` — machine-readable obligations;
10. `LORENTZIAN_HERMITIAN_COMPLETION.md` — why full `L_raw` must be Hermitian-completed;
11. `LORENTZIAN_HERMITIAN_PROJECTION_UNIQUENESS.md` — uniqueness of the minimal projection once `L_raw` is fixed;
12. `ROUTE_OPERATOR_KERNEL_SAFETY.md` — kernel-safe Sylvester theorem for singular positive route symbols;
13. `PETER_WEYL_HERMITIAN_FULL_HDA_PREREGISTRATION.md` — frozen physical finite-channel falsifier;
14. `verification_results/BCQG_V12_CUTOFF_SATURATED_HDA.json` — cutoff-saturated HDA certificate;
15. `verification_results/PETER_WEYL_OPERATOR_ROUTE_ALL_REACHED.json` — exhaustive 33-sector route regression;
16. `verification_results/OPERATOR_ROUTE_KERNEL_SAFETY.json` — exhaustive singular-symbol audit;
17. `PETER_WEYL_TWO_NODE_SINE_HDA_RESULT.md` — preregistered Euclidean sine HDA PASS;
18. `PETER_WEYL_LORENTZIAN_ENVTRACE_RESULT.md` and `LORENTZIAN_MULTI_NODE_ENVIRONMENT_CORRELATION.md` — Lorentzian finite amplitudes/correlations;
19. `GLOBAL_MANIFOLD_Q2_COMPLETION.md` — canonical PL-S3 completion;
20. `DEWITT_HDA_UNIQUENESS.md` and `BF_GR_DIRAC_COUNT_DISCRIMINATOR.md` — conditional GR-universality discriminators.

## Production chain

```text
binary routes
-> q=2
-> octahedral S2 local link
-> chosen minimal flag PL S3
-> d_space~3, z~1 finite scaling window
-> E = H_E^sine
-> K=[V,E]
-> L_raw = epsilon-oriented C(K)C(K)C(V)
-> S = -i/2 (L_raw-L_raw^dagger)
-> G = -2/3 E -32/9 S          (beta=hbar=1)
-> positive kernel-safe operator-first R_op
-> H = G + R_op
-> cutoff-saturated two-node HDA
-> collective/refinement GR-universality killer
-> conditional GR tensor IR.
```

The production route operator is

\[
R_{op}[N]=\frac12\{N,\sqrt{\hat Q^{ab}\hat P_a\hat P_b}\}.
\]

The old formula

```text
G=(-2/3)E+(32 i/9)L_raw
```

is **not** the general v1.2 definition. It is only the exact reduction on sectors where `L_raw^dagger=-L_raw`, including the clean one-body `iY` projection.

## Hard numerical anchors

### Physical Euclidean sine HDA

```text
p_cross = 1.0056948923496356
p_GG    = 2.007490390559045
p_joint = 1.0076444430189475
Delta_joint(1/64)=0.020030338775070305
```

### Exhaustive operator-first route audit

```text
H_E support                       41
all distinct reached sectors      33
power-law sectors                 30
numerical-zero sectors             3
p range       0.9997944068141106 .. 0.9999830934452917
max endpoint  1.405841033798129e-05
min symbol eig -1.0658141036401503e-14 (roundoff zero)
```

### Singular route-symbol safety

The same 33 sectors were audited over 25 momentum modes. There are 24 genuinely singular PSD symbol cases. The kernel/Sylvester diagnostics are

```text
max ||Q.p|| on ker(A)     1.9133237149764433e-15
max ||P0 dA P0||          1.8736833294989963e-15
max Sylvester residual    1.7614399735154202e-13
```

so the zero-eigenvalue sectors satisfy the exact kernel compatibility required by the operator-valued HDA principal anticommutator.

### Lorentzian one-body

\[
L_{raw,1body}=i\,1.3389293521464034Y,
\]

and after the v1.2 Hermitian completion/normalization

\[
H_{corr,1body}=-4.760637696520545Y
\]

in structural units.

### Strict spin wall

The full finite-depth Lorentzian HH action from the all-`j=1/2` seed has at most 12 fundamental hits per link:

\[
\boxed{J_{max}^{safe}=13/2}.
\]

For this frozen habitat `Jmax>=13/2` is support-exact: the spin-cutoff remainder is zero.

## HDA status

For smooth lapses the pure geometry antisymmetric smear has no `O(1)` term. The apparently dangerous route mixed `1/epsilon` term cancels algebraically. With the WKB target `D=O(epsilon^-1)`:

\[
C_{G\times R}/D=O(\epsilon),\qquad C_{GG}/D=O(\epsilon^2).
\]

The exhaustive route regression has `p~1`, hence on the frozen two-node habitat

\[
\boxed{\Delta_{full}=O(\epsilon^{\min(p,1)})\to0}
\]

with zero spin-cutoff remainder for `Jmax>=13/2`.

Route-symbol zero modes do not open an extra principal-symbol anomaly: for `A=sum_i B_i^dagger B_i`, `ker A=intersection ker B_i` implies `P0(partial A)P0=0`, which is precisely the compatibility condition for the singular Sylvester equation `Omega X+X Omega=partial A`.

The older `Jmax~epsilon^-1/8` certificate is retained only for **growing-spin/depth extension families**. It is not required for this finite-depth core closure.

## Collective GR frontier — active

The next science question is no longer whether the frozen two-node microscopic core closes. The active killer gate is

\[
\text{microscopic first-class BCQG}\longrightarrow\text{collective first-class GR phase}.
\]

A science PASS is an AND of five direct refinement trends on the same BCQG family:

\[
D_{space}\to3,\qquad c_{DW}\to1/2,
\]

\[
(r_G,r_D,r_H,r_{extra})\to(3,3,1,0),
\]

\[
N_{phys}\to2,\qquad \Delta_{HH}^{collective}\to0.
\]

The protocol is frozen in `COLLECTIVE_GR_UNIVERSALITY_PREREGISTRATION.md`. Target/oracle controls cannot fill missing direct BCQG measurements; missing data means `INCOMPLETE`, not PASS.

Current verified prerequisites:

- canonical 16-cell PL-S3 barycentric refinement carrier: exact f-vectors through explicit level 2 and no sampled link-homology defects;
- symmetric collective-volume ladder: the scalar `j=1/2` |V| obstruction is removed at `j=1` and nontrivial volume branches persist through `j=5/2`;
- exact first blocking map `scripts/collective_j1_block_isometry_gate.py`: two microscopic spin-1/2 carriers per face -> symmetric `j=1`, with SU(2), Gauss and oriented-volume compression defects at roundoff scale;
- classical DeWitt/ADM safe-window controls identify the GR target but are not counted as collective BCQG measurements.

The exact first block isometry is a real coarse-graining result, but **the collective science verdict remains INCOMPLETE** until production `G,D,H` are compressed through the block map on at least four independent levels/habitats and the five preregistered observables are measured.

## Physical finite falsifier

The production Hermitian geometry channels are

\[
[G_0,G_1]=\frac49EE+\frac{64}{27}(ES+SE)+\frac{1024}{81}SS,
\]

with walls `5/2,9/2,9/2,13/2`. Completing `ES/SE/SS` remains a valuable finite implementation/factor-ordering falsifier; a timeout is not a physics FAIL and this finite enumeration is not the logical basis of the asymptotic theorem.

## What remains genuinely open

- direct compression of production `G,D,H` through the first exact collective block isometry;
- four-or-more complete collective levels for the GR-universality AND gate;
- metric (not merely topological) `D_space` from the collective flux geometry;
- effective kinetic Hessian and non-circular `c_DeWitt` extraction;
- collective constraint-rank SVD and exclusion of extra/BF generators;
- collective HDA residual trend;
- uniqueness among alternative microscopic factor orderings **before** the unique Hermitian projection;
- exhaustive finite route regression over every `S`-reached sector;
- off-diagonal multi-node Lorentzian blocks;
- direct `ES/SE/SS` finite calibration;
- uniform theorem when initial spin/operator depth grows;
- matter coupling, Newton normalization, physical scale setting;
- experiment.

Mirror force, infoton, foam-spectrum and GW-resonance branches are extensions, not evidence for the gravity core.

## Reporting rule

Use only:

```text
definition
proved
conditional
tested_finite
open
```

Do not promote a finite computation into an experiment, a target control into a BCQG derivation, or a controlled-habitat theorem into a uniform full-Hilbert-space theorem.
