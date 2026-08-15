# START HERE — canonical BCQG research map

The repository contains several generations of exploratory calculations. **Do not infer current status from filename age or the long root README.**

Current integrated candidate:

```text
BCQG Core Candidate v1
```

Status: **computable candidate quantum-gravity architecture, not an experimentally established theory of nature.**

---

## 1. Canonical files

Read these first:

1. `BCQG_CORE_CANDIDATE_V1.md` — compact current gravity definition;
2. `THEORY_STATUS.md` — human-readable canonical ledger;
3. `theory_gates.json` — machine-readable gate ledger;
4. `PETER_WEYL_TWO_NODE_SINE_HDA_RESULT.md` — preregistered physical sine-order Euclidean two-node HDA PASS;
5. `ROUTE_OPERATOR_FIRST_QUANTUM_SELECTION.md` — positive linear operator-first route candidate;
6. `EUCLIDEAN_SINE_NORMALIZATION_MATCH.md` — code-bound Euclidean normalization;
7. `PETER_WEYL_LORENTZIAN_ENVTRACE_RESULT.md` — exact nonzero raw Lorentzian logical amplitude;
8. `LORENTZIAN_COMMUTATOR_PHASE_CERTIFICATE.md` — five-bracket phase;
9. `LORENTZIAN_REAL_NORMALIZATION_LEDGER.md` — signed Lorentzian coefficient inherited from the Euclidean/Thiemann convention;
10. `verification_results/LORENTZIAN_REPO_SIGN.json` — CI evidence for signed beta=1 coefficient;
11. `PETER_WEYL_FULL_GEOMETRY_COMMUTATOR_PREREGISTRATION.md` — frozen exact full geometry channel protocol;
12. `FINAL_CORE_ARCHITECTURE_CERTIFICATE.md` — fixed-cutoff composition theorem;
13. `JOINT_CUTOFF_DIAGONAL_CERTIFICATE.md` — explicit conditional simultaneous-cutoff path.

`ROUTE_OPERATOR_FIRST_TWO_NODE_REFERENCE.md` is an independent numerical reference and is **not** promoted to canonical tested evidence until its repository CI completes.

---

## 2. Current gravity chain

```text
q=2
-> octahedral S2 local link
-> minimal flag / recursive PL S3
-> d_space~3, z~1
-> 3+1D-like history
-> physical H_E^sine
-> K=[V,H_E^sine]
-> signed Lorentzian K-K-V
-> positive operator-first route R_op
-> HDA
-> GR-like tensor IR candidate.
```

Canonical joint path:

```text
Jmax(epsilon) ~ epsilon^-1/8
```

conditional on the frozen polynomial norm envelope.

---

## 3. Current anchors

### Physical Euclidean sine-order two-node HDA — preregistered PASS

```text
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

### Operator-first route

Canonical logical finite gate:

```text
endpoint(1/64, carrier=8)=3.837772425e-7
p=0.999960897
```

Independent two-node 4×4 reference:

```text
K0K0 endpoint(1/64)=8.205159710207801e-7
p=0.9999594708960342
sparse Fourier vs FFT max relative difference=5.74e-8
```

The two-node reference remains non-canonical until Actions evidence completes.

### Lorentzian raw amplitude and phase

```text
L_raw,1body = i*1.3389293521464034*Y + O(1e-16)
(1/i)^5 = -i
H_phase = -i L_raw
```

### Signed relative normalization

```text
H_E^phys = -2/(3 hbar) * E_raw
Hcorr/Hphase = -32/(9 hbar^7)
H_L/Hphase = -32/[9 hbar^7(1+beta^2)]
```

At `beta=hbar=1`:

```text
bare H_L/Hphase = -16/9
full correction/Hphase = -32/9
G_v = (-2/3) E_v + (32 i/9) L_raw,v
```

CI provenance:

```text
lorentzian-repo-sign
run 31857722477
artifact digest sha256:10f538abd68dc8945a46ec03410b5e4490a5d8e1fbbb05d56a10a56fd6220101
fitting_used=false
```

So **relative Lorentzian sign and magnitude are no longer open tuning parameters**.

### Signed logical Lorentzian-route cross

Unit phase-completed operator-first cross:

```text
+0.0536574847984 X +0.0929374897107 Z
```

Full beta=1 signed correction regression:

```text
-0.1907821681721 X -0.3304444078603 Z
shape norm = 0.3815643358315
```

### Corrected Euclidean anisotropy

```text
A_rel=0.9644798301915488
J_shape=-0.5564630119591318
J_orient=+2.18199564892363
Delta_aniso,ret=2.738458660882762
648 states=392 positive+256 negative
```

Old `Delta_aniso,ret=3.6832250321658044` is retired.

---

## 4. Current single decisive gravity gate

The next full operator is

```text
H_full[N] = H_E^sine[N] + (1+beta^2) H_L[N] + R_op[N].
```

At `beta=hbar=1` the geometry part is frozen in raw-code units as

```text
G_v=(-2/3)E_v+(32 i/9)L_raw,v.
```

The exact geometry commutator is preregistered as

```text
EE=E0E1-E1E0       Jmax wall 5/2
EL=E0L1-E1L0       Jmax wall 9/2
LE=L0E1-L1E0       Jmax wall 9/2
LL=L0L1-L1L0       Jmax wall 13/2
```

and the final target is

```text
[H_full[N],H_full[M]]
-> i hbar D[sharp_Q(N dM-M dN)].
```

No channel subtraction, sign flip, coefficient fit or threshold retuning is permitted after result inspection.

The branch now contains the computational pieces needed for this calculation:

- general full-state Lorentzian covariant→Gauss adapter;
- 24-way exact full-state Lorentzian ordered-triple workers + collector;
- distributed EE/EL/LE/LL workers + signed collector;
- exact sparse-Fourier operator-first route algebra;
- generic spin-changing route blocks.

The integration PR is temporarily closed while branch-push research workflows run, to prevent duplicate `pull_request synchronize` jobs from saturating Actions. The branch and all evidence remain intact.

---

## 5. Reproduction shortcuts

```bash
python scripts/verify_theory_gates.py
python scripts/canonical_ledger_consistency_gate.py
python scripts/peter_weyl_two_node_euclidean_sine_joint_gate.py
python scripts/operator_first_route_hda_gate.py
python scripts/euclidean_sine_normalization_match_gate.py
python scripts/lorentzian_commutator_phase_gate.py
python scripts/lorentzian_repo_sign_gate.py --hbar 1 --beta 1
python scripts/lorentzian_route_logical_cross_gate.py
python scripts/joint_cutoff_diagonal_gate.py
```

---

## 6. Reporting rule

Every result is labelled

```text
proved
conditional
tested_finite
open
```

A finite gate is not an experiment. A conditional continuum inference is not an exact theorem. A successful regression is not an independent observation.
