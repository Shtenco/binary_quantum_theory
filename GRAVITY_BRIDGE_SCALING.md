# Gravity bridge scaling: full Regge Hessian -> Fierz-Pauli

Status: **finite-lattice numerical evidence, not a proof of nonlinear Einstein gravity**.

This calculation was added specifically to avoid a circular TT-only check.  The microscopic 30-real-component Fourier Hessian of the flat 4D Regge lattice is computed first.  No TT projector is used.  The only geometric restriction is the linear map from the 15 edge-direction types to a general 10-component symmetric metric perturbation,

\[
\delta q_n=n^\mu n^\nu h_{\mu\nu}.
\]

The resulting full 10x10 quadratic kernel is fitted to the four independent two-derivative spin-2 tensor structures.  The continuum Fierz-Pauli target ratios are

\[
\boxed{(1,-2,2,-1)}.
\]

In parallel, the exact finite-Regge vertex-displacement gauge subspace is compared with the continuum metric subspace.  The leakage

\[
\epsilon_g=\frac{\|(I-P_{\rm metric})G_{\rm Regge}\|_F}{\sqrt{\dim G}}
\]

must vanish in the IR if the discrete gauge symmetry really becomes a metric gauge symmetry.

## Numerical scan

Lowest lattice momenta were used for three inequivalent orientations.  The kinetic convention is the repository convention after the sign audit,

\[
H_{\rm kin}=-H_{\rm Regge}.
\]

| orientation | L | gauge leakage | min gauge/metric cosine | full FP matrix residual | FP-ratio error |
|:--|--:|--:|--:|--:|--:|
| axial `(1,0,0,0)` | 3 | 3.44e-16 | 1.000000 | 0.110703 | 0.0690892 |
| axial `(1,0,0,0)` | 4 | 3.11e-16 | 1.000000 | 0.0603065 | 0.0386142 |
| axial `(1,0,0,0)` | 5 | 3.31e-16 | 1.000000 | 0.0379654 | 0.0246289 |
| diagonal2 `(1,1,0,0)` | 3 | 0.202430 | 0.957427 | 0.428674 | 0.131317 |
| diagonal2 `(1,1,0,0)` | 4 | 0.103160 | 0.989219 | 0.248615 | 0.0696412 |
| diagonal2 `(1,1,0,0)` | 5 | 0.0628422 | 0.996043 | 0.157486 | 0.0434141 |
| diagonal3 `(1,1,1,0)` | 3 | 0.316554 | 0.818232 | 0.501206 | 0.260722 |
| diagonal3 `(1,1,1,0)` | 4 | 0.168009 | 0.953201 | 0.316194 | 0.123993 |
| diagonal3 `(1,1,1,0)` | 5 | 0.100843 | 0.983346 | 0.201847 | 0.0738491 |

The fitted ratios themselves are:

| orientation | L | fitted ratios |
|:--|--:|:--|
| axial | 3 | `(1, -1.953480, 1.813946, -0.895343)` |
| axial | 4 | `(1, -1.973994, 1.896015, -0.941508)` |
| axial | 5 | `(1, -1.983404, 1.933680, -0.962691)` |
| diagonal2 | 3 | `(1, -1.894730, 1.789473, -0.657893)` |
| diagonal2 | 4 | `(1, -1.959434, 1.903406, -0.806291)` |
| diagonal2 | 5 | `(1, -1.979505, 1.944685, -0.876032)` |
| diagonal3 | 3 | `(1, -1.454538, 1.818184, -0.409091)` |
| diagonal3 | 4 | `(1, -1.789572, 1.956485, -0.672024)` |
| diagonal3 | 5 | `(1, -1.893090, 1.990206, -0.792609)` |

## Observed scaling

A power fit `error ~ L^-p` over `L=3,4,5` gives:

| observable | axial p | diagonal2 p | diagonal3 p |
|:--|--:|--:|--:|
| gauge leakage | exact-zero special axis | 2.292 | 2.238 |
| full FP matrix residual | 2.096 | 1.957 | 1.772 |
| FP-ratio error | 2.019 | 2.169 | 2.475 |

The principal result is that all nontrivial errors fall approximately as the expected leading lattice correction,

\[
\boxed{\epsilon\sim O(L^{-2})\sim O(k^2)}.
\]

This is materially stronger than the earlier TT-only positivity check because the full symmetric-tensor quadratic structure is being tested before any TT projection.

## Continuum extrapolation

A linear extrapolation of each fitted ratio in `1/L^2` gives:

- axial:
  \[
  (1,-2.000269,2.001154,-1.000645),
  \]
  relative distance to Fierz-Pauli = `4.27e-4`;
- diagonal2:
  \[
  (1,-2.031026,2.036439,-0.998326),
  \]
  relative distance = `1.51e-2`;
- diagonal3:
  \[
  (1,-2.159789,2.098729,-1.008771),
  \]
  relative distance = `5.95e-2`.

Only three sizes are used, so these intercepts are **diagnostics, not precision continuum estimates**.  The axial direction is also a special lattice direction: its exact Regge gauge subspace is already contained in the naive metric subspace at finite spacing.  The non-axial orientations are therefore essential falsifiers.

The orientation-to-orientation difference in the fitted coefficient vector also decreases approximately quadratically: diagonal2-vs-axial gives `p ~= 2.02`, diagonal3-vs-axial gives `p ~= 2.44`.  This is preliminary evidence that lattice rotational anisotropy is irrelevant in the same IR limit.

## What this closes, and what it does not

Supported by this scan:

1. The exact finite Regge gauge directions approach the 10-component metric subspace for generic low momenta.
2. The **unprojected** metric Hessian approaches the Fierz-Pauli two-derivative tensor structure.
3. The leading deviations are numerically consistent with `O(k^2)` lattice artefacts on the tested sizes.
4. Directional anisotropy decreases toward the IR on the tested orientations.

Not established:

1. cubic/nonlinear Ward closure;
2. the Einstein-Hilbert cubic vertex;
3. Lorentzian unitarity and a selected microscopic path-integral measure;
4. an explicit blocked effective action `S_eff[g]` and regulator-independent Wilson coefficients;
5. emergence of four dimensions without the 4D Regge scaffold;
6. a physical matter sector and anomaly cancellation;
7. experimental validation.

Therefore the correct statement is:

\[
\boxed{\text{quadratic Regge metric sector }\longrightarrow\text{ Fierz-Pauli is strongly supported on the tested finite lattices}}
\]

but

\[
\boxed{\text{binary microscopic theory }\Longrightarrow\text{ nonlinear continuum GR is still open}.}
\]

## Reproduction

```bash
python scripts/gravity_bridge_scaling.py --sizes 3 4 5 --output verification_results/gravity_bridge_scaling.json
```

The full three-orientation `L=3,4,5` scan is intentionally more expensive than the quick verifier because it evaluates numerical Regge Hessians repeatedly.
