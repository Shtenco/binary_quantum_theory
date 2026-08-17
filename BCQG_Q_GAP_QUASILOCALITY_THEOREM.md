# BCQG Q-gap -> quasi-local Schur-complement theorem

**Status:** exact conditional operator theorem. It does **not** assert that the BCQG collective eliminated sector is already gapped; the gap is the direct remaining science input.

## 1. Setting

Let

\[
P=W_gW_g^\dagger,\qquad Q=I-P,
\]

and let the collective constraint operator on one refinement level be self-adjoint and finite-range on the block graph,

\[
C=C^\dagger.
\]

On the homogeneous six-metric carrier the already frozen symmetry theorem gives

\[
PCP=0
\]

for the direct gravitational block. The exact zero-energy Schur/Feshbach return is therefore

\[
C_{\rm eff}(0)=-PCQ\,(QCQ)^{-1}QCP
\]

whenever the coupled eliminated block is invertible.

Write

\[
A=QCQ.
\]

Assume the **measured** eliminated spectrum obeys

\[
\sigma(A)\subset[-M,-\delta]\cup[\delta,M],
\qquad 0<\delta\le M<\infty,
\]

and that `A` has graph interaction range `R`.

No GR coefficient, DeWitt value, HDA residual or continuum target enters these assumptions.

## 2. Exact convergent inverse expansion

Since

\[
\delta^2I\le A^2\le M^2I,
\]

define

\[
c=\frac{M^2+\delta^2}{2},\qquad
D=I-\frac{A^2}{c}.
\]

Then

\[
\|D\|\le q,
\qquad
\boxed{q=\frac{M^2-\delta^2}{M^2+\delta^2}<1}.
\]

Hence

\[
(A^2)^{-1}=\frac1c\sum_{n=0}^{\infty}D^n
\]

and therefore

\[
\boxed{
A^{-1}=\frac{A}{c}\sum_{n=0}^{\infty}D^n.
}
\]

For the truncation

\[
A_N^{-1}=\frac{A}{c}\sum_{n=0}^{N}D^n
\]

the operator-norm error obeys

\[
\begin{aligned}
\|A^{-1}-A_N^{-1}\|
&\le \frac{\|A\|}{c}\frac{q^{N+1}}{1-q}\\
&\le \boxed{\frac{M}{\delta^2}q^{N+1}},
\end{aligned}
\]

because `c(1-q)=delta^2` exactly.

## 3. Exponential spatial decay

If `A` has graph range `R`, then `A^2` has range at most `2R`, `D^n` has range at most `2nR`, and

\[
A D^n
\]

has range at most

\[
(2n+1)R.
\]

Therefore, for states/local basis vectors `|x>`,`|y>` with graph distance

\[
d(x,y)>(2N+1)R,
\]

the truncated inverse has exactly zero matrix element,

\[
\langle x|A_N^{-1}|y\rangle=0,
\]

so the exact inverse satisfies

\[
\boxed{
|\langle x|A^{-1}|y\rangle|
\le
\frac{M}{\delta^2}
q^{N+1}.
}
\]

Choosing the largest `N` allowed by the distance gives exponential decay in `d/R`.

Thus a uniformly nonzero eliminated-sector gap implies a uniformly quasi-local resolvent.

## 4. Consequence for the collective effective constraint

If `PCQ` and `QCP` inherit finite range from the microscopic/block constraint, then

\[
C_{\rm eff}(0)=-PCQ A^{-1}QCP
\]

also has exponentially decaying couplings away from the metric block.

Therefore the old broad IR hypothesis

> “the blocked scalar becomes local enough for a derivative expansion”

can be replaced by a much sharper direct test:

\[
\boxed{
\inf_l \delta_l>0
}
\]

on every mode placed in the eliminated `Q_l` sector, together with an explicit check that no additional gapless irreducible representation was incorrectly eliminated.

If a zero or asymptotically gapless `Q` mode couples to `P`, it must be promoted into the low-energy carrier before applying the theorem; adding a regulator mass or tuning the resolvent is forbidden.

## 5. Relation to the IR universality theorem

The already frozen `BCQG_IR_UNIVERSALITY_CLOSURE_THEOREM.md` states that a nondegenerate 3D metric carrier + local two-derivative scalar + first-class HDA + complete regular constraints selects ADM/GR (up to `G`, `Lambda`, boundary terms and irrelevant corrections).

This theorem supplies a target-independent route to the locality part:

\[
\boxed{
\text{finite-range microscopic }C
+\text{uniform eliminated }Q\text{-gap}
\Longrightarrow
\text{quasi-local }C_{\rm eff}.
}
\]

A derivative expansion then concerns the remaining long-wavelength low-energy `P` fields rather than an arbitrary nonlocal inverse.

## 6. What remains to measure

This is an implication theorem, not a BCQG gap measurement. The required science producer must report, across refinement levels:

1. the smallest nonzero singular/eigenvalue `delta_l` of the coupled `Q_l C_l Q_l` block;
2. an upper spectral bound `M_l`;
3. which `S4`/collective irreps approach zero;
4. whether every gapless coupled irrep has already been included in `P_l`;
5. the induced quasi-local decay or the bound above.

No target value `c_DeWitt=1/2` may be used to select the `P/Q` split.
