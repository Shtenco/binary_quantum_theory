# Preregistration: physical sine-ordering two-node Euclidean × route HDA

**Frozen before evaluating the new sine-ordering two-node result.**

Protocol frozen in commit `9a53f5edf160f2b62efbaeb047e59f878dfc73d2`; implementation added only afterward. This edit exists solely to trigger the now-installed CI workflow and does not change any acceptance threshold.

## Why this gate is required

The historical two-node Euclidean × route regression uses the earlier Hermitian structural ordering

\[
H_+=(T+T^\dagger)/2.
\]

The subsequent physical Euclidean/Lorentzian pipeline independently selected

\[
H_{sine}=(T-T^\dagger)/(2i)
\]

because the standard Euclidean regularization carries the Poisson-to-commutator `1/i` phase and the antisymmetric curvature channel is the nontrivial classical trace channel.

The Lorentzian operator uses

\[
K_{sine}=[V,H_{sine}].
\]

Therefore the finite two-node HDA regression must be repeated with the same `H_sine`; the old `H_+` numbers are retained only as historical structural controls.

## Frozen operator

On the same all-`j=1/2`, all-`K=0` K5 input and `Jmax=5/2`, define

\[
H^{sine}[N]
=N(x_0)H^{sine}_0+N(x_1)H^{sine}_1+R[N;Q]
\]

with the exact same shared route metric, route lattice, lapses, WKB carrier, epsilon sequence and no channel-dependent normalization used by the historical two-node gate.

Only the Euclidean ordering changes:

```text
old:  H_plus = (T+T^dagger)/2
new:  H_sine = (T-T^dagger)/(2i)
```

The exact decomposition remains

\[
[H[N],H[M]]
=[R_N,R_M]+C_{cross}+(ad-bc)[H^{sine}_0,H^{sine}_1].
\]

## Frozen numerical protocol

```text
Jmax = 5/2
L = 48
carrier = 8
initial = all 10 links j=1/2, all five K=0
epsilon = 1/4, 1/8, 1/16, 1/32, 1/64
state prune tolerance = 1e-8
zero-aware exact-Q-nullspace volume convention = ON
```

No old plus-order commutator norm is used as a regression target.

## Frozen acceptance conditions

PASS requires all of the following:

1. both `H_sine,0` and `H_sine,1` have nonzero support and norm;
2. the raw two-node sine commutator is nonzero and finite;
3. final route-only defect `< 1e-4`;
4. fitted cross exponent
   \[
   0.75\le p_{cross}\le1.25;
   \]
5. fitted pure geometry relative exponent
   \[
   1.75\le p_{GG}\le2.25;
   \]
6. fitted joint exponent
   \[
   0.75\le p_{joint}\le1.25;
   \]
7. the five-point cross, pure-GG and joint sequences are strictly decreasing with decreasing `epsilon`;
8. the final joint defect at `epsilon=1/64` is `<0.05`.

The `0.05` endpoint is intentionally looser than the historical plus-order `0.02` threshold because the finite coefficient is genuinely unknown before this run. The asymptotic scaling exponents are the primary test.

## Falsification rule

A FAIL is retained. No phase, channel normalization, subtraction, route coupling or endpoint threshold may be changed after seeing the result.

If the gate fails only through a different finite coefficient while the exponents pass, the candidate retains the asymptotic composition theorem but the sine finite-habitat calibration is recorded as a failed finite endpoint control.

## Next step if PASS

Only after this gate passes should the phase- and real-normalization-completed Lorentzian `H_L` be inserted into the same two-node route habitat.
