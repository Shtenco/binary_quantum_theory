# Collective effective-constraint producer — implementation contract

This file specifies the computation needed to turn the preregistered collective GR killer from `INCOMPLETE` into a real PASS/FAIL experiment inside the theory.

## Blocking geometry

Use the canonical PL-S3 barycentric refinement family. At level `l`, blocks are fixed from the simplicial refinement combinatorics, not chosen after inspecting GR targets.

The minimal two-carrier map `spin-1/2 x spin-1/2 -> j=1` is retained as an exact representation-fusion control. It is **not** the first canonical spatial block.

For one barycentrically subdivided coarse tetrahedron the exact first spatial block has:

```text
24 fine tetrahedra / dual nodes
36 internal dual links
24 boundary dual links
6 fine boundary links on each of 4 coarse faces
```

Thus its maximal symmetric boundary channel is

\[
(\tfrac12)^{\otimes 6}_{sym}\to j=3
\]

on each coarse face. The direct tensor-network gate shows that the static all-`j=1/2`, maximal-symmetric `j=3` block has only a rank-one image in the seven-dimensional four-`j=3` coarse singlet space. Consequently **that static sector is only a background candidate, not the collective tangent space**.

The production collective block space must therefore be enlarged by a target-independent support rule to include at least the boundary/internal spin sectors reached by the frozen microscopic `E=H_E^sine`, Hermitian Lorentzian `S`, and spin-preserving route operator. Non-maximal face irreps may not be discarded merely because the maximal symmetric sector is simpler.

## Operator-first compression

For every Gauss/diffeomorphism/Hamiltonian generator `C_A`, compute

\[
C_A^{eff}=W_l^\dagger C_A W_l
\]

and the leakage

\[
\eta_A=\|(1-W_lW_l^\dagger)C_AW_l\|.
\]

Do not replace an operator by an expectation value before the constraint algebra is built.

If direct projection leakage is not small, a Feshbach/Schrieffer-Wolff correction may be evaluated only under a prescription frozen before the science result is inspected. Both raw projection and corrected result must be reported.

## Effective metric and D_space

Construct the collective flux Gram matrix and a nondegenerate metric from the retained block space. Distances must be derived from that collective metric (or a demonstrated equivalent dual metric), not from bare simplex-count graph distance. Measure ball volumes over an automatically defined pre-saturation window and report the full `(r,V(r))` data used for the dimension estimate.

Topological PL dimension 3 is a prerequisite, not a substitute for this metric observable.

## Effective DeWitt kinetic tensor

Choose a declared homogeneous/nondegenerate background from the direct block spectrum. Perturb the six independent metric momenta in the orthonormal `sym6` basis and evaluate the Hessian of the effective scalar constraint. Store the raw `6x6` Hessian. The killer gate, not the producer, extracts `c_eff`.

The background/tangent basis must have sufficient measured rank; a rank-one static maximal-symmetric block is not permitted to be padded with artificial six-component perturbations.

## Constraint rank

At the same background build the tangent/Jacobian maps for the three Gauss, three spatial-diffeomorphism, one scalar-Hamiltonian and any additional null generators. Report all singular values before thresholding. The relative SVD rank tolerance must be frozen globally before examining the refinement trend.

## Collective HDA

Use the same smooth lapse/shift family on every level after coordinate rescaling. Compute

\[
\Delta_{HH}=\frac{\|[H[N],H[M]]-i\hbar D[\sharp_Q(NdM-MdN)]\|}{\|D\|}.
\]

The producer stores raw commutator/target norms and `Delta_HH`; the killer fits the decay power across levels.

## Required output per level

Each level supplied to `collective_gr_universality_killer_gate.py` must contain at minimum:

```json
{
  "level": 0,
  "epsilon": 1.0,
  "D_space_metric": 0.0,
  "kinetic_hessian_sym6": [[0,0,0,0,0,0]],
  "r_G": 0,
  "r_D": 0,
  "r_H": 0,
  "r_extra": 0,
  "r_secondclass": 0,
  "delta_HH_collective": 1.0
}
```

The zeros above are schema placeholders, not theory targets or data. Every science row must additionally store block-space dimensions, support rule, compression leakage and numerical conditioning metadata.

## Non-circularity requirements

- do not insert `D=3` into the metric estimator;
- do not insert `c=1/2` into the Hessian fit;
- do not delete numerically small generator directions until the global SVD tolerance is frozen;
- do not normalize the HDA residual using a target-dependent fitted coefficient;
- retain all levels produced by the frozen blocking rule, including bad ones;
- do not project to the maximal face irrep solely because it improves the GR target;
- store compression leakage and conditioning diagnostics beside every science observable.

## Immediate implementation sequence

1. Treat `collective_j1_block_isometry_gate.py` as the minimal SU(2)/Gauss/volume fusion control only.
2. Use `collective_barycentric_tetra_block_gate.py` as the exact first canonical spatial-block carrier and static-background selection gate.
3. Generate the **one-hit dynamical support** of the first barycentric block under the production `E=H_E^sine`; retain every target-independent boundary irrep/intertwiner sector reached above the frozen numerical tolerance.
4. Add Hermitian `S` support and verify the block basis is closed enough to report finite leakage for `G=-2E/3-32S/9`.
5. Build/compress the route operator on the same retained geometry blocks.
6. Produce the first direct level JSON without comparing it to GR targets.
7. Repeat on at least four refinement scales/habitats.
8. Only then run the preregistered AND gate in `--require-complete` mode.
