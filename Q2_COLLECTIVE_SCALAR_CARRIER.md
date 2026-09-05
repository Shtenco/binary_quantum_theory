# q=2 collective scalar carrier

Status: **derived structural scalar-carrier precursor; physical scalar history remains open.**

`Q2_FIRST_SCALAR_EFFECTIVE_ACTION.md` proves that the currently registered local q=2 relational source produces an exact nonlinear `X/Z` shape 1PI action but does not contain the conformal/volume direction required for cosmological scalar gravity.

This note identifies the least arbitrary carrier already present in the BQG hierarchy that can supply that missing direction.

## 1. The missing cosmological scalar is radial flux scale, not another shape coordinate

For nondegenerate tetrahedral fluxes the spatial metric is reconstructed as

\[
q(E)=|\det C|C^{-1}C^{-T}.
\]

Under a common scale change

\[
E_f\to(1+\epsilon)E_f,
\]

one obtains

\[
q\to(1+\epsilon)q,
\]

so infinitesimally

\[
\boxed{\delta q=q.}
\]

For the DeWitt bilinear form

\[
Q_{DW}(\delta q)
=\operatorname{Tr}(q^{-1}\delta q q^{-1}\delta q)
-[\operatorname{Tr}(q^{-1}\delta q)]^2,
\]

this mode gives

\[
\boxed{Q_{DW}(q)=3-9=-6.}
\]

It is the unique local negative conformal direction.  The q=2 `X/Z` shape tangents are exactly orthogonal to it because

\[
\operatorname{Tr}(g_0^{-1}M_X)=
\operatorname{Tr}(g_0^{-1}M_Z)=0.
\]

Thus a gauge-complete scalar metric carrier must extend the fixed-spin shape qubit in the **radial flux/representation direction**, not merely add a third intrinsic-shape Pauli coordinate.

## 2. Why the microscopic j=1/2 carrier cannot do this

For four equal spin-1/2 faces the gauge-invariant intertwiner space is two-dimensional, but the absolute tetrahedral volume is proportional to the identity there.

The independent finite volume gate gives

```text
j=1/2:
intertwiner dimension = 2
absolute volume = one repeated nonzero value
volume_is_scalar_on_intertwiner = true
```

Consequently a volume source within the fixed `j=1/2` intertwiner does not create a new local scalar response channel.

This matches the exact q=2 metric result: fixed face-spin norm supports shape but freezes radial scale.

## 3. First collective threshold: j=1

For four equal spin-1 faces the intertwiner dimension is three and

\[
\operatorname{spec}Q=\{-\sqrt3,0,+\sqrt3\}.
\]

Hence, up to the already declared conventional volume scale,

\[
\boxed{
\operatorname{spec}V=\{0,3^{1/4},3^{1/4}\}.
}
\]

The volume is no longer scalar.

The repository's exact conditional representation-growth theorem supplies a direct q=2 route to this sector: two indistinguishable active graph-link strands, symmetrically blocked at each endpoint, give

\[
\operatorname{Sym}^2(\mathbb C^2)=V_{j=1},
\]

so

\[
\boxed{
n=2\quad\Longrightarrow\quad j=1.}
\]

This is why the first candidate conformal scalar carrier should be looked for at the first collective representation-growth scale rather than inside the original logical shape qubit.

The blocking statement is exact **conditional on symmetric endpoint blocking**.  The graph-changing dynamics has not yet proved that this is the physical coarse-graining channel or fixed its weight.

## 4. Exact local j=1 volume-source positive control

Let

\[
v=3^{1/4}
\]

and use the normalized trace over the three-dimensional `j=1` intertwiner with spectrum

\[
V=\{0,v,v\}.
\]

For dimensionless source

\[
q=\eta v,
\]

one has exactly

\[
\boxed{
Z_V(q)=\frac{1+2e^q}{3}.
}
\]

The dimensionless volume fraction is

\[
p=\frac{\langle V\rangle}{v}
=\frac{2e^q}{1+2e^q}.
\]

Its inverse is

\[
q=\log\frac{p}{2(1-p)}.
\]

The exact Legendre transform is

\[
\boxed{
\Gamma_V(p)
=p\log p
+(1-p)\log(1-p)
-p\log2
+\log3.
}
\]

At zero source,

\[
p_0=\frac23,
\qquad
\Gamma_V(p_0)=0,
\]

and

\[
\boxed{
\Gamma_V''(p_0)=\frac92.
}
\]

For the dimensional mean `m_V=vp`,

\[
\boxed{
\frac{d^2\Gamma_V}{dm_V^2}\bigg|_{p_0}
=\frac{9}{2\sqrt3}
=\frac{3\sqrt3}{2}.
}
\]

This is a real exact local scalar 1PI **positive control** in the first nontrivial volume carrier.

It is not yet `Gamma_FLRW`.  The normalized trace chooses a kinematic state-counting measure, not the theory-specific physical projector/history.  In particular `p_0=2/3` is not an observed scale factor, and `Gamma_V(p_0)=0` is not a prediction of zero cosmological constant.

## 5. Why this carrier is dynamically promising

The already registered collective `j=1` finite control also finds a nonzero curvature-volume commutator.  Therefore volume is not merely a passive label once representation growth occurs: curvature and volume access a larger cyclic sector than curvature alone.

This is precisely the qualitative ingredient that the fixed `j=1/2` qubit lacks.

However, a nonzero finite commutator is not yet a physical history measure.  The required next calculation is source-dressed graph-changing evolution/projector amplitudes in a carrier that retains this volume channel.

## 6. Lapse status

The repository also contains an exact dual-K5 lapse cochain identity

\[
\omega_{vw}=N_vM_w-N_wM_v.
\]

This closes the graph/cochain support of lapse smearings in the HDA construction.

But a lapse **smearing label** is not the same object as a lapse **response source** in

\[
W[J_g].
\]

For cosmological `Psi`, the future physical history must expose a source or relational response whose second derivatives generate the lapse/energy-constraint susceptibility after gauge reduction.

That bridge is still open.

## 7. Interblock scalar momentum structure

The four regular tetrahedral neighbor directions obey

\[
\sum_a n_a=0,
\qquad
\boxed{
\sum_a n_an_a^T=\frac43I.
}
\]

Therefore if the physical connected history derives a reciprocal scalar nearest-neighbor transfer coefficient, its leading small-`k` symbol is automatically isotropic:

\[
K_{scalar}(k)
=K_0+\kappa k^2+O(k^4).
\]

The geometry needed for an isotropic leading scalar Laplacian is already present.

What is **not** present is the microscopic physical coefficient `kappa`.  It cannot be imported from the constraint-resolvent spectral parameter or fitted to galaxy data.  It must come from a connected source-dressed physical history amplitude.

## 8. Minimal physical scalar carrier now implied by the repository

The next candidate field space is not merely `(X,Z)`.

At minimum it must resolve

\[
\boxed{
\mathcal C_{scalar}
=
\{
\text{radial flux/volume},
\text{lapse response},
\text{transported scalar shape/shear}
\}.
}
\]

For multiple neighboring blocks the physical history should produce a connected matrix kernel

\[
C_{AB}(b,c)
=\frac{\delta^2W_{phys}}
{\delta J_A(b)\delta J_B(c)},
\]

where `A,B` run over this scalar carrier.

After removing constraints/gauge directions and Legendre transforming,

\[
\Gamma_{scalar}^{(2)}(\omega,k)
=C_{phys}^{-1}(\omega,k)
\]

on the physical scalar quotient.

Only then is it legal to construct Bardeen potentials

\[
\Phi,\Psi
\]

and derive

\[
\mu_{BQG}(a,k),
\qquad
\Sigma_{BQG}(a,k).
\]

## 9. Consequence for dark matter, dark energy and lensing

The current calculation neither discovers nor rules out a BQG dark sector.

It does something more useful at this stage: it fixes where a valid answer must come from.

A dark-matter-like effect must arise from the connected scalar kernel and give the same derived `Phi/Psi` response for dynamics and lensing.

A dark-energy-like effect must arise from the homogeneous physical history/background sector and produce `rho_hist(a)` before `w_hist(a)` is inferred.

Neither may be manufactured from the q=2 shape Hessian, a TT coefficient, a Peter-Weyl constraint eigenvalue, or the kinematic `j=1` normalized trace.

## 10. Reproduction

```bash
python scripts/q2_collective_scalar_carrier_gate.py \
  --output verification_results/Q2_COLLECTIVE_SCALAR_CARRIER.json
```

A green result means the structural route to the missing scalar carrier is internally consistent.  `PHYSICAL_BACKGROUND_COSMOLOGY`, `PHYSICAL_SCALAR_COSMOLOGY`, `CONNECTED_INTERBLOCK_HISTORY` and `LENSING_DYNAMICS_CLOSURE` remain `open_physical`.
