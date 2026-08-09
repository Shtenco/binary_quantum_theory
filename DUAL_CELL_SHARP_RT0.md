# Generic dual-cell `sharp` from flux geometry

Status: **exact kinematic construction for a circumcentric dual / lowest-order H(div) reconstruction. Quantum HDA closure and dual-choice universality remain OPEN.**

## 1. From a dual-edge one-cochain to a primal face flux

In a three-dimensional tetrahedral complex a primal triangular face `f` is dual
to an edge `*f` joining the circumcenters of the two neighboring tetrahedra.
For a circumcentric dual the dual edge is orthogonal to the shared face.

Let

- `A_f` be the primal face area;
- `d_f=|*f|` the signed/positive dual-edge length in the declared convention;
- `omega_f` a dual 1-cochain approximating the line integral of a covector
  `beta^flat` along `*f`.

The diagonal circumcentric discrete Hodge star gives the corresponding primal
face flux

$$
\boxed{
\Phi_f=\frac{A_f}{d_f}\,\omega_f.
}
$$

This is the discrete form of

$$
\int_f *\beta^\flat
\simeq
\frac{|f|}{|*f|}\int_{*f}\beta^\flat.
$$

Discrete Exterior Calculus supplies the primal/dual and Hodge-star framework;
on a well-centered/circumcentric simplicial mesh the Hodge matrix is diagonal
with the primal/dual volume ratio.

## 2. Exact RT0 reconstruction inside one tetrahedron

Let tetrahedron `T` have vertices `x_0,...,x_3`, volume `V_T`, and let face
`f_i` be opposite vertex `x_i`.  Given **arbitrary** integrated outward face
fluxes `Phi_i`, define

$$
\boxed{
\beta_T(x)
=
\frac1{3V_T}
\sum_{i=0}^{3}
\Phi_i\,(x-x_i).
}
$$

This is the lowest Raviart--Thomas (`RT0`) vector field.  It has the exact face
moments

$$
\boxed{
\int_{f_i}\beta_T\cdot n_i\,dA=\Phi_i.
}
$$

Indeed, for `j != i`, the vector `x-x_j` is tangent to face `f_i`, while

$$
(x-x_i)\cdot n_i=h_i=\frac{3V_T}{A_i}
$$

on `f_i`.

Combining the Hodge and RT0 steps gives the generic low-order `sharp`

$$
\boxed{
\sharp_T(\omega)(x)
=
\frac1{3V_T}
\sum_{i=0}^{3}
\frac{A_i}{d_i}\,
\omega_i\,(x-x_i).
}
$$

## 3. Exact reconstruction of a constant vector field

For a constant vector `beta`, the circumcentric dual edge is normal to the
face, so

$$
\omega_i=d_i\,n_i\cdot\beta.
$$

Hence

$$
\Phi_i=A_i n_i\cdot\beta=E_i\cdot\beta,
$$

where

$$
E_i=A_i n_i
$$

is the canonical face-flux vector.  The RT0 reconstruction then returns

$$
\boxed{\sharp_T(\omega)=\beta}
$$

exactly.

`scripts/dual_cell_sharp_rt0_gate.py` verifies this on 1000 random
nondegenerate tetrahedra.  In the regression run used during derivation:

- worst constant-vector reconstruction error: about `2.6e-14`;
- worst arbitrary face-flux reproduction error: about `1.1e-14`;
- constant-vector face-flux closure error: about `3.6e-15`;
- for 1000 random adjacent tetrahedron pairs the circumcenter-to-circumcenter
  vector has relative tangent component below about `3.9e-14`.

## 4. Cell-centred dual-node formula

For the node-local K5 HDA it is useful to reconstruct the vector directly at a
dual cell rather than at every point of the tetrahedron.

Let

$$
n_{vw}=\frac{E_{vw}}{A_{vw}}
$$

be the outward unit normal of the shared face and let `d_vw` be the length of
the circumcentric dual edge to the neighbor `w`.

The edge samples are

$$
g_{vw}=\frac{\omega_{vw}}{d_{vw}}
\simeq n_{vw}\cdot\beta_v.
$$

Use the natural Hodge-weighted least-squares metric

$$
G_v
=
\sum_{w\sim v}
A_{vw}d_{vw}\,n_{vw}n_{vw}^{T}.
$$

Equivalently, in canonical flux variables,

$$
\boxed{
G_v
=
\sum_{w\sim v}
\frac{d_{vw}}{A_{vw}}
E_{vw}E_{vw}^{T}.
}
$$

The cell-centred `sharp` is therefore

$$
\boxed{
\beta_v
=
G_v^{-1}
\sum_{w\sim v}
\omega_{vw}E_{vw}.
}
$$

This formula uses only

- face fluxes `E_vw`;
- their areas `A_vw=|E_vw|`;
- dual lengths `d_vw`, reconstructible from the tetrahedral metric/edge
  geometry;
- the lapse one-cochain `omega`.

No reference 4-simplex and no externally fitted tensor coefficient is needed.

## 5. Nondegeneracy / uniqueness theorem

For positive dual lengths and a nondegenerate tetrahedron,

$$
x^{T}G_vx
=
\sum_w A_{vw}d_{vw}(n_{vw}\cdot x)^2.
$$

The four face normals of a nondegenerate tetrahedron span `R^3`.  Therefore

$$
\boxed{G_v>0}
$$

and the cell-centred `sharp` is unique.

Degeneracy of `G_v` is therefore itself a geometry gate: it signals a collapsed
cell / failure of the local three-dimensional metric phase.

## 6. Basis lapses on the generic dual K5 graph

From `DUAL_K5_HDA_COCHAIN_TARGET.md`, for

$$
N=\delta_i,\qquad M=\delta_j,
$$

the covector cochain has support only on dual link `(ij)`:

$$
\omega_{ij}=1.
$$

Consequently the generic **dual-node** shift at the two incident cells is

$$
\boxed{
\beta_i=G_i^{-1}E_{ij},
}
$$

and, using the opposite orientation at `j`,

$$
\boxed{
\beta_j=G_j^{-1}(-E_{ji}),
}
$$

with the two vectors compared after the usual parallel transport to a common
frame.  This is the geometry-dependent completion of the exact one-edge
cochain support derived earlier.

## 7. Global RT0 consistency

On a shared face the edge cochain changes sign when orientation reverses and so
does the outward face flux.  Therefore the integrated normal flux is equal and
opposite in the two neighboring tetrahedral conventions.  The reconstructed
field is consequently `H(div)`-conforming: its normal flux is single-valued
across the face.

This is the correct finite-volume/DEC type of continuity for a shift reconstructed
from face-normal data.  Pointwise tangential continuity is not imposed by RT0
and belongs to higher-order/refined reconstruction.

## 8. What remains OPEN

The **kinematic** circumcentric `sharp` is now explicit.  The remaining issues
are physical/universality questions:

1. circumcentric versus barycentric/Galerkin Hodge choice on non-well-centered
   quantum tetrahedra;
2. coarse shape matching so the two neighboring metrics define one shared face;
3. quantization/operator ordering of `G_v^{-1}` or, preferably, a densitized
   identity avoiding an explicit inverse;
4. the graph-changing/path representation needed for an exact embedded-LQG
   diffeomorphism action;
5. off-shell HH closure and regulator scaling.

For arbitrary meshes a barycentric/Galerkin Hodge can replace the diagonal
circumcentric star; the corresponding map is generally non-diagonal.  Hence the
correct universality test is **not** equality of raw Hodge matrices but equality
of reconstructed long-wavelength diffeomorphism responses under different dual
choices.
