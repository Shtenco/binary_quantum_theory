# Theory status — canonical ledger

**Frozen 2026-08-14.** This file supersedes historical frontier wording elsewhere in the repository.

The project is a **candidate theory**, not an experimentally established theory of nature.

---

## 1. Closed core candidate chain

The frozen structural chain is

```text
bits
 -> q=2
 -> local octahedral S2
 -> minimal/recursive PL S3
 -> 3D slice scaling
 -> z~1
 -> 4D-like history
 -> smooth IR
 -> SU(2)/Peter-Weyl quantum geometry
 -> H_E
 -> K=[V,H_E]
 -> C(V), C(K)
 -> H_E+(1+beta^2)H_L
 -> route-normal generator
 -> HDA composition certificate.
```

Frozen numerical anchors include

```text
d_H          = 2.999229782
z            = 0.998281156
d_s(slice)   = 3.004393867
d_s(history) ~ 4.004393867
```

and the preregistered two-node Euclidean geometry x route residual

```text
Delta_joint(1/64)=0.014707752821092098.
```

For all-`j=1/2` input, the full Lorentzian HH support is safe at `Jmax=13/2`.

At fixed safe cutoff,

```text
C_cross/D = O(epsilon)
C_GG/D    = O(epsilon^2)
```

so

```text
Delta_full
 <= Delta_route
  + C_cross epsilon
  + C_GG epsilon^2
 -> 0.
```

The admissible simultaneous cutoff estimate remains

```text
Jmax=o(epsilon^-2/13),
```

not a uniform theorem for every possible joint path.

---

## 2. Spin-2 / foam extension

Four spin-`1/2` qubits contain one exact `j=2` irrep. The extremal `m=+/-2` states pass the finite projector gate and provide the exact finite carrier for a candidate massless spin-2 helicity qubit after the usual TT/gauge reduction.

The foam inference

```text
P_foam(k)~k^1.003414
```

remains conditional on interpreting the frozen smoothing defect exponent as a quantum RMS exponent.

The GW-driven information-mode resonance also remains conditional on a nonzero microscopic TT coupling.

---

## 3. Exact mirror/chirality result

On the two-dimensional logical geometry qubit,

```text
X -> +X
Z -> +Z
Y -> -Y
Q_orientation=(sqrt(3)/4)Y.
```

Mirror conjugation flips orientation while preserving the intrinsic metric/shape data and absolute volume.

Therefore the currently tested mirror-even metric architecture gives

```text
g00(+chi)=g00(-chi).
```

So mirror orientation by itself does **not** produce metric antigravity.

Two simple sign-flip routes are also excluded as healthy mechanisms:

```text
H -> -H
```

is lapse/time-orientation reversal, while a negative Einstein-Hilbert coefficient gives a wrong-sign graviton kinetic term relative to positive-energy matter.

The perturbative cubic gauge-anomaly coefficient changes sign under conjugate representation, but realistic chiral matter and all global anomalies remain open.

---

## 4. Microscopic mirror order

The 16 tetrahedra of the minimal 16-cell have dual graph `Q4`.

With

```text
eta_v=(-1)^popcount(v)
sigma_v=eta_v Y_v
Sigma=(1/16)sum_v eta_v Y_v,
```

the alternating local orientation rule becomes uniform staggered order.

The two exact mirror vacua are

```text
Sigma=+1
Sigma=-1.
```

A local orientation defect costs `8J`; a half-hypercube domain wall costs `16J`.

At `h/J=0.2`, the full `2^16=65536` transverse-field control gives

```text
<Sigma^2>=0.997653947371...
```

with an unresolved-at-machine-scale mirror doublet splitting.

The bipartite staggered structure persists through the checked PL refinement family

```text
16 -> 384 -> 9216 tetrahedra.
```

Thus

```text
Y_L/Q -> staggered Sigma -> coarse sigma(x)
```

has a finite microscopic candidate.

---

## 5. Healthy positive-energy mirror-force branch

A canonical positive-kinetic mirror sector reproduces the matter HDA principal identity at relative defect

```text
7.146414566848946e-15.
```

For a light one-particle mirror mode,

```text
V_sigma(r)
 = - beta_1 beta_2 m1 m2 chi1 chi2
   exp(-m_sigma r)/(4*pi*Z_sigma*r).
```

Relative to tensor gravity,

```text
alpha=beta_m^2/(4*pi*G*Z_sigma).
```

The exact opposite-charge screening threshold is

```text
alpha_crit(x)=exp(x)/(1+x),
x=m_sigma r.
```

The existing circumcentric Hodge geometry fixes the spatial stiffness matching

```text
J_f=Z_sigma A_f/d_f.
```

For a regular tetrahedral seed,

```text
Z_sigma=(2sqrt(2)/3)J/ell
```

and therefore

```text
alpha
 = 3 beta_m^2 ell
   /(8sqrt(2)pi GJ).
```

Pure geometry has no automatic linear mirror charge: `beta_geometry=0`.

---

## 6. Matter matrix element

The earlier axial bridge remains useful for chirality/spin-sensitive physics but fails as a universal static cold-matter source:

```text
J5^0/J^0=h|p|/E,
```

so it vanishes at rest and averages to zero in unpolarized matter. The diagonal on-shell pseudoscalar bilinear also vanishes.

The static matter coefficient is now operationally defined by Hellmann-Feynman:

```text
beta_m
 = (1/(chi m))
   <dH_m/dsigma>_rest.
```

If this derivative vanishes for every physical matter state, then

```text
beta_m=0
alpha=0
```

and the one-particle static mirror-force branch fails.

For any mirror-covariant positive rest spectrum

```text
m_q(sigma)=m_-q(-sigma),
```

aligned mirror partners automatically have equal positive masses and opposite `sigma` derivatives.

A concrete Wilson-Dirac carrier has been finite-tested. It supports equal positive mirror spectra, opposite Hellmann-Feynman rest charges and standard Wilson corner-doubler removal simultaneously. Its numerical `beta_m` is still an input, not a derived Standard-Model prediction.

---

## 7. Massive Ising range is a conservative negative control

The mirror order is `Z2`, so the tiny finite mirror-doublet splitting is tunnelling, not a mediator mass.

After exact global parity resolution, the first additional `Sigma`-coupled odd excitation is

```text
Delta_sigma,odd/J
 = 7.9700878769647...
```

at `h/J=0.2`, and the softest checked finite-Q4 value is about

```text
5.58410566853 J.
```

The earlier raw `E2-E0 ~= 3.39685J` at `h/J=2.625` is not the physical `Sigma` spectral gap because it has the wrong parity.

The symmetry-resolved Lehmann expansion also supplies a finite-block temporal response, but not yet a continuum physical `m_sigma`.

---

## 8. Exact Bell-gluing Heisenberg parent

The frozen Bell-gluing term

```text
-J(XX-YY+ZZ)
```

is exactly mapped on the bipartite dual graph, by a `pi` rotation around logical `Y` on one sublattice, to

```text
+J(XX+YY+ZZ).
```

Thus the mirror order sits inside an antiferromagnetic Heisenberg pseudospin parent.

On the exact Q4 16-qubit parent,

```text
E0/J=-44.9139328337...
first triplet gap/J=2.31439334306...
```

with substantial staggered Neel correlations.

The recursive degree-four dual graphs also show a strongly softening graph spin-wave scale.

However this `SU(2)` is a property of the Bell-gluing parent, not yet a symmetry of the complete geometry dynamics.

---

## 9. Exact S4 coarse symmetry

The exact face-permutation twirl gives

```text
one-cell:
  only I survives

two-cell invariant space:
  span{II, XX+ZZ, YY}.
```

Therefore full tetrahedral face symmetry permits one and only one coarse pseudospin split:

```text
Delta_aniso
 = J_orientation-J_shape.
```

Tetrahedral symmetry and mirror `Z2` do **not** force `Delta_aniso=0`.

---

## 10. Decisive Peter-Weyl logical anisotropy result

Let `P` project to the all-`j=1/2` logical sector.

The fundamental holonomy support rule gives and the finite gate verifies

```text
P H_E P = 0
```

exactly on all 32 logical columns of the unbiased environment calculation.

Thus there is no first-order logical field or mirror splitting from `H_E`.

The first nonzero structural return object is

```text
K_ret
 = (1/8)Tr_{2,3,4}
   P(H_E,0+H_E,1)^2P.
```

This maximally mixed environment trace removes the earlier `K_2=K_3=K_4=0` shape bias.

The mirror-forbidden odd-`Y` Pauli channels remain suppressed to relative norm

```text
3.1887751872821285e-17.
```

So mirror `Z2` survives.

But in the Heisenberg frame the environment-unbiased coupling tensor is approximately

```text
[
  [-0.5020918898, 0, -0.6892178651],
  [ 0,            2.5842530087, 0],
  [+0.6892178651, 0, -1.6958521572]
].
```

The relative pseudospin anisotropy is

```text
A_rel=0.9627752706476244.
```

After exact `S4` twirling,

```text
J_shape  = -1.0989720235137607
J_orient = +2.5842530086520437
```

so

```text
Delta_aniso,ret
 = 3.6832250321658044.
```

Therefore the Bell-parent `SU(2)` is strongly broken in the first nonzero Euclidean Peter-Weyl return channel, while mirror `Z2` remains intact.

`K_ret` is **not** yet a static Schrieffer-Wolff Hamiltonian. Without a justified constrained resolvent it must not be called a physical mass gap.

It does have an exact short-time meaning because `P H_E P=0`:

```text
P exp(-itH_E)P
 = P - t^2 K_ret/2 + O(t^3),
```

so

```text
P_leak(t|psi)
 = t^2 <psi|K_ret|psi> + ... .
```

Thus the anisotropy is already a tested state-dependent short-time logical leakage anisotropy.

---

## 11. Route logical metric and ordering

The logical flux metric has only

```text
I,X,Z
```

components and no `Y`, so it is exactly mirror even.

For isotropic route-direction averaging, the linear metric contraction becomes scalar.

In the currently frozen expectation-first square-root control,

```text
<omega>_K=0
 = <omega>_K=2
 = 0.8598466001022401.
```

So the frozen averaged route gate does not itself establish a `K=0/K=2` split.

An operator-first spectral square-root ordering retains a finite `X/Z` component of norm

```text
0.04007491854520556.
```

Therefore additional route pseudospin anisotropy is an operator-ordering question that must be closed together with HDA; mirror `Z2` remains protected in both controls.

---

## 12. Conditional Goldstone branch has a different radial law

Even if an emergent Heisenberg symmetry reappears in the IR and a Neel vacuum selects the physical mirror `Y` direction,

```text
Sigma_Y
 = v-(pi_x^2+pi_z^2)/(2v)+...
```

has no one-Goldstone matrix element.

For a purely longitudinal mirror source, the leading free massless channel is two-Goldstone exchange:

```text
V_2G(r)
 = -Q1Q2/(32*pi^3*v^2*r^3).
```

Opposite charges repel, but

```text
F_2G ~ r^-4,
```

not Newton-like `r^-2`.

Therefore a `1/r` mirror potential still requires a light one-particle pole or a microscopic source that couples linearly to a transverse mode.

---

## 13. MIRRORMASTER massive one-particle criterion

For the light one-particle/Yukawa branch define

```text
g_*=GJ/ell
j_sigma=J ell/(hbar c_sigma)
R=r/ell
Delta_sigma=delta_sigma J.
```

Then

```text
alpha
 = 3 beta_m^2/(8sqrt(2)pi g_*),
```

and

```text
x=m_sigma r=delta_sigma j_sigma R.
```

Opposite-charge repulsion is equivalent to

```text
beta_m^2
 > (8sqrt(2)pi/3)
   g_*
   exp(x)/(1+x).
```

Thus `alpha` is not an independent force knob.

---

# Current single mirror frontier

The old frontier

```text
find m_sigma
```

is superseded.

The primary dynamical question is now

```text
Delta_aniso^eff
 = J_orientation^eff-J_shape^eff
 -> 0 ?
```

under the physically correct constrained intermediate-state weighting and PL/RG flow.

The immediate hierarchy is

```text
1. resolve the constrained/resolvent weighting of Peter-Weyl intermediate states;
2. determine the RG flow of Delta_aniso^eff;
3. if Delta_aniso^eff != 0:
      determine the anisotropic/massive mirror spectrum and use the one-particle MIRRORMASTER criterion if a light pole exists;
4. if Delta_aniso^eff -> 0:
      test the emergent continuous branch, remembering that a longitudinal source begins at two-Goldstone r^-3 potential;
5. derive a realistic microscopic beta_m and physical scale g_*;
6. close the full Peter-Weyl x route x mirror-matter HDA.
```

The current executable robustness test is

```text
scripts/peter_weyl_anisotropy_weight_robustness_gate.py.
```

It decomposes `Delta_aniso,ret` state by state and asks whether **any positive state-diagonal weighting** can change its sign.

---

## Other open questions beyond the fixed-cutoff core

Still separate and genuinely open:

- a fully uniform arbitrary-path `Jmax->infinity`, `epsilon->0` theorem;
- Lorentzian quantum history measure/global unitarity;
- a microscopic TT information-mode action/coupling;
- realistic gauge group, generations, chirality, Yukawa structure and all local/global anomalies;
- absolute Newton/length/time scale setting;
- blind physical predictions and observational comparison;
- independent external replication.
