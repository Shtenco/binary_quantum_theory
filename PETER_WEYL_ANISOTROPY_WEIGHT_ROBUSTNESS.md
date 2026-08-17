# Peter-Weyl anisotropy: audited intermediate-state decomposition

Status: **tested finite accounting certificate + representation/volume fingerprint; physical constrained resolvent remains open**.

The environment-unbiased logical geometry-qubit return kernel is

```text
K_ret=(1/8) Tr_env P(H_E,0+H_E,1)^2P.
```

The canonical S4-reduced structural anisotropy is

```text
Delta_aniso,ret=2.738458660882762.
```

It is a return/leakage coefficient, not a proved low-energy mass or interaction parameter.

---

## 1. Hard accounting certificate

The canonical gate

```text
scripts/peter_weyl_anisotropy_resolvent_audit_gate.py
```

constructs the direct 32-column kernel and the individual intermediate-state contributions `K_n` in the same run and requires

```text
||sum_n K_n-K_direct|| < 1e-10.
```

The current finite result is

```text
intermediate states             = 648
matrix reconstruction error     = 8.606528098114035e-15
Delta direct                    = 2.738458660882762
Delta reconstructed             = 2.7384586608827632
sum state Delta                 = 2.7384586608827624
sum class Delta                 = 2.7384586608827624
II direct                       = 9.04524203998966
II reconstructed                = 9.045242039989661.
```

Thus the state decomposition is certified at machine precision for this finite gate.

---

## 2. Correct sign cone

The audited cone is

```text
positive states = 392
negative states = 256
zero states     = 0

sum(delta_n>0) = +4.052816595873667
sum(delta_n<0) = -1.3143579349909067.
```

Therefore the cone is mixed. There is no theorem that an arbitrary positive state-diagonal weighting preserves the sign of `Delta_aniso`.

This does not license arbitrary denominator tuning: the actual weighting must come from the constrained dynamics.

---

## 3. Why the old spin-cost scan was vacuous

Every one of the 648 actual intermediate states has

```text
spin_cost     = 3
changed_edges = 3.
```

Therefore for any weighting of the form

```text
w_n=f(spin_cost_n)
```

all weights are equal and

```text
K_w=c K_ret,
Delta_w=c Delta_ret.
```

Such a scan is only an overall rescaling, not an independent robustness test.

---

## 4. Exact raising/lowering channel structure

Starting from `j=1/2`, one Euclidean action changes exactly three edge spins. Each changed edge is either

```text
j=1/2 -> 0   (lower)
j=1/2 -> 1   (raise).
```

Grouping the audited states by the number of raised and lowered edges gives

| raised | lowered | states | total Delta | total II | Delta/II |
|---:|---:|---:|---:|---:|---:|
| 0 | 3 | 36  | `+0.2734514505369862` | `0.4226067871935240` | `+0.647058823529412` |
| 1 | 2 | 108 | `+0.1242961138804483` | `0.6214805694022404` | `+0.2` |
| 2 | 1 | 216 | `-0.3715029773216430` | `1.5724624665804985` | `-0.2362555451829125` |
| 3 | 0 | 288 | `+2.712214073786969` | `6.428692216813412` | `+0.4218920399849792` |

The only net-negative one-hit representation channel is

```text
2 raises + 1 lowering.
```

For the SU(2) Casimir `j(j+1)`, the total one-hit Casimir shifts of these four channels are respectively

```text
-9/4, -1/4, +7/4, +15/4.
```

These are kinematic labels only; they are not physical energy denominators.

---

## 5. Volume is not the sign selector

The audited local-volume fingerprint shows strong overlap between positive and negative sectors.

```text
positive: count=392, <V_total>=2.7747718761477116
negative: count=256, <V_total>=2.6299746617864215
```

Both sectors occupy a broad overlapping volume range and both contain states with zero-volume nodes.

Diagnostic weights such as

```text
exp(-mu V_total)
1/(1+mu V_total)
```

remain positive in the tested controls; for example

```text
exp(-10 V_total): Delta=7.653856275172428e-7 > 0.
```

This establishes only the narrower result that `V_total` alone does not isolate the negative representation channel in this finite habitat.

---

## 6. Correct next question

The actual problem is to derive the constrained intermediate-state operator itself.

A physically meaningful effective kernel must follow from the same quantum constraint dynamics and then be tested through refinement/RG, rather than being chosen to preserve a desired sign.

---

## Reproduction

```bash
python scripts/peter_weyl_anisotropy_resolvent_audit_fast_gate.py \
  --output verification_results/PETER_WEYL_ANISOTROPY_RESOLVENT_AUDIT.json
```

Compatibility entry point:

```bash
python scripts/peter_weyl_anisotropy_weight_robustness_gate.py \
  --output verification_results/PETER_WEYL_ANISOTROPY_WEIGHT_ROBUSTNESS.json
```

---

## Scientific scope

This is a finite calculation inside the candidate quantum-geometry model. It establishes an audited decomposition of a return kernel and its representation/volume fingerprints. It does not establish a new particle, force, matter sector, mediator scale or macroscopic interaction.
