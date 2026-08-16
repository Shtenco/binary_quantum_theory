# BCQG minimal internal-closure frontier

Date: 2026-08-17

This note is the current shortest-path map after the repo-wide audit and the restricted IR HDA universality theorem.  It is deliberately narrower than the historical list of independent numerical targets.

## What is no longer a logically independent open problem

Provided the hypotheses of `BCQG_IR_HDA_UNIVERSALITY_CLOSURE.md` hold, the following are derived rather than independently adjustable:

- spatial metric phase has `D=3` once the recursive PL-S3 metric remains uniformly nondegenerate/bilipschitz;
- HDA selects `c_DeWitt=1/2`;
- HDA normalization selects `AB=1`;
- the leading TT cone has `z=1` / unit characteristic speed in hypersurface-normal units;
- DeWitt metric signature is one conformal negative plus five traceless positive directions;
- after the regular seven first-class generators and no second-class remainder, the metric sector has exactly two physical configuration modes.

The preregistered collective killer still measures these quantities independently as an overdetermined falsifier.  They are not deleted from testing; they are removed only from the list of logically independent assumptions.

## The three remaining closure certificates

### C1 — corrected microscopic Lorentzian operator

Finish the tetrahedral charged-volume V2 finite orbit:

```text
24 forward + 24 direct-adjoint ordered terms
-> Hermitian S
-> covariance/leakage/cutoff/parity guards
```

The original six-term workers hit execution-time granularity limits.  `pl-16cell-hermitian-lorentzian-v2-single.yml` now runs one frozen ordered term per job with unchanged physics and the same V2 collector.

C1 is an operator-correctness certificate.  It is not a GR fit.

### C2 — complete low-energy blocked carrier / canonical Schur fixed point

At each retained coarse scale:

1. start with the six directly calibrated metric directions `P=W_g W_g^dagger`;
2. construct only the target-independent `Q` Krylov states actually reached by the corrected `E+S+R_op` operator;
3. diagonalize/compress `QCQ` on that coupled support;
4. every exact/near-zero mode coupled to `P` is promoted into the retained low-energy carrier, never regularized away;
5. iterate until the remaining coupled `Q` sector has a stable nonzero gap;
6. construct the zero-constraint Schur complement

\[
C_eff(0)=PCP-PCQ(QCQ)^{-1}QCP.
\]

On the homogeneous gravitational six-edge carrier `PCP=0`.

Because of exact S4 covariance, the final homogeneous metric block contains only

\[
\kappa_{A_1},\qquad \kappa_E,\qquad \kappa_{T_2},
\]

not 36 independent matrix elements.

The independently measured metric map supplies the blind GR check

\[
\boxed{\kappa_{A_1}:\kappa_E:\kappa_{T_2}=-1/2:1:2}.
\]

C2 must also report across refinement:

- minimum coupled-Q gap;
- retained low-energy carrier dimension and irreps;
- metric-map smallest/largest singular values;
- S4/rotational splitting;
- Schur-compression leakage/error.

A stable gap after all exact zero modes are retained is the cleanest test that there is no hidden additional gapless scalar/vector gravitational sector.  This is physically sharper than searching for an arbitrary `r_extra` column after the fact.

### C3 — collective HDA fixed point

On the C2 low-energy carrier, use the already frozen lapse/refinement prescription and show

\[
\Delta_{HH}^{collective}\to0
\]

with the correct metric structure function.

For nondegenerate `q`, local lapse pairs such as `N=1`, `M=x^i` generate

\[
\beta^a=q^{ai},
\]

so a faithful HDA representation supplies three independent spatial-diffeomorphism directions automatically.  The flux-to-metric kernel supplies the three local Gauss/frame rotations.  The one scalar Hamiltonian plus these generators gives the standard seven-generator first-class set.

The remaining guard is not to tune a rank threshold but to verify:

- faithful action of the three shift directions on held-out perturbations;
- nonzero scalar constraint gradient/action;
- no additional exact/near-zero low-energy carrier sector after C2;
- no second-class residual in the projected constraint bracket matrix.

Once C3 and these completeness guards pass, the restricted IR HDA theorem forces the ADM/Einstein leading Hamiltonian up to `G` and `Lambda`.

## Why locality is folded into C2 rather than treated as a fourth monster calculation

The microscopic operator is finite-range/local.  If the eliminated coupled `Q` sector has a stable nonzero gap, its inverse is a regular low-energy resolvent and the blocked self-energy is quasilocal; its homogeneous long-wavelength symbol admits a derivative expansion.  Tetrahedral/parity symmetry removes forbidden odd spatial tensors, while first-class HDA forbids a graviton mass/anomalous trace kinetic term.  The leading nontrivial smooth metric term is therefore the two-derivative ADM class, with higher-derivative corrections tracked as irrelevant terms.

This statement must still be checked numerically by the scaling of the low-momentum symbol / block couplings, but it does not require fitting an arbitrary continuum action coefficient-by-coefficient.

## Internal closure criterion

The gravitational core may be labelled `INTERNALLY_CLOSED_CANDIDATE` only when all three certificates are green:

```text
C1 corrected Lorentzian operator      PASS
C2 low-energy Schur/RG fixed point    PASS
C3 collective HDA/completeness        PASS
```

Then the consequences are theorem-level:

```text
D=3 metric phase
c_DeWitt=1/2
AB=1
z=1
(5+,1-) metric kinetic signature
3 Gauss zeros in flux variables
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
