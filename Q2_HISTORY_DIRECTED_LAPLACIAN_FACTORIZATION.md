# q=2 directed history as an exact square root of the undirected graph Laplacian

## Scope

This note sharpens the orientation-resolved q=2 history result without promoting the history index to physical time.

The already-derived minimal one-step lift is

\[
W=P_+\otimes U_8+P_-\otimes U_8^{-1},
\qquad
P_\pm=\frac{I\pm Y_L}{2}.
\]

Here `U8` is the minimal reversible eight-state history shift and `Y_L` is the existing logical geometry-orientation pseudoscalar.

The question is whether the oriented one-step dynamics contains a natural first-order operator whose square reproduces the ordinary undirected history graph kernel.

The answer is exact.

---

## 1. Full directed difference

Define

\[
\Delta_W=W-I.
\]

Because `W` is unitary,

\[
\Delta_W^\dagger\Delta_W
=(W^\dagger-I)(W-I)
=2I-W-W^\dagger.
\]

But the orientation-resolved construction already gives

\[
W+W^\dagger
=I_{\rm geom}\otimes(U_8+U_8^\dagger).
\]

Therefore

\[
\boxed{
\Delta_W^\dagger\Delta_W
=I_{\rm geom}\otimes L_h
}
\]

with

\[
\boxed{
L_h=2I-U_8-U_8^\dagger.
}
\]

Since `W` is normal, the reverse product is identical:

\[
\boxed{
\Delta_W\Delta_W^\dagger
=I_{\rm geom}\otimes L_h.
}
\]

Thus the orientation-resolved first-order difference is an exact factor of the orientation-unresolved C8 graph Laplacian.

No continuum approximation is used.

---

## 2. Fourier-character form

On a history character

\[
U_8|\theta\rangle=e^{i\theta}|\theta\rangle,
\]

the orientation-resolved step is

\[
W(\theta)=\cos\theta\,I-\sin\theta\,J,
\]

where

\[
J=-iY_L=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
\qquad
J^2=-I.
\]

Hence

\[
\boxed{
\Delta(\theta)
=(\cos\theta-1)I-\sin\theta\,J.
}
\]

Its positive square is

\[
\boxed{
\Delta(\theta)^T\Delta(\theta)
=4\sin^2\frac{\theta}{2}\,I.
}
\]

But

\[
4\sin^2\frac{\theta}{2}=2-2\cos\theta
\]

is exactly the C8 graph-Laplacian eigenvalue.

---

## 3. Why the odd current alone is insufficient

The Hermitian orientation-odd current is

\[
D=\frac{W-W^\dagger}{2i}
=Y_L\otimes C_h,
\]

with

\[
C_h=\frac{U_8-U_8^\dagger}{2i}.
\]

On a character it has eigenvalue proportional to

\[
\sin\theta.
\]

Therefore

\[
D^2\sim\sin^2\theta.
\]

Exactly,

\[
\boxed{
D^2
=I_{\rm geom}\otimes
\left(L_h-\frac14L_h^2\right).
}
\]

This is not the full graph Laplacian.

On C8 the odd current vanishes both at

\[
\theta=0
\]

and at

\[
\theta=\pi.
\]

The second zero is the standard finite-lattice doubling pattern of a symmetric first-difference operator.

---

## 4. The complete minimal step removes the extra zero automatically

The full forward difference contains both

\[
-\sin\theta\,J
\]

and

\[
(\cos\theta-1)I.
\]

The second term is even under orientation reversal and begins only at second order:

\[
\cos\theta-1=-\frac{\theta^2}{2}+O(\theta^4).
\]

But at finite lattice spacing it is crucial.

For the full operator

\[
\Delta(\theta)
=(\cos\theta-1)I-\sin\theta J,
\]

the squared norm is

\[
4\sin^2(\theta/2),
\]

which on C8 has only the trivial zero `m=0`.

So the extra `theta=pi` zero of the pure odd current disappears.

This resembles the role of a Wilson correction algebraically, but no Wilson-fermion action has been derived or inserted. The even term is simply the unavoidable difference between the exact unitary step and the identity.

---

## 5. Small-angle hierarchy

For small history angle,

\[
\Delta(\theta)
=-\theta J-\frac{\theta^2}{2}I+O(\theta^3).
\]

The leading term is first-order and orientation sensitive.

The first scalar correction is second order.

Meanwhile

\[
\Delta^\dagger\Delta
=\theta^2I+O(\theta^4).
\]

Therefore the exact finite history system has the hierarchy

\[
\boxed{
\text{directed first order}
\quad\longrightarrow\quad
\text{undirected second order}
}
\]

already at the algebraic level.

This is stronger than simply observing that a cosine kernel has a quadratic expansion: the first-order oriented factor is explicitly known.

---

## 6. What is and is not established

### Exact

- the minimal orientation-resolved q=2 history step `W`;
- the real complex structure `J^2=-I`;
- the directed difference `Delta_W=W-I`;
- the exact factorization

\[
\Delta_W^\dagger\Delta_W=I\otimes L_h;
\]

- the C8 character spectrum;
- the extra `theta=pi` zero of the pure odd current;
- the absence of that extra zero in the complete forward difference.

### Not established

- that the history label is physical time;
- that `Delta_W` is the physical Dirac operator;
- that the q=2 orientation doublet is a fermion;
- spin statistics;
- a physical mass term;
- Standard-Model matter;
- a physical dispersion relation.

A legitimate physical-time or covariant-history construction is still required before any of those interpretations become physical claims.

---

## 7. Why this matters for the next frontier

The current structural chain now contains an exact factorization pattern:

\[
q=2
\to Y_L
\to W
\to J^2=-I
\to \Delta_W
\to \Delta_W^\dagger\Delta_W=L_h.
\]

So if a future physical projector or relational clock maps the microscopic history step to a true propagation generator, the correct candidate first-order object is not the odd current alone. It is the complete directed difference `W-I`, because only that object squares exactly to the undirected graph Laplacian and avoids the finite-lattice extra zero.

That physical identification remains open and must be tested rather than assumed.
