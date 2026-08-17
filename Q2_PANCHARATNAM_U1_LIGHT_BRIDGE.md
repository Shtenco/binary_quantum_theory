# q=2 -> Hopf/Pancharatnam U(1) -> candidate light carrier

Status: **exact kinematic derivation of a compact U(1) connection from local q=2 quantum rays; photon dynamics remains a separate deconfinement/effective-action gate**.

This bridge explains why a phase gauge structure is natural in the same q=2 microscopic setting that already produces the SU(2)/tetrahedral geometry carrier. It does not identify a gauge redundancy with an experimentally established photon by fiat.

## 1. The q=2 state space already contains the Hopf U(1)

A normalized two-component complex state

\[
|\psi\rangle=(z_0,z_1)^T,
\qquad |z_0|^2+|z_1|^2=1,
\]

is a point of

\[
S^3\subset\mathbb C^2.
\]

Physical pure states are rays,

\[
|\psi\rangle\sim e^{i\lambda}|\psi\rangle,
\]

so

\[
\mathcal P(\mathbb C^2)=\mathbb{CP}^1\simeq S^2.
\]

Thus q=2 contains the Hopf fibration

\[
\boxed{U(1)\longrightarrow S^3\longrightarrow S^2.}
\]

The `SU(2)` action rotates the Bloch sphere; the `U(1)` fiber is the phase redundancy of the representative state vector. These are two parts of the natural `U(2)` structure of a qubit, not unrelated groups inserted by hand.

## 2. Canonical discrete phase connection

For neighboring nonorthogonal rays `v,w`, define the normalized overlap

\[
\boxed{
U_{vw}
=\frac{\langle\psi_v|\psi_w\rangle}
{|\langle\psi_v|\psi_w\rangle|}
\in U(1).
}
\]

Under independent local changes of representatives,

\[
|\psi_v\rangle\mapsto e^{i\lambda_v}|\psi_v\rangle,
\]

one obtains exactly

\[
\boxed{
U_{vw}\mapsto e^{-i\lambda_v}U_{vw}e^{i\lambda_w}.
}
\]

Therefore `U_vw` transforms as a compact Abelian lattice gauge link.

The oriented plaquette product

\[
\boxed{
W_f=\prod_{(vw)\in\partial f}U_{vw}=e^{i\Phi_f}
}
\]

is gauge invariant. It is the Bargmann/Pancharatnam holonomy of the ordered rays around the face.

This provides an intrinsic q=2 construction of the phase variable used abstractly in the existing simplicial U(1) Maxwell gate.

## 3. Continuum Berry connection

For a smooth normalized ray field,

\[
\boxed{
A=-i\langle\psi|d\psi\rangle,
\qquad
A\mapsto A+d\lambda.
}
\]

Its curvature is

\[
F=dA.
\]

Using the Bloch-sphere representative

\[
|\psi(\theta,\phi)\rangle
=\begin{pmatrix}
\cos(\theta/2)\\
e^{i\phi}\sin(\theta/2)
\end{pmatrix},
\]

one finds in the north-chart convention

\[
A=\frac{1-\cos\theta}{2}d\phi,
\]

\[
\boxed{
F=\frac12\sin\theta\,d\theta\wedge d\phi.
}
\]

Consequently

\[
\boxed{
\frac1{2\pi}\int_{S^2}F=1.
}
\]

The minimal topological flux/charge normalization is therefore fixed by the first Chern number of the q=2 Hopf bundle.

## 4. Relation to the quantum geometric tensor

The same local rays possess the quantum geometric tensor

\[
Q_{\mu\nu}
=\langle\partial_\mu\psi|
(1-|\psi\rangle\langle\psi|)
|\partial_\nu\psi\rangle.
\]

Its real part is the Fubini-Study metric and its imaginary part is the Berry curvature:

\[
\operatorname{Re}Q=g_{FS},
\qquad
F_{\mu\nu}=-2\operatorname{Im}Q_{\mu\nu}
\]

(up to the fixed sign convention for `A`).

Thus shape distinguishability and geometric phase are two pieces of one q=2 projective geometry. This is the precise mathematical sense in which a phase/light carrier can emerge from the same microscopic information-bearing alternative that supplies the geometry qubit.

## 5. Weak-field Maxwell form

The local, orientation-even, compact plaquette action with the minimal Wilson form is

\[
S_W
=\kappa\sum_f w_f\left(1-\operatorname{Re}W_f\right).
\]

For small holonomy,

\[
W_f=e^{i\Phi_f},
\qquad
1-\cos\Phi_f=\frac12\Phi_f^2+O(\Phi_f^4),
\]

so

\[
\boxed{
S_W
=\frac{\kappa}{2}
\sum_f w_f\Phi_f^2+O(\Phi^4),
}
\]

which is the compact-lattice precursor of

\[
-\frac{Z_A}{4}\int\sqrt{-g}\,F_{\mu\nu}F^{\mu\nu}.
\]

The geometry/Hodge weights `w_f` are fixed by the emergent metric. The overall positive phase stiffness `kappa`, equivalently the continuum `Z_A`, is **not fixed by the Hopf topology or gauge covariance**.

This is important: the topological unit of charge is derived, while the electromagnetic coupling strength remains one dynamical scalar response.

## 6. Why this is not yet a photon theorem

`U_vw` constructed from ray overlaps is initially a **composite Berry connection**. A gauge redundancy does not automatically imply an independent massless particle.

To claim an emergent photon, the microscopic dynamics must demonstrate that the long-distance compact U(1) sector is in a deconfined/Coulomb phase with a positive Maxwell stiffness and two transverse Lorentzian poles.

The remaining gate is therefore concrete:

```text
q=2 rays
 -> Pancharatnam compact links U_vw                         [closed]
 -> gauge-invariant plaquette holonomy W_f                 [closed]
 -> blocked phase effective action Gamma_U1[U,g]           [open]
 -> positive deconfined Maxwell fixed point                [open]
 -> two transverse massless poles                          [open]
 -> Z_A                                                    [open]
 -> alpha=1/(4 pi Z_A)                                     [then blind]
```

This is much stronger than postulating electromagnetism, but deliberately weaker than claiming it has already been dynamically derived.

## 7. Light and information: the precise ordering

There are two inequivalent meanings of `information`.

If it means the microscopic distinguishable alternative `q=2`, then the ordering is

```text
q=2 alternative
 -> projective state CP1
 -> relative phase / Hopf U1
 -> collective gauge holonomy
 -> photon, only if the U1 Coulomb phase emerges.
```

In that ontic sense **the information-bearing alternative precedes light**.

If `information` means a classical record available to an observer, then

```text
coherent amplitudes
 -> phase propagation
 -> interference
 -> measurement
 -> classical record.
```

In that operational sense light/interference can precede the recorded information.

The compact statement consistent with both is

\[
\boxed{
\text{q=2 alternatives generate phase geometry; interference converts relative phase into observable information.}
}
\]
