# BQG ancilla-assisted Peter-Weyl refinement theorem

Status:
- **PROVED**: no nonzero SU(2)-intertwiner \(V_j\to V_{j+1/2}\) exists.
- **PROVED**: after adjoining one binary spin-\(1/2\) strand, the symmetric
  \(j+1/2\) channel is selected by a unique SU(2)-intertwining isometry up to
  phase.

## 1. Direct refinement no-go

For irreducible SU(2) representations \(V_j\) and \(V_{j+1/2}\),

\[
\mathrm{Hom}_{SU(2)}(V_j,V_{j+1/2})=0
\]

because the irreps are inequivalent.

Therefore the naive refinement arrow

\[
\boxed{
V_j\longrightarrow V_{j+1/2}
}
\]

cannot be SU(2)-equivariant.

Any full-habitat refinement that changes edge spin by \(1/2\) must add
microscopic degrees of freedom.

## 2. Binary ancilla resolves the obstruction

Add one fresh spin-\(1/2\) strand,

\[
V_j\otimes V_{1/2}.
\]

Clebsch-Gordan decomposition gives

\[
\boxed{
V_j\otimes V_{1/2}
=
V_{j+1/2}\oplus V_{j-1/2}.
}
\]

Each summand appears with multiplicity one.

Therefore

\[
\dim\mathrm{Hom}_{SU(2)}
\left(
V_{j+1/2},
V_j\otimes V_{1/2}
\right)=1.
\]

Hence the inclusion

\[
\boxed{
J_j:
V_{j+1/2}
\hookrightarrow
V_j\otimes V_{1/2}
}
\]

is unique up to overall phase.

Its adjoint

\[
\boxed{
B_j=J_j^\dagger:
V_j\otimes V_{1/2}
\to
V_{j+1/2}
}
\]

is the unique symmetric blocking coisometry.

This is exactly the representation-theoretic content of adding one active q=2
strand to the fully symmetric endpoint block.

## 3. Explicit occupation-basis isometry

Write \(n=2j\).  In the normalized symmetric occupation basis

\[
|k\rangle_n,
\qquad
k=0,\ldots,n,
\]

with \(m=k-n/2\), the inclusion
\(J_n:\mathrm{Sym}^{n+1}(\mathbb C^2)\to
\mathrm{Sym}^{n}(\mathbb C^2)\otimes\mathbb C^2\) is

\[
\boxed{
J_n|k\rangle_{n+1}
=
\sqrt{\frac{n+1-k}{n+1}}
\,|k\rangle_n\otimes|0\rangle
+
\sqrt{\frac{k}{n+1}}
\,|k-1\rangle_n\otimes|1\rangle,
}
\]

where absent basis terms at \(k=0\) or \(k=n+1\) are omitted.

It satisfies

\[
\boxed{
J_n^\dagger J_n=I_{n+2}.
}
\]

Let \(J_a^{(n/2)}\) be the spin-\(j\) generators and
\(s_a=\sigma_a/2\) the ancilla generators.  Then

\[
\boxed{
\left(
J_a^{(j)}\otimes I
+
I\otimes s_a
\right)J_n
=
J_n J_a^{(j+1/2)}
}
\]

for \(a=x,y,z\).

Thus the map is exactly SU(2)-equivariant.

## 4. Relation to the BQG q=2 tower

The repository already proves that \(n\) symmetrically blocked active q=2
strands carry

\[
j=\frac n2.
\]

The present theorem identifies the single refinement step

\[
n\to n+1
\]

as the unique ancilla-assisted map

\[
\boxed{
\mathrm{Sym}^n(\mathbb C^2)\otimes\mathbb C^2
\to
\mathrm{Sym}^{n+1}(\mathbb C^2).
}
\]

Therefore the Peter-Weyl refinement ladder is not an arbitrary representation
jump.  It is the repeated addition and symmetric blocking of one binary
microscopic strand.

## 5. Consequence for graph-changing habitat refinement

The selected-channel map \(\iota_0\) on the base logical carrier must be
extended to the one-hit graph/spin-changed habitat.

The present theorem supplies the canonical edgewise ingredient:

\[
\boxed{
\text{old edge }V_j
+
\text{new q=2 strand }V_{1/2}
\to
V_{j+1/2}.
}
\]

A full \(\iota_1\) is obtained only after:

1. specifying the ancillary q=2 strands on all affected edges;
2. applying the unique symmetric blocking map edgewise;
3. imposing the Gauss/intertwiner projection at the affected nodes;
4. matching graph/no-link sectors consistently.

Thus the theorem closes the representation-theoretic obstruction but leaves
the many-edge Gauss-compatible habitat map as the next finite construction.

This is the correct microscopic route for the two-sided habitat refinement
theorem.
