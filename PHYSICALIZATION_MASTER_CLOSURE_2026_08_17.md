# Physicalization master closure — 2026-08-17

Status: **canonical research-frontier ledger for the current PR.**

This file records the strongest self-consistent chain presently supported by the repository and separates three things that must never be conflated:

1. exact/finite structural closure;
2. algebraically closed observable mapping;
3. microscopic numerical coefficients that are still being produced.

---

## A. Structural chain now closed in declared scope

\[
\boxed{q+2=2^q\Rightarrow q=2}
\]

\[
q=2\to S^2\text{ local link}\to M^3\cong S^3\text{ canonical PL completion}
\]

\[
N_g=\frac{4\,8^g+10}{7}\Rightarrow\boxed{d_g\nearrow3}
\]

with

\[
\boxed{d_*^{causal-volume}=3}.
\]

Frozen dynamics gives

\[
d_H=2.999229782139151,
\qquad z\simeq0.998281156,
\]

\[
\frac{d_H}{z}=3.004393867,
\qquad 1+\frac{d_H}{z}=4.004393867.
\]

Thus topology, causal-volume scaling and relativistic dynamical scaling point coherently to a `3+1` infrared interpretation.

---

## B. Quantum geometry -> metric chain

The q=2 quantum carrier supports `SU(2)` Peter–Weyl geometry. Four spin-1/2 carriers contain a unique collective `j=2` irrep.

In the logical singlet sector

```text
X,Z = intrinsic shape
Y   = orientation pseudoscalar.
```

The exact Jacobian

\[
M:(X,Z)\longrightarrow \delta g_{TF}
\]

has rank two and orthogonal equal-norm trace-free tangent vectors.

The first refined six-edge metric kernel has

\[
6=A_1\oplus E\oplus T_2
\]

and measured local tangent splitting

\[
\boxed{\Delta_{ET}/\kappa_5=0.08430036026012608.}
\]

This is a real microscopic tetrahedral spin-2 anisotropy precursor. It is not by itself a physical quartic gravitational coefficient.

---

## C. No-numerology closures

Logical

\[
R_{aniso}\simeq0.08975326618
\]

is not `zeta4`: `Y` and `(X,Z)` occupy different `S4` operator irreps.

Likewise a scalar 8.43% `Q_tet` coefficient cannot split an irreducible three-generation `T2` matter triplet:

\[
M_{S4}=mI_3.
\]

Particle masses therefore require an independently derived flavor-breaking/Yukawa operator.

---

## D. Gravity structural closure

The Lorentzian kinetic combination satisfies the correct DeWitt structure.

HDA/ADM selection gives

\[
\boxed{c=1/2,\qquad AB=1}
\]

within the declared local ADM family.

The overall gravitational normalization and cosmological term remain familiar freedoms; HDA is not misused to invent their values.

Independent Plebanski/Urbantke and Regge/Fierz–Pauli/EH routes provide continuum consistency controls.

Held-out Regge TT residue:

```text
Z6_pred = 0.11876923193907167
Z6_obs  = 0.11876075461190198
relative error ~ 0.00714%
```

---

## E. Reduced TT control

The exact reduced propagator is

\[
G^{TT}_{AB}=\frac{\delta_{AB}}
{Z_T[4\sin^2(\omega/2)-(1/3)\sum_i4\sin^2(k_i/2)+i0]}.
\]

It has

\[
m_g=0,
\qquad P_{TT}(k)\propto k^{-1},
\]

and bare quartic coefficients

\[
\eta_{2,bare}=-1/45,
\qquad \zeta_{4,bare}=-1/12.
\]

These remain positive controls, not the full microscopic IR answer.

---

## F. Correct onsite kernel

At one tetrahedral block and `k=0`, full `S4` invariance gives

\[
\boxed{C_6^{(0)}(\omega)=a_0I+b_0A+c_0O.}
\]

On the five traceless metric modes,

\[
C_5^{(0)}=\kappa_5P_5+\Delta_{ET}Q_{tet}.
\]

The current full-`H_E` depth-two production calculation reconstructs this onsite return by exact sharding:

\[
H_Bu_e=\sum_{w=0}^{23}H_wu_e.
\]

The sharding changes computation only, not the operator.

---

## G. Correct generic momentum theorem

For nonzero directed momentum the full symmetry law is

\[
\boxed{C(g\mathbf k)=U_gC(\mathbf k)U_g^{-1}.}
\]

Therefore the three-orbit `aI+bA+cO` form is not the complete generic fixed-direction ansatz.

Before physical TT reduction there are 13 traceless quartic `S4` invariants.

After

\[
\operatorname{tr}h=0,
\qquad h_{ij}k_j=0,
\]

the exact polynomial quotient gives

\[
\boxed{\dim\mathcal W^{(4)}_{TT,S4}=6.}
\]

A complete canonical basis `W1...W6` is frozen in `S4_TT_QUARTIC_COMPLETE_BASIS.md`.

The full physical dimensionless prediction is therefore generically

\[
\boxed{\mathbf c^{IR}=(c_1,\ldots,c_6)^{IR}.}
\]

---

## H. Full-rank blind extractor

The three high-symmetry directions `(100),(110),(111)` span only rank five of the complete TT quartic sector.

Adding one preregistered generic direction `(120)` yields rank six.

For the frozen six polarization-resolved observables

\[
y=(K_{++}^{100},K_{\times\times}^{100},K_{++}^{110},K_{\times\times}^{110},K_{++}^{111},K_{++}^{120})^T
\]

and `c=(c1,...,c6)^T`,

\[
y=Ac,
\]

with exact

\[
\boxed{\det A=1/699840000\ne0.}
\]

The exact rational inverse is committed before microscopic momentum data are opened.

---

## I. Interblock momentum closure

A face-sharing tetrahedral pair has shared-face stabilizer `S3`.

Each edge carrier restricts as

\[
6=(A_1\oplus E)_{apex}\oplus(A_1\oplus E)_{face}.
\]

The reciprocal even nearest-neighbor transfer is two symmetric `2x2` multiplicity matrices and hence exactly six real scalar amplitudes.

`S4` transports one canonical face pair to the four local neighbor directions.

Regular tetrahedral displacement vectors satisfy

\[
\sum_an_a^in_a^j=\frac43\delta^{ij}
\]

and

\[
\boxed{\sum_a(k\cdot n_a)^4=\frac45(k^2)^2-\frac89Q_4^{cub}(k).}
\]

Thus an isotropic leading `k^2` cone and a tetrahedral quartic memory arise naturally at different derivative orders.

---

## J. Nested eta/zeta and birefringence hypotheses

The two-number scalar model

\[
\bar e_4=\eta_2+\zeta_4Q_4^{cub}
\]

is now a nested subspace of the full six-Wilson result.

If it passes,

\[
\zeta_4=2(e_{100}-e_{110}),
\]

\[
\eta_2=(e_{100}+4e_{110})/5
\]

and

\[
e_{100}-4e_{110}+3e_{111}=0.
\]

The single-`Q_tet` polarization submodel is another nested test. If it passes,

\[
\zeta_4=\gamma_4/4
\]

and

\[
\boxed{\Delta e_{100}:\Delta e_{110}:\Delta e_{111}=4:3:0.}
\]

Neither restriction may be imposed after opening external data.

---

## K. Real-physics map is closed algebraically

For each physical TT pole

\[
\omega_\sigma^2=c^2k^2[1+a_*^2k^2e_{4,\sigma}(\hat n)+\cdots].
\]

Then

\[
\frac{v_{g,\sigma}-c}{c}=\frac32a_*^2k^2e_{4,\sigma},
\]

\[
\delta\phi_\sigma=-\frac12La_*^2(\omega/c)^3e_{4,\sigma}.
\]

In standard modified-dispersion notation

\[
E^2=(pc)^2+A_4(pc)^4+\cdots
\]

with

\[
\boxed{A_{4,\sigma}(\hat n)=\frac{a_*^2}{(\hbar c)^2}e_{4,\sigma}(\hat n)=\frac{8\pi\lambda_R^{eff}}{E_P^2}e_{4,\sigma}(\hat n).}
\]

Thus the theory lands directly in an already-existing gravitational-wave propagation test class.

---

## L. Single absolute scale

The microscopic phase/composition equations leave one overall slope

\[
f(n)=sn.
\]

The scale map is

\[
\lambda_R^{eff}=a_*^2/(8\pi\ell_P^2).
\]

Either this one common normalization is derived from an additional microscopic principle or exactly one declared physical datum sets it.

The dimensionless six-vector must be frozen first.

---

## M. What remains numerical rather than conceptual

The architecture between microscopic dynamics and experiment is now closed.

The remaining physical calculation is finite:

```text
1. finish exact full-H_E onsite depth-two shards
2. compute six canonical shared-face full-H_E transfer amplitudes
3. compute a next-separation locality control
4. assemble second/fourth spatial moment tensors
5. verify Einstein leading cone and no anisotropy at derivative order <=2
6. TT-project and extract c1...c6 with the frozen inverse
7. perform declared refinement/regulator extrapolation
8. freeze the six-vector and uncertainty
9. derive or set the one common absolute scale
10. blind external GW comparison
```

No undefined “RG magic” remains between these steps.

---

## N. Scientific completion criterion

The first honest gravitational prediction is achieved only when

\[
\boxed{\mathbf c^{IR}\ \text{is frozen without external data}}
\]

and then survives a preregistered external comparison after no more than the one allowed common scale setting.

Until then the project is a highly constrained candidate architecture, not an experimentally established theory of nature.
