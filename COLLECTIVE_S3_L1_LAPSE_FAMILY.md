# Frozen collective S3 l=1 lapse family

## Purpose

The collective HDA experiment must use the same smooth lapse family at every refinement level.  Choosing new lapses after seeing a commutator residual would be a direct source of target leakage.

The canonical 16-cell PL-S3 carrier already has a target-independent embedding in R4: its eight primal vertices are `+/- e_mu`.  Barycentric subdivision preserves this piecewise-flat embedded carrier.

For every dual cell / tetrahedral chamber, let `c` be its Euclidean centroid in R4 and define the radial direction

\[
x=\frac{c}{\|c\|}\in S^3.
\]

The four frozen scalar lapse fields are the lowest nonconstant scalar harmonics of the unit 3-sphere,

\[
\boxed{N_\mu(x)=x_\mu,\qquad \mu=0,1,2,3.}
\]

No level-dependent amplitude normalization or refit is allowed.

## HDA pairs

There are six unordered harmonic pairs `(mu,nu)`, `0<=mu<nu<=3`.

The primary pair is frozen as

```text
(mu,nu) = (0,1)
```

before any collective `[H,H]` result.

The five remaining pairs

```text
(0,2), (0,3), (1,2), (1,3), (2,3)
```

are held-out covariance tests. A collective GR claim may not be based only on the best pair.

For the continuum unit-S3 metric,

\[
\nabla_a N_\mu=(e_\mu-x_\mu x)_a,
\]

so the antisymmetric HDA combination is

\[
\boxed{
N_\mu\nabla N_\nu-N_\nu\nabla N_\mu
=x_\mu e_\nu-x_\nu e_\mu.
}
\]

This is an `SO(4)` Killing rotation and is exactly tangent to `S3`:

\[
x\cdot\beta_{\mu\nu}=0.
\]

The collective diffeomorphism target still uses the **measured collective inverse metric** through `sharp_Q`; this lapse file does not insert the GR metric or a DeWitt coefficient.

## Refinement transport

At every barycentric level:

1. construct the level from the fixed 16-cell embedding;
2. evaluate each `N_mu` at every dual-cell radial centroid;
3. retain the raw dimensionless coordinate value with no per-level RMS fitting;
4. use the same six pair labels at every level;
5. rescale only the coordinate resolution parameter `epsilon` according to the separately frozen block/metric-resolution prescription, never the lapse amplitudes themselves.

## Guards

The executable gate checks through L3 that:

- every radial centroid is finite/nonzero;
- all four lapse means vanish up to numerical roundoff;
- their covariance is isotropic under coordinate permutations;
- the four RMS amplitudes are level-independent within the exact refinement symmetry;
- every one of six analytic rotation fields is tangent to the radial S3 direction;
- all six pair labels remain present on every level.

These are geometry/protocol checks only. They do not count as a collective HDA PASS.
