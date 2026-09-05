# Exact flat scalar ADM Ward quotient

Status: **flat/local scalar diffeomorphism quotient closed algebraically; FLRW/background-dependent physical scalar reduction remains open.**

This result advances the scalar ADM frontier without inserting new microscopic dynamics.

Use the linear scalar metric variables

\[
x=(\delta N,\,B,\,\zeta,\,E)
\]

with

\[
h_{00}=-2\delta N,
\qquad
h_{0i}=\partial_iB,
\qquad
h_{ij}=2\zeta\delta_{ij}+2\partial_i\partial_jE.
\]

On a flat local background, for scalar diffeomorphism parameters `(T,L)` and a formal time derivative `D`, choose the linear convention

\[
\delta(\delta N)=-DT,
\]

\[
\delta B=T-DL,
\]

\[
\delta\zeta=0,
\qquad
\delta E=-L.
\]

## 1. Exact quotient coordinates

Two independent gauge-invariant combinations remain:

\[
\boxed{
\mathcal Q=\delta N+DB-D^2E
}
\]

and

\[
\boxed{\zeta.}
\]

The quotient map is therefore

\[
\begin{pmatrix}\mathcal Q\\\zeta\end{pmatrix}
=
\begin{pmatrix}
1&D&0&-D^2\\
0&0&1&0
\end{pmatrix}
\begin{pmatrix}\delta N\\B\\\zeta\\E\end{pmatrix}.
\]

`scripts/scalar_adm_ward_basis_gate.py` verifies exactly that this map annihilates both scalar gauge generators.

## 2. Ten symmetric entries reduce to three functions

A generic symmetric `4x4` scalar Hessian has ten entries.  Imposing the exact Ward condition

\[
KG=0
\]

for both gauge generators leaves a three-dimensional solution space.

Equivalently every Ward-compatible kernel is the pullback of

\[
H_{inv}=\begin{pmatrix}A&B\\B&C\end{pmatrix}
\]

on `(Q,zeta)`:

\[
\boxed{
K=R^TH_{inv}R.
}
\]

Thus the quadratic form is exactly

\[
\boxed{
\Gamma^{(2)}_{scalar}
=A\mathcal Q^2+2B\mathcal Q\zeta+C\zeta^2.
}
\]

The microscopic scalar-history problem therefore does **not** require ten arbitrary functions.  At flat/local quadratic order it requires only

\[
\boxed{
A(\omega,k),\quad B(\omega,k),\quad C(\omega,k).
}
\]

This is a major compression of the production target.

## 3. Newtonian-gauge reference

For `B=E=0` on the flat reference,

\[
\mathcal Q=\delta N=\Psi,
\]

while the metric-sign convention gives

\[
\zeta=-\Phi.
\]

Therefore the final two-by-two invariant kernel is directly the correct type of object from which `Phi/Psi` response can eventually be read after the theory-specific history and constraint conditions are supplied.

This does **not** yet provide the values of `A,B,C`.

## 4. Source Ward identity

A compatible source must have zero overlap with both gauge directions.  Every quotient source is of the form

\[
J=R^T\begin{pmatrix}j_Q\\j_\zeta\end{pmatrix},
\]

and satisfies

\[
\boxed{G^TJ=0.}
\]

This matches the separately frozen conserved external probe convention: conservation of `T^{mu nu}` makes its linear metric source gauge-compatible.

## 5. Negative control

Adding an arbitrary lapse stiffness

\[
\epsilon(\delta N)^2
\]

to an otherwise Ward-compatible kernel produces

\[
KG\ne0.
\]

The CI gate checks this explicitly.  Therefore a future microscopic computation cannot independently assign a lapse mass/stiffness and still claim scalar diffeomorphism closure.

## 6. Relation to the exact q=2 volume seed

The already-derived local kinematic volume source gives

\[
K_{\zeta_V\zeta_V}^{local}=18
\]

for the log-volume coordinate

\[
\zeta_V=\frac13\log(p/p_0).
\]

The Ward quotient tells us where a physicalized version of that volume coordinate must land: in the `C` entry of the invariant `(Q,zeta)` kernel after the physical history fixes the mapping from the kinematic `zeta_V` to the physical scalar response variable.

It is not legal to set `C=18` in `Gamma_scalar(omega,k)` before that history normalization is derived.

## 7. FLRW boundary

On an expanding FLRW background, `zeta` transforms under time reparametrization through the background Hubble rate.  The physical combinations become the appropriate Bardeen/relational variables.  Therefore this result closes the **flat/local Ward quotient**, not the complete FLRW scalar gauge reduction.

The remaining physical target is now more precise:

```text
physical history
 -> derive A(omega,k), B(omega,k), C(omega,k)
 -> impose/solve scalar constraints in the background-dependent quotient
 -> frozen conserved probe
 -> Phi/Psi -> mu_BQG/Sigma_BQG.
```
