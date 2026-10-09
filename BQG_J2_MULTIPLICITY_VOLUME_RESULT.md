# First multiplicity-space geometry result: j=2

Status: **FINITE PASS / geometry resolves the first multiplicity ambiguity.**

At \(j=2\),

\[
\dim\mathrm{Inv}_{SU(2)}(V_2^{\otimes4})=5,
\]

and the exact multiplicity theorem gives

\[
m_{[2,2]}=2.
\]

Thus the \([2,2]\) isotypic sector has dimension four,

\[
\mathbb C^2_{\rm mult}\otimes V_{[2,2]}.
\]

For any \(S_4\)-invariant operator \(O\), Schur's lemma implies

\[
\boxed{
O|_{[2,2]\text{-iso}}
=
A_2\otimes I_2.
}
\]

The first test uses the existing absolute-volume operator

\[
V=|Q|^{1/4}.
\]

## Numerical result

The \(S_4\) commutator closes at

\[
\boxed{
\max_{p\in S_4}\|[V,U(p)]\|
=
5.27\times10^{-15}.
}
\]

The restricted \([2,2]\) spectrum is

\[
\boxed{
\operatorname{spec}V|_{[2,2]}
=
\{
1.9850118901300562,
1.9850118901300584,
3.022651919534288,
3.022651919534290
\}.
}
\]

The paired-degeneracy spread is only

\[
\boxed{
2.22\times10^{-15},
}
\]

while the multiplicity-channel splitting is

\[
\boxed{
\Delta V_{\rm mult}
=
1.0376400294042316.
}
\]

Thus the spectrum has exactly the Schur pattern

\[
\boxed{
A_2\otimes I_2
}
\]

with two distinct multiplicity eigenvalues.

## Algebraic pattern

Numerically,

\[
(1.9850118901300573)^4
=
15.52574504128169\ldots
\]

and

\[
(3.022651919534289)^4
=
83.47425495871829\ldots
\]

which match the two roots of

\[
x^2-99x+1296=0,
\]

namely

\[
\boxed{
x_\pm
=
\frac{99\pm9\sqrt{57}}2.
}
\]

So the observed volume eigenvalues are consistent with

\[
V_\pm
=
\left(
\frac{99\pm9\sqrt{57}}2
\right)^{1/4}.
\]

This algebraic identification is recorded as a candidate exact closed form until a separate symbolic recoupling proof is added.

## Interpretation

The first loss of \(S_4\)-uniqueness at \(j=2\) does **not** create an arbitrary basis ambiguity.

The already-existing geometric volume operator resolves the multiplicity space:

\[
\boxed{
\mathbb C^2_{\rm mult}
\to
\{|V_-\rangle,|V_+\rangle\}.
}
\]

Therefore no fitted projector is needed merely to define a canonical multiplicity basis.

The remaining physical question is which multiplicity channel is selected or mixed by the full master/history dynamics.

So the refined fast-closure chain is

\[
\boxed{
S_4\text{ isotypic sector}
\to
\text{volume-resolved multiplicity basis}
\to
A_j^{\rm master}
\to
\iota_j
\to
R_j
\to
\epsilon_j.
}
\]

## Claim boundary

Absolute volume selects a geometric multiplicity basis only.

It does not yet prove that the lower-volume or higher-volume channel is the physical RG trajectory.

That selection must come from the actual master/history dynamics.
