# Full signed geometry × operator-first route — logical selection theorem

Status: **exact projected selection statement + frozen finite coefficient regression; not the full off-shell HDA**.

Let `P` project onto the complete all-`j=1/2` Gauss sector. For four-valent all-`j=1/2` nodes this is exactly the logical intertwiner sector `K∈{0,2}`.

The frozen Peter-Weyl gate gives

\[
\boxed{P H_E^{sine} P=0}
\]

on all 32 logical columns.

The production route operator

\[
R_{op}[N]=\frac12\{N,\sqrt{\hat Q^{ab}\hat P_a\hat P_b}\}
\]

is built from flux scalar operators and route momenta. Flux operators act inside fixed SU(2) representation labels and do not change edge `j` labels. Therefore `R_op` preserves the fixed-spin sectors.

Since `H_E^sine P` has no component in the complete all-`j=1/2` sector, `R_op` cannot return its spin-changed output to `P`. Conversely `R_op P⊂P`, so applying `H_E^sine` afterwards again leaves the sector. Hence

\[
\boxed{P[H_E^{sine},R_{op}]P=0}.
\]

For `beta=hbar=1` the signed geometry operator is frozen upstream as

\[
G=-\frac23E_{raw}+\frac{32i}{9}L_{raw}.
\]

Therefore the projected full geometry-route cross obeys

\[
\boxed{P[G,R_{op}]P=P[H_{corr},R_{op}]P}.
\]

The latter coefficient is already frozen by the independent signed Lorentzian-route logical regression:

\[
\boxed{
P[G,R_{op}]P
\Rightarrow
-0.1907821681721X
-0.3304444078603Z
}
\]

for the full `beta=1` Lorentzian correction, with shape coefficient norm

\[
\boxed{0.3815643358315}.
\]

This is a strong regression for the future exact graph-changing two-node `G×R_op` collector. It does **not** imply that the full cross has no nonlogical channels; those channels and their regulator scaling remain part of the decisive HDA calculation.

Reproduction:

```bash
python scripts/logical_full_geometry_route_selection_gate.py \
  --output verification_results/LOGICAL_FULL_GEOMETRY_ROUTE_SELECTION.json
```
