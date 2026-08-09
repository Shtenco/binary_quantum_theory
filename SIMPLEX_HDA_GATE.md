# 4-simplex hypersurface-deformation gate

Status: **classical flat-simplex benchmark PASS; quantum K5 realization still OPEN**.

For the boundary of a four-simplex, fix vertex `0` and regard the opposite tetrahedron `sigma(0)` as the spatial hypersurface.  Let `V_tet=V(0)`.

Define:

- `H(k)`: translate vertex `k=1..4` along the outward unit normal to `sigma(0)`;
- `D(k,l)`: translate vertex `k` tangentially to `sigma(0)` and normally to the triangular face `sigma(0,l)` with the Bonzom--Dittrich normalization.

The flat simplex boundary algebra contains

\[
\boxed{
\{H(k),H(k')\}
=\frac{1}{3V_{tet}}
\left[D(k',k)-D(k,k')\right].
}
\]

This is the `d=4` specialization of the simplex boundary hypersurface-deformation algebra.

## Independent coordinate regression

`scripts/simplex_hda_geometric_gate.py` does not insert the right-hand side into the deformation rule.  It:

1. draws a random nondegenerate Euclidean 4-simplex in `R^4`;
2. constructs the spatial tetrahedron normal directly from the current vertices;
3. constructs the tangential face normals from barycentric gradients;
4. evaluates the commutator of the two normal-deformation vector fields by symmetric finite differences;
5. compares the resulting 5x4 vertex displacement field with the predicted combination of tangential deformations.

For one representative random simplex the relative defect is about

\[
4.8\times10^{-11}.
\]

For `20` random nondegenerate simplices and all six pairs `1<=k<k'<=4`, using a finite-difference step `3e-6`, the observed worst defect is about

\[
\boxed{1.42\times10^{-10}}.
\]

The result is therefore limited by numerical differentiation, not by the geometric identity.

## Why this matters for the current K5 model

The fully active `K5` quantum-link sector is precisely the boundary combinatorics of one four-simplex: five tetrahedral nodes and ten shared triangular faces.  Therefore the next quantum constraint test need not jump directly to a large lattice.

The correct hierarchy is now

\[
\boxed{
\text{K5 quantum constraints}
\to
\text{simplex HDA}
\to
\text{continuum HDA safe window}.
}
\]

A failure already at the first arrow rejects the proposed finite Hamiltonian regularization before any thermodynamic/continuum extrapolation.

## Quantum target

For semiclassical boundary states peaked on a nondegenerate flat four-simplex, construct local quantum Hamiltonians `H_k` and tangential generators `D_kl`, then test

\[
\boxed{
\Delta_{K5}^{HH}
=
\frac{
\|([\hat H_k,\hat H_{k'}]
-i\hbar[\hat D_{k'k}-\hat D_{kk'}]/(3\hat V_{tet}))|\Psi\rangle\|
}{
\|[\hat H_k,\hat H_{k'}]|\Psi\rangle\|
+\|[\hat D_{k'k}-\hat D_{kk'}]/(3\hat V_{tet})|\Psi\rangle\|
}
\to0.
}
\]

The inverse volume must be treated with the same finite regularization used in the Hamiltonian; post-hoc projection onto the classical formula is forbidden.

## Scope boundary

The finite simplex algebra is special.  Generic 4D Regge discretizations break vertex-translation/diffeomorphism symmetry away from flat or homogeneously-curved sectors.  Passing this gate is therefore necessary but not sufficient for continuum GR.  The subsequent low-momentum HDA scaling test in `HDA_SAFE_WINDOW_GATE.md` remains mandatory.
