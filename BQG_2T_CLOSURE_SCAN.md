# BQG → 2T Closure Scan

Status: **falsification-first research specification; no `Sp(2,R)` closure is claimed.**

## 1. Purpose

Test whether the existing Binary Quantum Gravity operator architecture contains a genuine Bars-type two-time parent rather than merely a finite relational-history construction.

The target is an operator/constraint triple

\[
C_1,C_2,C_3
\]

whose classical or quantum algebra closes as `sp(2,R)` (possibly only after a controlled continuum limit), together with a canonical two-time sector and an explicit gauge reduction to the existing one-time BQG dynamics.

Bars' 2T framework uses the canonical constraints

\[
Q_{11}=X^2,\qquad Q_{12}=X\cdot P,\qquad Q_{22}=P^2,
\]

with local `Sp(2,R)` gauge symmetry. The present document tests for this structure; it does not assume it.

## 2. Existing BQG starting point

The current microscopic architecture is spatial quantum-link/spin-network based. The finite theory has exact local `SU(2)` Gauss protection, while the difficult closures are spatial diffeomorphism and Hamiltonian sectors. The architecture explicitly states that the finite Lorentzian update/operator ordering and a held-out continuum run are not yet closed.

Therefore the 2T test must start from the actual BQG generators and constraints, not from symbols imported from 2T.

The C8 relational-history construction

\[
G=S_{clock}\otimes R_{geom},\qquad
P_{rel}=\frac18\sum_{\tau=0}^{7}G^\tau
\]

is retained as an exact control. It is **not** identified with `Sp(2,R)` because finite `Z_8` history is discrete and compact while `Sp(2,R)` is a continuous noncompact Lie group.

## 3. Constraint inventory

Before fitting any algebra, every candidate generator must be assigned one of:

1. **EXACT** — finite operator/matrix definition exists;
2. **CONTROLLED** — defined only after a declared approximation or continuum limit;
3. **PROPOSED** — notation/target only;
4. **ABSENT** — no operator currently exists in the repository.

Minimum inventory:

| Candidate | Required physical role | Acceptance requirement |
|---|---|---|
| `C_G^a` | local Gauss | exact `SU(2)` closure |
| `C_D^a` | spatial diffeomorphism | finite generator plus continuum closure |
| `C_H` | Hamiltonian constraint | Hermitian regulated operator |
| `C_clock` | relational/history generator | must act on a genuine clock sector |
| `C_1,C_2,C_3` | possible 2T constraints | independent operators with closed `sp(2,R)` brackets |

No candidate may be promoted from PROPOSED to EXACT by naming similarity.

## 4. Algebraic scan

For a candidate triple compute

\[
[C_i,C_j]
=i\hbar\sum_k f_{ij}^{\ k}C_k+R_{ij}.
\]

At finite cutoff use a normed residual

\[
\epsilon_{ij}
=\frac{\|R_{ij}\|}{\max(\|[C_i,C_j]\|,\|C_i\|\,\|C_j\|,\epsilon_0)}.
\]

The scan records both the best-fit structure constants and the residual; a small least-squares residual alone is not a proof because arbitrary finite matrices can have accidental approximate relations.

## 5. `sp(2,R)` fingerprint

In a standard basis the algebra is equivalent, up to real linear recombination and normalization, to

\[
\{Q_{11},Q_{12}\}=2Q_{11},
\]
\[
\{Q_{12},Q_{22}\}=2Q_{22},
\]
\[
\{Q_{11},Q_{22}\}=4Q_{12}.
\]

The scan must therefore test:

- rank = 3;
- Jacobi identity;
- nondegenerate Killing form with the `sl(2,R)`/`sp(2,R)` signature;
- stability under regulator/refinement changes;
- absence of a purely compact `su(2)` reinterpretation;
- closure on the same three-dimensional span without an uncontrolled fourth generator.

A finite `Z_8` history projector cannot pass this test by itself.

## 6. Canonical two-time test

A positive algebraic closure is still insufficient. Search for four canonical variables

\[
(\tau_1,\tau_2;p_1,p_2)
\]

with symplectic form

\[
\Omega_t=d\tau_1\wedge dp_1+d\tau_2\wedge dp_2
\]

and two timelike directions in the parent quadratic form.

The parent metric must have signature

\[
\operatorname{sig}(G_{parent})=(d,2)
\]

rather than merely having a history label or an extra Euclidean/internal coordinate.

The canonical variables must be derived from BQG observables/operators. They cannot be introduced solely to force the Bars dictionary.

## 7. Constraint-to-parent reconstruction

If the canonical sector exists, construct

\[
Q_{11}=X^MX_M,
\qquad
Q_{12}=X^MP_M,
\qquad
Q_{22}=P^MP_M.
\]

Then verify that the reconstructed operators agree with the independently extracted BQG generators, up to explicitly stated canonical transformations and regulator corrections.

The strongest positive result is not “BQG resembles 2T”; it is an equivalence class statement:

\[
\text{BQG parent constraints}
\simeq
\{X^2,X\cdot P,P^2\}
\]

with the same physical constraint surface and symplectic reduction.

## 8. Gauge-reduction test

Choose a legitimate gauge fixing that leaves one physical time. Demonstrate

\[
\mathcal P_{2T}\longrightarrow\mathcal P_{1T}
\]

with:

- nondegenerate reduced symplectic form;
- one physical time variable;
- recovery of the BQG Hamiltonian/constraint;
- no negative-norm physical states;
- preservation of Gauss/HDA constraints;
- refinement-independent gauge-invariant observables.

The reduced theory must reproduce the already established BQG leading chain

\[
q=2\to D_{space}=3\to c_{DW}=1/2\to z=1\to 3+1\text{ gravity kinematics}.
\]

## 9. Quantum consistency

For quantized constraints test

\[
[\hat C_i,\hat C_j]
=i\hbar f_{ij}^{\ k}\hat C_k+\hbar^2\mathcal A_{ij}.
\]

Report anomalies separately from truncation error. Physical states must satisfy

\[
\hat C_i|\Psi_{phys}\rangle=0
\]

in the appropriate rigging-map/group-averaging construction.

The scan must also test whether the physical inner product is positive on the reduced one-time sector.

## 10. Falsifiers

The Bars-type 2T hypothesis fails if any of the following persists under refinement:

1. no independent rank-three constraint algebra exists;
2. closure is only `su(2)` or another compact algebra;
3. residuals do not decrease toward the continuum;
4. no canonical two-time symplectic sector can be derived;
5. parent signature is not `(d,2)`;
6. gauge fixing does not reproduce BQG dynamics;
7. physical states contain unavoidable negative-norm modes;
8. the proposed second time is only the existing discrete history register.

A failure is a scientific result: it separates the relational-history mechanism from genuine 2T gauge structure.

## 11. Positive evidence ladder

**Level 0:** finite relational-history control only.

**Level 1:** approximate three-generator closure.

**Level 2:** stable `sp(2,R)` closure under refinement.

**Level 3:** derived canonical `(tau_1,tau_2;p_1,p_2)` sector.

**Level 4:** derived `(d,2)` parent metric and constraints.

**Level 5:** explicit 2T→1T gauge reduction reproducing BQG.

**Level 6:** quantum anomaly/inner-product control and regulator-independent observables.

Only Level 5–6 would justify calling the BQG construction a genuine 2T completion rather than an analogy or effective embedding.

## 12. Immediate implementation order

1. Inventory the repository for exact Gauss, diffeomorphism, Hamiltonian, clock/history, and graph-changing operators.
2. Mark every candidate EXACT/CONTROLLED/PROPOSED/ABSENT.
3. Build finite matrix representations where definitions are exact.
4. Compute commutator tensors and closure residuals.
5. Search rank-three spans and classify their Lie algebra.
6. Repeat across spin/refinement/volume sectors.
7. Only if a stable rank-three candidate survives, attempt canonical reconstruction and signature extraction.
8. Only after that attempt gauge reduction.

This ordering prevents the common failure mode of starting with a desired `(3,2)` metric and reverse-engineering constraints to fit it.

## 13. Current conclusion

The repository already contains a strong 3+1/HDA research programme and an exact finite relational-history control, but the present evidence does **not** establish a second timelike dimension or an `Sp(2,R)` gauge symmetry.

The decisive next experiment is therefore the closure scan, followed by canonical/signature reconstruction only if the algebraic gate passes.
