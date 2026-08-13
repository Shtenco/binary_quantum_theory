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

## Retained GR controls

The repository retains the DeWitt inertia result `(5+,1-,3 0)`, the declared ADM/HDA uniqueness result `c_DW=1/2` and `AB=1`, the corresponding `c_T=1` statement, two local physical metric configuration modes in D=3, BF/Ooguri negative controls, and the independent Regge IR universality branch.

## Beyond the certificate

No core integration arrow above remains `OPEN` at fixed safe cutoff. Separate questions are a uniform simultaneous `Jmax->infinity`, `epsilon->0` limit; uniqueness of the global q=2 gluing from the bare causal rewrite if the PL completion is not frozen; Lorentzian quantum measure/unitarity; matter/chirality/anomalies; scale setting; blind empirical predictions; and independent external replication.
