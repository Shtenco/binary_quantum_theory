# Frozen BCQG collective metric Hessian protocol — depth-two version

## Purpose

The six-dimensional intrinsic carrier and its first finite BCQG-native metric calibration are now measured. The remaining GR-universality question is no longer whether six metric coordinates exist; it is whether **depth-two gravitational dynamics on those measured coordinates** approaches the Einstein/DeWitt kinetic form.

This protocol is frozen before the depth-two `A1/E/T2` gravitational return eigenvalues are inspected.

## 1. Coordinate chain is now measured

Use three distinct coordinate layers:

1. `q` — orthonormal six-edge Hilbert tangent coordinates in `W_g`, with `W_g^dagger W_g=I_6`;
2. `Z` — six coarse face-flux Gram observables `Z_fg=X_f.X_g`, `f<g`;
3. `h` — orthonormal symmetric metric coordinates
   `(xx,yy,zz,sqrt(2)xy,sqrt(2)xz,sqrt(2)yz)`.

At the regular coarse background the exact flux-to-metric Jacobian is

\[
\delta Z=J_F^{bg}h,
\qquad
J_F^{bg}=\frac92J_F,
\]

with

\[
\det J_F=\frac{128\sqrt2}{729}\ne0.
\]

The direct exact coarse-block calculation gives

\[
(B_F)_{(fg),e}=2\,Re\langle0|Z_{fg}|\tau_e\rangle,
\qquad |\tau_e\rangle=-i|w_e\rangle,
\]

and

\[
\boxed{rank(B_F)=6},
\qquad
\boxed{cond(B_F)=1.0000000000000002}.
\]

The measured BCQG-native map is therefore

\[
\boxed{
h=M_{hq}q,
\qquad
M_{hq}=(J_F^{bg})^{-1}B_F.
}
\]

For the first finite block,

\[
rank(M_{hq})=6,
\qquad
cond(M_{hq})=\sqrt2
\]

to numerical precision.

This `M_hq` route is the **primary science calibration**. The older edge-squared route `y=Bq=J_edge h` is retained only as an independent coordinate cross-check. Setting `B=I` is forbidden.

## 2. Finite tetrahedral irreps

The six-edge representation decomposes exactly as

\[
\boxed{6=A_1\oplus E\oplus T_2=1\oplus2\oplus3}.
\]

At finite refinement, trace `A1`, two-dimensional traceless `E`, and three-dimensional traceless `T2` must be reported separately. Continuum rotational isotropy is stronger than tetrahedral symmetry and requires the `E` and `T2` channels to merge under refinement.

Any homogeneous real-symmetric `S4` operator on the six edges is determined by only three matrix elements:

\[
C=aI+bA_{adj}+cO_{opp},
\]

with channel eigenvalues

\[
\boxed{\lambda_{A_1}=a+4b+c},
\qquad
\boxed{\lambda_E=a-2b+c},
\qquad
\boxed{\lambda_{T_2}=a-c}.
\]

Thus every expensive homogeneous depth-two science operator should first be measured through `(diagonal, adjacent, opposite)` representatives plus covariance/leakage guards, not 36 brute-force entries.

## 3. Direct gravitational block is structurally zero

Under the frozen real Peter-Weyl recoupling convention,

\[
H_E^{sine}=iA_E,
\qquad A_E^T=-A_E,
\]

and the Hermitian-completed Lorentzian operator

\[
S=-\frac{i}{2}(L_{raw}-L_{raw}^\dagger)
\]

also has the form

\[
S=iA_S,
\qquad A_S^T=-A_S.
\]

The ordinary six-edge `S4` representation and its sign twist have no nonzero invariant real-antisymmetric matrix. Therefore

\[
\boxed{W_g^\dagger H_E^{sine}W_g=0},
\qquad
\boxed{W_g^\dagger S W_g=0}.
\]

At `beta=hbar=1`, for

\[
G=-\frac23H_E^{sine}-\frac{32}{9}S,
\]

we have

\[
\boxed{W_g^\dagger G W_g=0}.
\]

This forbids the central false shortcut: **a gravitational DeWitt tensor may not be inferred by fitting the direct homogeneous `6x6` projection**, because that projection is exactly zero. The nontrivial gravitational metric dynamics must arise through excursions outside `W_g` and return.

The operator-first route `R_op` is not constrained by this zero theorem: a homogeneous spin-preserving real-symmetric route block may carry `A1/E/T2`. Any direct route contribution must be reported separately and must not be renamed the gravitational DeWitt kinetic tensor.

## 4. First denominator-free depth-two observable

Before choosing any effective-Hamiltonian energy denominator, compute the target-independent positive return/leakage Gram

\[
\boxed{
L_G=(Q_\perp G W_g)^\dagger(Q_\perp G W_g),
\qquad
Q_\perp=1-W_gW_g^\dagger-|0\rangle\langle0|
}
\]

with the background subtraction adapted to the exact retained carrier.

`L_G` is not yet the Hamiltonian Hessian. It is the first non-circular dynamical diagnostic of which metric irreps gravity excites at depth two. Report:

- `(a_G,b_G,c_G)` = diagonal/adjacent/opposite representatives;
- `lambda_A1`, `lambda_E`, `lambda_T2`;
- `E/T2` relative split;
- action leakage/support;
- S4 covariance defect;
- contributions from `EE`, `ES+SE`, `SS` separately before summation.

For `G=-2E/3-32S/9`, the positive Gram expands as

\[
L_G=rac49L_{EE}+\frac{1024}{81}L_{SS}+\frac{64}{27}L_{ES}^{sym},
\]

where

\[
L_{ES}^{sym}=\frac12\left[(Q_\perp EW)^\dagger(Q_\perp SW)+(Q_\perp SW)^\dagger(Q_\perp EW)\right] \times 2
\]

or, equivalently, the cross term must be implemented directly from the two vectors with the exact algebraic coefficient. The code must store the unsummed channel pieces so sign/coefficient mistakes are auditable.

## 5. Physical effective scalar / Feshbach guard

A physical depth-two effective Hamiltonian may be built only after a target-independent resolvent prescription is frozen, for example

\[
C_{eff}=P C P-P C Q\,(Q C_0Q-E_0)^{-1}Q C P
\]

or another explicitly declared Schrieffer-Wolff/Feshbach construction.

The following are forbidden:

- choosing a denominator because it moves `c_eff` toward `1/2`;
- replacing the resolvent by a fitted scalar after seeing the three irrep channels;
- using `L_G` itself as if it were already the physical Hamiltonian Hessian;
- mixing a direct `R_op` matrix into the gravitational depth-two term without labeling the two pieces separately.

If no physical resolvent is yet frozen, report `L_G` as `DEPTH2_RETURN_PRECURSOR` and keep `c_eff=INCOMPLETE`.

## 6. Normalized-state Hessian once a physical `C_eff` exists

Let the retained background be orthogonal to the six tangent columns and define

\[
|\psi(q)\rangle=\frac{|0\rangle+W_gq}{\sqrt{1+q^Tq}}.
\]

For Hermitian `C_eff`, let

\[
C_{00}=\langle0|C_{eff}|0\rangle,
\qquad
C_{AB}=\langle w_A|C_{eff}|w_B\rangle.
\]

The exact normalized-state Hessian is

\[
\boxed{K_q=2\,Re(C_{AB})-2C_{00}I_6}.
\]

The subtraction term is mandatory.

Using the measured native map

\[
h=M_{hq}q,
\qquad
q=M_{hq}^{-1}h,
\]

the physical metric-coordinate Hessian is

\[
\boxed{
K_h=M_{hq}^{-T}K_qM_{hq}^{-1}.
}
\]

The extractor also retains the legacy cross-check route `q=B^{-1}J_edge h`; both routes must agree on a synthetic control before science data are accepted.

## 7. DeWitt extraction

Use

\[
t=\frac1{\sqrt3}(1,1,1,0,0,0)
\]

and the fixed orthonormal traceless basis

\[
T=\left[
\frac{(1,-1,0,0,0,0)}{\sqrt2},
\frac{(1,1,-2,0,0,0)}{\sqrt6},
e_{xy},e_{xz},e_{yz}
\right].
\]

Measure

\[
\lambda_{tr}=t^TK_ht,
\qquad
K_{TL}=T^TK_hT,
\qquad
\bar\lambda_{TL}=\frac15\operatorname{tr}K_{TL}.
\]

Only then define

\[
\boxed{
c_{eff}=\frac{1-\lambda_{tr}/\bar\lambda_{TL}}{3}.
}
\]

The GR target `c=1/2` appears only in the external universality killer threshold, never inside the producer or coordinate calibration.

Report separately:

- `lambda_trace`;
- all five traceless eigenvalues;
- `lambda_E` and `lambda_T2`;
- `E/T2` relative split;
- trace/traceless mixing;
- `E/T2` mixing;
- calibration conditioning;
- effective-operator leakage/resolvent conditioning.

## 8. Photon cross-observable

The same measured `M_hq` feeds photon phase:

\[
\boxed{
\Delta\Phi=\kappa D J_{edge}M_{hq}q,
\qquad
\kappa=\frac{k\ell_*}{2}.
}
\]

At the first finite block this response has rank five and unique uniform null direction. Therefore the five optical shape channels are a direct readout basis for the same traceless sector whose **depth-two gravitational eigenvalues** must merge into the DeWitt continuum channel.

This creates a clean cross-check: the geometry coordinates used in the gravity Hessian and in photon interference are no longer independently normalized constructions.

## 9. Required direct science input

A first finite depth-two row must contain at minimum:

```text
q_to_metric_h_map
metric_map_condition_number
G_depth2_return_representatives: diag, adjacent, opposite
G_depth2_irrep_eigenvalues: A1, E, T2
EE / ES / SS unsummed pieces
leakage/support/covariance diagnostics
```

A row may contain `c_DeWitt_eff` only after additionally providing:

```text
physical effective C_6x6
C00
frozen effective-resolvent prescription
resolvent conditioning
```

Then the same row proceeds to constraint ranks and collective `[H,H]`.

## 10. Reproducibility

- `scripts/collective_l1_coarse_flux_response_gate.py`
- `verification_results/COLLECTIVE_L1_COARSE_FLUX_RESPONSE.json`
- `scripts/collective_gravitational_direct_block_gate.py`
- `verification_results/COLLECTIVE_GRAVITATIONAL_DIRECT_BLOCK.json`
- `scripts/collective_metric_hessian_extractor.py`
- `verification_results/COLLECTIVE_METRIC_HESSIAN_EXTRACTOR_SELFTEST.json`
- `scripts/collective_s4_metric_channel_reduction_gate.py`
- `COLLECTIVE_GRAVITATIONAL_DIRECT_BLOCK_THEOREM.md`
- `BCQG_PHOTON_INTERFERENCE_BRIDGE.md`

## Current bottleneck

The metric carrier and finite metric calibration are now established. The next decisive computation is

\[
\boxed{L_G=(Q_\perp G W_g)^\dagger(Q_\perp G W_g)}
\]

through its three exact `S4` representative channels, followed by a separately preregistered physical resolvent and the normalized-state DeWitt Hessian.
