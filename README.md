# Information Graph Theory — canonical closed candidate package

**Repository status (18 August 2026): INTERNALLY CLOSED mathematical/computational candidate theory.**

**Experimental status: NOT experimentally established as a theory of nature.**

Those two statements are intentionally separate. “Closed” here means that the declared core construction is assembled end-to-end, its required arrows have explicit analytic, exact finite-dimensional, reproducible numerical, or explicitly conditional certificates, and the repository has a single machine-verifiable evidence chain. It does not mean that every stronger theorem over arbitrary graphs has been proved, nor that nature has passed the external tests.

The canonical core is:

```text
binary q=2 microstructure
  -> exact dimension-three refinement fixed point
  -> tetrahedral flux / face-qubit carrier
  -> graph-changing q=2 -> Peter-Weyl link representation
  -> selected recursive PL 3-manifold and exact carrier gluing
  -> B-field / simplicity / Urbantke metric / connection
  -> Regge / Einstein-Hilbert and ADM / DeWitt structure
  -> quantum HDA finite graph-changing controls + Lorentzian support
  -> spin-2 / transverse-traceless sector
  -> complete six-dimensional S4 quartic TT observable basis
  -> physical observable dictionary and experimental test protocol
```

The detailed evidence index is in `CANONICAL_THEORY_PACKAGE.md`. Observational consequences and tests are isolated in `PREDICTIONS_AND_EXPERIMENTAL_TESTS.md`.

---

## 1. Microscopic selector and emergent dimension

The frozen local rewrite uses q=2 binary route labels. The exact refinement count derived in the physicalization calculations is

```text
N_g = (4*8^g + 10)/7

d_g = log2(N_g/N_(g-1))
    = 3 + log2(1 - 35/(16*8^(g-1)+40))
```

Therefore every finite step is below 3 and the sequence increases monotonically to the exact fixed point

```text
d_* = 3.
```

The earlier finite train/held-out observables remain useful diagnostics:

```text
d_H          = 2.999229782
d_s(slice)   = 3.004393867
z            = 0.998281156
d_s(history) ≈ 4.004393867
```

The observer coarse-resolution control gives approximately

```text
metric fluctuation   ~ b^-2.001707
gradient fluctuation ~ b^-3.001458
curvature proxy      ~ b^-4.000524
```

Dimension and z participated in model construction/selection, so they are internal closure evidence, not advertised as blind external predictions.

---

## 2. Exact q=2 geometry carrier

The four route labels form Z2^2. The three nontrivial real Walsh characters map them to four vectors with exact Gram matrix

```text
n_a · n_a = 1
n_a · n_b = -1/3  for a != b
sum_a n_a = 0
```

Thus the route labels produce the four unit normals of a regular tetrahedron without fitting a target angle or metric.

Under the declared qubit lift and Gauss-singlet projection:

```text
flux closure norm                = 0
Gauss-singlet weight             = 2/9
logical Bloch vector             ≈ (0,+1,0)
oriented-volume eigenvalue       = sqrt(3)/4
reconstructed edge spread        = 0
orientation reversal             ≈ (0,-1,0)
```

The selected 16-cell PL completion then gives exact global gluing:

```text
16 tetrahedral cells
32 shared triangle faces
dual graph = Q4
four q=2 face colours per tetrahedron
opposite outward Walsh flux cancels on every shared face
```

The graph-changing no-link state supplies the missing state needed for the Peter-Weyl link representation:

```text
4 active q=2 labels + 1 no-link/j=0 state
    -> SO(5) vector carrier
    -> (2,2) + (1,1) under SU(2)_L x SU(2)_R
```

and the frozen q=2 Hamming adjacency factors exactly through two graph-changing transporter steps.

---

## 3. Metric, curvature and Einstein controls

The independent geometry chain is

```text
face qubits
 -> B variables
 -> simplicity/nondegeneracy
 -> Urbantke metric
 -> compatible connection
 -> curvature
 -> Einstein control
```

The repository also contains the exact local logical-shape -> metric Jacobian. The logical X/Z shape doublet maps with rank two to orthogonal equal-norm trace-free metric tangents, while the two orientation branches give the same intrinsic metric Jacobian.

The freshly reassembled L1 q4 six-edge compression from all 24 certified source columns gives

```text
lambda_E            = 1.1111917875584736
lambda_T2           = 1.0220278507464782
Delta_ET            = 0.08916393681199541
relative_ET_split   = 0.08359564595312347
```

where `relative_ET_split = Delta_ET / ((lambda_E+lambda_T2)/2)`. Thus the canonical first-refinement Euclidean tangent split is about **8.36%**. This quantity is a finite local tetrahedral spin-2 anisotropy precursor; it is not by itself a particle mass ratio or an externally measured Wilson coefficient.

The S4 Einstein oracle reconstruction produces Lambda≈3 in its unit-radius control geometry. That number is a reconstruction check of the supplied oracle geometry, not a prediction of the physical cosmological constant.

---

## 4. Peter-Weyl dynamics and higher shells

The canonical Peter-Weyl calculations include the j=1/2 logical sector, finite graph-changing Hamiltonian action, volume/extrinsic-curvature controls, parity/support theorems, and higher-shell return dynamics.

The exact 32-dimensional higher-shell calculation gives

```text
lambda_min(Lambda) = 10.635759878291307
lambda_max(Lambda) = 15.059927665966466
relative distance from scalar identity = 0.09440461833276048
block-Lanczos reconstruction residuals  ~ 1e-13
```

A separate 32D master-normalization gate checks the nonlinear support-projector normalization before tracing the logical environment. The j=1 S4 block calculation also identifies the multiplicity-one coarse geometry doublet used as a representation-RG consistency check.

These are finite quantum-constraint dynamics. They are not re-labelled as an ordinary external-time Hamiltonian.

---

## 5. ADM / HDA / Lorentzian closure evidence

The structural gravity layer combines:

```text
DeWitt / ADM parameter selection
route-vector and rerouting diffeomorphism controls
route-normal HDA structure function
factorization no-go control
Peter-Weyl x route two-node regression
Peter-Weyl x route three-node graph-changing regression
finite-word Peter-Weyl cutoff theorem
Lorentzian coefficient/support controls
```

The frozen three-node calculation retained j=0 graph-changing outputs and measured

```text
pair supports                        = 510, 648, 648
minimum graph-change norm^2 fraction = 0.4440331635
union reduced graph orbits           = 31
route exponent                       = 0.9999571195
cross exponent                       = 1.0024037289
pure-geometry exponent               = 2.0061524985
joint exponent                       = 1.0064429344
joint defect at epsilon=1/64         = 0.02522380790
```

For the frozen all-j=1/2 Euclidean HH word:

```text
maximum hits per link = 4
exact safe Jmax       = 5/2
cutoff error above wall = 0
```

The conservative support wall for the declared Lorentzian HH word is Jmax=13/2.

Stronger arbitrary-graph or uniform-unbounded-refinement theorems are catalogued as **non-blocking extensions**, not as missing arrows in the declared core package.

---

## 6. Regge continuum and held-out prediction control

The Regge/EH bridge is complemented by a preregistered held-out continuation of the TT residue. Using only L=3,4,5, the frozen rule

```text
Z_L = 1/8 + C/L^2 + D/L^4
```

predicted

```text
Z6_pred = 0.11876923193907167
```

before opening the independent L=6 value

```text
Z6_obs  = 0.11876075461190198
relative error ≈ 0.00714 %
```

This is a genuine internal held-out numerical control. It is not presented as an external experimental confirmation of quantum gravity.

Directional Regge Hessian calculations for axial, diagonal-2 and diagonal-3 directions provide independent finite-lattice checks of the approach to the common continuum tensor structure.

---

## 7. TT propagator and complete quartic observable space

The reduced TT positive-control calculation has a massless leading pole and equal-time vacuum covariance with the expected inverse-momentum scaling. Its bare lattice control coefficients include

```text
eta2_bare  = -1/45
zeta4_bare = -1/12
```

These are positive-control coefficients of the reduced model, not automatically the final microscopic interacting coefficients.

For generic directed momentum, exact S4 representation theory plus TT quotienting gives

```text
13 traceless quartic S4 singlets before TT reduction
6 independent physical parity-even quartic TT structures after reduction
```

The high-symmetry directions 100/110/111 have rank 5. Adding the preregistered direction 120 gives full rank 6 with exact extraction determinant

```text
det A = 1/699840000 != 0.
```

Thus the general quartic pole data are represented by one six-vector

```text
c_IR = (c1,c2,c3,c4,c5,c6).
```

The repository also proves the on-shell field-redefinition invariance of this six-dimensional pole quotient and provides exact nested tests for scalar-cubic and tetrahedral birefringent subspaces.

---

## 8. Real-observable dictionary

For a frozen TT pole branch written schematically as

```text
omega_sigma^2 = c^2 k^2 [1 + a_*^2 k^2 e4_sigma(n) + ...]
```

the repository maps the two polarization eigenvalues to group velocity, accumulated phase and the standard alpha=4 modified-dispersion coefficient. The six-Wilson predictor evaluates the two TT eigenvalues for any sky direction.

The common normalization relation is

```text
lambda_R_eff = a_*^2 / (8*pi*l_P^2).
```

If this overall scale is not independently derived, one declared calibration datum may set it once; independent per-observable rescaling is forbidden.

The observable map is closed algebraically. Actual confrontation with gravitational-wave or other external data is an **experimental test of the closed candidate theory**, documented separately.

---

## 9. What “closed” does and does not mean

Machine status distinguishes three categories:

```text
CORE
  proved / tested_finite / conditional
  -> participates in internal theory closure

EXTENSION
  external_extension
  -> stronger universality/generalization theorem; non-blocking

EXPERIMENT
  experimental_test
  -> held-out real-world validation; non-blocking for mathematical closure
```

Therefore the package can simultaneously report

```text
core_theory_closed                = true
candidate_framework               = true
experimentally_confirmed          = false
```

without contradiction.

---

## 10. Predictions / experimental tests

External tests are deliberately separated from the derivation. See `PREDICTIONS_AND_EXPERIMENTAL_TESTS.md`.

Quantities already used in construction or oracle controls are not counted as blind predictions. In particular:

```text
d≈3                    internal selector/closure evidence
z≈1                    internal selector/closure evidence
4D-like history        internal closure evidence
unit-S4 Lambda≈3       oracle reconstruction control
```

The external layer instead starts from frozen theory outputs and a frozen common scale rule, then tests observational quantities without post-hoc retuning.

---

## 11. Reproduction

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

The canonical workflow is `.github/workflows/core-regression.yml`. It reruns the complete practical regression set and also reconstructs the two expensive artifact-backed physicalization certificates.

Representative direct commands include:

```bash
python scripts/verify_theory_gates.py
python bcqg_observer_smoothing_unified.py
python bcqg_global_manifold_gate.py
python scripts/q2_dimension3_fixed_point_gate.py --max-generation 10
python scripts/micro_walsh_qgeom_gate.py
python scripts/q2_global_face_qubit_gluing_gate.py
python scripts/q2_graphlink_peter_weyl_gate.py
python scripts/logical_shape_metric_jacobian_gate.py
python scripts/qubit_to_einstein_end_to_end.py
python scripts/regge_eh_cubic_bridge.py
python scripts/peter_weyl_master_32_gate.py
python scripts/path_normal_hda_gate.py
python scripts/peter_weyl_three_node_graph_hda_gate.py
python scripts/s4_tt_quartic_complete_basis_gate.py
python scripts/tt_propagator_first_pass.py
python scripts/tt_vacuum_two_point_gate.py
python scripts/tt_regge_zt_l6_gate.py
python scripts/s4_tt_six_wilson_predictor.py --selftest
python bcqg_bit_to_gravity_final.py --strict
```

The expensive higher-shell matrix and L1 q4 metric compression are regenerated in CI from previously certified exact source-column artifacts, with an independent recomputation of the historically heavy higher-shell column before assembly.

---

## 12. Canonical files

| Layer | Canonical evidence |
|---|---|
| Full package index | `CANONICAL_THEORY_PACKAGE.md` |
| Human status | `THEORY_STATUS.md` |
| Machine status | `theory_gates.json` |
| Binary -> continuum formulation | `BIT_TO_SPACETIME_CENTRAL_EQUATION.md` |
| q=2 fixed point | `Q2_DIMENSION3_FIXED_POINT_CLOSURE.md` |
| q=2 quantum geometry | `MICRO_WALSH_QGEOM_BRIDGE.md`, `Q2_GRAPHLINK_PETER_WEYL_BRIDGE.md` |
| Qubit -> metric/Einstein | `QUBIT_TO_EINSTEIN_END_TO_END.md`, `LOGICAL_SHAPE_METRIC_JACOBIAN.md` |
| Regge/EH | `REGGE_EH_CUBIC_BRIDGE.md`, `TT_REGGE_ZT_L6_RESULT.md` |
| HDA | `THREE_NODE_GRAPH_HDA_RESULT.md`, `JOINT_REGULATOR_LIMIT.md` |
| Peter-Weyl higher shells | `PETER_WEYL_HIGHER_SHELL_LAMBDA_RESULT.md` |
| TT quartic space | `S4_TT_QUARTIC_COMPLETE_BASIS.md` |
| Observable map | `TT_TO_REAL_PHYSICS_OBSERVABLES.md` |
| External tests | `PREDICTIONS_AND_EXPERIMENTAL_TESTS.md` |

The repository’s scientific boundary is simple: **the internal candidate construction is closed; experimental truth remains a question for data.**
