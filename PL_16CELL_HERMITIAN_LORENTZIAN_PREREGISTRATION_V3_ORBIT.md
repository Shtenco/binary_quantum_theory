# Exact 16-cell PL-S3 Hermitian Lorentzian V3 — pairing-stabilizer orbit reduction

## Status and reason for V3

This preregistration is written **before any complete corrected tetrahedral-volume PL Lorentzian science column has been obtained**.

V2 changed the charged/intermediate volume for a target-independent tetrahedral-covariance reason and kept the brute-force requirement of 24 forward + 24 direct-adjoint ordered terms. Its distributed run was cancelled before a complete science result because the exact charged-sector workers were too expensive.

V3 changes **no physical operator, sign, cutoff, zero rule, scalar projection, Hermitian completion, or science threshold**. It replaces redundant direct evaluation inside exact symmetry orbits by a proved unitary transport, guarded by direct held-out V2 terms computed before reconstruction.

The physical definitions remain

\[
Q_{tet}=\frac14\sum_{r=0}^3(-1)^r q_{\widehat r},
\qquad V_{tet}=\sqrt{|Q_{tet}|},
\]

\[
E=H_E^{sine},\qquad K=[V_{tet},E],
\]

\[
L_{raw}=\sum_{s=0}^{23}\eta_s W_s,
\qquad
S=-\frac i2(L_{raw}-L_{raw}^\dagger),
\]

with `Jmax2=7` and all V2 acceptance thresholds unchanged.

## 1. Exact stabilizer group

The all-j=1/2, K=0 local intertwiner line uses the pairing `(01)(23)`. Its slot-permutation stabilizer is

\[
H\cong(S_2\times S_2)\rtimes S_2,
\qquad |H|=8.
\]

The 24 ordered Lorentzian slot words split into exactly three free H-orbits:

```text
O0 = [0,1,6,7,16,17,22,23]
O1 = [2,4,8,10,13,15,19,21]
O2 = [3,5,9,11,12,14,18,20]
```

The local K=0 seed transforms by a one-dimensional character `chi(h)=+/-1`. On the homogeneous 16-node product seed,

\[
\chi(h)^{16}=1,
\]

so the global source state is invariant under every `h in H`.

## 2. Operator covariance theorem

Under a local slot permutation `h`, the tetrahedral oriented grasping is a pseudoscalar,

\[
U_hQ_{tet}U_h^{-1}=sgn(h)Q_{tet},
\]

while the absolute volume is invariant,

\[
U_hV_{tet}U_h^{-1}=V_{tet}.
\]

The physical-sine Euclidean tetrahedral epsilon contraction is a pseudoscalar,

\[
U_hEU_h^{-1}=sgn(h)E,
\]

and hence

\[
U_hKU_h^{-1}=sgn(h)K.
\]

Every unweighted Lorentzian ordered word contains two K legs and one V leg. Therefore the two signs cancel:

\[
\boxed{U_hW_sU_h^{-1}=W_{h\cdot s}.}
\]

The exact same covariance holds for the direct-adjoint ordered word.

The PL epsilon coefficient obeys, for the worker indexing convention,

\[
\boxed{\eta_{h\cdot s}=sgn(h)\eta_s.}
\]

This relation is checked exhaustively over all 24 worker indices and all eight elements of H by `lorentzian_pairing_stabilizer_orbit_gate.py`.

Since the global seed is H-invariant,

\[
W_{h\cdot s}|\Omega\rangle
=U_hW_s|\Omega\rangle,
\]

and the complete weighted contribution of one orbit is exactly

\[
\boxed{
\sum_{h\in H}\eta_{h\cdot s}W_{h\cdot s}|\Omega\rangle
=
\eta_s\sum_{h\in H}sgn(h)U_hW_s|\Omega\rangle.
}
\]

Thus the full 24-term forward or adjoint sum is determined by three representatives, one per free orbit.

## 3. Direct held-out implementation guard

The theorem is not allowed to replace heavy workers merely from abstract slot algebra. The exact oriented Peter-Weyl state transport `U_h` must be validated on direct corrected V2 Lorentzian terms.

To maximize cache reuse, the direct set is frozen as two six-term shards:

### Forward shard

Use `mode=forward`, `first-slot=3`, which computes

```text
[0,2,6,8,12,14]
```

and therefore supplies one direct pair in every orbit:

```text
O0: (0,6)
O1: (2,8)
O2: (12,14)
```

### Adjoint shard

Use `mode=adjoint`, `first-slot=1`, which computes

```text
[0,1,14,15,20,21]
```

and supplies

```text
O0: (0,1)
O1: (15,21)
O2: (14,20)
```

For every pair `(representative, heldout)`, find the unique `h in H` mapping the representative worker slot tuple to the held-out tuple. Require simultaneously:

```text
exact sparse support equality
relative amplitude error < 1e-8
direct representative worker passed
direct held-out worker passed
same V2 operator provenance
```

All six pair checks must pass before any missing term is reconstructed.

## 4. Reconstruction rule

After the six pair checks pass, each missing term in the same orbit is generated only by the exact oriented Peter-Weyl unitary transport

\[
|T_j\rangle=U_h|T_s\rangle,
\qquad h\cdot s=j.
\]

The target worker metadata (`omit`, ordered local slots, target nodes and `PL_epsilon_coefficient`) is recomputed independently from the canonical `ordered_spec`, not copied from the representative.

Leakage/scalar-closure diagnostics may be inherited from the representative only because exact unitary covariance makes the corresponding norms invariant. Reconstructed metadata must explicitly record its representative index and transport permutation.

No amplitude may be scaled, fitted, thresholded or sign-flipped beyond the exact `U_h` action and the independently recomputed PL epsilon coefficient used later by the collector.

## 5. Final collector

The reconstruction stage must materialize a complete unique set

```text
24 forward JSON/NPZ terms
24 adjoint JSON/NPZ terms
```

so the existing V2 amplitude reduction can still check the complete worker-index orbit and form

\[
S=-\frac i2(L_{raw}-L_{raw}^\dagger).
\]

The V3 wrapper must additionally require:

```text
12 direct corrected-V2 terms
36 symmetry-reconstructed terms
6/6 held-out covariance pairs passed
all 48 metadata operator_version == tetrahedral-charged-volume-v2
```

The final science result must be labelled `AMPLITUDE_PRECURSOR_S_NODE0_V3_ORBIT_EXACT`, not as a 48-direct-worker result.

## 6. V2 science thresholds retained exactly

No V2 threshold changes:

- source node 0;
- all-j=1/2, all-K=0 16-cell seed;
- one-L `j<=7/2` wall;
- exact-zero ordered terms allowed;
- physical complete-basis/internal-volume leakage `<1e-8`;
- scalar closure `>1-1e-10` unless exact zero;
- nonscalar rejected norm `<1e-8`;
- no lower bound on `||S||`;
- Hermitian completion exactly `S=-i(L-Ldagger)/2`.

## 7. Failure policy

- Any one of the six direct pair validations fails -> **V3 ORBIT REDUCTION FAILS**. Do not reconstruct the remaining terms; return to direct evaluation or identify the broken covariance assumption.
- Structural H gate fails -> no orbit reduction.
- E-level exact Peter-Weyl transport gate fails -> no orbit reduction.
- A reconstructed complete collector fails a V2 science threshold -> physics/infrastructure failure according to the original V2 semantics; do not alter orbit representatives or tolerances.
- A V3 failure may not be repaired by choosing a different subgroup after inspecting Lorentzian amplitudes.

## 8. Computational consequence

The first exact validation run evaluates **12 heavy corrected terms instead of 48** while still directly testing every one of the three symmetry orbits in both forward and adjoint modes. After the theorem and held-out implementation checks are frozen, future identical-habitat regressions need only the six orbit representatives.

This is a symmetry reduction, not a model approximation.
