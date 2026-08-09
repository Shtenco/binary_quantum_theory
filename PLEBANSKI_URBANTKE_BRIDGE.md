# Plebanski/Urbantke bridge: coarse 2-forms -> metric geometry

Status: **exact finite algebraic control plus a new microscopic blocking gate; emergence from binary face/diamond variables is still open**.

## Why this changes the architecture

The previous gravity bridge reconstructed a metric perturbation from edge-length data on a pre-existing 4D Regge scaffold.  That route is useful after geometry already exists, but it cannot explain why a metric should be the correct coarse variable of a coordinate-free binary theory.

A connection-first route exists in four-dimensional GR.  The Plebański formulation uses a triple of self-dual two-forms rather than taking the metric as the fundamental field.  In the metric sector these forms satisfy the simplicity/metricity relation

\[
B^i\wedge B^j
\propto
\delta^{ij}\,\mathrm{vol}_4.
\]

A non-degenerate triple of two-forms also defines an Urbantke metric algebraically.  This makes local causal diamonds / plaquettes / 2-cells a much more natural candidate coarse carrier than the earlier slogan "one edge bit = one graviton".

The proposed bridge is therefore

\[
\boxed{
\text{binary face/diamond data}
\longrightarrow
B^i_{\mu\nu}
\xrightarrow{\Delta_{\rm simp}\to0}
\text{metric two-form sector}
\xrightarrow{\rm Urbantke}
g_{\mu\nu}.
}
\]

A microscopic qubit is **not** identified with a complete graviton or with the full curvature tensor.  A viable microscopic model must generate enough local/internal degrees of freedom that a coarse triplet `B^i` can be defined.

## Euclidean control convention

For a non-degenerate tetrad `e^I`, use the real Euclidean self-dual forms

\[
\Sigma^i
=
 e^0\wedge e^i
+\frac12\epsilon^i{}_{jk}e^j\wedge e^k.
\]

With the conventions of `scripts/plebanski_urbantke_gate.py`,

\[
\Sigma^i\wedge\Sigma^j
=
2\,\det(e)\,\delta^{ij}\,d^4x.
\]

Define the wedge matrix

\[
X^{ij}
=
\frac14
\epsilon^{\mu\nu\rho\sigma}
B^i_{\mu\nu}B^j_{\rho\sigma}.
\]

The dimensionless simplicity defect is

\[
\boxed{
\Delta_{\rm simp}
=
\frac{
\left\|X-\frac{{\rm Tr}X}{3}I\right\|_F
}{\|X\|_F}.
}
\]

The simple metric sector has `Delta_simp = 0`.

## Urbantke reconstruction

Define the cubic densitised tensor

\[
U_{\mu\nu}
=
\epsilon_{ijk}
\epsilon^{\alpha\beta\gamma\delta}
B^i_{\mu\alpha}
B^j_{\beta\gamma}
B^k_{\delta\nu}.
\]

For the self-dual tetrad forms above, direct contraction gives

\[
\boxed{
U_{\mu\nu}=12\,\det(e)\,g_{\mu\nu}
}
\]

up to the orientation/sign convention.  Thus the metric is reconstructed algebraically from the two-form triple; no edge length is used by the reconstruction.

## Numerical control

Eight independent random non-degenerate tetrads were tested.

The worst errors were

\[
\boxed{
\max\Delta_{\rm simp}=4.27\times10^{-16},
}
\]

\[
\boxed{
\max\epsilon_{U\sim g}=1.72\times10^{-15},
}
\]

and

\[
\boxed{
\max
\frac{\|U-12\det(e)g\|}{\|U\|}
=8.69\times10^{-16}.
}
\]

An independent internal `SO(3)` rotation of the triplet leaves both the simplicity defect and reconstructed conformal metric at machine zero, as it must.

## Crucial negative control: metric reconstruction is not enough

Take a volume-preserving anisotropic internal transformation

\[
B'^i=M^i{}_jB^j,
\qquad
M=e^{\alpha S},
\qquad
S=S^T,
\quad {\rm Tr}S=0.
\]

Then `det M = 1`.  The Urbantke cubic changes by `det M`, so its conformal metric is unchanged, but the wedge matrix is distorted and simplicity is lost.

Across eight random controls:

| distortion `alpha` | mean `Delta_simp` | minimum `Delta_simp` | max conformal metric error |
|--:|--:|--:|--:|
| 0.05 | 0.05766 | 0.05692 | 1.00e-15 |
| 0.10 | 0.11465 | 0.11174 | 1.07e-15 |
| 0.20 | 0.22364 | 0.21287 | 1.57e-15 |
| 0.40 | 0.40746 | 0.37481 | 9.91e-16 |
| 0.70 | 0.58573 | 0.52917 | 1.40e-15 |

Therefore

\[
\boxed{
\text{Urbantke metric exists}
\;\not\Rightarrow\;
\text{Plebański/GR metricity}.
}
\]

This is an important anti-circularity result.  A future binary model is not allowed to pass the geometry gate merely because three coarse two-forms produce some non-degenerate Urbantke tensor.

## Microscopic RG gate

For each block scale `b`, a frozen binary face/diamond rule must generate coarse observables `B^i_b` by a map fixed before the held-out run.  The following quantities are then measured without projection back onto the desired sector:

\[
\Delta_{\rm simp}(b),
\qquad
\kappa_X(b)=\operatorname{cond}X(b),
\qquad
\epsilon_{\rm loc}^{U}(b),
\qquad
\epsilon_{\rm block}^{U}(b).
\]

The intended limits are

\[
\boxed{
\Delta_{\rm simp}(b)\to0,
\qquad
\kappa_X(b)=O(1),
}
\]

while the reconstructed metric remains local and stable under alternative admissible blockings.

**Forbidden shortcut:** applying `X^{-1/2}` or another post-hoc whitening/projection to force `Delta_simp=0`.  Such an operation would insert the Plebański constraint by hand rather than derive it.

## Connection and Einstein gates after metricity

Metric reconstruction is only the first part of the connection-first bridge.  In the same scaling window one must next obtain a coarse connection `A^i` satisfying

\[
\boxed{
D_A B^i
=dB^i+\epsilon^{ijk}A^j\wedge B^k
\to0,
}
\]

and curvature

\[
F^i=dA^i+\frac12\epsilon^{ijk}A^j\wedge A^k.
\]

In the Plebański metric sector the Einstein condition can then be tested by decomposing `F^i` into the self-dual and anti-self-dual two-form bases and requiring the inappropriate anti-self-dual component to vanish (with the trace fixing the cosmological term).

This gives a coordinate-free research chain which can eventually join the already-tested Regge bridge:

\[
\boxed{
\text{binary 2-cell variables}
\to B^i
\to \Delta_{\rm simp}\to0
\to g_U
\to A_B
\to F(A_B)
\to \text{Einstein sector}
\to \text{Regge/FP/EH cross-checks}.
}
\]

## Relation to the dimension selector

The same architecture is compatible with `HODGE_DIMENSION_SELECTOR.md`: two-forms are special in four spacetime dimensions because the Hodge star maps the two-form sector back into itself.  This is only a **conditional selector** until a local duality is generated by the microscopic rules rather than imposed to obtain four dimensions.

## What remains open

The control in this file starts from continuum tetrads only to validate the algebraic gate.  It does **not** show that binary face/diamond variables generate:

- a non-degenerate triplet of coarse two-forms;
- Plebański simplicity without projection;
- Lorentzian reality conditions;
- a compatible connection;
- a four-dimensional manifold phase;
- the Einstein curvature equations;
- a quantum measure or matter.

Those are now explicit measurable obligations rather than an undefined `bit -> metric` arrow.

## Reproduction

```bash
python scripts/plebanski_urbantke_gate.py \
  --seeds 8 \
  --output verification_results/plebanski_urbantke_gate.json
```
