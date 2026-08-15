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
5. `THEORY_STATUS.md` — human status ledger;
6. `theory_gates.json` — machine-readable obligations;
7. `LORENTZIAN_HERMITIAN_COMPLETION.md` — why full `L_raw` must be Hermitian-completed;
8. `LORENTZIAN_HERMITIAN_PROJECTION_UNIQUENESS.md` — uniqueness of the minimal projection once `L_raw` is fixed;
9. `ROUTE_OPERATOR_KERNEL_SAFETY.md` — kernel-safe Sylvester theorem for singular positive route symbols;
10. `PETER_WEYL_HERMITIAN_FULL_HDA_PREREGISTRATION.md` — frozen physical finite-channel falsifier;
11. `verification_results/BCQG_V12_CUTOFF_SATURATED_HDA.json` — cutoff-saturated HDA certificate;
12. `verification_results/PETER_WEYL_OPERATOR_ROUTE_ALL_REACHED.json` — exhaustive 33-sector route regression;
13. `verification_results/OPERATOR_ROUTE_KERNEL_SAFETY.json` — exhaustive singular-symbol audit;
14. `PETER_WEYL_TWO_NODE_SINE_HDA_RESULT.md` — preregistered Euclidean sine HDA PASS;
15. `PETER_WEYL_LORENTZIAN_ENVTRACE_RESULT.md` and `LORENTZIAN_MULTI_NODE_ENVIRONMENT_CORRELATION.md` — Lorentzian finite amplitudes/correlations;
16. `GLOBAL_MANIFOLD_Q2_COMPLETION.md` — canonical PL-S3 completion;
17. `DEWITT_HDA_UNIQUENESS.md` and `BF_GR_DIRAC_COUNT_DISCRIMINATOR.md` — conditional GR-universality discriminators.

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

## Physical finite falsifier

The production Hermitian geometry channels are

\[
[G_0,G_1]=\frac49EE+\frac{64}{27}(ES+SE)+\frac{1024}{81}SS,
\]

with walls `5/2,9/2,9/2,13/2`. Completing `ES/SE/SS` remains a valuable finite implementation/factor-ordering falsifier; a timeout is not a physics FAIL and this finite enumeration is not the logical basis of the asymptotic theorem.

## What remains genuinely open

- uniqueness among alternative microscopic factor orderings **before** the unique Hermitian projection;
- exhaustive finite route regression over every `S`-reached sector;
- off-diagonal multi-node Lorentzian blocks;
- direct `ES/SE/SS` finite calibration;
- independent habitats and collective refinement;
- uniform theorem when initial spin/operator depth grows;
- demonstration of GR first-class rank in the collective IR;
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

Do not promote a finite computation into an experiment or a controlled-habitat theorem into a uniform full-Hilbert-space theorem.
