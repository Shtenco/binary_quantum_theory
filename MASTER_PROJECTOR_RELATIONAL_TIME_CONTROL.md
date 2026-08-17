# Master projector -> relational time: exact finite positive control

Status: **exact solvable control model; not a claim that the gravity theory already contains this clock.**

The gravity physicalization programme distinguishes a Hamiltonian-constraint spectral parameter from physical frequency. This note gives the smallest exact model showing how physical time is recovered only after conditioning the physical projector on relational clock boundary states.

## 1. Parametrized two-level system

Take

\[
H_s=\begin{pmatrix}0&0\\0&1\end{pmatrix},
\qquad
P_T=\begin{pmatrix}0&0\\0&-1\end{pmatrix}.
\]

On clock tensor system define

\[
\boxed{C=P_T\otimes I+I\otimes H_s.}
\]

The four basis eigenvalues are

```text
(p=0,  E=0)  ->  0
(p=0,  E=1)  -> +1
(p=-1, E=0)  -> -1
(p=-1, E=1)  ->  0.
```

The master constraint is `M=C^2` and

\[
\boxed{
P_{phys}=|0,0\rangle\langle0,0|+|-1,1\rangle\langle-1,1|.
}
\]

## 2. Clock boundary states

Define

\[
\boxed{|T\rangle=\frac1{\sqrt2}\sum_{p\in\{0,-1\}}e^{-ipT}|p\rangle.}
\]

Condition the timeless physical projector on two clock readings:

\[
K(T_{out},T_{in})=2\langle T_{out}|P_{phys}|T_{in}\rangle_{clock}.
\]

The `E=0` component matches `p=0` and gives phase `1`; the `E=1` component matches `p=-1` and gives `exp[-i(T_out-T_in)]`. Hence

\[
\boxed{
K(T_{out},T_{in})
=\begin{pmatrix}1&0\\0&e^{-i\Delta T}\end{pmatrix}
=e^{-iH_s\Delta T},
\quad \Delta T=T_{out}-T_{in}.
}
\]

Ordinary unitary evolution is therefore recovered from a timeless physical projector only after relational conditioning.

## 3. Composition and unitarity

The conditioned kernel satisfies

\[
K(T_3,T_2)K(T_2,T_1)=K(T_3,T_1),
\]

\[
K(T_2,T_1)^\dagger K(T_2,T_1)=I.
\]

These are properties of the relational boundary amplitude, not of a raw constraint spectral parameter.

## 4. Lesson for gravity

The control establishes

```text
constraint spectral parameter z         != physical frequency;
physical projector + relational labels  -> physical evolution/frequency.
```

For gravity the legal analogues are:

1. derive a genuine clock variable and condition on it;
2. use semiclassical geometric boundary data whose proper separation is the physical time observable.

The repository's first clock-free GW route uses the second option; a derived matter clock remains an independent future cross-check.

## 5. Scope

This toy model does not solve the gravity physical inner product, refinement limit or boundary-state problem. It verifies that the master-projector/relational-time logic has an exact solvable realization and needs no `z -> omega` identification.
