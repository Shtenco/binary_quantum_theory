# Three-node graph-changing Peter-Weyl × route HDA result

## Frozen protocol

The gate `scripts/peter_weyl_three_node_graph_hda_gate.py` was committed with its pass/fail thresholds before the first frontier result. It uses three distinct K5 nodes, the existing regulator-safe Euclidean Peter-Weyl Hamiltonian, the independent square-root route-normal diffeomorphism target, nonconstant frozen lapse functions and no channel-dependent normalization.

The input is the all-\(j=1/2\), all-\(K=0\) K5 state at \(J_{max}=5/2\). Hamiltonian outputs are **not projected back** onto the original spin sector. States containing \(j=0\) links are retained and classified after cylindrical graph reduction.

The exact finite decomposition is

\[
[H[N],H[M]]
=
[R_N,R_M]+C_{cross}
+\sum_{i<j}(N_iM_j-N_jM_i)[H_i^E,H_j^E].
\]

## CI result

Canonical Linux `core-regression #414`: **PASS**.

Single-node supports:

```text
H0: 37
H1: 37
H2: 42
```

Pair commutators:

| pair | support | norm | j=0 graph-change norm² fraction | reduced colored-graph orbits |
|---|---:|---:|---:|---:|
| 0–1 | 510 | 1.6815599737359501 | 0.44403316352482564 | 26 |
| 0–2 | 648 | 1.548519756740384 | 0.5307882987594685 | 31 |
| 1–2 | 648 | 1.5485197561819104 | 0.5307882978924992 | 31 |

The union contains 31 reduced colored-graph orbits. The minimum route-metric eigenvalue on the one-hit support is 0.25.

## Regulator hierarchy

For

\[
\epsilon\in\left\{\frac14,\frac18,\frac1{16},\frac1{32},\frac1{64}\right\},
\]

the full normalized defect decreases as

```text
0.41151500410786523
0.2030722564609432
0.10110971522442395
0.050478393122679655
0.02522380789581472
```

Fitted powers are

```text
route-only       ~ epsilon^0.9999571195
cross / D        ~ epsilon^1.0024037289
geometry / D     ~ epsilon^2.0061524985
joint defect / D ~ epsilon^1.0064429344
```

At \(\epsilon=1/64\):

```text
route-only defect             = 8.264687442454126e-7
cross / D                     = 0.02522257996497328
pure geometry / D             = 0.00024888550067309685
joint defect / D              = 0.02522380789581472
geometry-channel graph-change = 0.5516528227917817
```

Thus the predicted hierarchy survives the move from two nodes to three while retaining cylindrical graph-change support.

## Claim boundary

This result justifies a separate machine gate `HDA_3NODE = tested_finite`.

It does **not** justify changing broad `HDA_MULTI` to `proved`. Still open are arbitrary graphs, multiple held-out habitats/states, the full Lorentzian Hamiltonian amplitudes on the same graph-changing domain and a theorem uniform in graph/refinement size.
