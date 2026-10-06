# BQG topology-free emergence gate

Status: **controlled topology-free surrogate test; negative result for minimal valence-4 local gluing rule.**

This calculation removes coordinate labels, cubic lattices and target dimension from the graph-generation stage.

The question is:

$$
\boxed{
\text{can minimal local BQG-inspired gluing rules alone generate a robust }d_s\approx3?
}
$$

For the first tested rule, the answer is **no**.

---

## 1. What is removed

The generator is not told:

- a spatial coordinate system;
- 1D, 2D or 3D target dimension;
- a cubic/square lattice;
- a desired spectral dimension;
- a target return-probability law;
- any spectral feedback while the graph is grown.

The detector is calibrated separately on known manifolds and then frozen.

---

## 2. Minimal BQG-inspired graph rule

The current physical node comes from four spin-$1/2$ degrees of freedom and has a natural four-valent interpretation.

The topology-free surrogate therefore uses only:

1. maximum local valence $4$;
2. preference for unsaturated nodes by remaining free valence;
3. local loop closure within graph distance $\le2$;
4. no coordinates and no dimension target.

A new node always makes one edge to an unsaturated existing node. With probability

$$
\boxed{p_2=1/2}
$$

it makes a second edge. The second edge is chosen locally, favouring short graph distance, common neighbours and free valence.

This rule is **CANDIDATE / SURROGATE**, not a derivation from the fundamental graph-changing BQG constraint.

The parameter $p_2=1/2$ is not fitted to dimension. A robustness scan over

$$
p_2\in\{0.25,0.40,0.50,0.60,0.75\}
$$

is performed independently.

---

## 3. QFI weighting

For this first large-$N$ topology gate we use the homogeneous critical reference QFI conductance

$$
\boxed{
g_*=\frac{8}{\pi^2+4}.}
$$

Thus

$$
L_g=g_*L.
$$

Because a homogeneous positive conductance rescales diffusion time only,

$$
u=g_*\tau,
$$

it cannot change the plateau value of spectral dimension.

Therefore the present calculation isolates topology cleanly.

A fully self-consistent irregular many-body calculation of edge-dependent QFI weights remains a later step.

---

## 4. Automatic plateau detector

For graph Laplacian eigenvalues $\lambda_a$:

$$
P(\tau)=\frac1N\sum_a e^{-\tau\lambda_a},
$$

and

$$
\boxed{
d_s(\tau)=2\tau\frac{\sum_a\lambda_a e^{-\tau\lambda_a}}{\sum_a e^{-\tau\lambda_a}}.}
$$

The automatic detector searches contiguous log-time intervals satisfying fixed conditions on:

- small slope $|d d_s/d\ln\tau|$;
- minimum plateau width in decades;
- small relative variation;
- $d_s>0.5$ to reject the finite-size IR zero mode.

These thresholds are fixed before analysing the topology-free ensemble.

Calibration checks:

- a large cycle gives $d_s\approx1$;
- a periodic square lattice gives $d_s\approx2$;
- the exact infinite hypercubic formula gives $d_s\to D$ for $D=1,2,3$.

---

## 5. Matched null ensemble

The null generator has the same:

- maximum valence $4$;
- free-valence preference;
- probability of a second edge;
- growth schedule.

The only change is that the second edge is paired globally at random instead of by local loop closure.

Thus the null tests whether any plateau is merely caused by degree budget / growth rate.

---

## 6. Main numerical result

For six deterministic seeds at each size:

### $N=150$

$$
\boxed{
d_s^{\rm plateau}\approx1.316\pm0.106}
$$

with a valid plateau in $5/6$ realizations.

### $N=300$

$$
\boxed{
d_s^{\rm plateau}\approx1.226\pm0.031}
$$

with a valid plateau in $5/6$ realizations.

### $N=500$

$$
\boxed{
d_s^{\rm plateau}\approx1.232\pm0.030}
$$

with a valid plateau in $6/6$ realizations.

The $N=300$ and $N=500$ values are statistically stable within the ensemble spread.

Therefore the observed plateau is not drifting toward $3$ over the tested size range.

The average graph transitivity is approximately

$$
\boxed{T\approx0.20-0.21}
$$

and mean degree approaches

$$
\boxed{\langle k\rangle\approx3.}
$$

so the result is not simply a tree.

---

## 7. Matched null result

For $N=300$, twelve matched random-stub null realizations produced

$$
\boxed{0/12}
$$

accepted finite plateaus under the same detector.

The null graphs have almost the same average degree,

$$
\langle k\rangle\approx2.97,
$$

but much smaller transitivity,

$$
T\approx0.011.
$$

They also have a much larger spectral gap than the local-closure ensemble.

So local closure qualitatively changes diffusion geometry, but it still does **not** generate $d_s\approx3$.

---

## 8. Robustness scan

Without changing the detector, scan

$$
p_2=0.25,0.40,0.50,0.60,0.75.
$$

Whenever a stable plateau is detected, its ensemble mean remains below roughly

$$
\boxed{d_s\lesssim1.4}
$$

for the tested sizes and seeds.

No robust $d_s\approx3$ region appears.

This matters because a single tuned value of a graph-growth parameter would not count as emergence.

---

## 9. First topology-free no-go

The tested minimal rule consists of:

$$
\boxed{
\text{four-valent capacity}
+
\text{local free-valence attachment}
+
\text{local loop closure}.
}
$$

It produces a nontrivial low-dimensional diffusion geometry but not three-dimensional geometry.

Therefore:

$$
\boxed{
\textbf{four-valence plus local loop closure is insufficient to derive }d_s\approx3.
}
$$

This is the first topology-free falsification result of the emergence program.

---

## 10. What this does NOT prove

It does not prove that BQG cannot produce three dimensions.

It proves only that the present minimal surrogate local gluing rule does not.

In particular, the tested generator does not yet include:

- the full physical projector;
- graph-changing Hamiltonian/master constraints;
- shape-matching amplitudes from the actual quantum state;
- self-consistent edge-dependent QFI conductances;
- Pachner-like move amplitudes derived from BQG dynamics;
- interference between competing gluing histories;
- a dynamical action suppressing exponential branching or enforcing manifold-like closure.

So the correct conclusion is a constraint on the theory-building frontier, not a final no-go for BQG.

---

## 11. What the result teaches us

A four-valent local Hilbert-space structure does **not** determine three-dimensional continuum geometry by itself.

Something else must dynamically select the large-scale graph class.

The missing ingredient must distinguish between:

- random expander / branching graphs;
- quasi-one-dimensional locally closed graphs;
- manifold-like polynomial-growth graphs;
- specifically three-dimensional polynomial growth.

The natural place to search is no longer an arbitrary graph-growth heuristic, but the actual BQG quantum dynamics.

---

## 12. New frontier

The next real calculation should derive a **graph move amplitude** from the existing BQG constraint/projector machinery.

Schematically:

$$
\boxed{
\mathcal A(G\to G')
\propto
\langle G'|\Pi_{\rm phys}|G\rangle
}
$$

or from an effective graph-changing kernel.

Then graph histories should be sampled from these amplitudes rather than from hand-chosen attachment probabilities.

Only after that should the pipeline be repeated:

$$
\boxed{
\text{physical graph dynamics}
\to
\text{graph ensemble}
\to
\text{self-consistent QFI weights}
\to
L_g
\to
P(\tau)
\to
 d_s(\tau).
}
$$

That is the next genuine attempt to obtain dimension without putting topology in by hand.
