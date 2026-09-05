# Peter–Weyl Lorentzian middle-prefix result

Status: **measured microscopic partial result for the preregistered first logical input. Six of twelve ordered middle-prefix classes are pathwise zero; six remain open.**

This note records data from `physical-scalar-kernel-dynamics-sharded` run `33962645194` at frozen source node `v=0`, logical input index `0` (all local `K=0`), sine-Hermitian Euclidean ordering and `Jmax=7/2`.

The frozen ordered Lorentzian term is

\[
T_{abc}=\operatorname{Tr}_{aux}[C_a(K)C_b(K)C_c(V)],
\qquad K=[V,H_E^{sine}].
\]

For fixed ordered pair `(b,c)`, the state after the first two right-to-left actions,

\[
\boxed{\Xi_{bc}^{ijk}=C_b(K)_{jk}\,C_c(V)_{ki}|\psi_0\rangle},
\]

is independent of the outer edge `a`.  Hence if all eight auxiliary-path states `Xi_bc^{ijk}` vanish, both full triples sharing that `(b,c)` prefix vanish before `C_a(K)` is evaluated.

## 1. Six prefix classes already closed

The completed one-term artifacts occur in exact outer-edge pairs.  In each row the two independent full-term jobs produced identical `C(V)` support histories and zero middle-`C(K)` support on every one of the eight auxiliary paths.

| middle prefix `(b,c)` | completed full terms `(a,b,c)` | `C(V)` support over 8 paths | middle `C(K)` support over 8 paths | result |
|---|---|---|---|---|
| `(3,4)` | `(2,3,4)`, `(1,3,4)` | `0,0,0,0,0,0,0,0` | `0,0,0,0,0,0,0,0` | prefix zero |
| `(2,4)` | `(3,2,4)`, `(1,2,4)` | `0,0,0,0,0,0,0,0` | `0,0,0,0,0,0,0,0` | prefix zero |
| `(1,4)` | `(3,1,4)`, `(2,1,4)` | `0,0,0,0,0,0,0,0` | `0,0,0,0,0,0,0,0` | prefix zero |
| `(4,3)` | `(2,4,3)`, `(1,4,3)` | `2,1,2,1,1,2,1,2` | `0,0,0,0,0,0,0,0` | prefix zero after nonzero `C(V)` |
| `(4,2)` | `(3,4,2)`, `(1,4,2)` | `5,3,5,3,3,5,3,5` | `0,0,0,0,0,0,0,0` | prefix zero after nonzero `C(V)` |
| `(4,1)` | `(3,4,1)`, `(2,4,1)` | `5,3,5,3,3,5,3,5` | `0,0,0,0,0,0,0,0` | prefix zero after nonzero `C(V)` |

Thus twelve of the twenty-four preregistered ordered triples are already known to vanish for this input for a reason stronger than epsilon cancellation:

\[
\boxed{C_b(K)C_c(V)|\psi_0\rangle=0}
\]

path-by-path for the six ordered prefixes above.

The three classes with `b=4` are particularly useful controls because `C_c(V)` is manifestly nonzero before the middle `C_4(K)` annihilates the state.  The observed zero is therefore not merely the trivial statement that the first volume commutator vanished.

Numerical complete-basis leakage in the completed artifacts is at the floating-point floor (typically `~1e-16`) and below the frozen `1e-9` integrity thresholds.

## 2. Six prefix classes still open

The only remaining ordered pairs are

\[
\boxed{(1,2),(2,1),(1,3),(3,1),(2,3),(3,2).}
\]

They contain no edge `4` and correspond exactly to the twelve long-running full-term jobs in run `33962645194`.

A dedicated exact gate now computes only the eight middle states `Xi_bc^{ijk}` for these six prefixes and serializes any nonzero middle states for continuation.  This removes duplicated outer-edge work without changing the frozen operator.

## 3. Decision rule

If all six remaining prefixes are also pathwise zero, then every one of the 24 ordered triples is zero before its outer `C_a(K)` action, and therefore

\[
H_L^{raw}|\psi_0\rangle=0
\]

for this first logical input at the declared cutoff and ordering.  The scientific status would still be only

`FIRST_LOGICAL_COLUMN_ZERO_NO_GLOBAL_CONCLUSION`,

because the remaining 31 logical input columns would not yet have been evaluated.

If any remaining prefix is nonzero, only the two outer-edge continuations associated with that prefix need to be computed.  Prefixes already proven zero must not be recomputed.

## 4. Claim boundary

This is a finite Peter–Weyl selection-rule result for one boundary input.  It is not a physical projector, not a pole of `Gamma_scalar`, and not evidence for or against dark matter or dark energy.  Its purpose is to finish the microscopic `H_E+(1+beta^2)H_L` data packet with exact fail-closed computation rather than brute-force duplication.
