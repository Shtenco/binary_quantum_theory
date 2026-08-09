# Collective j=1 volume-dynamics gate

Status: **exact finite collective SU(2) control; demonstrates the first representation scale at which curvature plus volume opens a new intertwiner channel**.

## 1. Minimal collective link

Generalize the active/off quantum link to

\[
\mathcal H_{link}^{(j)}=(V_j^L\otimes V_j^R)\oplus\mathbf1.
\]

With the invariant spin-j tensor `epsilon`, an operator-valued transporter can be written schematically as

\[
U_{mn}=|m,n\rangle\langle off|
+\epsilon_{mp}\epsilon_{nq}|off\rangle\langle p,q|,
\]

and satisfies exact left/right SU(2) covariance.  For `j=1` the link Hilbert dimension is

\[
3^2+1=10.
\]

Use an exactly solvable stress-test graph: two four-valent nodes joined by four such links.  The raw Hilbert dimension is `10^4=10000`, while exact Gauss reduction leaves

\[
\boxed{1+6+3^2=16}
\]

states: one empty state, six two-link singlet sectors, and nine fully active left/right intertwiner states.

## 2. First non-scalar tetrahedral volume

For four spin-1 faces the three-dimensional intertwiner basis has intermediate pair spin `k=0,1,2`.  The oriented triple product has spectrum

\[
\operatorname{spec}Q=\{-\sqrt3,0,+\sqrt3\}.
\]

Therefore the absolute volume, up to the conventional overall scale, has spectrum

\[
\boxed{
\operatorname{spec}V=\{0,3^{1/4},3^{1/4}\}.
}
\]

This is the first collective scale at which `V` is not proportional to the identity on the four-valent intertwiner space.

## 3. Exact curvature-volume commutator

Let

\[
W=\sum_{1\le a<b\le4}\operatorname{Tr}(U_aU_b^\dagger)
\]

be the sum of the six exact two-link Wilson loops of the dipole graph.  The projected `16 x 16` matrix is Hermitian to about `1e-14`.

For the left-node volume operator,

\[
\boxed{
\|[W,V_L]\|_F=9.1180282278,
\qquad
\operatorname{rank}[W,V_L]=6.
}
\]

The Hermitian commutator `i[W,V_L]` has three positive and three negative nonzero eigenvalues,

\[
\pm4.02067252\quad(2\times),
\qquad
\pm3.03934274\quad(1\times),
\]

with ten zero modes.

For `V_L+V_R`,

\[
\|[W,V_L+V_R]\|_F=15.49766799,
\]

again with rank six.

## 4. Cyclic-space threshold

Starting from the empty state,

\[
\dim\mathcal K(W)|0\rangle=3,
\]

whereas

\[
\boxed{
\dim\mathcal K(W,V_L)|0\rangle=4.
}
\]

This is the qualitative change absent at microscopic `j=1/2`, where absolute volume is scalar inside the four-valent intertwiner qubit and scalar volume does not enlarge the Wilson cyclic sector.

Thus

\[
\boxed{
j=1/2:\ F+V\text{ adds no intertwiner channel},
\qquad
j=1:\ F+V\text{ adds one}.}
\]

## 5. Physical nature of the new channel

The extra direction is orthogonal to the pure-Wilson cyclic space and lies entirely in the nine-dimensional fully active intertwiner sector.

For the normalized fully-active component of `W^2|0>`, the left/right intertwiner Schmidt probabilities are numerically the exact rationals

\[
\boxed{
\left\{\frac{25}{33},\frac4{33},\frac4{33}\right\}
}
\]

and

\[
\frac{\langle V_L\rangle}{3^{1/4}}=\frac8{33}.
\]

For the new orthogonal volume-generated channel they are

\[
\boxed{
\left\{\frac{25}{66},\frac{25}{66},\frac8{33}\right\}
}
\]

and

\[
\boxed{
\frac{\langle V_L\rangle}{3^{1/4}}=\frac{25}{33}.
}
\]

Their left/right entanglement entropies are respectively

\[
S_W=1.04147276\text{ bits},
\qquad
S_{new}=1.55662428\text{ bits}.
\]

Hence the new cyclic direction is not an occupancy artifact.  It is a more strongly entangled, high-volume intertwiner/shape channel.

## 6. Interpretation

This supplies a concrete microscopic RG threshold:

\[
\boxed{
\text{single-qubit face }j=1/2
\xrightarrow{\text{first collective block}}
 j=1
\xrightarrow{}
\text{nontrivial shape-sensitive volume dynamics}.
}
\]

It explains why the microscopic `j=1/2` BF-like calculations can have exact recoupling/constraint structure while genuine gravity information first becomes distinguishable only after representation growth.

It still does not prove Lorentzian GR.  The next required calculation is whether collective shape-sensitive constraints acquire the DeWitt kinetic signature and first-class hypersurface-deformation algebra rather than merely a larger SU(2) cyclic algebra.
