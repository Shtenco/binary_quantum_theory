# BQG global K5 binary-ancilla symmetry test

The correct microscopic node refinement is bilinear in the old logical
\([2,2]\) state and a fresh ancilla \([2,2]\) state. A fixed local pure
ancilla is forbidden by tetrahedral symmetry, so the next object must be a
**correlated global ancilla layer** on shared graph edges.

The existing Peter-Weyl K5 implementation already contains a natural
all-\(j=\frac12\) spin-network contraction, called v5_tensor in the production
code, a 32-component tensor over the five local Gauss-singlet doublets.

This gate constructs the exact \(S_5\) vertex-permutation action on that 32D
logical space, including induced local \(S_4\) recouplings, and tests whether
the existing K5 tensor spans a unique one-dimensional trivial or sign symmetry
sector.

A positive result would provide a symmetry-selected correlated q=2 ancilla
layer

\[
\boxed{
|\Omega_{\rm anc}\rangle_{\rm K5}
}
\]

without introducing fitted local ancilla vectors.

That layer is the natural next candidate for extending the microscopic
bilinear refinement tensor from one node to the full graph-changing K5
habitat, where the one-hit residuals \(E_v,F_v\) can be measured.

The result remains kinematical until compatibility with the actual physical
master/history construction is demonstrated.
