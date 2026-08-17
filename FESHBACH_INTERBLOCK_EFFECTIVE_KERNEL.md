# Exact Feshbach / block-Lanczos definition of the coarse gravitational kernel

Status: **exact operator definition.**  This document closes the semantic gap between finite Peter–Weyl moments and the frequency-dependent coarse kernel.  No depth-two moment is renamed an effective action by itself.

---

## 1. Start with the microscopic Hamiltonian and a coarse carrier

Let `H` be the frozen finite-regulator microscopic Hermitian Hamiltonian on the chosen reachable Peter–Weyl habitat.

Let the non-orthonormal coarse metric carrier be stored in the columns of a map `V` from coarse coefficient space into the microscopic Hilbert space.  Its Gram matrix is

\[
K=V^\dagger V.
\]

When `K>0`, define the orthonormalized coarse embedding

\[
\boxed{
Q_0=VK^{-1/2},
\qquad Q_0^\dagger Q_0=I.
}
\]

The corresponding orthogonal projector is

\[
\boxed{
P_c=Q_0Q_0^\dagger,
\qquad Q_c=I-P_c.
}
\]

This definition works for one block or for a multi-block carrier assembled from several neighboring tetrahedra.

---

## 2. Exact projected resolvent

For complex spectral parameter `z` away from the microscopic spectrum, the exact coarse Green function is

\[
\boxed{
G_c(z)=Q_0^\dagger(z-H)^{-1}Q_0.
}
\]

Equivalently, in projector notation it is the representation of

\[
P_c(z-H)^{-1}P_c
\]

inside the orthonormal coarse basis.

Define the coarse inverse propagator / effective kernel by

\[
\boxed{
C_c(z)=G_c(z)^{-1}.
}
\]

No additional definition of an “effective Hamiltonian” is needed.

---

## 3. Exact Feshbach–Schur complement

Block-decompose `z-H` with respect to `P_c+Q_c=I`.

The Schur complement gives exactly

\[
\boxed{
C_c(z)
=zI-H_{PP}
-H_{PQ}(zI-H_{QQ})^{-1}H_{QP},
}
\]

where

\[
H_{PP}=Q_0^\dagger H Q_0,
\]

and the other blocks are the corresponding coarse/complement matrix elements.

Thus the self-energy is

\[
\boxed{
\Sigma_c(z)
=H_{PQ}(zI-H_{QQ})^{-1}H_{QP}.
}
\]

This is the unique exact object that local return amplitudes and interblock transfer amplitudes must approximate/reconstruct.

---

## 4. Relation to the currently computed K/A/B moments

For coarse source columns `V`, define

\[
K=V^\dagger V,
\]

\[
A=V^\dagger H V,
\]

\[
B=(HV)^\dagger(HV)=V^\dagger H^2V.
\]

Then the first block-Lanczos diagonal block is

\[
\boxed{
A_0=Q_0^\dagger H Q_0
=K^{-1/2}AK^{-1/2}.
}
\]

The first residual is

\[
R_1=(I-P_c)HQ_0.
\]

Therefore

\[
R_1^\dagger R_1
=Q_0^\dagger H(I-P_c)HQ_0.
\]

Substituting `Q0=V K^-1/2` gives the exact identity

\[
\boxed{
B_1^\dagger B_1
=K^{-1/2}
\left[
B-A^\dagger K^{-1}A
\right]
K^{-1/2}.
}
\]

For Hermitian `H` and an exactly assembled `A`, `A=A^dagger` up to numerical tolerance.

This is the correct meaning of the current onsite depth-two `K/A/B` calculation: it determines `A0` and the positive first leakage/return block `B1^dag B1` of the exact coarse resolvent.

It does **not** by itself determine the complete frequency dependence.

---

## 5. Block-Lanczos continued fraction

Normalize the residual to obtain the next orthonormal block `Q1`, continue the block-Lanczos recursion, and obtain

\[
H\;\longrightarrow\;
\begin{pmatrix}
A_0&B_1^\dagger&0&\cdots\\
B_1&A_1&B_2^\dagger&\cdots\\
0&B_2&A_2&\cdots\\
\vdots&\vdots&\vdots&\ddots
\end{pmatrix}.
\]

Then the exact projected resolvent has the matrix continued fraction

\[
\boxed{
G_0(z)=
\left[
 zI-A_0
-B_1^\dagger
 \left(zI-A_1-B_2^\dagger(\cdots)^{-1}B_2\right)^{-1}
 B_1
\right]^{-1}.
}
\]

The previously completed local logical higher-shell calculation is a special parity-graded example of this same construction.

A finite Lanczos truncation is a controlled approximation only when convergence / terminator dependence is explicitly checked.  A depth-two truncation must never be labelled exact full `C(z)`.

---

## 6. Multi-block carrier and spatial momentum

For physical propagation, assemble coarse edge/metric carriers on several PL blocks:

\[
V=(V_{P_1},V_{P_2},\ldots).
\]

The combined Gram matrix includes interblock overlaps and is orthonormalized **globally** on the chosen local patch before Feshbach projection.

The exact patch kernel is

\[
C_{PQ}(z).
\]

In a translation-like scaling window, or more generally in a locally reconstructed tangent frame with controlled normal modes, form the spatial symbol

\[
\boxed{
C(z,\mathbf k)
=\sum_{\delta}C^{(\delta)}(z)e^{i\mathbf k\cdot\mathbf r_\delta}
}
\]

or the corresponding discrete normal-mode representation when no exact translational symmetry is assumed.

This order matters:

```text
microscopic H
 -> multi-block coarse embedding V
 -> exact/global Gram orthonormalization
 -> Feshbach / converged block-Lanczos kernel C_PQ(z)
 -> local momentum or normal-mode symbol
 -> metric / TT projection
 -> derivative expansion
 -> six quartic Wilson coefficients.
```

A raw overlap matrix is not a propagator.

---

## 7. Frequency variable and Lorentzian continuation

The Euclidean Peter–Weyl Hamiltonian computation produces a resolvent in the spectral variable `z`.

The physical Lorentzian pole prescription must be fixed consistently with the repository's Lorentzian Hamiltonian/HDA construction before identifying

\[
z\leftrightarrow\omega+i0
\]

or an equivalent transfer-time variable.

The reduced TT kernel already supplies a positive-control convention.  The full microscopic branch must reproduce the leading massless Einstein pole before quartic coefficients are declared physical.

---

## 8. Exact failure tests before any quartic prediction

The coarse physicalization fails if the converged/Feshbach kernel has any of the following after the declared continuum/refinement extrapolation:

- nonzero TT mass not already permitted by the target theory;
- negative physical residue / ghost pole;
- unstable or regulator-dependent leading light cone;
- anisotropic order-`k^2` pole splitting that does not vanish in the IR;
- substantial dependence on the block-Lanczos terminator at the claimed extraction scale;
- nonlocal transfer tails that do not decrease with block separation.

Only after these gates pass are order-`k^4` Wilson coefficients interpreted as irrelevant physical corrections.

---

## 9. Minimal production consequence

The current 72-shard onsite calculation provides the exact ingredients for the first local block-Lanczos step.

The nearest-block calculation should therefore **not** merely compute six arbitrary cross overlaps.  It should construct the combined two-block carrier and report at minimum

```text
K_patch = V^dag V
A_patch = V^dag H V
B_patch = V^dag H^2 V
A0_patch
B1^dag B1_patch
```

with the shared-face `S3` decomposition used as an exact compression/consistency check.

Subsequent shells or a direct reachable-space resolvent then determine the frequency-dependent six-edge block kernel.

This gives a precise operator meaning to every future `C6(omega,k)` coefficient.
