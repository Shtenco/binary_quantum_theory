# Theory status — canonical package

**Canonical status date: 2026-08-18**

```text
core_theory_closed               = true
candidate_mathematical_framework = true
experimentally_confirmed          = false
```

These statements use different scopes and are not contradictory.

`core_theory_closed=true` means that the declared internal candidate construction has an end-to-end evidence chain and no missing core arrow in the repository’s present scope. Evidence may be exact analytic, exact finite-dimensional, reproducible numerical, or conditional on an explicitly named blocking/normalization assumption.

`experimentally_confirmed=false` means that external observations have not established this candidate as the correct theory of nature.

Machine-readable status is `theory_gates.json`; the full evidence index is `CANONICAL_THEORY_PACKAGE.md`.

---

## 1. Canonical closed chain

```text
q=2 binary microstructure
 -> exact refinement fixed point d*=3
 -> regular-tetrahedral Walsh flux carrier
 -> face-qubit / Gauss-singlet geometry carrier
 -> graph-changing active/no-link Peter-Weyl representation
 -> selected recursive PL 3-manifold + exact carrier gluing
 -> B / simplicity / Urbantke metric / compatible connection
 -> Regge / Einstein-Hilbert controls
 -> ADM / DeWitt / HDA structure
 -> Lorentzian coefficient and support controls
 -> spin-2 / TT sector
 -> complete six-dimensional quartic S4 TT quotient
 -> algebraic map to physical observables
```

The core is therefore a closed **candidate mathematical/computational theory package in its declared domain**.

---

## 2. Binary and dimensional closure

The exact q=2 refinement sequence is

```text
N_g = (4*8^g + 10)/7

d_g = 3 + log2(1 - 35/(16*8^(g-1)+40))
```

and approaches 3 monotonically from below. The exact fixed point is

```text
d_* = 3.
```

Finite diagnostics from the frozen train/held-out protocol remain

```text
d_H          = 2.999229782
d_s(slice)   = 3.004393867
z            = 0.998281156
d_s(history) ≈ 4.004393867
```

These are internal construction results, not blind external predictions.

---

## 3. Quantum-geometric carrier

The q=2 Walsh map gives four exact regular-tetrahedron normals:

```text
sum n_a = 0
n_a.n_a = 1
n_a.n_b = -1/3  (a != b)
```

The declared qubit lift gives

```text
Gauss-singlet weight       = 2/9
logical orientation volume = sqrt(3)/4
edge spread                = 0
```

On the selected 16-cell PL completion the same four carriers glue exactly across all 32 shared faces and the dual graph is Q4.

The active four-state q=2 sector plus the graph-changing no-link state realizes the exact `(2,2)+(1,1)` endpoint representation; the frozen q=2 Hamming adjacency factors through active -> no-link -> active transitions. Symmetric blocking then supplies the Peter-Weyl j tower as an explicit conditional representation-growth theorem.

---

## 4. Metric and Einstein sector

Independent gates reconstruct

```text
face qubits -> B -> simplicity -> Urbantke metric -> connection -> curvature
```

and distinguish Einstein from non-Einstein controls.

The logical X/Z shape doublet has an exact rank-two trace-free metric Jacobian.

The L1 q4 S4 metric compression, freshly reassembled from all 24 certified source columns, reports

```text
lambda_E          = 1.1111917875584736
lambda_T2         = 1.0220278507464782
Delta_ET          = 0.08916393681199541
relative_ET_split = 0.08359564595312347
```

so the canonical normalized first-refinement Euclidean tangent split is approximately **8.36%**.

The unit-S4 Lambda≈3 result remains an oracle reconstruction control only.

---

## 5. Peter-Weyl dynamics

The finite quantum-geometry stack includes graph-changing Hamiltonian action, volume/extrinsic-curvature controls, parity/support identities, 32D master normalization, j=1 S4 blocking and the completed 32D higher-shell matrix.

Higher-shell spectrum:

```text
lambda_min = 10.635759878291307
lambda_max = 15.059927665966466
relative non-scalarity = 0.09440461833276048
block-Lanczos residuals ~ 1e-13
```

These are finite constraint-dynamics results. They are not misidentified as an ordinary external-time spectrum.

---

## 6. ADM / HDA / Lorentzian sector

The declared core uses the completed hierarchy of DeWitt/ADM selection, route/diffeomorphism controls, route-normal structure function, Peter-Weyl two-node and three-node graph-changing HDA scaling, exact finite-word cutoff support, and Lorentzian coefficient/support controls.

Three-node measured hierarchy:

```text
route exponent          = 0.9999571195
cross exponent          = 1.0024037289
pure-geometry exponent  = 2.0061524985
joint exponent          = 1.0064429344
joint defect @ 1/64     = 0.02522380790
minimum graph-change fraction = 0.4440331635
```

For the frozen Euclidean HH word, Jmax=5/2 is exactly support-safe; the conservative declared Lorentzian HH wall is Jmax=13/2.

An arbitrary-graph theorem over every possible graph/habitat is a stronger extension, not a missing core calculation.

---

## 7. Regge and held-out continuum control

The preregistered continuation

```text
Z_L = 1/8 + C/L^2 + D/L^4
```

was fitted only on L=3,4,5 and predicted

```text
Z6_pred = 0.11876923193907167
```

before comparison to

```text
Z6_obs = 0.11876075461190198
relative error ≈ 0.00714 %.
```

This is an internal held-out numerical validation, not an external observation of nature.

---

## 8. TT and quartic observable closure

The reduced TT positive control is massless and has the expected inverse-momentum equal-time covariance. The generic parity-even S4 quartic TT quotient has exactly six independent physical structures.

The exact extraction system has

```text
rank(100,110,111) = 5
rank(+120)        = 6
det A             = 1/699840000
```

The on-shell six-dimensional pole quotient is invariant under local field redefinitions proportional to the leading TT equation of motion.

The theory therefore has a complete algebraic observable dictionary from a frozen six-vector to the two TT polarization eigenvalues and onward to modified-dispersion, velocity and phase observables.

---

## 9. Status categories

The v2 machine ledger has no generic `open` status. Instead it separates:

```text
CORE:
  proved
  tested_finite
  conditional

NON-BLOCKING EXTENSION:
  external_extension

EXPERIMENTAL LAYER:
  experimental_test
```

Examples of non-blocking extensions are a theorem uniform over arbitrary graph families or an unbounded refinement family. Those can strengthen universality but do not reopen the declared core.

Experimental tests are similarly separate. Failure of an external test would falsify or constrain the candidate; absence of such a test does not make the internal mathematical package unfinished.

---

## 10. Experimental boundary

The repository does **not** claim:

```text
experimental confirmation of quantum gravity
physical cosmological constant Lambda=3
blind prediction of d≈3 or z≈1
Standard-Model mass derivation from the current gravity-only package
```

The external programme is specified in `PREDICTIONS_AND_EXPERIMENTAL_TESTS.md` and must use frozen outputs, one common scale rule and no post-hoc retuning.

---

## 11. Canonical verification

The single workflow `.github/workflows/core-regression.yml` is the canonical machine certificate. It verifies the present core, the restored physicalization gates, the held-out Regge regression, the complete TT quartic basis and the artifact-backed higher-shell/L1 metric certificates.

A green workflow means:

```text
internal declared theory package reproduced = yes
experimental truth established              = no
```
