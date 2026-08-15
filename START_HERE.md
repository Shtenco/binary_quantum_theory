# START HERE — canonical BCQG research map

The repository contains several generations of exploratory calculations. **Do not infer current status from filename age or the long root README.**

Current integrated theory document:

```text
BCQG Candidate Theory v1.1
```

Status: **mathematically/computationally specified candidate quantum-gravity theory; not experimentally established.**

---

## 1. Canonical files

Read these first:

1. `BCQG_CANDIDATE_THEORY_V1_1.md` — current candidate theory, assumptions and physical/dimensionless predictions;
2. `BCQG_CORE_CANDIDATE_V1.md` — compact gravity-core definition;
3. `THEORY_STATUS.md` — human-readable status ledger;
4. `theory_gates.json` — machine-readable gate ledger;
5. `FULL_OPERATOR_FIRST_HDA_CERTIFICATE.md` — signed operator-first full-HDA asymptotic composition certificate;
6. `PETER_WEYL_TWO_NODE_SINE_HDA_RESULT.md` — preregistered physical sine-order Euclidean two-node HDA PASS;
7. `ROUTE_OPERATOR_FIRST_QUANTUM_SELECTION.md` — linear positive operator-first route construction;
8. `verification_results/PETER_WEYL_OPERATOR_ROUTE_SPINCHANGED_BLOCKS.json` — successful `R_op` HDA evidence on genuine spin-changed sectors;
9. `PETER_WEYL_LORENTZIAN_ENVTRACE_RESULT.md` — exact nonzero raw Lorentzian one-body partial trace;
10. `LORENTZIAN_MULTI_NODE_ENVIRONMENT_CORRELATION.md` — exact conditional neighbor/multi-node Lorentzian correlations recovered from MITM artifacts;
11. `LORENTZIAN_COMMUTATOR_PHASE_CERTIFICATE.md` — five-bracket phase;
12. `LORENTZIAN_REAL_NORMALIZATION_LEDGER.md` and `verification_results/LORENTZIAN_REPO_SIGN.json` — signed Lorentzian coefficient;
13. `PETER_WEYL_FULL_GEOMETRY_COMMUTATOR_PREREGISTRATION.md` — frozen channel-resolved finite falsifier;
14. `JOINT_CUTOFF_DIAGONAL_CERTIFICATE.md` — explicit conditional simultaneous-cutoff path.

---

## 2. Current gravity chain

```text
q=2
-> octahedral S2 local link
-> minimal flag / recursive PL S3
-> d_space~3, z~1
-> 3+1D-like history
-> physical H_E^sine
-> signed Lorentzian K-K-V
-> positive operator-first R_op
-> signed operator-first HDA composition
-> GR-like two-helicity tensor IR candidate.
```

At `beta=hbar=1`, the frozen raw-code geometry generator is

```text
G_v=(-2/3)E_v+(32 i/9)L_raw,v.
```

The route generator is

\[
R_{op}[N]=\frac12\{N,\sqrt{\hat Q^{ab}\hat P_a\hat P_b}\}.
\]

Canonical joint continuum path:

```text
Jmax(epsilon) ~ epsilon^-1/8
```

conditional on the frozen polynomial norm envelope.

---

## 3. Current hard anchors

### Physical sine two-node HDA — preregistered PASS

```text
||H0||=||H1||=2.171258176327055
||[H0,H1]||=2.8794538147049544
p_cross=1.0056948923496356
p_GG=2.007490390559045
p_joint=1.0076444430189475
Delta_joint(1/64)=0.020030338775070305
```

### Operator-first route after genuine geometry change — PASS

Five distinct higher-spin sectors reached by `H_E^sine` give

```text
p_R in [0.9998813243, 0.9999820816]
endpoint defects in [9.37065e-7, 3.63658e-6]
minimum symbol eigenvalue ~= -1.07e-14 (numerical zero).
```

Provenance:

```text
run      31858615323
artifact 9244277324
digest   sha256:c1af8de00183fddf328f6bdfba386e2320b842e10d3de98d90ad150b0876213c
```

### Signed Lorentzian normalization

```text
H_E^phys = -2/(3 hbar) E_raw
Hcorr/Hphase = -32/(9 hbar^7)
H_L/Hphase = -32/[9 hbar^7(1+beta^2)]
```

At `beta=hbar=1`:

```text
bare H_L/Hphase = -16/9
full correction/Hphase = -32/9
G_v=(-2/3)E_v+(32 i/9)L_raw,v
```

No relative sign or magnitude is fitted against HDA data.

### Environment-unbiased Lorentzian one-body result

```text
L_raw,1body = i*1.3389293521464034*Y + O(1e-16)
(1/i)^5=-i
```

### Newly recovered conditional multi-node structure

From the successful exact MITM environment run, with nodes `3,4` frozen at `K=0`, the diagonal logical Walsh decomposition has coefficient-vector norms

```text
source local             0.33709171624286727
source x node1           0.03631787483605024
source x node2           0.006983526478664483
source x node1 x node2   0.01396705295732858
```

with dominant pseudoscalar correlations

```text
Y I I   = +i 0.335901403339900
Y Z1 I  = -i 0.007028617222480
Y I Z2  = +i 0.002338130606599
Y Z1 Z2 = +i 0.004676261213198.
```

This is a tested **diagonal-environment** correlation result, not yet the complete multi-qubit Lorentzian Hamiltonian because off-diagonal environment transitions were not part of the historical trace workers.

---

## 4. Current HDA status

For smooth lapse probes

\[
N=\bar N+\epsilon n,\qquad M=\bar M+\epsilon m,
\]

the signed geometry smear has no zeroth-order term:

\[
N_0M_1-N_1M_0=O(\epsilon).
\]

For operator-first route transitions the apparently dangerous `1/epsilon` mixed term cancels algebraically before taking matrix elements. With bounded local geometry at every fixed safe finite Peter-Weyl cutoff,

\[
\boxed{C_{G\times R}/D=O(\epsilon)},
\qquad
\boxed{C_{GG}/D=O(\epsilon^2)}.
\]

Together with the measured operator-first route convergence on real spin-changed sectors,

\[
\boxed{\Delta_{full}=\Delta_{R,op}+O(\epsilon)+O(\epsilon^2)\to0}
\]

on the declared fixed-cutoff WKB habitat.

With the separately frozen joint-cutoff envelope and

```text
Jmax~epsilon^-1/8
```

the contaminating terms scale as

```text
C_GxR/D = O(epsilon^(3/16))
C_GG/D  = O(epsilon^(3/8)).
```

This is a **conditional candidate-theory closure statement**, not a uniform arbitrary-path theorem and not an experimental result.

---

## 5. Remaining decisive finite falsifier

The exact channel-resolved geometry commutator remains frozen as

```text
EE=E0E1-E1E0       Jmax wall 5/2
EL=E0L1-E1L0       Jmax wall 9/2
LE=L0E1-L1E0       Jmax wall 9/2
LL=L0L1-L1L0       Jmax wall 13/2
```

with signed assembly

\[
[G_0,G_1]
=\frac49EE-\frac{64i}{27}(EL+LE)-\frac{1024}{81}LL.
\]

`EE` is complete:

```text
support=514
norm=2.879453814704955.
```

The original brute-force `EL/LE/LL` jobs exhausted their runner wall before artifacts were written. This is a **computational timeout, not a physics FAIL**. The finite calculation remains valuable because it can falsify the candidate through unexpectedly large finite coefficients, scalar-projection/order errors, or a habitat-specific obstruction.

Frozen final five-point acceptance remains:

```text
p_cross in [0.75,1.25]
p_GG    in [1.75,2.25]
p_joint in [0.75,1.25]
Delta_joint(1/64) < 0.05
```

with no channel subtraction, sign flip, coefficient fit or threshold retuning after result inspection.

---

## 6. Core physical predictions

The candidate currently predicts, conditionally on successful continuum HDA and scale-independent assumptions stated in `BCQG_CANDIDATE_THEORY_V1_1.md`:

- spatial flow to `d_space=3`, dynamical exponent `z=1`, 4D-like history;
- one massless spin-2 IR sector with two TT helicities and no non-decoupling scalar gravity mode;
- restoration of relativistic tensor propagation in the IR;
- the HDA regulator hierarchy above;
- first-order logical Euclidean silence `P H_E^sine P=0`;
- a signed microscopic staggered orientation/chirality field;
- operator-first two-node entangling route channels;
- finite neighbor-dependent Lorentzian logical correlations before environment trace;
- positive route symbols on the tested physical spin sectors.

Absolute eV, meter, Newton or force predictions are deliberately withheld until the IR Newton/matter scale is derived.

---

## 7. Reporting rule

Every result must remain labelled

```text
proved
conditional
tested_finite
open
```

A finite gate is not an experiment. A conditional continuum theorem is not an unconditional theorem of the full Hilbert space. A computational timeout is not a falsification.
