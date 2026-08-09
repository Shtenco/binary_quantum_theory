# Plebański connection-first Einstein gate

Status: **nontrivial finite Euclidean control; gives the next measurable stage after the Urbantke/simplicity bridge**.

## Question

`PLEBANSKI_URBANTKE_BRIDGE.md` shows that a simple non-degenerate triple of two-forms can reconstruct a metric.  That is still not the Einstein equations.

The self-dual Plebański chain supplies a sharper test.  Given `B^i`, solve for the compatible connection `A^i` from

\[
\boxed{
D_A B^i
=dB^i+\epsilon^{ijk}A^j\wedge B^k=0.
}
\]

Then compute

\[
F^i(A)=dA^i+\frac12\epsilon^{ijk}A^j\wedge A^k
\]

and decompose it into the self-dual and anti-self-dual bases defined by the same `B`-metric sector,

\[
F^i
=F^{ij}B^j+\bar F^{ij}\bar B^j.
\]

For vacuum Einstein geometry, the anti-self-dual block must vanish; the trace of the self-dual block contains the cosmological-curvature part while its traceless part is the self-dual Weyl curvature.

This gives a direct connection-first observable

\[
\boxed{
\Delta_{\rm ASD}
=
\frac{\|\bar F\|_F}
{\|F\|_F+\|\bar F\|_F}
}
\]

which cannot be passed merely by reconstructing some metric.

## Positive control: Euclidean `S^4`

Use the unit four-sphere in stereographic coordinates,

\[
g_{\mu\nu}(x)=\Omega(x)^2\delta_{\mu\nu},
\qquad
\Omega(x)=\frac{2}{1+|x|^2}.
\]

Only the corresponding self-dual `B^i` forms are passed to the solver.  The Levi-Civita/spin connection is **not** supplied.  At every point the code solves the 12 linear equations `D_A B=0` for the 12 components `A^i_mu`, differentiates the reconstructed connection and forms its curvature.

Across five test points, the worst residuals are

\[
\boxed{
\max \frac{\|D_A B\|}{\|dB\|}
=3.64\times10^{-17},
}
\]

\[
\boxed{
\max\Delta_{\rm ASD}=8.22\times10^{-9},
}
\]

and

\[
\boxed{
\max\Delta_{\rm self,tf}=4.98\times10^{-9}.
}
\]

The reconstructed self-dual curvature matrix is

\[
F^{ij}\simeq-\delta^{ij}
\]

with the sign set by the Euclidean duality conventions.  Thus the code recovers the constant-curvature Einstein sector directly from `B -> A_B -> F(A_B)`.

## Negative control: metric but not Einstein

To prove that the gate is not merely recognizing a conformal metric, use another smooth positive conformal factor,

\[
\Omega_{\rm nonE}(x)
=
\exp\left[
0.15\left(
 x_0x_1+0.30x_2^2-0.20x_3
\right)
\right].
\]

This still produces a perfectly simple, non-degenerate two-form triple and therefore a valid Urbantke metric.  The same compatibility equation `D_A B=0` is solved to machine precision.

However, the anti-self-dual curvature defect at the five test points is

\[
0.74174,
\quad0.73853,
\quad0.73723,
\quad0.73810,
\quad0.73795.
\]

Hence

\[
\boxed{
\min\Delta_{\rm ASD}^{\rm nonEinstein}=0.7372,
}
\]

while the `S^4` positive control stays below `8.3e-9`.

This is a separation of roughly eight orders of magnitude.

## What the two controls prove

The finite test distinguishes three logically different levels:

\[
\boxed{
\text{non-degenerate }B
\not\Rightarrow
\text{simple }B
\not\Rightarrow
\text{Einstein curvature}.
}
\]

More explicitly:

\[
\text{arbitrary triple }B^i
\xrightarrow{\rm Urbantke}
[g]
\]

is weaker than

\[
\Delta_{\rm simp}=0,
\]

and even a simple metric triple must additionally satisfy

\[
\boxed{\bar F(A_B)=0}
\]

for the vacuum Einstein sector.

This directly blocks a dangerous circular shortcut in the microscopic programme: no future binary model may claim `GR emerged` merely because a coarse `B` triplet reconstructs a smooth metric.

## Microscopic blocking target

For a frozen binary face/diamond ensemble, at each scale `b` measure in this order, without projection:

\[
X^{ij}(b)
=\frac14\epsilon B^i_b B^j_b,
\]

\[
\Delta_{\rm simp}(b),
\]

\[
g_U[B_b],
\]

\[
A_B(b):\quad D_{A_B}B_b\approx0,
\]

\[
F(A_B),
\]

and finally

\[
\boxed{
\Delta_{\rm ASD}(b)
=\frac{\|\bar F_b\|}{\|F_b\|+\|\bar F_b\|}.
}
\]

The candidate gravitational scaling window must satisfy simultaneously

\[
\boxed{
\Delta_{\rm simp}\to0,
\quad
\Delta_{D_AB}\to0,
\quad
\Delta_{\rm ASD}\to0,
}
\]

alongside the independently measured topology/diffusion dimension, `z -> 1`, two physical spin-2 modes, ghost decoupling and the already-developed nonlinear Ward tests.

A post-hoc projection of `B` onto the simple/self-dual sector is forbidden: the defects must decrease under the frozen dynamics/blocking itself.

## Scope

This is a Euclidean finite-difference validation of the proposed observable chain.  It does not yet establish:

- a microscopic binary rule producing the `B^i` triplet;
- four-dimensional geometrogenesis;
- Lorentzian reality conditions;
- quantum unitarity;
- matter;
- universality or experiment.

It does show that the previously vague arrow `binary information -> metric -> GR` can be replaced by a sequence of **independently falsifiable local defects**.

## Reproduction

```bash
python scripts/plebanski_connection_einstein_gate.py \
  --B-step 2e-5 \
  --A-step 2e-4 \
  --output verification_results/plebanski_connection_einstein_gate.json
```
