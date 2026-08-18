# Canonical Theory Package v1

Status date: 2026-08-18

This document is the canonical index of the internally closed mathematical/computational candidate theory contained in this repository.

It does not assert experimental confirmation. It records what has actually been derived, calculated or reproducibly tested inside the declared candidate construction.

---

## A. Closure statement

```text
CORE THEORY PACKAGE: CLOSED IN DECLARED SCOPE
CANDIDATE FRAMEWORK: YES
EXPERIMENTALLY ESTABLISHED THEORY OF NATURE: NO
```

Core closure requires:

1. a specified microscopic route family;
2. an explicit quantum-geometric carrier;
3. global geometric gluing;
4. a metric/curvature reconstruction;
5. a GR/ADM/HDA dynamical bridge;
6. controlled Peter-Weyl support/cutoff calculations;
7. a spin-2/TT observable sector;
8. a complete low-energy quartic observable basis;
9. a direct map from frozen theory coefficients to testable observables;
10. machine-readable evidence and regression.

All ten are present in the package.

---

## B. Binary microstructure and dimension

### B1. Frozen q=2 route system

Evidence:

- `BIT_TO_SPACETIME_CENTRAL_EQUATION.md`
- `OBSERVER_SCALE_SMOOTHING.md`
- `bcqg_observer_smoothing_unified.py`

Finite diagnostics:

```text
d_H          = 2.999229782
d_s(slice)   = 3.004393867
z            = 0.998281156
d_s(history) ≈ 4.004393867
```

Coarse-resolution exponents:

```text
metric fluctuation   ~ b^-2.001707
gradient fluctuation ~ b^-3.001458
curvature proxy      ~ b^-4.000524
```

### B2. Exact dimension-three fixed point

Evidence:

- `Q2_DIMENSION3_FIXED_POINT_CLOSURE.md`
- `scripts/q2_dimension3_fixed_point_gate.py`

Exact count:

```text
N_g = (4*8^g + 10)/7
```

Exact finite-step dimension:

```text
d_g = log2(N_g/N_(g-1))
    = 3 + log2(1 - 35/(16*8^(g-1)+40))
```

Certificate:

```text
all finite steps below 3
monotone increase
limit d_* = 3 exactly
```

---

## C. Local quantum geometry from q=2

### C1. Walsh tetrahedral carrier

Evidence:

- `MICRO_WALSH_QGEOM_BRIDGE.md`
- `scripts/micro_walsh_qgeom_gate.py`

Exact identities:

```text
sum_a n_a = 0
n_a.n_a = 1
n_a.n_b = -1/3  for a != b
```

Qubit/Gauss outputs:

```text
Gauss-singlet weight       = 2/9
logical Bloch              ≈ (0,+1,0)
oriented volume            = sqrt(3)/4
edge spread                = 0
orientation reversal       ≈ (0,-1,0)
```

### C2. Graph-link representation

Evidence:

- `Q2_GRAPHLINK_PETER_WEYL_BRIDGE.md`
- `scripts/q2_graphlink_peter_weyl_gate.py`
- `scripts/su2_quantum_link_vector5_gate.py`

Result:

```text
4 active q=2 states alone: not a (2,2) endpoint bi-doublet
4 active + no-link/j=0: exact SO(5) vector = (2,2) + (1,1)
```

Transporter identity:

```text
P_g U_a P_0 U_b P_g = |a><b|
```

Hence the frozen q=2 Hamming adjacency factors through graph-changing two-step excursions via the no-link state.

### C3. Peter-Weyl representation growth

Evidence:

- `Q2_GRAPHLINK_PETER_WEYL_BRIDGE.md`
- `scripts/q2_symmetric_block_peter_weyl_growth_gate.py`

Conditional exact representation statement:

```text
Sym^n(C^2)_L x Sym^n(C^2)_R -> (j=n/2,j=n/2)
dimension = (n+1)^2 = (2j+1)^2
```

Occupancy n=0..N reproduces the diagonal Peter-Weyl tower through Jmax=N/2.

---

## D. Global spatial geometry

Evidence:

- `GLOBAL_MANIFOLD_Q2_COMPLETION.md`
- `bcqg_global_manifold_gate.py`
- `scripts/q2_global_face_qubit_gluing_gate.py`

Selected completion:

```text
boundary of the 4D cross-polytope
16 tetrahedral cells
32 shared triangle faces
dual graph Q4
```

Exact gluing certificate:

```text
same q=2 colour on both incidences of each shared face
neighbor orientation parity alternates
outward Walsh flux cancels pairwise
```

---

## E. Metric, B-field and Einstein reconstruction

### E1. Qubit -> B -> Urbantke -> Einstein

Evidence:

- `QUBIT_TO_EINSTEIN_END_TO_END.md`
- `PLEBANSKI_URBANTKE_BRIDGE.md`
- `PLEBANSKI_CONNECTION_EINSTEIN_GATE.md`
- `scripts/qubit_to_einstein_end_to_end.py`
- `scripts/plebanski_urbantke_gate.py`
- `scripts/plebanski_connection_einstein_gate.py`

The positive control reconstructs the declared Einstein geometry. An independent non-Einstein control is rejected after the metric stage.

The unit-S4 Lambda≈3 number is an oracle reconstruction check and is not a physical cosmological-constant prediction.

### E2. Exact logical metric Jacobian

Evidence:

- `LOGICAL_SHAPE_METRIC_JACOBIAN.md`
- `scripts/logical_shape_metric_jacobian_gate.py`

Certificate:

```text
rank = 2
X/Z tangents trace-free
X/Z tangents orthogonal
equal DeWitt norm
orientation branches share the intrinsic metric Jacobian
```

### E3. L1 q4 S4 metric-sector compression

Evidence:

- `L1_Q4_S4_METRIC_COMPRESSION_RESULT.md`
- `scripts/collective_l1_q4_s4_metric_compression.py`
- certified 24-column source artifact set from workflow run `31965359681`

Fresh canonical reassembly gives:

```text
lambda_E                    = 1.1111917875584736
lambda_T2                   = 1.0220278507464782
Delta_ET                    = 0.08916393681199541
relative_ET_split           = 0.08359564595312347
S4 commutator relative max  = 6.893947764166024e-16
S4 orbit residual           = 1.7916222470383044e-16
```

Here

```text
relative_ET_split = Delta_ET / ((lambda_E+lambda_T2)/2),
```

so the canonical normalized split is about `8.36%`.

---

## F. Regge / Einstein-Hilbert continuum controls

Evidence:

- `REGGE_EH_CUBIC_BRIDGE.md`
- `scripts/regge_eh_cubic_bridge.py`
- `REGGE_DIRECTIONAL_RESIDUE_RESULT.md`
- `scripts/gravity_bridge_scaling.py`
- `regge_flat_lattice.py`

The cubic Regge/EH bridge reproduces the declared finite continuum-scaling relations. Directional Hessian controls test axial, diagonal-2 and diagonal-3 finite-lattice residues against the common continuum tensor structure.

The canonical minimal Regge utility includes the exact periodic Freudenthal geometry plus the real 30-dimensional Fourier-mode map, central finite-difference Hessian and vertex-displacement gauge basis required by the directional calculation.

### F1. Held-out L=6 continuation

Evidence:

- `TT_REGGE_ZT_L6_PREREGISTRATION.md`
- `TT_REGGE_ZT_L6_RESULT.md`
- `scripts/tt_regge_zt_l6_gate.py`

Frozen training rule:

```text
Z_L = 1/8 + C/L^2 + D/L^4
training L = 3,4,5 only
```

Held-out comparison:

```text
Z6_pred = 0.11876923193907167
Z6_obs  = 0.11876075461190198
relative error ≈ 0.00714 %
```

No L=6 refit is allowed by the regression gate.

---

## G. Peter-Weyl quantum dynamics

### G1. Finite geometry/constraint stack

Evidence families include:

- `PETER_WEYL_TRUNCATION_GATE.md`
- `K5_PETER_WEYL_SAFE_HDA_FIRST_COLUMN.md`
- `scripts/k5_peter_weyl_safe_hda_column.py`
- `scripts/peter_weyl_lorentzian_K_block_gate.py`
- `scripts/peter_weyl_covariant_composition_gate.py`
- `scripts/peter_weyl_covariant_K_composition_gate.py`

### G2. 32D master normalization

Evidence:

- `scripts/peter_weyl_master_32_gate.py`

The nonlinear master normalization is performed before environment tracing and the support-projector limit is checked on the complete 32D logical sector.

### G3. Lorentzian parity / support structure

Evidence:

- `scripts/peter_weyl_lorentzian_parity_gate.py`
- `scripts/lorentzian_hit_depth_bound.py`
- `scripts/lorentzian_beta_cancellation_gate.py`

The Euclidean/Lorentzian doubled-spin grading, fixed coefficient and support bounds are used as operator-selection and cutoff certificates.

### G4. Completed higher-shell Lambda

Evidence:

- `PETER_WEYL_HIGHER_SHELL_LAMBDA_RESULT.md`
- `scripts/peter_weyl_higher_shell_lambda_gate.py`
- certified sparse source columns from workflow run `31844567559`

Historical certified result:

```text
lambda_min = 10.635759878291307
lambda_max = 15.059927665966466
relative distance from scalar identity = 0.09440461833276048
block-Lanczos identities close at ~1e-13 residual scale
```

Canonical regeneration reuses the 31 certified exact source columns, independently recomputes the historically heavy column 28, then reassembles and rechecks the full matrix.

### G5. j=1 S4 block

Evidence:

- `PETER_WEYL_J1_S4_BLOCK_RESULT.md`
- `scripts/peter_weyl_j1_s4_block_gate.py`

The four-j=1 singlet space contains the multiplicity-one S4 `[2,2]` coarse doublet used as the representation-RG consistency carrier.

---

## H. ADM / DeWitt / HDA

Evidence:

- `DEWITT_HDA_UNIQUENESS.md`
- `FLUX_DEWITT_SIGNATURE_THEOREM.md`
- `BF_GR_DIRAC_COUNT_DISCRIMINATOR.md`
- route-vector / route-normal gates
- `PETER_WEYL_TWO_NODE_EUCLIDEAN_RESULT.md`
- `THREE_NODE_GRAPH_HDA_RESULT.md`
- `JOINT_REGULATOR_LIMIT.md`
- `LORENTZIAN_BETA_CANCELLATION.md`

Three-node graph-changing result:

```text
pair supports                        = 510, 648, 648
minimum j=0 graph-change fraction    = 0.4440331635
union reduced graph orbits           = 31
route exponent                       = 0.9999571195
cross exponent                       = 1.0024037289
pure-geometry exponent               = 2.0061524985
joint exponent                       = 1.0064429344
joint defect at epsilon=1/64         = 0.02522380790
```

Exact finite-word cutoff theorem:

```text
Jmax >= j_in + r/2
```

For the frozen Euclidean HH word:

```text
j_in=1/2
r=4
safe Jmax=5/2
cutoff error above support wall = 0
```

Declared conservative Lorentzian HH support wall:

```text
Jmax=13/2.
```

---

## I. TT sector

### I1. Propagator positive control

Evidence:

- `TT_PROPAGATOR_FIRST_PASS.md`
- `scripts/tt_propagator_first_pass.py`

Certificate includes a massless leading TT pole and the expected inverse-momentum equal-time covariance.

Bare reduced-control coefficients:

```text
eta2_bare  = -1/45
zeta4_bare = -1/12
```

These are control-model values, not silently promoted to final interacting microscopic coefficients.

### I2. Vacuum two-point function

Evidence:

- `TT_VACUUM_TWO_POINT_RESULT.md`
- `scripts/tt_vacuum_two_point_gate.py`

The Gaussian TT vacuum covariance and polarization structure are independently checked.

---

## J. Complete S4 quartic TT observable space

Evidence:

- `S4_TT_QUARTIC_COMPLETE_BASIS.md`
- `scripts/s4_tt_quartic_complete_basis_gate.py`
- `C6_TO_TT_WILSON_COEFFICIENTS.md`
- `scripts/c6_tt_wilson_extractor.py`

Exact quotient result:

```text
physical parity-even quartic TT dimension = 6
```

Extraction rank:

```text
100/110/111 set = rank 5
adding 120      = rank 6
det A           = 1/699840000
```

The six-vector is therefore the general quartic pole datum in this symmetry class:

```text
c_IR = (c1,c2,c3,c4,c5,c6).
```

### J1. Local transfer and tetrahedral moments

Evidence:

- `NEAREST_BLOCK_S3_TRANSFER_CLOSURE.md`
- `scripts/nearest_block_s3_transfer_gate.py`

A reciprocal face-sharing nearest-neighbor transfer reduces to two symmetric 2x2 multiplicity matrices: six real amplitudes. The tetrahedral neighbor stencil has an isotropic second moment and a symmetry-resolved fourth moment.

### J2. On-shell invariance

Evidence:

- `ON_SHELL_TT_WILSON_INVARIANCE.md`

Four-derivative pieces proportional to the leading TT equation of motion are field-redefinition redundant on shell; the physical quartic pole quotient remains six-dimensional.

### J3. Nested birefringence tests

Evidence:

- `TETRAHEDRAL_TT_BIREFRINGENCE_THEOREM.md`
- `scripts/tetrahedral_tt_birefringence_gate.py`

The single-tetrahedral subspace gives the frozen high-symmetry polarization splitting pattern; failure of this nested submodel does not invalidate the full six-dimensional basis.

---

## K. Constraint resolvent and observable dictionary

### K1. Feshbach / Krylov identity

Evidence:

- `FESHBACH_INTERBLOCK_EFFECTIVE_KERNEL.md`
- `scripts/feshbach_block_krylov_identity_gate.py`

For a specified Hermitian constraint operator and carrier V, the projected resolvent and K/A/B block identities are exact. The spectral parameter is retained as a constraint-spectrum variable unless a physical-time construction is explicitly supplied.

### K2. Real observable map

Evidence:

- `TT_TO_REAL_PHYSICS_OBSERVABLES.md`
- `scripts/s4_tt_six_wilson_predictor.py`
- `scripts/physical_scale_prediction_bridge.py`

For a frozen branch

```text
omega_sigma^2 = c^2 k^2 [1 + a_*^2 k^2 e4_sigma(n) + ...]
```

the code maps the TT eigenvalues to:

```text
polarization-resolved group velocity
accumulated phase
alpha=4 modified-dispersion coefficient A4
```

Common scale convention:

```text
lambda_R_eff = a_*^2/(8*pi*l_P^2).
```

The translator performs no fitting.

---

## L. Closure semantics

The machine ledger separates:

```text
closure_role = core
  statuses: proved, tested_finite, conditional

closure_role = extension
  status: external_extension

closure_role = experiment
  status: experimental_test
```

A stronger extension is not allowed to turn the core back into an “open theory”. An external experiment is not allowed to be counted as an internal derivation.

The package is internally closed when every `core` gate has one of the accepted core statuses and the runtime integration regression passes.

---

## M. What remains scientifically uncertain

The central uncertainty is no longer “what is the theory?” but **whether this closed candidate describes nature and how universal its continuum phase is**.

Examples:

```text
arbitrary-graph universality theorem        -> extension
uniform unbounded-refinement theorem        -> extension
independent implementation/replication      -> extension/test
blind GW dispersion/birefringence analysis  -> experiment
physical scale calibration then holdout      -> experiment
```

These are catalogued in `PREDICTIONS_AND_EXPERIMENTAL_TESTS.md` and in the non-core roles of `theory_gates.json`.

---

## N. Reproducibility certificate

The single canonical workflow is:

```text
.github/workflows/core-regression.yml
```

It is the authoritative machine rerun. The workflow regenerates the practical core calculations directly and reconstructs the expensive historical physicalization certificates from their certified exact source-column artifacts with fresh assembly checks.

The intended interpretation of a green run is:

```text
repository-internal candidate theory package reproduced: YES
experimental confirmation of nature:                    NOT IMPLIED
```
