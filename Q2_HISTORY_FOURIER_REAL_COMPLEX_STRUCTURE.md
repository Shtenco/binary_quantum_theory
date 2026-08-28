# q=2 history Fourier phase is the real complex-structure rotation

The minimal orientation-resolved q=2 history lift is

\[
W=P_+\otimes U+P_-\otimes U^{-1},
\qquad
P_\pm=\frac{I\pm Y_L}{2}.
\]

Take one character of the history shift,

\[
U|\theta\rangle=e^{i\theta}|\theta\rangle.
\]

On that sector the geometry block is

\[
\begin{aligned}
W(\theta)
&=P_+e^{i\theta}+P_-e^{-i\theta}\\
&=\cos\theta\,I+i\sin\theta\,Y_L.
\end{aligned}
\]

Now define

\[
\boxed{J=-iY_L.}
\]

Because

\[
Y_L=\begin{pmatrix}0&-i\\i&0\end{pmatrix},
\]

we obtain the ordinary real matrix

\[
\boxed{
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad J^2=-I.
}
\]

Therefore

\[
\boxed{
W(\theta)=\cos\theta I-\sin\theta J=e^{-\theta J}.
}
\]

So the complex Fourier phase of the oriented history and the real q=2
quarter-turn complex structure are not two unrelated ingredients.  They are the
same rotation written in two representations.

The group law is ordinary real rotation composition:

\[
W(\theta_1)W(\theta_2)=W(\theta_1+\theta_2).
\]

If orientation is unresolved, the odd part cancels:

\[
\frac12\operatorname{Tr}_{geometry}W(\theta)=\cos\theta.
\]

At small angle,

\[
\cos\theta=1-\frac{\theta^2}{2}+O(\theta^4),
\]

whereas the orientation-resolved block retains the linear directed term

\[
W(\theta)=I-\theta J+O(\theta^2).
\]

This gives an exact representation-theoretic sense in which forgetting the
orientation removes the first-order directed information and leaves an
undirected cosine kernel.

It is tempting to compare this with first-order/chiral versus second-order wave
structures, but no matter Dirac equation is claimed here.  Likewise the history
character angle is not yet physical frequency: physical time still requires the
separate relational/boundary/projector bridge.
