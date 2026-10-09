# BQG projector-only causality no-go

Status: **NO-GO / PROVED finite theorem by explicit counterexample.**

## 1. Question

Can the physical projector block

\[
\Pi_{\Gamma'}P_{\rm phys}\Pi_\Gamma
\]

by itself determine the causal/graph-transition distance between graph sectors?

The answer is no.

The physical projector records the common zero eigenspace of the master constraint. It does not uniquely retain the support graph, locality radius, or shortest-path structure of the nonzero part of the master operator.

---

## 2. Exact counterexample

Consider three graph sectors, one-dimensional for simplicity.

Define the positive path-Laplacian master operator

\[
M_{\rm path}
=
\begin{pmatrix}
1&-1&0\\
-1&2&-1\\
0&-1&1
\end{pmatrix}.
\]

Its support graph is the path

\[
1-2-3,
\]

so

\[
d_{\rm path}(1,3)=2.
\]

Now define

\[
M_{\rm complete}
=
\begin{pmatrix}
2&-1&-1\\
-1&2&-1\\
-1&-1&2
\end{pmatrix}.
\]

Its support graph is the complete graph \(K_3\), so

\[
d_{\rm complete}(1,3)=1.
\]

Both matrices are positive semidefinite.

For \(M_{\rm path}\),

\[
\operatorname{spec}(M_{\rm path})=\{0,1,3\}.
\]

For \(M_{\rm complete}\),

\[
\operatorname{spec}(M_{\rm complete})=\{0,3,3\}.
\]

Both have exactly the same zero eigenspace

\[
\ker M
=
\operatorname{span}\left\{
\frac1{\sqrt3}(1,1,1)^T
\right\}.
\]

Therefore both define the identical physical projector

\[
\boxed{
P_{\rm phys}
=
\frac13
\begin{pmatrix}
1&1&1\\
1&1&1\\
1&1&1
\end{pmatrix}.
}
\]

In particular,

\[
\boxed{
\Pi_3P_{\rm phys}\Pi_1
=
\frac13
}
\]

for both theories.

Yet the causal/support distances differ:

\[
\boxed{
d_{\rm path}(1,3)=2,
\qquad
d_{\rm complete}(1,3)=1.
}
\]

Thus identical physical projector blocks are compatible with different underlying graph-changing causal structures.

---

## 3. Consequence

There cannot exist a universal function

\[
d(\Gamma,\Gamma')
=
F\!\left(
\Pi_{\Gamma'}P_{\rm phys}\Pi_\Gamma
\right)
\]

that reconstructs graph causal distance from the physical projector block alone.

More generally, even the full matrix \(P_{\rm phys}\) is insufficient: the two examples have exactly the same full projector but inequivalent master-support graphs.

Therefore

\[
\boxed{
P_{\rm phys}
\text{ does not uniquely determine causal order.}
}
\]

**Status: NO-GO / PROVED by counterexample.**

---

## 4. What information is lost in the projector limit

The heat kernel retains short-flow order:

\[
K_T=e^{-TM}
=
I-TM+\frac{T^2}{2}M^2-\cdots.
\]

Hence the first nonzero power of \(M\) can encode transition distance.

But

\[
P_{\rm phys}
=
\lim_{T\to\infty}e^{-TM}
\]

retains only the zero spectral subspace.

The nonzero spectrum, locality graph, and perturbative order of graph-sector transitions are discarded.

Therefore the limit

\[
M
\to
P_{\rm phys}
\]

is many-to-one with respect to causal structure.

---

## 5. Correct BQG interpretation

The projector still has the correct role:

\[
P_{\rm phys}
\]

selects physical states/amplitudes.

But causal order must come from additional structure, such as:

1. the local graph-changing constraint/master generator before projection;
2. a derived relational clock/history generator;
3. boundary-history ordering;
4. a continuum/refinement limit that preserves local propagation structure.

Thus the correct architecture is

\[
\boxed{
\{C_A\}
\to
M
\to
\text{local transition order}
\to
P_{\rm phys}
+
\text{relational history}
\to
\text{physical causal histories}.
}
\]

Not

\[
\boxed{
P_{\rm phys}
\to
\text{causality}
}
\]

by itself.

---

## 6. Relation to the graph-changing causal-order theorem

The companion theorem defines

\[
d_M(\Gamma,\Gamma')
=
\min\{n:\Pi_{\Gamma'}M^n\Pi_\Gamma\neq0\}.
\]

That object can distinguish the two examples:

\[
d_M^{\rm path}(1,3)=2,
\]

whereas

\[
d_M^{\rm complete}(1,3)=1.
\]

But their \(P_{\rm phys}\) is identical.

Therefore \(d_M\), or a relational-history descendant of it, is the correct carrier of causal-order information at finite regulator.

---

## 7. Scope

This no-go does not say the physical projector is useless.

It says only:

\[
\boxed{
\text{constraint selection}
\neq
\text{causal ordering}.
}
\]

Both structures are needed.
