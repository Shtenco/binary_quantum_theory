# BQG global K5 correlated-ancilla symmetry result

Status:
- **FINITE PASS**: the existing K5 spin-network tensor is exactly S5 covariant.
- **NO-GO / PROVED finite representation fact**: S5 symmetry alone does not uniquely select the global binary ancilla, because the relevant invariant sector has dimension two.

The production all-\(j=1/2\) K5 contraction defines a 32-component logical tensor

\[
|V_5\rangle
\in
\left([2,2]_{S_4}\right)^{\otimes5}.
\]

The exact induced \(S_5\) action was constructed from vertex relabeling plus
the corresponding local \(S_4\) recoupling matrices.

## Bare logical action

Without adding the canonical edge-orientation parity correction,

\[
\boxed{
R(g)|V_5\rangle
=
\operatorname{sgn}(g)|V_5\rangle
}
\]

within

\[
2.43\times10^{-15}.
\]

The sign-projector weight is

\[
\boxed{
\langle V_5|P_{\rm sign}|V_5\rangle=1
}
\]

within floating precision.

## Orientation-corrected action

Including the parity from reversing canonically oriented K5 epsilon edges,
the same tensor becomes a trivial scalar:

\[
\boxed{
R_{\rm oriented}(g)|V_5\rangle
=
|V_5\rangle
}
\]

again with error

\[
2.43\times10^{-15}.
\]

Thus \(V_5\) is an exact global correlated ancilla compatible with the full K5
permutation symmetry.

## But symmetry does not select it uniquely

The exact group projectors have

\[
\boxed{
\operatorname{rank}P_{\rm triv}=2,
\qquad
\operatorname{rank}P_{\rm sign}=2,
}
\]

depending on the orientation convention.

Therefore the global symmetry-allowed ancilla space is two-dimensional.

Hence

\[
\boxed{
S_5\text{ symmetry alone}
\not\Rightarrow
\text{unique global q=2 ancilla state}.
}
\]

This is the global analogue of the local pure-ancilla selection problem:
symmetry identifies a small physical candidate sector but not a unique line.

## Consequence

The existing \(V_5\) tensor remains a valid exact symmetry-compatible
candidate correlated ancilla.

However selecting it rather than the second invariant line requires an
additional criterion from:

- the actual constraint/master dynamics;
- a refinement fixed-point condition;
- or the physical history/boundary prescription.

The next minimal calculation is therefore to restrict the symmetric K5 master
to this two-dimensional global invariant ancilla sector and test whether it
has a nondegenerate eigenline, and whether that line coincides with \(V_5\).
