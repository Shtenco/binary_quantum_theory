# BQG dynamical distance theorem

Status: **PROVED for sign-definite local weighted graph Hamiltonians; causal interpretation beyond short-time locality remains OPEN.**

## 1. Setup

Let (G=(V,E)) be a connected finite graph and let every physical edge (e=(ab)) carry a strictly positive conductance/coupling

[
g_{ab}>0.
]

Consider a graph-local one-particle Hamiltonian

[
oxed{
h = V - A_g,
}
]

where (V) is any diagonal Hermitian onsite operator and

[
(A_g)_{ab}=
egin{cases}
g_{ab},&(ab)in E,\
0,&	ext{otherwise}.
end{cases}
]

The same theorem applies after an overall sign convention change on all edge couplings.

Define the propagator

[
U(t)=e^{-iht}.
]

For vertices (i,j), let (d_G(i,j)) be ordinary shortest-path graph distance.

---

## 2. Vanishing theorem below graph distance

Expand

[
U_{ij}(t)
=
sum_{n=0}^infty
rac{(-it)^n}{n!}(h^n)_{ij}.
]

Any monomial contributing to ((h^n)_{ij}) contains at most (n) off-diagonal edge hops. Diagonal insertions do not move the graph vertex.

Therefore, if

[
n<d_G(i,j),
]

no length-(n) operator word can connect (i) to (j), and

[
oxed{
(h^n)_{ij}=0
qquad
(n<d_G(i,j)).
}
]

Hence

[
oxed{
partial_t^nU_{ij}(0)=0
qquad
(n<d_G(i,j)).
}
]

This statement is independent of the onsite potential (V).

---

## 3. Exact first nonzero coefficient

Let

[
d=d_G(i,j).
]

At exactly order (n=d), no diagonal insertion is possible: every factor must be an edge hop, otherwise fewer than (d) hops would remain.

Thus

[
(h^d)_{ij}
=
(-1)^d
sum_{gammainmathrm{SP}(i,j)}
prod_{eingamma} g_e,
]

where (mathrm{SP}(i,j)) is the set of shortest paths from (i) to (j).

Because all (g_e>0),

[
sum_{gammainmathrm{SP}(i,j)}
prod_{eingamma}g_e>0,
]

so cancellation is impossible and

[
oxed{
(h^d)_{ij}
eq0.
}
]

Therefore

[
oxed{
U_{ij}(t)
=
rac{i^d}{d!}
left[
sum_{gammainmathrm{SP}(i,j)}
prod_{eingamma}g_e
ight]
t^d
+
O(t^{d+1}).
}
]

The transition probability begins as

[
oxed{
|U_{ij}(t)|^2
=
rac{1}{(d!)^2}
left[
sum_{gammainmathrm{SP}(i,j)}
prod_{eingamma}g_e
ight]^2
t^{2d}
+
O(t^{2d+1}).
}
]

---

## 4. Dynamical graph-distance identity

Define

[
d_{m dyn}(i,j)
=
minleft{
nge0:
partial_t^nU_{ij}(0)
eq0
ight}.
]

Then exactly

[
oxed{
d_{m dyn}(i,j)=d_G(i,j).
}
]

This gives a coordinate-free operational characterization of graph distance from the short-time propagation algebra itself.

**Status: PROVED.**

---

## 5. QFI-weighted BQG specialization

For the current emergence branch, physical edges carry positive QFI conductances

[
g_{ij}^{m QFI}
=
rac14F_Q(ho_{ij},K_{ij})>0
]

whenever the edge is active.

Choose

[
h_{m QFI}
=
V
-
sum_{(ij)in E}
g_{ij}^{m QFI}
left(
|ianglelangle j|
+
|janglelangle i|
ight).
]

Then

[
oxed{
d_G(i,j)
=
min{n:partial_t^n[e^{-ih_{m QFI}t}]_{ij}|_{t=0}
eq0}.
}
]

So the same local response weights used in the resistance metric also define a propagation operator whose first nonzero short-time order recovers the unweighted combinatorial geodesic exactly.

The amplitudes of the first signal retain the metric weights through

[
sum_{gammainmathrm{SP}(i,j)}
prod_{eingamma}g_e^{m QFI}.
]

This separates two pieces cleanly:

1. **causal/combinatorial order**: number of required local hops;
2. **metric/dynamical strength**: weighted shortest-path amplitude.

---

## 6. Phase robustness

Any diagonal deformation

[
V=sum_i v_i|ianglelangle i|
]

including staggered mass / onsite gap terms leaves the first nonzero propagation order invariant.

Therefore

[
oxed{
d_{m dyn}=d_G
}
]

is unchanged by the critical-to-gapped onsite deformation used in the reduced BQG chain.

This is stronger than the long-range mutual-information distance, which changed functional form between phases.

---

## 7. What this theorem does not prove

It does **not** yet prove Lorentzian spacetime causality.

In particular, it does not yet supply:

- a physical clock;
- a continuum light cone;
- a universal propagation speed;
- a Lorentzian metric;
- a Lieb-Robinson velocity derived from the full BQG physical history;
- graph-changing causal order under the projector.

It proves an exact local propagation-order invariant inside any supplied sign-definite weighted graph Hamiltonian.

So the correct interpretation is

[
oxed{
	ext{graph locality}
Rightarrow
	ext{exact short-time propagation distance},
}
]

not

[
oxed{
	ext{full relativistic causality already derived}.
}
]

---

## 8. Numerical regression

The accompanying gate generates connected random graphs with positive edge weights and arbitrary diagonal onsite potentials.

For every ordered pair ((i,j)), it computes

[
min{n:(h^n)_{ij}
eq0}
]

and compares it to BFS shortest-path distance.

Frozen regression:

- graph sizes: (N=6,8,10);
- 10 random realizations per size;
- arbitrary positive edge weights;
- random diagonal potentials;
- total graphs: 30;
- result: **30/30 PASS**.

This is a numerical regression of the exact theorem, not its proof.

---

## 9. New causal frontier

The next stronger target is a many-body operator-spreading formulation:

[
O_i(t)
=
sum_{n=0}^{infty}
rac{(it)^n}{n!}
operatorname{ad}_H^n(O_i).
]

For graph-local interactions, support at site (j) cannot appear before enough nested commutators have crossed a path from (i) to (j).

The future goal is therefore

[
oxed{
	ext{projector-derived physical graph histories}
	o
	ext{many-body local generator}
	o
	ext{operator front}
	o
v_{m LR}
	o
	ext{continuum causal cone}.
}
]

That is the correct next bridge from emergent spatial geometry toward causality.
