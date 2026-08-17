# Physical preferred-order consistency: regulator frame is not an observable

Status: **symmetry consistency theorem / falsification rule.**

A nonzero anisotropic or preferred-frame TT pole coefficient is physical only if the same preferred structure exists as a state/history/effective-action order parameter. A coordinate choice, triangulation orientation or regulator frame is not sufficient.

A nonzero preferred pole does **not** necessarily imply a deformed hypersurface-deformation algebra. A generally covariant theory can possess an undeformed constraint algebra while a physical state spontaneously breaks Lorentz/rotation symmetry through the expectation value of a dynamical tensor field. What is mandatory is a common physical order parameter.

## 1. Three symmetry outcomes

### A. Metric-only Lorentz/GR universality

No extra physical order parameter survives. Under the assumptions of `TT_POLE_UNIVERSALITY_NO_GO.md`,

\[
(c_1,\ldots,c_6)_{pole}=0
\]

at order `k^4` for the original massless branch.

### B. Spatially isotropic preferred foliation

A physical timelike vector/clock normal survives, `u^mu != 0`, while no spatial orientational tensor does. Spatial `SO(3)` is preserved in the rest frame of `u`, so the six-dimensional tetrahedral pole space collapses to one isotropic spatial coefficient.

### C. Tetrahedral spatial order

A nonzero spatial orientational tensor survives coarse graining. Then generic tetrahedral direction dependence and polarization response may be physical. Its orientation must be carried by the physical state/history and transform covariantly under frame changes.

## 2. Exact tetrahedral rank-four tensor

Use the four unit regular-tetrahedron directions

\[
n_1=(1,1,1)/\sqrt3,\quad n_2=(1,-1,-1)/\sqrt3,
\]
\[
n_3=(-1,1,-1)/\sqrt3,\quad n_4=(-1,-1,1)/\sqrt3.
\]

Their second moment is

\[
\boxed{\sum_a n_a^i n_a^j=\frac43\delta^{ij}.}
\]

Define

\[
S_{ijkl}=\sum_a n_{ai}n_{aj}n_{ak}n_{al}
\]

and

\[
U_{ijkl}=\frac13(\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}).
\]

Since `U_iikl=(5/3)delta_kl` and `S_iikl=(4/3)delta_kl`, the fully trace-free tetrahedral tensor is

\[
\boxed{T^{(4)}_{ijkl}=S_{ijkl}-\frac45U_{ijkl},}
\]

with

\[
\boxed{T^{(4)}_{iikl}=0.}
\]

Its scalar quartic contraction is

\[
\boxed{
T^{(4)}_{ijkl}k_i k_j k_k k_l
=-\frac89\left(k_x^4+k_y^4+k_z^4-\frac35(k^2)^2\right).
}
\]

Thus the repository's cubic harmonic is the scalar contraction of a physical `l=4` orientational order tensor.

## 3. Refinement observable

At refinement level `g`, reconstruct the normalized trace-free order tensor from the physical/coarse geometry state,

\[
\Theta_g^{(4)}
=\frac{\langle\Psi_g|P_g\widehat T_g^{(4)}P_g|\Psi_g\rangle}
{\langle\Psi_g|P_g|\Psi_g\rangle}.
\]

Transport refinement levels to the same coarse tangent frame and define

\[
\rho_4(g)=\sqrt{\Theta^{(4)}_{g,ijkl}\Theta_g^{(4),ijkl}}.
\]

Preregister the alternatives

```text
rho4(g) -> 0       : tetrahedral orientation is regulator/UV memory;
rho4(g) -> rho*>0  : a physical tetrahedral condensate survives.
```

A nonzero generic six-Wilson vector accompanied by `rho4 -> 0` is inconsistent and must not be called physical tetrahedral dispersion.

## 4. Frame covariance test

For a physical rotation `R` acting simultaneously on state/boundary data, momentum and order tensor,

\[
K_{TT}[R\Theta^{(4)},R\mathbf k]
=U_{TT}(R)K_{TT}[\Theta^{(4)},\mathbf k]U_{TT}(R)^{-1}.
\]

By contrast, rotating only the triangulation/regulator while holding physical boundary data fixed must not rotate a continuum observable.

```text
rotate physical order + apparatus -> covariance required;
rotate only regulator             -> continuum observable invariant.
```

## 5. Constraint algebra versus spontaneous order

Two mechanisms must not be conflated.

**Deformed-algebra mechanism:** if the effective constraint algebra acquires order-`a_*^2` structure tensors, the same tensors must appear consistently in the physical history/pole sector.

**Spontaneous-state mechanism:** the total action and HDA may remain generally covariant/undeformed while a dynamical field or collective state has a nonzero tensor expectation value. The physical pole can then depend on that state order parameter.

Therefore

\[
\boxed{
\text{preferred TT pole structure}
\Longrightarrow
\text{derived preferred structure in either effective constraints or physical state/history}.
}
\]

The converse is not automatic.

## 6. Connection to the six-Wilson extraction

The six-Wilson extractor remains the unbiased first step. After extracting the full vector, test jointly:

1. distance to the `SO(3)` one-dimensional subspace;
2. independent `rho4(g)` refinement flow;
3. any preferred timelike/foliation order parameter;
4. regulator-only rotation dependence;
5. order-`a_*^2` HDA/history covariance diagnostics.

Only a mutually consistent branch receives a physical interpretation.

## 7. Strong falsification rule

A finite microscopic tetrahedral split is not sufficient evidence for Lorentz violation or anisotropic quantum-gravity propagation.

The candidate theory fails its own physicalization test if it reports a nonzero anisotropic massless-pole signal while the physical orientational order flows to zero, rotating only the regulator rotates the signal, no derived state/field carries the orientation, or the continuum covariance diagnostics contradict the claimed pole.

This prevents the theory from mistaking its discretization for Nature.
