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
4. `FINAL_CORE_ARCHITECTURE_CERTIFICATE.md` — fixed-cutoff HDA composition theorem;
5. `JOINT_CUTOFF_DIAGONAL_CERTIFICATE.md` — explicit conditional simultaneous-cutoff path;
6. `PETER_WEYL_LORENTZIAN_ENVTRACE_RESULT.md` — exact nonzero raw Lorentzian logical amplitude;
7. `LORENTZIAN_COMMUTATOR_PHASE_CERTIFICATE.md` — five-bracket canonical complex phase;
8. `LORENTZIAN_16CELL_GLOBAL_ASSEMBLY.md` — globally oriented 16-cell interpretation;
9. `PETER_WEYL_TWO_NODE_SINE_HDA_PREREGISTRATION.md` — frozen next finite HDA falsifier.

The root `README.md` is a long pedagogical narrative and contains historical layers. When it conflicts with the files above, the canonical files above win.

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
 -> geometry-dependent route-normal generator
 -> HDA
 -> GR-like tensor IR candidate.
```

Canonical simultaneous-cutoff trajectory:

```text
Jmax(epsilon) ~ epsilon^-1/8
```

conditional on the declared polynomial norm envelope.

---

## 3. Current exact/finite anchors

### Dimension / topology

```text
q = 2
d_H = 2.999229782
z = 0.998281156
d_s(slice) = 3.004393867
d_s(history) ~ 4.004393867
16-cell seed Betti = (1,0,0,1)
```

### Historical plus-order Euclidean two-node HDA control

```text
H_plus = (T+T^dagger)/2
Delta_joint(1/64)=0.014707752821092098
p_cross=1.0058917161144039
p_EE=2.0074903905590453
p_joint=1.0071260819282668
```

These numbers are **historical structural controls**. They must not be silently relabelled as the physical sine-order result.

### Physical Euclidean ordering

The current Euclidean/Lorentzian stack uses

```text
H_E^sine=(T-T^dagger)/(2i)
K_sine=[V,H_E^sine].
```

The dedicated two-node sine HDA gate is preregistered in

```text
PETER_WEYL_TWO_NODE_SINE_HDA_PREREGISTRATION.md
```

and implemented in

```text
scripts/peter_weyl_two_node_euclidean_sine_joint_gate.py.
```

### Lorentzian raw amplitude

At `Jmax=7/2`, with all 16 logical environments and the full S4 orbit,

```text
L_raw,1body = i*1.3389293521464034*Y + O(1e-16)
S4 covariance defect = 1.3976239359266602e-15
physical basis/volume leakage = 6.532094795930893e-16.
```

### Lorentzian complex phase

For the declared nested Thiemann bracket structure,

```text
{A,{V,H_E}} {A,{V,H_E}} {A,V}
```

there are five Poisson brackets, so

```text
(1/i)^5=-i.
```

Hence the phase-completed finite logical block is Hermitian:

```text
-i L_raw = 1.3389293521464034 Y + O(1e-16)
```

before the remaining real normalization/sign.

### Global oriented 16-cell assembly

Exact facet orientation is

```text
eta_v=(-1)^popcount(v).
```

Therefore

```text
H_L,1body = g_R*c_L*sum_v eta_v Y_v
           = 16*g_R*c_L*Sigma.
```

For the ideal fixed-orientation mirror pair the structural splitting is

```text
42.84573926868491 * |g_R|.
```

This is a longitudinal orientation field, **not a mediator mass or a fifth force**.

---

## 4. Corrected Peter-Weyl anisotropy

Current audited values:

```text
A_rel = 0.9644798301915488
J_shape = -0.5564630119591318
J_orient = +2.18199564892363
Delta_aniso,ret = 2.738458660882762
648 states = 392 positive + 256 negative.
```

The older

```text
Delta_aniso,ret = 3.6832250321658044
```

is retired and must not be used.

---

## 5. What is gravity core versus extension

### Gravity core

- q=2 selector and PL manifold completion;
- dimension/dynamical scaling;
- SU(2)/Peter-Weyl quantum geometry;
- physical sine Euclidean ordering;
- Lorentzian K-K-V construction;
- geometry-dependent route-normal generator;
- HDA / simultaneous regulator limits;
- IR tensor/DeWitt interpretation.

### Separate extensions

These are **not** evidence for the gravity core:

- mirror force / antigravity-like fifth-force branch;
- `infoton` route boson;
- conditional `P_delta_g(k)~k^1.003414` vacuum spectrum;
- GW-driven route-mode resonance;
- realistic matter/chirality model.

---

## 6. Current decisive gates

The immediate research order is:

```text
A. physical H_E^sine two-node route HDA
B. real Lorentzian normalization/sign + full factor ordering
C. completed two-node H_E^sine + H_L + R_Q HDA
D. independent habitats / collective-spin / joint-cutoff scaling.
```

Do not reopen already separated questions unless one of these gates falsifies an upstream assumption.

---

## 7. Reproduction shortcuts

Machine ledger:

```bash
python scripts/verify_theory_gates.py
python scripts/canonical_ledger_consistency_gate.py
```

Joint cutoff:

```bash
python scripts/joint_cutoff_diagonal_gate.py
```

Lorentzian phase:

```bash
python scripts/lorentzian_commutator_phase_gate.py
```

Global 16-cell Lorentzian assembly:

```bash
python scripts/lorentzian_16cell_global_assembly_gate.py
```

Lorentzian × route logical ordering discriminator:

```bash
python scripts/lorentzian_route_logical_cross_gate.py
```

Physical sine two-node HDA:

```bash
python scripts/peter_weyl_two_node_euclidean_sine_joint_gate.py
```

---

## 8. Reporting rule

Every result should be labelled as one of:

```text
proved
conditional
tested_finite
open
```

A finite gate is not an experiment. A conditional continuum inference is not an exact theorem. A successful regression target is not an independent observation.

That distinction is part of the candidate theory, not a disclaimer added after the fact.
