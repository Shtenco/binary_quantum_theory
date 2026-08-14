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

Ordinary antimatter is not identified with the project orientation label `chi`. Charge conjugation, parity and the project-local orientation bit are distinct operations.

## Microscopic 16-cell mirror order

The 16 tetrahedra of the minimal flag 16-cell can be labelled by the four binary choices of one vertex from each antipodal pair. Two tetrahedra share a face exactly when their four-bit labels differ in one bit, so their dual graph is the four-dimensional hypercube `Q4` with 16 vertices, 32 edges and degree four.

Because `Q4` is bipartite, define

`eta_v=(-1)^popcount(v)`

and the staggered logical orientation variable

`sigma_v=eta_v Y_v`.

The geometric gluing preference `Y_v Y_w=-1` across a shared face then becomes `sigma_v sigma_w=+1`. This removes the alternating local frame orientation and exposes a genuine block order parameter

`Sigma=(1/16) sum_v eta_v Y_v`.

The two exact gluing vacua have `Sigma=+1` and `Sigma=-1` and are mirror partners. A single local orientation defect costs exactly `8J`; a half-hypercube mirror domain wall frustrates eight bonds and costs exactly `16J`.

`scripts/mirror_order_16cell_gate.py` diagonalizes the full `2^16=65536` staggered transverse-field Hilbert space. At `h/J=0.2` it finds `<Sigma^2>=0.997653947371...`, `<|Sigma|>=0.998747825258...`, an unresolved-at-machine-scale mirror-doublet splitting below `1e-12 J`, and a gap to the next state of `7.97008787696 J`.

As `h/J` is increased to 4, `<Sigma^2>` falls to about `0.146274`, providing a finite ordered-to-disordered control.

The same staggered two-colouring persists through the checked global barycentric PL refinements with 16, 384 and 9216 tetrahedra. Thus `Y_L/Q -> staggered Sigma -> sigma(x)` has a finite microscopic candidate along the actual recursive PL branch.

## Healthy orientation-dependent force construction

A direct metric sign flip was rejected as the minimal healthy mechanism. `H_chi=s_chi H_GR` preserves the same normalized HDA only for `s_chi^2=1`; the `s=-1` case is lapse/time-orientation reversal, not static antigravity. A negative Einstein-Hilbert coefficient would instead flip the graviton kinetic sign and create a ghost relative to positive-energy matter.

The healthy candidate keeps tensor gravity positive-energy and adds a canonical mirror-odd order/mediator sector. The continuum matter HDA principal identity passes numerically at relative defect `7.146414566848946e-15`.

For opposite orientation charges, the Yukawa force exceeds tensor attraction when

`alpha > alpha_crit(x)=exp(x)/(1+x)`, with `x=m_sigma r`.

Canonical normalization gives

`alpha=beta_m^2/(4*pi*G*Z_sigma)`.

The existing Hodge geometry fixes the spatial stiffness matching

`J_f=Z_sigma A_f/d_f`, hence `Z_sigma=J_f d_f/A_f`.

For a regular tetrahedral seed,

`Z_sigma=(2sqrt(2)/3)J/ell`

and therefore

`alpha=3 beta_m^2 ell/(8sqrt(2)pi G J)`

in natural units.

Pure geometry does not automatically source this force: the minimal orientation defect has the same energy in the two mirror vacua, hence `beta_geometry=0`.

## Matter matrix-element result: beta_m is now operationally defined

The earlier parity-even chirality bridge `sigma J5^0` remains a valid spin/chirality-sensitive candidate, but `scripts/mirror_matter_matrix_element_gate.py` gives a decisive static-source result for free massive Dirac matter:

`J5^0/J^0 = h |p|/E`.

Therefore the axial density vanishes at rest, and its unpolarized average vanishes at every momentum. The diagonal on-shell pseudoscalar bilinear also vanishes. Thus the old axial channel **cannot by itself provide a universal static mirror charge for cold unpolarized matter**.

The missing coefficient is instead defined directly by the rest-energy response:

`beta_m=(1/(chi m)) <dH_m/dsigma>_rest`.

This gives an immediate falsifier: if every physical microscopic matter state has zero mirror-odd rest-energy derivative, then `beta_m=0`, `alpha=0`, and the static mirror-force branch fails.

A minimal positive mirror-doublet control introduces `q=+/-1`, with `(sigma,q)->(-sigma,-q)`, and demands constant logarithmic response

`d ln m_q/dsigma=q beta`.

The unique positive solution at fixed normalization is

`m_q(sigma)=m_* exp(q beta sigma)`.

For aligned mirror partners `(sigma,q)=(chi v,chi)`, both branches have the same positive physical mass but opposite rest source `dE/dsigma=chi beta m`, so within this finite candidate `beta_m=beta`.

The same coefficient can be extracted from a mirror-resolved mass spectrum as

`beta=[ln m_+(sigma)-ln m_-(sigma)]/(2 sigma)`.

This derives the **form and extraction rule** for `beta_m`; it does not yet derive a numerical value from a realistic microscopic matter Hamiltonian.

## Sigma range result: long range is not automatic

The mirror order is `Z2`, so two ordered vacua do not imply a Goldstone mediator.

`scripts/mirror_sigma_range_gate.py` explicitly excludes the tiny finite-size tunnelling splitting and tracks

`Delta_sigma^(16)=E2-E0`.

At `h/J=0.2`,

`Delta_sigma^(16)/J=7.9700878769645...`.

The scanned finite-Q4 crossover softens the gap to about `3.39685259213 J` near `h/J=2.625`, but does not close it on the finite block.

Therefore the seed mirror order is not automatically long ranged. A physical mediator mass/range requires a refined collective-mode identification and temporal normalization. If a relativistic low-energy sigma mode exists,

`lambda_sigma=hbar c_sigma/Delta_sigma`.

Macroscopic mirror repulsion therefore requires an independent range condition

`m_sigma r <= O(1)`.

A mode that remains gapped at order microscopic `J` and has only microscopic range kills macroscopic repulsion even if `beta_m` is nonzero.

## Retained GR controls

The repository retains the DeWitt inertia result `(5+,1-,3 0)`, the declared ADM/HDA uniqueness result `c_DW=1/2` and `AB=1`, the corresponding `c_T=1` statement, two local physical metric configuration modes in D=3, BF/Ooguri negative controls, and the independent Regge IR universality branch.

## Beyond the certificate

No core integration arrow above remains `OPEN` at fixed safe cutoff. Separate questions include a fully uniform simultaneous `Jmax->infinity`, `epsilon->0` theorem; Lorentzian quantum measure/global unitarity; a microscopic TT information-mode action and coupling; realistic matter/gauge content, generations, chirality and all local/global anomalies; an explanation of any hidden mirror sector; physical scale/Newton constant; blind empirical predictions; and independent external replication.

For the mirror-force branch, the remaining chain is now sharply reduced to

`construct microscopic H_m(sigma)`

`-> compute beta_m=(chi m)^-1 <dH_m/dsigma>_rest`

`-> derive the refined/temporal sigma dispersion and m_sigma`

`-> combine with Hodge Z_sigma to predict alpha`

`-> require alpha>exp(m_sigma r)/(1+m_sigma r)`

`-> close the full Peter-Weyl x route x mirror quantum HDA`.

A viable macroscopic cross-sector repulsion requires all of these conditions simultaneously. The theory does not currently claim that they are satisfied in nature.
