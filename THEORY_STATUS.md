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

For two nodes, the coefficient `N0*M1-N1*M0` starts at order epsilon. The independently fixed nonzero route target is order `epsilon^-1`. Consequently the normalized geometry-route correction is `O(epsilon)` and the normalized pure-geometry correction is `O(epsilon^2)`.

`Delta_full <= Delta_route + C_cross*epsilon + C_GG*epsilon^2 -> 0`.

**Status:** the previous fixed-cutoff Lorentzian integration bottleneck is closed. A direct 11.3M-state `[H_L,H_L]` matrix enumeration is optional regression evidence, not a logical prerequisite.

## Admissible simultaneous cutoff path

Using conservative fixed-valence norm bounds,

`||V||=O(J^(3/2))`, `||H_E||=O(J^(3/2))`, `||K||=O(J^3)`, `||H_L||=O(J^(15/2))`, while the nondegenerate route target scales as `D=O(J^2/epsilon)`.

Hence

`C_cross/D = O(epsilon*J^(13/2))`,

`C_GG/D = O(epsilon^2*J^13)`.

For `Jmax(epsilon)=epsilon^-alpha`, both vanish whenever `0<alpha<2/13`. Thus an admissible simultaneous family exists, e.g. `Jmax=epsilon^-1/8`. This is not a uniform theorem for every possible joint path.

## Spin-2, foam and GW extension

The exact four-qubit decomposition contains one `j=2` irrep. The extremal `m=+/-2` states form a two-state code inside that spin-2 sector and pass the finite projector gate. This supports the candidate identification of a massless spin-2 polarization space with one logical helicity qubit.

If the frozen metric smoothing exponent is additionally interpreted as a quantum RMS exponent, the low-k conditional prediction is `P_foam(k)~k^1.003414`. If a physical TT information mode exists and has nonzero quadratic metric coupling, the candidate parametric resonance is centered near `Omega_GW=2*omega_I`. These are conditional physical extensions, not experimentally established facts.

## Mirror/chirality result

The logical-qubit mirror operation is complex conjugation in the real singlet basis:

`X_L -> X_L`, `Z_L -> Z_L`, `Y_L -> -Y_L`.

Because `Q=(sqrt(3)/4)Y_L`, mirror swaps `Q=+/-sqrt(3)/4` while preserving shape observables and absolute-volume information. A reflected tetrahedron reverses orientation but preserves the metric Gram matrix, absolute volume and face-flux Gram data.

Therefore in the currently tested mirror-even metric/HDA architecture

`g00(+chi)=g00(-chi)`.

**Orientation alone does not produce metric antigravity.** `H->-H` is lapse/time-orientation reversal, while a negative Einstein-Hilbert coefficient gives a wrong-sign graviton kinetic term relative to positive-energy matter.

The same mirror/conjugation structure gives `d(Rbar)=-d(R)` for the perturbative cubic gauge-anomaly coefficient. This is not yet a realistic chiral matter spectrum or a proof of all global anomaly conditions.

## Microscopic 16-cell mirror order

The 16 tetrahedra of the minimal flag 16-cell are labelled by four binary antipodal choices. Two tetrahedra share a face iff their labels differ in one bit, so the tetrahedron dual graph is exactly the four-dimensional hypercube `Q4` with 16 vertices, 32 edges and degree four.

Define

`eta_v=(-1)^popcount(v)`,

`sigma_v=eta_v Y_v`,

`Sigma=(1/16) sum_v eta_v Y_v`.

Because `Q4` is bipartite, the geometric gluing preference `Y_vY_w=-1` becomes uniform `sigma_vsigma_w=+1`. The two exact gluing vacua have `Sigma=+1` and `Sigma=-1`.

A local orientation defect costs exactly `8J`; a half-hypercube domain wall costs `16J`.

The full `2^16=65536` transverse-field control at `h/J=0.2` gives `<Sigma^2>=0.997653947371...`, `<|Sigma|>=0.998747825258...` and a mirror-doublet splitting below `1e-12 J`.

The staggered two-colouring persists through the checked recursive PL refinements with 16, 384 and 9216 tetrahedra. Thus

`Y_L/Q -> staggered Sigma -> sigma(x)`

has a finite microscopic candidate along the actual recursive PL branch.

## Healthy orientation-dependent force construction

The healthy candidate keeps tensor gravity positive-energy and adds a canonical mirror-odd order/mediator sector. The continuum canonical matter HDA principal identity passes at relative defect `7.146414566848946e-15`.

For opposite orientation charges, the Yukawa channel exceeds tensor attraction when

`alpha > alpha_crit(x)=exp(x)/(1+x)`, `x=m_sigma r`.

Canonical normalization gives

`alpha=beta_m^2/(4*pi*G*Z_sigma)`.

The existing Hodge geometry fixes the spatial stiffness matching

`J_f=Z_sigma A_f/d_f`, hence `Z_sigma=J_f d_f/A_f`.

For a regular tetrahedral seed,

`Z_sigma=(2sqrt(2)/3)J/ell`

and therefore

`alpha=3 beta_m^2 ell/(8sqrt(2)pi G J)`

in natural units.

Pure geometry does not automatically source the force: the minimal orientation defect has equal energy in the two mirror vacua, so `beta_geometry=0`.

## Matter matrix element: the static source is now sharply defined

The earlier chirality bridge `sigma J5^0` remains parity allowed and can describe spin/chirality-sensitive physics. But the explicit free-Dirac gate gives

`J5^0/J^0 = h |p|/E`.

Thus `J5^0=0` at rest and its unpolarized average vanishes at every momentum. The diagonal on-shell pseudoscalar bilinear also vanishes. Therefore this axial channel **cannot by itself supply a universal static mirror charge for cold unpolarized matter**.

The static coefficient is instead the Hellmann-Feynman rest-energy response

`beta_m=(1/(chi*m)) <dH_m/dsigma>_rest`.

If this vanishes for every physical state, then `beta_m=0`, `alpha=0`, and the static mirror-force branch fails.

More generally, let matter have a mirror label `q=+/-1` and a positive rest-mass law obeying only

`m_q(sigma)=m_-q(-sigma)`.

For aligned mirror vacua `(q,sigma)=(+1,+v)` and `(-1,-v)`, mirror covariance gives

`m_+(v)=m_-(-v)`

and, after differentiation,

`m_+'(v)=-m_-'(-v)`.

So mirror symmetry itself implies **equal positive mirror-partner masses and opposite static sigma derivatives**, whenever that derivative is nonzero. The source magnitude is

`beta_m=m_+'(v)/m_+(v)=-m_-'(-v)/m_-(-v)`.

The exponential law `m_q=m_*exp(q beta sigma)` is only the globally positive constant-`beta_m` control, not a prerequisite for the sign theorem.

## Concrete microscopic matter carrier: mirror Wilson-Dirac

A concrete finite matter Hamiltonian has now been built:

`H_q(k,sigma)=sum_i alpha_i sin(k_i)+beta_D[m_q(sigma)+r_W sum_i(1-cos k_i)]`.

For a mirror-covariant positive mass law, aligned mirror partners have identical positive spectra and opposite Hellmann-Feynman rest sources.

In the deterministic control `m_*=0.4`, `beta=0.37`, `v=0.8`, `r_W=1`,

`m_phys=0.5377880627328211`

and

`Q_sigma=+/-0.19898158321114381`.

The moving-state identity is satisfied to machine precision. In the separate massless Wilson corner control, only `k=(0,0,0)` remains zero; the other seven three-dimensional Brillouin corners are lifted by the Wilson term.

This proves compatibility of positive spectrum, opposite static mirror charge and Wilson corner-doubler removal in a concrete carrier. **It does not derive the numerical beta, realistic gauge/chiral matter, or the irregular PL/Peter-Weyl matter theory.**

## Sigma range: corrected symmetry-resolved result

The mirror order is `Z2`, so two ordered vacua do not imply a Goldstone mediator. The tiny finite mirror-doublet splitting is tunnelling, not a propagating sigma mass.

There is a second trap: raw `E2-E0` can belong to the wrong `Z2` parity and therefore have zero matrix element with the mirror-odd order operator `Sigma`.

The physically relevant finite diagnostic is

`Delta_sigma,odd = min(E_n-E0)`

for states outside the tunnelling doublet with nonzero `|<0|Sigma|n>|^2`.

`scripts/mirror_sigma_range_gate.py` block-diagonalizes the 65536-state Hilbert space into exact even/odd parity sectors of dimension 32768 each and computes the `Sigma` spectral weights.

At `h/J=0.2`,

`Delta_sigma,odd/J = 7.9700878769647...`.

The softest checked mirror-odd point is near `h/J=2.2`,

`Delta_sigma,odd/J = 5.5841056685297...`.

At `h/J=2.625`, the previously quoted raw value `E2-E0 ~= 3.39685J` is **not** the sigma mediator gap; the actual first additional `Sigma`-coupled odd excitation is

`Delta_sigma,odd/J = 6.110727269331...`.

Thus the finite seed is less favorable to long-range propagation than the raw spectrum suggested.

The gate also evaluates the low-frequency Lehmann response after removing the tunnelling state,

`chi_*(i omega)=A_*-B_* omega^2+...`,

so the finite-block inverse-susceptibility time coefficient is

`Z_t^(16)=B_*/A_*^2`.

At `h/J=0.2`, the 16-level odd spectrum captures more than `99.9998%` of the non-tunnelling `Sigma` weight, gives `J Z_t^(16) ~= 401.15`, and `omega_eff/J ~= 7.97009`.

This is microscopic finite-block time-response information, **not yet the continuum temporal normalization**. A physical `m_sigma` requires refined block/volume normalization, low-momentum dispersion and scale setting.

## Dimensionless MIRRORMASTER criterion

For the regular-seed Hodge normalization define

`g_*=GJ/ell`,

`j_sigma=J ell/(hbar c_sigma)`,

`R=r/ell`,

`Delta_sigma=delta_sigma J`.

Then `alpha` is no longer an independent phenomenological parameter:

`alpha=3 beta_m^2/(8sqrt(2)pi g_*)`.

The Yukawa range exponent is

`x=m_sigma r=delta_sigma j_sigma R`.

Therefore opposite-`chi` repulsion is exactly equivalent to

`beta_m^2 > (8sqrt(2)pi/3) g_* exp(x)/(1+x)`.

Equivalently,

`beta_m^2 > (8sqrt(2)pi/3) g_* exp(delta_sigma j_sigma R)/(1+delta_sigma j_sigma R)`.

The order-one range requirement `x<=1` gives

`j_sigma <= 1/(delta_sigma R)`.

So any future microscopic matter+mirror calculation only has to provide the genuinely microscopic inputs `beta_m`, `g_*`, and the refined `delta_sigma*j_sigma`; it is no longer legitimate to choose `alpha` by hand.

## Retained GR controls

The repository retains the DeWitt inertia result `(5+,1-,3 0)`, the declared ADM/HDA uniqueness result `c_DW=1/2` and `AB=1`, the corresponding `c_T=1` statement, two local physical metric configuration modes in D=3, BF/Ooguri negative controls, and the independent Regge IR universality branch.

## Beyond the certificate

No core integration arrow remains `OPEN` at fixed safe cutoff. Separate questions include a fully uniform simultaneous `Jmax->infinity`, `epsilon->0` theorem; Lorentzian quantum measure/global unitarity; a microscopic TT information-mode action and coupling; realistic matter/gauge content, generations, chirality and all local/global anomalies; physical scale/Newton constant; blind empirical predictions; and independent external replication.

For the mirror-force branch the unresolved chain is now sharply reduced to

`realistic microscopic H_m(sigma)`

`-> numerical beta_m=(chi m)^-1 <dH_m/dsigma>_rest`

`-> absolute g_*=GJ/ell`

`-> refined mirror-odd dispersion / delta_sigma*j_sigma`

`-> MIRRORMASTER PASS/FAIL`

`-> full Peter-Weyl x route x mirror-matter quantum HDA`.

A viable macroscopic cross-sector repulsion requires all of these conditions simultaneously. The project does **not** currently claim that they are satisfied in nature.
