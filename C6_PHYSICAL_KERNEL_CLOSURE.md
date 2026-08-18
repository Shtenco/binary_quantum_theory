# Physical C6 closure: onsite two-channel kernel -> full six-Wilson TT momentum sector

Status: **corrected canonical physicalization map.**  The local/on-site `S4` kernel reduces exactly to `A1+E+T2`, but a generic directed nonzero momentum obeys covariance rather than fixed-direction invariance.  The complete parity-even quartic TT sector therefore contains six physical Wilson structures, proven in `S4_TT_QUARTIC_COMPLETE_BASIS.md`.

This file supersedes the earlier over-restrictive statement that the entire momentum-dependent spin-2 frontier was only two scalar functions.

---

## 1. Exact onsite reduction remains valid

For the six unordered edges of one tetrahedral coarse block, an `S4`-invariant **onsite** kernel has

\[
\boxed{
C_6^{(0)}(\omega)=a_0I+b_0A_{adj}+c_0O_{opp}.
}
\]

Its irreducible eigenvalues are

\[
\lambda_{A_1}=a_0+4b_0+c_0,
\]

\[
\lambda_E=a_0-2b_0+c_0,
\]

\[
\lambda_{T_2}=a_0-c_0.
\]

On the five-dimensional traceless carrier define

\[
P_5=P_E+P_{T_2},
\qquad
Q_{tet}=\frac35P_E-\frac25P_{T_2},
\]

\[
\kappa_5^{(0)}=\frac{2\lambda_E+3\lambda_{T_2}}5,
\qquad
\Delta_{ET}^{(0)}=\lambda_E-\lambda_{T_2}=2(c_0-b_0).
\]

Then identically

\[
\boxed{
C_5^{(0)}(\omega)
=\kappa_5^{(0)}(\omega)P_5
+\Delta_{ET}^{(0)}(\omega)Q_{tet}.
}
\]

This is the correct place for the two-function reduction.

The first refined q4 tangent precursor measured

\[
\frac{\Delta_{ET}^{(0)}}{\kappa_5^{(0)}}
=0.08430036026012608
\]

in its stated Euclidean tangent-Gram scope.  It proves a nonzero microscopic tetrahedral spin-2 splitting at that level; it is not yet a derivative coefficient.

---

## 2. Why generic momentum is different

Spatial propagation requires coupling different coarse blocks.  Write

\[
C_{6,PQ}(\omega)
\]

for the block-space kernel and assemble its normal-mode/low-momentum symbol.

At nonzero vector momentum the symmetry law is

\[
\boxed{
C_6(\omega,g\mathbf k)
=U_gC_6(\omega,\mathbf k)U_g^{-1},
\qquad g\in S_4.
}
\]

A generic direction `k` is not fixed by the full group, so one may **not** impose

\[
C_6(\omega,\mathbf k)=a(\omega,\mathbf k)I+b(\omega,\mathbf k)A+c(\omega,\mathbf k)O
\]

as the complete general tensor form at fixed generic `k`.

That three-orbit formula remains exact for:

- `k=0` onsite response;
- angularly averaged kernels;
- momentum points whose stabilizer makes the reduction valid;
- deliberately restricted ansaetze declared before opening data.

---

## 3. Complete quartic physical space

The traceless metric transforms as

\[
H_5=E\oplus T_2.
\]

At degree `h^2 k^4`, before TT constraints, representation theory gives

\[
\mathrm{Sym}^2(H_5)
=2A_1\oplus2E\oplus T_1\oplus2T_2,
\]

and

\[
\mathrm{Sym}^4(T_2)
=2A_1\oplus2E\oplus T_1\oplus2T_2.
\]

Thus the unrestricted traceless quartic sector contains 13 `S4` singlets.

After imposing exactly

\[
\operatorname{tr}h=0,
\qquad
h_{ij}k_j=0,
\]

`S4_TT_QUARTIC_COMPLETE_BASIS.md` and its executable gate prove

\[
\boxed{
\dim\mathcal W^{(4)}_{TT,S_4}=6.
}
\]

Therefore the general leading parity-even quartic correction is

\[
\boxed{
\delta K_{TT}^{(4)}
=Z_Tc_T^2a_*^2\sum_{r=1}^{6}c_rW_r,
}
\]

with the canonical six Reynolds basis functions `W1...W6` frozen there.

The real dimensionless gravitational prediction is therefore generically

\[
\boxed{
\mathbf c^{IR}=(c_1,c_2,c_3,c_4,c_5,c_6)^{IR}.
}
\]

This is stronger than a two-number prediction.

---

## 4. Einstein/HDA infrared conditions

The project already has an anomaly-controlled leading GR/HDA sector.  The corresponding physical fixed-point requirements are:

1. no TT mass term;
2. common positive kinetic residue for the two physical polarizations;
3. common leading `k^2` light cone;
4. no regulator-dependent anisotropy surviving at derivative order `<=2` after the declared continuum/blocking limit.

Schematically,

\[
K_{TT}
=Z_T[-\omega^2+c_T^2k^2]I_{TT}
+Z_Tc_T^2a_*^2\sum_{r=1}^{6}c_rW_r
+O(\partial^6).
\]

A finite anisotropy at quartic order is an irrelevant correction because its ratio to the Einstein `k^2` term scales as

\[
a_*^2k^2\to0.
\]

So rotational restoration of the leading light cone does **not** require every anisotropic quartic Wilson coefficient to vanish.

---

## 5. eta2/zeta4 is now a nested hypothesis, not the general definition

The old scalar two-parameter form

\[
\bar e_4(\hat n)
=\eta_2+\zeta_4Q_4^{cub}(\hat n)
\]

is a useful restricted subspace of the full six-dimensional TT quartic space.

Likewise

\[
e_{4,\pm}=\eta_2+\gamma_4q_\pm(\hat n)
\]

with one `Q_tet` splitter is another restricted subspace.

The exact relations

\[
\zeta_4=\gamma_4/4
\]

and the high-symmetry birefringence ratio

\[
\Delta e_{100}:\Delta e_{110}:\Delta e_{111}=4:3:0
\]

remain correct **if the microscopic six-vector lies in that declared one-splitter subspace**.

The scientific protocol is therefore:

```text
first extract all six c_r
 -> test isotropic + Q4 nested subspace
 -> test single-Q_tet nested subspace
 -> report eta2/zeta4 only if the corresponding restriction passes
 -> otherwise report the full six-coefficient prediction.
```

No coefficient may be discarded after opening the result merely to recover a prettier two-number law.

---

## 6. Exact full extractor: 100, 110, 111 are not enough

The three traditional high-symmetry directions span only rank five of the complete six-dimensional TT quartic space.

A single preregistered generic direction `(120)` closes the missing direction.

The six observables

\[
(K_{++}^{(4)}(100),
K_{\times\times}^{(4)}(100),
K_{++}^{(4)}(110),
K_{\times\times}^{(4)}(110),
K_{++}^{(4)}(111),
K_{++}^{(4)}(120))
\]

are related to `c1...c6` by an exact rational matrix with

\[
\boxed{
\det A=1/699840000\ne0.
}
\]

`S4_TT_QUARTIC_COMPLETE_BASIS.md` contains the full matrix and its exact inverse.

Thus there is still **no generic tensor fit ambiguity**: the complete general sector has a finite, preregisterable six-number extractor.

---

## 7. Where momentum comes from

The onsite depth-two calculation currently being sharded computes the local return data.

The next physical object is nearest-block transfer.  On the recursively refined PL geometry,

\[
C_6(\omega,\mathbf k)
\]

is obtained from block-space couplings by a normal-mode/local-symbol expansion.  In a locally reconstructed tangent frame this can be written schematically as

\[
C_6(\omega,\mathbf k)
=C_6^{(0)}
+\sum_{\delta}
\left[
T_\delta e^{i\mathbf k\cdot r_\delta}
+T_\delta^\dagger e^{-i\mathbf k\cdot r_\delta}
\right].
\]

For the reciprocal parity-even sector, the even derivative moments determine the quadratic and quartic spatial tensors.

The correct finite hierarchy is:

1. onsite full-E depth-two return;
2. nearest-block full-E depth-two transfer;
3. next-separation locality control;
4. local low-momentum moment tensor / normal-mode symbol;
5. remove/FAIL any anisotropic derivative-order `<=2` residue;
6. TT projection;
7. extract the six quartic Wilson coefficients using the frozen `100/110/111/120` protocol;
8. test the simpler `eta/zeta` and single-`Q_tet` nested hypotheses;
9. one absolute scale calibration if the action slope is not derived internally;
10. blind external comparison.

This is a concrete finite programme, not an unspecified “future RG theory”.

---

## 8. Real-physics dictionary

For each physical TT pole branch write

\[
\omega_\sigma^2
=c^2k^2\left[1+a_*^2k^2e_{4,\sigma}(\hat n)+O(a_*^4k^4)\right],
\qquad \sigma=1,2.
\]

Then

\[
\boxed{
\frac{v_{g,\sigma}-c}{c}
=\frac32a_*^2k^2e_{4,\sigma}(\hat n)+\cdots,
}
\]

and at fixed frequency

\[
\boxed{
\delta\phi_\sigma
=-\frac12La_*^2\left(\frac\omega c\right)^3e_{4,\sigma}(\hat n)+\cdots.
}
\]

Using

\[
a_*^2=8\pi\lambda_R^{eff}\ell_P^2,
\]

all frequency, baseline, sky-direction and polarization dependence becomes a prediction once the six dimensionless Wilson coefficients and the single absolute scale are frozen.

The external experiment therefore sees not an internal Peter-Weyl matrix but the complete response field

\[
\boxed{
\{e_{4,1}(\hat n),e_{4,2}(\hat n)\}
\quad\Longrightarrow\quad
\{v_g(\hat n,E),\delta\phi(\hat n,E),\text{polarization splitting}\}.
}
\]

---

## 9. Current honest frontier

Closed algebraically:

```text
q=2 -> Dspace=3 -> z~1 -> GR/HDA leading sector
local shape -> metric
six-edge onsite S4 projectors
complete generic parity-even S4 quartic TT quotient: dimension 6
exact six-observable extractor
TT pole -> velocity/phase/optical observables
```

Still genuinely dynamical:

```text
full-E onsite depth-two artifact
nearest-block Peter-Weyl transfer
refinement/locality convergence
six frozen IR Wilson coefficients
one absolute scale setting if not derived internally
blind experiment
```

The local `8.43%` remains a real microscopic anisotropy precursor.  It is **not** silently promoted to any one of the six physical IR Wilson coefficients.
