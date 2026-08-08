# FLOOR A — Geometric block-spin

## What changed vs index-bin

Edges are assigned to coarse cells by **midpoint coordinates** on the unit 4-torus,
not by edge index.

\[
\mathrm{cell}(e) = \Big\lfloor \mathrm{mid}(e)/b \Big\rfloor \bmod L_c
\]

Axis-parallel edges reconstruct a diagonal metric proxy \(h_{\mu\mu}\) per cell.

## Results (L=3, b=1, Euclidean \(e^{-\beta S_{\mathrm{kin}}}\))

| quantity | value |
|---|---|
| coarse sites | 81 |
| unique cells hit | 81 |
| blocked scalar kinetic \(\alpha\) in \(G^{-1}\approx\alpha\mathrm{Lap}+m^2\) | \(>0\) |
| residual of fit | high (~0.94, small MC) |
| axis \(h_{\mu\mu}\) variance | \(O(10^{-5})\) |

## Floor status

| Floor | status |
|---|---|
| **A geometric block-spin** | **YES (structure)** |
| B S_eff → EH | NO |
| C Wilson coefficients | NO |
| D Lorentzian | NO |
| IR Einstein | NO |

## Next

More statistics / larger L; fit 2-derivative operators on blocked \(h_{\mu\nu}\) (Floor B).
