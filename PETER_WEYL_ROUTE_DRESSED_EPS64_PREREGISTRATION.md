# Peter--Weyl x route local gate: held-out epsilon=1/64 preregistration

Status: **frozen before evaluating epsilon=1/64**.

## Observed training regulator points

The first real regulator-safe Peter--Weyl x route run used the genuine-volume
`Jmax=5/2` Euclidean node Hamiltonian on the all-`j=1/2`, all-`K=0` K5 input.
The route metric was reconstructed from the diagonal intertwiner expectation

$$
Q_{ab}=\langle J_a\cdot J_b\rangle
$$

for local legs `(0,2)`.

The first five regulator values were

$$
\epsilon=(1/2,1/4,1/8,1/16,1/32).
$$

The observed cross-anomaly ratios were

$$
(0.40214012991369874,
0.20115016967971658,
0.10058510541208215,
0.050293805511581365,
0.025147059363797686).
$$

The route-only defects were

$$
(2.6432951717032992\times10^{-5},
1.3221741194383671\times10^{-5},
6.6115292990903105\times10^{-6},
3.30584706452613\times10^{-6},
1.6529339109419748\times10^{-6}).
$$

The original CI gate is retained as an honest FAIL because its pre-existing
endpoint condition required the joint defect at `epsilon=1/32` to be below
`0.02`, while the observed value was `0.02514705941812194`.

## Frozen scaling law

A log--log fit using only the five points above gives

$$
\boxed{p_\times=0.9998293732628482}
$$

and

$$
\boxed{p_{route}=0.9998293469584574}.
$$

No exponent is refit after opening the held-out point.

## Held-out prediction

For

$$
\boxed{\epsilon_{hold}=1/64}
$$

the frozen power-law predictions are

$$
\boxed{\Delta_\times^{pred}=0.012576237890178199},
$$

$$
\boxed{\Delta_{route}^{pred}=8.266449670538699\times10^{-7}},
$$

and, because the route error is negligible compared with the orthogonal
geometry-changing cross channel,

$$
\boxed{\Delta_{joint}^{pred}=0.012576237917346172}.
$$

## Pass/fail rule

The held-out point passes only if all of the following are true:

1. `epsilon=1/64` was not included in the fit above;
2. relative prediction error of the cross anomaly is below `5%`;
3. relative prediction error of the route-only defect is below `5%`;
4. relative prediction error of the joint defect is below `5%`;
5. the held-out joint defect is below `0.02` without changing any operator,
   metric definition, carrier, path lattice size, or coefficient.

If any condition fails, the held-out result is a FAIL.  No new fit or threshold
will replace it in the result document.
