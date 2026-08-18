# Logical shape -> metric Jacobian

Status: **exact local geometric map in the declared j=1/2 singlet carrier.**

For fixed face-spin norm `J_i^2=3/4` and closure, the two intrinsic logical shape coordinates `X,Z` determine the six pairwise face-flux inner products. Reconstructing the tetrahedral edge metric gives

```text
g(X,Z) = 2 sqrt(det G(X,Z)) G(X,Z)^-1.
```

At the regular tetrahedron branches

```text
(X,Z,Y) = (0,0,+1) and (0,0,-1)
```

the background metric is

```text
[[2,1,1],
 [1,2,1],
 [1,1,2]].
```

The exact derivatives with respect to `X` and `Z` form a rank-two metric Jacobian. They are trace-free with respect to the background metric, mutually orthogonal and have equal DeWitt/Frobenius norm:

```text
rank(J_metric) = 2
Tr(g0^-1 M_X) = 0
Tr(g0^-1 M_Z) = 0
Tr(g0^-1 M_A g0^-1 M_B) = (3/2) delta_AB.
```

The two orientation branches have the same intrinsic linear metric map. The metric determinant has no linear variation along either `X` or `Z` at the regular point.

This closes the local logical-shape -> intrinsic-metric dictionary without fitting a target metric. It does not by itself insert a momentum-space TT projector or an external experimental observable.

Reproduction:

```bash
python scripts/logical_shape_metric_jacobian_gate.py \
  --output verification_results/LOGICAL_SHAPE_METRIC_JACOBIAN.json
```
