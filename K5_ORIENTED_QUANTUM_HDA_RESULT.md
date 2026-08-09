# Oriented K5 quantum-HDA result at Jmax=1/2

Status: **strong finite diagnostic / FAIL as physical HDA; exact simplex-symmetry skeleton identified**.

This calculation uses the exact 140-dimensional Gauss Hilbert of the vector-5 (`Jmax=1/2`) K5 model, but corrects the node Hamiltonian sum by the geometric orientation signs of an oriented tetrahedron.

For a sorted neighbour list `[n0,n1,n2,n3]`, the triple omitting `nr` carries

\[
\epsilon_v(n_a,n_b,n_c)=(-1)^r.
\]

These signs are exactly the signs obtained from outward face normals of a regular oriented tetrahedron, up to one irrelevant overall sign per node.

## 1. Orientation restores S5 covariance

Before orientation correction, different vertex pairs had basis-invariant rank differences (`8` versus `0`) in their fixed-sector HH commutators.  After inserting the tetrahedral signs, all ten pairs `i<j` agree to numerical precision.

For the Hermitian completion

\[
H_v=\frac12(S_v+S_v^\dagger),
\]

all ten pairs have

\[
\boxed{\|[H_i,H_j]P_{full}\|=3906.6220702801},
\]

\[
\boxed{\epsilon_{graph}=\sqrt{37/69}=0.7322785563281},
\]

and

\[
\boxed{\operatorname{rank}(-iP_{full}[H_i,H_j]P_{full})=12.}
\]

The norm-squared decomposition is therefore

\[
\boxed{
\frac{\|P_{full}[H_i,H_j]P_{full}\|^2}
{\|[H_i,H_j]P_{full}\|^2}=\frac{32}{69},
\qquad
\frac{\|(1-P_{full})[H_i,H_j]P_{full}\|^2}
{\|[H_i,H_j]P_{full}\|^2}=\frac{37}{69}.
}
\]

Thus arbitrary-label asymmetry is removed, but a large graph-changing anomaly remains.

## 2. Fixed-sector operator is purely three-body in intertwiner qubits

Define

\[
Q_{ij}=-iP_{full}[H_i,H_j]P_{full}.
\]

For every pair,

\[
\boxed{\operatorname{spec}Q_{ij}=\{-768^{\times6},0^{\times20},+768^{\times6}\}.}
\]

A Pauli-string fit on the five tetrahedral intertwiner qubits gives

\[
\epsilon_{weight\le2}=1,
\qquad
\boxed{\epsilon_{weight\le3}<1.3\times10^{-14}}.
\]

So the fixed-triangulation part is a pure weight-three shape/intertwiner operator rather than a one-body deformation.

For the pair `(0,1)` one exact convention-dependent Pauli representation is

\[
\begin{aligned}
Q_{01}=96[&2(X_0Y_1-Y_0X_1)Z_2\\
&-(X_0Y_1-Y_0X_1)(Z_3+Z_4)\\
&+\sqrt3(Y_0Z_1-Z_0Y_1)(Z_3-Z_4)].
\end{aligned}
\]

Other pairs are related by the K5 permutation/recoupling symmetry.

## 3. The old V5 common kernel survives the orientation correction

Using the oriented **raw** node sums on the 32D fully-active sector, the stacked rank flow is

\[
21\to29\to31,
\]

so the common-kernel dimensions are

\[
11\to3\to\boxed1.
\]

The unique null vector has

\[
\boxed{|\langle\psi_{null}|V_5\rangle|^2=1}
\]

within machine precision.  For the first three oriented node sums the smallest nonzero singular value is approximately `40.8148`, while the null singular value is approximately `4.9e-14`.

Therefore the earlier BF/15j-like physical-state kernel is robust, whereas the HDA closure is not.  This is an explicit finite example of

\[
H_v\Psi=0
\quad\not\Rightarrow\quad
[H_v,H_w]\sim D_{vw}.
\]

## 4. Exact SO(5) Lie skeleton inside the fixed-sector commutators

The ten matrices `Q_ij` are linearly independent and Frobenius-orthogonal:

\[
\boxed{
\operatorname{rank}\operatorname{span}\{Q_{ij}\}=10,
\qquad
\|Q_{ij}\|^2=7\,077\,888=12\cdot768^2.
}
\]

Let `P_Q` be the Frobenius projector onto this ten-dimensional operator span.  For three distinct indices,

\[
\boxed{
P_Q\{-i[Q_{ij},Q_{ik}]\}=32Q_{jk}
}
\]

with the corresponding antisymmetric sign changes.  For disjoint pairs the projected bracket is zero.  Thus the projected structure constants are exactly those of `so(5)`, up to the common normalization `32`.

However the full operator bracket contains a large orthogonal component.  For overlapping generators,

\[
\frac{\|P_Q[-i[Q,Q]]\|^2}{\|[Q,Q]\|^2}=\boxed{\frac1{297}},
\]

and therefore

\[
\boxed{
\epsilon_{Lie}=\sqrt{\frac{296}{297}}=0.9983150788.
}
\]

For disjoint generator pairs the entire finite commutator is outside the `Q` span even though its `so(5)` projection correctly vanishes.

This identifies a much sharper collective-limit observable:

\[
\boxed{
\epsilon_{Lie}(j)
=\frac{\|(1-P_Q)[Q,Q]\|}{\|[Q,Q]\|}
\to0,
}
\]

while the normalized projected `so(5)` structure constants remain stable.

## 5. Regulator wall

This calculation must **not** be called a physical quantum-HDA failure of the whole Peter--Weyl architecture.  A local Hamiltonian term touches any one link at most twice; an HH product can touch the shared link at most four times.  The Peter--Weyl exactness condition is therefore

\[
J_{max}\ge j_{in}+2.
\]

For the all-`j=1/2` K5 boundary,

\[
\boxed{J_{max}^{safe}=5/2.}
\]

The current vector-5 model has `Jmax=1/2` and is far below that wall.

A combinatorial reachability calculation nevertheless shows that the safe problem is tractable: after one H there are 120 Gauss-admissible spin assignments with total spin-network dimension 816; after HH for any vertex pair there are 4193 admissible assignments with total spin-network dimension at most 24364, and the reachable spin exactly saturates `j=5/2`.

Thus the next exact calculation should use this reachable spin-network basis rather than a dense `91^10` link Hilbert space.
