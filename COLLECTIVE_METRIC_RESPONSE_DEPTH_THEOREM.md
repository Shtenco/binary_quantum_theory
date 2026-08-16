# Collective metric-response depth theorem

## Statement

Let `|Omega_0>` be the canonical all-`j=1/2` 16-cell seed and let

\[
|e_v\rangle=E_v|\Omega_0\rangle
\]

be the exact production physical-sine Euclidean node columns.

The distributed amplitude calculation and sparse-union reconstruction show that **every Peter-Weyl basis state appearing in every `|e_v>` differs from the seed on exactly four dual-edge irreps**.  In particular the seed key is absent from the complete 552-state first-E union and

\[
\langle\Omega_0|e_v\rangle=0.
\]

Any metric observable built purely from flux generators on fixed graph edges, including local flux Gram operators and their polynomial/spectral functions, preserves every edge representation `j_e`.  Therefore

\[
\boxed{
\langle\Omega_0|Q(J)|e_v\rangle=0
}
\]

for every such representation-preserving metric observable.

Consequently, for a perturbed state

\[
|\Psi(t)\rangle=|\Omega_0\rangle+t|e_v\rangle+O(t^2),
\]

the normalized metric expectation has no linear term from the Euclidean first Krylov direction:

\[
\boxed{
\frac{d}{dt}\langle Q\rangle_{\Psi(t)}\bigg|_{t=0}=0.
}
\]

The first nontrivial metric response can occur through quadratic/return sectors such as `EE`, `ES`, `SE`, `SS` or through other operators that bring the representation labels back into overlap with the seed sector.

## Consequence for the collective GR producer

The 16-dimensional exact first-E amplitude tangent space is a genuine dynamical Krylov layer, but it must **not** be reinterpreted as a six-dimensional first-order classical metric tangent merely by fitting expectation values.

In particular the direct `6x6` kinetic Hessian used to infer `c_DeWitt_eff` must be constructed from a target-independent effective block space containing the necessary depth-2 return sectors.  Padding the first-E space with artificial metric coordinates would violate the preregistered producer contract.

## Scope

This is a representation-selection theorem on the declared 16-cell seed and flux-metric observables. It does not say that every collective observable has zero first-order response; operators that themselves change edge representations are outside the statement.
