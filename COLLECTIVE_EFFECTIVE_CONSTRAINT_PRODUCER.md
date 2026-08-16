# Collective effective-constraint producer — implementation contract

This file specifies the computation needed to turn the preregistered collective GR killer from `INCOMPLETE` into a real PASS/FAIL experiment inside the theory.

## Blocking

Use the canonical PL-S3 refinement family. At level `l`, choose disjoint/interlocking blocks by a deterministic rule fixed from combinatorics only. Boundary collective faces use the symmetric SU(2) channel `n` spin-1/2 -> `j=n/2`; internal intertwiners are retained or integrated out by a frozen rule.

The compression is operator-first. For every Gauss/diffeomorphism/Hamiltonian generator `C_A`, compute

`C_eff = W^dagger C_A W`

and the leakage `||(1-WW^dagger) C_A W||`. Do not replace an operator by an expectation value before the constraint algebra is built.

## Effective metric and D_space

Construct the collective flux Gram matrix and the nondegenerate metric on the block boundary. Distances must be derived from that collective metric (or a demonstrated equivalent dual metric), not from bare simplex-count graph distance. Measure ball volumes over an automatically defined pre-saturation window and report the full `(r,V(r))` data used for the dimension estimate.

## Effective DeWitt kinetic tensor

Choose a declared homogeneous/nondegenerate background. Perturb the six independent metric momenta in the orthonormal `sym6` basis and evaluate the Hessian of the effective scalar constraint. Store the raw `6x6` Hessian. The killer gate, not the producer, extracts `c_eff`.

## Constraint rank

At the same background build the tangent/Jacobian maps for the three Gauss, three spatial-diffeomorphism, one scalar-Hamiltonian and any additional null generators. Report singular values before thresholding. The eventual relative rank tolerance must be frozen globally before examining the refinement trend.

## Collective HDA

Use the same smooth lapse/shift family on every level after coordinate rescaling. Compute

`Delta_HH = || [H[N],H[M]] - i hbar D[sharp_Q(N dM-M dN)] || / ||D||`.

The producer stores the raw commutator/target norms and `Delta_HH`; the killer fits the decay power across levels.

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

The zeros above are schema placeholders, not theory targets or data.

## Non-circularity requirements

- do not insert `D=3` into the metric estimator;
- do not insert `c=1/2` into the Hessian fit;
- do not delete numerically small generator directions until the global SVD tolerance is frozen;
- do not normalize the HDA residual using a target-dependent fitted coefficient;
- retain all levels produced by the frozen blocking rule, including bad ones;
- store compression leakage and conditioning diagnostics beside every science observable.

## Immediate implementation sequence

1. Build `W_l` for the first `j=1` collective face/block sector.
2. Verify `W_l^dagger W_l=I` and report boundary/interior leakage.
3. Compress the already frozen v1.2 `G,D,H` operators.
4. Generate one level JSON without comparing it to GR targets.
5. Repeat for at least four scales/habitats.
6. Only then run the preregistered AND gate in `--require-complete` mode.
