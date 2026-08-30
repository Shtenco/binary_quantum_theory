# Q4 ↔ K5 local four-valent carrier bridge — preregistration

Status: **exact local representation-compatibility diagnostic; not a graph isomorphism, not a Hamiltonian-covariance theorem, not a continuum result.**

## Why this bridge is needed

The repository currently contains two distinct finite graph structures that must not be conflated:

- the Q4 / 16-node background and its signed-coordinate symmetry `B4=(Z2)^4 ⋊ S4`;
- the K5 / five-node 4-simplex laboratory used by the current graph-changing Peter-Weyl Hamiltonian and active-habitat master diagnostics.

They are not globally isomorphic graphs.  What they do share is a local four-valent Gauss-singlet carrier.  This preregistration freezes the first compatibility theorem at that **local** level before any attempt is made to transport a Q4 symmetry statement onto K5 dynamics.

## Frozen local spaces

### Q4-side carrier

Use the explicit four-spin-1/2 singlet basis

\[
|i_0\rangle = |s\rangle_{12}|s\rangle_{34},
\]

\[
|i_1\rangle = \frac{1}{\sqrt3}
\left(|t_+t_-\rangle-|t_0t_0\rangle+|t_-t_+\rangle\right).
\]

Leg order is frozen as tensor axes `(0,1,2,3)` and a permutation `p` acts by `np.transpose(T, axes=p)`.

### K5-side carrier

Use the canonical Peter-Weyl four-valent intertwiner tensors from

`scripts/k5_peter_weyl_safe_hda_column.py`

at local doubled spins `(1,1,1,1)` and recoupling labels `K=0,2`, in that order.

No basis rotation, fitted phase, Procrustes alignment, SVD alignment or post-hoc relabelling is permitted before the primary basis comparison.

## Preregistered exact checks

A GREEN local bridge must establish all of the following with the pre-existing numerical precision scale (`2e-12` unless a floating spectral square root is explicitly involved):

1. both bases are orthonormal and span dimension two;
2. the raw overlap matrix

   \[
   O_{ab}=\langle i_a|K_b\rangle
   \]

   is the identity, not merely unitary up to an inferred change of basis;
3. for all 24 `S4` leg permutations, the Q4-side and K5-side induced matrices are equal in this frozen basis;
4. both realizations obey the same permutation composition law and are unitary;
5. their conjugacy-class characters equal the `[2,2]` character

   \[
   \chi=(2,0,2,-1,0)
   \]

   on cycle types `1^4`, `2 1^2`, `2^2`, `3 1`, `4`;
6. the full `S4` group-average projector vanishes on the local carrier, confirming that the same local pure-isotropy obstruction is present in both graph contexts;
7. the canonical absolute local volume operator restricted to this j=1/2 singlet carrier is the same matrix in the explicit Q4 and K5 bases and is proportional to the identity to the existing floating spectral accuracy.

## Deliberately excluded claims

Even a GREEN result does **not** establish:

- `Q4 ≅ K5` as graphs;
- a map between the 16 Q4 vertices and five K5 tetrahedral nodes;
- covariance of the K5 Hamiltonian under the full B4 group;
- transport of Q4 XOR translations into K5;
- equality of global Wilson loops, HDA constraints, master constraints or refinement histories;
- a physical projector or continuum dynamics.

## Scientific consequence if GREEN

A GREEN result licenses only the following compatibility square:

\[
\begin{array}{ccc}
\text{Q4 four-valent neighbourhood} & \longrightarrow & \mathcal H_{\rm singlet}^{(4)}\\
\downarrow S_4 & & \downarrow [2,2]\\
\text{K5 tetrahedral local patch} & \longrightarrow & \mathcal H_{\rm singlet}^{(4)}
\end{array}
\]

where the two right-hand carriers are shown to be the **same frozen representation realization**.  The next theorem must then address incidence/frame transport separately rather than assuming it.
