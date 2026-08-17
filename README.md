# Information Graph Theory: binary quantum microstructure → smooth GR

This repository studies a **candidate mathematical/computational route to quantum gravity** in which the microscopic degrees of freedom are discrete and binary, while smooth spacetime geometry is required to emerge only after quantum-geometric reconstruction, coarse-graining/refinement and a controlled continuum limit.

The project is deliberately scoped to one chain:

```text
frozen binary/qubit microstructure
        ↓
quantum-geometric carrier
        ↓
discrete metric / curvature / constraints
        ↓
coarse-graining + refinement
        ↓
Einstein / ADM / HDA continuum behaviour
```

It is **not an experimentally established theory of nature**. Exact finite-dimensional theorems, numerical finite tests, conditional composition results and open physical transitions are kept separate in `theory_gates.json` and `THEORY_STATUS.md`.

---

## 1. Binary microscopic rule and scale

The frozen route family uses q binary labels per local rewrite. In the declared train/held-out protocol, q=2 is selected from q∈{1,2,3} before the held-out generation.

For the current q=2 finite protocol:

```text
d_H          = 2.999229782
d_s(slice)   = 3.004393867
z            = 0.998281156
d_s(history) ~ 4.004393867
```

and the observer-smoothing control gives

```text
metric fluctuation   ~ b^-2.001707
gradient fluctuation ~ b^-3.001458
curvature proxy      ~ b^-4.000524
```

These are finite model results. Dimension and z entered the selection protocol, so they are not later counted as blind physical predictions.

The microscopic cutoff is written \(\ell_*\). Identifying \(\ell_*\) with the Planck length is a physical hypothesis until a common scale-setting mechanism is derived.

---

## 2. New exact bridge: q=2 route bits → tetrahedral flux → geometry qubit

The four frozen q=2 route labels are

\[
G=\mathbb Z_2^2=\{00,01,10,11\}.
\]

Take the three nontrivial real Walsh characters of \(G\):

\[
\Phi(g)=\frac1{\sqrt3}
(\chi_1(g),\chi_2(g),\chi_3(g)).
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

So the four microscopic labels themselves form the four unit face normals of a regular tetrahedron. No target angle, random B-field or background metric is fitted to obtain this frame.

Under the declared Pauli/Bloch lift

\[
\rho_f=\frac12(I+n_f^i\sigma_i),
\]

the exact four-spin Gauss-singlet projection gives

```text
flux closure norm                  = 0
Gauss-singlet weight               = 2/9
logical geometry Bloch             ≈ (0,+1,0)
oriented-volume eigenvalue         = sqrt(3)/4
reconstructed tetrahedron spread   = 0
orientation reversal               ≈ (0,-1,0)
```

Machine gate: `scripts/micro_walsh_qgeom_gate.py`.

Detailed result: `MICRO_WALSH_QGEOM_BRIDGE.md`.

**Claim boundary:** this is an exact local carrier theorem inside the declared quantum lift. It does not by itself derive the complete noncommutative Peter-Weyl operator dynamics from classical character multiplication.

---

## 3. Exact global gluing on the selected q=2 PL completion

The selected global completion is the boundary of the 4D cross-polytope:

- 16 tetrahedral cells;
- 32 triangular shared faces;
- four canonical face colours per tetrahedron, given by the omitted coordinate axis;
- those four colours map to q=2 labels `00,01,10,11`;
- the dual graph is exactly \(Q_4\);
- neighboring tetrahedra differ by one sign bit and have opposite parity orientation;
- outward q=2 Walsh flux cancels pairwise on every shared face.

Machine gate: `scripts/q2_global_face_qubit_gluing_gate.py`.

This proves exact **kinematic compatibility** of the local carrier with the selected PL completion. It does not prove that the microscopic dynamics uniquely selects this global phase.

---

## 4. Qubit → B → metric → Einstein control

The independent Euclidean reconstruction chain is

\[
\rho_f
\to B^i
\to \Delta_{simp}
\to g_U
\to A_B
\to F(A_B).
\]

`scripts/qubit_to_einstein_end_to_end.py` reconstructs the declared S4 positive control and rejects a non-Einstein negative control after the metric stage.

The internal S4 reconstruction yields \(\Lambda\simeq3\), but this is **not** a prediction of the physical cosmological constant: the S4 geometry is an oracle control.

Related finite gates:

- `scripts/plebanski_urbantke_gate.py`
- `scripts/plebanski_connection_einstein_gate.py`
- `scripts/regge_eh_cubic_bridge.py`
- `regge_flat_lattice.py`

---

## 5. Smoothness means coarse resolution, not a distance force

The useful wall analogy is purely about resolution: nearby microscopic structure can be resolved, while a coarse observer averages many microscopic degrees of freedom into one effective cell.

Schematically

\[
\mathcal G_{micro}
\xrightarrow{\mathcal C_b}
\mathcal G_{eff}(b).
\]

The wall or spacetime does not become physically smoother because the observer moves away; the effective description becomes smoother because the accessible resolution is coarser.

---

## 6. HDA as the decisive dynamical test

Classical canonical GR satisfies

\[
\{H[N],H[M]\}
=D\!\left[q^{ab}(N\partial_bM-M\partial_bN)\right].
\]

The quantum target is the corresponding commutator on a common off-shell graph-changing domain.

The repository now has a hierarchy of increasingly strong controls:

1. path-vector and rerouting diffeomorphism gates;
2. route-normal principal-symbol HDA;
3. exact no-go for a fully factorized geometry-only Hamiltonian;
4. frozen two-node Peter-Weyl × route regression;
5. **frozen three-node graph-changing Peter-Weyl × route regression**.

The three-node gate retains j=0 cylindrical graph-reduction outputs rather than projecting them away. `core-regression #414` measured

```text
pair supports                         = 510, 648, 648
minimum graph-change norm² fraction  = 0.4440331635
union reduced colored-graph orbits   = 31
route exponent                        = 0.9999571195
cross exponent                        = 1.0024037289
pure-geometry exponent                = 2.0061524985
joint exponent                        = 1.0064429344
joint defect at epsilon=1/64          = 0.02522380790
```

Detailed result: `THREE_NODE_GRAPH_HDA_RESULT.md`.

This justifies `HDA_3NODE = tested_finite`. It does **not** justify `HDA_MULTI = proved`: arbitrary graphs, held-out habitats and full Lorentzian amplitudes remain open.

---

## 7. Joint epsilon / Peter-Weyl cutoff control

For a finite word of fundamental holonomies, if a link begins at spin \(j_{in}\) and is hit at most r times, no amplitude can appear above

\[
j_{in}+r/2.
\]

Thus a truncation with

\[
J_{max}\ge j_{in}+r/2
\]

is exact for that word.

For the frozen all-j=1/2 three-node Euclidean HH family:

```text
max hits/link = 4
safe Jmax     = 5/2
cutoff error  = exactly 0 above the wall
joint HDA fit = epsilon^1.0064429344
```

For the declared full Lorentzian HH support analysis, the conservative wall is `Jmax=13/2`.

Detailed result: `JOINT_REGULATOR_LIMIT.md`.

This establishes `JOINT_FIXED_INPUT = tested_finite` with an exact support theorem. The uniform refinement problem with growing graph/collective-spin size remains open.

---

## 8. Current machine-readable status

The most important new subgates are

```text
MICRO_WALSH_TETRA  = proved
MICRO_GLOBAL_GLUE  = proved
HDA_3NODE          = tested_finite
JOINT_FIXED_INPUT  = tested_finite
```

The stronger frontiers remain

```text
MICRO_TO_QGEOM = open
HDA_MULTI      = open
JOINT_LIMIT    = open
PHYS_PRED      = open
```

This is intentional. A finite PASS is not silently promoted into a theorem over arbitrary graph families or into an experimental claim.

---

## 9. Why PHYS_PRED is still open

A valid first blind physical prediction must not reuse a target that already entered model selection or an oracle control.

Therefore the following are explicitly excluded as the first blind prediction:

- spatial dimension near 3;
- z near 1;
- 4D-like history scaling;
- the S4 oracle value \(\Lambda=3\).

Before opening an external target value, the repository must freeze:

```text
observable and units
microscopic estimator
one common physical scale map
all model parameters
allowed calibration data
forbidden fitting operations
uncertainty model
accept/reject threshold
held-out external dataset identity/hash
```

See `PHYSICAL_PREDICTION_FREEZE_CRITERIA.md`.

---

## 10. Reproduction

```bash
python -m pip install -r requirements.txt
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
python bcqg_quantum_hda_killer.py
python bcqg_bit_to_gravity_final.py --strict
```

`joint_regulator_limit_gate.py` consumes the machine-readable three-node output generated by CI.

The single canonical GitHub workflow is `.github/workflows/core-regression.yml`.

---

## 11. Key files

| Purpose | File |
|---|---|
| Central binary → continuum formulation | `BIT_TO_SPACETIME_CENTRAL_EQUATION.md` |
| Exact q=2 local/global geometry carrier | `MICRO_WALSH_QGEOM_BRIDGE.md` |
| Qubit → Einstein control | `QUBIT_TO_EINSTEIN_END_TO_END.md` |
| Regge → EH bridge | `REGGE_EH_CUBIC_BRIDGE.md` |
| HDA structural target | `GRAPH_CHANGING_HDA_TARGET.md` |
| Three-node graph-changing result | `THREE_NODE_GRAPH_HDA_RESULT.md` |
| Fixed-input joint limit | `JOINT_REGULATOR_LIMIT.md` |
| Blind-prediction rules | `PHYSICAL_PREDICTION_FREEZE_CRITERIA.md` |
| Canonical human status | `THEORY_STATUS.md` |
| Machine ledger | `theory_gates.json` |
| Remaining tasks | `OPEN_PROBLEMS.md` |

The project’s standard is not maximum claim size. It is a single chain in which every arrow is either proved, reproducibly tested, explicitly conditional or still open.
