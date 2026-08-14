# Peter-Weyl logical anisotropy: canonical unbiased return result

Status: **exact first-order support no-go + tested finite 32-column return kernel + audited 648-state decomposition; physical constrained master/RG flow still open**.

The finite Euclidean result has a sharp symmetry split:

```text
mirror Z2        -> survives
Bell-parent SU(2)-> broken in the raw first return kernel.
```

The raw return kernel is a structural/short-time object, **not** a proved static mass Hamiltonian.

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

Therefore `H_E` generates no first-order logical field and no first-order mirror splitting.

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

To remove the earlier fixed-environment shape bias, the canonical pair kernel is

```text
Kbar_01
 =(1/8) Tr_{2,3,4}
  P(H_E,0+H_E,1)^2P,
```

using all

```text
4 pair states x 8 environment states = 32 columns.
```

---

## 3. Canonical Pauli coefficients

Before the bipartite Heisenberg-frame rotation the main coefficients are

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

The mirror-forbidden odd-`Y` channels

```text
IY,YI,XY,YX,YZ,ZY
```

have relative norm

```text
2.7985693281119945e-33.
```

Thus mirror `Z2` survives to numerical precision.

---

## 4. Heisenberg frame and S4 reduction

After the `pi` rotation around `Y` on the second logical qubit,

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

and the unique S4-allowed raw structural split is

```text
Delta_aniso,ret
 =J_orient-J_shape
 =2.738458660882762.
```

Mirror symmetry permits this split; it does not imply full pseudospin `SU(2)`.

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

Therefore the raw anisotropy is a genuine tested **short-time logical leakage anisotropy** even though it is not yet a static low-energy mass term.

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

The previous documentation values `492/156` were stale and are retired.

---

## 7. Spin-cost robustness is not a physical result

Every one-hit intermediate state has

```text
spin_cost=3
changed_edges=3.
```

Therefore every weight depending only on `spin_cost` is a common scalar factor and cannot test robustness. The former spin-cost scans are retired.

The exact representation-channel decomposition is more informative. Starting from `j=1/2`, the three changed edges can be lowered to `j=0` or raised to `j=1`:

| raises | lowers | states | total Delta |
|---:|---:|---:|---:|
| 0 | 3 | 36  | `+0.2734514505369862` |
| 1 | 2 | 108 | `+0.1242961138804483` |
| 2 | 1 | 216 | `-0.3715029773216430` |
| 3 | 0 | 288 | `+2.712214073786969` |

The only net-negative one-hit representation channel is therefore

```text
2 raises + 1 lowering.
```

This is a kinematic classification, not yet an energy denominator.

---

## 8. Volume does not isolate the sign

The audited positive and negative sectors have strongly overlapping local-volume distributions. Zero-volume nodes occur in both sectors:

```text
positive: 200/392 states
negative: 160/256 states.
```

Their mean total volumes are

```text
positive <V_total>=2.7747718761477116
negative <V_total>=2.6299746617864215.
```

Simple total-volume diagnostic weights remain positive throughout the tested scan, including

```text
exp(-10 V_total): Delta=7.653856275172428e-7 > 0.
```

So `V_total` alone is not the missing physical selector.

---

## 9. Correct frontier

The finite result is

```text
P H_E P=0                       exact first-order protection
mirror-odd channels ~ 0        mirror Z2 survives
A_rel ~=0.964480                raw return kernel strongly anisotropic
Delta_aniso,ret=2.73845866      unique S4 raw structural split
648-state cone=mixed            arbitrary diagonal sign not protected
spin_cost weights=trivial       retired as robustness evidence
volume_total selector=negative  does not isolate the sign.
```

Therefore the next problem is **not** to invent a denominator. It is to derive the constrained intermediate-state operator from the dynamics itself.

The raw `K_ret` must not be identified with a physical mirror mass.

---

## Reproduction

```bash
python scripts/peter_weyl_logical_anisotropy_gate.py \
  --output verification_results/PETER_WEYL_LOGICAL_ANISOTROPY.json

python scripts/peter_weyl_anisotropy_resolvent_audit_fast_gate.py \
  --output verification_results/PETER_WEYL_ANISOTROPY_RESOLVENT_AUDIT.json
```

Legacy `peter_weyl_anisotropy_weight_robustness_gate.py` is now only a compatibility entry point to the same audited calculation.

---

## Scientific scope

These are finite properties of a candidate model. They do not establish a physical mirror particle, antigravity, a fifth force or a measured mediator mass. The constrained master operator, Lorentzian sector, route sector, matter matrix element and refinement/RG limit remain separate requirements.
