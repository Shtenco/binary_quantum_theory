# Dimensionless master criterion for mirror repulsion

Status: **exact algebraic reduction of the healthy mirror-force conditions; microscopic inputs remain open**.

The mirror branch now has separate gates for

```text
Sigma order
Z_sigma spatial stiffness
beta_m matter matrix element
Delta_sigma mirror-odd spectral gap
```

so the force condition can be written without treating `alpha` as an independent parameter.

---

## 1. Dimensionless microscopic ratios

For the regular tetrahedral normalization define

```text
g_* = G J/ell
```

and

```text
j_sigma = J ell/(hbar c_sigma).
```

Also define

```text
R = r/ell
```

and write the physical mirror-mode gap as

```text
Delta_sigma = delta_sigma J.
```

If the refined mode has low-energy propagation speed `c_sigma`, then

```text
x = m_sigma r
  = Delta_sigma r/(hbar c_sigma)
  = delta_sigma j_sigma R.
```

---

## 2. alpha is no longer independent

The Hodge matching gives

```text
Z_sigma=(2*sqrt(2)/3) J/ell.
```

The canonical force normalization is

```text
alpha=beta_m^2/(4*pi*G*Z_sigma).
```

Substitution yields

```text
alpha
 = 3 beta_m^2
   /(8*sqrt(2)*pi*g_*).
```

Thus, once the microscopic matter response `beta_m` and the dimensionless gravity/gluing ratio `g_*` are known, `alpha` is fixed.

---

## 3. One master inequality

Opposite-`chi` repulsion requires

```text
alpha(1+x)exp(-x) > 1.
```

Using the reduced `alpha`, this is exactly equivalent to

```text
beta_m^2
 > (8*sqrt(2)*pi/3)
   * g_*
   * exp(x)/(1+x),
```

with

```text
x=delta_sigma j_sigma R.
```

Therefore the complete dimensionless force criterion is

```text
beta_m^2
 > (8*sqrt(2)*pi/3)
   g_*
   exp(delta_sigma j_sigma R)
   /(1+delta_sigma j_sigma R).
```

This is the main master equation of the current mirror-force branch.

---

## 4. Independent range condition

Before strength matters, the mediator must reach the requested distance.

A simple order-one range requirement is

```text
x <= 1.
```

Therefore

```text
j_sigma
 <= 1/(delta_sigma R).
```

This makes the finite seed result immediately informative.

At the deep ordered 16-cell point,

```text
delta_sigma ~= 7.97009.
```

For a distance `R=r/ell`, the corresponding necessary range condition is approximately

```text
j_sigma <= 0.12547/R.
```

Even at the softest checked finite-Q4 mirror-odd point,

```text
delta_sigma ~= 5.58411,
```

so

```text
j_sigma <= 0.17908/R.
```

Thus a truly macroscopic `R` requires a parametrically small refined gap/speed ratio. The finite seed does not provide that automatically.

---

## 5. Matter-side form

The general mirror-mass theorem gives

```text
beta_m
 = d ln m_+(sigma)/d sigma |_(sigma=v)
```

with the opposite mirror branch carrying the negative derivative.

The master inequality can therefore be written directly as a condition on a microscopic mass eigenvalue:

```text
|d ln m/dsigma|_vac^2
 > (8*sqrt(2)*pi/3)
   g_*
   exp(delta_sigma j_sigma R)
   /(1+delta_sigma j_sigma R).
```

This is the form to use once a real microscopic matter Hamiltonian `H_m(sigma)` is built.

---

## 6. Exact PASS/FAIL structure

At a requested dimensionless distance `R`, the branch must satisfy all of

```text
1. beta_m != 0
2. x=delta_sigma j_sigma R <= O(1)
3. beta_m^2 > (8*sqrt(2)*pi/3) g_* exp(x)/(1+x)
4. positive-energy stable Hamiltonian
5. closed enlarged HDA.
```

No choice of the phenomenological symbol `alpha` can bypass these requirements.

---

## 7. What remains genuinely microscopic

The master equation removes `alpha` as an independent unknown, but it does not determine:

- `beta_m`, which must come from the mirror-resolved rest spectrum;
- `g_* = GJ/ell`, which requires absolute gravity/gluing scale matching;
- `j_sigma`, which requires the refined temporal/propagation normalization;
- `delta_sigma` in the continuum/refined mirror-odd sector.

These are now the only quantities required by the force inequality itself.

---

## Reproduction

```bash
python scripts/mirror_master_criterion_gate.py \
  --output verification_results/MIRROR_MASTER_CRITERION.json
```
