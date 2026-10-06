# BQG physical graph-transition kernel

Status: **EXACT finite projector bridge + EXACT regulated graph-changing support + OPEN numerical BQG transition amplitudes.**

This note replaces heuristic graph-growth probabilities by the first operator-level transition rule already implied by the existing BQG constraint/projector machinery.

The central distinction is mandatory:

1. a regulated constraint can have nonzero support on graph-changed sectors;
2. this does **not** by itself equal a physical transition probability;
3. the physical coherent amplitude is a matrix element of the physical projector.

---

## 1. Master constraint and physical projector

Let the regulated constraint family be

$$
\{C_A\},
$$

and let $G^{AB}$ be a positive-definite metric on constraint labels. Define

$$
\boxed{
\mathbb M
=
\sum_{A,B}C_A^\dagger G^{AB}C_B.
}
$$

For positive $G$,

$$
\langle\psi|\mathbb M|\psi\rangle
=
\|G^{1/2}C\psi\|^2\ge0,
$$

hence in the finite regulated setting

$$
\boxed{
\ker\mathbb M
=
\bigcap_A\ker C_A.
}
$$

The physical projector is therefore

$$
\boxed{
P_{\rm phys}
=
\mathbf 1_{\{0\}}(\mathbb M).
}
$$

Equivalently, whenever the regulated spectrum has a gap above the zero eigenspace,

$$
\boxed{
P_{\rm phys}
=
\lim_{T\to\infty}e^{-T\mathbb M}.
}
$$

This is projector/constraint flow. The parameter $T$ must **not** automatically be interpreted as external physical time.

---

## 2. Graph-sector decomposition

Let $\Pi_\Gamma$ project onto the cylindrical Hilbert sector associated with abstract graph $\Gamma$ after removal of $j=0$ links.

Then the finite-$T$ graph-sector kernel is

$$
\boxed{
K_T(\Gamma',\Gamma)
=
\Pi_{\Gamma'}e^{-T\mathbb M}\Pi_\Gamma.
}
$$

The physical graph-sector block is

$$
\boxed{
K_{\rm phys}(\Gamma',\Gamma)
=
\Pi_{\Gamma'}P_{\rm phys}\Pi_\Gamma.
}
$$

For basis microstates $|\Gamma,\alpha\rangle$ and $|\Gamma',\beta\rangle$ the coherent physical amplitude is

$$
\boxed{
\mathcal A^{\rm phys}_{\beta\alpha}
(\Gamma'\leftarrow\Gamma)
=
\langle\Gamma',\beta|P_{\rm phys}|\Gamma,\alpha\rangle.
}
$$

Equivalently,

$$
\boxed{
\mathcal A^{\rm phys}_{\beta\alpha}
=
\lim_{T\to\infty}
\langle\Gamma',\beta|e^{-T\mathbb M}|\Gamma,\alpha\rangle.
}
$$

This is the first non-heuristic graph-transition amplitude definition in the current emergence program.

**Status: EXACT in any finite regulated realization in which the full $\mathbb M$ is explicitly assembled.**

---

## 3. Short-$T$ matrix element

Expanding the heat kernel,

$$
e^{-T\mathbb M}
=
I-T\mathbb M+O(T^2),
$$

so for distinct graph microstates

$$
\langle\Gamma',\beta|e^{-T\mathbb M}|\Gamma,\alpha\rangle
=
-T\,\langle\Gamma',\beta|\mathbb M|\Gamma,\alpha\rangle
+O(T^2).
$$

The master matrix element is

$$
\boxed{
\langle\beta|\mathbb M|\alpha\rangle
=
\sum_{A,B}G^{AB}
\langle C_A\beta|C_B\alpha\rangle.
}
$$

Therefore graph-sector coupling is determined by **overlaps of constraint images**, not by an independently chosen graph-growth probability.

This identifies exactly what numerical object must be produced next.

---

## 4. Existing K5/Peter-Weyl calculation proves graph-changing support is nonzero

The repository already contains a regulator-safe K5/Peter-Weyl calculation with:

- finite link cutoff;
- exact SU(2) Clebsch-Gordan recoupling;
- genuine local volume operator;
- orientation-covariant Hermitian node Hamiltonians;
- the commutator $[H_0,H_1]$ acting on the all-$j=1/2$, $K_v=0$ K5 boundary state.

The output norm is distributed by the number $n_0$ of links driven to $j=0$ as

| $n_0$ | fraction of $\|[H_0,H_1]\psi\|^2$ |
|---:|---:|
| 0 | 0.55596684 |
| 1 | 0.18246774 |
| 2 | 0.15668486 |
| 3 | 0.08535889 |
| 4 | 0.01602488 |
| 5 | 0.00262260 |
| 6 | 0.00087420 |

After cylindrical reduction, $j=0$ links are absent from the abstract graph. Hence all $n_0>0$ channels are graph-changing.

Their total support fraction is

$$
\boxed{
0.44403316\ldots
}
$$

or about

$$
\boxed{44.4\%}
$$

of the regulated commutator-column norm.

For the frozen total norm

$$
\|[H_0,H_1]\psi\|
=1.681559985798016,
$$

the sector norm magnitudes are approximately

| $n_0$ | sector norm |
|---:|---:|
| 0 | 1.253824665 |
| 1 | 0.718299247 |
| 2 | 0.665619262 |
| 3 | 0.491288665 |
| 4 | 0.212867695 |
| 5 | 0.086114918 |
| 6 | 0.049718471 |

Thus graph-changing support in the regulated constraint habitat is not hypothetical.

### Critical caveat

The number

$$
44.4\%
$$

is **not**

$$
|\mathcal A^{\rm phys}_{\Gamma'\Gamma}|^2
$$

and is **not** a graph transition probability.

It is only the fraction of the norm of one regulated constraint-commutator column that lies in sectors whose cylindrical graph changes.

Conflating these two objects would be a category error.

---

## 5. Finite projector bridge selftest

The new gate

`script/bqg_projector_graph_transition_gate.py`

constructs a finite master-constraint model with two graph sectors and a common physical kernel that mixes them.

It verifies:

1. positivity and the correct zero eigenspace of $\mathbb M$;
2. recovery of $P_{\rm phys}$ from zero modes;
3. a nonzero cross-graph block
   $$
   \Pi_{\Gamma'}P_{\rm phys}\Pi_\Gamma\ne0;
   $$
4. the semigroup identity
   $$
   e^{-(T_1+T_2)\mathbb M}
   =e^{-T_1\mathbb M}e^{-T_2\mathbb M};
   $$
5. the short-$T$ derivative;
6. exponential convergence to the physical projector controlled by the master gap;
7. the matrix-element identity
   $$
   \langle\beta|\mathbb M|\alpha\rangle
   =\sum_{AB}G^{AB}\langle C_A\beta|C_B\alpha\rangle.
   $$

This is an operator-algebra verification of the bridge, not a substitute for the real enlarged BQG master matrix.

---

## 6. What is now genuinely derived

The graph-history pipeline no longer needs an arbitrary rule of the form

$$
p(G\to G')=\text{chosen heuristic}.
$$

The correct finite-regulator object is instead

$$
\boxed{
\mathcal A(G\to G')
\equiv
\Pi_{G'}P_{\rm phys}\Pi_G
}
$$

at graph-sector level, or its matrix elements at microstate level.

Thus the architecture becomes

$$
\boxed{
\{C_A\}
\to
\mathbb M
\to
P_{\rm phys}
\to
\mathcal A_{\Gamma'\Gamma}
\to
\text{graph-history amplitudes}.
}
$$

This is the first operator-derived replacement for the failed topology-free heuristic generator.

---

## 7. What is still OPEN

The current repository does **not yet contain the full numerical matrix**

$$
\boxed{
\mathbb M_{\rm enlarged}
}

on a graph-changing Peter-Weyl habitat large enough to evaluate

$$
\Pi_{\Gamma'}P_{\rm phys}\Pi_\Gamma
$$

for the actual K5 graph sectors.

Therefore we do **not** yet have numerical physical values for

$$
\mathcal A^{\rm phys}_{\Gamma'\Gamma}.
$$

This is now the precise bottleneck.

---

## 8. Next exact computational object: the graph-changing shell

Choose an initial regulated state $|\psi_0\rangle$ and build the finite Krylov/constraint shell

$$
\boxed{
\mathcal H_{\rm shell}^{(r)}
=
\mathrm{span}
\left\{
|\psi_0\rangle,
C_A|\psi_0\rangle,
C_BC_A|\psi_0\rangle,
\ldots,
C_{A_r}\cdots C_{A_1}|\psi_0\rangle
\right\}.
}
$$

Every basis state is then assigned an abstract graph signature by deleting $j=0$ links.

Let

$$
\Pi_\Gamma^{(r)}
$$

be the projector onto each graph orbit in this shell.

Then assemble all restricted constraint matrices

$$
C_A^{(r)}
$$

and

$$
\boxed{
\mathbb M^{(r)}
=
\sum_{AB}
(C_A^{(r)})^\dagger G^{AB}C_B^{(r)}.
}
$$

Diagonalize it and construct

$$
P_0^{(r)}
=
\mathbf1_{\{0\}}(\mathbb M^{(r)}).
$$

The first actual numerical graph-transition blocks are then

$$
\boxed{
A_{\Gamma'\Gamma}^{(r)}
=
\Pi_{\Gamma'}^{(r)}P_0^{(r)}\Pi_\Gamma^{(r)}.
}
$$

This is the next calculation that can genuinely replace hand-built graph dynamics.

---

## 9. Why a graph-history probability is one step further

$P_{\rm phys}$ gives coherent amplitudes, not automatically a classical Markov process.

One must not silently define

$$
p_{\Gamma'\Gamma}=|A_{\Gamma'\Gamma}|^2
$$

and iterate it as if graph label were external time.

A history interpretation requires either:

1. a relational clock/history projector;
2. a consistent/decoherent histories construction;
3. or a carefully defined Euclidean transfer interpretation of finite-$T$ kernels.

For a specified state $|\psi_\Gamma\rangle$, a finite-$T$ diagnostic weight can be defined as

$$
W_T(\Gamma'\leftarrow\Gamma;\psi)
=
\left\|
\Pi_{\Gamma'}e^{-T\mathbb M}\Pi_\Gamma|\psi\rangle
\right\|^2,
$$

but this must be described as **constraint/projector flow**, not external physical time.

The existing relational-history machinery is therefore the natural next bridge after the numerical graph-sector projector blocks are known.

---

## 10. Updated physical pipeline

The honest pipeline is now

$$
\boxed{
\text{regulated BQG constraints}
\to
\mathbb M_{\rm enlarged}
\to
P_{\rm phys}
\to
\mathcal A_{\Gamma'\Gamma}
\to
\text{relational graph histories}
\to
\rho_{ij}
\to
g_{ij}^{\rm QFI}
\to
L_g
\to
P(\tau)
\to
d_s(\tau).
}
$$

The next milestone is not another graph generator. It is the first explicit numerical block

$$
\boxed{
\Pi_{\Gamma'}P_{\rm phys}\Pi_\Gamma
}
$$

from the real Peter-Weyl graph-changing shell.
