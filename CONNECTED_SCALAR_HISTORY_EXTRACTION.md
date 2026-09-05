# Connected scalar history -> Ward kernel

Status: **exact extraction algebra closed; three theory-specific connected physical cumulants remain to be computed.**

The flat/local scalar Ward quotient reduces the metric source space to

\[
(\mathcal Q,\zeta).
\]

Therefore the theory-specific connected physical history does not need to output an arbitrary `4x4` ADM Hessian.  It must supply the symmetric connected source Hessian

\[
G_{conn}(\omega,k)
=
\begin{pmatrix}
G_{QQ}&G_{Q\zeta}\\
G_{Q\zeta}&G_{\zeta\zeta}
\end{pmatrix}
\]

after vacuum-disconnected pieces have been removed and after physical `omega` has been defined by the relational/boundary history construction.

## 1. Exact Legendre inversion

On a nonsingular physical source quotient and in a convention with

\[
\Gamma^{(2)}=(W^{(2)})^{-1},
\]

define

\[
D_G=G_{QQ}G_{\zeta\zeta}-G_{Q\zeta}^2.
\]

Then

\[
\boxed{
A=\frac{G_{\zeta\zeta}}{D_G},
\qquad
B=-\frac{G_{Q\zeta}}{D_G},
\qquad
C=\frac{G_{QQ}}{D_G}.
}
\]

Thus

\[
\boxed{
G_{QQ},G_{Q\zeta},G_{\zeta\zeta}
\longrightarrow
A,B,C
}
\]

is exact and contains no phenomenological ansatz.

## 2. Singular source Hessian is not a dark pole

If

\[
D_G=0,
\]

the extractor refuses to use a Moore--Penrose inverse as a physical propagator.  A singular connected source Hessian means that an exact constraint/gauge/null source direction remains and the source quotient must be reduced further.

This is deliberately consistent with the scalar ADM Dirac engine: pseudoinverting a constraint direction can manufacture a spurious scalar mode.

## 3. Provenance required for a physical kernel

The extractor labels the result physical only when the input certifies:

```text
theory_specific_connected_history
vacuum_disconnected_pieces_removed
physical_omega_certified
ward_source_basis_certified
legendre_hessian_convention_certified
```

and carries hashes for the connected history, Ward basis and history convention.

The resulting `BQG_SCALAR_WARD_KERNEL_V1` packet also requires the already frozen conserved probe and the common background/scale convention before the response/pole analyzer may interpret it physically.

## 4. What may not be substituted

The following objects are useful microscopic inputs but do not satisfy this gate by themselves:

- constraint-resolvent `z` kernels;
- Feshbach spectral transfer with `z` renamed `omega`;
- local normalized j=1 volume trace;
- factorized local source Hessians with zero interblock cumulant;
- static lapse cochains without source-dressed connected history.

The required `omega` is the physical history frequency, not a constraint spectral coordinate.

## 5. Production target after all current algebraic reductions

The scalar microscopic computation is now narrowed to exactly three functions:

\[
\boxed{
G_{QQ}(\omega,k),
\quad
G_{Q\zeta}(\omega,k),
\quad
G_{\zeta\zeta}(\omega,k).
}
\]

Once they are obtained from the same physical BQG history,

\[
G_{conn}
\to
(A,B,C)
\to
\Delta=AC-B^2
\to
\Psi,\Phi
\to
\text{poles/residues/stability}
\]

is fully executable with the committed gates.
