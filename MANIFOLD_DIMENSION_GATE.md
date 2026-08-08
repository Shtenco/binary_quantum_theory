# Local manifold-dimension gate

Status: **coordinate-free necessary topology test; ready for future frozen-rule output**.

## Purpose

A spectral dimension close to an integer is not enough to establish an emergent manifold.  Random and fractal graphs can display transient diffusion exponents that imitate integer dimensions over finite windows.

For an abstract simplicial complex there is a separate local criterion which uses no embedding coordinates: in a combinatorial `D`-manifold the link of an ordinary vertex is a `(D-1)`-sphere.

Thus a spatial `3`-manifold candidate must have

\[
\operatorname{link}(v)\sim S^2
\]

for almost all coarse vertices, while a full Euclideanized `4`-dimensional history complex must have

\[
\operatorname{link}(v)\sim S^3.
\]

## Implemented test

`scripts/manifold_dimension_gate.py` receives maximal simplices and, for each vertex:

1. constructs its abstract link;
2. builds all boundary matrices over `GF(2)`;
3. computes the link Betti numbers;
4. checks whether they match a homology sphere;
5. infers the local manifold dimension as one plus the sphere dimension.

For a homology sphere `S^m`, `m>=1`, the required pattern is

\[
b_0=b_m=1,
\qquad
b_k=0\quad(0<k<m).
\]

The reported `manifold_link_defect_fraction` is the fraction of vertices whose inferred local dimension differs from the dominant one or whose links fail the homology-sphere test.

This is a **necessary** local manifold test, not a complete PL-manifold recognition theorem.  Homology spheres can still contain nontrivial topology not detected by Betti numbers alone.

## Dimension-blind controls

The script constructs periodic Freudenthal triangulations only for self-test.  It is not told a target answer by the link analyzer.

| control complex | vertices | maximal simplices | inferred local dimension | defect fraction |
|:--|--:|--:|--:|--:|
| 2D periodic triangulation | 9 | 18 | 2 | 0 |
| 3D periodic triangulation | 27 | 162 | 3 | 0 |
| 4D periodic triangulation | 81 | 1944 | 4 | 0 |

Representative vertex-link homology is:

\[
D=2:\quad (b_0,b_1)=(1,1),
\]

\[
D=3:\quad (b_0,b_1,b_2)=(1,0,1),
\]

\[
D=4:\quad (b_0,b_1,b_2,b_3)=(1,0,0,1).
\]

## Required use on the microscopic theory

Once a frozen rule produces a coarse hypergraph/simplicial complex, the dimension claim should require **agreement of independent observables**, not one fitted exponent.

For a canonical spatial-slice interpretation:

\[
\boxed{
D_{\rm link}\to3,
\qquad
d_s^{\rm slice}\to3,
\qquad
z\to1,
\qquad
\Delta_{3+1}\to0.
}
\]

The Hodge-duality hypothesis in `HODGE_DIMENSION_SELECTOR.md` adds a third structural requirement: edge/frame and loop/curvature sectors should develop the appropriate local duality in the same scaling window.

For an interpretation in which the microscopic complex already contains the full causal history, target instead

\[
D_{\rm link}\to4,
\qquad
d_s^{\rm history}\to4,
\]

and do not add a second time direction.

## Strong falsifier

A rule is rejected as a manifold geometrogenesis mechanism if an apparent integer spectral plateau occurs while

\[
\boxed{
\liminf_{b\to\infty}
\text{manifold-link-defect}(b)>0.
}
\]

This specifically protects the project against confusing random-graph crossover behaviour with a genuine local continuum manifold.

## Reproduction

Self-test:

```bash
python scripts/manifold_dimension_gate.py
```

Frozen-rule output:

```bash
python scripts/manifold_dimension_gate.py \
  --input coarse_maximal_simplices.json \
  --output verification_results/manifold_dimension_gate.json
```

where the input JSON contains

```json
{"maximal_simplices": [[0,1,2,3], [0,1,3,4]]}
```

with no embedding coordinates required.
