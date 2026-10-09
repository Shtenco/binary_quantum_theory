# BQG refinement-projector stability theorem

Status: **PROVED exact finite operator theorem.**

This theorem turns a controlled master-constraint intertwining residual directly into a controlled physical-projector intertwining residual.

It is the central analytic bridge needed for the BQG refinement programme.

## 1. Setup

Let

\[
M_d\ge0,\qquad M_{d+1}\ge0
\]

be finite-dimensional positive semidefinite master operators on Hilbert spaces

\[
\mathcal H_d,\qquad \mathcal H_{d+1}.
\]

Let

\[
\iota_d:\mathcal H_d\to\mathcal H_{d+1}
\]

be an isometric embedding,

\[
\iota_d^\dagger\iota_d=I.
\]

Define the finite physical projectors

\[
P_d=\mathbf1_{\{0\}}(M_d),
\qquad
P_{d+1}=\mathbf1_{\{0\}}(M_{d+1}).
\]

Let the first positive master gaps be

\[
\Delta_d
=
\min(\operatorname{spec}M_d\setminus\{0\}),
\]

\[
\Delta_{d+1}
=
\min(\operatorname{spec}M_{d+1}\setminus\{0\}).
\]

Define the refinement residual

\[
\boxed{
R_d
=
M_{d+1}\iota_d-\iota_dM_d.
}
\]

No assumption of exact intertwining is made.

---

# 2. Physical-to-unphysical leakage

Take a coarse physical vector

\[
x=P_dx.
\]

Since

\[
M_dx=0,
\]

we have

\[
M_{d+1}\iota_dx=R_dx.
\]

On the orthogonal complement of the fine physical kernel,

\[
M_{d+1}\ge
\Delta_{d+1}(I-P_{d+1}).
\]

Equivalently the reduced inverse satisfies

\[
\left\|
M_{d+1}^{-1}
\right\|_{\ker(M_{d+1})^\perp}
\le
\frac1{\Delta_{d+1}}.
\]

Hence

\[
(I-P_{d+1})\iota_dP_d
=
M_{d+1,+}^{-1}
(I-P_{d+1})R_dP_d,
\]

and therefore

\[
\boxed{
\|(I-P_{d+1})\iota_dP_d\|
\le
\frac{\|R_d\|}{\Delta_{d+1}}.
}
\]

Thus a coarse physical state remains asymptotically physical after refinement whenever

\[
\|R_d\|/\Delta_{d+1}\to0.
\]

---

# 3. Unphysical-to-physical leakage

Let

\[
Q_d=I-P_d.
\]

Because

\[
P_{d+1}M_{d+1}=0,
\]

left-multiplying the residual identity gives

\[
P_{d+1}R_d
=
-P_{d+1}\iota_dM_d.
\]

On \(Q_d\mathcal H_d\), \(M_d\) is invertible with

\[
\|M_{d,+}^{-1}\|\le\frac1{\Delta_d}.
\]

Therefore

\[
P_{d+1}\iota_dQ_d
=
-P_{d+1}R_dQ_dM_{d,+}^{-1},
\]

so

\[
\boxed{
\|P_{d+1}\iota_d(I-P_d)\|
\le
\frac{\|R_d\|}{\Delta_d}.
}
\]

Thus refinement cannot create a large spurious physical component from a coarse unphysical state when the same residual-to-gap ratio is small.

---

# 4. Exact projector-intertwining bound

Decompose

\[
P_{d+1}\iota_d-\iota_dP_d
=
P_{d+1}\iota_d(I-P_d)
-
(I-P_{d+1})\iota_dP_d.
\]

The two terms act on orthogonal domain subspaces and land in orthogonal codomain subspaces.

Therefore their operator norm combines by a maximum rather than a triangle sum:

\[
\left\|
P_{d+1}\iota_d-\iota_dP_d
\right\|
=
\max\left(
\|P_{d+1}\iota_d(I-P_d)\|,
\|(I-P_{d+1})\iota_dP_d\|
\right).
\]

Using the two leakage bounds,

\[
\boxed{
\left\|
P_{d+1}\iota_d-\iota_dP_d
\right\|
\le
\frac{\|R_d\|}
{\min(\Delta_d,\Delta_{d+1})}.
}
\]

This is the main theorem.

---

# 5. Exact intertwining corollary

If

\[
\boxed{
R_d=0,
}
\]

then immediately

\[
\boxed{
P_{d+1}\iota_d
=
\iota_dP_d.
}
\]

So exact master intertwining implies exact physical-projector cylindrical consistency.

---

# 6. Asymptotic refinement corollary

Define

\[
\epsilon_d
=
\frac{\|R_d\|}
{\min(\Delta_d,\Delta_{d+1})}.
\]

If

\[
\boxed{
\epsilon_d\to0,
}
\]

then

\[
\boxed{
\|P_{d+1}\iota_d-\iota_dP_d\|
\to0.
}
\]

This is precisely the sufficient condition sought in the BQG fast-closure programme.

It is stronger and cleaner than separately comparing zero-mode bases because it controls the physical projector as an operator.

---

# 7. Inductive-limit consequence

Assume coherent isometric embeddings

\[
\iota_{d+1}\iota_d
=
\iota_{d\to d+2},
\]

and assume the accumulated projector mismatch is summable,

\[
\boxed{
\sum_d\epsilon_d<\infty.
}
\]

Then for every vector represented at finite depth, the embedded sequence of physical projections is Cauchy.

Therefore the projectors define a unique bounded projector on the Hilbert inductive limit,

\[
\boxed{
P_\infty
=
\varinjlim P_d,
}
\]

on the dense union of embedded finite-depth spaces, extended by continuity.

Thus a practical sufficient route to a continuum physical projector is

\[
\boxed{
\sum_d
\frac{\|M_{d+1}\iota_d-\iota_dM_d\|}
{\min(\Delta_d,\Delta_{d+1})}
<\infty.
}
\]

This is the sharp target that future BQG refinement calculations should measure.

---

# 8. Why the gap matters

Small raw residual alone is not enough.

If

\[
\Delta_d\to0
\]

faster than \(\|R_d\|\), the physical projector can change strongly under an apparently small operator perturbation.

The scientifically correct refinement diagnostic is therefore not

\[
\|R_d\|\to0
\]

alone, but

\[
\boxed{
\epsilon_d
=
\|R_d\|/\Delta_{\min,d}
\to0.
}
\]

This is now the canonical refinement control parameter.

---

# 9. Relation to BQG

The repository already supplies:

- exact finite master-projector theorem;
- finite master gaps in several regulated sectors;
- canonical representation-theoretic coarse embeddings, beginning with the unique \(S_4[2,2]\) \(j=1/2\to j=1\) intertwiner;
- depth-4 and depth-6 finite master information.

Therefore the next theory-specific task is no longer conceptually ambiguous.

For every available refinement pair:

1. freeze \(\iota_d\);
2. assemble \(M_d\) and \(M_{d+1}\) on matching carriers;
3. compute
   \[
   R_d=M_{d+1}\iota_d-\iota_dM_d;
   \]
4. compute \(\Delta_d,\Delta_{d+1}\);
5. report
   \[
   \epsilon_d=\|R_d\|/\min(\Delta_d,\Delta_{d+1});
   \]
6. test decay/summability.

---

# 10. Claim boundary

This theorem proves

\[
\boxed{
\text{master refinement control}
\Rightarrow
\text{physical-projector refinement control}.
}
\]

It does not prove that the current BQG master residuals actually decay.

That is the next theory-specific calculation.

The theorem also does not by itself provide physical time or an interacting graviton kernel. It closes only the mathematical arrow

\[
\boxed{
M_d\xrightarrow{\iota_d}M_{d+1}
\quad\Longrightarrow\quad
P_d\xrightarrow{\iota_d}P_{d+1}
}
\]

under the stated residual/gap condition.
