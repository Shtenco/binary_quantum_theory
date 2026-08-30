# Q4 local S4 background obstruction

Status: **exact local representation theorem / diagnostic; not a claim of physical anisotropy.**

The old L0 Euclidean Krylov collector grouped normalized node-column overlaps only by Q4 Hamming distance.  That diagnostic implicitly assumes more than exact XOR translation covariance: it also assumes that coordinate permutations act trivially (up to a scalar character) on the chosen local recoupling seed.

For four spin-1/2 legs the SU(2) Gauss-singlet space is two-dimensional.  In the standard pair-coupling basis it carries the irreducible `S4 [2,2]` representation with character

```text
cycle type          1^4   2 1^2   3 1   2^2   4
character [2,2]       2      0     -1      2    0
```

Consequently

\[
\frac1{24}\sum_{\pi\in S_4}U_\pi=0
\]

on the local singlet sector, and there is no nonzero vector satisfying

\[
U_\pi|\psi\rangle=|\psi\rangle\qquad\forall\pi\in S_4.
\]

A fixed `K=0` pure singlet therefore chooses a direction in this two-dimensional recoupling space.  Exact Gauss invariance does not imply full local `S4` invariance of that pure vector.

This resolves the logical status of the historical diagnostic:

```text
exact XOR node transport       != raw Hamming-distance isotropy
```

The former was already verified for the sixteen Euclidean node columns.  The latter additionally probes the background-state transformation under coordinate permutations.

For an irreducible local `[2,2]` carrier, Schur twirling gives

\[
\frac1{24}\sum_\pi U_\pi\rho U_\pi^\dagger=\frac{I_2}{2}
\]

for every pure density matrix `rho`.  This gives one symmetry-covariant local ensemble route, but it is not asserted to be the physical background.

A second, fully pure route remains open: tensor products of several local `[2,2]` representations can contain a global trivial representation.  A globally entangled invariant background may therefore exist even though no local pure invariant vector exists.

## Correct next symmetry questions

1. Construct the full induced `S4` recoupling matrices, not scalar phases, and verify operator covariance.
2. Distinguish transformation of the Hamiltonian operator from transformation/invariance of the chosen background state.
3. Test whether a globally entangled multi-node singlet exists in the required graph sector and whether it restores the desired Q4 isotropy.
4. Only after fixing the background symmetry representation should Hamming-distance Gram degeneracies become a hard covariance criterion.

## Claim boundary

This theorem explains why the old `q4_distance_covariance_manifest=false` diagnostic cannot by itself be called a physical symmetry violation.  It does not establish that the full theory is isotropic, does not select a mixed state as physical, and does not prove existence of a global invariant pure background.
