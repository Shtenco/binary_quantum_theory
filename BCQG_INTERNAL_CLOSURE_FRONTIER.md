# BCQG minimal internal-closure frontier

Date: 2026-08-17

This note is the current shortest-path map after the repo-wide audit and the restricted IR HDA universality theorem. It is deliberately narrower than the historical list of independent numerical targets.

## What is no longer a logically independent open problem

Provided the hypotheses of `BCQG_IR_HDA_UNIVERSALITY_CLOSURE.md` hold, the following are derived rather than independently adjustable:

- spatial metric phase has `D=3` once the recursive PL-S3 metric remains uniformly nondegenerate/bilipschitz;
- HDA selects `c_DeWitt=1/2`;
- HDA normalization selects `AB=1`;
- the leading TT cone has `z=1` / unit characteristic speed in hypersurface-normal units;
- DeWitt metric signature is one conformal negative plus five traceless positive directions;
- after the regular seven first-class generators and no second-class remainder, the metric sector has exactly two physical configuration modes.

The preregistered collective killer still measures these quantities independently as an overdetermined falsifier. They are not deleted from testing; they are removed only from the list of logically independent assumptions.

## The three remaining closure certificates

### C1 — corrected microscopic Lorentzian operator

Finish the tetrahedral charged-volume physical Hermitian Lorentzian column.

The original V2 `24 forward + 24 direct-adjoint` execution was cancelled before a complete science result. The attempted V3 order-eight slot-orbit shortcut was correctly blocked because the first 16-cell Euclidean source column is not a one-dimensional pseudoscalar of the full pairing stabilizer.

The shortest symmetry-independent route is now the exact direct-Hermitian identity

\[
\boxed{
S
=-\frac i2
\sum_d\eta_d\sum_{cyclic(a,b,c)}
\operatorname{Tr}_{aux}
\{[C_a(K),C_b(K)],C_c(V_{tet})\}.
}
\]

This is algebraically identical to the frozen 24-forward + 24-adjoint definition and uses no tetrahedral reconstruction hypothesis. The V4 execution computes twelve physical Hermitian pair words with the unchanged v1.3 charged volume, cutoff and acceptance semantics.

C1 requires:

```text
direct-Hermitian identity gate PASS
12 physical pair workers PASS
unchanged V2 primitive leakage/scalar/spin guards PASS
one independently serialized held-out V2 primitive-pair equivalence PASS
final node-0 S column PASS
```

Then validate node transport on at least one held-out nonzero mask before using any symmetry transport for the remaining source nodes.

C1 is an operator-correctness certificate. It is not a GR fit.

### C2 — complete low-energy blocked carrier / canonical Schur fixed point

At each retained coarse scale:

1. start with the six directly calibrated metric directions `P=W_g W_g^dagger`;
2. construct only the target-independent `Q` Krylov states actually reached by the corrected `E+S+R_op` production constraint;
3. retain the full measured direct block
   \[
   A=PCP;
   \]
4. diagonalize/compress
   \[
   D=QCQ;
   \]
5. every exact/near-zero mode coupled to `P` is promoted into the retained low-energy carrier, never regularized away;
6. iterate until the remaining coupled `Q` sector has a stable nonzero gap;
7. construct the unique zero-constraint Schur complement

\[
\boxed{
C_{eff}(0)=A-PCQ(QCQ)^{-1}QCP.
}
\]

A crucial scope distinction is now explicit:

\[
\boxed{PGP=0}
\]

for the homogeneous six-edge **geometry-only** block

\[
G=-\frac23E-\frac{32}{9}S,
\]

but the full production Hamiltonian is

\[
H=G+R_{op},
\]

and therefore

\[
\boxed{PHP=PR_{op}P}
\]

may be nonzero. Production C2 must measure this route block; it may not set the full `A` to zero by convention.

Because of S4 covariance, the final homogeneous six-metric part is reported through

\[
\kappa_{A_1},\qquad \kappa_E,\qquad \kappa_{T_2},
\]

rather than 36 independently fitted entries.

The independently measured metric map supplies the blind GR shape diagnostic

\[
\kappa_{A_1}:\kappa_E:\kappa_{T_2}=-1/2:1:2,
\]

but this ratio is **not a C2 acceptance condition**. It is reported only after production. The theorem-level value `c_DeWitt=1/2` is selected later by C3 first-class HDA.

C2 must report across refinement:

- minimum coupled-Q gap;
- retained low-energy carrier dimension and irreps;
- metric-map smallest/largest singular values;
- direct route block `PR_opP` and geometry-only zero-block regression;
- S4/rotational splitting;
- Schur-compression leakage/error;
- quasilocality of the residual inverse/effective scalar.

A stable gap after every coupled low mode is promoted is the cleanest test that there is no hidden additional gapless scalar/vector gravitational sector.

The exact metric-regularity and gap-locality theorems reduce the vague IR assumptions to directly measurable inequalities. A uniformly positive metric singular-value lower bound fixes the three-dimensional metric phase; a uniformly gapped finite-range eliminated sector gives an exponentially quasilocal Schur resolvent.

### C3 — collective HDA fixed point

On the C2 low-energy carrier, use the already frozen lapse/refinement prescription and show

\[
\Delta_{HH}^{collective}\to0
\]

with the correct **measured coarse-metric structure function**.

The exact compression/intertwining identity gives

\[
\|[H_{eff}[N],H_{eff}[M]]-i\hbar D_{eff}[\beta_{eff}]\|
\le
\delta_{micro}+2\eta_N\eta_M+\hbar\delta_{str}.
\]

Thus C3 can be diagnosed through three independently measured mechanisms:

```text
projected microscopic residual delta_micro
carrier leakage product eta_N eta_M
structure-function blocking defect delta_str
```

plus the direct collective bracket as a held-out overdetermined check.

For nondegenerate `q`, local lapse pairs such as `N=1`, `M=x^i` generate

\[
\beta^a=q^{ai},
\]

so a faithful HDA representation supplies three independent spatial-diffeomorphism directions. The flux-to-metric kernel supplies the three local Gauss/frame rotations. The one scalar Hamiltonian plus these generators gives the standard seven-generator first-class set.

The remaining guards are:

- faithful action of the three shift directions on held-out perturbations;
- nonzero scalar constraint gradient/action;
- C2 leaves no unclassified gapless sector;
- no second-class residual in the projected constraint bracket matrix.

Once C3 and these completeness guards pass, the restricted IR HDA theorem forces the ADM/Einstein leading Hamiltonian up to `G` and `Lambda`. Then `D=3`, `c_DeWitt=1/2`, `z=1` and the two physical tensor configuration modes are consequences, not fitted targets.

## Why locality is folded into C2 rather than treated as a fourth monster calculation

The microscopic operator is finite-range/local. If the eliminated coupled `Q` sector has a stable nonzero spectral gap, the exact inverse expansion

\[
(QCQ)^{-1}
=\frac{QCQ}{c}\sum_{n\ge0}
\left(I-\frac{(QCQ)^2}{c}\right)^n
\]

converges with exponential graph-distance decay. Equivalently, when a frozen local split `D=D0+T` satisfies `||D0^-1 T||<1`, the Neumann series supplies an explicit locality length.

Thus H2 is no longer a free continuum assumption: production C2 must measure the gap/locality certificate. Higher-derivative corrections remain explicit irrelevant terms.

## Internal closure criterion

The gravitational core may be labelled `INTERNALLY_CLOSED_CANDIDATE` only when all three **production** certificates are green:

```text
C1 corrected physical Lorentzian operator   PASS
C2 low-energy Schur/RG fixed point          PASS
C3 collective HDA/completeness              PASS
```

The supporting theorem engines are already separate from these production verdicts; a green self-test is not a substitute for measured BCQG data.

Then the consequences are theorem-level:

```text
D=3 metric phase
c_DeWitt=1/2
AB=1
z=1
(5+,1-) metric kinetic signature
3 Gauss/frame gauge directions
3 spatial diffeomorphism directions
1 scalar first-class direction
0 second-class remainder
2 physical tensor configuration modes
leading ADM/Einstein gravity up to G,Lambda
```

The existing numerical killer remains as an independent cross-check and should agree with every derived quantity.

## What is outside "internal gravitational closure"

Even after C1--C3 pass, the following are not mathematical inconsistencies and should not be confused with an unfinished gravitational operator:

- choosing/measuring the absolute low-energy Newton scale `G`;
- the value of `Lambda`;
- vacuum/state selection and the true geometry two-point function;
- full Standard Model/chiral matter completion and anomaly analysis;
- absolute photon/interferometer prediction after scale/state fixing;
- experimental confirmation or falsification.

Those are the phenomenology/matter programme after the gravitational candidate is internally closed.
