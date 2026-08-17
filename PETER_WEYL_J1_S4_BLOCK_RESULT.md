# Peter-Weyl j=1 S4 blocking carrier — finite PASS

Status: **completed exact finite representation/volume gate.  The subsequent j=1 higher-shell dynamics is still being computed.**

The latest `physicalization-j1-rg-pilot` run was cancelled during the expensive higher-shell column step, but its preceding canonical carrier gate completed successfully.  The cancellation therefore does not invalidate the representation result.

## Representation result

For four face spins `j=1` the singlet space is three-dimensional and decomposes under tetrahedral `S4` as

\[
\boxed{\mathcal H_{singlet}^{j=1}=[4]\oplus[2,2].}
\]

The fine four-`j=1/2` singlet geometry qubit transforms as `[2,2]`.

Because `[2,2]` occurs with multiplicity one in the coarse `j=1` singlet space, the symmetry-selected coarse logical doublet and the fine->coarse intertwiner are unique up to an overall phase.

In the recoupling basis `K=(0,2,4)` one convenient convention is

\[
|0\rangle_c=|K=2\rangle,
\]

\[
|1\rangle_c=\frac{2|K=0\rangle-\sqrt5|K=4\rangle}{3},
\]

up to the irrelevant overall sign of the second vector.

The orthogonal trivial vector is

\[
|A_1\rangle=\frac{\sqrt5|K=0\rangle+2|K=4\rangle}{3}.
\]

## Numerical certificate

The completed gate reported

```text
projector error                         2.3551386880256624e-16
completeness error                      2.3551386880256624e-16
intertwiner max error, all 24 S4 perms 5.20740757162067e-16
isometry error                          0
range-projector error                   0
```

For the absolute-volume operator,

```text
doublet volume                 1.3160740129524928
expected 3^(1/4)               1.3160740129524924
relative value error           3.374348292568962e-16
relative scalar error          3.6086528615557073e-16
trivial-sector absolute volume 1.4558210615294837e-08
trivial/doublet                 1.1061847944732842e-08
spectral relative tolerance    3e-8
```

Thus the trivial channel is zero at the declared floating spectral floor, while the `[2,2]` doublet carries the expected scalar volume to machine precision.

## What this closes

The first internal representation-growth step

\[
(j=1/2,[2,2])\longrightarrow(j=1,[2,2])
\]

has no projector-tuning freedom: `S4` fixes the coarse two-dimensional geometry carrier.

This is exactly the missing representation-theory prerequisite for a nonseparable internal RG calculation.

## What remains open

The old monolithic pilot attempted

\[
a_i=(H_0+H_1)|i\rangle,
\qquad
b_i=(H_0+H_1)^2|i\rangle
\]

and hit the workflow's 60-minute wall during `b_i`.

The replacement calculation shards the exact identity

\[
\boxed{(H_0+H_1)^2=\sum_{r,s\in\{0,1\}}H_rH_s}
\]

and will assemble all 32 logical columns before reporting a coarse `R_aniso(j=1)`.

Until that assembly succeeds, no j=1 representation-RG beta function or physical `zeta4` is claimed.
