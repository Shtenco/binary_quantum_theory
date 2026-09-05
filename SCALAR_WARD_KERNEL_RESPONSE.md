# Scalar Ward-kernel response and pole classifier

Status: **algebraic response/pole consumer closed; theory-specific functions A,B,C remain microscopic physical-history outputs.**

After the exact flat/local Ward quotient, the scalar metric Hessian is represented on

\[
(\mathcal Q,\zeta)
\]

by

\[
H(\omega,k)=
\begin{pmatrix}
A&B\\
B&C
\end{pmatrix}.
\]

In the flat Newtonian-gauge reference,

\[
\mathcal Q=\Psi,
\qquad
\zeta=-\Phi.
\]

The frozen conserved probe supplies one source vector

\[
j=(j_Q,j_\zeta)^T,
\]

and the response equation is

\[
H\begin{pmatrix}\mathcal Q\\\zeta\end{pmatrix}=-j.
\]

## 1. Common denominator

Every scalar response has the same denominator

\[
\boxed{\Delta=AC-B^2.}
\]

Using the adjugate rather than assuming invertibility,

\[
\begin{pmatrix}\mathcal Q\\\zeta\end{pmatrix}
=-\frac1\Delta
\begin{pmatrix}C&-B\\-B&A\end{pmatrix}
\begin{pmatrix}j_Q\\j_\zeta\end{pmatrix}.
\]

Therefore

\[
\Psi
=-\frac{Cj_Q-Bj_\zeta}{\Delta},
\]

\[
\Phi
=\frac{Bj_Q-Aj_\zeta}{\Delta},
\]

up to the frozen sign conventions of the flat reference.

Dynamics and lensing are thus not independently adjustable: `Psi` and `Phi+Psi` share the same kernel and the same source.

## 2. Pole decision tree

The exact algebraic pole condition is

\[
\boxed{\Delta(\omega^2,k^2)=0.}
\]

The production classifier distinguishes:

```text
no omega^2 pole
 -> static/constraint modified-response candidate

simple extra omega^2 pole
 -> compute inverse-kernel residue matrix
 -> test residue sign
 -> test omega^2(k=0) >= 0
 -> extract d omega^2 / d k^2 = c_s^2

negative residue
 -> ghost candidate / reject physical interpretation

negative omega^2 at k=0
 -> tachyon candidate / reject physical interpretation
```

A pole is still not dark matter merely because it exists.  Clustering, source overlap, anisotropic stress, background abundance and lensing/dynamics consistency remain required.

## 3. Exact synthetic controls

`scripts/scalar_ward_kernel_response_gate.py` registers five controls.

### GR-like/static response

\[
A=k^2,\qquad B=0,\qquad C=2k^2
\]

has no `omega^2` pole.

### Modified static response

A deformed static `A,B,C` changes the response but still has no propagating scalar pole.

### Healthy extra scalar

\[
A=k^2,
\qquad B=0,
\qquad C=\omega^2-\frac14k^2-2
\]

gives

\[
\boxed{\omega^2=\frac14k^2+2},
\]

with positive nonzero residue, `m^2=2` and

\[
\boxed{c_s^2=\frac14}.
\]

### Ghost control

Flipping the kinetic sign gives a negative inverse-kernel residue and is detected.

### Tachyon control

Keeping positive kinetic residue while changing the root to

\[
\omega^2=\frac14k^2-2
\]

is detected by negative `omega^2(k=0)`.

These are classifier controls only, not BQG predictions.

## 4. Fail-closed physical interpretation

The analyzer may label its result physical only if the packet certifies:

```text
theory_specific_connected_history
physical_omega_certified
ward_reduction_certified
conserved_probe_frozen
background_and_scale_convention_frozen
```

and supplies hashes for connected history, Ward certificate, source convention and background convention.

Without them it returns

```text
ALGEBRAIC_RESPONSE_ONLY_PHYSICAL_HISTORY_INCOMPLETE
```

regardless of how attractive a pole looks.

## 5. What is now left

The scalar algebra from microscopic response to interpretation is therefore executable:

\[
\boxed{
A,B,C
\to
\Delta=AC-B^2
\to
\Psi,\Phi
\to
\text{poles/residues/stability}
}
\]

The remaining scientific calculation is to obtain the **theory-specific**

\[
\boxed{A(\omega,k),\ B(\omega,k),\ C(\omega,k)}
\]

from the connected physical BQG history with the physical frequency construction and background normalization.
