# Peter--Weyl local volume cross-representation audit

Status: **frozen before evaluating local operator differences.**

The strict covariant-K audit currently fails because the symmetry-adapted all-J
implementation of the Euclidean Hamiltonian differs from the older magnetic
implementation by a relative column norm of about `4.48e-9`; at `1e-9`
pruning their supports are 37 and 38.  Full charged-representation covariance
is otherwise exact in the tested column.

This audit tests the suspected source directly, before any Lorentzian triple is
constructed.

For every local four-leg spin quartet encountered immediately before a volume
insertion in the frozen all-j=1/2 `H_E` word at `Jmax=5/2`, construct three
representations of the same operator

$$
Q=J_1\cdot(J_2\times J_3),\qquad V=\sqrt{|Q|}.
$$

1. `V_magnetic`: the existing `volume123_matrix` acting on legs 1--3 and the
   identity on leg 4;
2. `V_block`: the direct sum of existing symmetry-adapted total-J blocks;
3. `V_zeroaware`: full magnetic functional calculus with eigenvalues whose
   magnitude is below a backward-error tolerance set to zero before the square
   root.

The zero tolerance is not fitted to HDA data:

$$
\tau_Q=1000\,\epsilon_{mach}\,D\,\max(1,\|Q\|_2).
$$

For each quartet report:

- basis completeness of the total-J recoupling transform;
- relative Frobenius/operator differences among the three V constructions;
- relative defects in $V^4=Q^2$;
- $[V,J_{tot}^2]$ covariance defects;
- norm of $V$ acting on the numerically identified exact-Q kernel;
- the separation between the zero-eigenvalue cluster and the smallest nonzero
  $|Q|$ eigenvalue.

Decision rule: a numerical-zero-space diagnosis is accepted only if the Q
spectrum has a clear gap of at least $10^8\tau_Q$, `V_zeroaware` has kernel and
SU(2) defects below `1e-12`, and the dominant `V_magnetic-V_block` difference is
accounted for by their action on the Q-nullspace.  Otherwise the mismatch is
left unresolved and the covariant K leg remains unaccepted.

No threshold in the existing HDA or C(K) gates is relaxed by this audit.
