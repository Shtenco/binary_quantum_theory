# Peter-Weyl anisotropy: positive-weight robustness cone

Status: **tested finite state-by-state decomposition of the environment-unbiased Euclidean return kernel; physical constrained resolvent remains open**.

The environment-unbiased logical return kernel is

```text
K_ret
 = (1/8) Tr_env
   P(H_E,0+H_E,1)^2P.
```

After the exact tetrahedral `S4` twirl its only pseudospin-breaking coefficient is

```text
Delta_aniso
 = J_orientation-J_shape.
```

A physical second-order constrained kernel would generally weight intermediate Peter-Weyl states nonuniformly. The purpose of this gate is to determine how much of the sign of `Delta_aniso` is already fixed before a physical energy denominator/resolvent is supplied.

---

## 1. State-by-state decomposition

Write the first-action amplitudes through intermediate Peter-Weyl basis states `n`. The maximally mixed environment return kernel decomposes as

```text
K_ret = sum_n K_n,
```

where each `K_n` is a positive-semidefinite outer-product contribution.

For any positive state-diagonal reweighting,

```text
K_w = sum_n w_n K_n,
w_n > 0.
```

Because the `S4`-reduced anisotropy is linear in the kernel,

```text
Delta_w = sum_n w_n delta_n.
```

The executable gate reconstructs every nonzero intermediate contribution separately.

---

## 2. Canonical artifact numbers

The final CI artifact contains

```text
648 intermediate states.
```

The unweighted environment-unbiased kernel gives

```text
Delta_aniso,ret = 2.7384586608827632
II weight       = 9.04524203998966
Delta/II        = 0.3027512861210171.
```

This is the canonical state-by-state value. It supersedes earlier provisional documentation values from a prior return-kernel revision.

The sign cone is mixed:

```text
positive states = 492
negative states = 156
zero states     = 0

sum(delta_n>0) = +0.9585825547153505
sum(delta_n<0) = -0.3107878924256691.
```

The positive/negative absolute-sum ratio is

```text
0.9585825547153505 / 0.3107878924256691
 ~= 3.084.
```

Therefore

```text
sign_definite_under_arbitrary_positive_state_weights = false.
```

This is an important negative result:

> an arbitrary positive state-diagonal resolvent can in principle cancel or reverse the structural anisotropy if it preferentially enhances the negative intermediate sector strongly enough.

There is no denominator-independent sign theorem.

---

## 3. Intermediate spin classes

The 648 intermediate states collapse into three spin-cost classes in the finite gate.

| spin cost | changed edges | max `2j` | min `2j` | states | total `Delta` | total `II` |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 3 | 2 | 1 | 384 | `+2.965184320680376` | `9.486628444349037` |
| 4 | 4 | 2 | 0 | 72 | `-0.22516138038269654` | `0.5639155147335205` |
| 4 | 4 | 2 | 1 | 192 | `-0.0015642794149160255` | `2.961447491962253` |

The dominant positive class contains three changed edges with spins in the `j=1/2,1` range.

The main negative sector is sharply localized in the class

```text
spin_cost=4
changed_edges=4
max 2j=2   (j=1)
min 2j=0   (j=0).
```

A much smaller negative contribution also appears in the four-changed-edge `j=1/2,1` class.

Thus cancellation is not controlled by spin cost alone; it depends on finer geometric/intertwiner content inside the four-edge return sector.

---

## 4. Broad monotone spin-cost reweightings

The gate scans three families of positive weights over broad parameter ranges:

```text
rational:
  w_n = 1/(1+mu*spin_cost_n)

exponential:
  w_n = exp(-mu*spin_cost_n)

inverse-shift:
  w_n = 1/(mu+spin_cost_n).
```

Across all tested values of `mu`, every scan keeps the same positive sign as the unweighted kernel.

Examples:

```text
rational, mu=0.01:
  Delta = 2.658697729012391

rational, mu=100:
  Delta = 0.021461903950335686

exponential, mu=5:
  Delta = 8.37700858962359e-7

inverse-shift, mu=0.01:
  Delta = 0.6938538160697034

inverse-shift, mu=100:
  Delta = 0.026225935027539737.
```

The normalized `Delta/II` ratio remains positive in all these controls.

Therefore ordinary monotone suppression by a coarse spin-excitation cost does **not** remove the orientation-vs-shape split in the tested families.

---

## 5. What a sign flip would require

Because the cone is mixed, a physical positive diagonal resolvent can in principle produce

```text
Delta_eff = 0
```

or change its sign.

But it cannot do so merely by assigning a generic monotone penalty to larger spin cost within the tested families.

It must distinguish the negative four-edge/intertwiner sector from the dominant positive three-edge sector more selectively.

That makes the next calculation concrete:

```text
classify the 648 states by actual geometric observables
(volume, affected-node volume spectrum, shape/intertwiner channel, support pattern)
```

and test whether the physically motivated constrained resolvent preferentially weights the negative class.

---

## 6. What is and is not proved

### Tested finite

- exact state-by-state reconstruction of the environment-unbiased return kernel;
- 648 nonzero intermediate contributions;
- mixed positive/negative anisotropy cone;
- canonical unweighted `Delta_aniso,ret=2.7384586608827632`;
- all tested monotone spin-cost weighting families retain positive `Delta`.

### Not proved

- the actual constrained-gravity Feshbach/Schrieffer-Wolff resolvent;
- that every physically admissible positive weighting retains the sign;
- a static physical mass/gap;
- the RG flow of the weighted anisotropy under recursive PL refinement.

So the correct conclusion is

```text
arbitrary positive diagonal weighting:
  sign not protected

simple monotone spin-cost weighting:
  positive sign robust in tested families

physical answer:
  requires geometric/intertwiner-sensitive resolvent.
```

---

## Reproduction

```bash
python scripts/peter_weyl_anisotropy_weight_robustness_gate.py \
  --output verification_results/PETER_WEYL_ANISOTROPY_WEIGHT_ROBUSTNESS.json
```
