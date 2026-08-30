# K5 full-active S5 carrier symmetry — preregistration

Status: **finite exact representation-theory theorem on the j=1/2 fully-active K5 carrier.  It is not yet a graph-changing Hamiltonian covariance theorem.**

## Frozen object

The complete graph `K5` has automorphism group `S5`.  In the fully-active all-edge `j=1/2` sector each of its five four-valent nodes carries the two-dimensional Gauss-singlet recoupling carrier with ordered basis `(K=0,K=2)`, hence

\[
\mathcal H_{\rm full}^{j=1/2}\cong(\mathbb C^2)^{\otimes5},\qquad \dim=32.
\]

For a vertex permutation `g in S5`, the induced action is frozen as follows:

1. old node `v` is sent to new node `g(v)`;
2. the four neighbours of `v` and `g(v)` are each listed in ascending canonical vertex order;
3. the resulting relabelling of the four local tensor legs induces the canonical `[2,2]` recoupling matrix obtained by direct magnetic-space overlap;
4. the five transformed local carriers are placed at their relabelled nodes with no fitted phases, basis rotations or target-state alignment.

This defines a 32D matrix `U_g` for each of all 120 vertex permutations.

## Preregistered representation checks

A GREEN gate must verify:

- all 120 `U_g` are unitary;
- the identity permutation gives `I_32`;
- composition with each adjacent-transposition Coxeter generator agrees with the group product for every `g in S5`;
- adjacent generators satisfy the exact S5 Coxeter relations;
- characters are constant within every S5 conjugacy class;
- the class characters are

  - `1^5 : 32`,
  - `2 1^3 : 0`,
  - `2^2 1 : 8`,
  - `3 1^2 : 2`,
  - `3 2 : 0`,
  - `4 1 : 0`,
  - `5 : 2`;

- the trivial-representation multiplicity computed from the character average is exactly `2`;
- the alternating/sign-representation multiplicity computed from the parity-weighted character average is exactly `2`;
- direct group-average projectors onto both sectors are Hermitian idempotents of rank two and are mutually orthogonal.

## Oriented five-tetrahedron vertex check

Use the independent tensor `scripts/five_tetrahedron_vertex_gate.py::vertex_tensor`, normalized in the same 32-component ordered recoupling basis.

The gate must test, without fitting a phase per group element,

\[
\boxed{U_g|V_5\rangle=\operatorname{sgn}(g)|V_5\rangle\quad\forall g\in S_5.}
\]

Equivalently, `V5` must lie in the alternating projector and be orthogonal to the trivial projector.

Because the alternating multiplicity is preregistered as two, **symmetry alone is explicitly not allowed to be interpreted as uniquely selecting `V5`**.

## Claim boundary

Even a GREEN result proves only the automorphism representation of the 32D fully-active carrier and the orientation character of the independent simplicial vertex.  It does not prove

- covariance of `H_v` on graph-changing Peter-Weyl output states;
- HDA closure;
- uniqueness of the physical simplicial state;
- Q4↔K5 global graph equivalence;
- a physical projector, continuum limit or phenomenology.

The next required theorem after GREEN is an `S5`-covariant transport of **general graph-changing K5 Peter-Weyl state keys**, followed by a direct test of

\[
U_gH_vU_g^{-1}=H_{g(v)}
\]

or the correctly derived orientation-character variant if the implementation contains a pseudoscalar node convention.
