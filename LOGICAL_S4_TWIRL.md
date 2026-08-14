# Exact logical S4 twirl and the unique coarse anisotropy

Status: **exact finite representation-theory gate on the four-spin singlet geometry qubit**.

The logical geometry qubit is the two-dimensional singlet sector of four spin-`1/2` face qubits. A natural coarse question is whether full tetrahedral face-permutation symmetry forces the Bell-gluing pseudospin coupling to become Heisenberg isotropic.

It does not.

The exact `S4` twirl reduces the allowed two-cell operator space to three invariants and leaves one independent orientation-vs-shape anisotropy.

---

## 1. One-cell Schur result

Project all 24 permutations of the four face labels onto the two-dimensional singlet logical basis `K=0,2`.

The resulting matrices form the nontrivial two-dimensional representation of the permutation group.

For a one-cell operator `O`, define

```text
T_1(O)
 = (1/24) sum_{g in S4}
   U_g O U_g^dagger.
```

The exact finite gate finds

```text
T_1(I)=I
T_1(X)=T_1(Y)=T_1(Z)=0.
```

Thus a fully face-permutation-symmetric one-cell Hamiltonian is scalar on the logical geometry qubit.

This independently explains why no preferred local logical axis should be inserted by hand.

---

## 2. Two-cell diagonal S4 twirl

For two neighboring logical geometry qubits use the same tetrahedral frame permutation on both cells:

```text
T_2(O)
 = (1/24) sum_g
   (U_g tensor U_g)
   O
   (U_g tensor U_g)^dagger.
```

The exact invariant operator space has dimension

```text
3.
```

A convenient basis is

```text
II
XX+ZZ
YY.
```

Therefore every fully twirled two-cell mirror-even kernel has the form

```text
K_sym
 = c0 II
 + J_shape (XX+ZZ)
 + J_orient YY.
```

The two bilinears `XX+ZZ` and `YY` are independent invariants.

---

## 3. Consequence: S4 does not imply Heisenberg SU(2)

Heisenberg isotropy would require

```text
J_shape = J_orient.
```

But tetrahedral face-permutation symmetry does not enforce this equality.

The unique symmetry-allowed coarse pseudospin anisotropy is therefore

```text
Delta_aniso
 = J_orient-J_shape.
```

All local fields, `XZ/ZX` label artifacts and other noninvariant Pauli components are removed by the exact twirl, but `Delta_aniso` can survive.

Thus the RG question becomes one-dimensional:

```text
Does Delta_aniso -> 0 under coarse graining?
```

rather than tracking an arbitrary 16-component two-qubit operator.

---

## 4. Application to the unbiased Peter-Weyl return kernel

The environment-traced Peter-Weyl return kernel has, after the bipartite Heisenberg-frame rotation,

```text
J_X = -0.5020918898145224
J_Y = +2.5842530086520437
J_Z = -1.695852157212999.
```

Its `S4`-twirled shape coefficient is

```text
J_shape
 = (J_X+J_Z)/2
 = -1.0989720235137607,
```

while

```text
J_orient
 = J_Y
 = 2.5842530086520437.
```

Hence the structural return anisotropy is

```text
Delta_aniso,ret
 = 3.6832250321658044.
```

The exact `S4` theorem tells us that this orientation-vs-shape split cannot be dismissed as a face-label artifact.

Its static low-energy relevance, however, still requires the physically correct constrained resolvent/RG weighting.

---

## 5. Mirror symmetry versus pseudospin symmetry

Mirror conjugation acts as

```text
X -> +X
Z -> +Z
Y -> -Y.
```

Therefore the bilinear `YY` is mirror even, just like `XX+ZZ`.

This is why mirror `Z2` can remain exact while pseudospin `SU(2)` is broken:

```text
mirror Z2 permits Delta_aniso != 0.
```

The two symmetries must not be conflated.

---

## Reproduction

```bash
python scripts/logical_s4_twirl_gate.py \
  --output verification_results/LOGICAL_S4_TWIRL.json
```
