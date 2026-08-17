# Preregistration: first internal Peter-Weyl anisotropy RG step

Status: **frozen before assembling the j=1 higher-shell Lambda**.

This document fixes the first nontrivial internal coarse-graining test after the recursive-PL geometry-only no-flow control.

## 1. Fine datum already open

The completed all-edge `j=1/2` higher-shell calculation gives the S4-reduced pair kernel

\[
K_{1/2}
=c_0II+J_{shape}(XX+ZZ)+J_{orient}YY
\]

and

\[
\boxed{R_{1/2}=\frac{J_{orient}-J_{shape}}{c_0}=0.0897532661805313.}
\]

This value is already open and is not fitted in the present test.

## 2. Why geometry-only blocking is excluded

`PL_GALERKIN_ANISOTROPY_NO_FLOW.md` proves for the canonical barycentric P0 control

\[
P^TL_{g+1}P=\frac14L_g
\]

and, for a separable internal kernel,

\[
R'_{aniso}=R_{aniso}.
\]

Therefore a nonzero beta function must come from internal/non-separable dynamics rather than spatial averaging alone.

## 3. Coarse carrier fixed before the result

Two fine spin-`1/2` face carriers are combined in the symmetric SU(2) channel

\[
\frac12\otimes\frac12\supset1.
\]

The four-face `j=1` gauge-singlet space has K-basis

```text
K = 0,2,4          # doubled-spin convention
```

and the exact tetrahedral permutation representation decomposes as

\[
\boxed{\mathcal H_{j=1}^{singlet}=[4]\oplus[2,2].}
\]

The microscopic `j=1/2` logical qubit is itself the unique `[2,2]` irrep. Because the coarse `[2,2]` occurs with multiplicity one, symmetry fixes the coarse logical projector uniquely.

The frozen phase convention is

\[
|0\rangle_c=|K=2\rangle,
\]

\[
|1\rangle_c=\frac{2|K=0\rangle-\sqrt5|K=4\rangle}{3}.
\]

No projector may be changed after the j=1 higher-shell result is opened.

## 4. Frozen dynamics

Use exactly the same Euclidean sine ordering as the completed fine calculation:

```text
H = H_E,0 + H_E,1
H_E = (T-T^dagger)/(2i)
```

with all ten K5 edges initialized at `j=1` and the same zero-aware Peter-Weyl/volume implementation.

For each of the 32 product logical basis states compute

\[
a_i=H|i\rangle,
\qquad
b_i=H^2|i\rangle.
\]

Then

\[
K_{ij}=\langle a_i|a_j\rangle,
\]

\[
H^{(4)}_{ij}=\langle b_i|b_j\rangle,
\]

\[
M=H^{(4)}-K^2,
\]

and, if `K` is full rank,

\[
\boxed{\Lambda_1=K^{-1/2}MK^{-1/2}.}
\]

No energy denominator or external physical datum is introduced.

## 5. Frozen observable

Trace the three environment logical qubits exactly as in the fine calculation and apply the same diagonal tetrahedral `S4` reduction. Write

\[
\Lambda_{1,pair}^{S4}
=c_0^{(1)}II+J_{shape}^{(1)}(XX+ZZ)+J_{orient}^{(1)}YY.
\]

The sole preregistered internal anisotropy observable is

\[
\boxed{R_1=\frac{J_{orient}^{(1)}-J_{shape}^{(1)}}{c_0^{(1)}}.}
\]

Report, without refitting,

\[
\Delta R=R_1-R_{1/2}
\]

and

\[
R_1/R_{1/2}.
\]

No `dR/dlog(b)` is allowed yet: the representation step `j=1/2 -> 1` has not been assigned an arbitrary spatial scale factor. The beta function per physical blocking scale is defined only after this carrier is embedded into the common recursive PL block.

## 6. Outcomes fixed in advance

### Restoration tendency

```text
|R_1| < |R_1/2|
```

This is evidence that the first internal representation step suppresses the symmetry-allowed anisotropy. It is **not** yet proof that `R -> 0` in the IR.

### Relevant-anisotropy tendency

```text
|R_1| > |R_1/2|
```

This is evidence that the first internal representation step enhances the anisotropy. It does not yet prove a nonzero fixed point.

### Sign-changing / nonmonotone tendency

```text
R_1 * R_1/2 < 0
```

This is reported as a sign change, not massaged into either restoration or relevance. Higher representation levels are then mandatory.

### Carrier failure

The step fails in its declared form if any of the following occurs:

- first-order spin-parity projection is nonzero beyond numerical tolerance;
- the 32-state coarse logical basis is not orthonormal;
- `K` loses rank in the selected coarse carrier;
- `M` or `Lambda` violates the positive block-Lanczos requirement beyond the frozen numerical tolerance;
- the result depends on changing the S4 projector or phase convention after inspection.

A failure here does not retroactively invalidate the fine `j=1/2` higher-shell or the fixed-cutoff HDA results; it invalidates this proposed first internal RG carrier.

## 7. Relation to the physical TT prediction

The logical quantity `R_aniso` is **not** identified by fiat with the spatial cubic coefficient `zeta4`.

The required remaining bridge is

```text
R_1/2 -> R_1 -> higher representation steps
      + recursive spatial PL blocking
      -> K_TT(omega,k;b)
      -> eta2_iso(b), zeta4_cub(b)
      -> eta2_IR, zeta4_IR.
```

Only after that map is derived can the project freeze its first external modified-dispersion prediction.

## Reproduction paths

Symmetry carrier:

```bash
python scripts/peter_weyl_j1_s4_block_gate.py \
  --output verification_results/PETER_WEYL_J1_S4_BLOCK.json
```

Column calculation:

```bash
python scripts/peter_weyl_j1_higher_shell_lambda_gate.py \
  --column 0 \
  --output verification_results/j1_columns/column_0.json
```

Assembly after all 32 columns:

```bash
python scripts/peter_weyl_j1_higher_shell_lambda_gate.py \
  --assemble-dir verification_results/j1_columns \
  --output verification_results/PETER_WEYL_J1_HIGHER_SHELL_LAMBDA.json
```
