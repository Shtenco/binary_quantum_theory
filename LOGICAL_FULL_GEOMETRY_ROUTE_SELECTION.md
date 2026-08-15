# Full signed two-node geometry × operator-first route — logical selection theorem

Status: **exact projected selection statement + finite 4×4 shared-route regression; not the full off-shell HDA**.

This file corrects one important scope error in the earlier one-node logical regression: the coefficient of the one-node 2×2 route average must **not** be transplanted into the two-node shared operator

\[
\Omega_{shared}=\sqrt{\tfrac12(Q_0+Q_1)^{ab}P_aP_b},
\]

because the spectral square root is nonlinear.

---

## 1. Exact Euclidean selection

Let `P` project onto the complete all-`j=1/2` Gauss sector. For four-valent all-`j=1/2` nodes this is the full logical intertwiner sector `K∈{0,2}`.

The executable gate independently re-runs the physical-sine first-order test on all 32 logical columns and verifies

\[
\boxed{P(H_{E,0}^{sine}+H_{E,1}^{sine})P=0}.
\]

The production route operator

\[
R_{op}[N]=\frac12\{N,\sqrt{\hat Q^{ab}\hat P_a\hat P_b}\}
\]

is built from flux scalars and route momenta and therefore preserves edge SU(2) representation labels `j`. Hence

\[
\boxed{P[H_{E,0}^{sine}+H_{E,1}^{sine},R_{op}]P=0}.
\]

Thus the projected two-node geometry-route cross is purely Lorentzian.

---

## 2. Exact 4×4 shared route block

Use the same local route legs `(1,2)` as the physical sine two-node habitat. On basis

```text
(K0,K1)=(0,0),(0,2),(2,0),(2,2)
```

the exact shared geometry metric is

\[
Q_{shared}^{ab}=\frac12(Q_0^{ab}\otimes I+I\otimes Q_1^{ab}).
\]

The angularly averaged positive spectral square root has nonzero Pauli content not only in `XI/ZI` and `IX/IZ`, but also in correlation channels `XX/XZ/ZX/ZZ`.

This is the key nonlinear effect missed by a naive one-node embedding.

---

## 3. Signed beta=1 local Lorentzian coefficient

The upstream CI-verified normalization gives, at `beta=hbar=1`,

\[
H_{corr,node}^{log}=gY_{node},
\qquad
\boxed{g=-4.760637696520545}.
\]

Define

\[
C_0=-i[gY_0,\bar\Omega_{shared}],
\qquad
C_1=-i[gY_1,\bar\Omega_{shared}].
\]

At `n_theta=32768`, the node-0 cross is approximately

\[
\boxed{
\begin{aligned}
C_0\simeq{}&-0.09539104\,XI
-0.16522213\,ZI\\
&-0.08261107\,XX
+0.04769552\,XZ\\
&-0.14308656\,ZX
+0.08261107\,ZZ.
\end{aligned}}
\]

The node-1 result is the exact node swap of `C0` up to numerical angular-integration precision.

---

## 4. Local and entangling norms

For `C0`, the local shape contribution

\[
\sqrt{c_{XI}^2+c_{ZI}^2}
\]

and the entangling contribution

\[
\sqrt{c_{XX}^2+c_{XZ}^2+c_{ZX}^2+c_{ZZ}^2}
\]

are both approximately

\[
\boxed{0.19078208},
\]

with equality at the numerical integration precision used by the gate.

The full Frobenius norm is approximately

\[
\boxed{0.53961322}.
\]

Thus the two-node operator-first square root generates an entangling geometry-route cross of the **same coefficient norm** as the local part in this symmetric logical control.

This is a materially stronger and more informative result than the old one-node 2×2 diagnostic.

---

## 5. Why the old coefficient cannot be copied

The previous one-node signed full-correction regression was

\[
-0.1907821682X-0.3304444079Z.
\]

Embedding that naively as a node-0 4×4 operator and comparing with the true shared-route `C0` gives relative mismatch approximately

\[
\boxed{1.0}.
\]

So the old coefficient is **not wrong**; its scope was one-node. The error was only attempting to reuse it as the two-node shared coefficient.

The current 4×4 cross replaces that naive transplant for all future two-node `G×R_op` regressions.

---

## 6. What is exact and what remains open

Exact / executable:

- 32-column physical-sine first-order projection zero;
- route preservation of edge representation labels;
- therefore `P[H_E^sine,R_op]P=0`;
- node-swap covariance of the two-node logical Lorentzian-route cross.

Finite regression:

- the angularly averaged 4×4 coefficients above.

Still open:

- nonlogical spin-changing `G×R_op` channels;
- regulator scaling of the full cross;
- exact full `EE+EL+LE+LL+G×R+R×G+RR` HDA.

---

## Reproduction

```bash
python scripts/two_node_lorentzian_route_logical_cross_gate.py \
  --n-theta 32768 \
  --output verification_results/TWO_NODE_LORENTZIAN_ROUTE_LOGICAL_CROSS.json

python scripts/logical_full_geometry_route_selection_gate.py \
  --n-theta 32768 \
  --output verification_results/LOGICAL_FULL_GEOMETRY_ROUTE_SELECTION.json
```
