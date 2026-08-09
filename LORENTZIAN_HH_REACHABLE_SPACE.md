# Full Lorentzian K5 HH reachability upper bound

Status: **exact support/CSP enumeration for the stated Thiemann-type operator tree; amplitudes and cancellations are not yet included.**

This calculation asks how large the next full Lorentzian quantum-HDA problem can
be before any Clebsch--Gordan amplitude, volume matrix element or commutator
cancellation is used.

The local support model contains

$$
H=H_E+H_L,
$$

with

$$
H_E\sim h_{\alpha_{ab}}h_c[h_c^{-1},V]
$$

and the standard nested-commutator Lorentzian support

$$
H_L\sim C_i(K)C_j(K)C_k(V),
\qquad
C_e(X)=h_e[h_e^{-1},X],
\qquad
K\sim[V,H_E].
$$

Only representation reachability is counted. Each fundamental holonomy hit can
change a link spin by `j -> j +/- 1/2`. At the end of each complete local
Hamiltonian the output is required to admit a Gauss-invariant four-valent
intertwiner at every K5 node.

The standalone enumerator is `scripts/lorentzian_reachability_gate.cpp`.

## 1. Unique local hit profiles

After identifying duplicate support patterns, one K5 node has

- 12 distinct Euclidean profiles;
- 240 distinct Lorentzian profiles;
- therefore **252** distinct profiles for `H_E + H_L`.

The conservative per-link transient bounds are documented separately in
`scripts/lorentzian_hit_depth_bound.py`:

$$
r_e(H_E)=2,
\qquad
r_e(H_L)=6,
\qquad
r_e(HH)=12.
$$

Hence an all-`j=1/2` input is guaranteed transient-cutoff-safe at

$$
\boxed{J_{max}=13/2}.
$$

## 2. Reachable sector after one full Hamiltonian

Starting from all ten links at `j=1/2`, before using any matrix-element
cancellation, the support union followed by the exact Gauss admissibility test
contains

$$
\boxed{1843\ \text{global spin assignments}}
$$

with total four-valent intertwiner dimension

$$
\boxed{9750}.
$$

The largest **final** spin is only

$$
\boxed{j_{max}^{final}=5/2}.
$$

Across this support there are 489 distinct local four-spin blocks. Their
intertwiner-dimension distribution is

$$
\boxed{
253\times d=1,
\quad153\times d=2,
\quad57\times d=3,
\quad25\times d=4,
\quad1\times d=5.
}
$$

## 3. Reachable sector after a second local Hamiltonian

For one K5 pair, e.g. `H_1 H_0`, imposing Gauss admissibility again after the
second complete local Hamiltonian gives

$$
\boxed{615\,884\ \text{global spin assignments}}
$$

and total spin-network dimension

$$
\boxed{11\,314\,085}.
$$

The largest final spin is

$$
\boxed{j_{max}^{final}=11/2}.
$$

This is below the conservative transient wall `13/2`: intermediate operator
paths can require a higher representation than the final state, so `11/2`
should **not** replace `13/2` as the rigorous cutoff without an intermediate-
path analysis.

The entire 11.3-million-dimensional final support is assembled from only

$$
\boxed{2850}
$$

distinct local four-spin blocks. Their intertwiner-dimension distribution is

$$
\boxed{
\begin{array}{c|rrrrrrr}
d&1&2&3&4&5&6&7\\\hline
N&1159&807&488&262&108&25&1
\end{array}}
$$

so the largest local matrix is only `7 x 7`.

## 4. Interpretation

This is a deliberately conservative **support upper bound**.

It ignores:

- zero Clebsch--Gordan coefficients beyond representation admissibility;
- destructive interference between color contractions;
- cancellations inside `[V,H_E]`;
- cancellations between the two `HH` orderings;
- semiclassical state localization;
- diffeomorphism/physical projections.

Therefore the actual Lorentzian quantum-HDA state support can only be smaller.

The important result is computational:

$$
1015^{10}
\quad\text{is not the problem.}
$$

The exact calculation should be organized as a sparse tensor-network/
recoupling engine whose local cache contains only 2850 matrices of size at most
`7 x 7`, while global states are streamed rather than stored as a dense
Hamiltonian matrix.

## 5. Current computational strategy

1. Precompute the 2850 local intertwiner bases and volume matrices.
2. Precompute fundamental-holonomy recoupling blocks between them.
3. Build `K=[V,H_E]` directly in this local block language.
4. Apply the two Lorentzian `C(K)` factors without expanding magnetic indices.
5. Stream one `HH` pair and measure actual reached spin/support.
6. Only then allocate the minimal Peter--Weyl cutoff actually required by the
   nonzero amplitude paths.
7. Compare the resulting commutator to the independently verified discrete
   simplex `D(k,l)/(3V)` benchmark and then to the continuum HDA safe-window
   benchmark.

This is the shortest exact route from the present canonical kinematics to the
first genuinely Lorentzian quantum-HDA falsifier.
