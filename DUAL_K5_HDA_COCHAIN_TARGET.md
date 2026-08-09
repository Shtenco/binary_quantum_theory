# Generic dual-K5 HDA cochain target

Status: **exact combinatorial support structure; geometry-dependent sharp map remains OPEN**.

The previous reference-simplex HDA benchmark acts on the primal vertices of one
chosen spatial tetrahedron.  The canonical Peter--Weyl model instead places
Hamiltonians/lapses on the five **dual tetrahedral nodes** of K5.  Before any
metric coefficient is derived, the graph/cochain part of the generic dual-node
structure function can already be fixed exactly.

## 1. Lapses as zero-cochains

Let

$$
N=(N_0,\ldots,N_4),\qquad M=(M_0,\ldots,M_4)
$$

be lapse 0-cochains on the five dual nodes.  Orient each K5 link from `v` to
`w`, `v<w`.  The discrete exterior derivative is

$$
(dN)_{vw}=N_w-N_v.
$$

Using the symmetric midpoint product on an edge,

$$
\bar N_{vw}=\frac{N_v+N_w}{2},
$$

define the discrete analogue of `N dM - M dN`:

$$
\omega_{vw}
=\bar N_{vw}(dM)_{vw}-\bar M_{vw}(dN)_{vw}.
$$

A direct expansion gives the exact identity

$$
\boxed{
\omega_{vw}=N_vM_w-N_wM_v.
}
$$

No metric, volume, coordinate embedding or continuum approximation enters this
step.

## 2. Basis lapses select exactly one dual edge

For

$$
N=\delta_i,\qquad M=\delta_j,\qquad i<j,
$$

we get

$$
\boxed{
\omega_{vw}=\delta_{(vw),(ij)}.
}
$$

Thus before raising the one-form index with the spatial metric, the bracket of
two node-local Hamiltonians has the combinatorial support of **one shared dual
link**.

This gives the natural generic interpretation of the ten antisymmetric pairs

$$
[H_i,H_j],\qquad i<j:
$$

five node lapses produce ten candidate dual-edge tangential generators, exactly
matching the ten links of K5.

The old fact that the projected finite model produced ten linearly independent
`Q_ij` is therefore structurally natural; their exact SO(5)-like projection at
the regular symmetric point is **not** by itself the generic HDA, because the
metric-dependent structure functions have not yet been inserted.

## 3. Geometry-dependent sharp map

The continuum shift is

$$
\beta^a=q^{ab}(N\partial_bM-M\partial_bN).
$$

The discrete cochain `omega` above is the covector part.  The remaining generic
K5 problem is the discrete musical map

$$
\boxed{
\beta=\sharp_{E,q}\,\omega,
}
$$

which converts the edge one-cochain into a tangential deformation using the
collective tetrahedral geometry.

For link `(vw)` the required geometry is local to the shared triangular face.
The canonical data already contain its flux:

$$
E_{vw},
\qquad
E_{wv}=-\operatorname{Ad}(g_{vw}^{-1})E_{vw}.
$$

The exact tetrahedral identity

$$
E_f=3V\nabla\lambda_f
$$

from `FLUX_HABITAT_DIFFEO_BRIDGE.md` shows that the required face-normal /
metric-raising information is encoded in these fluxes once a consistent local
geometry and frame transport are reconstructed.

What is **not yet proved** is the generic coefficient/averaging rule which
combines the two neighboring tetrahedral metrics/volumes into the dual-link
`sharp` appropriate to the node-local Hamiltonian regularization.

## 4. Correct generic quantum target

For basis lapses at nodes `i,j`, the future off-shell test should have the form

$$
\boxed{
-i[H_i,H_j]'
\longrightarrow
\hbar\,D_{ij}'[\sharp_{E,q}\,e^{ij}]
}
$$

on the relational/habitat dual space, where `e^{ij}` is the one-cochain
supported on the single oriented link `(ij)`.

A densitized form is preferred to avoid inverse-volume zero-mode problems.
The exact volume/flux weighting must be derived from the same dual-cell
regularization rather than copied from the one-reference-simplex formula.

## 5. Immediate falsifiers

A generic dual-K5 candidate fails before any continuum extrapolation if:

1. the lapse pair `(i,j)` produces a tangential principal support which cannot
   be associated with shared dual link `(ij)` modulo declared graph-changing
   equivalences;
2. the result depends on arbitrary vertex labels after geometric orientation
   has been fixed;
3. no local flux/metric sharp map can reproduce the relative responses for
   different nonconstant habitat functionals with one common normalization;
4. the first-class rank flows to the six independent BF flatness directions
   rather than the `3D+1H` GR structure.

## 6. Regression script

`scripts/dual_k5_lapse_cochain_gate.py` verifies for random lapses that the
midpoint-cochain expression equals `N_v M_w-N_w M_v` to machine precision and
that every one of the ten basis-lapse pairs has exactly one-edge support.

This is a small but important correction to the roadmap: the **generic dual
support** of the HDA can be fixed exactly now, while the regular-tetrahedron
`1/(3V)` formula remains a separate symmetric/reference-simplex benchmark.
