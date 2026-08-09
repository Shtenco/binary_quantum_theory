# BF versus GR: first-class degree-count discriminator

Status: **exact canonical counting gate**.

A future microscopic constraint algebra can close perfectly and still describe
the wrong universality class.  The cleanest example is four-dimensional BF
theory versus general relativity.

## 1. Common canonical phase space

On a spatial slice use an SU(2) connection and densitized triad,

$$
(A_a^i,E^a_i),
$$

with

$$
9+9=18
$$

phase-space dimensions per spatial point before constraints.

## 2. Topological BF count

SU(2) BF has

- 3 Gauss constraints;
- flatness constraints `F_ab^i=0`.

There are nominally `3 x 3 = 9` curvature components (`ab` antisymmetric in
three spatial dimensions), but the Bianchi identities supply three
reducibility relations.  Thus the independent flatness rank is six.

Assuming the regular first-class sector,

$$
N_{phase}^{BF}
=18-2(3+6)
=\boxed{0}.
$$

There are no local propagating configuration degrees of freedom.

This is exactly the universality class represented by the Ooguri/15j flatness
control discussed in `K5_DUAL_BF_CONTROL.md`.

## 3. GR count

Canonical general relativity has

- 3 Gauss constraints;
- 3 spatial diffeomorphism constraints;
- 1 Hamiltonian constraint.

Hence

$$
N_{phase}^{GR}
=18-2(3+3+1)
=\boxed{4},
$$

or

$$
\boxed{N_{config}^{GR}=2}.
$$

These are the two local gravitational configuration degrees of freedom which
become the two helicities in the weak-field limit.

## 4. RG discriminator

Therefore a successful microscopic gravity phase must not merely show that
`some constraints close`.  It must show the correct **independent first-class
rank and reducibility structure**.

The held-out target is

$$
\boxed{
\operatorname{rank}_{FC}
\longrightarrow
3_G+3_D+1_H=7,
}
$$

with four remaining physical phase dimensions.

A flow toward

$$
\boxed{
3_G+6_{flat}=9
}
$$

is a BF/topological FAIL even if:

- the operators are gauge invariant;
- their local form looks like `EEF`;
- the 15j / 4-simplex state is annihilated;
- the Regge action appears in a semiclassical phase;
- the constraint algebra is anomaly free.

## 5. Practical finite test

On each collective blocking scale `b`, compute the numerical rank of the
constraint Jacobian / commutator-generated first-class distribution after
removing exact reducibilities.

Track

$$
r_G(b),\qquad r_D(b),\qquad r_H(b),\qquad r_{extra}(b).
$$

The GR target is

$$
\boxed{
(r_G,r_D,r_H,r_{extra})\to(3,3,1,0).
}
$$

The BF control is

$$
\boxed{
(3,0,0,6)
}
$$

when the six independent extra constraints are identified as flatness
projections rather than HDA generators.

This rank test should be evaluated together with the nontrivial off-shell HDA
functional test.  Rank alone cannot identify the structure functions, but it
can immediately reject a topological BF fixed point masquerading as gravity.
