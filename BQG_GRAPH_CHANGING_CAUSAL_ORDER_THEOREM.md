# BQG graph-changing causal-order theorem

Status:
- **PROVED**: exact graph-sector short-\(T\) support theorem for the finite master heat kernel.
- **PROVED**: if every elementary constraint changes graph sector by at most one microscopic graph move, then one master step changes graph sector by at most two such moves.
- **PROVED**: exact relational-history locality theorem for a supplied local system step.
- **OPEN**: identification of master-flow parameter \(T\) or any current finite positive-control clock with physical spacetime time of full BQG.

## 1. Graph-sector decomposition

Let

\[
\mathcal H=\bigoplus_{\Gamma}\mathcal H_\Gamma,
\qquad
\Pi_\Gamma:\mathcal H\to\mathcal H_\Gamma
\]

be a finite regulated graph-sector decomposition.

Let

\[
\boxed{
M=C_A^\dagger G^{AB}C_B\ge0
}
\]

be the finite master constraint, with \(G>0\).

The graph-sector heat kernel is

\[
\boxed{
K_T(\Gamma',\Gamma)
=
\Pi_{\Gamma'}e^{-TM}\Pi_\Gamma.
}
\]

Expanding,

\[
K_T(\Gamma',\Gamma)
=
\sum_{n=0}^{\infty}
\frac{(-T)^n}{n!}
\Pi_{\Gamma'}M^n\Pi_\Gamma.
\]

Therefore graph-changing order is encoded in powers of the actual master operator, not in an externally chosen transition probability.

---

## 2. Exact master-transition distance

Define the block-support graph of \(M\):

\[
\Gamma\sim_M\Gamma'
\quad\Longleftrightarrow\quad
\Pi_{\Gamma'}M\Pi_\Gamma\neq0.
\]

Let \(d_{\mathrm{supp}(M)}(\Gamma,\Gamma')\) be shortest-path distance in that support graph.

Because multiplication by one \(M\) can traverse at most one support-graph edge,

\[
\boxed{
\Pi_{\Gamma'}M^n\Pi_\Gamma=0
\qquad
n<d_{\mathrm{supp}(M)}(\Gamma,\Gamma').
}
\]

Hence

\[
\boxed{
\partial_T^nK_T(\Gamma',\Gamma)\big|_{T=0}=0
\qquad
n<d_{\mathrm{supp}(M)}(\Gamma,\Gamma').
}
\]

Define the exact operator transition distance

\[
\boxed{
d_M(\Gamma,\Gamma')
=
\min\left\{
n:
\Pi_{\Gamma'}M^n\Pi_\Gamma\neq0
\right\}.
}
\]

Then

\[
\boxed{
d_M(\Gamma,\Gamma')
=
\min\left\{
n:
\partial_T^nK_T(\Gamma',\Gamma)|_{T=0}\neq0
\right\}.
}
\]

Always,

\[
\boxed{
d_M\ge d_{\mathrm{supp}(M)}.
}
\]

Equality holds whenever the sum of shortest block-operator products does not cancel.

For generic sign/phase-indefinite graph-changing amplitudes cancellation is possible, so equality must not be assumed without checking the actual operator blocks.

This is the graph-changing analogue of the earlier fixed-graph dynamical-distance theorem.

---

## 3. Elementary constraint-move graph

Now define a finer graph \(G_C\) from elementary constraint support.

Say that two sectors are one microscopic constraint move apart when for at least one \(A\),

\[
\Pi_{\Lambda}C_A\Pi_\Gamma\neq0.
\]

Assume the declared regulator has locality radius one in this graph:

\[
\boxed{
\Pi_{\Lambda}C_A\Pi_\Gamma=0
\quad\text{if}\quad
d_C(\Gamma,\Lambda)>1.
}
\]

This is exactly the statement that one elementary constraint action changes the abstract graph by at most one registered microscopic graph move.

---

## 4. Master constraint can move at most two elementary graph steps

Insert a resolution of graph sectors into one master block:

\[
\Pi_{\Gamma'}M\Pi_\Gamma
=
\sum_{A,B,\Lambda}
G^{AB}
\Pi_{\Gamma'}C_A^\dagger\Pi_\Lambda
C_B\Pi_\Gamma.
\]

A nonzero term requires

\[
d_C(\Gamma,\Lambda)\le1
\]

and

\[
d_C(\Lambda,\Gamma')\le1.
\]

By the triangle inequality,

\[
d_C(\Gamma,\Gamma')\le2.
\]

Therefore

\[
\boxed{
\Pi_{\Gamma'}M\Pi_\Gamma=0
\qquad
d_C(\Gamma,\Gamma')>2.
}
\]

Iterating \(n\) master factors gives

\[
\boxed{
\Pi_{\Gamma'}M^n\Pi_\Gamma=0
\qquad
d_C(\Gamma,\Gamma')>2n.
}
\]

Equivalently,

\[
\boxed{
d_M(\Gamma,\Gamma')
\ge
\left\lceil
\frac{d_C(\Gamma,\Gamma')}{2}
\right\rceil.
}
\]

This statement is exact and does not depend on positivity of individual off-diagonal blocks or on absence of phase cancellation.

---

## 5. Short-\(T\) graph-changing causal order

Let

\[
d_C=d_C(\Gamma,\Gamma').
\]

Then all Taylor coefficients below

\[
n_*=\left\lceil d_C/2\right\rceil
\]

vanish:

\[
\boxed{
K_T(\Gamma',\Gamma)
=
O\left(T^{\lceil d_C/2\rceil}\right).
}
\]

More explicitly,

\[
\boxed{
\partial_T^nK_T(\Gamma',\Gamma)|_{T=0}=0
\quad
\forall n<\lceil d_C/2\rceil.
}
\]

This is a strict graph-changing locality hierarchy.

It says that the master-projector flow cannot connect sectors arbitrarily far away at arbitrarily low perturbative order.

**Important:** \(T\) is still constraint/projector flow, not automatically physical time.

---

## 6. Why \(P_{\rm phys}\) alone does not define causal ordering

The physical projector is

\[
P_{\rm phys}
=
\lim_{T\to\infty}e^{-TM}.
\]

The block

\[
\Pi_{\Gamma'}P_{\rm phys}\Pi_\Gamma
\]

is a coherent physical amplitude between graph sectors, but the \(T\to\infty\) limit does not retain an external temporal ordering.

Therefore the correct separation is

\[
\boxed{
M
\to
\text{short-flow graph-changing locality}
}
\]

and

\[
\boxed{
P_{\rm phys}
\to
\text{physical constraint-selected amplitude}.
}
\]

A spacetime causal interpretation requires a relational/boundary history construction.

---

## 7. Relational-history upgrade

Suppose a derived relational model has clock states \(|t\rangle\) and a system step \(R\), with history state

\[
|\Psi\rangle
=
\frac1{\sqrt N}
\sum_t
|t\rangle\otimes R^t|\psi_0\rangle.
\]

Let graph sectors satisfy

\[
\Pi_{\Gamma'}R\Pi_\Gamma=0
\quad\text{when}\quad
d_R(\Gamma,\Gamma')>1.
\]

Then by exactly the same path-support argument,

\[
\boxed{
\Pi_{\Gamma'}R^t\Pi_\Gamma=0
\qquad
t<d_R(\Gamma,\Gamma').
}
\]

Therefore the conditioned relational amplitude obeys

\[
\boxed{
\langle\Gamma'|\psi(t)\rangle=0
\qquad
t<d_R(\Gamma,\Gamma')
}
\]

for an initial state supported in \(\Gamma\).

This is a genuine causal-order statement with respect to the supplied relational clock.

**Status: PROVED as a finite relational theorem.**

For BQG, the missing step is to derive \(R\) or the corresponding relational generator from the actual graph-changing constraints/projector rather than insert it as a positive control.

---

## 8. Finite regression

The accompanying gate constructs random finite graph-sector Hilbert spaces with:

- sector graph a line;
- sector dimension \(2\);
- several random constraints;
- every \(C_A\) containing only onsite and nearest-sector blocks;
- arbitrary complex coefficients;
- positive master metric \(G\).

It verifies:

1. every one-step master block beyond elementary distance \(2\) vanishes;
2. every \(M^n\) block beyond elementary distance \(2n\) vanishes;
3. the first nonzero block order is never below \(\lceil d_C/2\rceil\);
4. for generic random instances the lower bound is saturated throughout the tested sector line;
5. a local relational step \(R\) cannot connect graph sectors before graph distance many clock ticks.

The numerical test is a regression of the theorem, not its proof.

---

## 9. Consequence for the BQG causal programme

The causal hierarchy is now

\[
\boxed{
\text{elementary graph-changing constraints }C_A
\to
M=C^\dagger G C
\to
d_M
\to
K_T(\Gamma',\Gamma)
}
\]

with the exact lower bound

\[
\boxed{
d_M
\ge
\left\lceil d_C/2\right\rceil.
}
\]

The physical-history target is

\[
\boxed{
P_{\rm phys}
\to
\text{derived relational graph step/generator}
\to
\text{conditioned graph histories}
\to
\text{causal cone}.
}
\]

This is the first exact bridge in the repository from graph-changing constraint locality to graph-history causal order.

---

## 10. Scope boundary

What is now proved:

\[
\boxed{
\text{local graph-changing constraints}
\Rightarrow
\text{finite-order graph-sector propagation bound}.
}
\]

What is not yet proved:

\[
\boxed{
\text{full BQG}
\Rightarrow
\text{Lorentzian spacetime causal cone}.
}
\]

Still open:

- actual converged K5 graph-sector master blocks;
- theory-specific relational clock;
- continuum/refinement limit of the history generator;
- isotropic macroscopic causal cone;
- equality of gravity, photon and matter cones.
