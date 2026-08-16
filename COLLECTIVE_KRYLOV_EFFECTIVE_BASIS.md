# Collective effective basis: target-independent depth-2 operator image

This file freezes the compression rule required to turn the finite support walls into a practical direct collective BCQG calculation without inserting GR information into the basis.

## Why support alone is not the basis

The exact one-S support contains `121` unique hit tuples on a coarse face and reaches `j=0,1/2,...,6`. Expanding every reachable microscopic spin sector with every multiplicity channel would create an enormous direct sum and is not the physical image of the production operator.

Conversely, retaining only the static maximal-symmetric `j=3` channel is forbidden: the exact one-E and one-S support gates prove that it is not dynamically closed.

## Frozen carrier wall

For one production action:

\[
j_{face}\le 6.
\]

For the two actions required by the Hamiltonian commutator:

\[
\boxed{j_{face}^{(d=2)}\le9}.
\]

The depth-2 wall is exact and target-independent: `121` one-S hit tuples produce `4447` unique pair-sum hit tuples with doubled-spin support `0..18`. Route is spin-preserving and E has smaller support, so the SxS wall contains every E/S/R depth-2 term.

## First-refinement Euclidean rank theorem

The static all-j=1/2 block projected to maximal symmetric j=3 has rank-one image, but that obstruction is not dynamically stable.

On the first barycentric refinement, one coarse tetrahedron contains 24 fine chambers.  Let

\[
c_u=E_u^{sine}|\Omega_{L1}\rangle,
\]

for those 24 source chambers.  Every chamber has six q=4, four q=6 and two q=8 oriented plaquette specs.

Define `P4` as the exact projector onto final Gauss-basis states with exactly four microscopic spin labels changed from the all-j=1/2 seed.  Because every plaquette edge receives one fundamental hit, q=6 and q=8 terms necessarily change at least six or eight plaquette-edge spin labels.  Therefore `P4` isolates the q=4 curvature sector exactly.

The direct q=4 amplitude calculation gives

\[
\operatorname{rank}\{P_4c_u\}_{u=1}^{24}=24.
\]

Since a projector cannot increase rank,

\[
24\le\operatorname{rank}\{c_u\}\le24,
\]

hence

\[
\boxed{\operatorname{rank}\{E_u^{sine}|\Omega_{L1}\rangle\}=24}.
\]

The local exact calculation has projected Gram minimum eigenvalue `0.8436999771224867`, minimum singular value `0.9185314241344641`, 60 projected states per source, and 12 support states unique to every source chamber.  `COLLECTIVE_L1_E_Q4_RANK_THEOREM.md` records the proof and the distributed reproduction workflow.

This is a **fine-Hilbert tangent rank**, not a GR constraint rank and not a count of physical metric modes.

## Complete boundary-face recoupling

The coarse boundary isometry must not repeat the static maximal-j truncation.  Each coarse triangular face has six fine boundary links.  The canonical production basis therefore uses the complete unitary sequential SU(2) coupling tree

\[
(((((j_1j_2)J_{12}j_3)J_{123}j_4)J_{1234}j_5)J_{12345}j_6)J,M,
\]

retaining the intermediate multiplicity labels as well as total `J,M`.

For the q=4 one-E boundary sectors, the ordered fine-spin patterns are the all-j=1/2 baseline and every pattern with two links changed to doubled spin 0 or 2.  The complete recoupling map is unitary on all of them; the total coarse-face support is `J2=0,2,4,6,8`.  The historical fully symmetric `j=3` Dicke isometry is exactly the `J2=6` maximal-J subblock of this complete basis, not a competing construction.

Thus the next `W_block` stage is an internal-link contraction expressed in this complete boundary basis, followed by amplitude SVD.  No face irrep or multiplicity channel may be removed using GR target information.

## Production basis

Let `|Omega_l>` be the declared homogeneous/nondegenerate block background at refinement level `l`. Let `O_a` range over the frozen local/smeared production components of

\[
E,\qquad S,\qquad R_{op}.
\]

Construct boundary amplitude vectors for all target-independent histories of depth at most two,

\[
\mathcal K_l^{(2)}=\operatorname{span}\{\,|\Omega_l\rangle,\ O_a|\Omega_l\rangle,\ O_bO_a|\Omega_l\rangle\,\},
\]

inside the exact `j_face<=9` wall. Histories are deduplicated only after their actual complex boundary amplitudes are known.

Stack the amplitude vectors as columns of `A_l`. Define `W_l` from the left singular vectors of `A_l` using the globally frozen relative threshold

```text
sigma_i / sigma_max > 1e-10
```

and publish **all** singular values. This SVD is numerical linear-dependence removal only; no vector may be retained or discarded using `D=3`, `c=1/2`, GR constraint ranks, TT count or HDA residual.

## Operator-first compression

For every generator,

\[
C_A^{eff}=W_l^\dagger C_AW_l,
\]

and report

\[
\eta_A=\|(1-W_lW_l^\dagger)C_AW_l\|.
\]

The raw depth-2 image rank, condition number, discarded singular spectrum and every `eta_A` are mandatory science metadata.

If leakage is not acceptably small, enlarge the target-independent Krylov depth/support. Do **not** tune the basis to improve a GR observable. A Feshbach/Schrieffer-Wolff correction may be tested only as a separately preregistered calculation while preserving the raw projection result.

## First direct science row

The first level supplied to `collective_gr_universality_killer_gate.py` must be produced from this amplitude-level `W_l`, not from static target controls. It must contain the direct collective metric observable, raw `6x6` kinetic Hessian, generator singular values/ranks and `[H,H]` residual on the same compressed habitat.

The present L1 Euclidean rank theorem is a prerequisite for that row, not the row itself: internal-link contraction, full E/S/R depth-two closure and collective observables are still required.

This protocol is designed so the collective GR test can fail honestly: the support wall is fixed before amplitudes, the basis is fixed before GR observables, and the killer thresholds are already frozen.
