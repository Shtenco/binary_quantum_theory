# BCQG collective metric-regularity and gap-locality closure theorem

**Status:** exact finite-dimensional perturbation theorem + exact finite-range Neumann locality theorem.  This reduces H1/H2 to measurable norm/gap conditions; it does not assert that the production refinement data already satisfy those conditions.

## 1. Why this theorem is useful

The restricted IR HDA closure requires two hypotheses that should not be left as vague continuum assumptions:

1. the dynamically reconstructed coarse metric must remain nondegenerate and uniformly equivalent to the recursive PL-S3 carrier;
2. after eliminating gapped microscopic sectors, the effective low-energy scalar must remain local/quasilocal so that a derivative expansion is meaningful.

Both can be turned into direct finite-scale inequalities.

---

## 2. Metric regularity from one singular-value defect

Let

\[
M_{ref,\ell}:\mathbb R^6\to\mathrm{Sym}^2(T^*\Sigma)
\]

be the target-independent reference metric map at refinement level \(\ell\), and let \(M_\ell\) be the dynamically measured collective map on the same normalized coordinates.

Write

\[
M_\ell=M_{ref,\ell}+\Delta M_\ell,
\qquad
\delta_\ell=\|\Delta M_\ell\|_2.
\]

For every vector \(x\),

\[
\|M_\ell x\|
\ge
\|M_{ref,\ell}x\|-\|\Delta M_\ell x\|
\ge
\big(s_{min}^{ref}(\ell)-\delta_\ell\big)\|x\|,
\]

and similarly

\[
\|M_\ell x\|
\le
\big(s_{max}^{ref}(\ell)+\delta_\ell\big)\|x\|.
\]

Therefore, whenever

\[
\boxed{\delta_\ell<s_{min}^{ref}(\ell),}
\]

we have the explicit bilipschitz bounds

\[
\boxed{
s_{min}(M_\ell)\ge s_{min}^{ref}(\ell)-\delta_\ell>0,
}
\]

\[
\boxed{
s_{max}(M_\ell)\le s_{max}^{ref}(\ell)+\delta_\ell.
}
\]

Hence \(M_\ell\) remains rank six and

\[
\boxed{
\kappa(M_\ell)
\le
\frac{s_{max}^{ref}(\ell)+\delta_\ell}
{s_{min}^{ref}(\ell)-\delta_\ell}.
}
\]

This is an elementary operator-norm theorem; no fitted dimension enters it.

### First canonical BCQG block

The exact measured first-block reference map has

\[
(s_{min}^{ref})^2=\frac16,
\qquad
(s_{max}^{ref})^2=\frac13,
\]

so

\[
\boxed{s_{min}^{ref}=1/\sqrt6,\qquad s_{max}^{ref}=1/\sqrt3.}
\]

A convenient strong finite certificate is therefore

\[
\boxed{\delta_\ell\le\frac12s_{min}^{ref}(\ell),}
\]

which implies

\[
s_{min}(M_\ell)\ge\frac12s_{min}^{ref}(\ell)
\]

with a finite explicit condition-number bound.

The factor `1/2` is only a conservative reporting threshold; the mathematical nondegeneracy boundary is the exact inequality \(\delta<s_{min}^{ref}\).

---

## 3. Consequence for spatial dimension

Suppose the recursive PL carrier is a three-manifold and, on all sufficiently fine levels, the reference maps have uniform bounds

\[
0<m\le s_{min}^{ref}(\ell),
\qquad
s_{max}^{ref}(\ell)\le M<\infty,
\]

while

\[
\sup_\ell\delta_\ell\le\rho m,
\qquad 0\le\rho<1.
\]

Then the dynamical coarse metrics are uniformly bilipschitz-equivalent to the reference PL metric. Local Hausdorff dimension is therefore unchanged:

\[
\boxed{D_H=3.}
\]

If the associated metric Laplacians also converge to a smooth uniformly elliptic second-order operator, the standard local heat-kernel scaling gives the same local spectral dimension.

Thus H1 does not require independently fitting a dimension at every scale.  It requires the stronger and cleaner observable: **uniform lower/upper metric singular-value control**.

The existing spectral/FEM dimensions remain held-out cross-checks.

---

## 4. Exact finite-range resolvent locality from a convergent block split

Now consider the residual coupled `Q` operator of C2,

\[
D=QCQ.
\]

Assume the retained Krylov basis carries a graph/block distance `dist(i,j)` and split

\[
D=D_0+T,
\]

where:

1. `D0` is block diagonal in that locality decomposition and invertible;
2. `T` has finite range \(R\): \(T_{ij}=0\) whenever `dist(i,j)>R`;
3. the dimensionless hopping ratio
   \[
   r=\|D_0^{-1}T\|_2
   \]
   satisfies
   \[
   \boxed{r<1.}
   \]

Then

\[
D^{-1}
=(I+D_0^{-1}T)^{-1}D_0^{-1}
=\sum_{n=0}^\infty(-D_0^{-1}T)^nD_0^{-1}
\]

converges in operator norm.

Because each factor of `T` propagates support by at most range \(R\), a matrix element connecting blocks separated by distance \(d\) receives no contribution before

\[
n\ge\left\lceil\frac dR\right\rceil.
\]

Therefore

\[
\boxed{
\|(D^{-1})_{ij}\|
\le
\frac{\|D_0^{-1}\|}{1-r}
\,r^{\lceil d/R\rceil}
}
\]

up to the declared block norm convention.

This is an explicit exponential/quasilocality certificate derived from a geometric series; no continuum assumption is required.

---

## 5. Quasilocality of the Schur complement

Let

\[
B=PCQ
\]

have finite microscopic/block range \(R_B\). The C2 effective scalar is

\[
C_{eff}=PCP-BD^{-1}B^\dagger.
\]

Combining finite-range `B` with the exponential bound above gives exponential decay of the self-energy between well-separated retained blocks. Schematically,

\[
\boxed{
\|(C_{eff})_{xy}\|
\lesssim
K\,r^{\lceil(d(x,y)-2R_B)/R\rceil}
}
\]

for a finite prefactor `K` determined by \(\|B\|\), \(\|D_0^{-1}\|\), and \((1-r)^{-1}\).

Hence a C2 stage satisfying a **uniform** `r<1` bound does more than permit numerical inversion: it proves that integrating out the residual Q sector does not generate an unsuppressed long-range nonlocal scalar.

On a smooth homogeneous/refinement family, the long-wavelength symbol is then analytic around `k=0` inside the corresponding locality radius and admits a derivative expansion.

Parity/tetrahedral symmetry removes forbidden odd tensor structures.  Once C3 supplies first-class HDA, the restricted IR uniqueness theorem fixes the leading two-derivative metric scalar to the ADM/Einstein class; the remaining higher-derivative terms are explicit irrelevant corrections rather than an independent H2 assumption.

---

## 6. Relation to a spectral gap

A nonzero `QCQ` spectral gap is necessary for the C2 inverse after low modes are promoted, but the elementary Neumann certificate above is deliberately stronger: it also gives a constructive locality bound.

If production `QCQ` is gapped but no convenient split satisfies `r<1`, C2 is not falsified.  One may then use a more general resolvent-locality estimate, but that theorem and its assumptions must be frozen before the production claim.

For the shortest internal-closure route, prefer the directly auditable sufficient condition

\[
\boxed{\|D_0^{-1}T\|<1.}
\]

when available.

---

## 7. Reduced H1/H2 certificate

At each C2 refinement level report:

### metric regularity

```text
smin_ref
smax_ref
delta_metric = ||M_dynamic-M_ref||_2
lower_bound = smin_ref-delta_metric
upper_bound = smax_ref+delta_metric
condition_bound = upper_bound/lower_bound
```

Require a level-independent positive lower bound in the refinement window.

### resolvent locality

For the frozen target-independent local split `D=D0+T`, report

```text
||D0^-1||
||T||
r = ||D0^-1 T||
range_R
range_RB
locality_length_bound = R/|log r|
```

when `r<1`.

A common refinement window with positive metric lower bound, classified/promoted Q zero modes, residual Q gap, and bounded `r<1` supplies the metric-regularity/locality content of H1/H2.

---

## 8. What remains after this theorem

This theorem does not manufacture production data.  It changes the remaining logical burden:

```text
C1 corrected S
   -> C2 actual Krylov C and QCQ
      -> metric singular-value defect + Q gap/locality certificate
         -> C3 HDA intertwining defects
            -> restricted IR HDA uniqueness
               -> ADM/Einstein(G,Lambda), two tensor modes
```

Thus spatial dimension, DeWitt coefficient, tensor speed, graviton count, and leading locality are no longer separate adjustable targets once the measured C2/C3 inequalities hold.
