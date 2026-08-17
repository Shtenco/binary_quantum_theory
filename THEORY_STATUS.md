# Theory status — binary quantum geometry → continuum GR

**Scope reset: 2026-08-17.**

This file is the canonical human-readable status of the repository. The project is a **candidate mathematical/computational framework**, not an experimentally established theory of nature.

The repository now tracks only one scientific question:

```text
Can a discrete binary/qubit microscopic quantum system produce,
under controlled coarse-graining and regulator removal,
the smooth geometric dynamics of general relativity?
```

The machine-readable counterpart is `theory_gates.json`.

---

## 1. Current core chain

```text
binary local degrees of freedom
 -> frozen q=2 route rule
 -> local S2 shell
 -> selected recursive PL S3 completion
 -> d_slice ~ 3
 -> z ~ 1
 -> 4D-like history scaling
 -> coarse-grained smooth metric candidate
 -> SU(2)/Peter-Weyl quantum geometry
 -> B / simplicity / Urbantke metric reconstruction
 -> discrete curvature / Regge-EH controls
 -> Hamiltonian + diffeomorphism constraints
 -> HDA continuum target
 -> Einstein dynamics in the semiclassical/continuum regime
```

The chain is intentionally split into exact, finite-tested, conditional and open arrows.

---

## 2. Binary dimension and smoothing gate

The frozen train/held-out binary-route experiment reports

```text
d_H          = 2.999229782
z            = 0.998281156
d_s(slice)   = 3.004393867
d_s(history) ~ 4.004393867
```

and finite coarse-graining exponents

```text
metric fluctuation   ~ b^-2.001707
gradient fluctuation ~ b^-3.001458
curvature proxy      ~ b^-4.000524
```

Status: **tested_finite**.

Interpretation: the declared $q=2$ finite rule has the desired dimensional/scaling behaviour on the current train/held-out protocol. These values do not establish a universal law of nature.

Evidence:

- `BIT_TO_SPACETIME_CENTRAL_EQUATION.md`
- `OBSERVER_SCALE_SMOOTHING.md`
- `bcqg_observer_smoothing_unified.py`

---

## 3. Global PL completion

The $q=2$ local shell is the suspension of $Q_2=C_4$, giving an octahedral $S^2$ link. The implemented global gate chooses the boundary of the 4D cross-polytope and verifies its PL 3-manifold properties under barycentric refinement.

Status: **tested_finite / exact for the selected completion**.

What is established: the chosen completion is a consistent recursive PL $S^3$ construction.

What is not established: uniqueness or dynamical selection of that completion by the bare microscopic rewrite.

Evidence:

- `GLOBAL_MANIFOLD_Q2_COMPLETION.md`
- `bcqg_global_manifold_gate.py`

---

## 4. Qubit → Einstein single-data-path control

The Euclidean control

$$
\rho_f
\to B^i
\to \Delta_{simp}
\to g_U
\to A_B
\to F(A_B)
$$

reconstructs the Einstein curvature of a unit-$S^4$ input encoded only through face-qubit density matrices.

Reported positive-control value:

```text
Lambda_rec = 2.999999897308107
Lambda_exact = 3
relative error ≈ 3.423e-8
```

A separate smooth non-Einstein input passes the early reconstruction arrows but fails the final Einstein-curvature criterion.

Status: **tested_finite**.

This is an oracle-encoded composability test. It does not yet derive the required face-qubit state from the microscopic binary rewrite.

Evidence:

- `QUBIT_TO_EINSTEIN_END_TO_END.md`
- `scripts/qubit_to_einstein_end_to_end.py`

---

## 5. Discrete curvature and Einstein-Hilbert bridge

The repository contains independent Regge, geometric-cell and connection/Ward controls intended to test the passage from discrete geometric data to continuum curvature/action.

Status: **tested_finite for the implemented controls**.

Evidence:

- `REGGE_EH_CUBIC_BRIDGE.md`
- `scripts/regge_eh_cubic_bridge.py`
- `scripts/verify_geometric_cell.py`
- `scripts/verify_connection_ward.py`

A full regulator-independent theorem for the microscopic ensemble remains open.

---

## 6. Canonical HDA target

The classical target is

$$
\{H[N],H[M]\}
=
D\!\left[q^{ab}(N\partial_bM-M\partial_bN)\right].
$$

The quantum target is

$$
\frac{1}{i\hbar}[\hat H[N],\hat H[M]]
\longrightarrow
\hat D\!\left[q^{ab}(N\partial_bM-M\partial_bN)\right]
$$

on an appropriate off-shell domain/habitat.

Current sub-results:

1. path-vector and rerouting diffeomorphism kinematics pass their finite scaling tests;
2. the route-normal operator reproduces the correct HDA structure function at principal-symbol level;
3. the old fully factorized geometry-only Hamiltonian is ruled out because it cannot generate the nontrivial path derivative on the right-hand side;
4. a preregistered two-node Euclidean Peter-Weyl × route regression shows the expected hierarchy of route, cross and pure-geometry terms;
5. a fixed-cutoff Lorentzian composition argument gives the declared $O(\epsilon)$ and $O(\epsilon^2)$ relative suppression bounds.

However the central microscopic statement remains:

```text
full graph-changing, multi-node, off-shell quantum HDA: OPEN
```

This distinction is mandatory. A route principal-symbol PASS is not the same as a complete quantum constraint-algebra proof.

Evidence:

- `QUANTUM_HDA_KILLER_RESULT.md`
- `GRAPH_CHANGING_HDA_TARGET.md`
- `PETER_WEYL_TWO_NODE_EUCLIDEAN_RESULT.md`
- `FINAL_CORE_ARCHITECTURE_CERTIFICATE.md`
- `bcqg_quantum_hda_killer.py`
- `scripts/peter_weyl_two_node_euclidean_joint_gate.py`

---

## 7. Fixed-cutoff composition result

At the current regulator-safe finite Peter-Weyl cutoff, the repository records the decomposition

$$
\Delta_{full}
\le
\Delta_{route}
+C_{cross}\epsilon
+C_{GG}\epsilon^2,
$$

with the route target carrying the leading physical-derivative scaling in the declared habitat family.

Status: **proved within the stated fixed-cutoff assumptions / conditional as a statement about the full theory**.

This result does not provide a uniform theorem for an arbitrary simultaneous

$$
J_{max}\to\infty,
\qquad
\epsilon\to0.
$$

Evidence: `FINAL_CORE_ARCHITECTURE_CERTIFICATE.md`.

---

## 8. Current claim boundary

### Supported inside the declared models

- exact algebraic identities explicitly proved in their finite spaces;
- reproducible finite numerical gates;
- the frozen q=2 train/held-out dimension experiment;
- the selected PL completion and refinements;
- the finite qubit-to-Einstein Euclidean control;
- finite Regge/EH and connection controls;
- route-normal HDA principal-symbol result;
- two-node Euclidean Peter-Weyl × route scaling result;
- fixed-cutoff composition bound under its stated assumptions.

### Not established

- that the microscopic binary rule is uniquely selected by nature;
- that the microscopic cutoff is experimentally known to be the Planck length;
- that the required geometric qubit state is dynamically generated rather than prepared as a control;
- full graph-changing multi-node quantum HDA closure;
- a uniform regulator-removal theorem;
- a complete Lorentzian physical Hilbert space and quantum measure;
- derived physical values of $G$, $\Lambda$, particle masses or other dimensional constants from first principles;
- any blind experimental prediction until the prediction protocol is frozen before comparison with data.

---

## 9. Required next milestones

The shortest scientifically meaningful route is:

```text
A. microscopic dynamics
   -> geometric qubit / B-field sector

B. same microscopic dynamics
   -> global manifold phase

C. geometry + route Hamiltonian
   -> graph-changing multi-node off-shell HDA

D. refinement/cutoff sequence
   -> regulator-independent continuum observables

E. physical scale setting
   -> G, time and length units

F. preregistered blind observable
   -> independent comparison with experiment
```

A result in stage F is only a prediction if the observable, parameters, fitting prohibition, uncertainty rule and comparison dataset are fixed before the experimental value is inspected.

---

## 10. Canonical regression commands

```bash
python scripts/verify_theory_gates.py
python bcqg_observer_smoothing_unified.py
python bcqg_global_manifold_gate.py
python scripts/qubit_to_einstein_end_to_end.py
python scripts/regge_eh_cubic_bridge.py
python scripts/path_normal_hda_gate.py
python scripts/peter_weyl_two_node_euclidean_joint_gate.py
python bcqg_quantum_hda_killer.py
python bcqg_bit_to_gravity_final.py --strict
```

These commands define the public core. Experimental side calculations are not allowed to silently upgrade the status of a core claim.
