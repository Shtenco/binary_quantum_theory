# Peter-Weyl master-projector pilot — first post-HDA result

Date: **2026-08-18**

Status: **finite tested result on the declared 6D carrier; no exact physical zero sector found.**

This calculation does not test HDA. It consumes the already-defined five regulated K5 Peter-Weyl Hamiltonian constraints `H_v` and constructs

\[
M_G=\sum_{v,w} H_v^\dagger G^{vw}H_w
\]

on the six-dimensional low-logical-excitation carrier

```text
all ten links j=1/2
all K_v=0
plus the five states with one node K_v=2 and the other four K=0
```

with `Jmax=5/2`.

The frozen zero tolerance was `1e-10 * max(|lambda|)`.

## Identity constraint metric

For `G=I`, the master spectrum is

```text
11.08533732466261
11.791991154697095
12.04178781892493
12.29313673816942
12.73348482722436
13.44557133696495
```

Hence

```text
zero-sector rank = 0
minimum master eigenvalue = 11.08533732466261
```

and there is no exact common kernel of all five `H_v` inside this declared six-dimensional carrier.

## Positive-metric robustness

Two additional positive constraint metrics were frozen and evaluated.

For the diagonal metric the spectrum begins at

```text
lambda_min = 32.71110521893697
zero-sector rank = 0
```

and for a fixed-seed random positive metric

```text
lambda_min = 152.66824386964814
zero-sector rank = 0
```

with minimum metric eigenvalue `0.7247424644175176`.

All three choices therefore agree on the exact finite nullity: zero. The zero projectors are all the zero operator and have pairwise difference exactly zero.

## Numerical/operator checks

```text
master Hermiticity error = 0
internal checks = PASS
finite exact zero sector found = false
```

The actual `H_v` column supports in the six-state carrier range from 39 to 52 sparse Peter-Weyl output states per node/source column.

## Interpretation

This is not a failure of HDA and does not motivate another HDA calculation. It says only:

> the chosen six-dimensional all-j=1/2 low-logical-excitation carrier does not intersect the exact common kernel of the five regulated `H_v` at `Jmax=5/2`.

The immediate falsifier is therefore carrier/refinement enlargement. The next frozen calculation is the full 32-dimensional all-j=1/2 `K_v in {0,2}` domain using the same five `H_v`, `Jmax`, master construction and zero criterion.

If the full 32D domain also has no exact zero sector, the programme moves to a preregistered spectral-window/refinement/rigging sequence and studies the flow of the lowest normalized master eigenvalues and metric matrix elements. It does **not** retune the HDA sector.

No constraint spectral parameter is interpreted as physical frequency. Physical `omega` still requires the later physical history/rigging or relational construction leading to `Z[J_g] -> W[J_g] -> Gamma[g] -> K_TT(omega,k)`.

Executable: `scripts/peter_weyl_master_projector_pilot.py`.
