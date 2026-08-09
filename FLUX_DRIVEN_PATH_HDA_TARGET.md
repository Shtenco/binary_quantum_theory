# Flux-driven path representation of the canonical HDA target

Status: **kinematic target assembled from independently tested components; the Hamiltonian commutator equality itself remains OPEN.**

This file combines three previously separate constructions into one explicit
right-hand side for the canonical graph-changing HDA.

## 1. Lapse pair -> dual one-cochain

Put the lapse values on dual tetrahedral nodes.  For an oriented dual edge
`e=(v,w)`,

$$
\boxed{
\omega_{vw}(N,M)=N_vM_w-N_wM_v.
}
$$

This is exactly the midpoint discretization of

$$
N\,dM-M\,dN.
$$

For basis lapses `delta_i,delta_j`, only the shared dual edge `(ij)` is
supported.  See `DUAL_K5_HDA_COCHAIN_TARGET.md`.

## 2. Dual one-cochain -> spatial shift

For a circumcentric tetrahedral dual, reconstruct the metric `sharp` from the
canonical face fluxes.  At cell `v` define

$$
G_v
=
\sum_{w\sim v}
\frac{d_{vw}}{A_{vw}}
E_{vw}E_{vw}^{T}.
$$

Then

$$
\boxed{
\beta_v
=
\sharp_{E,q}(\omega)_v
=
G_v^{-1}
\sum_{w\sim v}\omega_{vw}E_{vw}.
}
$$

For a nondegenerate tetrahedron `G_v` is positive definite.  The same map is
obtained from the dual-edge Hodge star followed by exact RT0 face-flux
reconstruction.  See `DUAL_CELL_SHARP_RT0.md`.

For arbitrary dual choices a non-diagonal Hodge / weighted directional
reconstruction can replace the circumcentric formula; universality is judged by
the long-wavelength reconstructed shift, not by equality of raw Hodge matrices.

## 3. Spatial shift -> edge rerouting

An embedded spin-network edge has a local unit tangent `t_e`.  The component of
a spatial shift tangent to the path only changes its parametrization.  The
geometrically visible rerouting component is

$$
\boxed{
\beta_{\perp,e}
=(I-t_et_e^T)\beta.
}
$$

Choose any local orthonormal transverse frame `(u_e,v_e)` and write

$$
\beta_{\perp,e}=\beta_e^1u_e+\beta_e^2v_e.
$$

A refined microscopic path register carries route-position shifts `S_1,S_2`
and centered derivatives

$$
\nabla_{\alpha,e}^{path}
=\frac{S_{\alpha,e}-S_{\alpha,e}^{\dagger}}{2a}.
$$

The finite diffeomorphism generator is

$$
\boxed{
\hat D_{path}[\beta]
=-i\hbar
\sum_e
\left(
\beta_e^1\nabla_{1,e}^{path}
+
\beta_e^2\nabla_{2,e}^{path}
\right)
+\hat G[\beta\cdot A],
}
$$

where the final Gauss/end-point term restores the gauge-covariant
Ashtekar--Barbero diffeomorphism constraint convention.

The scalar product `beta_perp . nabla_perp` is independent of the arbitrary
SO(2) choice of transverse frame.

## 4. The complete finite canonical target

The graph-changing HDA can now be stated without inventing a post-hoc
`D` operator:

$$
\boxed{
[\hat H[N],\hat H[M]]
\stackrel{IR}{=}
 i\hbar\,
\hat D_{path}
\left[
\sharp_{E,q}(N\,dM-M\,dN)
\right]
}
$$

on the declared off-shell/habitat domain, up to the standard density and
normalization conventions fixed before the run.

In expanded discrete form the right-hand side follows the chain

$$
\boxed{
(N,M)
\to
\omega_{vw}=N_vM_w-N_wM_v
\to
\beta_v=G_v^{-1}\sum_w\omega_{vw}E_{vw}
\to
\beta_{\perp,e}
\to
-i\hbar\beta_{\perp,e}\cdot\nabla_e^{path}.
}
$$

Every object in this chain is determined by the current state and the lapse
pair.  No Pauli-basis fit or separately chosen tangential coefficient remains.

## 5. Existing independent gates for the RHS

### Lapse/cochain support

`scripts/dual_k5_lapse_cochain_gate.py` verifies the exact antisymmetric edge
cochain and one-edge support for basis lapses.

### Geometry-dependent sharp

`scripts/dual_cell_sharp_rt0_gate.py` verifies the Hodge/RT0 and cell-centred
reconstruction on random tetrahedral geometries at approximately machine
precision.

### Gauge-covariant rerouting

`scripts/path_rerouting_diffeo_gate.py` verifies that two microscopic routes
with the same endpoints transform identically under local SU(2) frames, while
their relative holonomy is loop curvature.

### Continuum path derivative

`scripts/path_diffeo_lie_gate.py` gives an approximately `L^-1.95` defect for
the one-coordinate Lie bracket.

`scripts/path_vector_diffeo_gate.py` gives

$$
\boxed{\Delta_{vec}\sim L^{-1.982}}
$$

for the full two-transverse-direction vector-field Lie bracket.

Thus the **right-hand-side kinematics** already has an independent continuum
route with approximately quadratic lattice corrections.

## 6. Exact embedded route versus intrinsic effective route

This path representation is required only if one wants an exact finite
realization of the standard embedded-LQG diffeomorphism action.  There remains
a second, cheaper semiclassical route:

- reconstruct the Regge/tetrahedral geometry from `(j,iota)`;
- implement a discrete vertex displacement directly as a canonical
  transformation of the intrinsic geometric data.

The two routes should agree after coarse graining, but finite-cutoff results
from one route must not be silently used as results for the other.

## 7. New computational priority

The expensive 11-million-state Lorentzian support calculation should not be the
next blind run.  First implement the finite path/rerouting register and the
flux-driven `D_path` above on a small refined edge/plaquette complex.  Then the
Hamiltonian commutator has a **nontrivial, explicitly represented** right-hand
side to compare against.

Only once this finite off-shell comparison is operational should the full
Lorentzian `H_E+H_L` amplitude engine be scaled to the complete K5 reachable
support.
