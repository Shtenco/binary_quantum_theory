# q=2 quantum geometric tensor: distinguishability and phase from one ray space

Status: **exact qubit geometry; dynamical identification of the phase sector with electromagnetism remains conditional.**

The q=2 state space resolves the phrase “information first or light first” without a cosmological storytelling assumption.  Quantum distinguishability geometry and geometric phase are the real and imaginary parts of one projective tensor.

---

## 1. Qubit ray space

Use the normalized Bloch spinor

\[
|\psi(\theta,\phi)\rangle
=\begin{pmatrix}
\cos(\theta/2)\\
e^{i\phi}\sin(\theta/2)
\end{pmatrix}.
\]

Physical pure states are rays, so

\[
S^3/U(1)=\mathbb{CP}^1\simeq S^2.
\]

---

## 2. Quantum geometric tensor

Define

\[
\boxed{
Q_{ab}
=\langle\partial_a\psi|
(1-|\psi\rangle\langle\psi|)
|\partial_b\psi\rangle.
}
\]

Its real part is the Fubini-Study metric,

\[
\boxed{
g_{ab}=\operatorname{Re}Q_{ab}.}
\]

Its antisymmetric imaginary part gives the Berry curvature,

\[
\boxed{F_{ab}=2\operatorname{Im}Q_{ab}}
\]

up to the sign convention associated with `A=-i<psi|d psi>`.

For the Bloch coordinates,

\[
\boxed{
ds_{FS}^2
=\frac14\left(d\theta^2+\sin^2\theta\,d\phi^2\right).
}
\]

The same spinor has Berry/Hopf curvature

\[
\boxed{
F=\frac12\sin\theta\,d\theta\wedge d\phi
}
\]

in the repository's positive Chern convention.

Thus metric distinguishability and compact phase curvature are not two unrelated structures added to the qubit.

---

## 3. Information meaning of the real part

For neighboring rays,

\[
1-|\langle\psi(\lambda)|\psi(\lambda+d\lambda)\rangle|^2
=g_{ab}d\lambda^ad\lambda^b+O(d\lambda^3).
\]

Therefore `Re Q` measures infinitesimal quantum-state distinguishability.

In this precise sense, an information geometry already exists at the kinematic q=2 ray level before any claim that the phase connection is a propagating photon.

---

## 4. Phase meaning of the imaginary part

The Berry connection

\[
A=-i\langle\psi|d\psi\rangle
\]

transforms as a compact `U(1)` connection under local ray rephasing.  Its curvature is the imaginary geometric component above and has

\[
\frac1{2\pi}\int_{S^2}F=1.
\]

This supplies the phase/holonomy carrier used in the compact-U1 construction.

The existence of this connection is kinematic.  The canonical Maxwell/deconfinement gates are required before calling its collective excitation physical light.

---

## 5. Correct causal/conceptual order

Two meanings of “information” must be distinguished.

### Quantum distinguishability information

It is already present in the projective q=2 state geometry:

```text
q=2 ray -> Fubini-Study distinguishability geometry.
```

### Classical accessible information

A record requires dynamics, interaction and measurement.  In a photon branch one possible chain is

```text
q=2 projective information geometry
 -> compact geometric phase
 -> deconfined Maxwell dynamics
 -> propagating light
 -> interference/detection
 -> classical record/information.
```

Thus “light before information” is false if information means microscopic quantum distinguishability, while “light can precede the recorded information it carries” is operationally true.

---

## 6. Why this matters for the candidate theory

The same minimal q=2 object naturally exposes two kinematic faces:

\[
\boxed{
q=2\text{ ray geometry}
\longrightarrow
\begin{cases}
\operatorname{Re}Q & \text{projective/distinguishability geometry},\\
\operatorname{Im}Q & \text{compact phase curvature}.
\end{cases}
}
\]

The gravitational SU(2)/shape-metric construction and the U(1) phase construction are more elaborate descendants and must still be dynamically matched to their physical effective actions.  The QGT identity does not equate the Fubini-Study metric numerically with the emergent spacetime metric.

That last warning is essential: common microscopic ancestry is not permission to identify distinct metrics without a derived map.
