# Exact Bell-gluing Heisenberg parent of mirror order

Status: **exact bipartite unitary equivalence + finite 16-qubit spectrum + recursive graph spin-wave diagnostic; Goldstone continuum remains conditional**.

The conservative mirror-range branch used a staggered transverse-field Ising truncation. That truncation is useful as a strict `Z2` negative control, but it is not the full gluing dynamics already present in the geometry-qubit construction.

The exact two-cell Bell-gluing term was

```text
H_glue
 = -J sum_<vw>
   (X_v X_w - Y_v Y_w + Z_v Z_w).
```

On the bipartite tetrahedron dual graph this Hamiltonian has a stronger continuous-symmetry parent.

---

## 1. Exact bipartite rotation

Rotate every logical qubit on one sublattice by `pi` around logical `Y`.

On that sublattice,

```text
X -> -X
Y ->  Y
Z -> -Z.
```

Every dual edge joins opposite sublattices, so edge by edge

```text
-J(XX - YY + ZZ)
```

becomes

```text
+J(XX + YY + ZZ).
```

Therefore exactly

```text
U H_glue U^dagger
 = J sum_<vw> sigma_v . sigma_w.
```

In spin-1/2 normalization `sigma=2S`, this is

```text
4J sum_<vw> S_v . S_w,
```

the antiferromagnetic Heisenberg Hamiltonian.

`scripts/mirror_heisenberg_parent_gate.py` verifies the two-qubit matrix identity to machine precision.

---

## 2. The mirror order is one component of the Neel vector

The microscopic staggered mirror order was

```text
Sigma_Y
 = (1/N) sum_v eta_v Y_v.
```

The bipartite rotation leaves `Y` unchanged. Hence `Sigma_Y` is exactly the `Y` component of the Neel vector of the transformed Heisenberg model.

The full staggered vector is

```text
N_vec
 = (1/N) sum_v eta_v (X_v,Y_v,Z_v).
```

Thus the isolated `Z2` mirror variable sits inside a continuous pseudospin parent when the complete Bell-gluing interaction is retained.

This is a major structural distinction:

```text
Ising truncation:
  one mirror axis -> massive Z2 fluctuation generically

full Bell-gluing parent:
  three-component Neel vector -> continuous spin-wave channel possible.
```

---

## 3. Exact 16-qubit Q4 spectrum

The full Hilbert space still has

```text
2^16 = 65536
```

states.

The finite gate diagonalizes the lowest four states of

```text
H_AF=J sum sigma_v.sigma_w
```

on the exact `Q4` dual graph.

It obtains

```text
E0/J = -44.91393283371546
```

and a threefold-degenerate first excited level

```text
E1/J = E2/J = E3/J
      = -42.5995394906539...
```

with triplet gap

```text
Delta_triplet/J
 = 2.31439334306155...
```

The triplet degeneracy is the expected finite signature of the continuous Heisenberg symmetry.

The ground state has vanishing total magnetization to numerical precision and substantial staggered correlations:

```text
<N_y^2> = 0.368702848150999...
```

and, by exact SU(2) symmetry of the nondegenerate singlet ground state,

```text
<N_x^2>=<N_y^2>=<N_z^2>.
```

So the finite parent is not a classical `Sigma_Y=+/-1` state; it is the symmetric finite precursor of a possible ordered Neel phase.

---

## 4. Recursive dual-graph spin-wave diagnostic

The same recursive PL branch has a connected bipartite degree-four dual graph at generations

```text
16 -> 384 -> 9216 tetrahedra.
```

Let `mu` be a small combinatorial graph-Laplacian eigenvalue and `lambda=4-mu` the corresponding adjacency eigenvalue.

For the Pauli-normalized Heisenberg parent

```text
H=J sum sigma_i.sigma_j
  =4J sum S_i.S_j,
```

linear spin-wave theory on a degree-four bipartite graph gives the graph mode diagnostic

```text
omega_SW/J
 = 8 sqrt(1-(lambda/4)^2)
 = 8 sqrt(1-(1-mu/4)^2).
```

Using the actual recursive dual graphs:

```text
g=0: mu2 = 2.0000000000
     omega_SW/J ~= 6.92820

g=1: mu2 ~= 0.152240935
     omega_SW/J ~= 2.18609

g=2: mu2 ~= 0.011719063
     omega_SW/J ~= 0.61193.
```

The dimensionless long-wave scale softens strongly as the dual graph is refined.

This is a **graph spin-wave diagnostic**, not yet a physical mass prediction: the physical cell length and the renormalization of `J` under refinement must be included before interpreting the numerical decrease as an SI-energy gap.

---

## 5. Why this can remove the sigma-mass bottleneck

If the complete low-energy projected gluing dynamics satisfies both

```text
1. continuous pseudospin symmetry survives in the mirror/order sector
2. the refined/infinite-volume phase develops Neel order,
```

then mirror-orientation fluctuations are part of a Goldstone/spin-wave sector.

In that branch there is no independent local `m_sigma` to tune by hand: the low-energy mode is protected by the continuous symmetry, and its small energy is momentum/finite-volume controlled rather than a `Z2` mass term.

This is **conditional**, because the full gravity dynamics contains more than `H_glue`.

---

## 6. The new killer test is anisotropy

The exact one-cell geometry note already states that a fully face-permutation-symmetric one-cell Hamiltonian is trivial on the two-dimensional singlet geometry qubit. Nontrivial dynamics comes from inter-cell couplings.

The next decisive question is therefore not

```text
can we invent a light sigma?
```

but

```text
does the actual projected Peter-Weyl / route dynamics
preserve or break the X/Y/Z pseudospin symmetry of H_glue?
```

A surviving anisotropy such as

```text
Delta_x X_vX_w
+ Delta_y Y_vY_w
+ Delta_z Z_vZ_w
```

or an allowed single-axis effective term can gap/mix the mirror component.

Thus the physically correct range bottleneck has become an **anisotropy/RG gate**.

---

## 7. Relation to the conservative Ising range gate

`MIRROR_SIGMA_RANGE.md` remains useful as a negative control:

- if shape channels `X,Z` are frozen out and only the mirror `Y` axis remains dynamical, the finite `Z2` mode is strongly gapped;
- if the full Bell-gluing pseudospin parent survives, the same mirror order belongs to a continuous Heisenberg sector and can have a spin-wave/Goldstone route.

Therefore the theory now has a clean discriminator:

```text
IR anisotropy survives
 -> Ising-like massive mirror mode

IR anisotropy -> 0
 + Neel order survives
 -> continuous spin-wave mirror mode candidate.
```

---

## Reproduction

```bash
python scripts/mirror_heisenberg_parent_gate.py \
  --output verification_results/MIRROR_HEISENBERG_PARENT.json
```
