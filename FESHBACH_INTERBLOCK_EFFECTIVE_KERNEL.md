# Exact Feshbach / block-Lanczos reduction of the microscopic constraint operator

Status: **exact operator/spectral definition, not yet the physical history graviton propagator.**  This document defines how Peter–Weyl constraint moments become a controlled coarse **constraint resolvent**.  The separate bridge from Hamiltonian constraints to a physical history effective action is fixed in `HAMILTONIAN_CONSTRAINT_TO_EFFECTIVE_ACTION.md`.

No depth-two moment, no raw overlap and no constraint spectral parameter `z` is silently renamed a physical `omega`-propagator.

---

## 1. Microscopic constraint operator and coarse carrier

Let `H` be a frozen finite-regulator Hermitian constraint operator on a chosen reachable Peter–Weyl habitat.

Let coarse carrier columns form the map `V`.  Their Gram matrix is

\[
K=V^\dagger V.
\]

For `K>0`, define

\[
\boxed{Q_0=VK^{-1/2},\qquad Q_0^\dagger Q_0=I}
\]

and

\[
P_c=Q_0Q_0^\dagger,
\qquad Q_c=I-P_c.
\]

This works for one block or a multi-block carrier.

---

## 2. Exact projected **constraint** resolvent

For spectral parameter `z`,

\[
\boxed{
G_c^{constraint}(z)
=Q_0^\dagger(z-H)^{-1}Q_0.
}
\]

Its inverse

\[
\boxed{
C_c^{constraint}(z)
=[G_c^{constraint}(z)]^{-1}
}
\]

is an exact coarse spectral kernel for `H`.

Unless a relational physical Hamiltonian has been derived, or a history/rigging-map construction has established the correspondence, one must keep

\[
\boxed{z\ne\omega\quad\text{as a physical statement}.}
\]

---

## 3. Exact Feshbach–Schur complement

Block decomposition with respect to `P_c+Q_c=I` gives

\[
\boxed{
C_c^{constraint}(z)
=zI-H_{PP}
-H_{PQ}(zI-H_{QQ})^{-1}H_{QP}.
}
\]

Thus

\[
\Sigma_c(z)=H_{PQ}(zI-H_{QQ})^{-1}H_{QP}.
\]

This is the exact spectral object reconstructed by block-Lanczos or direct reachable-space inversion.

---

## 4. Exact K/A/B identities

For one and the same Hermitian operator `H`, define

\[
K=V^\dagger V,
\qquad
A=V^\dagger HV,
\qquad
B=V^\dagger H^2V=(HV)^\dagger(HV).
\]

Then

\[
\boxed{
A_0=K^{-1/2}AK^{-1/2}
}
\]

and the first block-Lanczos residual obeys

\[
\boxed{
B_1^\dagger B_1
=K^{-1/2}
[B-A^\dagger K^{-1}A]
K^{-1/2}.
}
\]

`scripts/feshbach_block_krylov_identity_gate.py` independently verifies these identities on deterministic finite Hermitian systems.

---

## 5. Continued fraction

After normalizing the first residual and continuing block Lanczos,

\[
H\to
\begin{pmatrix}
A_0&B_1^\dagger&0&\cdots\\
B_1&A_1&B_2^\dagger&\cdots\\
0&B_2&A_2&\cdots\\
\vdots&\vdots&\vdots&\ddots
\end{pmatrix}
\]

and

\[
\boxed{
G_0(z)=
\left[
zI-A_0
-B_1^\dagger
(zI-A_1-B_2^\dagger(\cdots)^{-1}B_2)^{-1}
B_1
\right]^{-1}.
}
\]

A finite depth is a truncation unless convergence / terminator dependence is bounded.

---

## 6. Critical scope correction for the current 72-shard calculation

The current production worker does **not** apply the full refined-complex constraint sum.  It defines the parent-block operator

\[
\boxed{
H_B=\sum_{w\in B}H_w
}
\]

over the 24 fine chambers of one parent tetrahedron and computes

\[
u_e=(1/2)\sum_{c\to e}H_c|\Omega\rangle,
\qquad
v_e=H_Bu_e.
\]

Therefore its matrices are exactly

\[
K=V^\dagger V,
\qquad
A_B=V^\dagger H_BV,
\qquad
B_B=V^\dagger H_B^2V.
\]

They are an exact **local block-constraint Krylov diagnostic**.

They are **not** automatically the first Lanczos blocks of the full global constraint `H_total`, and they are not the 1PI metric Hessian.

This distinction is now frozen in the scientific scope.

---

## 7. Why simply replacing HB by a global sum is also not enough

For a global kinematical reference spin-network, distant local constraint terms can create disconnected excitations unrelated to a local metric insertion.

A raw extensive

\[
V^\dagger H_{total}^2V
\]

would therefore mix connected local propagation with vacuum/disconnected processes unless the physical state/history normalization is treated correctly.

The physical history generating functional

\[
W[J]=-i\hbar\log Z[J]
\]

is the natural object that removes disconnected vacuum factors.

So the path to the physical kernel is not

```text
make H sum larger -> call its resolvent the graviton propagator.
```

It is

```text
constraint local data
 -> physical history/projector + connected metric sources
 -> Gamma[g]
 -> physical K_TT(omega,k).
```

---

## 8. Multi-block Feshbach remains valuable

Within the microscopic constraint analysis, a combined carrier

\[
V=(V_{P_1},V_{P_2},\ldots)
\]

must be Gram-orthonormalized globally before extracting spectral transfer blocks.

A two-block/shared-face calculation should report, for a clearly named **patch constraint** `H_patch`,

```text
K_patch
A_patch = V^dag H_patch V
B_patch = V^dag H_patch^2 V
A0_patch
B1^dag B1_patch
```

and use the exact shared-face `S3` decomposition as a compression/covariance check.

These quantities are valuable microscopic inputs to the history construction and linked-cluster analysis.

---

## 9. From spectral block data to physical omega

The legal chain is

\[
\boxed{
\text{Peter--Weyl constraint moments/resolvents}
\to
\text{history / physical projector or relational deparametrization}
\to
Z[J]
\to W[J]
\to\Gamma[g]
\to K_{TT}(\omega,\mathbf k).
}
\]

`HAMILTONIAN_CONSTRAINT_TO_EFFECTIVE_ACTION.md` defines this bridge and its open measure/state requirements.

Only `K_TT` from that physical construction supplies the poles whose quartic shifts are reconstructed as the six on-shell Wilson coefficients.

---

## 10. Failure tests

Before any quartic microscopic number is called physical, the completed history kernel must pass:

- massless leading TT pole;
- positive common residue;
- common `z~1` leading cone;
- Fierz–Pauli/DeWitt structure;
- no surviving anisotropy at derivative order `<=2`;
- locality/refinement control;
- history/measure and block-Lanczos/truncation stability.

Only then do four-derivative pole coefficients enter the six-Wilson physical prediction.
