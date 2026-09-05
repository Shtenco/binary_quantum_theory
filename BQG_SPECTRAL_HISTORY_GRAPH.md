# BQG spectral-history graph: exact finite-regulator closure, scope, and audit

Status: **executable finite-regulator spectral theorem + fail-closed production interface. The theory-specific physical history remains open until an actual regulated BQG master operator and refinement-compatible physical amplitude are supplied.**

Date: 2026-09-06.

This note deliberately separates three statements that must not be conflated:

1. the exact finite spectral mathematics of a positive master constraint;
2. the theory-specific BQG master operator generated from the actual regulated constraints;
3. the physical/continuum history amplitude from which `W[J]`, `Gamma[g]`, and physical poles are derived.

The repository already enforces this distinction in `MASTER_CONSTRAINT_PHYSICAL_PROJECTOR.md`, `FESHBACH_INTERBLOCK_EFFECTIVE_KERNEL.md`, and `HAMILTONIAN_CONSTRAINT_TO_EFFECTIVE_ACTION.md`. This note adds the missing **derived spectral graph** between the finite master operator and its seed-sector heat/projector history.

---

## 1. Input object

Freeze one finite regulator and a Hermitian positive semidefinite master constraint

\[
\mathbb M \ge 0
\]

on its declared finite habitat, together with a seed/carrier block

\[
V=(v_1,\ldots,v_p).
\]

No phenomenological graph topology is introduced. The graph below is derived from repeated action of the already-defined operator.

Let `Q0` be an orthonormal basis of `range(V)`. The cyclic Krylov space is

\[
\mathcal K_r(\mathbb M,V)=\mathrm{span}\{V,\mathbb M V,\ldots,\mathbb M^rV\}.
\]

A rank-revealing block Lanczos/Krylov recursion produces orthonormal blocks `Q0,Q1,...` and projected blocks

\[
A_n=Q_n^\dagger\mathbb M Q_n
\]

with nearest-layer couplings `B_{n+1}`. In exact arithmetic,

\[
\mathbb M Q_n=Q_{n-1}B_n^\dagger+Q_nA_n+Q_{n+1}B_{n+1}.
\]

The resulting derived graph is the block-Jacobi operator

\[
J_r=Q^\dagger\mathbb M Q,\qquad Q=(Q_0,\ldots,Q_r).
\]

For a Hermitian polynomial Krylov basis, `J_r` is block tridiagonal. The implementation checks this rather than assuming it.

---

## 2. Exact finite closure theorem

Define the next residual after projection onto the accumulated cyclic space,

\[
R_{r+1}=\left(I-QQ^\dagger\right)\mathbb M Q_r.
\]

The exact closure condition is

\[
\boxed{R_{r+1}=0}
\]

or, equivalently after rank-revealing factorization,

\[
\boxed{B_{r+1}=0}.
\]

Then `range(Q)` is invariant under `M`:

\[
\mathbb M Q=QJ_r.
\]

Therefore for every polynomial `p`,

\[
p(\mathbb M)Q=Qp(J_r).
\]

In finite dimension this extends to every function defined on the finite spectrum of `M`, hence for the normalized seed block

\[
\boxed{Q_0^\dagger f(\mathbb M)Q_0=E_0^\dagger f(J_r)E_0}
\]

where `E0` injects the first block into the full Krylov coordinate space.

For the original, possibly non-orthonormal, seed `V=Q0 C`,

\[
\boxed{V^\dagger f(\mathbb M)V=C^\dagger E_0^\dagger f(J_r)E_0 C.}
\]

This is stronger than matching a finite list of moments.

---

## 3. Exact finite heat history and zero-sector projector

For every `sigma >= 0`,

\[
\boxed{V^\dagger e^{-\sigma\mathbb M}V=C^\dagger E_0^\dagger e^{-\sigma J_r}E_0C}
\]

after certified closure.

If zero is an isolated eigenvalue, the same closed graph gives

\[
\boxed{V^\dagger P_0V=C^\dagger E_0^\dagger\mathbf 1_{\{0\}}(J_r)E_0C,}
\]

where

\[
P_0=\mathbf 1_{\{0\}}(\mathbb M).
\]

Thus the derived graph can exactly reproduce the finite master-projector content visible from the chosen seed sector.

This is compatible with the existing theorem

\[
\|e^{-T\mathbb M}-P_0\|=e^{-T\Delta_M}
\]

when the first positive master gap `Delta_M` is isolated.

---

## 4. Matrix-valued spectral measure

Diagonalize the closed `J_r`,

\[
J_r u_a=\lambda_a u_a.
\]

The seed-sector spectral measure is

\[
d\Sigma_V(\lambda)=\sum_a W_a\,\delta(\lambda-\lambda_a)\,d\lambda,\qquad W_a=E_0^\dagger u_au_a^\dagger E_0.
\]

For a degenerate eigenvalue, the projectors in the degenerate eigenspace are summed before forming `W`.

Then

\[
Q_0^\dagger f(\mathbb M)Q_0=\int f(\lambda)\,d\Sigma_V(\lambda).
\]

In particular,

\[
\mu_n=\int\lambda^n\,d\Sigma_V(\lambda),
\]

\[
H_V(\sigma)=\int e^{-\sigma\lambda}\,d\Sigma_V(\lambda),
\]

and the seed-visible zero-sector is

\[
\Sigma_V(\{0\}).
\]

The implementation checks spectral-weight normalization

\[
\sum_a W_a=I_{\mathrm{rank}(V)}.
\]

---

## 5. Finite spectral zeta and constraint spectral dimension

At a finite regulator no analytic continuation is needed for the positive nonzero spectrum. Define only

\[
\zeta^{(+)}_V(s)=\sum_{\lambda_a>0}\mathrm{tr}(W_a)\lambda_a^{-s}.
\]

This is a finite diagnostic, not a formula for fundamental constants.

The heat-trace derivative gives a useful scale diagnostic

\[
\boxed{d^{(V)}_{s,\mathbb M}(\sigma)=2\sigma\frac{\sum_a\lambda_a e^{-\sigma\lambda_a}\mathrm{tr}(W_a)}{\sum_a e^{-\sigma\lambda_a}\mathrm{tr}(W_a)}.}
\]

The repository name for this quantity is deliberately **constraint spectral dimension**.

It is **not** declared to be spacetime dimension. A relation to physical spacetime dimension would require a separate continuum/refinement geometry theorem and agreement with the physical history kernel.

---

## 6. What is useful in the referenced spectral-small-world article

Reference: `https://habr.com/ru/articles/1046730/`

The reusable machinery is substantial:

- operator spectra rather than a handful of scalar observables;
- heat traces and spectral measures;
- gap scaling;
- spectral zeta as an operator diagnostic;
- refinement/RG comparison;
- spectral-dimension diagnostics;
- numerical negative controls and held-out comparisons.

Those ideas are valuable when the operator and graph are **derived from BQG** rather than selected to reproduce target constants.

---

## 7. What must not be imported from that article

### 7.1 Three-dimensionality and `K=6` are assumptions in the graph construction

The article starts from effective spatial dimension three, uses a claimed optimal degree range, introduces

\[
pK=N^{-1/3},
\]

and then fixes `K=6`.

For BQG this cannot serve as an independent derivation of dimension three. Dimension, locality, and coordination must remain outputs of the already registered geometry/refinement gates.

### 7.2 The three-dimensional lattice sum at `s=1` is not an ordinary convergent sum

The article writes

\[
\sum_{\mathbf n\in\mathbb Z^3\setminus\{0\}}\frac{1}{|\mathbf n|^2}=6\zeta(2).
\]

As an ordinary lattice sum this diverges. The Epstein-zeta defining series in `n` dimensions converges in its defining half-plane `Re(s)>n/2`; here `n=3`, `s=1`, so the point lies outside that half-plane.

An analytic continuation can be defined, but it is a **different declared operation** and must not be silently substituted for the divergent sum.

BQG therefore uses finite-regulator spectral zeta directly and postpones any continuum zeta regularization until a regulator-removal prescription has been derived.

### 7.3 `zeta(4) -> zeta(2)` is not accepted without a derivation

The article first obtains a nonlocal contribution proportional to

\[
p\ln K\,\zeta(4)
\]

and then replaces the leading contribution by one proportional to `\zeta(2)` before exponentiation.

BQG does not import that replacement. Every spectral factor must arise from the frozen operator and its measured spectral weights.

### 7.4 Numerical agreement is not an independence proof when inputs overlap

A comparison of two formulae is not a strong cross-check if both inherit shared choices such as `d=3`, `K=6`, the same graph family, or a target-scale construction. BQG keeps a zero-fit ledger and requires held-out observables after the microscopic output is frozen.

---

## 8. Executable gate

`scripts/bqg_spectral_history_graph_gate.py` accepts

```text
NPZ:
  M : finite Hermitian positive master-constraint matrix
  V : seed/carrier columns
```

and performs:

1. Hermiticity and positivity checks;
2. rank-revealing seed orthonormalization;
3. full-reorthogonalized block Krylov construction;
4. block-tridiagonality audit;
5. residual closure test;
6. invariant-action test `||MQ-QJ||`;
7. matrix-valued spectral-measure normalization;
8. moment checks `n=0..6`;
9. heat-kernel checks on several scales;
10. zero-projector equality on the seed sector;
11. finite positive spectral zeta;
12. constraint spectral dimension;
13. explicit physical-scope flags.

With no input file it runs a deterministic positive control whose master operator contains a six-dimensional seed-cyclic invariant sector embedded in a nine-dimensional Hilbert space.

The expected reference closure is

```text
block dimensions = [2, 2, 2]
total cyclic dimension = 6
closed = true
```

and the full/compressed moment, heat, and zero-projector identities must pass.

A negative CI control truncates the recursion at depth zero and requires the gate to fail, proving that the script cannot claim closure merely because a compressed matrix exists.

---

## 9. What this closes and what it does not

### Closed by this layer

- the exact finite cyclic-subspace closure criterion;
- the derived block spectral graph;
- exact seed-sector functional calculus after closure;
- finite heat history;
- finite zero-projector content;
- finite matrix-valued spectral measure;
- finite positive spectral zeta;
- constraint spectral dimension;
- numerical falsification gates for all of the above.

### Still open for actual BQG

The repository currently does not contain a production NPZ (or equivalent artifact) containing the **full declared theory-specific master matrix** `\mathbb M_G` together with the selected physicalization seed block.

Therefore the new self-test does **not** claim that the actual BQG production history has already closed.

Required next production chain:

```text
actual regulated graph-changing constraints C_A
  -> assemble positive M_G = C^dag G C
  -> freeze seed/carrier V
  -> run spectral-history graph
  -> if B_(r+1) != 0: continue Krylov depth
  -> if B_(r+1) == 0: finite seed-sector history closed
  -> repeat across regulator/refinement sequence
  -> compare normalized projector/source matrix elements
  -> only then attempt rigging-map / continuum history closure
  -> Z[J] -> W[J] -> Gamma[g] -> physical Gamma^(2)
```

The physical gate in `physicalization_gates.json`

```text
PHYSICAL_PROJECTOR_HISTORY = open_physical
```

must remain open until the theory-specific refinement/history requirements are met.

---

## 10. Falsification conditions

The spectral-history programme fails, or remains open, if any of the following occurs:

- the production `M_G` is not Hermitian positive within its declared numerical error budget;
- the chosen `V` is not reproducibly defined;
- Krylov residuals do not close at the available finite habitat size;
- the projected operator develops material non-block-tridiagonal couplings after reorthogonalization;
- `MQ=QJ` fails at claimed closure;
- moment or heat-kernel full/compressed identities fail;
- zero-projector content is unstable under allowed positive choices of `G`;
- normalized seed-sector projectors fail to converge under refinement;
- a constraint spectral scale is relabeled as physical time/frequency;
- constraint spectral dimension is relabeled as spacetime dimension without a separate theorem;
- parameters are selected after looking at external target constants.

---

## 11. Scientific status after this audit

The strongest defensible statement is now:

> BQG has a mathematically controlled route from a finite positive master constraint to an operator-derived spectral graph. If and when the production Krylov residual closes, that graph exactly contains the entire seed-visible finite master-constraint heat/projector history. This is a genuine strengthening over finite-moment fitting. It is not yet a proof of the continuum physical history of the candidate gravity theory.

That distinction is intentional and should remain machine-enforced.
