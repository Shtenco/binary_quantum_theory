# BCQG collective HDA structure-function reduction theorem

**Status:** exact norm decomposition for C3.  It reduces the structure-function blocking defect to a diffeomorphism-generator intertwining defect plus a coarse inverse-metric defect.  It does not assert that the production defects are already small.

## 1. Setup

Let

\[
W:\mathcal H_{eff}\to\mathcal H_{fine},\qquad W^\dagger W=I,
\]

and let `I_beta` denote the frozen linear blocking map for shift fields.

The microscopic and effective diffeomorphism generators are linear in their shift argument:

\[
D_f[\beta],\qquad D_c[\beta].
\]

For a lapse pair define the one-form

\[
\omega_b=N\partial_bM-M\partial_bN.
\]

The microscopic and coarse structure functions are

\[
\beta_f^a=Q_f^{ab}\omega_b,
\qquad
\beta_c^a=Q_c^{ab}\omega_b.
\]

The C3 structure-function blocking defect is

\[
\delta_{str}
=\|W^\dagger D_f[\beta_f]W-D_c[\beta_c]\|.
\]

## 2. Exact add-and-subtract decomposition

Insert the blocked microscopic shift:

\[
D_c[I_\beta\beta_f].
\]

Then

\[
\begin{aligned}
\delta_{str}
\le{}&
\|W^\dagger D_f[\beta_f]W-D_c[I_\beta\beta_f]\|\\
&+\|D_c[I_\beta\beta_f-\beta_c]\|.
\end{aligned}
\]

Define the direct diffeomorphism intertwining defect on the actual shift

\[
\boxed{
\delta_D(\beta_f)
=\|W^\dagger D_f[\beta_f]W-D_c[I_\beta\beta_f]\|.
}
\]

Because `D_c` is linear, define its finite operator norm as a map from the frozen shift norm to operators,

\[
\boxed{
L_D=\sup_{\gamma\ne0}
\frac{\|D_c[\gamma]\|}{\|\gamma\|}.
}
\]

Then

\[
\boxed{
\delta_{str}
\le
\delta_D(\beta_f)
+L_D\|I_\beta\beta_f-\beta_c\|.
}
\]

## 3. Metric/structure-function reduction

Let the blocked microscopic inverse-metric map on the declared lapse one-form be compared directly with the independently measured coarse inverse metric.  Define

\[
\Delta Q
=I_Q(Q_f)-Q_c
\]

in the frozen coarse tensor convention, and assume the shift blocking is compatible with the declared tensor blocking so that

\[
I_\beta(Q_f\omega)=I_Q(Q_f)\,\omega.
\]

Then

\[
I_\beta\beta_f-\beta_c
=\Delta Q\,\omega.
\]

Hence

\[
\|I_\beta\beta_f-\beta_c\|
\le
\|\Delta Q\|\,\|\omega\|.
\]

With

\[
\boxed{\delta_Q=\|\Delta Q\|}
\]

we obtain

\[
\boxed{
\delta_{str}
\le
\delta_D+L_D\,\delta_Q\,\|\omega\|.
}
\]

This bound is target-independent.  `Q_c` is measured from the BCQG coarse flux metric, not set to the GR structure function.

## 4. Reduced collective HDA bound

Combining with `COLLECTIVE_HDA_INTERTWINING_THEOREM.md`,

\[
\|[H_{eff}[N],H_{eff}[M]]-i\hbar D_c[\beta_c]\|
\le
\delta_{micro}+2\eta_N\eta_M+\hbar\delta_{str},
\]

gives the directly measurable sufficient bound

\[
\boxed{
\Delta_{HH}^{bound}
\le
\delta_{micro}
+2\eta_N\eta_M
+\hbar\left(
\delta_D+L_D\delta_Q\|\omega\|
\right).
}
\]

Thus C3 does not require one opaque giant number.  Its possible failure mechanisms are separated into:

1. microscopic projected anomaly `delta_micro`;
2. Hamiltonian carrier leakage `eta_N eta_M`;
3. failure of the diffeomorphism generator to intertwine, `delta_D`;
4. failure of the inverse metric/structure function to block correctly, `delta_Q`.

## 5. Rank-three shift consequence

For local lapse pairs

\[
N=1,\qquad M=x^i,
\]

we have

\[
\omega_b=\delta_b^i,
\qquad
\beta^a=Q^{ai}.
\]

If the coarse inverse metric is nondegenerate, its three columns are linearly independent.  Therefore the HDA structure function supplies three independent **shift vectors** automatically.

This does not by itself prove that `D_c` acts faithfully on the retained Hilbert space.  C3 must still verify that the three corresponding operators/actions are independent on held-out perturbations.  Once that faithfulness check passes, the diffeomorphism rank is three; no separate fit to `r_D=3` is needed.

## 6. Production measurements

For every held-out lapse pair and refinement level report:

```text
delta_micro
eta_N
eta_M
delta_D
L_D
delta_Q
||omega||
HDA_bound = delta_micro + 2 eta_N eta_M + hbar*(delta_D + L_D delta_Q ||omega||)
direct_collective_HH_residual
```

The direct collective bracket is retained as an overdetermined held-out check and must satisfy the theorem bound up to the declared numerical tolerance.

No quantity may be tuned using `c_DeWitt=1/2`, the ADM target, or the direct-bracket answer.
