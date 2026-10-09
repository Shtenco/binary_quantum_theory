# BQG microscopic bilinear refinement theorem

Status:
- **NO-GO / PROVED**: a fixed pure four-qubit Gauss-singlet ancilla cannot
  produce an \(S_4\)-equivariant linear refinement map from the old
  \([2,2]\) logical carrier to the coarse \([2,2]\) carrier.
- **PROVED finite representation structure**: the correct microscopic object is
  the bilinear refinement tensor
  \([2,2]_{\rm old}\otimes[2,2]_{\rm anc}\to[2,2]_{\rm coarse}\).

The four fresh binary edge strands form a Gauss singlet space

\[
\mathcal A
=
\mathrm{Inv}_{SU(2)}[(1/2)^{\otimes4}]
\simeq [2,2]_{S_4}.
\]

This representation has no trivial \(S_4\) subrepresentation, hence

\[
\boxed{
\mathcal A^{S_4}=\{0\}.
}
\]

Therefore no nonzero fixed ancilla state \(|\chi\rangle\) is invariant under all
tetrahedral permutations.  Fixing such a vector necessarily breaks the
symmetry, so the induced map

\[
T_\chi:[2,2]_{\rm old}\to[2,2]_{\rm coarse}
\]

cannot be the canonical \(S_4\) intertwiner.

The correct product decomposition is

\[
\boxed{
[2,2]\otimes[2,2]
=
[4]\oplus[2,2]\oplus[1^4].
}
\]

In particular,

\[
\dim\mathrm{Hom}_{S_4}
([2,2]\otimes[2,2],[2,2])=1.
\]

Thus the microscopic symmetric-blocking construction contains a **unique
bilinear \([2,2]\) refinement vertex up to normalization**.

The companion gate constructs this tensor from:

1. an old four-spin-\(1/2\) Gauss singlet;
2. a fresh four-spin-\(1/2\) ancilla Gauss singlet;
3. the unique symmetric edge blocking
   \(V_{1/2}\otimes V_{1/2}\to V_1\);
4. projection onto the coarse spin-1 Gauss singlet sector.

After projection to the coarse \([2,2]\) sector it verifies exact simultaneous
\(S_4\) covariance.

## Consequence for continuum refinement

The microscopic refinement is not an isometry on the old logical Hilbert space
alone.

It is an interaction/isometry involving newly created binary degrees of
freedom:

\[
\boxed{
\mathcal L_j\otimes\mathcal A_{\rm new}
\longrightarrow
\mathcal H_{j+1/2}^{\rm coarse}.
}
\]

A reduced channel on \(\mathcal L_j\) appears only after the theory supplies a
state/history prescription for the new ancillas or keeps them as part of the
enlarged refinement Hilbert space.

Therefore the final continuum construction should be formulated either as:

- an inductive isometry on **old system + new binary ancillas**, or
- a covariant quantum channel after ancilla/environment reduction.

This is a sharper formulation than assuming a direct pure-state embedding
\(V_j\to V_{j+1/2}\).
