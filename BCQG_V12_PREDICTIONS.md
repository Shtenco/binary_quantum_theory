# BCQG v1.2 — falsifiable prediction ledger

Status: **canonical prediction surface for the v1.2 gravity core**.  Predictions below are separated into hard structural predictions on the frozen habitat and conditional IR predictions.  Absolute dimensional predictions are deliberately excluded until scale setting and matter coupling exist.

## A. Hard structural / finite-regulator predictions

### P1. Cutoff plateau on the frozen HH habitat

For the all-`j=1/2` seed and the declared finite-depth two-node Hamiltonian,

\[
\boxed{J_{max}\ge13/2}
\]

must give the same exact spin-supported result.  Increasing `Jmax` further may increase unused basis capacity but must not change the physical finite-depth amplitude through spin truncation.

A detected dependence above `13/2` falsifies the current hit-depth/support implementation.

### P2. Full HDA regulator scaling

For the frozen smooth-lapse/WKB family,

\[
\boxed{\Delta_{full}=O(\epsilon^{\min(p_R,1)})},
\]

where the exhaustive operator-first route audit gives `p_R ~= 1`.  Thus the expected leading full residual is approximately linear in `epsilon` unless an additional cancellation makes it faster.

### P3. Parity-resolved anomaly structure

On the even all-`j=1/2` seed:

```text
even: EE, SS, SxR, route/D target
odd : ES, SE, ExR
```

Therefore

\[
\boxed{\langle C_{odd},D\rangle=0}
\]

exactly in the doubled-spin grading.  Odd and even anomalies cannot cancel one another in the norm.

Pure-geometry odd channels `ES/SE` inherit the two-node antisymmetric lapse factor and are predicted to be `O(epsilon^2)` relative to the `O(epsilon^-1)` WKB diffeomorphism target.  The odd `E x R` channel is at most `O(epsilon)` relative after the exact inverse-epsilon cancellation.

### P4. First-order logical Euclidean silence

On the all-`j=1/2` logical sector,

\[
\boxed{P H_E^{sine} P=0}.
\]

Any nonzero first-order all-`j=1/2` Euclidean logical return above numerical tolerance falsifies the declared grading/operator implementation.

### P5. Hermitian Lorentzian one-body coefficient

The environment-unbiased logical one-body block in repository structural units is predicted to remain

\[
\boxed{H_{corr,1body}=-4.760637696520545\,Y}
\]

at `beta=hbar=1`, because the Hermitian completion exactly preserves already anti-Hermitian pure-`iY` raw sectors.

### P6. Neighbor-dependent Lorentzian pseudoscalar structure

In the already measured diagonal environment cube with nodes `3,4` frozen at `K=0`, Hermitian completion preserves the raw imaginary pseudoscalar anchors

```text
Y I I    = +i 0.3359014033398999
Y Z1 I   = -i 0.00702861722247964
Y I Z2   = +i 0.002338130606598994
Y Z1 Z2  = +i 0.004676261213197787
```

before multiplication by the global real correction coefficient.  Future off-diagonal environment calculations must reduce to these diagonal matrix elements when restricted to the same blocks.

### P7. Positive, kernel-safe operator-first route symbol

For every finite physical route block,

\[
A(p)=Q^{ab}p_ap_b=\sum_iB_i^\dagger B_i\ge0.
\]

Zero modes are allowed.  At a zero mode the kernel compatibility condition predicts

\[
\boxed{P_0(\partial_{p_c}A)P_0=0},
\]

so the Sylvester anticommutator defining the principal HDA structure remains solvable.  The current exhaustive one-step audit finds 24 singular cases with defects at `~1e-13` or below.

## B. Conditional continuum / IR predictions

These are predictions **if** the frozen microscopic theory reaches a nondegenerate local metric phase with the standard first-class HDA.

### P8. Spatial dimension and relativistic scaling

The continuum window must retain

\[
\boxed{D_{space}\to3},\qquad \boxed{z\to1}.
\]

The existing finite anchors are `d_H=2.999229782` and `z=0.998281156`; future larger/independent ensembles should approach the same universality class rather than drift systematically away.

### P9. DeWitt coefficient

The effective kinetic trace coefficient must approach

\[
\boxed{c_{DW}\to1/2}.
\]

A stable different value signals a non-GR universality class unless an additional first-class constraint changes the counting.

### P10. First-class rank and graviton content

The collective constraint distribution must approach

\[
\boxed{(r_G,r_D,r_H,r_{extra})\to(3,3,1,0)}.
\]

This leaves two local gravitational configuration degrees of freedom, which in a local two-derivative metric phase are the two helicities of one massless spin-2 tensor sector.  A BF-like rank with six independent flatness constraints is a FAIL even if the algebra is anomaly-free.

### P11. Relativistic tensor cone

In the same GR-like phase the leading TT kinetic and gradient coefficients must satisfy

\[
\boxed{A_{eff}B_{eff}\to1},
\]

so the tensor dispersion is relativistic in units selected by the hypersurface normal.

## C. Explicitly not predicted yet

BCQG v1.2 does **not** currently make a controlled numerical prediction for:

- Newton's constant in SI units;
- an absolute Planck-to-laboratory conversion beyond externally supplied scale setting;
- particle masses or energy splittings in eV;
- a mirror-force strength or range;
- matter cross sections;
- cosmological parameters;
- an experimentally detectable signal amplitude.

Those require a derived matter sector, Newton normalization and collective RG matching.  Assigning such numbers now would turn structural units into unjustified physical units.

## Falsification rule

A failed hard structural prediction is retained as a failure of the current v1.2 implementation/candidate; no post-result sign flip, coefficient refit, channel deletion or threshold widening is allowed.  A failed conditional IR prediction falsifies the claimed GR universality class, even if the microscopic finite gates remain internally consistent.
