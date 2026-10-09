# BQG multiplicity-channel spectral selection theorem

Status: **PROVED finite operator theorem.**

Suppose an \(S_4\)-equivariant positive operator \(M_j\) acts on the \([2,2]\)-isotypic sector as

\[
\mathcal H_{22}^{(j)}
\cong
\mathbb C^{m_j}\otimes V_{[2,2]},
\qquad
P_{22}M_jP_{22}=A_j\otimes I_2.
\]

If \(A_j\) has an isolated simple eigenvalue \(\lambda_j\) with normalized eigenvector \(u_j\), then the rank-two subspace

\[
\boxed{
\mathcal L_j
=
\operatorname{span}\{u_j\}\otimes V_{[2,2]}
}
\]

is the unique \(S_4\)-covariant copy selected by that eigenvalue.

No additional basis choice inside the multiplicity space is required.

Let the spectral separation be

\[
\gamma_j
=
\min_{\mu\in\operatorname{spec}(A_j),\ \mu\ne\lambda_j}
|\mu-\lambda_j|.
\]

For a Hermitian perturbation

\[
A_j\to A_j+E_j
\]

with \(\|E_j\|<\gamma_j/2\), the corresponding rank-one multiplicity projector
\(p_j=|u_j\rangle\langle u_j|\) obeys the standard spectral-subspace bound

\[
\boxed{
\|\tilde p_j-p_j\|
\le
\frac{2\|E_j\|}{\gamma_j}.
}
\]

Therefore the selected logical-copy projector

\[
\Pi_{\mathcal L_j}=p_j\otimes I_2
\]

obeys the identical bound

\[
\boxed{
\|\widetilde\Pi_{\mathcal L_j}-\Pi_{\mathcal L_j}\|
\le
\frac{2\|E_j\|}{\gamma_j}.
}
\]

This gives the BQG refinement programme a second independent control ratio:

\[
\boxed{
\eta_j
=
\frac{\|\delta A_j\|}{\gamma_j}.
}
\]

The physical refinement channel is stable when \(\eta_j\to0\), while the physical projector itself is controlled by

\[
\epsilon_j
=
\frac{\|R_j\|}{\Delta_{\min,j}}.
\]

Thus the fast-closure hierarchy becomes

\[
\boxed{
A_j
\to
\gamma_j
\to
\Pi_{\mathcal L_j}
\to
\iota_j
\to
R_j
\to
\epsilon_j
\to
P_\infty.
}
\]

The theorem does not assert which eigenvalue of \(A_j\) is physically selected.
That choice must be fixed by the master/history principle (for example the
lowest physical master channel if that principle is derived and nondegenerate).
