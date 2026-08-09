# Dual-K5 EEF control: why an EEF-looking constraint can still be BF

Status: **literature-anchored structural control; separates the old K5/15j sector from genuine 4D GR dynamics.**

## 1. Exact same dual graph

Bonzom's canonical treatment of the quantum 4-simplex uses the LQG phase space
on the complex `Gamma` dual to the boundary of a 4-simplex:

- five tetrahedra -> five dual nodes `a=1,...,5`;
- ten triangles `(ab)` -> ten dual links;
- primal edges `(abc)` -> triangular dual cycles.

This is exactly the combinatorics of the K5 laboratory used in this repository.
The canonical data are SU(2) holonomies `g_ab` and fluxes `E_ab` on the ten
links, with closure/Gauss symmetry at the five tetrahedral nodes.

Primary reference:

- V. Bonzom, *Spin foam models and the Wheeler-DeWitt equation for the quantum
  4-simplex*, Phys. Rev. D 84, 024009 (2011), arXiv:1101.1615.

## 2. Curvature projected on two fluxes

For a triangular cycle `(abc)`, define

$$
g_{(abc)}=g_{ab}g_{bc}g_{ca}.
$$

The dual-graph constraint introduced there is

$$
\boxed{
H^a_{bc}
=
E_{ab}\cdot E_{ac}
-
E_{ab}\cdot\operatorname{Ad}(g_{(abc)})E_{ac}.
}
$$

For a small cycle curvature, write

$$
\operatorname{Ad}(g_{(abc)})
=I+F_{abc}\times+O(F^2).
$$

Then

$$
\begin{aligned}
H^a_{bc}
&=-E_{ab}\cdot(F_{abc}\times E_{ac})+O(F^2)\\
&=(E_{ab}\times E_{ac})\cdot F_{abc}+O(F^2).
\end{aligned}
$$

Therefore

$$
\boxed{H^a_{bc}\sim EEF}
$$

in precisely the local sense used throughout the canonical K5 programme.

## 3. Critical lesson: EEF does not uniquely identify GR

Bonzom's construction is a Hamiltonian reformulation of the flat Ooguri model,
i.e. four-dimensional topological SU(2) BF theory.  For nondegenerate triads,
having enough projected constraints around a cycle enforces the cycle holonomy
to be trivial (up to the finite sign ambiguity), hence flatness.

At the quantum level the corresponding Wheeler--DeWitt difference equations
are recursion relations of the SU(2) 15j symbol.

Thus

$$
\boxed{
\text{gauge invariant} + EEF\text{-looking} + 15j\text{ kernel}
\not\Rightarrow
\text{4D GR}.
}
$$

This is the clean theoretical explanation for why the old finite K5 constraints
could possess a beautiful five-tetrahedron `V5` kernel and still be correctly
classified as **BF-like**.

## 4. Consequence for the repository's old finite results

The following observations remain valuable but must not be used as a GR proof:

- `V5`/15j-like common kernels;
- exact SU(2) recoupling identities;
- Wilson/shape generation of the 4-simplex boundary state;
- projected SO(5)-like operator skeletons at the symmetric K5 point.

They demonstrate that the microscopic finite-link architecture naturally
contains the known topological/simplicial quantum-geometry sector.

The regulator-safe genuine-volume calculation strengthens the separation:

$$
\|H_0^{safe}V_5\|=1.4002194669856702\ne0,
$$

so the canonical genuine-volume operator does not simply preserve the old BF
physical state.

## 5. What has to distinguish GR from this BF control

A genuine canonical GR claim must pass tests which flat BF does not:

1. real Ashtekar--Barbero Lorentzian correction and the classical
   `beta`-cancellation target;
2. nontrivial off-shell hypersurface-deformation structure functions rather
   than only a flatness/15j recursion;
3. DeWitt kinetic inertia `(5+,1-,3 zeros)`;
4. first-class Gauss+diffeomorphism+Hamiltonian counting leaving two local
   physical configuration degrees of freedom;
5. interacting nonlinear GR / Regge-Einstein continuum cross-check;
6. regulator universality.

The BF operator above should therefore be retained as a **negative/structural
control** in future code.  A candidate quantum Hamiltonian which collapses to
this constraint class in the collective limit has recovered topological BF,
not four-dimensional gravity.
