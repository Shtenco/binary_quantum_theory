# BCQG IR HDA universality closure theorem

**Status:** conditional IR theorem + directly measured finite metric prerequisites.  This does not replace the preregistered collective GR killer and is not experimental confirmation.

## 1. Why this theorem is needed

The collective programme has historically listed several IR targets separately:

\[
D_{space}\to3,\qquad c_{DW}\to\frac12,\qquad z\to1,\qquad N_{phys}\to2,\qquad \Delta_{HH}\to0.
\]

They are valuable as independent numerical falsifiers, but in a regular local metric phase they are not independent physical knobs.  The purpose of this theorem is to identify the smallest logically independent closure set and to prevent brute-force calculations from being mistaken for separate laws of nature.

The old `COLLECTIVE_GR_UNIVERSALITY_PREREGISTRATION.md` remains frozen as an independent cross-check.  Nothing below changes its PASS/FAIL thresholds retroactively.

## 2. Direct BCQG prerequisites already established at the first coarse block

The first exact barycentric coarse block supplies a six-dimensional intrinsic carrier

\[
P=W_gW_g^\dagger,\qquad 6=A_1\oplus E\oplus T_2.
\]

The BCQG-native coarse face-flux Gram response has

\[
\operatorname{rank} B_F=6,\qquad \operatorname{cond}B_F=1,
\]

and therefore a nondegenerate metric map

\[
\boxed{h=M_{hq}q}
\]

with

\[
M_{hq}^TM_{hq}=\frac14I-\frac1{12}O_{opp},
\]

\[
s_{A_1}^2=s_E^2=\frac16,\qquad s_{T_2}^2=\frac13.
\]

Thus the six coarse quantum directions are not merely labelled as metric directions: they are directly calibrated by gauge-invariant flux observables.

The homogeneous direct gravitational block also vanishes exactly in the frozen real Peter--Weyl convention:

\[
\boxed{P H_E P=0,\qquad P S P=0,\qquad PGP=0}.
\]

Consequently a nontrivial collective gravitational kinetic tensor is necessarily a return/self-energy effect rather than a fitted direct 6x6 term.

## 3. Canonical depth-two operator: no free denominator

Let `C` denote the Hermitian collective scalar constraint on a target-independent enlarged Krylov space and decompose

\[
\mathcal H=P\mathcal H\oplus Q\mathcal H,\qquad Q=I-P.
\]

Write a zero-constraint state as

\[
|\Psi\rangle=|p\rangle+|q\rangle.
\]

The two projected equations are

\[
PCP|p\rangle+PCQ|q\rangle=0,
\]

\[
QCP|p\rangle+QCQ|q\rangle=0.
\]

On the coupled `Q` subspace where `QCQ` is invertible,

\[
|q\rangle=-(QCQ)^{-1}QCP|p\rangle,
\]

hence

\[
\boxed{
C_{eff}(0)=PCP-PCQ(QCQ)^{-1}QCP.
}
\]

For the homogeneous gravitational carrier `PCP=0`, so

\[
\boxed{
C_{eff}(0)=-PCQ(QCQ)^{-1}QCP.
}
\]

This is the zero-energy Schur/Feshbach complement of the actual constraint equation.  Its denominator is derived, not fitted.

If `QCQ` has an exact kernel coupled to `P`, the corresponding states are low-energy/constraint directions and must be promoted into the retained carrier.  They may not be hidden by an arbitrary regulator chosen after inspecting the GR target.  After exact kernel separation a Moore--Penrose inverse on the orthogonal complement is an equivalent canonical statement.

## 4. S4 collapses the effective metric problem to three real numbers

If the homogeneous block operator commutes with the tetrahedral `S4` action, then `P`, `Q`, `QCQ`, its inverse on an invariant coupled subspace, and therefore `C_eff` are all equivariant.

Because the six-edge carrier is multiplicity free,

\[
6=A_1\oplus E\oplus T_2,
\]

Schur's lemma gives

\[
\boxed{
C_{eff}=\kappa_{A_1}P_{A_1}+\kappa_E P_E+\kappa_{T_2}P_{T_2}.
}
\]

Therefore a homogeneous 6x6 collective scalar never requires 36 independent physical amplitudes.  It requires three channel eigenvalues plus covariance/leakage diagnostics.

After the independently measured metric calibration, physical metric-coordinate eigenvalues scale as

\[
\lambda_{A_1}^{(h)}=6\kappa_{A_1},\qquad
\lambda_E^{(h)}=6\kappa_E,\qquad
\lambda_{T_2}^{(h)}=3\kappa_{T_2}.
\]

Hence rotational restoration of the five traceless modes is equivalent to the blind raw-coordinate condition

\[
\boxed{\kappa_{T_2}=2\kappa_E}.
\]

For the ADM inverse-DeWitt coefficient `c=1/2`, the trace/traceless ratio further gives

\[
\boxed{
\kappa_{A_1}:\kappa_E:\kappa_{T_2}=-\frac12:1:2.
}
\]

The overall common scale is not a GR-shape test; it belongs to the Newton/wave-function normalization.

## 5. Restricted IR HDA uniqueness theorem

Assume the collective long-wavelength phase satisfies all of the following target-independent conditions.

### H1. Uniform nondegenerate metric phase

The coarse BCQG metric map remains rank six under refinement with finite upper and lower singular-value bounds, so the dynamical metric is uniformly equivalent to the recursive PL-S3 background on the smooth sector.

### H2. Local parity-even two-derivative leading Hamiltonian

After retaining every exact zero/low-energy Krylov sector, the leading smooth metric Hamiltonian admits the derivative expansion

\[
H[N]=\int d^3x\,N\left[
A\frac{\pi_{ab}\pi^{ab}-c\pi^2}{\sqrt q}
-B\sqrt q(R-2\Lambda)
\right]+O(\epsilon^p,\partial^4),
\]

with finite nonzero `A,B` and corrections vanishing in the declared IR/refinement limit.

### H3. First-class hypersurface-deformation algebra

The collective constraints satisfy

\[
\{H[N],H[M]\}\to D[q^{ab}(N\partial_bM-M\partial_bN)]
\]

with the Gauss and spatial-diffeomorphism sectors closing first class and the normalized defect tending to zero.

### H4. Regular complete constraint set

After Gauss reduction there is no additional independent first-class or second-class constraint acting on the regular metric phase, and the metric kinetic form is nondegenerate.

Then the repository's direct ADM bracket identity

\[
\{H[N],H[M]\}
=AB\left[D[\beta]+4\left(c-\frac12\right)I[N,M]\right]
\]

forces, for generic canonical data and arbitrary lapses,

\[
\boxed{c=\frac12,\qquad AB=1.}
\]

Thus the leading local two-derivative collective Hamiltonian belongs to the ADM/Einstein family, up to the usual remaining couplings `G` and `Lambda`:

\[
A=16\pi G,\qquad B=(16\pi G)^{-1}.
\]

No fit of `c` is available once H1--H4 hold.

## 6. Consequences that are no longer independent miracles

### 6.1 DeWitt signature

At `c=1/2` the six-dimensional metric kinetic form has one conformal negative direction and five positive traceless directions.  Pulling it back to nine flux components adds exactly the three common-rotation Gauss zeros:

\[
\boxed{(N_+,N_-,N_0)=(5,1,3)}.
\]

### 6.2 Relativistic tensor cone

For the TT sector,

\[
\ddot h_{TT}=AB\,\nabla^2h_{TT}+\cdots,
\]

so `AB=1` implies

\[
\boxed{c_T^2=1,\qquad z=1}
\]

in units set by the hypersurface normal, up to irrelevant higher-derivative corrections.

### 6.3 Two physical metric modes

After the exact three-dimensional Gauss/frame quotient, the nondegenerate metric phase has 12 canonical metric phase-space dimensions.  Three first-class momentum constraints plus one first-class scalar constraint remove eight phase-space dimensions, leaving four physical phase-space dimensions:

\[
\boxed{N_{phys}^{config}=2}.
\]

Equivalently, in the unreduced connection/flux count used by the preregistered killer,

\[
\frac{18-2(3+3+1)-0}{2}=2.
\]

### 6.4 Spatial dimension

The recursive background is a PL three-manifold.  If H1 holds uniformly, the dynamical coarse metric is bilipschitz-equivalent to that background on the smooth sector, so its local Hausdorff dimension remains three.  With the additional standard smooth uniformly elliptic continuum limit of the metric Laplacian, the local heat-kernel/spectral dimension is also three.  The existing FEM sequence is retained as an independent finite-resolution cross-check, not as the logical source of the number three.

## 7. What remains logically independent

The theorem reduces the internal GR closure problem to four genuinely independent classes rather than a long list of correlated targets:

1. **operator correctness:** finish the corrected tetrahedral-volume Hermitian Lorentzian finite rerun and preserve covariance/Hermiticity;
2. **RG metric regularity/locality:** show uniform nondegeneracy and that nonlocal/higher-derivative pieces are irrelevant in the smooth blocked phase;
3. **collective HDA:** demonstrate the first-class HDA on the blocked theory in the declared refinement limit;
4. **constraint completeness:** verify that the known `3 Gauss + 3 diffeomorphism + 1 Hamiltonian` generators are independent on the regular carrier and that no additional first/second-class sector survives.

Once these four are established, `c=1/2`, `AB=1`, `z=1`, DeWitt signature and two graviton configuration modes are consequences, not separately tunable assumptions.

The old collective killer should still measure them independently.  Agreement is then a powerful overdetermined validation; disagreement falsifies at least one hypothesis of this theorem.

## 8. What "internal closure" would and would not mean

If the four classes above pass and the microscopic/collective ledgers are synchronized, BCQG may legitimately be called a **closed internal candidate theory of the gravitational IR phase**: the microscopic operator, coarse geometry, leading IR constraint algebra, mode count and matter-coupling interface are all defined with explicit falsifiers.

This still does **not** mean that nature has been proved to obey BCQG.  Absolute scale setting, vacuum/state selection, precision phenomenology and experimental comparison remain empirical work.  `G` and `Lambda` being low-energy couplings is not by itself a logical inconsistency of the gravitational theory.

## 9. Practical shortest path

Do not next compute arbitrary 36-entry 6x6 matrices.

The shortest non-circular route is:

```text
corrected Lorentzian V2
        |
        v
build exact coupled P+Q Krylov block
        |
        +--> separate exact QCQ kernel into retained low-energy carrier
        |
        v
canonical zero-energy Schur complement
        |
        v
three S4 channel eigenvalues + leakage
        |
        +--> blind ratio -1/2 : 1 : 2   (independent cross-check)
        |
        v
collective HDA + rank/completeness over refinement
        |
        v
restricted IR uniqueness theorem
        |
        v
ADM/GR(G,Lambda) + 2 tensor modes
```

This is the current minimal theorem-level closure programme.
