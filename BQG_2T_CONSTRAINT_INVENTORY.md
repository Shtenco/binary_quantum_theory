# BQG → 2T constraint inventory

Status: **audit layer / not a positive 2T claim**.

This document freezes what the repository actually has before any attempt to identify a Bars-type `Sp(2,R)` sector.

## 1. Required Bars data

A genuine Bars-style two-time embedding requires, at minimum, three first-class constraints which can be represented in a canonical phase space by the quadratic prototype

\[
Q_{11}=X^2,\qquad Q_{12}=X\cdot P,\qquad Q_{22}=P^2,
\]

with an `Sp(2,R)` Poisson/commutator algebra, together with a parent Lorentzian structure of signature `(d,2)` and an explicit gauge reduction to a one-time shadow. Bars' formulation identifies `Sp(2)` duality and `SO(d,2)` symmetry as the characteristic structures of the two-time construction. citeturn0academia3turn0academia1

The BQG audit therefore separates four logically independent gates:

```text
A. operator/constraint algebra
B. canonical two-time sector
C. parent metric signature (d,2)
D. explicit 2T -> 1T gauge reduction
```

Passing A does not automatically pass B–D.

## 2. Existing BQG constraint evidence

### HDA / Hamiltonian sector — PRESENT

`DEWITT_HDA_UNIQUENESS.md` defines the continuum Hamiltonian family

\[
H_c[N]=\int d^3x\,N\left[\frac{\pi_{ab}\pi^{ab}-c\pi^2}{\sqrt q}-\sqrt qR\right]
\]

and derives the HDA bracket defect proportional to `4(c-1/2)`. The declared GR value is therefore `c=1/2`. This is a continuum identity/control, not yet a microscopic `Sp(2,R)` triple. 

### Graph-changing HDA — PRESENT AS FINITE CONTROL

`THREE_NODE_GRAPH_HDA_RESULT.md` contains a genuine finite three-node graph-changing calculation with nonconstant lapse functions, retained graph-change sectors, and a regulator hierarchy whose joint defect scales approximately as `epsilon^1.0064`. The repository explicitly labels this `HDA_3NODE = tested_finite`, not an arbitrary-graph theorem.

### Physicalization bridge — PRESENT AS INTERFACE, NOT CLOSED

`HAMILTONIAN_CONSTRAINT_TO_EFFECTIVE_ACTION.md` defines the legal chain

\[
\{C_A\}\to M_G\to P_{phys}/\eta\to Z_{phys}[J]\to W_{phys}[J]\to\Gamma\to\Gamma^{(2)}_{physical}.
\]

It explicitly states that the theory-specific physical history/inner product remains open.

### Relational history — PRESENT AS FINITE EXACT CONTROL

The repository's C8 construction uses

\[
G=S_{clock}\otimes R_{geom},\qquad
P_{rel}=\frac18\sum_{\tau=0}^{7}G^\tau.
\]

This proves a finite relational-history projector construction, but `Z8` is a finite cyclic group and is not itself `Sp(2,R)`.

## 3. What is NOT yet an identified BQG constraint

The audit does **not** currently treat the following as established physical constraints:

```text
Q11 = X^2
Q12 = X·P
Q22 = P^2
```

Nor does it treat `J`, `C8`, a Feshbach spectral variable, or an arbitrary 3-dimensional matrix subspace as an `Sp(2,R)` realization.

In particular:

```text
C8 history generator != continuous Sp(2,R) gauge generator
constraint spectrum != physical frequency
HDA != Sp(2,R)
```

These distinctions are hard gates, not wording preferences.

## 4. Candidate extraction rule

A candidate triple may enter the closure scan only if each member has an independent repository definition as one of:

1. microscopic graph-changing constraint/operator;
2. Hamiltonian constraint;
3. diffeomorphism/route-normal constraint;
4. Gauss/frame constraint;
5. relational/history generator;
6. a mathematically derived linear combination whose coefficients are fixed before closure is inspected.

An arbitrary fitted linear combination chosen to maximize closure is rejected.

## 5. Closure criterion

For candidate operators `C_i`, compute

\[
[C_i,C_j]=i\hbar\sum_k f_{ij}^{\ k}C_k+R_{ij}.
\]

At finite regulator the scan records:

```text
closure residual ||R||
ranks of candidate span
Jacobi residuals
structure constants
Killing form signature
refinement dependence
```

A positive `Sp(2,R)` identification requires:

```text
rank = 3
Jacobi -> 0
Killing signature = (2,1) up to convention
nondegenerate structure constants
residual -> 0 under the declared refinement
```

The Killing-form signature is a discriminator: compact `su(2)`-type closure is not `sl(2,R) ~= sp(2,R)`.

## 6. Canonical-sector gate

Only after algebraic closure may we ask whether there exist operators/coordinates

\[
(\tau_1,\tau_2,p_1,p_2)
\]

with the required symplectic rank and two timelike directions. The map must be derived from BQG observables, not introduced by hand.

## 7. Signature gate

The parent metric must have exactly two timelike directions:

\[
\operatorname{signature}(G_{parent})=(d,2).
\]

The existing BQG result `d_history≈4` is not sufficient: a history dimension count is not a metric signature.

## 8. Reduction gate

A valid positive result must explicitly exhibit

\[
(d,2)\longrightarrow(d-1,1)
\]

through gauge fixing/constraint reduction and recover the already-existing BQG one-time observables without introducing new physical degrees of freedom.

Required checks:

```text
symplectic form reduces correctly
one physical time remains
BQG HDA/kinematics recovered
no negative-norm physical states
observables gauge-equivalent across admissible gauges
refinement stability
```

## 9. Current verdict

```text
HDA constraint structure             PRESENT / finite+continuum
Graph-changing constraint controls   PRESENT / finite
Relational history                   PRESENT / finite exact
Sp(2,R) algebra                      OPEN
Canonical two-time sector            OPEN
(d,2) parent signature               OPEN
Explicit 2T -> 1T reduction          OPEN
```

The next scientific calculation is therefore **not** to declare 2T, but to expose the actual microscopic operator matrices and run the closure test against them.
