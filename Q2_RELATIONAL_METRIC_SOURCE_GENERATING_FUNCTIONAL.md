# From the relational projector to a finite metric-source generating functional

## Purpose

The candidate theory must not identify a Hamiltonian-constraint resolvent with a physical frequency propagator.

The legal order is

\[
\text{constraint}
\to P_{\rm phys}
\to Z[J]
\to W[J]
\to \Gamma
\to \Gamma^{(2)}_{\rm metric}.
\]

This note implements that order exactly in the finite q=2 relational positive control built in the preceding projector gate.

It is deliberately **not** yet the physical graviton calculation. Its job is to make the correct source/projector machinery executable before inserting the genuine graph-changing gravitational amplitude.

---

## 1. Physical-history isometry

For the C8 positive control define

\[
V|\psi\rangle
=\frac1{\sqrt8}\sum_{t=0}^{7}
|t\rangle\otimes R^t|\psi\rangle,
\]

with the registered system step `R=J`.

Then

\[
\boxed{V^\dagger V=I}
\]

and

\[
\boxed{VV^\dagger=P_{\rm rel}.}
\]

Thus the invariant physical subspace is exactly isometric to the two-dimensional q=2 geometry carrier in this positive control.

---

## 2. Gauge-invariant relational observables

For any geometry operator `O` define

\[
\boxed{
\mathcal O_{\rm rel}
=\sum_t |t\rangle\langle t|
\otimes R^t O R^{-t}.
}
\]

It obeys

\[
[\mathcal O_{\rm rel},G]=0.
\]

More strongly,

\[
\boxed{
\mathcal O_{\rm rel}V=VO,
}
\]

and hence

\[
\boxed{
V^\dagger\mathcal O_{\rm rel}V=O.
}
\]

So source operators can be inserted **after projection to the constrained physical history** without losing the original q=2 operator algebra.

The gate checks this for the logical `X`, `Y`, and `Z` operators.

---

## 3. Physical source generating functional

Take the q=2 shape source

\[
K(j)=j_X X+j_Z Z.
\]

Because

\[
X^2=Z^2=I,
\qquad
\{X,Z\}=0,
\]

we have

\[
K(j)^2=(j_X^2+j_Z^2)I.
\]

The normalized trace over the two-dimensional physical history sector is therefore

\[
\boxed{
Z(j_X,j_Z)
=\cosh\sqrt{j_X^2+j_Z^2}.
}
\]

Define the connected functional

\[
W(j)=\log Z(j).
\]

At zero source,

\[
\boxed{
\frac{\partial^2W}{\partial j_a\partial j_b}\bigg|_0
=\delta_{ab},
\qquad a,b\in\{X,Z\}.
}
\]

This is a finite exact source-response statement on the projected relational Hilbert space.

---

## 4. Push the connected response into metric components

The frozen q=2 shape-to-metric bridge supplies the two tracefree tangent matrices

\[
M_X=
\begin{pmatrix}
\sqrt3/2&0&\sqrt3/2\\
0&-\sqrt3/2&-\sqrt3/2\\
\sqrt3/2&-\sqrt3/2&0
\end{pmatrix},
\]

\[
M_Z=
\begin{pmatrix}
1/2&1&-1/2\\
1&1/2&-1/2\\
-1/2&-1/2&-1
\end{pmatrix}.
\]

Flattening the full symmetric `3x3` components with the Frobenius inner product gives a `9x2` Jacobian matrix

\[
B=(\mathrm{vec}M_X,\mathrm{vec}M_Z).
\]

Exactly,

\[
\boxed{
B^TB=\frac92 I_2.
}
\]

The zero-source connected metric response is

\[
\boxed{
C_{\rm metric}=BB^T.
}
\]

It has rank two, exactly matching the q=2 logical shape tangent.

Its two nonzero eigenvalues are

\[
\boxed{\lambda_C=\frac92.}
\]

---

## 5. Finite `Gamma^(2)` positive control on the tangent

The Moore–Penrose inverse is

\[
\boxed{
C_{\rm metric}^{+}
=\frac4{81}C_{\rm metric}.
}
\]

The tangent projector is

\[
\boxed{
P_{\rm tangent}
=\frac29C_{\rm metric}.
}
\]

Therefore

\[
C C^+ C=C,
\qquad
C^+ C C^+=C^+,
\]

and

\[
CC^+=C^+C=P_{\rm tangent}.
\]

On the two physical tangent directions the corresponding inverse-response eigenvalue is

\[
\boxed{\lambda_{\Gamma^{(2)}}=\frac29.}
\]

This is a finite source-response positive control, **not** the spacetime graviton inverse propagator.

---

## 6. Why this matters

The formal bridge is now executable in the correct order:

\[
\boxed{
P_{\rm rel}
\to \mathcal O_{\rm rel}
\to Z[J]
\to W[J]
\to C_{\rm metric}
\to C_{\rm metric}^{+}.
}
\]

This avoids the incorrect shortcut

\[
(z-H_{\rm constraint})^{-1}
\stackrel{\text{wrong}}{=}
G(\omega).
\]

The remaining physical task is to replace the registered finite positive control by the genuine gravitational history amplitude.

---

## 7. Physical frontier

To obtain a real graviton prediction we still need:

1. a clock/boundary-history carrier derived from the microscopic q=2 constrained theory;
2. a combined rigging map or boundary amplitude built from the actual graph-changing Euclidean/Lorentzian constraint;
3. metric sources inserted in that physical amplitude;
4. connected interblock/refinement correlators;
5. the continuum/IR physical `Gamma^(2)_metric(omega,k)`;
6. TT projection;
7. extraction of the already preregistered six quartic Wilson coefficients;
8. one common physical scale;
9. blind comparison to external gravitational-wave data.

No physical `omega`, six-Wilson vector, graviton propagator, or `g_YC^gravity` is claimed by this finite gate.
