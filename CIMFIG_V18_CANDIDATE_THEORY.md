# Causal-Invariant Multiway Frame-Infograph Gravity (CIMFIG)

## Status

**Computable architecture candidate. Not a proven theory of nature.**

## 1. Fundamental state

A microscopic state is

\[
\Omega=(H,e,q),
\]

where:

- \(H\) is a finite directed hypergraph;
- \(e\) assigns oriented frame/connection qubits or finite group elements to causal links or local diamonds;
- \(q\) contains matter labels and internal degrees of freedom.

The physical state is not one update history but a multiway history ensemble

\[
|\Psi\rangle=\sum_{\gamma} A[\gamma]|\gamma\rangle.
\]

## 2. Local dynamics

A finite family of local rewrite rules acts as

\[
R_a: (H,e,q)\longrightarrow(H',e',q').
\]

A rule family is admissible only if it passes multiple independent gates.

### Gate C1 — causal critical-pair confluence

Locally divergent update events must reconverge in the causal structure. In the finite implementation this is tested through bounded diamond completion.

### Gate C2 — frame-holonomy confluence

Reconvergent histories must agree on gauge-invariant boundary transport. Structural causal invariance alone does not imply this condition.

### Gate Q1 — history-space isometry

Individual update histories remain orthogonal at the fundamental quantum level. A local step must act isometrically or unitarily on the history Hilbert space.

### Gate Q2 — branchial observation map

Reconverged visible states are obtained by a density matrix, decoherence functional or quantum measure. Their amplitudes must not be naively added in a way that destroys unitarity.

## 3. Quantum measure

A candidate history amplitude is

\[
A[\gamma]
=\prod_{v\in\gamma} w(R_v,\Omega_v)
\exp\!\left(iS_{\rm frame}[\gamma]+iS_{\rm matter}[\gamma]\right).
\]

The weights and phases remain undetermined. They must satisfy normalization, composition, causal consistency and an appropriate positivity/unitarity condition.

## 4. Continuum condition

Let \(\Phi_D\) be a vector of scalar, frame and matter observables on a local causal diamond \(D\). A continuum candidate must satisfy projected, distributional RG convergence:

\[
P_\perp\bigl(\Phi(BD)-R_B\Phi(D)\bigr)\longrightarrow0
\]

in expectation and covariance over the multiway ensemble, while correlation length in lattice units diverges.

A four-dimensional phase must be obtained dynamically rather than inserted through the test corpus.

## 5. Gravity gate

The second variation of the ensemble effective action must possess:

- gauge/foliation null directions;
- exactly two positive gapless transverse-traceless modes;
- \(\omega^2\sim k^2\) in the infrared;
- no scalar ghost or negative-norm physical state;
- nonlinear Ward identities and universal coupling to stress-energy.

V17 showed that the tested scalar spectral-causal action span fails this gate. An oriented frame/connection sector reconstructs the free Fierz–Pauli ratio \(1:-2:2:-1\), but its dynamical emergence is open.

## 6. Matter gate

The theory must generate, rather than assume:

- a non-Abelian internal gauge structure;
- chiral fermions;
- anomaly cancellation;
- stable particle-like configurations;
- universal gravitational coupling;
- a scale-setting observable.

## 7. Falsifiers

CIMFIG is rejected if any of the following persists in the large-system limit:

1. update-order dependence of causal observables;
2. frame holonomy disagreement after reconvergence;
3. nonzero history-space unitarity defect;
4. no interacting four-dimensional critical phase;
5. failure of the microscopic TT Hessian gate;
6. unavoidable ghosts or anomalies;
7. regulator-dependent predictions with no universal limit.
