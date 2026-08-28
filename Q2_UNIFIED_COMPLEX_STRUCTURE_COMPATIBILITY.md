# One q=2 real complex structure across history, phase weight and quantum realification

## Result

Several previously separate q=2 constructions now use the same exact real matrix

\[
\boxed{
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad J^2=-I.
}
\]

The cross-layer audit checks that this `J` is simultaneously the one appearing in:

1. the oriented C4 arithmetic/complex bridge;
2. the orientation-resolved history Fourier block;
3. the unique quadratic phase-invariant weight;
4. the realification of finite-dimensional complex Hermitian dynamics;
5. the exact directed-history Laplacian factorization.

No new matrix is introduced to identify these sectors.

## Sign convention

There is one deliberate convention distinction.

Standard realification of multiplication by

\[
e^{+i\theta}
\]

is

\[
\exp(+\theta J).
\]

The current history-forward convention gives

\[
W(\theta)=\exp(-\theta J),
\]

which corresponds to the conjugate scalar phase

\[
e^{-i\theta}.
\]

This is exactly the global orientation choice already left free by the minimal history theorem. Reversing history orientation

\[
U\leftrightarrow U^\dagger
\]

sends

\[
\theta\to-\theta
\]

and exchanges the two conventions.

Thus the carrier `J` agrees exactly; only the name assigned to the forward orientation fixes the overall sign of the generator.

## Quadratic weight

For a real symmetric quadratic form

\[
Q(v)=v^TAv,
\]

invariance under the same quarter-turn

\[
J^TAJ=A
\]

forces

\[
A=\lambda I.
\]

Positivity and the normalization `Q(1,0)=1` give

\[
\boxed{Q(v)=v^Tv=|z|^2.}
\]

Both `exp(+theta J)` and `exp(-theta J)` preserve this form, so the forward-orientation sign convention cannot affect the quadratic weight.

This remains a **Born-weight precursor**, not a derivation of the full Born measurement rule.

## Real quantum representation

The existing realification theorem uses

\[
J_n=\begin{pmatrix}0&-I_n\\I_n&0\end{pmatrix}.
\]

For `n=1`, this is exactly the same q=2 matrix `J`.

Hence the real representation of

\[
i\dot\psi=H\psi
\]

uses the same local complex structure as the q=2 history/phase carrier. This is a representation compatibility result only; the physical Hamiltonian and physical time are still open.

## Directed history

The exact directed difference may be written in either orientation convention as

\[
\Delta_\pm(\theta)
=(\cos\theta-1)I\pm\sin\theta J.
\]

Both satisfy

\[
\boxed{
\Delta_\pm^T\Delta_\pm
=4\sin^2(\theta/2)I.
}
\]

Therefore the orientation sign changes the first-order generator but not the scalar graph-Laplacian square.

## Claim boundary

The exact closure is now

\[
q=2\ C_4
\to J^2=-I
\to SO(2)\simeq U(1)
\to |z|^2\text{ quadratic invariant}
\]

and independently

\[
J
\to \text{realification of complex finite-dimensional dynamics},
\]

while the history construction selects the same `J` up to the global forward-orientation convention.

Still open:

- physical history/projector measure;
- physical time;
- physical Hamiltonian;
- full Born outcome rule;
- matter/fermion interpretation;
- experimental validation.
