# Causal-Invariant Multiway Frame-Infograph Gravity (CIMFIG)

## Status

**Computable architecture candidate. Not a proven theory of nature.**

## 1. Fundamental state

A microscopic state is

$$
\Omega=(H,e,q),
$$

where:

- \(H\) is a finite directed hypergraph;
- \(e\) assigns oriented frame/connection qubits or finite group elements to causal links or local diamonds;
- \(q\) contains matter labels and internal degrees of freedom.

The physical state is not one update history but a multiway history ensemble

$$
|\Psi\rangle=\sum_{\gamma} A[\gamma]|\gamma\rangle.
$$

## 2. Local dynamics

A finite family of local rewrite rules acts as

$$
R_a: (H,e,q)\longrightarrow(H',e',q').
$$

A rule family is admissible only if it passes multiple independent gates.

### Gate C1 — causal critical-pair confluence

Locally divergent update events must reconverge in the causal structure. In the finite implementation this is tested through bounded diamond completion.

### Gate C2 — frame-holonomy confluence

Reconvergent histories must agree on gauge-invariant boundary transport. Structural causal invariance alone does not imply this condition.

### Gate Q1 — history-space isometry

Individual update histories remain orthogonal at the fundamental quantum level. A local step must act isometrically or unitarily on the history Hilbert space.

### Gate Q2 — branchial observation map

Reconverged visible states are obtained by a density matrix, decoherence functional or quantum measure. Their amplitudes must not be naively added in a way that destroys unitarity.

## 3. Quantum measure

A candidate history amplitude is

$$
A[\gamma]
=\prod_{v\in\gamma} w(R_v,\Omega_v)
\exp\!\left(iS_{\rm frame}[\gamma]+iS_{\rm matter}[\gamma]\right).
$$

The weights and phases remain undetermined. They must satisfy normalization, composition, causal consistency and an appropriate positivity/unitarity condition.

## 4. Continuum condition

Let \(\Phi_D\) be a vector of scalar, frame and matter observables on a local causal diamond \(D\). A continuum candidate must satisfy projected, distributional RG convergence:

$$
P_\perp\bigl(\Phi(BD)-R_B\Phi(D)\bigr)\longrightarrow0
$$

in expectation and covariance over the multiway ensemble, while correlation length in lattice units diverges.

A four-dimensional phase must be obtained dynamically rather than inserted through the test corpus.

## 5. Gravity gate

The second variation of the ensemble effective action must possess:

- gauge/foliation null directions;
- exactly two positive gapless transverse-traceless modes;
- \(\omega^2\sim k^2\) in the infrared;
- no scalar ghost or negative-norm physical state;
- nonlinear Ward identities and universal coupling to stress-energy.

V17 showed that the tested scalar spectral-causal action span fails this gate. An oriented frame/connection sector reconstructs the free Fierz–Pauli ratio \(1:-2:2:-1\), but its dynamical emergence is open.

## 6. Matter gate

The theory must generate, rather than assume:

- a non-Abelian internal gauge structure;
- chiral fermions;
- anomaly cancellation;
- stable particle-like configurations;
- universal gravitational coupling;
- a scale-setting observable.

## 7. Falsifiers

CIMFIG is rejected if any of the following persists in the large-system limit:

1. update-order dependence of causal observables;
2. frame holonomy disagreement after reconvergence;
3. nonzero history-space unitarity defect;
4. no interacting four-dimensional critical phase;
5. failure of the microscopic TT Hessian gate;
6. unavoidable ghosts or anomalies;
7. regulator-dependent predictions with no universal limit.

## 8. Mathematical completion of the candidate

The previous gates become a well-defined research programme only after the
objects compared at a diamond are fixed.  For a finite boundary $B$, let
$\mathcal H_B$ be the boundary history space and let

$$
U_D:\mathcal H_{B_-}\longrightarrow
\mathcal H_{B_+}\otimes\mathcal H_{E_D}
$$

be the update map for a diamond $D$; $E_D$ records microscopic information
which is invisible at the boundary.  The observable channel is

$$
\mathcal E_D(\rho)=\operatorname{Tr}_{E_D}(U_D\rho U_D^\dagger).
$$

This formulation separates three statements which must not be conflated:

1. **causal confluence:** two update orders have isomorphic final causal
   boundaries;
2. **frame confluence:** their boundary Wilson loops (or complete separating
   set of holonomy invariants) agree;
3. **quantum consistency:** the corresponding channels agree,

   $$
   \left\|\mathcal E_{D,1}-\mathcal E_{D,2}\right\|_\diamond=0,
   $$

   after the canonical boundary identification.

The diamond norm supplies an operational finite-size defect

$$
\delta_D=\left\|\mathcal E_{D,1}-\mathcal E_{D,2}\right\|_\diamond,
$$

rather than a visual comparison of rewrite graphs.  A continuum sequence is
causally invariant only if the supremum of this defect over diamonds of fixed
physical diameter tends to zero.

### Proposition 1 — why reconvergent amplitudes cannot be added naively

Let $|\gamma_1\rangle,|\gamma_2\rangle$ be orthogonal microscopic histories
which have the same visible endpoint.  An isometry preserves

$$
\langle\gamma_1|\gamma_2\rangle=0.
$$

Replacing both histories by the same endpoint ket and assigning it amplitude
$A_1+A_2$ is therefore not an isometry: it erases the record which preserves
orthogonality.  Interference is legitimate only after embedding the record in
an environment and applying the channel above.  This proves the need for Q2;
it does **not** select the amplitudes $A[\gamma]$.

### Proposition 2 — two TT modes are necessary, not sufficient

For a nonzero spatial momentum $k_i$, a symmetric spatial tensor has six
components.  The three transverse conditions $k^ih_{ij}=0$ and the trace
condition $h^i{}_i=0$ leave two independent components.  Thus a rank-two TT
projector is a necessary kinematic gravity test.  It is not evidence that a
microscopic rule generates diffeomorphism symmetry: that requires the null
directions, constraint algebra, nonlinear Ward identities and universal soft
coupling to arise from one and the same microscopic action.

### Proposition 3 — exact content of the reduced critical model

The critical-phase demonstration uses

$$
S_{\rm red}=-\beta\sum_{\langle xy\rangle}
\left(s_x^+s_y^+ + s_x^\times s_y^\times\right),
\qquad s_x^a\in\{-1,+1\}.
$$

The partition function factorizes exactly,

$$
Z_{\rm red}(\beta)=Z_{\rm Ising}(\beta)^2,
$$

because there is no $+$-to-$\times$ interaction.  Consequently the model
contains two degenerate polarization channels by construction.  A crossing of
$\xi_L/L$ near the scanned interval can demonstrate that this *reduced
model* has a finite-size critical regime, but cannot establish the missing RG
map

$$
\mathcal R:\{R_a,w,e,q\}\longrightarrow S_{\rm red}+\text{irrelevant terms}.
$$

The required extension of CIMFIG is therefore not another fit of the reduced
model: it is an explicit coarse-graining map and a bound showing that every
symmetry-allowed polarization-mixing or ghost operator is irrelevant.

## 9. Quantitative verification ledger

The supplied unified program tests several logically different layers.  Its
results must be reported with these labels:

| Check family | Mathematical status | What it can establish | What remains open |
|:--|:--|:--|:--|
| 32,768-state boundary enumeration and Walsh transform | exact finite computation | the stated toy coarse action and truncation error | thermodynamic limit and universality |
| orientation and lattice pole | analytic/numerical kinematics | symmetric pole prescription and massless $L^{-2}$ gap scaling | interacting causal dynamics |
| TT projector and transfer matrix | finite-dimensional identity | two reduced modes and symplectic/unitary transfer | microscopic emergence of the reduction |
| flat Regge Hessian | finite-background calculation | gauge nulls and lifting of tested spurious nulls | all backgrounds and nonlinear stability |
| spin-2 bootstrap / linear ADM | conditional algebraic result | Fierz--Pauli ratio and two canonical modes under the assumptions | derivation of assumptions from rewrites |
| growth axioms | finite composition test | uniqueness in the tested phase ansatz | uniqueness of the full history measure |
| nonlinear HDA spectral test | truncated numerical test | residuals in the retained basis | closure without truncation |
| two-copy critical scan | stochastic finite-size evidence | a critical regime of $S_{\rm red}$ | the CIMFIG-to-Ising RG map |

The reference values embedded in the verifier are regression targets, not
independent experimental observations.  A successful run establishes that the
implementation reproduces those targets on the current platform.

## 10. Dimensionless continuum tests

For sizes $L$ and scale factor $b>1$, define observables which do not require
an externally chosen unit:

$$
z_{\rm eff}(L)=-\frac{\log[m(bL)/m(L)]}{\log b},
\qquad
\Delta_{\mathcal O}(L)=-\frac{\log[C_{\mathcal O}(bL)/C_{\mathcal O}(L)]}{\log b}.
$$

A candidate relativistic phase requires $z_{\rm eff}\to1$, stable scaling
dimensions, a diverging correlation length in lattice units, and restoration
of rotational symmetry in dispersion.  For the channel defect and unwanted
sectors the stronger limits are

$$
\delta_D(L)\to0,
\qquad
\frac{m_{\rm ghost}(L)}{m_{\rm phys}(L)}\to\infty,
\qquad
\frac{m_{\rm scalar}(L)}{m_{\rm phys}(L)}\to\infty.
$$

These ratios distinguish decoupling from merely failing to observe a mode on a
small lattice.

## 11. Minimal next calculation

The next falsifiable version should freeze a finite rule table and publish:

1. the complete critical-pair catalogue through a declared radius;
2. boundary holonomies and $\delta_D$ for every nontrivial diamond;
3. the coarse variables and blocking kernel defining $\mathcal R$;
4. covariance matrices and independent seeds for every stochastic estimate;
5. joint fits including correction-to-scaling terms, with held-out sizes;
6. the microscopic Hessian before TT projection, so that absence of ghosts is
   tested rather than imposed;
7. at least one dimensionless prediction fixed before the held-out run.

Until all seven items are present, V18 is a sharper **candidate architecture**:
it unifies causal, frame, quantum, continuum, gravity and matter requirements,
but it does not yet close the derivation from rewrite rules to nature.
