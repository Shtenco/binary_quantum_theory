# Spatial qubit geometry bridge

Status: **exact/finite canonical geometry control; not yet a frozen topology-changing microscopic theory**.

## 1. Lorentzian-safe correction

A single qubit with unitary `SU(2)` transport is a natural carrier for the canonical spatial Ashtekar--Barbero gauge algebra, but it is not an exact finite-dimensional carrier of the full Lorentzian self-dual `SL(2,C)` spacetime connection.  Therefore the minimal binary route is interpreted canonically:

\[
\text{face qubits on a spatial slice}
+SU(2)\text{ holonomy}
+\text{causal rewrite time}.
\]

Lorentzian physics must then be tested through the dynamical exponent, extrinsic-curvature/Hamiltonian dynamics and constraint algebra, rather than assumed from the internal `SU(2)` label.

## 2. Binary dimension selector

For one qubit,

\[
\dim_{\mathbb R}su(2)=2^2-1=3.
\]

Its three Pauli expectation values can therefore supply a three-component face flux

\[
E_f^i=\operatorname{Tr}(\rho_f\sigma^i).
\]

If the gauge-invariant coarse node satisfies closure,

\[
\sum_{f\ni v}E_f=0,
\]

then Minkowski reconstruction interprets the areas and normals as a convex three-dimensional polyhedron.  A non-degenerate minimal closed cell has four faces, hence a tetrahedron.

This gives the conditional dimension chain

\[
\boxed{
\dim\mathcal H_{micro}=2
\Rightarrow \dim su(2)=3
\Rightarrow 3D\text{ spatial flux geometry}
\Rightarrow 3+1\text{ only if }z\to1.
}
\]

The last implication is dynamical and remains open.

## 3. Exact Gauss blocking: four qubits -> one geometry qubit

Four spin-1/2 face qubits decompose as

\[
\left(\frac12\right)^{\otimes4}
=
2\times j=0\oplus3\times j=1\oplus1\times j=2.
\]

Therefore the exact gauge-invariant singlet sector has dimension two:

\[
\boxed{4\text{ face qubits}\xrightarrow{J_{tot}=0}1\text{ logical geometry qubit}.}
\]

For the Gauss penalty

\[
H_G=\lambda\,\mathbf J_{tot}^2
\]

the exact spectrum is

\[
0\;(2\times),\qquad2\lambda\;(9\times),\qquad6\lambda\;(5\times),
\]

so the logical geometry sector is separated from gauge-violating states by gap `2 lambda`.

## 4. The logical Pauli algebra is tetrahedral geometry

In the natural two-dimensional singlet basis,

\[
J_1\cdot J_2=-\frac14I-\frac12Z_L,
\]

\[
J_1\cdot J_3=-\frac14I+\frac14Z_L-\frac{\sqrt3}{4}X_L,
\]

while the oriented triple product is

\[
Q=J_1\cdot(J_2\times J_3)=\frac{\sqrt3}{4}Y_L.
\]

Thus the three Bloch coordinates of the logical qubit are not arbitrary labels: two parameterize independent gauge-invariant shape/dihedral observables and the third is oriented volume.  The exact oriented-volume eigenvalues are

\[
\boxed{\pm\frac{\sqrt3}{4}}.
\]

A fully face-permutation-symmetric one-cell Hamiltonian is trivial on this irreducible two-dimensional sector by Schur's lemma.  Nontrivial geometry dynamics must therefore arise from couplings between neighboring cells, not from a preferred on-site geometry rotation.

## 5. Exact tetrahedral reconstruction from fluxes

Let `A=(a,b,c)` contain the three edge vectors from one tetrahedron vertex.  Define three oriented face-area vectors

\[
E_1=\frac12 b\times c,
\qquad
E_2=\frac12 c\times a,
\qquad
E_3=\frac12 a\times b,
\]

and `E_0=-(E_1+E_2+E_3)`.  With

\[
C=(2E_1,2E_2,2E_3)
\]

one has

\[
C=\det(A)A^{-T},
\qquad
\det C=(\det A)^2,
\]

hence

\[
\boxed{A=\sqrt{|\det C|}\,C^{-T}.}
\]

The finite control reconstructs random non-degenerate tetrahedra to machine precision.  Independent flux noise makes both the closure defect and reconstructed shape error grow continuously, so these are useful RG observables rather than only exact identities.

## 6. Neighbor gluing is naturally Bell-entangled

For two neighboring logical geometry qubits, the Bell state

\[
|\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2}
\]

satisfies

\[
\langle X_vX_w\rangle=+1,
\quad
\langle Z_vZ_w\rangle=+1,
\quad
\langle Y_vY_w\rangle=-1.
\]

The two intrinsic shape coordinates therefore match while oriented volume/normal reverses across the common face.  The minimal gluing Hamiltonian

\[
\boxed{H_{glue}=-J(X_vX_w-Y_vY_w+Z_vZ_w)}
\]

has exact spectrum

\[
\boxed{-3J,+J,+J,+J}
\]

and therefore a unique Bell-glued ground state with gap `4J`.

## 7. Twisted-geometry falsifier

Area/normal matching alone does not imply Regge gluing.  Two triangles can have identical area and face normal but different intrinsic shapes.  The supplied negative control uses two equal-area triangles and obtains zero area mismatch but a normalized shape defect about

\[
\boxed{\Delta_{shape}\simeq0.2593}.
\]

Thus the microscopic scaling window must satisfy both

\[
\Delta_{closure}\to0,
\qquad
\Delta_{shape}\to0.
\]

This prevents a collection of individually valid quantum polyhedra from being misidentified as one smooth spatial metric.

## 8. New upstream chain

The Lorentzian-safe candidate architecture is now

\[
\boxed{
\text{face qubits}
\to SU(2)\text{ Gauss singlets}
\to\text{logical geometry qubits}
\to\text{Bell/shape gluing}
\to\text{3D Regge-like slice}
\to\text{causal rewrite dynamics}
\to 3+1\text{ only if }z\to1\text{ and HDA closes}.
}
\]

This removes the need to pretend that a finite `SU(2)` qubit is itself a Lorentzian `SL(2,C)` spacetime connection.

## 9. What remains open

The exact local Hilbert and gluing structure still does not supply the full microscopic rule.  A frozen candidate must next specify, without post-hoc tuning:

1. which local neighboring-cell pairs interact at each causal step;
2. how triangulation/topology changes reversibly;
3. how extrinsic-curvature information is encoded;
4. a unitary/history measure preserving the Gauss/gluing physical sector;
5. a common scaling window with `d_s^slice -> 3`, `z -> 1`, shape matching, two gapless spin-2 modes, ghost decoupling and nonlinear HDA/Ward closure.

## Reproduction

```bash
python scripts/spatial_qubit_geometry_gate.py \
  --trials 100 \
  --output verification_results/spatial_qubit_geometry_gate.json
```
