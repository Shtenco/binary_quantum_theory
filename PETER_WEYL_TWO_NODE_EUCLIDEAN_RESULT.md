# Two-node regulator-safe Peter--Weyl x route Euclidean HDA result

Status: **preregistered finite two-node Euclidean PASS. Full Lorentzian quantum HDA remains OPEN.**

The protocol was frozen before evaluation in
`PETER_WEYL_TWO_NODE_EUCLIDEAN_PREREGISTRATION.md`.

## Operator

On the frozen all-$j=1/2$, all-$K=0$ K5 input, with regulator-safe
$J_{\max}=5/2$, the single smeared joint operator is

$$
\boxed{
H[N]=N(x_0)H_0^E+N(x_1)H_1^E+R[N;Q],
}
$$

with

$$
R[N;Q]=\frac12\left\{N,\sqrt{Q_g^{AB}P_AP_B}\right\}.
$$

The route metric is the frozen shared densitized flux Gram expectation

$$
Q_g^{AB}=\frac12\left(Q_{g,0}^{AB}+Q_{g,1}^{AB}\right),
$$

using non-shared local legs `(1,2)` at nodes 0 and 1. There is no independent
route lapse or fitted coupling constant.

For

$$
a=N(x_0),\quad b=N(x_1),\quad c=M(x_0),\quad d=M(x_1),
$$

the evaluated decomposition is

$$
\boxed{
[H[N],H[M]]
=[R_N,R_M]+C_{cross}+(ad-bc)[H_0^E,H_1^E].
}
$$

## Actual regulator-safe Euclidean commutator

The code recomputed the full safe HH vector rather than importing its old norm:

$$
\boxed{\operatorname{supp}[H_0^E,H_1^E]\psi_0=510},
$$

$$
\boxed{\|[H_0^E,H_1^E]\psi_0\|=1.6815599737359501}.
$$

The previous independent regression target was

$$
1.681559985798016,
$$

so the absolute regression error is

$$
\boxed{1.2062065790630072\times10^{-8}},
$$

inside the preregistered $5\times10^{-8}$ bound.

The initial shared route metric is

$$
\boxed{Q_0=\frac34 I_2}.
$$

## Frozen regulator sequence

The frozen WKB probe was $f=e^{i(8y+7z)}$, path lattice $L=48$, and

$$
\epsilon=(1/4,1/8,1/16,1/32,1/64).
$$

The measured channel defects relative to the same frozen $D$ target are:

| $\epsilon$ | route-only | cross / $D$ | pure $EE$ / $D$ | joint / $D$ |
|---:|---:|---:|---:|---:|
| 1/4 | 1.3221741194e-5 | 0.2393557732 | 0.02102553142 | 0.2402774632 |
| 1/8 | 6.6115292991e-6 | 0.1186026540 | 0.005196617774 | 0.1187164454 |
| 1/16 | 3.3058470645e-6 | 0.05903215331 | 0.001291650519 | 0.05904628267 |
| 1/32 | 1.6529339109e-6 | 0.02944874276 | 0.0003219725991 | 0.02945050287 |
| 1/64 | 8.2646874425e-7 | 0.01470753318 | 8.037551971e-5 | 0.01470775282 |

The fitted exponents are

$$
\boxed{p_{cross}=1.0058917161144039},
$$

$$
\boxed{p_{EE}=2.0074903905590453},
$$

$$
\boxed{p_{joint}=1.0071260819282668}.
$$

Thus the preregistered scaling predictions are realized:

$$
\boxed{\Delta_{cross}=O(\epsilon)},
$$

$$
\boxed{\Delta_{EE}=O(\epsilon^2)},
$$

$$
\boxed{\Delta_{joint}=O(\epsilon)}.
$$

At the final frozen regulator,

$$
\boxed{\Delta_{joint}(1/64)=0.014707752821092098<0.02},
$$

while

$$
\boxed{\Delta_{EE}(1/64)=8.037551971374878\times10^{-5}}.
$$

All eight preregistered conditions pass without channel-dependent
normalization, subtraction or post-hoc refit.

## What this result removes

The previous concern was that a genuine graph/spin-changing Peter--Weyl
Hamiltonian could destroy the square-root route-normal HDA mechanism once two
nodes and a real $[H_0,H_1]$ were present. This finite test falsifies that
failure mode on the frozen probe: the actual Euclidean geometry commutator is
subleading relative to the route HDA target, while the complete residual tends
to zero linearly with the regulator.

Therefore the Euclidean two-node geometry x route coupling is no longer the
primary operator bottleneck.

## Exact remaining boundary

This result is **not** full quantum GR HDA closure. Still open are:

1. actual Lorentzian $H_L^{(\beta)}$ amplitudes rather than support counting;
2. the full $H_E+H_L$ two-node commutator on the same route domain;
3. the operator-valued flux metric rather than diagonal intertwiner
   expectations;
4. multiple independent habitat/WKB channels;
5. collective-spin / continuum scaling;
6. the preferred densitized volume-anticommutator HDA target with the complete
   Lorentzian operator.

The next single operator task is therefore

$$
\boxed{
K\sim[V,H_E]
\;\longrightarrow\;
H_L^{(\beta)}\text{ amplitudes}
\;\longrightarrow\;
H_E+H_L+R
}
$$

with the Lorentzian coefficient frozen from the classical Ashtekar--Barbero
identity rather than fitted to HDA data.
