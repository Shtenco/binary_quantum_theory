# BQG multi-block TT Wilson production status

Status: **downstream physical extractor closed; actual multi-block BQG science input still missing.**

This note records the exact state of the calculation

\[
C_{\rm BQG}\to C_{\rm eff}\to K_q\to K_h(\mathbf k)\to K_{TT}(\mathbf k)\to(c_1,\ldots,c_6)_{\rm BQG}^{IR}
\]

without introducing a new microscopic operator, clock, history postulate or fitted transfer coefficient.

## 1. What is now executable

`scripts/bqg_multiblock_tt_wilson_extractor.py` implements the frozen downstream chain:

1. accept an already-produced Hermitian collective multi-block BQG constraint matrix `C_full`;
2. define the supplied metric carrier `P` and its complement `Q`;
3. diagonalize `QCQ` and reject every zero/gapless `Q` mode that still couples to `P`;
4. on the remaining gapped range compute the zero-constraint-energy Schur/Feshbach operator

\[
\boxed{
C_{eff}=PCP-PCQ(QCQ)^{-1}QCP;
}
\]

5. form the normalized-state six-metric Hessian

\[
\boxed{K_q=2\,\operatorname{Re}C_{eff}-2C_{00}I;}
\]

6. transport each block through the independently measured metric map

\[
\boxed{K_h=M_{hq}^{-T}K_qM_{hq}^{-1};}
\]

7. require the center plus four neighbors to reproduce the frozen tetrahedral nearest-neighbor shell;
8. form the small-momentum Fourier/Taylor symbol from the actual center-neighbor blocks;
9. project to the deterministic two-polarization TT frame;
10. verify zero TT mass, positive common leading `k^2` residue, leading isotropy and reciprocal/parity-even transfer;
11. extract the complete six-dimensional parity-even tetrahedral quartic TT vector using the exact full-rank six-observable matrix already certified by `S4_TT_QUARTIC_COMPLETE_BASIS.md`;
12. emit

\[
\boxed{\mathbf c_{\rm BQG}^{IR}=(c_1,c_2,c_3,c_4,c_5,c_6)}
\]

**only** if every production/provenance/gap/geometry/IR/Wilson guard passes.

A failed or incomplete input returns `c_BQG_IR = null`; no coefficient is replaced by zero or inferred from an unrelated precursor.

## 2. Frozen metric map

The extractor uses the already measured L1 map from `scripts/collective_l1_coarse_flux_response_gate.py` unless an explicitly supplied production map is present.

In the metric coordinate convention

```text
h = (xx, yy, zz, sqrt(2)xy, sqrt(2)xz, sqrt(2)yz)
```

its exact reconstructed form is

\[
M_{hq}=\begin{pmatrix}
1/\sqrt{12}&0&0&0&0&1/\sqrt{12}\\
0&1/\sqrt{12}&0&0&1/\sqrt{12}&0\\
0&0&1/\sqrt{12}&1/\sqrt{12}&0&0\\
0&0&1/\sqrt6&-1/\sqrt6&0&0\\
0&1/\sqrt6&0&0&-1/\sqrt6&0\\
1/\sqrt6&0&0&0&0&-1/\sqrt6
\end{pmatrix},
\]

with

\[
\boxed{\operatorname{cond}(M_{hq})=\sqrt2}.
\]

No identity-coordinate substitution is permitted.

## 3. Exact production input contract

The science path accepts one NPZ with at minimum:

```text
C_full          full compressed Hermitian multi-block constraint matrix
p_indices       indices of the retained P metric carrier inside C_full
p_block         block id for every P vector
p_coord         metric q coordinate 0..5 for every P vector
block_positions one three-vector per sorted P block id
central_block   id of the central block
C00             retained background expectation entering normalized-state Hessian
metadata_json   provenance declaration
```

Optional:

```text
metric_map      production 6x6 M_hq, if a later frozen refinement map supersedes L1
```

The provenance declaration must state at least

```json
{
  "actual_bqg_operator": true,
  "synthetic": false,
  "operator_components": ["E", "S", "R_op"],
  "source_commit": "<exact commit>",
  "regulator": "<complete cutoff/support declaration>",
  "target_fitting_used": false
}
```

The current extractor deliberately accepts no free physical transfer coefficient.

## 4. Gapless-mode rule is fail-closed

If `QCQ` contains a numerically zero mode `u_0` with

\[
PCQ\,u_0\ne0,
\]

the calculation stops with

```text
GAPLESS_COUPLED_Q_MODE_REQUIRES_PROMOTION
```

because that mode belongs in the low-energy carrier. The code does not add `i eta`, a mass shift, denominator clipping or a fitted pseudoinverse.

Only exactly uncoupled zero modes may receive zero Moore-Penrose inverse on their null subspace.

## 5. Downstream known-answer test

The extractor contains a synthetic test solely to verify implementation. It is explicitly labelled

```text
INFRASTRUCTURE_SELFTEST_NOT_BQG_EVIDENCE
```

The test embeds a known five-block tetrahedral metric kernel into a larger P+Q Hermitian operator, performs the Schur reduction, transports it through the frozen nontrivial `M_hq`, reconstructs the momentum expansion, TT-projects it and recovers a precomputed six-Wilson vector.

Current local result:

```text
Schur relative error             0.0
leading k^2 isotropy defect      4.965248094601316e-16
TT mass defect                   3.3306690738754686e-16
six-Wilson fit defect            4.8669169352894896e-17
c-vector relative error          1.7845646559535552e-15
```

The known-answer vector is

\[
-\frac1{20}\,\mathbf c_{iso}+\frac1{18}\,\mathbf c_{Q4},
\]

and is recovered numerically as

```text
[-0.16666666666666669,
 -1.8333333333333302,
 -0.16666666666666674,
 -2.3333333333333335,
  0.75,
 -1.500000000000005]
```

This verifies the downstream algebra only. These numbers are **not** BQG Wilson coefficients.

## 6. Repository audit: why the real c-vector cannot yet be emitted

The existing frozen calculations do not yet supply the required physical five-block metric-carrier `C_full`.

### Local L1 depth-two result

`collective_l1_metric_edge_depth2_shard_collect.py` reconstructs the exact full-E response of one parent block,

\[
v_e=H_Bu_e,
\]

and its local `K/A/B` Krylov moments. Its own hard scope guard explicitly says that the local `E/T2` splitting is not `zeta4`; a momentum-dependent interblock effective kernel is still required.

### Multi-node Lorentzian environment result

`LORENTZIAN_MULTI_NODE_ENVIRONMENT_CORRELATION.md` reconstructs exact diagonal-environment dependence, but states explicitly that the historical workers did not calculate the off-diagonal environment blocks

\[
\langle e'|L|e\rangle,\qquad e'\ne e.
\]

It is therefore not the complete multi-node Hamiltonian needed here.

### Two-node logical route result

`two_node_lorentzian_route_logical_cross_gate.py` is an exact shared-route **4x4 logical ordering regression**. Its own scope states that it is not the full collective HDA/multi-block metric operator.

### Frozen collective Krylov protocol

`COLLECTIVE_KRYLOV_EFFECTIVE_BASIS.md` explicitly states that the first-refinement Euclidean rank result is only a prerequisite. The full production row still requires internal-link contraction plus full `E/S/R_op` depth-two closure on the target-independent complete boundary basis.

### Nearest-block S3 closure

The nearest-neighbor geometry is already fixed, but the physical shared-face Peter-Weyl transfer amplitudes themselves were not generated by the geometric transfer gate.

Therefore, as of this audit,

\[
\boxed{
\mathbf c_{\rm BQG}^{IR}=\text{NOT COMPUTED}
}
\]

—not zero, not unknown because of a missing formula, but blocked by one concrete missing **existing-operator amplitude calculation**.

## 7. The one remaining production calculation

No new theory is needed. The next producer must apply the already frozen `E+S+R_op` microscopic operators to the target-independent complete boundary/Krylov basis on a centered block and its four shared-face neighbors, then write the resulting compressed Hermitian matrix in the NPZ contract above.

The calculation must preserve:

- the complete boundary-face recoupling/multiplicity support already frozen by the collective Krylov protocol;
- exact source commit and cutoff/support provenance;
- no GR/TT/experimental target pruning;
- all coupled gapless modes rather than regularizing them away;
- one common block coordinate convention and the measured metric calibration.

Once that matrix exists, the remaining sequence

```text
actual C_full
 -> Q-gap audit
 -> exact zero-energy Schur complement
 -> normalized K_q
 -> measured M_hq
 -> K_h(k)
 -> TT projection
 -> c1..c6
```

is now executable without adding a new physical assumption.

## 8. Scientific claim discipline

The leading two-derivative physical TT form derived separately remains

\[
\Gamma_{TT}^{(2)}(\omega,\mathbf k)
=Z_T[-(\omega+i0)^2+k^2]I_2+O(\partial^4).
\]

This note does **not** claim the six `O(k^4)` coefficients have already been obtained. It freezes the exact calculation that will obtain them from the first valid actual multi-block BQG operator and makes it impossible for placeholders, reduced-propagator coefficients, local anisotropy diagnostics or synthetic controls to masquerade as that result.
