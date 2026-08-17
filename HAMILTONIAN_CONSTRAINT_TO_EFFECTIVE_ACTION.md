# Hamiltonian constraint -> physical history -> metric effective action

Status: **canonical conceptual bridge and non-claim boundary.**  The repository has strong finite Peter–Weyl Hamiltonian-constraint data and HDA closure, but a Hamiltonian constraint is not automatically an ordinary time-evolution Hamiltonian.  A physical `omega`-dependent graviton kernel requires a history/physical-projector construction or a genuine relational deparametrization.

This document prevents the spectral parameter of a local constraint resolvent from being silently renamed physical frequency.

---

## 1. What the Peter–Weyl calculations actually provide

The finite microscopic calculations construct matrix elements of regulated gravitational constraint operators such as

\[
\hat H_E[N],
\qquad
\hat H_L[N],
\qquad
\hat H[N]=\hat H_E[N]+\hat H_L[N],
\]

on controlled Peter–Weyl spin-network habitats.

Their powers, Krylov blocks and resolvents are mathematically meaningful:

\[
K=V^\dagger V,
\quad
A=V^\dagger\hat HV,
\quad
B=V^\dagger\hat H^2V,
\]

\[
G_c(z)=V_c^\dagger(z-\hat H)^{-1}V_c.
\]

They probe support, recoupling, leakage/return, anisotropy and finite-shell spectral structure.

But `z` is a constraint-spectrum variable unless an additional physical-time construction is supplied.

Therefore

\[
\boxed{z\not\equiv\omega\quad\text{by notation alone}.}
\]

---

## 2. Why HDA is necessary here

In canonical gravity the Hamiltonian constraint generates normal deformations of spatial slices, not evolution with respect to a pre-existing external clock.

The project tests the hypersurface-deformation structure

\[
[\hat H[N],\hat H[M]]
\to i\hbar\hat D[\sharp(NdM-MdN)].
\]

This matters physically because a covariant history construction must not assign different amplitudes to descriptions related only by refoliation.

Thus the HDA result is the consistency prerequisite for turning local constraints into a continuum history theory.

It is not itself the physical projector or quantum measure.

---

## 3. Route A: relational deparametrization

If the final matter sector supplies a monotonic physical clock field `T`, one may solve the total constraint schematically as

\[
P_T+H_{phys}(g,\pi;T)=0
\]

and obtain genuine relational evolution

\[
i\hbar\frac{\partial}{\partial T}\Psi
=\hat H_{phys}\Psi.
\]

Then a standard retarded resolvent/frequency variable of `H_phys` has a direct physical interpretation.

This route is presently **not closed**, because the realistic matter/clock sector has not yet been derived.

No arbitrary coordinate label is promoted to a physical clock merely to close the calculation.

---

## 4. Route B: covariant physical projector / rigging map

Without choosing a matter clock, the canonical route is a physical projector/group-averaging construction.

Formally, after Gauss/diffeomorphism treatment and gauge fixing/measure are specified,

\[
\boxed{
\mathcal P_{phys}
\sim
\int \mathcal DN\,\mu[N]\,
\mathcal T\exp\left[
\frac{i}{\hbar}\int dt\,\hat H[N(t)]
\right].
}
\]

Equivalently, a Trotterized microscopic history amplitude can be built from short normal-deformation transfer factors and then quotient/gauge-average the redundant slicing data.

The exact measure `mu`, physical inner product and regulator-removal prescription are part of the theory.  They are not harmless normalization details.

A spinfoam/history realization may provide the same physical object in covariant language, but equivalence to the frozen canonical operator ordering must be demonstrated rather than assumed.

---

## 5. Add metric sources before taking the effective action

Let `O_g` denote the derived coarse metric observables obtained through the exact logical-shape -> metric map and its interblock extension.

Introduce a source `J` in the physical history amplitude:

\[
Z[J]
=\langle\Psi_{out}|\,
\mathcal P_{phys}[J\cdot O_g]\,
|\Psi_{in}\rangle.
\]

Define connected functional

\[
W[J]=-i\hbar\log Z[J]
\]

and mean coarse metric

\[
g=\frac{\delta W}{\delta J}.
\]

The Legendre transform defines the 1PI effective action

\[
\boxed{
\Gamma[g]=W[J]-J\cdot g.
}
\]

(up to the chosen sign convention).

The physical inverse connected metric propagator is the Hessian

\[
\boxed{
K_{metric}
=\frac{\delta^2\Gamma}
{\delta g\,\delta g}.
}
\]

After gauge reduction and TT projection,

\[
\boxed{
K_{TT}(\omega,\mathbf k)
=\Pi_{TT}K_{metric}(\omega,\mathbf k)\Pi_{TT}.
}
\]

This is the object whose poles define physical gravitational-wave propagation.

---

## 6. Where the current Peter–Weyl K/A/B data enter

Finite constraint moments are not discarded.  They are microscopic local data controlling the short-history transfer and its coarse-grained cumulants.

The correct interpretation is

```text
constraint matrix elements / Krylov moments
 -> short-step transfer / history amplitudes
 -> connected cumulants
 -> physical projector / effective action
 -> K_metric
 -> K_TT.
```

They can be used to construct and benchmark transfer kernels, identify active irreps and compress the calculation before the expensive history sum.

The local 8.43% `E/T2` split and the full-H_E depth-two response are therefore **UV dynamical seeds** for the metric effective action, not already its infrared Wilson coefficients.

---

## 7. Vacuum bubbles and connectedness

A global sum of local constraint terms acting on a kinematical reference state contains contributions far from a local metric insertion.

Those disconnected vacuum processes must not become an extensive “self-energy” of the local graviton merely because `H^2` was evaluated globally.

The `W=-i log Z` connected construction removes disconnected vacuum bubbles automatically once the physical history measure/state is defined.

This is another reason not to identify a raw global `V^dag H^2 V` with the 1PI TT Hessian.

---

## 8. Positive-control requirement

Before any microscopic quartic coefficient is called physical, the history/effective-action implementation must reproduce the already-frozen continuum controls in the common scaling window:

1. massless leading TT pole;
2. positive common residue;
3. `z -> 1` leading cone;
4. Fierz–Pauli/DeWitt tensor structure;
5. absence of physical anisotropy at derivative order `<=2`;
6. correct reduced-kernel limit where the exact positive-control calculation applies.

Only the residual four-derivative pole response is then matched to the six-Wilson basis.

---

## 9. What is formally closed and what remains dynamical

The **definition** of the physical bridge is now unambiguous:

\[
\boxed{
\hat H[N]
\to\mathcal P_{phys}[J]
\to Z[J]
\to W[J]
\to\Gamma[g]
\to K_{TT}(\omega,k)
\to(c_1,\ldots,c_6)_{pole}.
}
\]

But a definition is not a completed microscopic calculation.

Still required for a first-principles physical prediction:

```text
physical-projector / history measure
state / boundary-condition prescription
canonical-ordering <-> history-amplitude consistency
connected interblock metric cumulants
regulator/refinement limit
```

or, alternatively, a derived relational clock and physical Hamiltonian.

Until one of these routes is numerically implemented and passes the positive controls, the six physical Wilson coefficients remain open.

---

## 10. Consequence for the word “closure”

The project can correctly say:

> the structural gravity architecture and the observable dictionary are closed in their declared scope, and the remaining physicalization problem has been reduced to a finite history/measure/interblock computation.

It cannot yet correctly say:

> the full microscopic theory has produced the physical interacting graviton propagator.

That distinction is part of the theory, not a disclaimer added from outside.
