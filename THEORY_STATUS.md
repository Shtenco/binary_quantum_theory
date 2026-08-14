# Theory status — canonical ledger

**Frozen working frontier: 2026-08-14.**

This repository develops a **candidate theory**. It is not an experimentally established theory of nature, does not establish antigravity, and does not establish a physical mirror particle or fifth force.

This file is the human-readable canonical status surface. Historical frontier notes remain useful as derivation records but do not override this ledger.

---

## 1. Closed fixed-cutoff core candidate chain

The currently frozen structural chain is

```text
bits
 -> q=2
 -> local octahedral S2
 -> minimal/recursive PL S3
 -> 3D slice scaling
 -> z~1
 -> 4D-like history
 -> smooth IR
 -> SU(2)/Peter-Weyl geometry
 -> H_E
 -> K=[V,H_E]
 -> C(V), C(K)
 -> H_E+(1+beta^2)H_L
 -> route-normal generator
 -> fixed-cutoff HDA composition certificate.
```

Numerical anchors:

```text
d_H          = 2.999229782
z            = 0.998281156
d_s(slice)   = 3.004393867
d_s(history) ~ 4.004393867
```

The preregistered two-node Euclidean geometry x route residual is

```text
Delta_joint(1/64)=0.014707752821092098.
```

For all-`j=1/2` input the full Lorentzian HH hit-depth support is safe at

```text
Jmax=13/2.
```

At fixed safe cutoff the final composition certificate has

```text
C_cross/D = O(epsilon)
C_GG/D    = O(epsilon^2),
```

hence

```text
Delta_full
 <= Delta_route
  + C_cross epsilon
  + C_GG epsilon^2
 ->0.
```

A conservative simultaneous diagonal estimate exists for

```text
Jmax=o(epsilon^-2/13),
```

under the declared nondegenerate fixed-shape assumptions. This is not a theorem uniform over every arbitrary two-parameter path.

---

## 2. q=2 global topology status

The recursive q=2 PL construction provides a global S3 completion.

Under the additional **minimal 8-vertex + flag completion** semantics, octahedral vertex links force the unique graph

```text
K8 minus four antipodal edges,
```

hence the 16 tetrahedra of the 4D cross-polytope boundary (16-cell), up to relabeling.

This is a uniqueness theorem for that minimal flag globalization, not a theorem that the bare causal rewrite uniquely forces the same complex among every larger or nonflag completion.

---

## 3. Spin-2 / foam extension

Four microscopic spin-`1/2` qubits contain exactly one `j=2` irrep:

```text
(1/2)^4 = 2*j=0 + 3*j=1 + 1*j=2.
```

The extremal `m=+/-2` states have zero leakage from the finite `j=2` projector. After the standard massless TT/gauge reduction, the two physical helicities can therefore be carried by a two-state logical polarization sector.

The project-local information/route bosonic mode remains hypothetical. The conditional foam inference

```text
P_foam(k)~k^1.003414
```

requires interpreting the frozen smoothing exponent as a quantum RMS exponent.

The GW-driven Mathieu/Floquet resonance remains conditional on a nonzero microscopic TT quadratic coupling.

---

## 4. Exact mirror/orientation result

On the two-dimensional four-spin singlet geometry qubit,

```text
X -> +X
Z -> +Z
Y -> -Y
Q_orientation=(sqrt(3)/4)Y.
```

Mirror conjugation reverses orientation while preserving the intrinsic shape/metric and absolute volume.

Therefore the tested metric architecture gives

```text
g00(+chi)=g00(-chi).
```

So orientation reversal by itself does **not** produce metric antigravity.

The two naive alternatives remain excluded as healthy mechanisms:

```text
H -> -H
```

is lapse/time-orientation reversal, while a negative Einstein-Hilbert kinetic coefficient produces a wrong-sign graviton relative to ordinary positive-energy matter.

---

## 5. Microscopic mirror order

The 16 tetrahedra of the minimal 16-cell have dual graph `Q4`.

With

```text
eta_v=(-1)^popcount(v)
sigma_v=eta_v Y_v
Sigma=(1/16)sum_v eta_v Y_v,
```

the alternating orientation rule becomes uniform staggered order.

The finite model has two exact mirror vacua

```text
Sigma=+1,
Sigma=-1.
```

A local orientation defect costs `8J`; a half-hypercube domain wall costs `16J`.

At `h/J=0.2`, the full `2^16` transverse-field control gives

```text
<Sigma^2>=0.997653947371...
```

with a mirror-doublet splitting below the finite numerical resolution used there.

The staggered bipartite structure persists in the checked recursive PL family

```text
16 -> 384 -> 9216 tetrahedra.
```

Thus

```text
Y_L/Q -> staggered Sigma -> coarse sigma(x)
```

has a finite microscopic carrier.

---

## 6. Bell-gluing Heisenberg parent and its limitation

On every bipartite dual edge,

```text
-J(XX-YY+ZZ)
```

is mapped by a `pi` rotation around logical `Y` on one sublattice to

```text
+J(XX+YY+ZZ).
```

The exact Q4 16-qubit parent has

```text
E0/J=-44.9139328337...
first triplet gap/J=2.31439334306...
```

and substantial staggered Neel correlations.

However this pseudospin `SU(2)` is a property of the Bell-gluing parent, not an exact symmetry of the complete Peter-Weyl dynamics.

---

## 7. Exact logical S4 coarse symmetry

The exact tetrahedral face-permutation twirl gives

```text
one-cell invariant space:
  span{I}

two-cell invariant space:
  span{II, XX+ZZ, YY}.
```

Therefore the unique symmetry-allowed two-cell pseudospin split is

```text
Delta_aniso=J_orientation-J_shape.
```

Full tetrahedral symmetry removes one-cell nonidentity fields and label artifacts, but it does **not** force the two-cell equality

```text
J_orientation=J_shape.
```

Mirror `Z2` and Bell-parent pseudospin `SU(2)` are distinct symmetries.

---

## 8. Corrected Euclidean Peter-Weyl logical return

Let `P` project to the all-`j=1/2` logical sector.

The fundamental support rule gives, and the finite calculation verifies on all 32 logical columns,

```text
P H_E P=0.
```

Thus Euclidean dynamics generates no first-order logical field.

The first nonzero raw return object for neighboring logical nodes 0 and 1 is

```text
K_ret
 =(1/8)Tr_env
  P(H_E,0+H_E,1)^2P.
```

The **canonical corrected** Pauli coefficients before the bipartite `pi-Y` rotation include

```text
II = 9.04524203998966
XX = 0.45691119919191336
YY = 2.18199564892363
ZZ = 0.6560148247263502
XZ = -0.17242879769840605
ZX = -0.17242879769840608.
```

The mirror-forbidden odd-`Y` channels are suppressed to relative norm

```text
2.7985693281119945e-33.
```

After the Heisenberg-frame rotation,

```text
A_rel=0.9644798301915488.
```

After exact `S4` twirling,

```text
J_shape  = -0.5564630119591318
J_orient = +2.18199564892363
Delta_aniso,ret = 2.738458660882762.
```

The older values

```text
3.683225032...
492/156 sign counts
```

are stale and retired.

`K_ret` is a raw short-time/return kernel, **not** a physical static mass Hamiltonian.

---

## 9. Audited 648-state decomposition

The direct 32-column kernel and the state-by-state intermediate decomposition are now reconstructed in the same audited gate.

The exact finite accounting gives

```text
intermediate states         = 648
||sum_n K_n-K_direct||      = 8.606528098114035e-15
Delta direct                = 2.738458660882762
Delta reconstructed         = 2.7384586608827632
II direct                   = 9.04524203998966
II reconstructed            = 9.045242039989661.
```

The corrected sign cone is

```text
positive states = 392
negative states = 256
sum positive Delta = +4.052816595873667
sum negative Delta = -1.3143579349909067.
```

All one-hit intermediate states have

```text
changed_edges=3
spin_cost=3.
```

Therefore the former `spin_cost` weighting scans were only common rescalings and are retired as robustness evidence.

The exact raising/lowering representation channels are

```text
0 raises + 3 lowers : Delta=+0.2734514505369862
1 raise  + 2 lowers : Delta=+0.1242961138804483
2 raises + 1 lower  : Delta=-0.3715029773216430
3 raises + 0 lowers : Delta=+2.712214073786969.
```

The only net-negative representation-flow class is

```text
2 raises + 1 lowering.
```

Total volume alone does not isolate the sign: positive and negative sectors have strongly overlapping volume distributions and both contain zero-volume nodes.

---

## 10. Euclidean master normalization removes the leading raw anisotropy

Define the one-hit map

```text
A=Q H_E P,
K=A^dagger A.
```

For the minimal positive two-shell master normalization,

```text
K_MC(mu)
 = A^dagger(AA^dagger+mu^2 I)^-1 A
 = K(K+mu^2 I)^-1.
```

The canonical `4x4` kernel is full rank with eigenvalues

```text
5.7503203671
7.9640955226
10.8411073380
11.6254449321.
```

Therefore

```text
K_MC(mu)->I
```

as `mu->0`.

The normalized anisotropy scales approximately as

```text
Delta_MC/II ~ 0.04235178 mu^2.
```

This is not an artifact of tracing the logical environment too early.

The full `32x32` logical Gram matrix also has

```text
rank=32/32
lambda_min=4.3060809...
lambda_max=13.3527778...
```

and applying the nonlinear normalization **before** the environment trace still gives

```text
(1/8)Tr_env[K32(K32+mu^2 I)^-1] -> I4
```

with limiting pair anisotropy at numerical zero.

Therefore the raw `H_E^2` anisotropy is **not** currently a leading physical mass candidate.

The next denominator-free Euclidean higher-shell observable is

```text
Lambda_E
 = K^-1/2
   (P H_E^4 P-K^2)
   K^-1/2
 >=0,
```

where the block identity

```text
P H_E^4 P-K^2
 = A^dagger C^dagger C A
```

isolates second-hit leakage from the odd one-hit sector into nonlogical even states.

The algebraic identity is tested; the full Peter-Weyl numerical `Lambda_E` is not yet computed.

---

## 11. Exact doubled-spin parity splits Euclidean and Lorentzian sectors

Define

```text
Pi |{s_e}> = (-1)^(sum_e s_e)|{s_e}>,
s_e=2j_e.
```

Every primitive `H_E` sequence has five fundamental segment hits and flips exactly three edge parity bits, so

```text
{Pi,H_E}=0.
```

The local volume is parity even:

```text
V : even.
```

Hence

```text
K=[V,H_E] : odd.
```

For the covariant leg

```text
C_e(O)=h_e[h_e^-1,O]=O-h_e O h_e^-1,
```

the two fundamental conjugation hits preserve the parity of `O`. Therefore

```text
C(V) : even
C(K) : odd.
```

The declared Lorentzian structural triple

```text
H_L ~ Tr_aux[C(K) C(K) C(V)]
```

is parity even:

```text
[Pi,H_L]=0.
```

For the even logical projector `P`, this gives the exact selection rules

```text
P H_E P=0,
P H_L P is allowed,
P(H_E H_L+H_L H_E)P=0.
```

For

```text
G=H_E+lambda H_L,
lambda=1+beta^2,
```

one gets

```text
P G P=lambda P H_L P,
```

and

```text
P G^2 P
 =P H_E^2 P
 +lambda^2 P H_L^2 P.
```

This makes the direct Lorentzian logical amplitude the present highest-priority full-constraint geometry test.

---

## 12. Current Lorentzian amplitude frontier

The real Peter-Weyl stack already implements the state-to-state sine-ordered structural triple

```text
Tr_aux[C_a(K_sine) C_b(K_sine) C_c(V)]
```

at the single-`H_L` safe wall

```text
Jmax=7/2.
```

The current research gate assembles the full oriented node sum

```text
4 omitted faces x 6 signed permutations = 24 ordered triples
```

and projects the final scalar covariant state back to the all-`j=1/2` Gauss logical sector.

The immediate killer question is

```text
P L_raw,epsilon P = 0 ?
```

where `L_raw,epsilon` denotes the ordered structural K-K-V sum before a final declared Hermitian Lorentzian completion/prefactor.

**Current status in this ledger: calculation running on the research branch. Do not infer a nonzero `P H_L P` until the artifact is green and inspected.**

The raw auxiliary partial trace is operator-valued, so ordinary scalar trace cyclicity cannot be used to infer raw Hermiticity. A final Hermitian Lorentzian ordering must therefore be constructed explicitly after the amplitude test.

If the direct projection vanishes, `Lambda_E` becomes the next geometry source.

If it is nonzero, the next steps are

```text
raw logical return
 -> declared Hermitian H_L completion
 -> unbiased 32D logical/environment projection
 -> S4 two-cell reduction
 -> Delta_aniso^L
 -> refinement/RG.
```

---

## 13. Matter matrix element

The earlier axial density remains a chirality/spin-sensitive channel but fails as a universal static cold-matter source:

```text
J5^0/J^0=h|p|/E.
```

It vanishes in the rest frame and averages to zero in unpolarized matter. The diagonal on-shell pseudoscalar bilinear also vanishes.

The operational static coefficient is

```text
beta_m
 = (1/(chi m))
   <dH_m/dsigma>_rest.
```

For every mirror-covariant positive mass law

```text
m_q(sigma)=m_-q(-sigma),
```

aligned mirror partners have equal positive rest masses and opposite `sigma` derivatives.

A finite Wilson-Dirac carrier demonstrates compatibility of

```text
positive mirror-degenerate spectrum
+ opposite Hellmann-Feynman rest charge
+ Wilson doubler removal.
```

But a realistic numerical `beta_m` is still not derived.

If

```text
beta_m=0
```

for all physical matter states, the one-particle static mirror-force branch fails independently of the geometry range calculation.

---

## 14. Massive Ising branch is a conservative negative control

The tiny finite splitting of the two mirror vacua is tunnelling, not the mediator mass.

After exact global-Z2 parity resolution, the first additional `Sigma`-coupled odd excitation is

```text
Delta_sigma,odd/J=7.9700878769647...
```

at `h/J=0.2`, with the softest checked Q4 value about

```text
5.58410566853 J.
```

Thus the Ising truncation is not automatically long ranged.

The Bell/continuous parent is a distinct control and its physical IR fate is governed by the complete anisotropy/resolvent/RG problem above.

---

## 15. Conditional Goldstone branch has a different radial law

Even if an emergent continuous Neel phase survives in the IR, for a longitudinal physical mirror observable

```text
Sigma_Y
 = v-(pi_x^2+pi_z^2)/(2v)+...
```

there is no one-Goldstone matrix element.

The leading free two-Goldstone static channel is

```text
V_2G(r)
 = -Q1Q2/(32*pi^3*v^2*r^3),
```

so

```text
F_2G~r^-4.
```

Opposite charges repel in this conditional channel, but it is not Newton-like.

A `1/r` mirror potential still requires a light one-particle pole or a microscopic source that couples linearly to a transverse mode.

---

## 16. Healthy one-particle mirror-force criterion

For a positive-kinetic light one-particle mirror mode,

```text
V_sigma(r)
 = -beta_1 beta_2 m1 m2 chi1 chi2
   exp(-m_sigma r)
   /(4*pi*Z_sigma*r).
```

Relative to tensor gravity,

```text
alpha=beta_m^2/(4*pi*G*Z_sigma).
```

The circumcentric Hodge matching gives

```text
J_f=Z_sigma A_f/d_f.
```

For a regular tetrahedral seed,

```text
Z_sigma=(2sqrt(2)/3)J/ell.
```

Define

```text
g_*=GJ/ell
j_sigma=J ell/(hbar c_sigma)
R=r/ell
Delta_sigma=delta_sigma J.
```

Then

```text
alpha
 =3 beta_m^2/(8sqrt(2)pi g_*),
```

and

```text
x=m_sigma r=delta_sigma j_sigma R.
```

Opposite-charge repulsion dominates tensor attraction exactly when

```text
beta_m^2
 > (8sqrt(2)pi/3)
   g_*
   exp(x)/(1+x).
```

The order-one range requirement is

```text
x<=1.
```

`alpha` is therefore not an independent knob.

---

## 17. What is genuinely open

The present highest-value unresolved calculations are now narrow:

```text
1. Direct safe-cutoff Lorentzian logical amplitude:
     P L_raw,epsilon P.

2. If nonzero:
     final Hermitian H_L completion,
     unbiased logical/environment projection,
     S4 two-cell Delta_aniso^L,
     refinement/RG.

3. If the direct Lorentzian term vanishes:
     actual Peter-Weyl Lambda_E from normalized second-hit Euclidean leakage.

4. Realistic microscopic matter:
     beta_m from a gauge/chiral/PL matter Hamiltonian.

5. Absolute scale:
     GJ/ell and temporal normalization without imported calibration.

6. Full Peter-Weyl x route x mirror-matter HDA.

7. Realistic matter/chirality/global-anomaly completion.

8. Blind observational predictions and independent external replication.
```

The old broad question

```text
what is m_sigma?
```

has therefore been replaced by a sharper dynamical hierarchy:

```text
Lorentzian direct logical term?
 -> Hermitian/S4 two-cell anisotropy?
 -> constrained/RG flow?
 -> physical mode gap/range?
 -> combine with beta_m and absolute scale.
```

---

## 18. Scientific status

The fixed-cutoff core architecture has a finite composition certificate inside the declared model.

The mirror-force construction remains **conditional** because the decisive physical inputs are not all derived:

```text
physical Lorentzian/effective range operator,
beta_m,
absolute scale/time normalization,
full matter+route HDA,
experimental prediction and replication.
```

Accordingly the repository must continue to describe the framework as a **candidate theory**, not as demonstrated antigravity or a confirmed theory of nature.
