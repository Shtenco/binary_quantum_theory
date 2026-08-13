# Global q=2 PL-manifold completion

## Result

The frozen binary-route rule has

$$
q=2,\qquad Q_2=C_4.
$$

With the two endpoint states, the local route shell is

$$
\Sigma C_4\cong S^2,
$$

the boundary of an octahedron. Its f-vector is

$$
(V,E,F)=(6,12,8),\qquad \chi=2.
$$

There is a particularly economical closed simplicial globalization: the
boundary of the four-dimensional cross-polytope (the 16-cell). It has

$$
(V,E,F,T)=(8,24,32,16),
$$

and exactly the local incidence required by the frozen shell:

- every vertex link is the octahedral $S^2$;
- every edge link is $C_4\cong S^1$;
- every triangle link is $S^0$;
- every triangle belongs to exactly two tetrahedra.

Over $\mathbb F_2$ the seed complex has

$$
\boxed{\beta=(1,0,0,1)},
$$

so it is the expected homology $S^3$. The orientation equations are globally
consistent.

## Recursive held-out PL refinement

The executable gate `bcqg_global_manifold_gate.py` performs global barycentric
subdivision, which is a PL homeomorphism, and nevertheless rechecks every
simplex link rather than relying only on the theorem.

The first three levels are

| generation | V | E | F | tetrahedra | bad vertex links | bad edge links | bad face links |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 24 | 32 | 16 | 0 | 0 | 0 |
| 1 | 80 | 464 | 768 | 384 | 0 | 0 | 0 |
| 2 | 1696 | 10912 | 18432 | 9216 | 0 | 0 | 0 |

At every level

$$
\partial^2=0,
$$

all codimension-one faces are two-sided, the complex is orientable and

$$
\chi(M^3)=0.
$$

Thus the **canonical PL completion** of the frozen $q=2$ local shell is a closed
orientable global 3-manifold and remains so under recursive PL refinement.

## Exact scope

This closes an existence/stability statement:

$$
\boxed{
q=2\ \text{local binary shell}
\longrightarrow
\text{natural closed PL }M^3\cong S^3
\longrightarrow
\text{stable recursive refinements}.
}
$$

It is not a uniqueness theorem for the bare causal graph. The original
edge-rewrite rule by itself does not specify a complete global face-pairing
map. Therefore the statement **"the microscopic graph uniquely forces this
S3 gluing"** remains open unless the PL completion rule is promoted to a frozen
part of the microscopic model.
