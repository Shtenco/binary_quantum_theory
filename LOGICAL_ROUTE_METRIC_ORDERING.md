# Logical route metric: orientation parity and ordering dependence

Status: **exact logical flux-metric decomposition + tested finite ordering control; full operator-valued route HDA remains open**.

The route-normal generator uses the geometry-dependent flux Gram metric. On the all-`j=1/2` four-valent singlet geometry qubit, that metric has an exact logical decomposition.

This note separates what the currently frozen expectation-first route gate actually proves from what a more operator-valued ordering may do.

---

## 1. Exact logical flux scalar

For the selected local legs used by the route control,

```text
J_0 . J_2
 = -1/4 I
   - sqrt(3)/4 X
   + 1/4 Z.
```

Numerically the direct Peter-Weyl intertwiner projection gives

```text
[
  [ 0,                -0.4330127018922193],
  [-0.4330127018922193, -0.5]
]
```

with exact-formula error at roundoff scale.

The diagonal Casimirs are

```text
J_0^2 = J_2^2 = 3/4 I.
```

The key symmetry fact is immediate:

```text
flux metric logical content = I, X, Z
orientation coordinate       = Y.
```

Therefore the route flux metric is even under the logical orientation reflection

```text
Y -> -Y.
```

It cannot by itself distinguish the two signs of the oriented-volume coordinate at the linear logical-operator level.

---

## 2. Linear isotropic angular average

For a two-leg route direction

```text
p=(cos theta, sin theta)
```

form the logical quadratic metric contraction `Q(p)`.

A uniform angular average removes the `X/Z` shape-plane components of the **linear** contraction:

```text
< Q(p) >_theta ~= 0.75 I.
```

The residual `X,Y,Z` coefficients are at floating-point roundoff.

Thus ordinary isotropic route averaging restores a scalar linear metric response.

---

## 3. Frozen expectation-first ordering

The currently used finite route logic first evaluates the geometry expectation value and then takes the positive square root:

```text
omega_K(theta)
 = sqrt( <K|Q(p)|K> ).
```

After isotropic angular averaging the two logical basis states give

```text
<omega>_{K=0}
 = 0.8598466001022401

<omega>_{K=2}
 = 0.8598466001022401.
```

Hence the tested frozen expectation-first route control does **not** produce a diagonal `K=0/K=2` shape anisotropy in this averaged setting.

This corrects any stronger statement that the already frozen route gate itself had established a logical pseudospin split.

---

## 4. Operator-first square-root ordering

A different quantization order first treats `Q(p)` as a positive logical operator, applies its spectral square root, and only then performs the angular average:

```text
< sqrt_operator(Q(p)) >_theta.
```

The finite control gives approximately

```text
0.8197716816 I
-0.0347058975 X
+0.0200374593 Z
```

with `Y` at numerical zero.

The surviving shape-plane norm is

```text
sqrt(X^2+Z^2)
 = 0.04007491854520556.
```

Therefore

```text
linear averaging       -> isotropic
expectation-first sqrt -> K=0/K=2 equality in the tested control
operator-first sqrt    -> finite X/Z logical anisotropy.
```

The difference is a genuine noncommutativity/ordering effect of the nonlinear square root.

---

## 5. What is protected and what is not

Both orderings agree on the exact orientation-parity statement:

```text
Y coefficient = 0.
```

Thus the route flux metric is insensitive to the sign of the oriented-volume coordinate at this level.

But full pseudospin `SU(2)` is not kinematically protected because the metric naturally lives in the `X/Z` shape plane.

Whether that shape information survives into the **quantized route constraint** depends on the chosen operator ordering and the HDA closure of that ordering.

---

## 6. Relation to the Peter-Weyl anisotropy result

The Euclidean Peter-Weyl return kernel independently shows a strong environment-unbiased orientation-vs-shape split while suppressing the same `Y`-odd linear channels.

The route result should therefore be read carefully:

- it does **not** rescue exact pseudospin `SU(2)`;
- it also does **not** prove an extra route anisotropy in the already frozen expectation-first averaged gate;
- it identifies operator ordering as an additional place where `X/Z` shape anisotropy can enter a more fully quantized route construction.

---

## 7. Next route gate

The legitimate next construction is an operator-valued route/HDA gate in which

```text
Q_hat -> chosen positive sqrt / densitized alternative
```

is fixed before the commutator test.

The criterion is not merely spectral positivity. The chosen ordering must also retain the correct route-normal HDA limit and preserve the tested orientation-parity selection rule.

Until that is done, the operator-first `0.0400749185` shape norm is an ordering diagnostic, not a new term in the canonical Hamiltonian.

---

## Reproduction

```bash
python scripts/logical_route_metric_operator_gate.py \
  --output verification_results/LOGICAL_ROUTE_METRIC_OPERATOR.json
```
