# Microscopic mirror order from the 16-cell geometry qubits

Status: **exact finite 16-cell combinatorics + sparse 16-qubit ordered-phase control + recursive PL persistence; force normalization still open**.

The continuum mirror-force construction introduced a coarse pseudoscalar `sigma`. This note derives a natural candidate for that order parameter directly from the already frozen 16-cell / geometry-qubit structure and checks that the staggered order survives the actual recursive PL branch used by the global-manifold gate.

---

## 1. The 16 tetrahedra form a four-bit dual hypercube

The minimal flag globalization has four antipodal vertex pairs. A tetrahedron is obtained by choosing one vertex from each pair.

Therefore every tetrahedron can be labelled by a four-bit string

```text
b = b1 b2 b3 b4.
```

There are

```text
2^4 = 16
```

such tetrahedra.

Two tetrahedra share a triangular face exactly when they differ in one of the four choices, i.e. when their labels have Hamming distance one.

Hence the dual adjacency graph is exactly

```text
Q4 = four-dimensional hypercube.
```

It has

```text
16 vertices
32 edges
degree 4 at every vertex.
```

`Q4` is bipartite.

---

## 2. Why neighboring oriented volumes have opposite signs

The logical geometry qubit has an oriented coordinate

```text
Q_v = (sqrt(3)/4) Y_v.
```

Across a correctly glued common face, the outward orientation reverses. The existing Bell-gluing structure correspondingly favors

```text
Y_v Y_w = -1
```

on neighboring tetrahedra.

At first sight that seems to prevent a uniform macroscopic orientation order.

The dual hypercube solves the problem.

Define the bipartite sign

```text
eta_v = (-1)^popcount(v).
```

Every dual edge connects opposite parity, so

```text
eta_v eta_w = -1.
```

Now define the **staggered orientation variable**

```text
sigma_v = eta_v Y_v.
```

Then the correct geometric gluing condition becomes

```text
Y_v Y_w = -1
```

if and only if

```text
sigma_v sigma_w = +1.
```

Thus the alternating local orientation required by geometry is equivalent to **ferromagnetic uniform order** in the staggered variable.

---

## 3. Exact global mirror bit

Define the block order parameter

```text
Sigma = (1/16) sum_v eta_v Y_v.
```

There are two exact classical gluing vacua:

```text
Y_v = +eta_v  -> Sigma = +1
Y_v = -eta_v  -> Sigma = -1.
```

Both satisfy

```text
Y_v Y_w = -1
```

on all 32 dual edges and have the same gluing energy.

Mirror conjugation flips every `Y_v`, therefore

```text
Sigma -> -Sigma.
```

This is the desired microscopic-to-coarse bridge:

```text
local oriented geometry qubits
 -> staggered block order
 -> one global mirror bit Sigma=+/-1.
```

The sign is not the arbitrary alternating sign of neighboring tetrahedron frames; the staggered factor `eta_v` divides that conventional alternation out.

---

## 4. Exact defect energies

Take the orientation part of the gluing energy as

```text
H_Y = J sum_<vw> Y_v Y_w,
J > 0.
```

The two perfect mirror vacua have

```text
E0 = -32 J.
```

### One local orientation error

Each tetrahedron has four dual neighbors. Flipping one `Y_v` changes four bonds from `-J` to `+J`.

Each bond costs `2J`, so

```text
Delta E_single = 4 * 2J = 8J.
```

The finite gate reproduces exactly

```text
single flip cost = 8J.
```

### A mirror domain wall

Flip the mirror sector on one half of the hypercube, for example all labels with `b1=1`.

The cut contains eight dual edges. Each becomes frustrated, therefore

```text
Delta E_wall = 8 * 2J = 16J.
```

The gate finds exactly eight frustrated bonds and cost `16J`.

So the mirror order has a real finite energetic stiffness.

---

## 5. Quantum dynamics: staggered transverse-field Ising model

To test whether the two mirror sectors survive quantum fluctuations, use the staggered variable and write

```text
H = -J sum_<vw> sigma_v sigma_w
    -h sum_v X_v.
```

This is the ordinary ferromagnetic transverse-field Ising Hamiltonian on `Q4`, unitarily equivalent to the alternating `Y` orientation problem.

The full Hilbert dimension is

```text
2^16 = 65536.
```

The executable gate diagonalizes the lowest three levels with sparse Lanczos.

At

```text
h/J = 0.2
```

it obtains approximately

```text
E0/J = -32.0800166771
E1/J = -32.0800166771
E2/J = -24.1099288002
```

with

```text
mirror-doublet splitting < 1e-12 J
gap to next level          = 7.97008787696 J
<Sigma^2>                  = 0.99765394737
<|Sigma|>                  = 0.99874782526.
```

Thus the low-energy sector is overwhelmingly concentrated near the two classical mirror orientations.

Because the cluster is finite, the exact quantum eigenstates need not individually choose `Sigma=+1` or `-1`; tunnelling produces even/odd superpositions. The nearly degenerate doublet is precisely the finite-size precursor of spontaneous `Z2` mirror-order breaking.

---

## 6. Ordered-to-disordered crossover control

The gate scans

```text
h/J = 0.2, 0.5, 1, 2, 3, 4.
```

The order measure decreases monotonically in the control:

| `h/J` | `<Sigma^2>` |
|---:|---:|
| 0.2 | 0.9976539474 |
| 0.5 | 0.9852611313 |
| 1.0 | 0.9399276867 |
| 2.0 | 0.7354521879 |
| 3.0 | 0.2938840311 |
| 4.0 | 0.1462741385 |

So the ordered mirror doublet is not an artifact of the observable definition: increasing quantum-flip strength destroys the order as expected.

---

## 7. The continuum sigma field is no longer purely postulated

The previous continuum construction used a pseudoscalar order parameter `sigma(x)` with two mirror vacua.

This finite result supplies its microscopic candidate:

```text
sigma(x)
 ~ block average of eta_v Y_v.
```

In other words,

```text
Y_L/Q
 -> staggered 16-cell order parameter Sigma
 -> coarse pseudoscalar sigma(x).
```

The soft collective fluctuations of this order parameter can themselves act as a candidate mediator mode. Therefore the auxiliary `phi` field of the conservative two-field continuum model need not necessarily be fundamental; a minimal future branch can test whether the coarse `sigma` fluctuation supplies the same Yukawa channel by itself.

---

## 8. What the seed calculation does and does not derive

### Derived / finite

- the 16-cell dual tetrahedron graph is `Q4`;
- its bipartite parity exactly removes the alternating face-orientation convention;
- the block variable `Sigma=(1/16)sum eta_v Y_v` has two exact mirror vacua `+/-1`;
- the local orientation defect costs `8J`;
- a half-hypercube domain wall costs `16J`;
- the full 16-qubit quantum Hamiltonian has a strongly ordered low-energy mirror doublet at small `h/J`;
- the order disappears as transverse fluctuations are increased.

### Still not derived

- the physical value of `J` in joules;
- the continuum kinetic normalization of `sigma`;
- the mediator mass/range in SI units;
- the coupling of `Sigma/sigma` to ordinary rest mass or another matter charge;
- therefore the dimensionless force ratio `alpha`;
- the enlarged microscopic Peter-Weyl x route x mirror HDA.

---

## 9. Recursive PL persistence: the mirror order survives refinement

The seed result would be much weaker if bipartiteness disappeared as soon as the manifold were refined. Therefore `scripts/mirror_order_recursive_pl_gate.py` applies **the same global barycentric subdivision** used by `bcqg_global_manifold_gate.py`, constructs the tetrahedron dual graph at every checked generation, and solves its two-colouring problem independently.

The result is:

| generation | tetrahedra | dual edges | degree | bipartite |
|---:|---:|---:|---:|:---:|
| 0 | 16 | 32 | 4 | yes |
| 1 | 384 | 768 | 4 | yes |
| 2 | 9216 | 18432 | 4 | yes |

For every checked generation there exists `eta_t=+/-1` such that

```text
eta_t eta_u = -1
```

on every shared-face dual edge. Therefore

```text
sigma_t = eta_t Y_t
```

again converts the geometric orientation rule

```text
Y_t Y_u = -1
```

into uniform order

```text
sigma_t sigma_u = +1.
```

Both exact global mirror branches survive:

```text
Sigma_g = (1/T_g) sum_t eta_t Y_t = +1
```

or

```text
Sigma_g = -1.
```

Thus the staggered mirror variable is not a special accident of the 16-cell seed. It persists through the checked recursive PL `S3` family that the candidate theory already uses for its continuum route.

### Low-mode diagnostic

The gate also records the first combinatorial dual-Laplacian eigenvalue:

```text
g=0: lambda_2 = 2.0000000000
g=1: lambda_2 = 0.152240935...
g=2: lambda_2 = 0.011719063...
```

The decreasing low mode is the expected qualitative signal of growing long-wavelength structure under refinement. It is **not yet converted into a physical mass or `Z_sigma`**, because that requires a physical dual-edge length/volume normalization and the time-kinetic normalization of the collective mode.

This makes the remaining bottleneck narrower:

```text
mirror order survives recursive PL refinement
 -> derive physical length/time normalization
 -> Z_sigma
 -> matter coupling beta_m
 -> alpha.
```

---

## 10. Current bottleneck

The question

```text
where could sigma come from?
```

is now finite-tested both at the seed and through two recursive PL refinements.

The remaining question is

```text
what is the physical normalization and matter coupling of the derived Sigma mode?
```

That is the quantity needed to predict `alpha` rather than postulate it.

---

## Reproduction

Seed quantum-order gate:

```bash
python scripts/mirror_order_16cell_gate.py \
  --output verification_results/MIRROR_ORDER_16CELL.json
```

Recursive PL persistence gate:

```bash
python scripts/mirror_order_recursive_pl_gate.py \
  --refinements 2 \
  --output verification_results/MIRROR_ORDER_RECURSIVE_PL.json
```
