# Binary adjoint dimension theorem

Status: **conditional structural theorem inside the canonical face-qubit architecture; not an empirical proof that nature must use these axioms**.

## Assumptions

Let the elementary local quantum carrier have Hilbert dimension `q` and assume:

1. local geometric observables are the traceless Hermitian operators on that carrier;
2. local frame changes act by the full unitary conjugation modulo global phase;
3. coarse geometric variables are additive fluxes in that adjoint space;
4. physical coarse nodes obey the corresponding Gauss/closure constraint;
5. closed nondegenerate flux configurations are interpreted geometrically through their areas and normals.

## Result

The real vector space of traceless Hermitian `q x q` matrices has dimension

\[
\boxed{D_{adj}=q^2-1}.
\]

For `q=2`, the Pauli basis identifies this space with `R^3`, and `SU(2)` conjugation induces `SO(3)` rotations of the Bloch/flux vector.  Under closure, Minkowski reconstruction therefore gives convex three-dimensional polyhedra.

Hence, under the stated assumptions,

\[
\boxed{D_{spatial}=q^2-1.}
\]

If the causal rewrite supplies one independent macroscopic time direction and its continuum scaling is relativistic (`z -> 1`), then

\[
\boxed{d_{spacetime}=1+D_{spatial}=q^2.}
\]

For a nontrivial integer local Hilbert dimension `q >= 2`, the equation `d_spacetime=4` has the unique solution

\[
\boxed{q=2.}
\]

Thus the binary carrier gives

\[
\boxed{
\mathbb C^2
\to su(2)\simeq\mathbb R^3
\to 3D\text{ spatial flux geometry}
\to 3+1\text{ only if causal }z\to1.
}
\]

## Minimal cell

In three dimensions a bounded nondegenerate convex cell requires at least four face normals.  The minimal closed cell is therefore a tetrahedron.  Four microscopic spin-1/2 face carriers have

\[
\left(\frac12\right)^{\otimes4}=2(0)\oplus3(1)\oplus1(2),
\]

so their exact `SU(2)`-invariant closure sector has dimension two.  This is the microscopic quantum-tetrahedron qubit analyzed in `SPATIAL_QUBIT_GEOMETRY_BRIDGE.md`.

## Continuum correction

The two-dimensional intertwiner space is only the `j=1/2` microscopic cell.  A coarse face made from `N` aligned microscopic qubits has `j=N/2`, and

\[
\dim\operatorname{Inv}(V_j^{\otimes4})=2j+1=N+1.
\]

Therefore the shape Hilbert space grows rather than remaining a qubit.  For a spin-coherent coarse face,

\[
\frac{\Delta J_\perp}{|\langle J\rangle|}=N^{-1/2}.
\]

If `N_face ~ b^2`, the normal-direction fluctuation scales as

\[
\boxed{\Delta n\sim b^{-1}.}
\]

This gives a parameter-free smooth-face scaling target for a future frozen microscopic ensemble.

## Boundary of the theorem

The conclusion is conditional.  It fails if geometry is not represented by the adjoint traceless observable algebra, if the relevant local frame group is a proper subgroup, if fluxes are not the geometric normals, if closure does not emerge, or if causal rewrite time fails to become a single relativistic direction.

In particular, this theorem does **not** replace the required measurements

\[
d_s^{slice}\to3,\qquad D_{link}\to3,\qquad z\to1,
\]

on held-out sizes of one frozen microscopic dynamics.  It supplies a structural reason for why a binary canonical theory can select `3+1`; the dynamical phase must still realize it.
