# Collective PL-S3 intrinsic FEM spectral-dimension precursor

Status: **static background precursor, not a collective-GR science row**.

This gate provides an independent metric check of the canonical barycentric PL-S3 carrier. It deliberately does **not** use graph-hop distance and it does **not** insert `D=3` into the estimator.

## Observable

On every tetrahedron we build the linear finite-element stiffness matrix

\[
K^{(T)}_{ij}=V_T\,\nabla\phi_i\cdot\nabla\phi_j
\]

from the intrinsic Gram matrix of the tetrahedron embedded in the regular 16-cell realization. With lumped vertex mass `M`, the positive symmetric Laplacian is

\[
L=M^{-1/2}KM^{-1/2}.
\]

The normalized heat return and spectral dimension are

\[
P(t)=\frac1N\operatorname{Tr}e^{-tL},\qquad
 d_s(t)=-2\frac{d\log P}{d\log t}.
\]

L0-L2 are diagonalized exactly. L3 has 40,256 vertices, so its trace is estimated with a deterministic 24-vector Rademacher/Hutchinson ensemble.

## Held-out L3 window

The L3 time window is not chosen after inspecting closeness to three. The exact L2 peak is transferred only by mesh `h^2` scaling,

\[
t_{3,\mathrm{pred}}=t_{2,\mathrm{peak}}(h_3/h_2)^2,
\]

and the fixed interval `[t_pred/4, 2 t_pred]` is scanned.

## Result

Peak sequence:

```text
L0  1.9085210169
L1  2.3877002596
L2  2.7553265235
L3  2.8529008753 +/- 0.0217976734   (24 probes)
```

The L3 peak occurs at `t = 0.00459436127` in the held-out window. Total intrinsic PL volume is conserved through refinement.

The trend is monotone and strongly supports dimensional growth toward a three-dimensional local regime, but the finest static central value has

\[
|d_s-3|=0.1470991247,
\]

so it does **not** pass the preregistered `0.10` collective killer tolerance. More importantly, even a static value inside that tolerance would still not populate `D_space_metric`: the killer requires the same observable on the dynamically enlarged `E/S/R` effective block states.

## Reproduce

```bash
python scripts/collective_fem_spectral_dimension_gate.py \
  --probes 24 \
  --output verification_results/COLLECTIVE_FEM_SPECTRAL_DIMENSION.json
```

Frozen reference: `verification_results/COLLECTIVE_FEM_SPECTRAL_DIMENSION.json`.
