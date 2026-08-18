# Master constraint -> finite physical projector

Status: **exact finite-dimensional theorem; theory-specific history/refinement limit open.**

Let the already-defined regulated gravitational constraints on a finite carrier be `C_A`. For any positive-definite Hermitian constraint metric `G`, define

\[
\mathbb M_G=\sum_{A,B} C_A^\dagger G^{AB} C_B.
\]

Then

\[
\langle\psi|\mathbb M_G|\psi\rangle
=\|G^{1/2}C\psi\|^2\ge0,
\]

and therefore

\[
\boxed{\ker\mathbb M_G=\bigcap_A\ker C_A.}
\]

The exact common zero sector is independent of the arbitrary positive `G`; only the nonzero spectrum and numerical conditioning depend on `G`.

If zero is isolated at a finite regulator,

\[
P_{\rm phys}=\mathbf 1_{\{0\}}(\mathbb M_G)
\]

is the unique orthogonal projector onto the common constraint kernel. With first positive master gap `Delta_M`, the heat-kernel approximation satisfies

\[
\|e^{-T\mathbb M_G}-P_{\rm phys}\|=e^{-T\Delta_M}.
\]

This is the first post-HDA operator step. It does **not** re-test the hypersurface-deformation algebra and it does not introduce an external time variable.

For this repository the next calculation is to build `M_G` from the actual Peter-Weyl `H_v` columns, determine whether a finite common zero sector exists on declared carriers, and then test refinement/rigging convergence of normalized physical matrix elements.

The physical graviton kernel requires the further chain

```text
P_phys / rigging-history
 -> Z[J_g]
 -> W[J_g] = -i log Z[J_g]
 -> Gamma[g]
 -> K_TT(omega,k)
 -> six on-shell quartic Wilson coefficients.
```

A constraint resolvent parameter is not renamed physical `omega`. If the finite exact zero sector is empty, the result must be reported and followed by a frozen spectral-window/refinement analysis rather than by another HDA tuning cycle.

Executable theorem self-test: `scripts/master_constraint_physical_projector_gate.py`.

Gravity-specific finite pilot: `scripts/peter_weyl_master_projector_pilot.py`.
