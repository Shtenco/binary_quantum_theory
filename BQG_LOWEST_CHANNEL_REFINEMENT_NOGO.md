# BQG lowest-master-channel refinement NO-GO

Status: **NO-GO / FINITE exact counterexample to the rule "always choose the lowest local master multiplicity eigenchannel".**

A temporary simplification in the refinement programme was to identify the
physical representation-RG lineage with the lowest eigenchannel of the local
\(S_4\)-twirled multiplicity master \(A_j\) at every scale.

The microscopic binary-ancilla refinement tensor provides a direct finite test
of that rule.

## First multiplicity branch

At

\[
j=\frac32\to2
\]

the source \([2,2]\) carrier is unique, while the target has two master
multiplicity channels.

The exact channel-flow row is

\[
\boxed{
\mathcal F_{3/2\to2}
=
\begin{pmatrix}
0.05404213255283678 &
0.9459578674471627
\end{pmatrix}.
}
\]

Therefore the microscopic refinement image is almost orthogonal to the lowest
target master channel and instead aligns overwhelmingly with the second
channel.

In particular,

\[
\boxed{
\mathcal F_{\rm lowest}=0.0540421\ne1.
}
\]

Thus exact microscopic refinement does **not** select the lowest target
eigenchannel at the first scale where multiplicity appears.

## Higher-scale independent counterexample

For the low-source / low-target comparison

\[
j=3\to\frac72
\]

the exact finite overlap is even smaller:

\[
\boxed{
\mathcal F_{\rm low\to low}
=
0.0010798724532179987,
}
\]

with projector distance

\[
\boxed{
\chi=0.9994599179290695.
}
\]

Hence the lowest-eigenchannel rule fails independently at a later scale.

## Correct conclusion

The rule

\[
\boxed{
\text{physical RG channel at scale }j
=
\arg\min\operatorname{spec}A_j
}
\]

is rejected as an exact microscopic ancestry principle for the current
binary-ancilla blocking plus local Euclidean master construction.

This does **not** reject the master spectrum or the BQG continuum programme.

It means that the local master eigenvalue ordering is not, by itself, the
refinement-selection principle.

The correct finite object is the full ancestry matrix

\[
\boxed{
\mathcal F_j^{ab}
=
\frac12\operatorname{Tr}
\left(
P_{j\to j+1/2,a}^{\rm block}
P_{j+1/2,b}^{\rm master}
\right),
}
\]

followed by an ancestry-consistent path through its channels.

## Scope

This NO-GO is finite and representation-level.

It does not establish which ancestry-consistent channel is ultimately physical
in the full Lorentzian/refinement history.  That requires the full
graph-changing habitat residual and physical-history construction.

It only removes the unsupported shortcut "lowest local master eigenvalue =
physical RG lineage".
