# Exact six-channel coarse-boundary tangent theorem at L1

This note records the first dynamical contraction of the canonical 24-chamber barycentric tetra block through all 36 internal dual links.

It is deliberately narrower than the final production `W_block`: the theorem uses the **strict-interior q=4 / vacuum-exterior channel** so that the block/environment split is exact by support before any amplitude is inspected.

## 1. Strict-interior channel

For every one of the 24 fine chambers `u` in a canonical coarse tetrahedron there are six oriented Euclidean specs with dual-plaquette length `q=4`.

Exactly one of those six has both

1. the complete q=4 curvature plaquette inside the same coarse block, and
2. the double-hit source link inside the same coarse block.

Thus this single oriented spec touches no exterior node and no coarse-boundary link.  After the exactly-four-spin-change projector `P4`, the exterior is **exactly** the homogeneous background by representation labels, not approximately so.

The physical-sine amplitude of that strict spec contains

```text
20 microscopic Gauss states per source chamber
24 source chambers
480 state occurrences
192 distinct block restrictions
```

with every coarse-boundary link still carrying `j=1/2`.

## 2. Exact internal-link contraction

For each microscopic block restriction, use its actual internal edge spins and fine-node intertwiners and contract the 36 internal dual links with the frozen SU(2) epsilon orientation convention.  The 24 boundary magnetic indices are left open.

The raw boundary tensor has dimension `2^24`, so it is not materialized.  Its inner products are computed as an equivalent closed double-layer tensor network.  At every fine node the shared boundary magnetic index is contracted between bra and ket and the three bra/ket internal legs are fused.  Contracting the resulting 24 rank-three transfer tensors gives exactly

\[
K_{ab}=\langle B_a|B_b\rangle .
\]

Because the complete six-link face recoupling map is unitary, this Gram is identical in the full recoupled boundary basis.

## 3. Chamber Gram and six coarse-edge cosets

Let `b_u` be the strict-channel boundary amplitude vector sourced by fine chamber `u`.  Label the 24 chambers by permutations `p in S4` in the canonical barycentric order and rephase them by permutation parity,

\[
\widetilde b_p = \operatorname{sgn}(p)b_p .
\]

The exact numerical contraction reveals a much stronger structure than a generic rank calculation.  Define the chamber class by the unordered pair

\[
e(p)=\{p_1,p_2\}.
\]

There are exactly six such classes, each containing four permutations.  They are naturally the six edges of the coarse tetrahedron.

The rephased Gram has only two overlaps:

\[
\frac{\langle\widetilde b_p|\widetilde b_q\rangle}{d}
=
\begin{cases}
1,&e(p)=e(q),\\
r,&e(p)\neq e(q),
\end{cases}
\]

with the direct contraction values

```text
d = 3.137686859428218e-10
r = 0.8523308467411363
```

and relative block-structure defect

```text
4.084649355260909e-16
```

(the maximum same-class and different-class normalized entry defects are both below `9e-16`).

Therefore, up to the diagonal parity rephasing,

\[
G=d\left[(1-r)\operatorname{diag}(J_4,J_4,J_4,J_4,J_4,J_4)+rJ_{24}\right].
\]

This is an algebraic rank statement.  The nonzero spectrum is

\[
\lambda_{0}=4d(1+5r)
=6.603769339181267\times10^{-9},
\]

and

\[
\lambda_{shape}=4d(1-r)
=1.8533582468929123\times10^{-10}
\]

with multiplicity five.  The remaining 18 eigenvalues are **exactly zero in the block model**; their direct double-precision eigensolver values fluctuate around zero at the `1e-25` roundoff scale.

Hence

\[
\boxed{\operatorname{rank}\{b_u\}_{u=1}^{24}=6}.
\]

## 4. Interpretation

The static maximal-symmetric block had a rank-one image.  Production Euclidean dynamics first expands the fine-Hilbert tangent span to rank 24, and exact internal-link contraction then organizes those 24 chamber directions into six coarse-edge-labelled boundary channels.

The homogeneous strict channel further decomposes as

\[
6=1+5,
\]

one uniform direction plus five degenerate orthogonal shape directions.

This is precisely the dimension expected for a symmetric three-dimensional metric tensor, and the six labels are geometrically the six edges of a tetrahedron.  **That dimensional match is a structural precursor, not yet a GR claim.**  No `D=3`, DeWitt `c=1/2`, physical TT count, or target constraint rank was used to construct or select the six channels.

## 5. What remains before the GR killer can consume the result

The production `W_block` still has to include, without target tuning:

1. the q=4 sectors that cross the coarse boundary, using an extended-Hilbert / edge-mode environment label rather than deleting exterior excitations;
2. the full one-E support, including q=6 and q=8 sectors where needed after exact support compression;
3. the Hermitian Lorentzian `S` image through the preregistered `j_face<=6` wall;
4. the spin-preserving operator-first route image;
5. all depth-two histories inside the exact `j_face<=9` HDA wall;
6. amplitude SVD and leakage of the complete target-independent image;
7. only then the raw 6x6 kinetic Hessian, DeWitt extractor, sequential constraint-rank SVD and collective `[H,H]` residual.

The current theorem is therefore a major positive bridge from microscopic dynamics to a six-dimensional coarse geometric tangent carrier, while the collective GR-universality verdict remains `INCOMPLETE`.
