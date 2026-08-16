# Frozen BCQG collective metric Hessian protocol

## Purpose

The next GR-universality measurement is the kinetic Hessian on the independently derived six-dimensional intrinsic carrier. This protocol is frozen before direct `W_g^dagger G W_g` data are inspected.

## 1. Three coordinate systems must not be conflated

The six-dimensional spaces are isomorphic, but their normalizations are not automatically identical:

1. `q` — orthonormal microscopic Peter-Weyl coordinates in the frozen six-column isometry `W_g`, so `W_g^dagger W_g=I_6`;
2. `y` — fractional coarse squared-edge observables `y_e=delta(ell_e^2)/ell_*^2`;
3. `h` — orthonormal symmetric metric coordinates `(xx,yy,zz,sqrt(2)xy,sqrt(2)xz,sqrt(2)yz)`.

The regular-tetrahedron geometry fixes exactly

\[
y=Jh,\qquad \det J=-\frac{\sqrt2}{2}.
\]

But the microscopic-to-geometric calibration must be measured from BCQG:

\[
\boxed{y=Bq},\qquad B_{eA}=\left.\frac{\partial\langle \hat y_e\rangle}{\partial q_A}\right|_{q=0}.
\]

At finite tetrahedral symmetry the six-edge representation decomposes exactly as

\[
\boxed{6=A_1\oplus E\oplus T_2=1\oplus2\oplus3}.
\]

Therefore an exactly tetrahedrally equivariant response may carry **three** independent channel normalizations `b_A1,b_E,b_T2`. Full rotational isotropy is stronger and requires the `E` and `T2` traceless channels to merge under refinement. Consequently **`B=I` is not allowed as a science assumption**. If direct `B` is absent or singular, `c_eff` is `INCOMPLETE`.

A further selection-rule guard is now frozen: on the original sharp all-`j=1/2` seed, `W_g` lies entirely in changed-spin `P4` sectors while flux/metric observables preserve spin irreps. Hence the linear expectation-value response `B` is exactly zero there. The direct science producer must therefore use a target-independent coherent/refinement background with overlapping spin support, not silently identify the sharp-spin Hilbert coordinates with classical metric coordinates.

## 2. Normalized-state Hessian

On a background for which the chosen tangent carrier is orthogonalized, use real tangent coordinates

\[
|\psi(q)\rangle=\frac{|0\rangle+Wq}{\sqrt{1+q^Tq}}.
\]

For a Hermitian collective scalar constraint `C`, define

\[
C_{00}=\langle0|C|0\rangle,\qquad C_{AB}=\langle w_A|C|w_B\rangle.
\]

The exact second derivative at the background is

\[
\boxed{K_q=2\,\mathrm{Re}\,C_{AB}-2C_{00}I_6}.
\]

The subtraction term is mandatory; omitting it confuses state normalization with kinetic curvature.

Since `y=Bq=Jh`,

\[
q=B^{-1}Jh,
\]

hence the physical metric-coordinate Hessian is

\[
\boxed{K_h=(B^{-1}J)^T K_q(B^{-1}J)}.
\]

## 3. Trace/traceless extraction

Use

\[
t=\frac1{\sqrt3}(1,1,1,0,0,0)
\]

and a fixed orthonormal traceless basis

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
\qquad K_{TL}=T^TK_hT,
\qquad \bar\lambda_{TL}=\frac15\mathrm{tr}K_{TL}.
\]

Only after direct `B` is supplied define

\[
\boxed{c_{eff}=\frac{1-\lambda_{tr}/\bar\lambda_{TL}}{3}}.
\]

GR/ADM target `c=1/2` is used only by the external killer threshold, never inside the extractor.

## 4. Exact S4 reduction and finite-block diagnostics

The six coarse edges form the edge representation of `S4`. Any exactly tetrahedrally invariant Hermitian scalar has the association-scheme form

\[
C=aI+bA_{adj}+cO_{opp},
\]

where `A_adj` joins coarse edges sharing a vertex and `O_opp` joins opposite edges. Its three channel eigenvalues are

\[
\boxed{\lambda_{A_1}=a+4b+c},
\]

\[
\boxed{\lambda_E=a-2b+c},
\]

\[
\boxed{\lambda_{T_2}=a-c}.
\]

Thus an exact homogeneous six-edge scalar needs only three representative matrix elements `(diagonal, adjacent, opposite)` plus a covariance/leakage check, rather than 36 independent elements. The same three-channel reduction applies to an equivariant metric-response matrix `B`.

At finite refinement report separately:

- `A1`/trace channel;
- the two-dimensional `E` traceless channel;
- the three-dimensional `T2` traceless channel;
- relative `E/T2` split;
- mixing between irreps;
- total trace/traceless mixing;
- full five traceless eigenvalues.

Continuum `SO(3)` isotropy requires `E` and `T2` kinetic and metric-calibration channels to merge under refinement; the finite splitting must not be averaged away before publication.

## 5. Required direct input

A science row must provide on the same refinement level:

- Hermitian `C_6x6 = W^dagger C W` from the production `E+S+R_op` scalar constraint or its properly enlarged depth-two effective carrier;
- `C00`;
- direct metric-response matrix `B_6x6` from a BCQG geometric observable on the same coherent/refinement background;
- leakage of the action outside the effective Krylov carrier;
- conditioning of `B` and `W`;
- S4 covariance defect and the three representative `(a,b,c)` channel elements when the symmetry reduction is used.

The extractor returns `INCOMPLETE` rather than a DeWitt number if the metric calibration is missing.

## 6. Reproducibility

- `scripts/collective_metric_hessian_extractor.py`
- `scripts/collective_s4_metric_channel_reduction_gate.py`
- `verification_results/COLLECTIVE_S4_METRIC_CHANNEL_REDUCTION.json`
- `COLLECTIVE_SHARP_SPIN_METRIC_RESPONSE_OBSTRUCTION.md`

The extractor self-test deliberately uses a nontrivial calibration matrix and must recover a synthetic `c=1/2` Hessian. This is an implementation certificate only, not BCQG science evidence.
