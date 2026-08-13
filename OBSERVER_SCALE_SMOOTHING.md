# Binary route geometrogenesis v2: bit -> smooth spacetime candidate

Candidate checks: **13/13**

## Frozen local rule

Each causal link carries `q` binary route bits. One rewrite exposes all `2^q`
two-step routes between the same endpoints. Route states receive an intra-cell
frame link iff their bit labels have Hamming distance one. Only causal child
links are recursively rewritten.

The rule contains no coordinate dimension. Observer distance enters only after
the rule is frozen, through

$$
\ell_{obs}(r)=\sqrt{\ell_P^2+(\theta r)^2},\qquad
b(r)=2^{\lfloor\log_2(\ell_{obs}/\ell_P)\rfloor}.
$$

Train generations `g=2,3,4` select among `q=1,2,3` using only the declared
$D_{slice}\approx3$ and $z\approx1$ score. The winner is frozen before the
held-out generation is evaluated:

$$
\boxed{q_*=2}.
$$

The local topology result below is **not** used in that selection score.

## Train rule search

The three binary-route candidates give approximately

$$
q=1:\quad d_H=1.92065,\ z=1.00153,
$$

$$
\boxed{q=2:\quad d_H=2.97280,\ z=0.99134},
$$

$$
q=3:\quad d_H=3.99232,\ z=0.98028.
$$

The rule itself contains no spatial coordinate dimension. For `q` route bits,
there are $2^q$ binary-labelled routes and the asymptotic causal-edge volume
scaling gives $d_H\to q+1$; the finite spectral-gap scaling supplies the
independent dynamical exponent.

## Held-out generation 5

After freezing `q=2`, the transition `g=4 -> 5` gives

$$
\boxed{d_H=2.999229782},\qquad
\boxed{z=0.998281156}.
$$

Hence

$$
\boxed{d_s^{slice}=3.004393867},\qquad
\boxed{d_s^{history}\approx1+d_s^{slice}=4.004393867}.
$$

No 3D or 4D lattice is inserted into this held-out calculation.

## Independent local topology check

For a route cell, binary labels form the Hamming graph $Q_q$. Adding the two
causal endpoints gives its suspension as the local route shell. Over
$\mathbb F_2$:

- `q=1`: $\beta=(1,0,0)$;
- `q=2`: $\boxed{\beta=(1,0,1)}$;
- `q=3`: $\beta=(1,0,5)$.

Thus the frozen `q=2` shell is a single homology $S^2$ and admits a natural
local 3-cell completion. This is a strong local manifold precursor, but it is
**not yet** a theorem that all recursively glued global vertex links are $S^2$.

## Observer smoothing on the discovered rule

Using the discovered spatial volume together with one causal-time scaling
direction, the same frozen rule gives

$$
\boxed{\delta g\sim b^{-2.001707}},
$$

$$
\boxed{\nabla\delta g\sim b^{-3.001458}},
$$

$$
\boxed{\delta R\sim b^{-4.000524}}.
$$

The two-form sector built from the same observer-cell multiplicities gives

$$
\boxed{\Delta_{simp}\sim b^{-1.994838}},\qquad
\boxed{\Delta_{g_U}\sim b^{-2.019746}}.
$$

Thus the earlier $b^{-2/-3/-4}$ smoothing law survives after removing the
positive-branch 4D torus.

## Diffeomorphism kinematics

The frozen rule has exactly two route bits. In the refined path description
these supply two transverse rerouting coordinates. The independent vector-field
path test gives

$$
\boxed{\Delta_{Lie}\sim L^{-1.981810}},
$$

so the local non-Abelian diffeomorphism kinematics approaches its continuum Lie
bracket with approximately quadratic defect.

## Conditional graviton count

The held-out slice dimension is within $0.005$ of three. Therefore, **if** the
full Hamiltonian and diffeomorphism constraints become first class, the local
two-derivative HDA selects

$$
c_{DW}=\frac{1}{D-1}=\frac12,
$$

and Dirac counting gives

$$
\boxed{N_{grav}=2}
$$

local metric configuration modes. This is a conditional consequence of HDA
closure, not an independent proof that the microscopic Hamiltonian has already
closed.

The classical real-Ashtekar--Barbero kinetic cancellation also remains at
machine precision in the same master program:

$$
H_E^{kin}+H_L^{corr}=H_{DW},
$$

with maximum relative regression error about $1.9\times10^{-12}$.

## Scientific status

The strongest current chain is therefore

$$
\boxed{
\text{binary route bits}
\to q_*=2
\to S^2\ \text{cell shell}
\to d_s^{slice}\approx3
\to z\approx1
\to \text{observer smoothing}
\to \text{smooth IR candidate}
}.
$$

The **13/13** result is a finite candidate-geometrogenesis PASS. It does not yet
close two decisive gates:

1. **Global manifold emergence:** one local homology-$S^2$ shell does not prove
   the recursively glued global complex is a 3-manifold.
2. **Full quantum HDA:** the path-diffeomorphism RHS is known, but the same
   graph-changing Hilbert space must still satisfy

$$
\boxed{
[\hat H[N],\hat H[M]]
\to
i\hbar\hat D[\sharp(NdM-MdN)]
}.
$$

Until both are passed, this is a direct `bit -> spacetime candidate` rather than
a proof of quantum general relativity.
