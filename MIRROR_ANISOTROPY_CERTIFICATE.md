# Mirror anisotropy frontier certificate

Status: **canonical frontier statement after the environment-unbiased Peter-Weyl logical projection**.

This certificate replaces the older wording that treated the unknown mirror-mode mass `m_sigma` as the primary range bottleneck.

The current finite theory has resolved a more fundamental hierarchy:

```text
mirror Z2 orientation symmetry
        survives

Bell-gluing accidental pseudospin SU(2)
        does not survive the tested Euclidean return dynamics

therefore the actual IR range problem is
        Delta_aniso^eff -> 0 ?
```

where

```text
Delta_aniso
 = J_orientation-J_shape.
```

---

## 1. What is exact/proved at the logical level

The four-spin singlet geometry qubit has

```text
Q_orientation = (sqrt(3)/4)Y.
```

Mirror conjugation acts as

```text
X -> +X
Z -> +Z
Y -> -Y.
```

The exact Bell-gluing term on a bipartite dual graph is unitarily equivalent to an antiferromagnetic Heisenberg parent,

```text
-J(XX-YY+ZZ)
  --B-sublattice pi-Y rotation-->
+J(XX+YY+ZZ).
```

This gives a continuous pseudospin parent, but not an exact symmetry theorem for all other geometry dynamics.

The exact diagonal tetrahedral `S4` twirl on two logical geometry qubits has invariant space

```text
span{ II, XX+ZZ, YY }.
```

Therefore the unique coarse pseudospin split allowed simultaneously by mirror symmetry and tetrahedral face-permutation symmetry is

```text
Delta_aniso=J_orientation-J_shape.
```

---

## 2. Euclidean Peter-Weyl first-order protection

Let `P` project onto the all-`j=1/2` logical sector.

The fundamental holonomy support rule gives

```text
P H_E P = 0.
```

The executable gate verifies zero projected norm on all 32 logical columns of the unbiased calculation.

Thus Euclidean Peter-Weyl dynamics produces no first-order local logical field and no first-order mirror splitting.

---

## 3. First nonzero environment-unbiased return channel

Define

```text
K_ret
 = (1/8) Tr_{2,3,4}
   P(H_E,0+H_E,1)^2P.
```

This is the maximally mixed partial trace over the other three logical K5 geometry qubits.

It preserves the mirror selection rule at relative forbidden-channel norm

```text
3.1887751872821285e-17.
```

But in the Bell/Heisenberg frame the coupling tensor is approximately

```text
[
  [-0.5020918898145224,  0, -0.6892178651005363],
  [ 0,                   2.5842530086520437, 0],
  [+0.6892178651005363,  0, -1.695852157212999]
].
```

The relative pseudospin anisotropy is

```text
A_rel = 0.9627752706476244.
```

Therefore the strong symmetry breaking is not caused by fixing the environment to one logical shape basis state.

---

## 4. S4 reduction to one number

After the exact tetrahedral twirl,

```text
K_sym
 = 14.318438270666093 II
 - 1.0989720235137607 (XX+ZZ)
 + 2.5842530086520437 YY.
```

Hence

```text
J_shape  = -1.0989720235137607
J_orient = +2.5842530086520437
```

and

```text
Delta_aniso,ret
 = 3.6832250321658044.
```

This is a structural return-kernel coefficient, not yet a physical energy gap.

---

## 5. Exact short-time meaning

Because `P H_E P=0`,

```text
P exp(-itH_E) P
 = P - t^2 K_ret/2 + O(t^3)
```

and the probability of leaving the logical sector begins as

```text
P_leak(t|psi)
 = t^2 <psi|K_ret|psi> + O(t^3).
```

Thus `Delta_aniso,ret` already measures anisotropic short-time Euclidean geometry leakage. It is not merely a basis decomposition with no dynamical content.

A static low-energy Hamiltonian still needs the correct constrained resolvent/transfer weighting.

---

## 6. Route sector does not change the mirror conclusion

The logical flux metric lies in

```text
I/X/Z
```

and has no `Y` component, so it is mirror even.

For the tested isotropic angular average, the frozen expectation-first route ordering gives equal values on the two logical basis states:

```text
0.8598466001022401
0.8598466001022401.
```

An operator-first spectral square-root ordering instead retains a finite `X/Z` shape component of norm

```text
0.04007491854520556.
```

Therefore the tested route sector preserves mirror `Z2`; possible additional pseudospin anisotropy is operator-ordering dependent and requires a new HDA-closed quantized-route construction.

---

## 7. Consequences for the range problem

The conservative Ising branch remains a valid massive negative control.

The exact Bell-gluing Heisenberg parent remains useful as a continuous-symmetry parent, but the Euclidean Peter-Weyl return dynamics shows that its `SU(2)` is accidental rather than exactly protected.

Therefore the correct next IR question is

```text
Delta_aniso^eff
 = J_orientation^eff-J_shape^eff
 -> 0 ?
```

under the physically correct constrained resolvent and PL/RG flow.

### If `Delta_aniso^eff != 0`

The mirror sector is generically easy-axis/easy-plane and the low-energy mirror excitation is not symmetry-protected massless. A light one-particle pole, if present, belongs to the massive/Yukawa `MIRRORMASTER` branch.

### If `Delta_aniso^eff -> 0`

An emergent Heisenberg/Goldstone sector can reappear. But for a physical mirror source aligned longitudinally with the chosen Neel vacuum,

```text
Sigma_Y
 = v - (pi_x^2+pi_z^2)/(2v)+...
```

so there is no one-Goldstone vertex. The leading free two-Goldstone potential is

```text
V_2G(r)
 = -Q1Q2/(32*pi^3*v^2*r^3),
```

with force `~r^-4`.

Thus even an emergent Goldstone branch does not automatically reproduce the previous Newton-like `1/r` mirror potential.

---

## 8. Current single frontier

The previous broad question

```text
what is m_sigma?
```

has been replaced by the sharper hierarchy

```text
1. derive the physically correct constrained weighting of intermediate Peter-Weyl states;
2. compute/renormalize Delta_aniso^eff;
3. determine whether the IR is anisotropic/massive or emergent-continuous;
4. combine that branch with the independent microscopic matter coefficient beta_m;
5. close the enlarged Peter-Weyl x route x mirror-matter HDA.
```

The immediate executable test is the positive-weight intermediate-state decomposition in

```text
scripts/peter_weyl_anisotropy_weight_robustness_gate.py.
```

It asks whether the sign of `Delta_aniso` can be changed at all by a positive state-diagonal resolvent weighting.

---

## Scientific status

This certificate belongs to a **candidate theory**. It establishes finite algebraic and numerical properties of the declared model. It does not establish experimental antigravity, a physical mirror particle, or a measured fifth force.
