# Uniqueness of the tetrahedral charged-volume completion

Let

\[
q_r\equiv q_{\widehat r},\qquad r=0,1,2,3,
\]

be the four epsilon-contracted triple graspings obtained by omitting one local leg of a four-valent node.  Consider the most general linear continuation

\[
Q(c)=\sum_{r=0}^{3}c_rq_r.
\]

No metric/GR target is used below.

## S4 action

A permutation `pi` of the four local legs maps the omitted label `r` to `pi(r)` and contributes the orientation sign of the induced permutation on the remaining ordered triple.  This defines a real 4-dimensional representation `R(pi)` on the coefficient space of the `q_r`.

A tetrahedral pseudoscalar must satisfy

\[
\boxed{R(\pi)c=\operatorname{sgn}(\pi)c\qquad\forall\pi\in S_4.}
\]

Stacking the linear constraints for all 24 permutations gives a matrix of rank 3. Therefore the sign-representation eigenspace has dimension exactly one.

Its generator is

\[
\boxed{c\propto(1,-1,1,-1).}
\]

Thus, among linear combinations of the four local triple graspings, the only tetrahedrally pseudoscalar charged continuation is

\[
Q\propto\sum_{r=0}^{3}(-1)^rq_{\widehat r}.
\]

The executable gate verifies every permutation identity exactly at the integer representation-matrix level and independently confirms the magnetic-tensor operator covariance to floating-point roundoff.

## Normalization

The remaining overall scale is fixed without GR fitting.  On a Gauss `J=0` four-valent intertwiner closure gives the usual relation among the four triple graspings.  Requiring the absolute volume to agree with the already frozen `q_123` normalization gives

\[
\boxed{
Q_{tet}=\frac14\sum_{r=0}^{3}(-1)^rq_{\widehat r}.
}
\]

Consequently

\[
\boxed{V_{tet}=\sqrt{|Q_{tet}|}}
\]

is permutation-even and inherits the existing zero-aware spectral convention.

## Scope

This is a uniqueness theorem only inside the declared local ansatz: **linear combinations of the four fundamental triple graspings with tetrahedral S4 pseudoscalar covariance and continuity to the frozen Gauss-sector volume normalization**.

It does not claim uniqueness among arbitrary higher-order flux operators or different microscopic quantization prescriptions.
