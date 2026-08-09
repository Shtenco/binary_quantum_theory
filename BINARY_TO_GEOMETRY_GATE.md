# Binary -> geometry gate: dimension-blind null-model test

Status: **negative structural result for the minimal binary reconvergent rule; not a test of a frozen full CIMFIG rule set**.

## Why this calculation is needed

The current repository has a strong finite-lattice `Regge -> GR` chain, but the larger derivation still starts too late: the 4D Regge scaffold is supplied before the gravity tests begin.  The missing object is a concrete coordinate-free microscopic rule table whose generated ensemble can be tested for emergent dimension.

The existing `scripts/eml_blitz.py` is only a storage/description-size estimate for an Edge--Message--Law primitive and explicitly reports `physics_derived: false`.  It does not define a physical rewrite dynamics.

Before inventing a complicated rule set, this file tests the least-structured causal possibility compatible with binary competing histories and reconvergence.

## Dimension-blind calibration

`scripts/dimension_emergence_gate.py` first checks its heat-kernel spectral-dimension estimator on periodic lattices of known dimensions.  The target dimension is not passed to the estimator.

Using the common diffusion window `t=5..10`:

| control | measured spectral dimension |
|:--|--:|
| 1D torus | 1.01942 |
| 2D torus | 2.03883 |
| 3D torus | 3.05825 |
| 4D torus | 4.07763 |

The common relative lattice bias is about 1.9%, so the estimator is not preferentially returning four.

## Minimal binary causal diamond

Start from one causal link.  At every generation replace every link by two alternative two-step paths which reconverge:

```text
u ---- v

becomes

u -- a -- v
 \      /
  - b --
```

No coordinates, metric, target dimension, TT projector or Regge simplex is used.

For generation `g`, graph distance between the original boundary vertices doubles.  Direct graph construction gives:

| generation | vertices | diameter | step effective volume dimension |
|--:|--:|--:|--:|
| 2 | 12 | 4 | -- |
| 3 | 44 | 8 | 1.87447 |
| 4 | 172 | 16 | 1.96683 |
| 5 | 684 | 32 | 1.99159 |

Thus

\[
\boxed{d_H\to2}
\]

for this minimal reconvergent binary geometry.

The complete normalized-Laplacian spectrum of generation 5 gives a heat-kernel plateau over `t=6..12`

\[
\boxed{d_s=2.06975\pm0.01814}.
\]

Therefore the minimal binary reconvergence rule fails the four-dimensional gate decisively:

\[
\boxed{\text{binary branching + causal reconvergence}\not\Rightarrow d=4.}
\]

This is a useful falsification because it prevents the words *binary*, *diamond* or *causal confluence* from being mistaken for a derivation of spacetime dimension.

## Finite internal frame states cannot repair this by themselves

There is a second structural point.  Suppose each causal site or link is decorated by a finite internal fibre `F` (frame qubits, a finite group label, messages, etc.) of uniformly bounded size and diameter, while the large-scale causal connectivity remains the same.

For graph balls, multiplication by a bounded finite fibre changes volume only by bounded factors and bounded radius shifts:

\[
c_1|F|V_G(r-C)\le V_{G\times F}(r)\le c_2|F|V_G(r+C).
\]

Hence the logarithmic growth exponent is unchanged:

\[
\boxed{d_H(G\times F)=d_H(G)}.
\]

For a product-type Laplacian, the heat trace factorises.  After the finite fibre has mixed, its non-zero internal modes are gapped and contribute only exponentially decaying factors, leaving the same infrared power law of the base graph.  Therefore

\[
\boxed{d_s(G\times F)=d_s(G)}
\]

in the IR unless the internal sector itself becomes gapless with system size or feeds back into the connectivity.

So adding frame qubits to the two-dimensional causal diamond **without changing the rewrite geometry cannot create four dimensions**.

## Consequence for the microscopic theory

The missing mechanism must modify causal connectivity dynamically.  A viable frozen rule set must therefore make the geometry itself state-dependent, for example through local split/merge/reconnection operations whose probabilities or amplitudes depend on gauge-invariant local data.  The four-dimensional result must then be measured after the rule is frozen, not encoded through a chosen coordination number, simplex dimension, number of branches or target spectral dimension.

The next admissible test is therefore:

1. specify one finite local rewrite table with no dimensional parameter;
2. freeze it before the large-size run;
3. generate independent causal/frame ensembles;
4. measure `d_H`, `d_s` and diffusion exponent without coordinates;
5. reject the rule if no common 4D scaling window appears;
6. only if it passes, reconstruct coarse metric/connection fields and run the already-established Fierz--Pauli / cubic-EH / Ward gates.

The principal open arrow remains

\[
\boxed{\text{frozen binary causal/frame rule}\dashrightarrow\text{4D Regge/metric phase}.}
\]

## Reproduction

```bash
python scripts/dimension_emergence_gate.py \
  --max-generation 5 \
  --output verification_results/dimension_emergence_gate.json
```
