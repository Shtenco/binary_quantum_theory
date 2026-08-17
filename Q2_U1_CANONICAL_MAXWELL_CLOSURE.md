# q=2 compact phase -> canonical Maxwell dynamics

Status: **exact finite canonical/gauge theorem conditional on a positive local quadratic blocked phase action.  The microscopic deconfinement/stiffness calculation remains open.**

The Hopf/Pancharatnam construction already derives compact link phases from q=2 rays.  This document closes the next structural arrow: once the blocked phase sector is local, analytic, parity-even and has a positive quadratic deconfined regime, gauge covariance forces the leading canonical dynamics into the Maxwell form up to one overall stiffness and geometric Hodge/time normalization.

It does **not** claim that the microscopic q=2 dynamics has already been shown to lie in that phase.

---

## 1. Spatial cochain complex

On the canonical 16-cell boundary use oriented cochains

```text
C0 --d0--> C1 --d1--> C2.
```

The seed has

```text
V=8, E=24, F=32, T=16.
```

For ascending edge/face orientations,

\[
\boxed{d_1d_0=0.}
\]

The exact ranks are

\[
\boxed{\operatorname{rank}d_0=7,\qquad \operatorname{rank}d_1=17.}
\]

Thus

\[
\dim\ker d_1=24-17=7=\dim\operatorname{im}d_0
\]

and hence

\[
\boxed{H^1(S^3)=0}
\]

in this finite cochain realization: every zero-curvature one-form is pure gauge.

---

## 2. Compact phase variables from q=2

For every oriented neighboring pair,

\[
U_e=e^{i\theta_e}
\]

is the normalized Pancharatnam overlap link.  Local ray rephasing gives

\[
\theta\mapsto\theta+d_0\lambda\pmod{2\pi}.
\]

The plaquette curvature is

\[
\Phi=d_1\theta\pmod{2\pi},
\]

which is gauge invariant because `d1 d0=0`.

The Hopf first Chern number fixes the topological normalization of the compact phase/charge unit.  It does not fix the kinetic stiffness.

---

## 3. Most economical quadratic Lorentzian phase action

Let `M1` and `M2` be positive geometric Hodge matrices on one- and two-cochains in the semiclassical metric background.  Introduce a vertex temporal potential `A0` and the gauge-covariant electric velocity

\[
\mathcal E_t=\dot\theta-d_0A_0.
\]

Under

\[
\theta\mapsto\theta+d_0\lambda,
\qquad
A_0\mapsto A_0+\dot\lambda,
\]

`E_t` and `Phi=d1 theta` are invariant.

The parity-even local quadratic action with one common Maxwell stiffness is

\[
\boxed{
L_A
=\frac{Z_A}{2}\mathcal E_t^TM_1\mathcal E_t
-\frac{Z_A}{2}\Phi^TM_2\Phi.
}
\]

A more general microscopic action can initially have different electric/magnetic coefficients.  The common-coefficient form is the target Lorentzian scaling fixed point after the physical time/space unit ratio is chosen.  Equality is therefore a **dynamical universality test**, not an identity of the Hopf bundle.

---

## 4. Gauss law follows from the action

The canonical electric momentum is

\[
\boxed{
p=Z_AM_1(\dot\theta-d_0A_0).
}
\]

Varying `A0` gives

\[
\boxed{d_0^Tp=0.}
\]

Thus the lattice Gauss law is not separately postulated once local gauge invariance and the canonical kinetic term are fixed.

The Hamiltonian on the constraint surface is

\[
\boxed{
H_A
=\frac1{2Z_A}p^TM_1^{-1}p
+\frac{Z_A}{2}(d_1\theta)^TM_2(d_1\theta).
}
\]

The seven independent gauge generators remove seven configuration directions and their conjugate Gauss constraints, leaving 17 canonical transverse/coexact pairs on this finite spatial `S3` discretization.

This finite count is not to be read as 17 photon polarizations.  In a local translation/scaling window those coexact modes organize into the usual transverse normal modes; the physical continuum polarization count must be checked in the Lorentzian history kernel.

---

## 5. Linear wave operator and why ZA cancels

In temporal gauge on the Gauss-reduced sector,

\[
\dot\theta=\frac1{Z_A}M_1^{-1}p,
\]

\[
\dot p=-Z_A d_1^TM_2d_1\theta.
\]

Therefore

\[
\boxed{
\ddot\theta
=-M_1^{-1}d_1^TM_2d_1\theta.
}
\]

The overall stiffness `Z_A` cancels from the linear wave spectrum.

This is the clean separation:

```text
geometry/Hodge + electric/magnetic ratio -> light cone / propagation speed;
ZA                                 -> canonical normalization and charge coupling.
```

After canonical field normalization, if the compact Wilson charge is normalized to one,

\[
e=Z_A^{-1/2},
\qquad
\boxed{\alpha=\frac1{4\pi Z_A}}.
\]

Hence topology/compactness can fix integer charge normalization while the fine-structure constant remains one genuine dynamical scalar response.

---

## 6. Unit-Hodge finite positive control

For `M1=I`, `M2=I`, the seed curl Laplacian

\[
K_1=d_1^Td_1
\]

has exact spectral multiplicities

\[
\boxed{
0^{\times7},\qquad
4^{\times6},\qquad
6^{\times8},\qquad
8^{\times3}.
}
\]

The seven zero modes equal `im d0` exactly.  There are no additional flat physical one-form modes, consistent with `b1=0` on `S3`.

These eigenvalues are a topology/symmetry positive control for unit Hodge weights, not physical photon frequencies of the final emergent metric.

---

## 7. What remains to turn the carrier into a photon

The microscopic q=2 phase sector must still demonstrate, from its own history/effective action:

1. a positive blocked electric kinetic term;
2. a positive magnetic curvature term;
3. no gauge-invariant photon mass term;
4. electric/magnetic scaling consistent with one Lorentzian light cone;
5. deconfined long-distance compact-U(1) behavior rather than a gapped/confined phase;
6. two transverse massless poles in the local continuum window;
7. a regulator/refinement-stable positive `Z_A`;
8. only then a blind numerical value of `alpha=1/(4 pi Z_A)`.

The correct chain is therefore

\[
\boxed{
q=2\ \text{rays}
\to U(1)\ \text{links}
\to \text{compact curvature}
\to \Gamma_{U(1)}
\to \text{Maxwell fixed point?}
\to Z_A
\to \alpha.
}
\]

The question mark is a genuine physical gate.  It is not filled by the existence of a Berry connection alone.
