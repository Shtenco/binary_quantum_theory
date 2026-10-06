# BQG QFI-weighted spectral dimension calibration

Status: **exact hypercubic calibration + branching topology discriminator.**

This result continues the local-information-resistance branch:

$$
\rho_{ij}
\to
F_Q(\rho_{ij},K_{ij})
\to
g_{ij}
\to
L_g
\to
P(\tau)
\to
d_s(\tau).
$$

---

## 1. QFI-weighted graph Laplacian

For local information conductances $g_{ij}>0$, define

$$
\boxed{
(L_g)_{ij}
=\delta_{ij}\sum_k g_{ik}-g_{ij}.
}
$$

The heat kernel is

$$
\boxed{K(\tau)=e^{-\tau L_g}.}
$$

Return probability

$$
\boxed{
P(\tau)
=\frac1N\operatorname{Tr}e^{-\tau L_g}
}
$$

for finite graphs, with the usual per-site thermodynamic-limit interpretation for infinite homogeneous lattices.

Spectral dimension:

$$
\boxed{
d_s(\tau)
=-2\frac{d\ln P(\tau)}{d\ln\tau}.
}
$$

---

## 2. Exact homogeneous hypercubic solution

Take an infinite homogeneous $D$-dimensional hypercubic graph with the same QFI conductance $g$ on every nearest-neighbor edge.

The weighted Laplacian dispersion is

$$
\lambda(\mathbf k)
=2g\sum_{a=1}^D(1-\cos k_a).
$$

Therefore the return probability factorizes exactly:

$$
\boxed{
P_D(\tau)
=\left[e^{-2g\tau}I_0(2g\tau)\right]^D,
}
$$

where $I_0$ is the modified Bessel function.

Using

$$
\frac{d}{dx}\ln I_0(x)=\frac{I_1(x)}{I_0(x)},
$$

we obtain the exact running spectral dimension

$$
\boxed{
d_s^{(D)}(\tau)
=4Dg\tau
\left[
1-\frac{I_1(2g\tau)}{I_0(2g\tau)}
\right].
}
$$

---

## 3. Infrared dimension theorem

For large $x$,

$$
\frac{I_1(x)}{I_0(x)}
=1-\frac{1}{2x}+O(x^{-2}).
$$

Substituting $x=2g\tau$ gives

$$
\boxed{
d_s^{(D)}(\tau)
=D+O((g\tau)^{-1}).
}
$$

Hence

$$
\boxed{
\lim_{\tau\to\infty}d_s^{(D)}(\tau)=D.
}
$$

This is exact for every positive homogeneous conductance $g$.

Therefore the local QFI scale changes the diffusion clock but not the asymptotic dimension of a fixed homogeneous topology.

---

## 4. Phase robustness

The critical and staggered-volume-gapped BQG reduced states produce different local QFI conductances:

$$
g_{\rm critical}\neq g_{\rm gapped}.
$$

Define dimensionless diffusion time

$$
\boxed{u=g\tau.}
$$

Then

$$
\boxed{
d_s^{(D)}(u)
=4Du\left[1-\frac{I_1(2u)}{I_0(2u)}\right],
}
$$

which contains no $g$.

Thus all homogeneous phases collapse onto the same running dimension curve after the physically required local diffusion-time rescaling.

For example, using the critical QFI conductance

$$
g_*=\frac{8}{\pi^2+4}\approx0.576800878
$$

and the representative gapped $m=1$ value

$$
g_{m=1}\approx0.249855,
$$

we obtain exactly the same $d_s$ at fixed $u$.

At $u=10$:

$$
d_s^{(1)}\approx1.01318,
$$

$$
d_s^{(2)}\approx2.02636,
$$

$$
d_s^{(3)}\approx3.03954.
$$

At $u=100$:

$$
\boxed{
d_s^{(1)}\approx1.001256,
\quad
d_s^{(2)}\approx2.002513,
\quad
d_s^{(3)}\approx3.003769.
}
$$

So the calibration converges cleanly to $1,2,3$.

---

## 5. Interpretation

This gives the first actual dimension-calibration result of the emergence branch:

$$
\boxed{
\text{local QFI response}
\to
\text{weighted Laplacian}
\to
\text{heat diffusion}
\to
\text{correct topological dimension on regular lattices}.
}
$$

The important point is not just that a chain gives $1$.

The same rule, without retuning the conductance functional, gives

$$
D=1\to d_s=1,
$$

$$
D=2\to d_s=2,
$$

$$
D=3\to d_s=3.
$$

The local quantum phase changes the metric/diffusion scale through $g$, while topology controls the dimension.

---

## 6. Branching topology control

A regular branching graph should not be forced into a fake finite Euclidean dimension.

For the infinite 3-regular Bethe lattice, the unweighted Laplacian spectral bottom is

$$
\boxed{
\lambda_0=3-2\sqrt2>0.
}
$$

With homogeneous edge conductance $g$, the long-time return probability has the form

$$
P_{\rm Bethe}(\tau)
\sim
A\,\tau^{-3/2}e^{-g\lambda_0\tau}.
$$

Therefore

$$
\boxed{
d_s^{\rm Bethe}(\tau)
=2g\lambda_0\tau+3+o(1).
}
$$

Hence

$$
\boxed{
d_s^{\rm Bethe}(\tau)\to\infty
\quad(\tau\to\infty),
}
$$

rather than approaching a finite manifold-like plateau.

This is useful: the QFI-weighted diffusion geometry distinguishes regular Euclidean-like lattices from non-amenable exponential branching.

---

## 7. What this proves

Within the current reduced information-geometry construction:

1. the QFI-weighted Laplacian has an exact heat kernel on homogeneous hypercubic lattices;
2. the running spectral dimension is known in closed form;
3. $d_s\to D$ for $D=1,2,3,\ldots$;
4. changing the local QFI conductance only rescales diffusion time;
5. critical and gapped homogeneous phases therefore have the same asymptotic spectral dimension on the same topology;
6. a regular branching tree does not fake a finite Euclidean dimension.

This is the first **phase-robust emergent-dimension calibration** in the new BQG branch.

---

## 8. What is not yet proved

We have not shown that:

- the fundamental BQG vacuum dynamically selects a 3D-like graph;
- $d_s=3$ emerges without supplying 3D connectivity;
- the QFI twist generator is uniquely selected by the full BQG constraint algebra;
- an irregular/dynamical BQG graph flows to a stable $d_s=3$ infrared fixed point;
- Lorentzian causal structure follows from this diffusion geometry.

The result is a **calibration theorem**, not yet a derivation of three-dimensional space from binary dynamics alone.

---

## 9. Next falsification gate

The next calculation must remove the topology-by-hand loophole.

Instead of feeding a 1D/2D/3D regular graph and verifying its dimension, we should generate an irregular weighted graph from the local BQG gluing/state data and ask whether the QFI-Laplacian itself develops a stable infrared plateau.

The strongest next target is

$$
\boxed{
\text{dynamical/irregular QFI-weighted BQG graph}
\to
P(\tau)
\to
d_s(\tau)
\to
\text{test for an emergent plateau}.
}
$$

Only if a nontrivial graph family flows to $d_s\approx3$ without hard-coding cubic connectivity will we have evidence for genuine emergent three-dimensionality.
