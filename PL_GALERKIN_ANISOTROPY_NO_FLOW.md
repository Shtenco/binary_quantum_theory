# Recursive PL Galerkin no-flow certificate for the logical anisotropy

Status: **exact factorization + tested finite recursive-PL control; this is a no-go for geometry-only RG, not the physical quantum RG**.

The completed higher-shell S4 seed is

\[
K_{S4}
=c_0 II+J_{shape}(XX+ZZ)+J_{orient}YY
\]

with

```text
c0       = 12.860443113390883
J_shape  = -0.3629900150598623
J_orient = +0.7912767588958898
R_aniso  = (J_orient-J_shape)/c0
         = 0.0897532661805313
```

The immediate question was whether the already-established recursive PL smoothing could itself drive this number toward zero.

## 1. Canonical geometry-only Galerkin control

Use exactly the spatial recursion of `bcqg_global_manifold_gate.py`:

```text
16-cell boundary
 -> global barycentric subdivision
 -> global barycentric subdivision.
```

Let `L_g` be the combinatorial Laplacian of the tetrahedron dual graph at generation `g`.

Every parent tetrahedron has exactly

\[
4!=24
\]

barycentric top-dimensional children. Define the normalized block-constant prolongation

\[
P_{cC}=\begin{cases}
1/\sqrt{24}, & c\subset C,\\
0,&\text{otherwise}.
\end{cases}
\]

The actual recursive complexes give

```text
g=0: 16 tetrahedra
g=1: 384 tetrahedra
g=2: 9216 tetrahedra
```

and every coarse dual edge is crossed by exactly six fine dual edges.

Consequently the checked identity is

\[
\boxed{P^T L_{g+1}P=\frac14 L_g}.
\]

For both `0 -> 1` and `1 -> 2` the relative matrix residual is approximately

```text
2.22e-16.
```

The factor has a simple combinatorial origin:

\[
\frac{6\ \text{crossing child edges}}{24\ \text{block normalization}}=\frac14.
\]

## 2. Internal-coupling factorization

Suppose spatial blocking is geometry-only and separable from the internal S4 channel:

\[
K_{fine}=L_{g+1}\otimes J_{int},
\qquad
\mathcal P=P\otimes I_{int}.
\]

Then identically

\[
\mathcal P^T K_{fine}\mathcal P
=(P^TL_{g+1}P)\otimes J_{int}
=\frac14L_g\otimes J_{int}.
\]

Thus every internal coefficient is multiplied by the same factor:

```text
c0       -> c0/4
J_shape  -> J_shape/4
J_orient -> J_orient/4
```

and therefore

\[
\boxed{R_{aniso}'=R_{aniso}.}
\]

For the current seed the first projected values are

```text
c0/4       = 3.2151107783477206
J_shape/4  = -0.09074750376496557
J_orient/4 = +0.19781918972397244
R_aniso'   = 0.0897532661805313
```

with zero floating-point change at the reported precision.

## 3. Scientific consequence

This rules out a tempting but incorrect shortcut:

```text
PL refinement / geometric smoothing alone
 -> R_aniso -> 0
```

is **not** obtained in the canonical separable Galerkin control.

A nontrivial beta function for `R_aniso` requires a genuinely internal/non-separable operation, for example:

```text
Peter-Weyl representation growth
+ SU(2) recoupling inside a coarse block
+ projection to the renormalized logical geometry sector
+ recomputation of the higher-shell/resolvent operator.
```

In particular, the already-existing `collective_volume_rg_gate.py` independently identifies `j=1` as the first equal-spin four-valent intertwiner space with nontrivial absolute-volume spectrum. This makes the representation step

\[
\boxed{j=1/2\to j=1}
\]

the next honest internal RG target.

## 4. What this does not prove

The result does **not** show that `R_aniso` survives in the infrared. It only proves that the canonical geometry-only linear blocking has zero beta function for this internal ratio.

The physical RG may still produce

```text
R_aniso -> 0
R_aniso -> nonzero fixed point
or no stable fixed point,
```

but only after the internal Peter-Weyl degrees of freedom are actually coarse-grained.

## Reproduction

```bash
python scripts/pl_galerkin_anisotropy_no_flow_gate.py \
  --refinements 2 \
  --output verification_results/PL_GALERKIN_ANISOTROPY_NO_FLOW.json
```
