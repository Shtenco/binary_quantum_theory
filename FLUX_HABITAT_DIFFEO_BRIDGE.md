# Flux representation of the simplex diffeomorphism action

Status: **exact classical bridge / finite numerical regression PASS**.

The graph-changing HDA correction creates a new practical question: how should
the discrete tangential generator `D(k,l)` act on a vertex-smooth test
functional without introducing an external coordinate field by hand?

For a tetrahedral spatial slice the answer is already contained in the
canonical flux geometry.

## 1. Barycentric identity

Let the oriented tetrahedron have vertices `x_0,...,x_3`, volume `V`, and
barycentric coordinates `lambda_l`.  The gradient

$$
\nabla\lambda_l
$$

is normal to the triangular face opposite vertex `l` and points toward
increasing `lambda_l`.  Its norm is the inverse height above that face.  Since

$$
V=\frac13 A_l h_l,
$$

we have

$$
\boxed{
E_l=3V\,\nabla\lambda_l,
}
$$

where `E_l` is the oriented area/flux vector of the opposite face.  The four
fluxes close,

$$
\boxed{\sum_{l=0}^{3}E_l=0}.
$$

This is the same normalization that appears in the flat d=4 simplex-boundary
deformation algebra of Bonzom--Dittrich: their tangential normal
`check N(l|0)=3 V N(l|0)` has magnitude equal to the opposite face area.

Therefore, up to the once-fixed orientation convention,

$$
\boxed{\check N(l|0)=E_l}.
$$

## 2. Vertex-smooth diffeomorphism generator

Their `D(k,l)` translates spatial vertex `k` by `-check N(l|0)`.  Hence on a
smooth test functional `f(x_0,...,x_3)`,

$$
\boxed{
D(k,l)f
=-E_l^a\frac{\partial f}{\partial x_k^a}.
}
$$

Consequently the flat 4-simplex HH structure function

$$
\{H(k),H(k')\}
=\frac{D(k'k)-D(kk')}{3V}
$$

can be evaluated entirely from the canonical face fluxes:

$$
\boxed{
\{H(k),H(k')\}f
=
\frac{
-E_k\cdot\partial_{x_{k'}}f
+E_{k'}\cdot\partial_{x_k}f
}{3V}
}
$$

with sign changes only from the declared orientation convention.

This is the important bridge: the off-shell RHS does **not** require an
independently invented tangential quantum operator.  Its deformation vector is
already a fundamental flux observable.

## 3. Numerical regression

`scripts/flux_habitat_diffeo_gate.py` tests 100 random nondegenerate oriented
tetrahedra.

For each tetrahedron it constructs

$$
E_l=3V\nabla\lambda_l
$$

from the inverse edge matrix and compares `|E_l|` with the directly computed
opposite-face area.  With seed `260809`:

- worst relative face-area error: below `6.2e-16`;
- worst closure residual `||sum_l E_l||`: below `1.2e-15`.

It then generates random quadratic vertex-smooth functionals and compares

$$
-E_l\cdot\partial_{x_k}f
$$

with the centered finite difference obtained from

$$
x_k\to x_k\mp\epsilon E_l,
\qquad \epsilon=10^{-7}.
$$

The worst relative derivative error is below `2.6e-8`.

The finite-difference error is only a regression check; the barycentric/flux
identity itself is exact.

## 4. Consequence for the quantum test

The next off-shell quantum functional can be made relational:

1. reconstruct/coarse-grain flux expectation values `E_l` from the
   spin-network state;
2. require closure and shape matching so that a spatial tetrahedral geometry is
   defined;
3. choose preregistered nonconstant vertex-smooth functions `f`;
4. evaluate the dual graph-changing HH action on `F_f`;
5. compare it with
   `(-E_k.partial_{x_k'}+E_k'.partial_{x_k})f/(3V)`.

Thus the target uses the same canonical flux variables as the Peter--Weyl
Hamiltonian and avoids both bad extremes:

- no artificial projection to a fixed spin sector;
- no trivial full-diffeomorphism average that can hide a vanishing-commutator
  anomaly.

The remaining hard step is quantum: define the vertex-smooth/relational
functional on the collective coherent spin-network outputs and check the dual
HH action in a regulator-safe Lorentzian window.
