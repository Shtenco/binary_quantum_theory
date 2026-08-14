# Healthy orientation-odd sector: HDA construction and mirror-force threshold

Status: **continuum canonical construction + finite HDA control + healthy mirror-force candidate; microscopic Peter-Weyl embedding still open**.

The mirror calculation established an exact orientation bit

```text
chi = sign(Q) = +/-1
```

with `Q ~ Y_L`, but also established the negative result

```text
g00(+chi) = g00(-chi)
```

inside the current mirror-even metric sector. This note asks the next admissible question:

> can one build a nontrivial `chi`-dependent interaction that is stable and compatible with the hypersurface-deformation algebra, without identifying mirror orientation with negative energy?

The answer is **yes at the continuum candidate level**, but the healthy construction is not a literal sign flip of the Einstein metric. It is an additional mirror-charge mediator whose force can screen or overcome tensor gravity between opposite orientation sectors.

---

## 1. First no-go: multiplying the gravity Hamiltonian by a mirror sign

Take the simplest imaginable branch

```text
H_chi[N] = s_chi H_GR[N]
```

with constant `s_chi` in one superselection sector.

If the ordinary constraint satisfies

```text
{H_GR[N], H_GR[M]} = D[beta]
```

then

```text
{H_chi[N], H_chi[M]} = s_chi^2 D[beta].
```

Keeping the same diffeomorphism generator and lapse normalization requires

```text
s_chi^2 = 1.
```

Thus only

```text
s = +1
s = -1
```

preserve the same HDA normalization.

But `s=-1` is just

```text
H[N] -> -H[N] = H[-N]
```

which reverses the orientation of normal evolution / time. It does **not** reverse a static Newtonian force.

So

```text
H -> -H
```

is not a healthy antigravity mechanism.

---

## 2. Second no-go: negative Einstein-Hilbert coefficient

A more aggressive attempt is to make the effective coefficient in front of `R` negative in the mirror branch, schematically

```text
S_grav ~ F_chi * integral sqrt(-g) R
```

with

```text
F_- < 0.
```

This can formally flip the sign associated with an effective Newton coupling, but the same coefficient multiplies the linearized graviton kinetic term.

Therefore

```text
F_- < 0
```

also means a negative graviton kinetic energy relative to ordinary positive-energy matter: a ghost instability.

So direct metric-sign antigravity is not obtained for free. The sign flip that would look attractive phenomenologically destroys the healthy tensor sector.

This is why the viable construction below keeps the Einstein-Hilbert coefficient positive.

---

## 3. Mirror order parameter from the microscopic orientation bit

The microscopic gate already has

```text
Q = (sqrt(3)/4) Y_L
chi = sign(Q).
```

At coarse scales introduce a pseudoscalar order parameter `sigma(x)` whose two mirror vacua represent the two orientations:

```text
sigma ~ +v   -> chi=+1
sigma ~ -v   -> chi=-1.
```

Mirror acts as

```text
sigma -> -sigma.
```

Now introduce a second pseudoscalar field `phi`, also mirror odd:

```text
phi -> -phi.
```

The product

```text
phi * sigma
```

is mirror even.

This allows an ordinary scalar Hamiltonian density without putting a negative sign into the metric kinetic term.

---

## 4. Minimal stable candidate action

Use

```text
S = integral sqrt(-g) [
      Mpl^2 R / 2
    - (d phi)^2 / 2
    - (d sigma)^2 / 2
    - U(phi,sigma)
]
```

with

```text
U(phi,sigma)
 = mu^2 phi^2 / 2
 + lambda phi^4 / 4
 + g phi sigma
 + kappa (sigma^2-v^2)^2 / 4.
```

For

```text
mu^2 > 0
lambda > 0
kappa > 0
```

both fields have positive canonical kinetic terms and the quartics make the potential bounded at large field amplitude.

The full mirror transformation

```text
(phi,sigma) -> (-phi,-sigma)
```

leaves the action invariant.

Thus the two orientation branches can be related by an exact `Z2` mirror symmetry without introducing negative excitation energies.

---

## 5. Canonical HDA identity of the new sector

In one spatial dimension, used only as a clean finite control of the canonical principal identity, take

```text
H[N] = integral dx N [
    p_phi^2/2 + (phi')^2/2
  + p_sigma^2/2 + (sigma')^2/2
  + U(phi,sigma)
].
```

Functional differentiation gives

```text
dH[N]/dp_phi   = N p_phi
dH[N]/dphi     = -(N phi')' + N U_phi

dH[N]/dp_sigma = N p_sigma
dH[N]/dsigma   = -(N sigma')' + N U_sigma.
```

In the antisymmetric Poisson bracket, every local potential term cancels:

```text
N M U_phi - M N U_phi = 0
N M U_sigma - M N U_sigma = 0.
```

What remains is exactly

```text
{H[N],H[M]}
 = D[ N M' - M N' ]
```

with

```text
D[beta]
 = integral dx beta (p_phi phi' + p_sigma sigma').
```

The executable spectral gate uses `L=512` and obtains

```text
H-H bracket = 0.0007282211771021175
D target    = 0.0007282211771021123
abs error   = 5.204170427930421e-18
rel error   = 7.146414566848946e-15
```

So the new orientation/mirror matter sector passes the canonical HDA principal identity to machine precision.

This is a continuum matter-sector control. The full microscopic Peter-Weyl x route x orientation-sector quantum HDA is still a separate gate.

---

## 6. The healthy source is an orientation charge, not negative mass

For a coarse object define an orientation charge

```text
Q_chi = eta * m * chi.
```

The charge changes sign under mirror orientation while the inertial/rest mass `m` stays positive.

Exchange of the canonical mediator gives the Yukawa potential

```text
U_12(r)
 = -G_T m1 m2 / r
   - alpha G_T m1 m2 chi1 chi2 exp(-m_phi r) / r,
```

where `G_T` is the tensor-gravity coupling and `alpha` is the dimensionless strength of the orientation force relative to it.

For equal orientation,

```text
chi1 chi2 = +1
```

so the new channel is attractive.

For opposite orientation,

```text
chi1 chi2 = -1
```

so the new channel is repulsive.

No negative mass is needed.

---

## 7. Exact screening and repulsion threshold

Let

```text
x = m_phi r.
```

The magnitude of the Yukawa force relative to bare tensor gravity is

```text
F_chi / F_T
 = alpha (1+x) exp(-x).
```

For opposite mirror charges, the total radial force changes sign when

```text
alpha (1+x) exp(-x) > 1.
```

Therefore the exact screening threshold is

```text
alpha_crit(x) = exp(x)/(1+x).
```

Examples:

| `m_phi r` | `alpha_crit` |
|---:|---:|
| 0.0 | 1.0000000000 |
| 0.1 | 1.0047008346 |
| 0.5 | 1.0991475138 |
| 1.0 | 1.3591409142 |
| 2.0 | 2.4630186996 |
| 5.0 | 24.7355265171 |

So in the long-range limit

```text
m_phi r << 1
```

we get the particularly simple rule

```text
alpha = 1   -> complete screening
alpha > 1   -> opposite-chi repulsion.
```

A demonstration point used by the gate is

```text
alpha = 2
m_phi r = 0.1.
```

It gives

```text
orientation repulsion / bare tensor gravity = 1.990642319679...
net opposite-chi outward force / bare tensor gravity = 0.990642319679...
```

So a mathematically healthy repulsive **cross-sector** interaction can exceed Newtonian attraction without a negative-energy mediator.

---

## 8. Important reinterpretation: this is not yet `g00 -> -g00`

The construction above does **not** make the Einstein metric itself change sign under `chi`.

Instead it gives

```text
tensor gravity
+
mirror-charge force.
```

Thus it is best described at this stage as

```text
antigravity-like cross-sector repulsion
```

or a

```text
mirror fifth force.
```

This is actually the healthier result: the tensor graviton remains positive-energy and the new repulsion is carried by a separate canonical field.

A literal mirror-dependent `g00` response would still require a scalar-tensor, bimetric or other modified-geometric embedding and a fresh HDA/stability analysis.

---

## 9. Why a pseudoscalar mediator is natural here

The microscopic orientation coordinate is parity odd:

```text
Y_L -> -Y_L.
```

The coarse order parameter `sigma` is therefore naturally pseudoscalar.

Choosing `phi` pseudoscalar makes

```text
phi sigma
```

parity even, so the mediator can couple to the orientation sector without explicitly breaking the mirror symmetry.

The same `sigma` can in principle couple to fermionic axial/pseudoscalar bilinears, giving a common bridge between

```text
microscopic orientation
 -> chirality
 -> mirror charge
 -> parity-sensitive force.
```

That is more coherent than identifying ordinary antimatter with negative mass.

---

## 10. Relation to known parity-odd gravity structures

A constant-coefficient gravitational Pontryagin term is topological and does not create a static Newtonian sign flip. If its coefficient is promoted to a dynamical pseudoscalar, as in dynamical Chern-Simons-type constructions, parity-sensitive dynamics becomes physical, especially in rotating/gravitomagnetic and gravitational-wave sectors.

This supports the general strategy of adding a dynamical pseudoscalar rather than flipping the sign of the Einstein kinetic term.

It does **not** prove the specific CIMFIG orientation-force coupling.

Useful primary literature:

- S. Alexander and N. Yunes, *Chern-Simons Modified General Relativity*, arXiv:0907.2562.
- M. Bojowald and R. Das, *Canonical Gravity with Fermions*, arXiv:0710.5722.
- D. Benedetti and S. Speziale, *Perturbative quantum gravity with the Immirzi parameter*, arXiv:1104.4028.

---

## 11. What is closed by this construction

### Exact / analytic

- `H_chi=s H_GR` preserves the same HDA normalization only for `s^2=1`;
- `s=-1` is normal/time-orientation reversal, not static antigravity;
- a negative Einstein-Hilbert coefficient gives the wrong graviton kinetic sign;
- the two-pseudoscalar local potential cancels out of the antisymmetric matter `H-H` bracket;
- opposite orientation Yukawa charges repel;
- the exact screening threshold is `alpha_crit=exp(x)/(1+x)`.

### Finite numerical

- the spectral two-field HDA identity passes with relative error about `7.15e-15`;
- the gate reproduces all screening thresholds and the long-range `alpha=1` boundary.

### Still conditional

- deriving `sigma` as a real coarse mode of microscopic `Y_L/Q` rather than postulating it;
- deriving `phi` and the charge-to-mass coupling `eta` from the route/Peter-Weyl dynamics;
- demonstrating a coherent nonzero macroscopic orientation charge rather than cancellation of random microscopic orientations;
- embedding the new Hamiltonian into the quantum geometry x route constraint and closing its full off-shell HDA;
- experimental compatibility with fifth-force, equivalence-principle and cosmological constraints;
- a literal mirror-dependent metric response, if desired, rather than an extra force.

---

## 12. New bottleneck

The previous question

```text
can chirality alone flip gravity?
```

has been answered negatively.

The next question is now sharply constructive:

```text
microscopic Y_L/Q
 -> coarse sigma
 -> orientation charge Q_chi
 -> positive-kinetic mediator phi
 -> alpha
 -> mirror repulsion
 -> microscopic quantum HDA
```

The key number to derive from first principles is

```text
alpha = orientation-force strength / tensor-gravity strength.
```

If the microscopic theory predicts

```text
alpha <= 1
```

in the long-range regime, there is no cross-sector antigravity.

If it predicts

```text
alpha > 1
```

while the Hamiltonian remains bounded and the enlarged quantum HDA closes, the candidate theory has a genuine stable mirror-repulsion mechanism.

---

## Reproduction

```bash
python scripts/orientation_odd_hda_gate.py \
  --L 512 \
  --output verification_results/ORIENTATION_ODD_HDA.json
```
