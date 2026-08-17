# Theory status — binary quantum geometry → continuum GR

**Canonical status update: 2026-08-18.**

This repository is a **candidate mathematical/computational framework**, not an experimentally established theory of nature. The central question is deliberately narrow:

```text
Can one frozen binary/qubit microscopic system generate quantum geometry
whose controlled coarse-grained/refined dynamics approaches GR/HDA?
```

Machine-readable status: `theory_gates.json`.

---

## 1. Current chain

```text
frozen q=2 binary route labels
 -> exact local tetrahedral flux carrier
 -> pure face qubits
 -> exact Gauss-singlet logical geometry qubit
 -> exact gluing on selected 16-cell PL completion
 -> SU(2)/Peter-Weyl quantum geometry controls
 -> B / simplicity / Urbantke / connection
 -> Regge / Einstein-Hilbert controls
 -> route-normal HDA structure function
 -> two-node Peter-Weyl x route HDA
 -> three-node graph-changing Peter-Weyl x route HDA
 -> fixed-input joint epsilon/Jmax control
 -> [OPEN] arbitrary-graph Lorentzian HDA + uniform refinement
 -> [OPEN] common physical scale setting
 -> [OPEN] preregistered blind external prediction
```

The distinction between exact, finite-tested, conditional and open arrows is mandatory.

---

## 2. Frozen q=2 geometrogenesis

The existing frozen train/held-out protocol reports

```text
d_H          = 2.999229782
d_s(slice)   = 3.004393867
z            = 0.998281156
d_s(history) ~ 4.004393867
```

and the finite smoothing control reports

```text
metric fluctuation   ~ b^-2.001707
gradient fluctuation ~ b^-3.001458
curvature proxy      ~ b^-4.000524
```

Status: **tested_finite**. Dimension and z participated in rule selection, so they are not eligible to be advertised later as blind predictions.

---

## 3. Exact q=2 route labels → tetrahedral quantum-geometric carrier

For \(G=\mathbb Z_2^2\), the three nontrivial real Walsh characters define

\[
\Phi(g)=\frac1{\sqrt3}(\chi_1(g),\chi_2(g),\chi_3(g)).
\]

Character orthogonality gives exactly

\[
\sum_g\Phi(g)=0,
\qquad
\Phi(g)\cdot\Phi(h)=
\begin{cases}
1,&g=h,\\
-1/3,&g\ne h.
\end{cases}
\]

Thus the same four frozen route labels `00,01,10,11` generate the four unit face normals of a regular tetrahedron with no fitted angle or target metric.

Under the declared Pauli/Bloch quantum lift, `scripts/micro_walsh_qgeom_gate.py` gives

```text
flux closure norm                  = 0
gauss singlet weight               = 0.22222222222222215 ≈ 2/9
logical geometry Bloch             ≈ (0,+1,0)
oriented volume                    = sqrt(3)/4
reconstructed edge relative spread = 0
orientation reversal               ≈ (0,-1,0)
```

Status: **proved inside the declared local carrier construction** (`MICRO_WALSH_TETRA`).

Important boundary: the Walsh characters are commuting functions of the classical route labels. The Pauli/Bloch lift supplies the declared quantum representation; this result alone is not a derivation of the complete noncommutative Peter-Weyl dynamics.

---

## 4. Exact global carrier gluing on the selected PL completion

On the boundary of the 4D cross-polytope:

- 16 tetrahedral cells;
- 32 triangular shared faces;
- four faces of each cell are canonically coloured by the omitted coordinate axis;
- those four colours map to the four q=2 route labels;
- the dual graph is exactly \(Q_4\);
- neighbors differ by one sign bit and have opposite parity orientation;
- opposite outward Walsh fluxes cancel on every shared face.

Status: **proved for the selected completion** (`MICRO_GLOBAL_GLUE`).

Still open: uniqueness/dynamical selection of this global phase and its semiclassical measure by the bare microscopic dynamics.

---

## 5. Qubit → B → metric → Einstein controls

The Euclidean chain

\[
\rho_f\to B^i\to\Delta_{simp}\to g_U\to A_B\to F(A_B)
\]

passes the finite positive and negative controls. The unit-S4 oracle control reconstructs \(\Lambda\simeq3\) to numerical precision, while a non-Einstein conformally flat control fails the Einstein-curvature criterion.

Status: **tested_finite**. The S4 value is an oracle reconstruction, not a prediction of the physical cosmological constant.

---

## 6. Discrete curvature / Einstein-Hilbert controls

The repository keeps separate Regge/EH, geometric-cell, Plebanski/Urbantke and connection/Ward controls.

Status: **tested_finite for the declared finite geometries**. A universal microscopic RG theorem remains open.

---

## 7. HDA target and current hierarchy

The classical target is

\[
\{H[N],H[M]\}
=D\!\left[q^{ab}(N\partial_bM-M\partial_bN)\right].
\]

The quantum target is the corresponding off-shell commutator on one common graph-changing habitat.

Current hierarchy:

1. route-vector/rerouting diffeomorphism gates pass;
2. square-root route-normal generator reproduces the HDA metric structure function at principal-symbol level;
3. a factorized geometry-only Hamiltonian is exactly ruled out;
4. frozen two-node Peter-Weyl × route scaling passes;
5. frozen **three-node graph-changing** Peter-Weyl × route scaling now passes without projecting j=0 outputs away.

Three-node result (`HDA_3NODE = tested_finite`):

```text
pair supports                  = 510, 648, 648
minimum j=0 graph-change frac = 0.4440331635
union reduced graph orbits     = 31
route exponent                 = 0.9999571195
cross exponent                 = 1.0024037289
pure-geometry exponent         = 2.0061524985
joint exponent                 = 1.0064429344
joint defect at epsilon=1/64   = 0.02522380790
```

This is real finite multi-node graph-change evidence, not arbitrary-graph closure. Therefore broad `HDA_MULTI` remains **open** for arbitrary graphs, multiple held-out habitats and full Lorentzian amplitudes on the same domain.

---

## 8. Joint regulator/cutoff result

For a finite fundamental-holonomy word with \(r\) hits on a link,

\[
J_{max}\ge j_{in}+r/2
\]

makes Peter-Weyl truncation exactly inactive.

For the frozen all-\(j=1/2\) Euclidean three-node HH family:

```text
maximum hits/link = 4
safe Jmax         = 5/2
cutoff error      = exactly 0 above the wall
joint epsilon fit = epsilon^1.0064429344
```

The conservative support wall for the declared full Lorentzian HH word is `Jmax=13/2`.

Status: `JOINT_FIXED_INPUT = tested_finite` plus an exact support theorem.

Broad `JOINT_LIMIT` remains **open** for refinement sequences with growing graph size/collective spin and a uniform habitat/norm bound.

---

## 9. What is established inside the declared models

- frozen q=2 finite geometrogenesis/smoothing evidence;
- selected recursive PL 3-manifold completion;
- exact q=2 Walsh regular-tetrahedron carrier;
- exact Gauss-singlet local geometry-qubit projection in the declared lift;
- exact global face-carrier gluing on the selected 16-cell completion;
- finite Peter-Weyl/SU(2) geometry controls;
- finite qubit→B→Urbantke→Einstein control;
- finite Regge/EH and connection controls;
- route-normal HDA principal-symbol result;
- two-node and three-node Euclidean Peter-Weyl × route scaling results;
- exact finite-word cutoff support wall and fixed-input simultaneous cutoff/regulator control;
- fixed-cutoff composition and DeWitt/HDA structural theorems in their stated ansätze.

---

## 10. What remains open

1. **Dynamic MICRO_TO_QGEOM:** show that the same microscopic graph-changing dynamics generates/selects the full noncommutative Peter-Weyl geometric phase and semiclassical measure from generic microscopic states.
2. **Dynamic global phase selection:** show why the good PL completion is selected, not merely available.
3. **HDA_MULTI:** arbitrary-graph, multi-habitat, full Lorentzian off-shell closure.
4. **JOINT_LIMIT:** a uniform theorem along refinement with unbounded graph/collective-spin growth.
5. **Lorentzian physical state space:** physical inner product/measure, constraints and relational unitary observables.
6. **Physical scale setting:** one reproducible map from dimensionless micro-observables to length/time/energy and \(G\), without per-observable fitting.
7. **PHYS_PRED:** one genuinely blind external prediction frozen before the held-out physical value is opened.

---

## 11. Blind-prediction discipline

The following are explicitly disallowed as the first blind prediction:

- spatial dimension near 3;
- \(z\approx1\);
- 4D-like history scaling;
- the S4 oracle value \(\Lambda=3\).

They are selection-tainted or oracle-tainted.

Before an external comparison, the repository must freeze the observable, all parameters, the common physical scale map, forbidden fitting operations, uncertainty model, accept/reject threshold and held-out dataset identity. See `PHYSICAL_PREDICTION_FREEZE_CRITERIA.md`.

`PHYS_PRED` therefore remains **open**.

---

## 12. Canonical regression

```bash
python scripts/verify_theory_gates.py
python bcqg_observer_smoothing_unified.py
python bcqg_global_manifold_gate.py
python scripts/micro_walsh_qgeom_gate.py
python scripts/q2_global_face_qubit_gluing_gate.py
python scripts/qubit_to_einstein_end_to_end.py
python scripts/regge_eh_cubic_bridge.py
python scripts/path_normal_hda_gate.py
python scripts/peter_weyl_two_node_euclidean_joint_gate.py
python scripts/peter_weyl_three_node_graph_hda_gate.py
python scripts/joint_regulator_limit_gate.py --multi-node-json <three-node-result.json>
python bcqg_quantum_hda_killer.py
python bcqg_bit_to_gravity_final.py --strict
```

A green regression certifies the registered finite/exact claims only. It is intentionally insufficient to label the framework an experimentally confirmed theory of quantum gravity.
