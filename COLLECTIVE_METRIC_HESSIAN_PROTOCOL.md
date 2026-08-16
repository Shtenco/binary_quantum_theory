# Frozen BCQG collective metric Hessian protocol

## Purpose

The next GR-universality measurement is the kinetic Hessian on the independently derived six-dimensional intrinsic metric carrier. This protocol is frozen before direct `W_g^dagger G W_g` data are inspected.

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

Tetrahedral symmetry alone permits independent trace and traceless response scales. Therefore **`B=I` is not allowed as a science assumption**. If direct `B` is absent or singular, `c_eff` is `INCOMPLETE`.

## 2. Normalized-state Hessian

Use the background-orthogonal microscopic carrier and real tangent coordinates,

\[
|\psi(q)\rangle=\frac{|0\rangle+W_gq}{\sqrt{1+q^Tq}}.
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

## 4. Tetrahedral finite-block diagnostics

At finite refinement the five-dimensional traceless representation may split under tetrahedral symmetry into a two-dimensional diagonal-traceless sector `E` and three-dimensional off-diagonal sector `T2`. Report separately:

- mean eigenvalue in `E`;
- mean eigenvalue in `T2`;
- relative `E/T2` split;
- mixing between `E` and `T2`;
- total trace/traceless mixing;
- full five traceless eigenvalues.

Continuum isotropy requires these finite-lattice splittings/mixings to vanish under refinement; they must not be averaged away before publication.

## 5. Required direct input

A science row must provide on the same refinement level:

- Hermitian `C_6x6 = W_g^dagger C W_g` from the production `E+S+R_op` scalar constraint or its properly enlarged depth-two effective carrier;
- `C00`;
- direct metric-response matrix `B_6x6`;
- leakage of the action outside the effective Krylov carrier;
- conditioning of `B` and `W`.

The extractor returns `INCOMPLETE` rather than a DeWitt number if the metric calibration is missing.

## 6. Self-test

`scripts/collective_metric_hessian_extractor.py --selftest` constructs a synthetic `c=1/2` Hessian, deliberately distorts trace and traceless microscopic calibrations with a nontrivial `B`, maps the Hessian back to microscopic coordinates, then requires exact recovery of `c=1/2`, zero trace/TL mixing and equal `E/T2` eigenvalues.

The self-test is an implementation certificate only; it is not BCQG science evidence.
