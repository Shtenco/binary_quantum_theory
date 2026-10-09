# BQG scale-free refinement residual theorem

Status: **PROVED finite operator theorem.**

The physical projector of a positive master operator is invariant under any
positive scalar rescaling,

\[
P(M)=P(cM),\qquad c>0.
\]

Therefore a refinement test must not depend on arbitrary engineering
normalizations of \(M_j\) at different representation scales.

Let

\[
M_f\ge0,\qquad M_c\ge0,
\]

with physical projectors \(P_f,P_c\), positive gaps
\(\Delta_f,\Delta_c\), and isometry \(\iota\).

For any \(\rho>0\), define

\[
R_\rho=M_c\iota-\rho\,\iota M_f.
\]

Because \(P_f\) is also the zero projector of \(\rho M_f\), the ordinary
refinement-projector stability theorem applies to the pair
\((\rho M_f,M_c)\):

\[
\boxed{
\|P_c\iota-\iota P_f\|
\le
\frac{\|R_\rho\|}
{\min(\Delta_c,\rho\Delta_f)}.
}
\]

Since this holds for every positive \(\rho\),

\[
\boxed{
\|P_c\iota-\iota P_f\|
\le
\epsilon^{\rm sf}
}
\]

with

\[
\boxed{
\epsilon^{\rm sf}
=
\inf_{\rho>0}
\frac{\|M_c\iota-\rho\,\iota M_f\|}
{\min(\Delta_c,\rho\Delta_f)}.
}
\]

This quantity is invariant under independent positive rescalings

\[
M_f\to aM_f,\qquad M_c\to bM_c.
\]

Indeed, the change is absorbed by
\(\rho\to (b/a)\rho\), while numerator and denominator acquire the same
overall factor \(b\).

A convenient gauge is gap normalization,

\[
\widehat M_f=M_f/\Delta_f,\qquad
\widehat M_c=M_c/\Delta_c,
\]

for which both first positive gaps equal one.  Then one may equivalently
minimize

\[
\boxed{
\epsilon^{\rm sf}
=
\inf_{s>0}
\frac{\|\widehat M_c\iota-s\,\iota\widehat M_f\|}
{\min(1,s)}.
}
\]

This is the canonical BQG refinement-control quantity whenever master
normalization changes with representation scale.

It replaces raw cross-scale operator mismatch as the preferred continuum
diagnostic.
