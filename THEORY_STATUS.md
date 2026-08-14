# Theory status — canonical ledger

**Frozen 2026-08-14.** This file supersedes historical frontier wording elsewhere in the repository.

## Closed core candidate chain

`bits -> q=2 -> S2 -> recursive PL S3 -> 3D slice scaling -> z~1 -> 4D-like history -> smooth IR`

`SU(2) -> H_E -> K=[V,H_E] -> C(V), C(K) -> H_E+(1+beta^2)H_L -> H_geom+route -> HDA`

The first line is supported by the frozen binary-route family, q=2 octahedral shell, canonical PL completion, held-out scaling and observer smoothing. The second line uses the finite Peter-Weyl geometry gates, the independently fixed sharp/path sector, the two-node Euclidean joint gate, the Lorentzian support wall and the final fixed-cutoff composition theorem.

Frozen numerical anchors include `d_H=2.999229782`, `z=0.998281156`, `d_s(slice)=3.004393867`, `d_s(history)~4.004393867`, and `Delta_joint(1/64)=0.014707752821092098` in the preregistered two-node Euclidean geometry x route gate.

## Final fixed-cutoff Lorentzian composition theorem

For an all-`j=1/2` input the full Lorentzian HH support is safe at `Jmax=13/2`. At that fixed cutoff the local operator `G_v=H_E,v+(1+beta^2)H_L,v` is bounded.

Use the frozen route-habitat family `N=Nbar+epsilon*n`, `M=Mbar+epsilon*m`, and `Omega_Q=epsilon^-1 OmegaTilde_Q`. For every geometry transition, the apparent `epsilon^-1` geometry-route contribution cancels state by state between the two lapse orderings. The remainder is order one.

For two nodes, the coefficient `N0*M1-N1*M0` has no constant term and starts at order epsilon. The independently fixed nonzero route target is order `epsilon^-1`. Consequently the normalized geometry-route correction is `O(epsilon)` and the normalized pure-geometry correction is `O(epsilon^2)`.

The resulting fixed-cutoff bound is

`Delta_full <= Delta_route + C_cross*epsilon + C_GG*epsilon^2 -> 0`.

The constants may depend on the fixed cutoff, input sector and fixed beta, but not on epsilon. No Lorentzian coefficient or channel normalization is fitted to obtain this statement.

The exact algebraic expansion is recorded in `FINAL_CORE_ARCHITECTURE_CERTIFICATE.md`. Its executable premises are independently covered by `scripts/path_normal_hda_gate.py`, `scripts/peter_weyl_two_node_euclidean_joint_gate.py`, `scripts/lorentzian_hit_depth_bound.py`, and the retained real-beta regression.

**Status:** the previous fixed-cutoff Lorentzian integration bottleneck is closed. A direct 11.3M-state `[H_L,H_L]` matrix enumeration is optional regression evidence, not a logical prerequisite.

## Admissible simultaneous cutoff path

Using conservative fixed-valence norm bounds,

`||V||=O(J^(3/2))`, `||H_E||=O(J^(3/2))`, `||K||=O(J^3)`, `||H_L||=O(J^(15/2))`, while the nondegenerate route target scales as `D=O(J^2/epsilon)`.

Hence the normalized extra channels obey the conservative estimates

`C_cross/D = O(epsilon*J^(13/2))`,

`C_GG/D = O(epsilon^2*J^13)`.

For `Jmax(epsilon)=epsilon^-alpha`, both vanish whenever `0<alpha<2/13`. Thus an admissible simultaneous family exists, for example `Jmax=epsilon^-1/8`, but this is not yet a uniform theorem for every possible joint path.

## Spin-2, foam and GW extension

The exact four-qubit decomposition contains one `j=2` irrep. The extremal `m=+/-2` states form a two-state code inside that spin-2 sector and pass the finite projector gate. This supports the candidate identification of a massless spin-2 polarization space with one logical helicity qubit.

If the frozen metric smoothing exponent is additionally interpreted as a quantum RMS exponent, the low-k conditional prediction is `P_foam(k)~k^1.003414`. If a physical TT information mode exists and has nonzero quadratic metric coupling, the candidate parametric resonance is centered near `Omega_GW=2*omega_I`. These are conditional physical extensions, not experimentally established facts.

## Mirror/chirality result

The exact logical-qubit mirror operation is complex conjugation in the real singlet basis:

`X_L -> X_L`, `Z_L -> Z_L`, `Y_L -> -Y_L`.

Because the oriented volume coordinate is `Q=(sqrt(3)/4)Y_L`, mirror conjugation swaps the two orientation states `Q=+/-sqrt(3)/4` while preserving the two intrinsic shape observables and absolute-volume information. `scripts/mirror_chirality_gravity_gate.py` verifies this and an independent reflected-tetrahedron control.

For `A' = R A` with `R^T R=I` and `det R=-1`,

`det(A')=-det(A)` but `(A')^T A'=A^T A`.

Thus orientation reverses while the metric, absolute volume and face-flux Gram data remain unchanged. In the currently tested mirror-even metric/HDA architecture,

`g00(+chi)=g00(-chi)`.

Therefore **chirality/orientation alone does not produce antigravity in the present theory**.

A phenomenological orientation-odd acceleration `a_chi=a_even+chi*a_odd`, calibrated by `a_+=g_N`, gives `a_-/g_N=1-2f` with `f=a_odd/g_N`. Complete screening requires `f=1/2`, repulsion requires `f>1/2`, and equal-magnitude opposite acceleration requires `f=1`. The current mirror-even gate corresponds to `f=0`.

The same mirror/conjugation structure gives an exact perturbative cubic gauge-anomaly sign identity `d(Rbar)=-d(R)`, so a perfect `R + Rbar` mirror pair cancels that anomaly coefficient. This does not yet derive a realistic chiral matter spectrum or all global anomalies.

Ordinary antimatter is not identified with the project orientation label `chi`. Charge conjugation, parity and the project-local orientation bit are distinct operations. The ALPHA-g antihydrogen result is consistent with attractive Earth gravity and rules out repulsive `1g` gravity for ordinary antihydrogen.

## Microscopic 16-cell mirror order

The 16 tetrahedra of the minimal flag 16-cell can be labelled by the four binary choices of one vertex from each antipodal pair. Two tetrahedra share a face exactly when their four-bit labels differ in one bit, so their dual graph is the four-dimensional hypercube `Q4` with 16 vertices, 32 edges and degree four.

Because `Q4` is bipartite, define

`eta_v=(-1)^popcount(v)`

and the staggered logical orientation variable

`sigma_v=eta_v Y_v`.

The geometric gluing preference `Y_v Y_w=-1` across a shared face then becomes `sigma_v sigma_w=+1`. This removes the alternating local frame orientation and exposes a genuine block order parameter

`Sigma=(1/16) sum_v eta_v Y_v`.

The two exact gluing vacua have `Sigma=+1` and `Sigma=-1` and are mirror partners. A single local orientation defect costs exactly `8J`; a half-hypercube mirror domain wall frustrates eight bonds and costs exactly `16J`.

`scripts/mirror_order_16cell_gate.py` diagonalizes the full `2^16=65536` staggered transverse-field Hilbert space. At `h/J=0.2` it finds

`<Sigma^2>=0.997653947371...`,

`<|Sigma|>=0.998747825258...`,

an unresolved-at-machine-scale mirror-doublet splitting below `1e-12 J`, and a gap to the next state of `7.97008787696 J`.

As `h/J` is increased to 4, `<Sigma^2>` falls to about `0.146274`, providing a finite ordered-to-disordered control.

This is the first finite microscopic derivation of the coarse mirror order parameter: `Y_L/Q -> staggered Sigma -> sigma(x)`. The physical normalization, continuum kinetic coefficient and matter coupling are not fixed by this gate.

## Healthy orientation-dependent force construction

A direct metric sign flip was tested conceptually and rejected as the minimal healthy mechanism. If one simply rescales the gravitational Hamiltonian,

`H_chi[N]=s_chi H_GR[N]`,

then the HDA bracket scales as `s_chi^2 D`. Preserving the same HDA normalization requires `s_chi^2=1`. The `s=-1` branch is equivalent to `N->-N`, i.e. reversal of normal/time orientation, not reversal of static gravity.

Likewise, making the Einstein-Hilbert coefficient negative would make an effective Newton coupling negative only by also flipping the graviton kinetic sign, producing a ghost relative to positive-energy matter.

The first healthy candidate therefore keeps the tensor-gravity kinetic term positive and introduces a mirror-odd order/mediator sector. A conservative continuum realization uses `sigma` plus a second pseudoscalar `phi`, positive canonical kinetic terms and the mirror-even bounded potential

`U=mu^2 phi^2/2 + lambda phi^4/4 + g phi sigma + kappa(sigma^2-v^2)^2/4`.

Mirror acts as `(phi,sigma)->(-phi,-sigma)`.

The canonical matter-sector HDA principal identity is

`{H_m[N],H_m[M]} = D_m[N dM - M dN]`.

`scripts/orientation_odd_hda_gate.py` checks it on a periodic spectral grid with `L=512` and obtains

`abs error = 5.204170427930421e-18`,

`relative error = 7.146414566848946e-15`.

The local potential terms cancel from the antisymmetric bracket exactly at continuum level.

For a coarse orientation charge `Q_chi=eta*m*chi`, mediator exchange gives the candidate Yukawa potential

`U12=-G_T m1 m2/r - alpha G_T m1 m2 chi1 chi2 exp(-m_phi r)/r`.

Equal `chi` gives extra attraction. Opposite `chi` gives repulsion. With `x=m_phi r`, the orientation-force magnitude relative to bare tensor gravity is

`alpha(1+x)exp(-x)`.

Thus the exact screening threshold is

`alpha_crit(x)=exp(x)/(1+x)`.

In the long-range limit `x<<1`, `alpha=1` gives complete screening and `alpha>1` gives cross-sector repulsion. At the finite demonstration point `alpha=2`, `x=0.1`, the net opposite-chi outward force is `0.990642319679...` times the bare tensor-gravity force after cancellation.

This is a **healthy antigravity-like fifth-force candidate**, not yet a mirror sign flip of `g00`. The microscopic mirror-order gate now removes the need to postulate `sigma` from nothing. A minimal next branch can test whether soft fluctuations of the derived `Sigma/sigma` order parameter itself can play the mediator role, eliminating the auxiliary `phi` field.

## Retained GR controls

The repository retains the DeWitt inertia result `(5+,1-,3 0)`, the declared ADM/HDA uniqueness result `c_DW=1/2` and `AB=1`, the corresponding `c_T=1` statement, two local physical metric configuration modes in D=3, BF/Ooguri negative controls, and the independent Regge IR universality branch.

## Beyond the certificate

No core integration arrow above remains `OPEN` at fixed safe cutoff. Separate questions include a fully uniform simultaneous `Jmax->infinity`, `epsilon->0` theorem; Lorentzian quantum measure/global unitarity; a microscopic TT information-mode action and coupling; realistic matter/gauge content, generations, chirality and all local/global anomalies; an explanation of any hidden mirror sector; physical scale/Newton constant; blind empirical predictions; and independent external replication.

For the mirror-force branch, the open chain is now narrower:

`Y_L/Q -> staggered Sigma` is finite-tested,

while

`Sigma -> continuum normalization -> matter charge -> alpha -> full Peter-Weyl x route x mirror HDA`

remains to be derived. A viable cross-sector repulsion requires `alpha>alpha_crit(m_phi r)` in the desired range while keeping the Hamiltonian bounded and the enlarged constraint algebra first class.
