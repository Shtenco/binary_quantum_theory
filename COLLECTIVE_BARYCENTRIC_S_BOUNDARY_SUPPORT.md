# Collective barycentric one-S boundary support

Status: **exact conservative representation-support theorem for one production Lorentzian action**.

For the canonical first spatial block (24 fine tetrahedra, 24 boundary dual links, six boundary links on each coarse face), enumerate the nested raw Lorentzian support

\[
C_i(K)C_j(K)C_k(V),\qquad K\sim[V,E],
\]

on the full L1 barycentric subdivision of the 16-cell. The physical Hermitian block

\[
S=-\frac{i}{2}(L_{raw}-L_{raw}^\dagger)
\]

has the same fundamental-holonomy hit support, so dagger does not enlarge the wall.

For every one of the 16 coarse tetrahedral blocks the exhaustive census contains `82,944` support profiles. All 16 blocks are identical. The maximum number of fundamental hits is six on one coarse face and six on one fine boundary link.

Starting from six fine `j=1/2` links per coarse face and applying exact SU(2) coupling reachability gives

\[
\boxed{j_{face}=0,\tfrac12,1,\tfrac32,2,\tfrac52,3,\tfrac72,4,\tfrac92,5,\tfrac{11}{2},6}.
\]

Thus one `S` action expands the earlier exact one-`E` support `j<=4` to `j<=6`. Because the operator-first route block preserves spin labels, the complete **one-step** production `G+R` carrier has the same conservative face wall `j<=6` before amplitude pruning.

Exact boundary-hit pattern census per block:

```text
()       1296
(1,1)    1728
(1,3)    9216
(1,5)   12096
(2,)     9936
(2,2)     576
(2,4)    1728
(4,)    25200
(6,)    21168
```

This is support reachability, not a statement that all sectors have nonzero final amplitudes. Sectors may be removed only after explicit amplitude computation demonstrates cancellation; they may not be deleted before GR comparison. Repeated collective actions require a separately frozen closure depth or leakage-controlled compression.

Reproduce:

```bash
python scripts/collective_barycentric_S_boundary_support_gate.py \
  --output verification_results/COLLECTIVE_BARYCENTRIC_S_BOUNDARY_SUPPORT.json
```
