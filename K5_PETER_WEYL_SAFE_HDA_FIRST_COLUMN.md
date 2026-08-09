# First regulator-safe Peter--Weyl K5 HH column

Status: **regulator-safe first-column support diagnostic. It is NOT by itself an HDA FAIL because the canonical Hamiltonian is graph-changing. Full Lorentzian HDA remains OPEN.**

## Why this calculation is different from the old 140D result

The old vector-5 model is the `Jmax=1/2` Peter--Weyl truncation. A local
Hamiltonian can hit one link twice and an `HH` composition can hit a shared
link four times. Therefore an all-`j=1/2` boundary requires

$$
\boxed{J_{max}^{safe}=\frac12+2=\frac52}.
$$

The calculation below uses

$$
\mathcal H_{link}^{J_{max}}
=\bigoplus_{j\le J_{max}}V_j^L\otimes V_j^R
$$

with `Jmax=5/2`, exact Clebsch--Gordan multiplication by the fundamental
holonomy, oriented four-valent intertwiners, and the genuine local volume

$$
\boxed{V_v=\sqrt{|J_1\cdot(J_2\times J_3)|}}.
$$

Projection to the Gauss/intertwiner basis is performed only after a complete
gauge-invariant local term. Projecting after each fundamental holonomy would
erase charged intermediate states.

## 1. One genuinely safe HH column

Input state: all ten K5 links at `j=1/2`, all five recoupling labels `K=0`.
The exact sparse calculation gives

$$
\boxed{\|[H_0,H_1]\psi_0\|=1.681559985798016}
$$

with 510 recoupling-basis output states.

The old coarse split was

$$
f_{all\,j=1/2}=0.29790166313739946,
\qquad
f_{outside\,32D}=0.7020983368626005.
$$

That split is numerically correct but physically too coarse.  Decomposing by
whether the ten abstract K5 links remain nontrivial gives

$$
\boxed{
\begin{array}{l|r}
\text{sector} & \text{fraction of norm}^2\\\hline
\text{same K5, all }j=1/2 & 0.29790166313739946\\
\text{same K5, all links nonzero but spins changed} & 0.25806517638704190\\
\text{at least one }j=0\text{ link} & 0.44403316047555935
\end{array}}
$$

Thus

$$
\boxed{0.5559668395244414}
$$

of the norm squared remains on the same ten-edge combinatorial K5 graph. Only
`44.4033%` contains a trivial-representation edge which can be removed under
cylindrical equivalence.

The distribution by number of `j=0` links is

$$
\boxed{
\begin{array}{c|rrrrrrr}
N_{j=0}&0&1&2&3&4&5&6\\\hline
f&0.55596684&0.18246774&0.15668486&0.08535889&0.01602488&0.00262260&0.00087420
\end{array}}
$$

and the actually reached maximum spin is only `j=3/2`, safely below `Jmax=5/2`.

## 2. K5 automorphism quotient

The 510 recoupling-basis outputs contain 305 distinct edge-spin assignments.
Quotienting those assignments by all `5! = 120` vertex automorphisms of K5
leaves only

$$
\boxed{26\ \text{abstract spin-graph orbits}}.
$$

Orbit counts by the number of trivial `j=0` links are

$$
\boxed{
\begin{array}{c|rrrrrrr}
N_{j=0}&0&1&2&3&4&5&6\\\hline
N_{orbits}&5&4&8&4&3&1&1.
\end{array}}
$$

This is only an abstract-label quotient, not the full spatial-diffeomorphism
quotient. It nevertheless shows quantitatively that raw basis support grossly
overcounts physically equivalent labels.

## 3. Correct interpretation: graph change is allowed

Thiemann's QSD Hamiltonian is graph-changing: its action on spin networks can
create, annihilate and reroute angular-momentum quanta. QSD III further treats
the constraint algebra through dual operators and the diffeomorphism-invariant,
group-averaged framework.

Therefore

$$
(1-P_{fixed})[H[N],H[M]]|\psi\rangle\ne0
$$

is **not** by itself an HDA anomaly.

The old fixed-sector fractions remain useful diagnostics, but the true quantum
anomaly is the component of

$$
[H[N],H[M]]-i\hbar D[\beta]
$$

which survives after the appropriate cylindrical/diffeomorphism equivalence or
on the chosen graph-changing habitat/dual space.  The new target is formalized
in `GRAPH_CHANGING_HDA_TARGET.md`.

The safe column therefore establishes only:

1. cutoff safety of this tested action;
2. substantial spin and graph dynamics;
3. failure of the hypothesis that increasing `Jmax` makes the action remain in
   the original all-`j=1/2` subspace.

It **does not** establish failure of the full HDA.

## 4. The old BF vertex is not the genuine-volume canonical kernel

The old five-tetrahedron state `V5` has 12 nonzero components and norm squared
`7/18` before normalization. Applying the regulator-safe genuine-volume node
Hamiltonian gives

$$
\boxed{\|H_0^{safe}|V_5\rangle\|=1.4002194669856702}.
$$

After zero pruning:

- output support: 251 spin-network states;
- component in the original all-`j=1/2` 32D sector: zero;
- maximum spin reached: `j=1`.

Hence

$$
H_v^{old}V_5=0
\not\Rightarrow
H_v^{safe}V_5=0.
$$

The earlier `V5` kernel is therefore a valuable BF/15j-like finite result but
must not be imposed as a tuning target on the canonical genuine-volume theory.

## 5. Canonical and covariant routes

### Canonical real-SU(2)

$$
\boxed{
H_E
\to H_E+H_L^{(\beta)}
\to \Delta_\beta
\to \Delta_{HH}^{hab}.
}
$$

### Covariant BF/spinfoam

$$
\boxed{
BF\xrightarrow{\;P_{simp}\;}\text{EPRL/FK-like gravity amplitudes}.
}
$$

EPRL simplicity is an independent covariant cross-check; it is not a
preprocessing operator inserted into the real-SU(2) canonical Hamiltonian.

## 6. Computational size

For the Euclidean safe calculation the complete HH reachable Gauss space is
bounded by

- 4193 admissible global spin assignments;
- total spin-network dimension 24364;
- 163 distinct local four-spin blocks;
- local intertwiner multiplicity at most 3.

The full Lorentzian support bound is documented separately in
`LORENTZIAN_HH_REACHABLE_SPACE.md`.

## 7. Current canonical pass condition

The candidate advances only if one common collective window gives

$$
\boxed{
\Delta_\beta\to0,
\qquad
\Delta_{HH}^{hab}\to0,
\qquad
\operatorname{inertia}K_E\to(5+,1-,3\,0),
\qquad
z\to1.
}
$$

Only after that may two physical tensor degrees of freedom be inferred from
first-class Dirac counting and independently checked spectrally.
