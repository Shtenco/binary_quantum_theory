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

This protocol is designed so the collective GR test can fail honestly: the support wall is fixed before amplitudes, the basis is fixed before GR observables, and the killer thresholds are already frozen.
