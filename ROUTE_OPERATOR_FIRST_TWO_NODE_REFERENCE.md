# Two-node operator-first route — independent numerical reference

Status: **independent algebraic/numerical cross-check; not promoted to the canonical machine ledger until the repository CI gate completes**.

This note records an independent calculation of the exact two-node logical route block implemented in `scripts/operator_first_two_node_route_hda_gate.py` and the sparse-Fourier equivalent implemented in `scripts/operator_route_sparse_fourier.py`.

It is deliberately separated from canonical `tested_finite` evidence so that GitHub Actions remains the code-level source of truth.

---

## 1. Exact shared 4×4 geometry metric

For the same local route legs `(1,2)` used by the physical sine two-node habitat, the exact one-node logical flux block is

\[
Q^{00}=Q^{11}=\frac34 I,
\]

\[
Q^{01}=Q^{10}
=-\frac14I-\frac{\sqrt3}{4}X+\frac14Z.
\]

On the two-node geometry basis

```text
(K0,K1) = (0,0), (0,2), (2,0), (2,2)
```

the shared metric is

\[
Q_{shared}^{ab}
=\frac12(Q_0^{ab}\otimes I+I\otimes Q_1^{ab}).
\]

The off-diagonal geometry norm is

```text
0.8660254037844386
```

so this is genuinely operator-valued and does not collapse to the historical diagonal expectation metric.

---

## 2. Frozen carrier-8 regulator sequence

Using the same lapse family and WKB carrier as the physical sine two-node gate, the independent sparse-Fourier calculation gives for the initial `K0K0` state:

| epsilon | route defect |
|---:|---:|
| 1/4  | `1.3126605728879455e-5` |
| 1/8  | `6.563923939492644e-6` |
| 1/16 | `3.2820396179034527e-6` |
| 1/32 | `1.6410295154019502e-6` |
| 1/64 | `8.205159710207801e-7` |

with

\[
\boxed{p=0.9999594708960342}.
\]

This passes the already frozen repository acceptance window

```text
endpoint < 1e-6
0.99 < p < 1.01.
```

---

## 3. Logical-state robustness

At `epsilon=1/64`, carrier 8:

| two-node logical spinor | endpoint | epsilon exponent |
|:--|--:|--:|
| `K0K0` | `8.2051597102e-7` | `0.999959471` |
| `K0K2` | `1.3262764410e-6` | `0.999953922` |
| `K2K0` | `1.3262764410e-6` | `0.999953922` |
| `K2K2` | `1.4729647871e-6` | `0.999945807` |
| equal superposition | `1.5729464547e-6` | `0.999911102` |
| fixed phase spinor | `8.3840617074e-7` | `0.999958774` |
| fixed random spinor | `1.8685452300e-6` | `0.999947120` |

Every checked state satisfies the preregistered multi-state endpoint bound `<2e-6` and retains exponent approximately one.

A useful correction to the earlier one-node intuition follows: the two-node shared operator does **not** generically improve the finite defect by a factor near two. Its initial-state endpoint is instead close to the historical expectation-metric two-node route defect. The robust result is the scaling, not a claimed finite-coefficient improvement.

---

## 4. Carrier robustness

For `K0K0` at `epsilon=1/64`:

| carrier | endpoint | epsilon exponent |
|---:|---:|---:|
| 2  | `1.5961657598e-5` | `0.999926911` |
| 4  | `3.5017070289e-6` | `0.999950580` |
| 8  | `8.2051597102e-7` | `0.999959471` |
| 16 | `2.0070079915e-7` | `0.999963094` |

Thus the finite error decreases strongly with carrier while the regulator exponent remains essentially one.

---

## 5. Sparse Fourier versus 48×48 FFT

An independent 48×48 spectral-grid implementation was evaluated on the same `K0K0`, carrier-8 sequence.

Maximum relative difference between the sparse-Fourier and FFT route defects:

\[
\boxed{5.74\times10^{-8}}.
\]

The fitted exponents are

```text
sparse Fourier: 0.9999594708960342
48x48 FFT:      0.9999594477002136.
```

The repository equivalence gate freezes the acceptance criterion

```text
max relative difference < 1e-7.
```

The independent reference therefore satisfies that criterion.

---

## 6. Interpretation

This reference supports two design decisions already encoded in the branch:

1. the production route normal should remain **operator-first**;
2. the exact sparse-Fourier engine can replace the 48×48 FFT for the frozen finite-harmonic lapse / plane-wave probe family, reducing the route cost dramatically before the full spin-changing `G × R_op` calculation.

It does **not** upgrade `ROUTE_OP_2NODE` to canonical `tested_finite` by itself. That status change is reserved for the corresponding GitHub Actions evidence.
