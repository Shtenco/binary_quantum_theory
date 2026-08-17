# Physical-projector refinement and geometric boundary time

Status: **operational continuum protocol; numerical implementation in the candidate theory remains open.**

The finite master-projector theorem solves only the finite common-kernel problem.  This document defines the two additional operations required before a physical gravitational-wave frequency can be extracted without inserting an arbitrary external clock:

1. refinement consistency of physical projectors;
2. a semiclassical geometric boundary-time construction.

---

## 1. Physical projectors across refinement

Let `H_g` be the regulated Hilbert space at refinement level `g`, with constraint family `C_A^(g)`, master constraint `M_g`, and finite zero-sector projector

\[
P_g=\mathbf 1_{\{0\}}(M_g)
\]

when zero is isolated.

Let

\[
I_g:\mathcal H_g\to\mathcal H_{g+1}
\]

be the declared refinement/coarse embedding for the same physical region.

A physical continuum sector requires more than convergence of individual spectra.  The projectors themselves must become cylindrically compatible:

\[
\boxed{
\Delta_P(g)
=P_{g+1}I_g-I_gP_g.
}
\]

Use the normalized mismatch

\[
\boxed{
\delta_P(g)
=\frac{\lVert\Delta_P(g)\rVert}
{\max(\lVert I_gP_g\rVert,\epsilon_{num})}.
}
\]

The continuum-projector gate is

\[
\boxed{\delta_P(g)\to0.}
\]

This is stronger and more physical than asking whether an arbitrary nonzero master eigenvalue stabilizes.

---

## 2. Projected observables must refine consistently too

For a coarse metric observable `O_g`, define its physical compression

\[
O_g^{phys}=P_gO_gP_g.
\]

The observable consistency residual is

\[
\boxed{
\Delta_O(g)
=P_{g+1}O_{g+1}P_{g+1}I_g
-I_gP_gO_gP_g.
}
\]

and must vanish after the same declared normalization/coarse map.

For the five trace-free metric channels this test is performed representation by representation.  A disappearing `E/T2` mismatch is evidence for rotational universality; a stable nonzero mismatch requires a derived physical order parameter.

---

## 3. Why a timeless projector can still give a frequency

A projector onto constraints is timeless.  A physical frequency arises only after specifying a relational or boundary observable that measures separation.

For the first gravitational-wave prediction the cleanest no-new-matter route is a semiclassical boundary amplitude.

Choose boundary states

\[
|\Psi_{in}[g_{in},K_{in}]\rangle,
\qquad
|\Psi_{out}[g_{out},K_{out}]\rangle
\]

peaked on intrinsic 3-geometry `g` and extrinsic geometry `K` that bound a near-flat four-dimensional slab.

The classical saddle associated with these data has a geometric proper separation

\[
\tau=\tau[g_{in},K_{in};g_{out},K_{out}],
\]

which is invariant under a mere relabelling of the interior lapse.

Define

\[
\boxed{
\mathcal A_\tau
=\langle\Psi_{out}(\tau)|P_{phys}|\Psi_{in}(0)\rangle.
}
\]

The frequency used for physical propagation is conjugate to this **geometric boundary proper time**, not to the spectral parameter of the constraint operator.

---

## 4. Source-deformed connected metric amplitude

Insert the derived coarse metric channels with a frozen symmetric source prescription and define

\[
Z_\tau[J]
=\langle\Psi_{out}(\tau)|P_{phys}[J\cdot O_g]|\Psi_{in}(0)\rangle.
\]

Normalize by the source-free boundary amplitude before taking connected derivatives so vacuum normalization does not masquerade as a local graviton self-energy.

Define

\[
W_\tau[J]=-i\hbar\log\frac{Z_\tau[J]}{Z_\tau[0]}.
\]

Then

\[
G^{conn}_{AB}(\tau,\mathbf r)
=\frac{\delta^2W_\tau}{\delta J_A\delta J_B}\Big|_{J=0}.
\]

After the declared gauge/relational reduction, Fourier transform the boundary proper separation and tangent-space displacement:

\[
G_{TT}(\omega,\mathbf k)
=\int d\tau\,d^3r\,
 e^{i\omega\tau-i\mathbf k\cdot\mathbf r}
 G^{conn}_{TT}(\tau,\mathbf r).
\]

Its inverse/1PI continuation supplies the physical pole kernel.

---

## 5. Absolute scale is not needed for the first dimensionless result

Let one coarse physical length unit in the scaling window be `a_*` and define the corresponding proper-time unit from the leading cone,

\[
\tau_*=a_*/c.
\]

Use

\[
\hat k=a_*k,
\qquad
\hat\omega=\tau_*\omega.
\]

Then the two physical TT branches can be fitted entirely in internal units:

\[
\boxed{
\hat\omega_\sigma^2
=\hat k^2\left[1+e_{4,\sigma}(\hat n)\hat k^2+O(\hat k^4)\right].
}
\]

The six Wilson coefficients extracted from `e4_sigma(n)` are dimensionless and can be blind-frozen **before** any Planck/metre/second calibration.

Only later does one common `a_*` convert the dimensionless result to

\[
A_{4,\sigma}=\frac{a_*^2}{(\hbar c)^2}e_{4,\sigma}.
\]

This prevents the absolute scale datum from contaminating the shape prediction.

---

## 6. Required positive controls

A physical boundary/history implementation must pass all of the following before any order-four coefficient is opened:

1. `delta_P(g)` decreases under refinement;
2. projected metric observables refine consistently;
3. changing interior lapse/slicing while holding boundary geometry fixed does not change the physical amplitude beyond the measured regulator error;
4. the leading TT mode is massless;
5. the two helicities have positive common residue at `k->0`;
6. the leading cone has `z->1` after one time/space unit ratio is fixed;
7. the two-derivative tensor structure approaches Fierz-Pauli/DeWitt;
8. all order-`k^2` direction/polarization splitting vanishes in the target IR window;
9. only then is the full six-dimensional order-`k^4` vector extracted.

---

## 7. Symmetry decision tree after extraction

The frozen six-vector is not automatically interpreted as new physics.

Test in this order:

```text
full S4 six-vector
 -> does it collapse to the one-dimensional SO3 scalar subspace?
 -> does that scalar also vanish on the Lorentz-invariant massless pole?
```

Thus the physical outcomes are

```text
6 : surviving tetrahedral order / anisotropic preferred structure
1 : spatially isotropic but preferred foliation / Lorentz breaking
0 : metric-only Lorentz/GR universality for the massless pole at k^4.
```

This decision tree is frozen before the microscopic physical pole is known.
