# Exact logical S4 twirl and the unique coarse anisotropy

Status: **exact finite representation-theory gate on the four-spin singlet geometry qubit**.

The logical geometry qubit is the two-dimensional singlet sector of four spin-`1/2` face qubits. Full tetrahedral face-permutation symmetry does **not** force the Bell-gluing pseudospin coupling to become Heisenberg isotropic.

The exact `S4` twirl reduces the allowed two-cell operator space to three invariants and leaves one independent orientation-vs-shape anisotropy.

---

## 1. One-cell Schur result

Project all 24 permutations of the four face labels onto the logical basis `K=0,2` and define

```text
T_1(O)
=(1/24) sum_g U_g O U_g^dagger.
```

The exact finite gate gives

```text
T_1(I)=I
T_1(X)=T_1(Y)=T_1(Z)=0.
```

Thus a fully face-permutation-symmetric one-cell Hamiltonian is scalar on the logical geometry qubit.

---

## 2. Two-cell diagonal S4 twirl

For two neighboring logical geometry qubits use the same face permutation on both cells:

```text
T_2(O)
=(1/24) sum_g
(U_g tensor U_g)
O
(U_g tensor U_g)^dagger.
```

The exact invariant operator space has dimension

```text
3
```

with basis

```text
II
XX+ZZ
YY.
```

Therefore every fully twirled two-cell mirror-even kernel has the form

```text
K_sym
=c0 II
+J_shape(XX+ZZ)
+J_orient YY.
```

The two bilinears are independent invariants.

---

## 3. S4 does not imply Heisenberg SU(2)

Heisenberg isotropy would require

```text
J_shape=J_orient.
```

But tetrahedral face-permutation symmetry does not enforce this equality.

The unique symmetry-allowed coarse pseudospin anisotropy is

```text
Delta_aniso
=J_orient-J_shape.
```

All local fields, `XZ/ZX` label artifacts and other noninvariant Pauli components twirl away, but `Delta_aniso` can survive.

Thus the coarse RG question becomes one-dimensional:

```text
Does Delta_aniso -> 0 under coarse graining?
```

---

## 4. Application to the canonical unbiased Peter-Weyl return kernel

The final environment-unbiased CI artifact gives, after the bipartite Heisenberg-frame rotation,

```text
J_X = -0.45691119919191336
J_Y = +2.18199564892363
J_Z = -0.6560148247263502.
```

Therefore

```text
J_shape
=(J_X+J_Z)/2
=-0.5564630119591318
```

and

```text
J_orient
=J_Y
=2.18199564892363.
```

The canonical structural return anisotropy is

```text
Delta_aniso,ret
=2.738458660882762.
```

This supersedes earlier provisional application numbers from a previous return-kernel revision.

The exact `S4` theorem means that this orientation-vs-shape split cannot be dismissed as a face-label artifact. Its static low-energy relevance still requires the physically correct constrained resolvent/RG weighting.

---

## 5. Mirror symmetry versus pseudospin symmetry

Mirror conjugation acts as

```text
X -> +X
Z -> +Z
Y -> -Y.
```

Therefore `YY` is mirror even, just like `XX+ZZ`.

Hence

```text
mirror Z2 permits Delta_aniso != 0.
```

Mirror `Z2` and pseudospin `SU(2)` must not be conflated.

---

## 6. Weight-robustness refinement

The state-by-state decomposition of the same canonical return kernel contains 648 intermediate states and a **mixed** anisotropy cone. Therefore arbitrary positive diagonal weighting can in principle alter the sign of `Delta_aniso`.

However every tested monotone spin-cost weighting family retains positive `Delta_aniso`.

See `PETER_WEYL_ANISOTROPY_WEIGHT_ROBUSTNESS.md`.

---

## Reproduction

```bash
python scripts/logical_s4_twirl_gate.py \
  --output verification_results/LOGICAL_S4_TWIRL.json
```
