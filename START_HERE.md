# START HERE — canonical BCQG research map

The repository contains several generations of exploratory calculations. **Do not infer the current scientific status from filename age or from the long pedagogical README alone.**

Current integrated candidate:

```text
BCQG Core Candidate v1
```

Status: **computable candidate quantum-gravity architecture, not an experimentally established theory of nature.**

---

## 1. Canonical files

Read these first, in this order:

1. `BCQG_CORE_CANDIDATE_V1.md` — compact definition of the current gravity candidate;
2. `THEORY_STATUS.md` — current human-readable proof/status ledger;
3. `theory_gates.json` — machine-readable gate ledger;
4. `PETER_WEYL_TWO_NODE_SINE_HDA_RESULT.md` — preregistered physical Euclidean sine-order two-node HDA PASS;
5. `ROUTE_OPERATOR_FIRST_QUANTUM_SELECTION.md` — linear positive operator-first quantum route selection and matrix HDA;
6. `EUCLIDEAN_SINE_NORMALIZATION_MATCH.md` — code-bound canonical Euclidean relative normalization;
7. `PETER_WEYL_LORENTZIAN_ENVTRACE_RESULT.md` — exact nonzero raw Lorentzian logical amplitude;
8. `LORENTZIAN_COMMUTATOR_PHASE_CERTIFICATE.md` — five-bracket canonical complex phase;
9. `LORENTZIAN_REAL_NORMALIZATION_LEDGER.md` — Lorentzian magnitude inherited from Euclidean normalization;
10. `FINAL_CORE_ARCHITECTURE_CERTIFICATE.md` — fixed-cutoff HDA composition theorem;
11. `JOINT_CUTOFF_DIAGONAL_CERTIFICATE.md` — explicit conditional simultaneous-cutoff path.

The root `README.md` is a long pedagogical narrative and contains historical layers. When it conflicts with the canonical files above, the canonical files win.

---

## 2. Current gravity-core chain

```text
binary q=2
 -> octahedral S2 local link
 -> minimal flag / recursive PL S3
 -> d_space ~ 3
 -> z ~ 1
 -> 3+1D-like history
 -> SU(2)/Peter-Weyl quantum geometry
 -> physical H_E^sine
 -> K=[V,H_E^sine]
 -> Lorentzian K-K-V
 -> linear positive operator-first route normal R_op
 -> HDA
 -> GR-like tensor IR candidate.
```

Canonical simultaneous-cutoff trajectory:

```text
Jmax(epsilon) ~ epsilon^-1/8
```

conditional on the declared polynomial norm envelope.

---

## 3. Current exact / finite anchors

### Dimension / topology

```text
q = 2
d_H = 2.999229782
z = 0.998281156
d_s(slice) = 3.004393867
d_s(history) ~ 4.004393867
16-cell seed Betti = (1,0,0,1)
```

### Physical Euclidean sine-order two-node HDA — preregistered PASS

```text
H_E^sine=(T-T^dagger)/(2i)
K_sine=[V,H_E^sine]

||H0||=||H1||=2.171258176327055
||[H0,H1]||=2.8794538147049544
p_cross=1.0056948923496356
p_GG=2.007490390559045
p_joint=1.0076444430189475
Delta_joint(1/64)=0.020030338775070305
```

Provenance:

```text
GitHub Actions run 31855735615
artifact digest sha256:21e2da508fd583d9007a5bd400d074e8cee39990656e6c75e5968d2601323526
```

The older `H_plus=(T+T^dagger)/2` endpoint `0.014707752821092098` is historical only and must not be relabelled as the physical result.

### Quantum route operator-first HDA

The production candidate is

```text
R_op[N] = 1/2 {N, sqrt(Qhat^{ab} P_a P_b)}.
```

Expectation-first state-dependent square-root maps are nonlinear on superpositions and remain semiclassical surrogates only.

Exact logical matrix control:

```text
operator-first route defect(epsilon=1/64, carrier=8)=3.837772425e-7
p=0.999960897
```

The PASS is robust across five logical spinors and carriers `2,4,8,16`.

### Euclidean / Lorentzian relative normalization

The production `oriented_specs` and `T_sequences` match the canonical tetrahedral epsilon combinatorics. In the original fundamental-trace convention,

```text
H_E^phys = n_E H_sine^raw
n_E = -2/(3 hbar).
```

Therefore the Lorentzian K-K-V magnitude is not an independent fit parameter. At `hbar=1`,

```text
full beta=1 correction magnitude = 32/9
bare repository H_L magnitude    = 16/9
```

when the total constraint is written `H_E+(1+beta^2)H_L`.

These are relative structural coefficients, not physical energies.

### Lorentzian raw amplitude and phase

At `Jmax=7/2`, all 16 logical environments and the full S4 orbit give

```text
L_raw,1body = i*1.3389293521464034*Y + O(1e-16)
S4 covariance defect = 1.3976239359266602e-15
physical basis/volume leakage = 6.532094795930893e-16.
```

The declared nested Thiemann stack contains five Poisson brackets, hence

```text
(1/i)^5=-i
```

and

```text
-i L_raw = 1.3389293521464034 Y + O(1e-16).
```

### Corrected Euclidean anisotropy

```text
A_rel = 0.9644798301915488
J_shape = -0.5564630119591318
J_orient = +2.18199564892363
Delta_aniso,ret = 2.738458660882762
648 states = 392 positive + 256 negative.
```

The older `Delta_aniso,ret=3.6832250321658044` is retired.

---

## 4. Current single decisive gravity gate

The separate Euclidean-ordering and route-ordering questions are no longer the immediate bottlenecks.

The next full operator is

```text
H_full[N]
 = H_E^sine[N]
 + (1+beta^2) H_L[N]
 + R_op[N].
```

The immediate killer calculation is

```text
[H_full[N], H_full[M]]
 -> i hbar D[sharp_Q(N dM - M dN)]
```

on the same graph-changing two-node Peter-Weyl habitat with:

```text
full spin-changing H_L amplitudes;
canonical five-bracket phase;
upstream-fixed relative magnitude;
operator-first route square root;
nonconstant off-shell lapses;
no channel-dependent subtraction or post-hoc fit.
```

A PASS moves the frontier to independent habitats, collective-spin/refinement scaling and a stronger simultaneous-cutoff theorem. A FAIL stays recorded and identifies the anomalous full Lorentzian channel.

---

## 5. Gravity core versus extensions

Gravity core:

- q=2 selector and PL manifold completion;
- dimension/dynamical scaling;
- physical sine-Hermitian SU(2)/Peter-Weyl geometry;
- Lorentzian K-K-V construction;
- operator-first route-normal generator;
- HDA and regulator limits;
- IR DeWitt/tensor interpretation.

Separate extensions, not evidence for the gravity core:

- mirror-force / antigravity-like branch;
- `infoton` route boson;
- conditional `P_delta_g(k)~k^1.003414` vacuum spectrum;
- GW-driven route-mode resonance;
- realistic matter/chirality completion.

---

## 6. Reproduction shortcuts

```bash
python scripts/verify_theory_gates.py
python scripts/canonical_ledger_consistency_gate.py
python scripts/peter_weyl_two_node_euclidean_sine_joint_gate.py
python scripts/operator_first_route_hda_gate.py
python scripts/euclidean_sine_normalization_match_gate.py
python scripts/lorentzian_commutator_phase_gate.py
python scripts/lorentzian_real_normalization_gate.py
python scripts/joint_cutoff_diagonal_gate.py
```

---

## 7. Reporting rule

Every result is labelled as one of:

```text
proved
conditional
tested_finite
open
```

A finite gate is not an experiment. A conditional continuum inference is not an exact theorem. A successful regression is not an independent observation.
