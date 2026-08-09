# Minimal path/rerouting register for exact embedded diffeomorphisms

Status: **kinematic architecture gate; separates exact embedded-LQG HDA from intrinsic Regge-effective HDA.**

## 1. Fixed abstract graph limitation

A K5 spin-network basis which retains only

$$
|\{j_e\},\{\iota_v\}\rangle
$$

has forgotten how each abstract edge is embedded/routed through the spatial
manifold.  The finite automorphism group is

$$
\operatorname{Aut}(K_5)=S_5,
\qquad |S_5|=120.
$$

Any continuous homomorphism from a connected one-parameter spatial
diffeomorphism subgroup into this finite/discrete relabeling group has constant
image.  Thus **combinatorial relabeling alone** cannot realize a nontrivial
infinitesimal diffeomorphism generator.

This statement is deliberately scoped: an intrinsic Regge-effective theory can
still represent a vertex displacement as a transformation of reconstructed
geometric data on a fixed combinatorial complex.  What is impossible is to
reproduce the standard embedded-LQG action of connected diffeomorphisms using
only finite abstract graph permutations.

## 2. Why this matters for QSD/HDA

In the finite-triangulation construction of Laddha--Varadarajan the
diffeomorphism constraint is engineered so that

$$
\boxed{
1+i\delta\hat D_T(\vec N)
\simeq
\hat U_{\phi(\vec N,\delta)}
}
$$

and the spin-network edge is actually translated/rerouted along the integral
curves of the shift vector.  The curvature approximant and the Gauss term work
together to replace the original path by its displaced path.

Therefore an exact embedded-LQG realization of the HDA needs a state variable
which distinguishes different routes with the same abstract endpoints.

Primary reference:

- A. Laddha and M. Varadarajan, *The Diffeomorphism Constraint Operator in Loop
  Quantum Gravity*, arXiv:1105.0636.

## 3. Minimal two-route carrier

Take one elementary plaquette/diamond with two paths sharing endpoints,

$$
p_A:0\to1\to2,
\qquad
p_B:0\to3\to2.
$$

Their holonomies are

$$
h_A=U_{01}U_{12},
\qquad
h_B=U_{03}U_{32}.
$$

Under arbitrary local frames,

$$
U_{ab}\to g_aU_{ab}g_b^\dagger,
$$

both routes transform with the same endpoint representation,

$$
\boxed{
h_A\to g_0h_Ag_2^\dagger,
\qquad
h_B\to g_0h_Bg_2^\dagger.
}
$$

The relative route curvature

$$
\boxed{C=h_Bh_A^\dagger}
$$

transforms only by conjugation at the start vertex,

$$
C\to g_0Cg_0^\dagger,
$$

so `Tr C` is gauge invariant.

This cleanly separates two notions:

- **endpoint representation / physical flux geometry**;
- **which microscopic route realizes the coarse edge**.

## 4. Path qubit

The smallest local route register is

$$
\mathcal H_{path}=\operatorname{span}\{|A\rangle,|B\rangle\}\cong\mathbb C^2.
$$

A local rerouting is a unitary rotation

$$
\boxed{
R(\theta)=e^{-i\theta Y_{path}/2}.
}
$$

At finite refinement this is an elementary plaquette deformation.  A macroscopic
edge is a string/path on the underlying 2-complex and a small spatial
diffeomorphism is represented by a sequence of local reroutings.  As the
microscopic cell size decreases, one path move corresponds to a smaller
physical displacement.

The path qubit is **gauge/embedding data**, not a new propagating graviton
polarization.  It must disappear from the physical degree count after the
diffeomorphism constraint is imposed.

## 5. Curvature and diffeomorphism become the same local geometry

The two routes differ by the plaquette boundary:

$$
\boxed{
U(p_B)U(p_A)^{-1}=U(\partial\Sigma).
}
$$

For a small cell,

$$
U(\partial\Sigma)
=I+F_{ab}\Sigma^{ab}+O(\Sigma^2).
$$

Thus the microscopic variable needed to **reroute an edge under a spatial
diffeomorphism** is already controlled by the same loop curvature which enters
the Hamiltonian/vector constraints.

This makes a path register a natural extension of the existing
connection/holonomy architecture rather than an unrelated new degree of
freedom.

## 6. Numerical regression

`scripts/path_rerouting_diffeo_gate.py` checks 1000 random SU(2) configurations.
It finds:

- endpoint covariance error below `8e-16`;
- relative-loop trace gauge error below `1.6e-15`;
- path-qubit rerouting unitarity at machine precision;
- exact small-curvature route-difference identities.

## 7. Two valid future routes

### Route A -- exact embedded-LQG HDA

Augment the coarse spin-network state by route data,

$$
|\Gamma,j,\iota;\{p_e\}\rangle.
$$

Then construct finite diffeomorphisms as local path reroutings and test the
Hamiltonian commutator against the nontrivial translated-path action on a
vertex-smooth habitat.

### Route B -- intrinsic Regge-effective HDA

Do not introduce path gauge registers.  Instead reconstruct a semiclassical
metric/flux geometry and represent `D` as the canonical transformation induced
by discrete vertex displacement on the intrinsic data.  This is cheaper but is
an effective large-spin route, not an exact microscopic realization of the
standard embedded-LQG diffeomorphism action.

The two routes should agree in the same semiclassical continuum window, but
they must not be conflated at finite cutoff.

## 8. Recommended architecture

For the binary microscopic programme the most direct exact route is

$$
\boxed{
\text{Peter--Weyl spin/flux links}
\times
\text{binary path/rerouting register}
}
$$

with the path register realized by local alternatives on the already-existing
underlying 2-complex.  This preserves a finite/binary microscopic description
while adding precisely the gauge information which the off-shell
diffeomorphism algebra needs.
