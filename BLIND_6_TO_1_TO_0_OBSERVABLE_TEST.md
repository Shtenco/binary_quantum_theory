# Blind observable hierarchy: 6 -> 1 -> 0

Status: **exact consequence of the frozen six-observable extractor plus the declared symmetry assumptions.**

The complete quartic TT basis and extractor already define

\[
y=A c,
\]

with six preregistered polarization/direction observables and six Wilson coefficients.

The rotationally invariant TT structure has coefficient vector

\[
\boxed{
v_{iso}=(6,24,6,36,-9,18)^T.
}
\]

Exact multiplication by the frozen extraction matrix gives

\[
\boxed{
A v_{iso}=(1,1,1,1,1,1)^T.
}
\]

Therefore the full symmetry decision tree has an exceptionally simple observable form.

## 1. Generic tetrahedral S4 phase: six numbers

No additional symmetry is imposed:

\[
\boxed{y=(y_1,y_2,y_3,y_4,y_5,y_6)\in\mathbb R^6.}
\]

The six components are the already frozen `(100)+`, `(100)x`, `(110)+`, `(110)x`, `(111)+`, `(120)+` quartic TT responses after lower-derivative subtraction and common normalization.

## 2. Continuous spatial isotropy: one number

If the physical state/vacuum restores spatial `SO(3)`, then

\[
\boxed{y_1=y_2=y_3=y_4=y_5=y_6=\eta_s.}
\]

Equivalently the five exact anisotropy residuals

\[
r_i=y_{i+1}-y_1,\qquad i=1,\ldots,5
\]

must vanish.

In coefficient space this is

\[
\boxed{c=\eta_s(6,24,6,36,-9,18)^T.}
\]

No Euclidean norm in Wilson-coordinate space is needed to define this test.

## 3. Local Lorentz-invariant metric-only massless pole: zero

Under the additional assumptions of `TT_POLE_UNIVERSALITY_NO_GO.md`, a local analytic Lorentz-invariant metric-only four-derivative correction is proportional to additional powers of

\[
s=-\omega^2+c^2k^2
\]

and does not perturbatively shift the original massless branch `s=0`.

Therefore

\[
\boxed{\eta_s=0}
\]

and hence

\[
\boxed{y=(0,0,0,0,0,0),\qquad c=(0,0,0,0,0,0).}
\]

## 4. Two-stage blind hypothesis test

The correct order is fixed before microscopic physical-pole data are opened.

### Stage I: 6 -> 1

Test the five contrasts

\[
\boxed{
r=(y_2-y_1,y_3-y_1,y_4-y_1,y_5-y_1,y_6-y_1).}
\]

If they are not compatible with zero after declared numerical/statistical errors, a physical `SO(3)` vacuum has not been reached and the full six-vector is retained.

If they pass, define the common isotropic response by the preregistered estimator appropriate to the covariance model.  For equal deterministic weights,

\[
\eta_s=\frac16\sum_i y_i.
\]

For correlated numerical/experimental covariance `Sigma`, use the generalized least-squares estimator

\[
\boxed{
\hat\eta_s
=\frac{\mathbf1^T\Sigma^{-1}y}
{\mathbf1^T\Sigma^{-1}\mathbf1}.
}
\]

The covariance prescription must be fixed before opening the final data.

### Stage II: 1 -> 0

Test

\[
\boxed{\eta_s=0.}
\]

A significant nonzero common value with Stage I passed is the signature class of a spatially isotropic preferred foliation/order parameter rather than generic tetrahedral order.

## 5. Why this is unusually clean

The six-to-one reduction does not depend on an arbitrary norm or post-hoc rotation in Wilson space.  In the already frozen observable coordinates it is simply equality of all six numbers.

Thus the physical outcomes are operationally distinct:

```text
six unequal values       -> surviving anisotropic/preferred spatial order;
six equal nonzero values -> SO3-preserving preferred foliation / Lorentz breaking;
six values zero          -> metric-only Lorentz/GR universality at quartic massless-pole order.
```

A physical-order-parameter consistency test must accompany the first two nonzero branches.

## 6. Exact matrix identity used by the test

The identity to preserve in CI is

```text
A @ [6,24,6,36,-9,18]^T = [1,1,1,1,1,1]^T.
```

Any future change of basis/extractor that breaks this identity must be treated as a change of the preregistered physicalization protocol, not a harmless refactor.
