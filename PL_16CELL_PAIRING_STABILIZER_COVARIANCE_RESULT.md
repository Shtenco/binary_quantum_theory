# 16-cell pairing-stabilizer covariance result — finite regulator symmetry frontier

**Status:** direct exact sparse Peter-Weyl result. The order-8 structural pairing stabilizer exists, but the physical-sine Euclidean source column is not a pure pseudoscalar under the full group on the first 16-cell regulator.

This document records the result of the preregistered amplitude-level symmetry check. It does not alter the earlier V3 preregistration after seeing the data.

## 1. Proven structural subgroup

For the all-j=1/2, all-K=0 source state with local pairing `(01)(23)`, the exact line stabilizer is

\[
H\cong(S_2\times S_2)\rtimes S_2,
\qquad |H|=8.
\]

The structural gate passes:

- exact order 8;
- three free worker-index orbits of size 8;
- PL epsilon coefficient transforms by permutation parity;
- local K=0 line character is `+/-1`;
- the 16-node product seed has trivial total character.

The first serialization failure in the workflow was infrastructure-only and was fixed before the science verdict.

## 2. Exact global Peter-Weyl transport checks

The independent amplitude gate constructs the actual sparse spin-network action `U_h`, including oriented local intertwiner recoupling phases.

All non-amplitude prerequisites pass:

```text
H_order8                                      PASS
graph_neighbor_slot_covariance                PASS
coordinate permutations preserve edge order  PASS
edge maps bijective                           PASS
global K0 seed invariant                      PASS
local K-line recoupling exact                 PASS
E sparse support covariant                    PASS
E norm preserved                              PASS
```

Numerically,

\[
\max\Delta_{K\text{-line}}=4.44\times10^{-16},
\qquad
\max\Delta_{|phase|}=4.44\times10^{-16},
\]

and the E norm is

\[
\|E_0|\Omega\rangle\|=2.1442780425164956.
\]

Thus the failing observable is not graph transport, support, norm, seed covariance or recoupling completeness.

## 3. Full H pseudoscalar hypothesis fails at finite regulator

The tested hypothesis was

\[
U_h E_0|\Omega\rangle
\stackrel{?}{=}
\operatorname{sgn}(h)E_0|\Omega\rangle.
\]

The exact relative errors are

| h | parity | relative error |
|---|---:|---:|
| `(0,1,2,3)` | +1 | `5.091239918e-15` |
| `(0,1,3,2)` | -1 | `0.6692489278586203` |
| `(1,0,2,3)` | -1 | `5.109650077e-15` |
| `(1,0,3,2)` | +1 | `0.6692489278586203` |
| `(2,3,0,1)` | +1 | `0.4816961052956292` |
| `(2,3,1,0)` | -1 | `0.4816961052956292` |
| `(3,2,0,1)` | -1 | `0.4816961052956292` |
| `(3,2,1,0)` | +1 | `0.48169610529562906` |

Therefore

\[
\boxed{
E_0|\Omega\rangle
\text{ is not a one-dimensional sign representation of the full }H
}
\]

on this finite regulator.

This is a genuine finite-regulator symmetry result, not a floating-point failure: support is identical and norm is preserved in every row while the amplitude errors are order unity relative to numerical precision.

## 4. Exact surviving subgroup

Within the tested H elements, the exact pseudoscalar stabilizer of this source column is at least

\[
\boxed{H_E^{exact}=\{e,(01)\}\cong C_2,}
\]

where `(01)` denotes local slot permutation `(1,0,2,3)`.

Both elements satisfy the amplitude equation to about `5.1e-15` relative error.

No larger subgroup of the tested H can be promoted from this result because every remaining nonidentity H element individually fails the one-dimensional pseudoscalar equation.

## 5. Quantified symmetry-breaking power

Because `U_h` is norm preserving, for the target sign character

\[
\epsilon_h^2
=
\frac{\|U_hE-\chi(h)E\|^2}{\|E\|^2}
=
2-2\,\operatorname{Re}\frac{\langle\chi(h)E,U_hE\rangle}{\|E\|^2}.
\]

Averaging over H gives the norm-squared fraction of the sign-irrep projection:

\[
\boxed{
\frac{\|P_{sign}E\|^2}{\|E\|^2}
=0.8860054496057664.
}
\]

Hence the orthogonal finite-regulator symmetry-breaking power is

\[
\boxed{
1-0.8860054496057664
=0.1139945503942336.
}
\]

The corresponding orthogonal norm fraction is approximately

\[
\sqrt{0.1139945503942336}\simeq0.33763.
\]

This is a useful refinement observable: a fully restored pseudoscalar continuum regulator should drive the breaking power to zero.

## 6. Consequence for the V3 orbit reduction

The preregistered `24 -> 3` per-mode reconstruction in

`PL_16CELL_HERMITIAN_LORENTZIAN_PREREGISTRATION_V3_ORBIT.md`

requires full-H amplitude covariance before heavy Lorentzian terms may be reconstructed.

That prerequisite fails. Therefore

\[
\boxed{\text{V3 full-H 24->3 production reconstruction is BLOCKED.}}
\]

The workflow hard guard is functioning correctly; no 36-term reconstruction may be promoted from the full H theorem.

The V3 preregistration remains in the repository as an immutable record of the proposed test and its failure condition.

## 7. What can still be used safely

Two scientifically clean routes remain:

1. **Exact C2 reduction.** Use only the proven `e,(01)` subgroup. It pairs the 24 worker indices into 12 exact structural pairs. This can reduce production cost without assuming the failed larger symmetry, but the full K-K-V word must still receive direct held-out validation before reconstruction.
2. **Covariant-regulator derivation.** Derive a target-independent tetrahedrally covariant Euclidean regulator (for example by an operator-level group projection or an equivalent fully antisymmetrized regulator prescription), then rerun all affected E/HDA regressions before using the enlarged symmetry. This is an operator change and must not be introduced merely to improve a GR target.

The second route is potentially more fundamental because the measured breaking is itself an IR/refinement observable. It should be judged by symmetry/locality and held-out HDA/refinement tests, not by coefficient fitting.

## 8. Provenance

GitHub Actions run:

```text
31985744227
```

The science output was produced after both JSON `np.bool_` serialization issues had been removed. The amplitude step then returned `passed=false` from the actual numerical checks.

Key values:

```text
E_source0_support = 82
E_source0_norm = 2.1442780425164956
max_local_intertwiner_line_leakage = 4.440892098500626e-16
max_local_phase_modulus_defect = 4.440892098500626e-16
max_E_relative_covariance_error = 0.6692489278586203
max_E_norm_defect = 1.0658141036401503e-14
```

## 9. Scientific interpretation

This does **not** falsify the BCQG fixed-cutoff HDA architecture. It falsifies a stronger computational shortcut: the assumption that the first finite 16-cell Euclidean source column already transforms as the full order-8 pairing-stabilizer pseudoscalar.

For candidate-theory closure, the new observable is explicit:

\[
\boxed{
\Delta_{tetra,E}(\ell)
=1-\frac{\|P_{sign}E(\ell)\|^2}{\|E(\ell)\|^2}
\longrightarrow0
}
\]

must either be demonstrated under refinement or eliminated by a separately justified covariant regulator whose previous HDA/normalization results are then re-audited.
