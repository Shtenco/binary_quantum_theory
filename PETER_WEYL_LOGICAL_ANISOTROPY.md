# Peter-Weyl logical geometry-qubit anisotropy

Status: **exact first-order support no-go + tested finite 32-column return kernel + audited 648-state decomposition; physical constrained/RG flow remains open**.

This note records a finite property of the logical geometry-qubit sector. It does not introduce an additional particle species, matter sector or force.

---

## 1. Exact first-order protection

Let `P` project to the all-`j=1/2` logical geometry-qubit sector. Every Euclidean triangle term contains fundamental holonomy hits and a fundamental hit changes

```text
j -> j +/- 1/2.
```

The finite gate verifies on all 32 logical columns

```text
P H_E P=0
```

with projected norm exactly `0.0`.

Therefore `H_E` generates no first-order logical field inside this projected sector.

---

## 2. First nonzero environment-unbiased return kernel

For nodes 0 and 1 define

```text
H_01=H_E,0+H_E,1
```

in the sine ordering. The first nonzero logical return object is

```text
K_ret=P H_01^2 P.
```

To remove the fixed-environment shape bias, the canonical pair kernel is

```text
Kbar_01
 =(1/8) Tr_{2,3,4}
  P(H_E,0+H_E,1)^2P,
```

using all

```text
4 pair states x 8 environment states = 32 columns.
```

`K_ret` is a structural return/leakage kernel. It is **not** by itself a low-energy Hamiltonian because no constrained resolvent or energy denominator has been derived.

---

## 3. Canonical Pauli coefficients

Before the declared bipartite basis rotation the main coefficients are

```text
II = 9.04524203998966
IX = +0.08054446950018196
IZ = +0.04650237114766842
XI = +0.08054446950018226
ZI = +0.04650237114766753
XX = +0.45691119919191336
YY = +2.18199564892363
ZZ = +0.6560148247263502
XZ = -0.17242879769840605
ZX = -0.17242879769840608.
```

The channels with an odd number of `Y` factors,

```text
IY,YI,XY,YX,YZ,ZY
```

have relative norm

```text
2.7985693281119945e-33.
```

This is reported as a `Y`-parity / basis-conjugation diagnostic only.

---

## 4. S4 reduction

After the declared `pi` rotation around `Y` on the second logical qubit,

```text
J_ret ~=
[
 [-0.45691119919191336, 0, +0.17242879769840605],
 [ 0,                    2.18199564892363,    0],
 [+0.17242879769840608, 0, -0.6560148247263502]
].
```

Its relative distance from an isotropic scalar coupling is

```text
A_rel=0.9644798301915488.
```

The exact diagonal tetrahedral `S4` twirl leaves only

```text
II,
XX+ZZ,
YY.
```

Hence

```text
J_shape
 =(-0.45691119919191336-0.6560148247263502)/2
 =-0.5564630119591318

J_orient
 =+2.18199564892363
```

and the unique `S4`-allowed raw structural split is

```text
Delta_aniso,ret
 =J_orient-J_shape
 =2.738458660882762.
```

The result says only that tetrahedral face-permutation symmetry does not force the two invariant bilinears to have equal coefficients.

---

## 5. Exact short-time meaning

Because `P H_E P=0`,

```text
P exp(-itH_E)P
 =P-t^2 K_ret/2+O(t^3)
```

and

```text
P_leak(t|psi)
 =t^2 <psi|K_ret|psi>+O(t^3).
```

Therefore the measured anisotropy is a tested **short-time logical leakage anisotropy**. No static mass, mediator or macroscopic interaction follows from it.

---

## 6. Audited 648-state decomposition

The companion audit reconstructs the direct kernel as

```text
K_direct=sum_n K_n
```

with matrix error

```text
8.606528098114035e-15.
```

The certified sign cone is

```text
positive states = 392
negative states = 256
zero states     = 0

sum positive Delta = +4.052816595873667
sum negative Delta = -1.3143579349909067.
```

Thus arbitrary positive state-diagonal weighting is **not** sign-protected.

Every one-hit intermediate state has

```text
spin_cost=3
changed_edges=3.
```

so weighting only by `spin_cost` is a common scalar rescaling and not a robustness test.

The exact representation-channel decomposition is more informative:

| raises | lowers | states | total Delta |
|---:|---:|---:|---:|
| 0 | 3 | 36  | `+0.2734514505369862` |
| 1 | 2 | 108 | `+0.1242961138804483` |
| 2 | 1 | 216 | `-0.3715029773216430` |
| 3 | 0 | 288 | `+2.712214073786969` |

This is a kinematic classification, not an energy spectrum.

---

## 7. Correct frontier

The finite result is

```text
P H_E P=0                       exact first-order protection
Y-odd channels ~ 0             finite basis-parity diagnostic
A_rel ~=0.964480                raw return kernel strongly anisotropic
Delta_aniso,ret=2.73845866      unique S4 raw structural split
648-state cone=mixed            arbitrary diagonal sign not protected
spin_cost weights=trivial       retired as robustness evidence
```

The next task is to derive the constrained intermediate-state operator from the dynamics itself and then test the anisotropy along a refinement/RG sequence.

---

## Reproduction

```bash
python scripts/peter_weyl_logical_anisotropy_gate.py \
  --output verification_results/PETER_WEYL_LOGICAL_ANISOTROPY.json

python scripts/peter_weyl_anisotropy_resolvent_audit_fast_gate.py \
  --output verification_results/PETER_WEYL_ANISOTROPY_RESOLVENT_AUDIT.json
```

These are finite properties of the candidate geometry sector. They are not evidence for any additional particle or force.
