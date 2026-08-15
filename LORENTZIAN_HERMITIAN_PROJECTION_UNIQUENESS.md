# Lorentzian Hermitian projection uniqueness certificate

## Statement

Let the phase-completed raw finite-cutoff operator be

\[
A=-iL_{raw}.
\]

On every finite Peter-Weyl cutoff block, `End(H)` is a real Hilbert space with Hilbert-Schmidt inner product and has the unique direct-sum decomposition

\[
\operatorname{End}(\mathcal H)
=\operatorname{Herm}(\mathcal H)\oplus\operatorname{AntiHerm}(\mathcal H).
\]

The components are

\[
A_H=\frac{A+A^\dagger}{2},\qquad
A_A=\frac{A-A^\dagger}{2}.
\]

Therefore the unique linear projection whose range is the Hermitian subspace and whose kernel is the anti-Hermitian subspace is

\[
\boxed{P_H(A)=\frac{A+A^\dagger}{2}}.
\]

For `A=-iL_raw`,

\[
\boxed{
P_H(-iL_{raw})
=-\frac{i}{2}(L_{raw}-L_{raw}^\dagger)
=S.
}
\]

Thus the v1.2 Hermitian completion is not an arbitrary interpolation.

## Closest-point property

Hermitian and anti-Hermitian subspaces are orthogonal with respect to the real Hilbert-Schmidt inner product. For every Hermitian `X`,

\[
\|A-(A_H+X)\|_{HS}^2
=\|A_A\|_{HS}^2+\|X\|_{HS}^2.
\]

Hence

\[
\boxed{A_H=\arg\min_{H=H^\dagger}\|A-H\|_{HS}}.
\]

The minimizer is unique.

## Covariance and fixed points

For every unitary frame transformation `U`,

\[
P_H(UAU^\dagger)=UP_H(A)U^\dagger.
\]

Also

\[
P_H(H)=H\quad(H^\dagger=H),
\qquad
P_H(K)=0\quad(K^\dagger=-K).
\]

Therefore the projection preserves already-correct Hermitian sectors and cannot introduce a preferred frame.

## Exact boundary of the result

This closes **uniqueness of the minimal Hermitian projection of the already-defined raw operator**. It does not prove that no different microscopic factor ordering, chosen before constructing `L_raw`, could define another Hermitian quantization with the same classical limit. That broader quantization-ordering uniqueness remains an extension problem.
