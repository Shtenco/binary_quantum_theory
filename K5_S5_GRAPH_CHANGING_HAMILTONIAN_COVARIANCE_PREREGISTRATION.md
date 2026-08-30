# K5 S5 graph-changing Hamiltonian covariance v1 — preregistration

Status: **finite safe-cutoff operator-covariance theorem on the complete 32D all-j=1/2 input sector.  Not an HDA-closure or continuum theorem.**

## Frozen dynamical input

Use the canonical graph-changing Peter-Weyl Hamiltonian implementation

`scripts/k5_peter_weyl_safe_hda_column.py`

with exactly:

- graph `K5`;
- all 32 basis states returned by `basis_full_jhalf()` as the input sector;
- nodes `v=0,1,2,3,4`;
- doubled cutoff `JMAX2=5`, i.e. `Jmax=5/2`;
- the canonical Hermitian oriented node action `apply_H_cached_state`;
- no projection of graph-changing images back to the 32D sector before covariance is tested.

Precompute all 160 columns

\[
H_v|e_j\rangle,\qquad v=0,\dots,4,\quad j=0,\dots,31.
\]

## Frozen graph-automorphism transport

For a vertex permutation `g in S5`:

1. every old edge `(u,v)` is relabelled to the canonically sorted new edge `(g(u),g(v))`, carrying the same spin;
2. old node `v` is sent to `g(v)`;
3. the old local sorted neighbour list and new local sorted neighbour list define a unique permutation of the four local tensor legs;
4. a canonical all-outgoing intertwiner tensor with old local spins and recoupling label `K` is permuted by that leg map and decomposed into the complete allowed `K'` basis at the new node;
5. local recoupling coefficients at all five nodes are multiplied, so a single Peter-Weyl state key may map to a superposition of state keys;
6. no fitted phase, Procrustes alignment, singular-vector selection or target-state alignment is permitted.

The same transport restricted to the 32D all-j=1/2 sector must agree with the independently defined K5 S5 carrier representation.

## Frozen orientation character

The canonical local oriented triple pattern has coefficient `(-1)^r` for the triple omitting local neighbour slot `r`.  Under a vertex permutation `g`, the induced four-leg permutation at node `v` has parity

\[
\boxed{
\eta(g,v)=\operatorname{sgn}(p_v)
=\operatorname{sgn}(g)(-1)^{v+g(v)}.
}
\]

This identity is a cofactor identity of the 5x5 permutation matrix and must be verified combinatorially for all `120 x 5` `(g,v)` pairs before any Hamiltonian comparison.

The raw node Hamiltonian covariance target is therefore frozen as

\[
\boxed{
U_g H_v U_g^{-1}=\eta(g,v) H_{g(v)}.
}
\]

Equivalently define boundary-oriented constraints

\[
\widehat H_v=(-1)^vH_v.
\]

Then

\[
\boxed{
U_g\widehat H_vU_g^{-1}
=\operatorname{sgn}(g)\widehat H_{g(v)}.
}
\]

Multiplying an individual constraint by `(-1)^v` does not change its kernel and leaves the master quadratic form invariant:

\[
\ker\widehat H_v=\ker H_v,
\qquad
\sum_v\widehat H_v^\dagger\widehat H_v
=\sum_vH_v^\dagger H_v.
\]

## Preregistered test set

The operator equality is tested on the **entire 32D input basis**, but only the four adjacent-transposition Coxeter generators are required as independent group elements:

- `(01)`;
- `(12)`;
- `(23)`;
- `(34)`.

Because these generate `S5`, because the transport representation law is checked independently, and because the orientation character above is checked as a cocycle, covariance on all four generators implies covariance on the generated group within the tested input domain.

For every generator `g`, every node `v`, and every input basis state `|e_j>`, compare the full sparse states

\[
U_gH_v|e_j\rangle
\]

and

\[
\eta(g,v)H_{g(v)}U_g|e_j\rangle.
\]

The right side must be assembled linearly from the already precomputed 160 columns; no projected shortcut is allowed.

## Required transport checks on graph-changing outputs

Before accepting the Hamiltonian covariance comparison, the gate must verify on every unique state key appearing in the 160 columns and every Coxeter generator:

- transported state norm is preserved;
- inverse transport returns the original key state;
- mapped spin labels agree exactly with edge relabelling;
- the local recoupling decomposition is complete within numerical precision;
- no state-support truncation is introduced by transport.

## Master-form consequence

Build the full-image 32D master Gram matrix

\[
[M]_{ij}=\sum_v\langle H_ve_i,H_ve_j\rangle.
\]

The gate must verify that `M` is invariant under the full 120-element input representation:

\[
\boxed{U_g M U_g^\dagger=M\qquad\forall g\in S_5}
\]

up to the frozen numerical tolerance.  This follows from the pseudoscalar-vector covariance above but is tested independently as a high-value cross-check.

## PASS criteria frozen before the run

GREEN requires:

1. exact combinatorial verification of `eta(g,v)=sgn(g)(-1)^(v+g(v))` for all 600 pairs;
2. graph-changing transport norm/inverse/completeness checks pass for every encountered output key under all four generators;
3. input-sector transport is unitary and consistent with the frozen local recoupling rule;
4. maximum relative sparse-state defect in all `4 x 5 x 32 = 640` raw covariance comparisons is below `5e-9`;
5. the equivalent boundary-oriented covariance defect is below `5e-9`;
6. the full-image master Gram is Hermitian/PSD up to numerical roundoff;
7. its maximum relative `S5` invariance defect over all 120 group elements is below `5e-9`;
8. raw and boundary-oriented master matrices are equal up to numerical roundoff.

These tolerances are fixed now.  They may not be loosened after seeing the result.

## Deliberately excluded claims

A GREEN result does **not** prove:

- Hamiltonian-constraint kernel nontriviality;
- HDA closure or anomaly freedom;
- covariance outside the all-j=1/2 input sector;
- Lorentzian-constraint covariance unless that term is separately included;
- Q4↔K5 global equivalence;
- continuum diffeomorphism invariance;
- a physical projector, physical time or phenomenology.

A RED result must be diagnosed as transport convention, orientation convention or genuine operator-covariance failure; no tolerance relaxation or projection back into the 32D sector is permitted as a repair.
