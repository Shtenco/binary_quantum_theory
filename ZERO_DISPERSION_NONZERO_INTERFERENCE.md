# Zero vacuum dispersion does not imply zero quantum-geometry interference

Status: **observable-logic closure.**

If the infrared theory reaches the Lorentz/metric universality branch, the original massless photon and graviton poles can remain exactly on the common light cone while connected quantum metric fluctuations remain nonzero.

Therefore the project must distinguish two classes of experiment:

```text
one-point / pole propagation tests;
two-point / fluctuation / interference tests.
```

A null result in the first class does not mathematically imply a null result in the second.

---

## 1. Pole universality branch

Under the assumptions of `MASSLESS_TT_POLE_ALL_ORDERS_THEOREM.md`,

\[
K_{TT}(s)=sF_g(s)
\]

and the original vacuum massless branch remains

\[
s=0.
\]

Likewise, in the common-metric Maxwell branch,

\[
K_\gamma(s)=sF_\gamma(s)
\]

with the same leading cone.

Thus vacuum time-of-flight/dispersion coefficients can vanish.

---

## 2. Connected metric covariance can still be nonzero

The physical history generating functional determines the connected metric correlator

\[
C_h(x,y)
=\langle h(x)h(y)\rangle_c.
\]

A massless Lorentz-invariant pole itself implies long-distance correlations; pole location and fluctuation amplitude are different observables.

The absence of a shifted pole says nothing by itself about whether

\[
C_h(x,y)\ne0.
\]

---

## 3. Exact six-edge optical phase map

For the frozen tetrahedral six-direction optical geometry, the linear metric-to-phase response is

\[
\boxed{
\delta\phi
=\frac{k\ell}{2}J h.
}
\]

Here `h` is represented in the orthonormal symmetric-metric basis and `J` is the already-derived invertible six-edge response matrix.

Therefore the phase covariance is

\[
\boxed{
C_\phi(\omega)
=\left(\frac{k\ell}{2}\right)^2
J C_h(\omega)J^T.
}
\]

For two separated optical devices `A,B`, the cross-spectrum is similarly

\[
\boxed{
C_{\phi,AB}(\omega)
=\left(\frac{k_A\ell_A}{2}\right)
\left(\frac{k_B\ell_B}{2}\right)
J_A C_{h,AB}(\omega)J_B^T.
}
\]

A correlated signal is experimentally preferable to an unexplained single-instrument noise excess because the geometry calculation predicts cross-channel structure.

---

## 4. S4 channel decomposition remains useful in the isotropic branch

The six edge phases decompose into

\[
A_1\oplus E\oplus T_2.
\]

The exact metric-response squared gains are

```text
A1 : 2
E  : 1/2
T2 : 1.
```

For the trace-free physical metric sector the balanced response removes the common/trace mode.  Define the per-mode phase spectral powers

\[
S_E=\frac12\operatorname{Tr}(P_EC_\phi),
\]

\[
S_T=\frac13\operatorname{Tr}(P_{T_2}C_\phi).
\]

Correcting for the known response gains gives

\[
\boxed{
R_\gamma(\omega)
=\frac{S_E/g_E^2}{S_T/g_T^2}
=2\frac{S_E}{S_T}.
}
\]

In a rotationally invariant physical metric covariance,

\[
\boxed{R_\gamma\to1.}
\]

Thus `R_gamma=1` is not a null experiment.  The absolute correlated phase spectrum can remain nonzero while its symmetry ratio becomes isotropic.

---

## 5. Single-photon visibility

For a two-path photon whose relative phase is promoted to an operator `Delta phi`, the ideal output probabilities are controlled by

\[
\langle e^{i\Delta\hat\phi}\rangle.
\]

The fringe visibility is

\[
\boxed{
\mathcal V=\left|\langle e^{i\Delta\hat\phi}\rangle\right|.
}
\]

For a centered Gaussian phase fluctuation,

\[
\boxed{
\mathcal V
=\exp\left[-\frac12\operatorname{Var}(\Delta\phi)\right].
}
\]

This is a fluctuation observable.  It does not require a modified mean propagation speed.

---

## 6. Revised experimental decision tree

### Test A — leading common cone

Check that photon and graviton sectors approach the same metric light cone.

### Test B — vacuum pole deformation

Extract the six quartic TT pole observables and apply the blind `6 -> 1 -> 0` hierarchy.

A zero result is an allowed, and under metric-only Lorentz universality expected, outcome.

### Test C — connected quantum geometry

Independently measure/predict

- absolute metric/phase PSD;
- cross-device correlations;
- the `E/T2` ratio `R_gamma`;
- frequency and separation dependence;
- single-photon visibility where applicable.

Thus the theory remains experimentally falsifiable even in the zero-dispersion branch.

---

## 7. What is still missing numerically

The exact optical response matrix is already known.  The missing object is the physical connected history correlator

\[
C_h^{phys}(\omega,\mathbf r),
\]

including its absolute normalization after the common gravitational scale is fixed.

No numerical phase-noise amplitude is claimed before that object is computed.
