# First-refinement S4 metric-sector compression

Status: **reanalysis of already-certified exact CI amplitudes; finite Euclidean tangent result, not yet the physical TT Hessian**.

Source evidence is the successful `collective-l1-e-q4-rank` workflow run

```text
run = 31965359681
head = 919f64856c2e2b232c94ffbd48593f1c4d0c2d6b
```

which computed all 24 exact q4-projected Euclidean amplitude columns on the first barycentric refinement of one parent tetrahedron. No Peter–Weyl amplitudes are recomputed here.

## 1. Why 24 columns have an exact S4 meaning

The 24 fine tetrahedral chambers inside one barycentrically subdivided parent tetrahedron are indexed by the 24 permutations of its four vertices. They therefore carry the regular representation of `S4`.

Reconstructing the complex Gram matrix directly from the saved sparse CI amplitudes gives

```text
Hermiticity defect = 0
max relative [G,L_g] defect over all g in S4 = 6.9e-16
```

so the finite dynamics respects the left regular tetrahedral action to machine precision.

The regular-representation spectrum splits exactly into the expected multiplicities. In the repository convention, where the ordinary tetrahedral vector/edge triplet is called `T2`, the Gram eigenvalues are

```text
A1 : 0.8436999771224868
A2 : 1.8553221449315234

E  : 1.0655274365167005 x2
     1.6334946855373118 x2

T2 : 0.9180477151760883 x3
     1.1157093789153100 x3
     1.5089650050405063 x3

T1 : 1.1900571170295533 x3
     1.5833127431468714 x3
     1.7809744068091118 x3
```

The multiple copies inside the full regular representation are not yet a unique metric carrier. The next step removes that multiplicity without a fit.

## 2. Canonical 24 -> 6 parent-edge map

The parent tetrahedron has six unordered edges. For an edge `{a,b}`, collect the four barycentric chambers whose first two permutation entries are exactly `{a,b}` and define the normalized coarse-edge vector as their equal sum with coefficient

\[
\frac1{\sqrt4}=\frac12.
\]

This produces an isometric, `S4`-equivariant map

\[
24\longrightarrow 6.
\]

The six-edge representation has the exact decomposition

\[
\boxed{6=A_1\oplus E\oplus T_2.}
\]

This is the same intrinsic metric representation used by the existing metric-photon bridge.

## 3. Actual compressed Euclidean tangent kernel

The compressed six-edge Gram has exactly the orbit form

\[
K_6=aI+bA_{adj}+cO_{opp}
\]

with

\[
\boxed{a=1.022027850746478},
\]

\[
\boxed{b=-0.0445819684059977},
\]

\[
\boxed{c=0}
\]

up to machine precision. Here `A_adj` connects tetrahedral edges sharing one endpoint, while `O_opp` connects opposite edges.

Therefore

\[
\lambda_{A_1}=a+4b+c
=0.843699977122487,
\]

\[
\boxed{\lambda_E=a-2b+c=1.111191787558474},
\]

\[
\boxed{\lambda_{T_2}=a-c=1.022027850746478}.
\]

The symmetry-resolved traceless-metric split is

\[
\boxed{\Delta_{ET}=\lambda_E-\lambda_{T_2}=0.0891639368119954}.
\]

Normalized to the mean of the two traceless sectors,

\[
\boxed{
\frac{\Delta_{ET}}{(\lambda_E+\lambda_{T_2})/2}
=0.08359564595
}
\]

or about `8.36%` at this first-refinement Euclidean tangent level.

## 4. Why this is more relevant than the old logical orientation split

For the intrinsic six-edge metric representation, restoration of continuum rotational symmetry requires the five traceless metric components to become degenerate. Under tetrahedral symmetry those five components split as

\[
5\to E\oplus T_2.
\]

Hence

\[
\boxed{\Delta_{ET}\to0}
\]

is a direct internal diagnostic of rotational restoration in the metric sector.

This is conceptually closer to the future cubic dispersion coefficient `zeta4` than the logical orientation-vs-shape quantity `R_aniso`, because `E` and `T2` are both intrinsic metric sectors whereas the logical `Y` direction is an orientation pseudoscalar.

## 5. Critical interpretation boundary

The present `K6` is the Gram matrix of first-order Euclidean tangent states,

\[
(K_6)_{ef}=\langle u_e|u_f\rangle.
\]

It is **not yet proved identical** to the quadratic effective-action Hessian that determines the physical TT pole. Therefore

\[
\boxed{\Delta_{ET}=0.08916\ldots\ \text{is not }\zeta_4.}
\]

Calling it `zeta4` now would be an unjustified identification.

The remaining dynamical bridge is sharply defined:

```text
same six-edge metric carrier
 -> depth-two / effective response C_6x6(omega,k)
 -> S4 orbit values {same, adjacent, opposite}
 -> lambda_E(omega,k), lambda_T2(omega,k)
 -> TT projection
 -> eta2_iso(b), zeta4_cub(b).
```

Because `S4` reduces every six-edge invariant kernel to three orbit numbers, the next calculation no longer requires a generic matrix fit.

## Reproduction

```bash
python scripts/collective_l1_q4_s4_metric_compression.py \
  --input-dir verification_results/l1_q4_columns \
  --output verification_results/L1_Q4_S4_METRIC_COMPRESSION.json
```

The accompanying workflow downloads the immutable source artifacts from run `31965359681` and performs only this symmetry reanalysis.
