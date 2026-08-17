# Open problems — discrete quantum geometry → continuum GR

This file lists only unresolved steps required by the central programme. Recent exact/finite passes deliberately **narrow** the open problems rather than erase them.

```text
binary microphysics
 -> local/global quantum-geometric carrier      [stronger now]
 -> dynamical geometric phase                   [OPEN]
 -> smooth GR controls                          [finite-tested]
 -> arbitrary-graph Lorentzian HDA              [OPEN]
 -> uniform refinement/cutoff limit             [OPEN]
 -> physical scale + blind prediction           [OPEN]
```

---

## 1. Dynamic completion of MICRO_TO_QGEOM

The frozen q=2 labels now give an exact local Walsh-character tetrahedral flux frame, pure face qubits, nonzero Gauss-singlet support and a logical volume eigenstate. The same carrier also glues exactly on the selected 16-cell PL completion.

What remains is stronger:

\[
\boxed{
\text{generic microscopic quantum state + graph-changing update}
\longrightarrow
\text{selected noncommutative Peter-Weyl geometric phase}
}
\]

Required next tests:

1. derive a microscopic update for the face/link quantum variables rather than only a kinematic carrier map;
2. show attraction/measure concentration toward the geometric sector from more than one initial ensemble;
3. derive the growth of the required SU(2)/Peter-Weyl representation content under blocking;
4. recover simplicity/nondegeneracy/coarse B-field scaling without post-hoc projection;
5. include negative controls where the same update fails to form a geometric phase.

The exact Walsh result must not be overstated: commuting group characters do not by themselves derive the full noncommutative SU(2) operator algebra.

---

## 2. Dynamical global-manifold selection

The selected q=2 16-cell completion is a valid recursive PL 3-manifold, and the new face-carrier gluing is exact on it.

Still open:

\[
\boxed{
\text{Why does the microscopic dynamics select this manifold phase?}
}
\]

Distinguish existence from uniqueness, dynamical preference, measure concentration and stability under graph-changing updates.

---

## 3. Arbitrary-graph Lorentzian HDA (`HDA_MULTI`)

The three-node frozen Euclidean gate now satisfies the preregistered finite hierarchy while retaining j=0 cylindrical graph-change outputs. This closes the old requirement “use more than two interacting nodes” only at **tested_finite** level.

The decisive remaining target is

\[
\frac1{i\hbar}[\hat H[N],\hat H[M]]
\to
\hat D[q^{ab}(N\partial_bM-M\partial_bN)]
\]

uniformly over a declared graph-changing off-shell domain.

Next falsifiers must add:

- more graph sizes/topologies, not merely more nodes of one K5 scaffold;
- multiple held-out geometry states and WKB/habitat probes;
- the full Lorentzian geometry Hamiltonian amplitudes on the same domain;
- one independently fixed D/structure-function target;
- absolute and normalized residuals;
- no post-hoc normalization;
- scaling versus both regulator and graph/refinement size.

---

## 4. Uniform joint regulator/refinement theorem (`JOINT_LIMIT`)

For the current finite input, the Peter-Weyl support wall is exact:

\[
J_{max}\ge j_{in}+r/2.
\]

For the three-node all-j=1/2 Euclidean HH family, \(r=4\) and \(J_{max}=5/2\) is already cutoff-exact. Together with the measured \(\epsilon^{1.00644}\) HDA scaling, this controls the fixed-input simultaneous limit.

What remains is a uniform theorem for a refinement family in which graph size, collective spin or hit depth can grow:

\[
\boxed{
\sup_{\Gamma_b,\psi_b}
\Delta_{HDA}(\epsilon,b,J_{max}(b))\to0.
}
\]

Need explicit bounds on \(j_{in}(b)\), hit depth, support growth, cross terms, pure-geometry commutators and habitat norms.

---

## 5. Continuum action/Ward identities from the same microscopic ensemble

Regge/EH, Plebanski/Urbantke and connection controls are finite tests on controlled geometries.

The stronger target is

\[
S_{micro}[\Psi_b]
\longrightarrow
S_{EH}[g_{eff}]
\]

where \(g_{eff}\) is reconstructed from the same microscopic ensemble, not separately supplied to the final estimator.

---

## 6. Lorentzian physical state space

Still required:

- physical inner product or Lorentzian quantum measure;
- complete treatment of first-class constraints;
- reality conditions where applicable;
- relational causal/unitary observables;
- stability of the semiclassical sector.

Finite Euclidean HDA and a Lorentzian support/coefficient gate do not solve this problem.

---

## 7. Physical scale setting

Current strongest results are primarily dimensionless. A theory of nature needs one reproducible map

\[
\text{dimensionless micro-observables}
\to
\{\ell_{phys},t_{phys},E_{phys},G,\ldots\}
\]

with no independent rescaling for each observable.

Identifying the microscopic cutoff with the Planck length is still a hypothesis, not a derived result.

---

## 8. Blind external prediction (`PHYS_PRED`)

Do not use dimension near 3, z near 1, 4D-like history scaling or the S4 oracle \(\Lambda=3\) as the first blind prediction: they are selection-tainted or oracle-tainted.

A valid first prediction requires a committed preregistration containing:

```text
observable and units
microscopic estimator
common scale-setting map
all frozen parameters
allowed calibration data
forbidden fitting operations
uncertainty model
accept/reject threshold
held-out external dataset identity/hash
```

See `PHYSICAL_PREDICTION_FREEZE_CRITERIA.md`.

An internal held-out numerical extrapolation, even at sub-percent error, is not an external physical prediction.

---

## 9. Universality

Challenge q=2 rather than protect it:

- alternative binary local rules with comparable parameter count;
- alternative global completions/refinements;
- multiple microscopic initial-state ensembles;
- different coarse observables and blocking maps;
- perturbations not used in selection;
- larger held-out generations and graph families.

Long-distance GR-like observables should become insensitive to irrelevant microscopic choices if the phase is genuinely universal.

---

## 10. Independent replication

The strongest remaining gates should eventually have:

- deterministic seed or exact derivation;
- machine-readable output;
- preregistered tolerances;
- negative controls;
- runtime/memory metadata;
- CI;
- an independently written implementation.

The goal is not more PASS labels. It is a smaller set of increasingly dangerous falsification tests that remain standing under independent implementations and genuinely held-out data.
