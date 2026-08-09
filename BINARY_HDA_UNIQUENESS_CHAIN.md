# Binary + HDA conditional uniqueness chain

Status: **mathematical conditional chain; the microscopic dynamical hypotheses are not yet proved**.

This note sharpens the earlier binary-adjoint dimension argument and corrects an over-broad qudit generalization.

## 1. Local quantum carrier and full isotropy

For a `q`-level local Hilbert space, the real vector space of traceless Hermitian observables has dimension

\[
D_q=q^2-1.
\]

Unitary conjugation modulo the center acts through `PSU(q)` and

\[
\dim PSU(q)=q^2-1=D_q.
\]

If this observable space is to be interpreted as an **isotropic spatial vector space**, the available local frame transformations must cover the full orientation-preserving rotation group `SO(D_q)`, whose dimension is

\[
\dim SO(D_q)=\frac{D_q(D_q-1)}2.
\]

A necessary dimension equality is therefore

\[
D_q=\frac{D_q(D_q-1)}2.
\]

For a nontrivial carrier this gives

\[
\boxed{D_q=3,\qquad q=2.}
\]

For the qubit this necessary condition is also realized: the adjoint action is the standard double cover

\[
\boxed{SU(2)/\mathbb Z_2\simeq SO(3).}
\]

For `q>2`, `PSU(q)` is a proper subgroup of `SO(q^2-1)` and preserves additional Lie-algebraic structure.  Therefore the previous heuristic statement `D_space=q^2-1 for every qudit` is too strong.  The qubit is special because its full unitary frame freedom is exactly the full three-dimensional rotation freedom.

## 2. HDA dimension estimator

In `D` spatial dimensions the inverse DeWitt metric entering the ADM Hamiltonian has trace coefficient

\[
\boxed{c_D=\frac1{D-1}}.
\]

Thus a microscopic kinetic form fitted to

\[
\pi_{ab}\pi^{ab}-c_{eff}\pi^2
\]

provides an independent dimension estimator

\[
\boxed{D_{HDA}=1+\frac1{c_{eff}}.}
\]

For the binary/isotropic result `D=3`, HDA therefore requires

\[
\boxed{c_{eff}\to\frac12,}
\]

exactly the value selected independently by `DEWITT_HDA_UNIQUENESS.md`.

This gives a cross-check that does not use diffusion dimension:

\[
D_{rot}=3
\quad\Longleftrightarrow\quad
D_{HDA}=1+1/c_{eff}=3.
\]

## 3. HDA fixes the relativistic tensor cone

For the two-derivative TT sector of

\[
H_{A,B}=\int d^Dx\left[A\pi_{TT}^2+\frac B4(\partial h_{TT})^2\right],
\]

Hamilton's equations give

\[
\boxed{\ddot h_{TT}=AB\,\nabla^2 h_{TT}.}
\]

The standard HDA normalization selects `AB=1`, so in units set by the hypersurface normal

\[
\boxed{c_T^2=1,\qquad z=1.}
\]

Thus `z->1` is not an independent fit once the leading local metric Hamiltonian and HDA are recovered.

## 4. Constraint counting gives the graviton count

A spatial metric in `D` dimensions has

\[
N_q=\frac{D(D+1)}2
\]

configuration components.  The `D` momentum constraints plus one Hamiltonian constraint are first class, so they remove `D+1` configuration degrees of freedom after quotienting the associated gauge orbits.  Therefore

\[
\boxed{
N_{phys}^{config}
=\frac{D(D+1)}2-(D+1)
=\frac{(D+1)(D-2)}2.
}
\]

At `D=3`:

\[
\boxed{N_{phys}^{config}=2.}
\]

This equals the standard massless spin-2 polarization count in spacetime dimension `d=D+1`,

\[
N_{pol}=\frac{d(d-3)}2.
\]

Hence, under the stated hypotheses,

\[
\boxed{
\text{qubit full isotropy}
\Rightarrow D=3
\Rightarrow c_{DW}=1/2
\Rightarrow AB=1
\Rightarrow z=1
\Rightarrow 2\text{ physical tensor modes}
\Rightarrow 3+1\text{ relativistic gravity kinematics}.
}
\]

## 5. What is and is not proved

The chain is **conditional**.  It does not prove that the microscopic theory actually:

- uses the entire traceless qubit observable algebra as spatial flux geometry;
- restores full local rotational isotropy rather than a subgroup;
- generates the standard first-class HDA;
- reaches a local two-derivative metric phase;
- supplies Lorentzian unitarity, matter, or experimental correctness.

But it dramatically reduces redundancy among the target observables.  A future frozen run should not independently tune `D`, `c_DW`, `z` and the graviton count.  They are linked by the above identities.

## 6. Strong joint falsifier

In one common regulator-safe scaling window require

\[
\boxed{
D_{rot}\to3,
\qquad
1+1/c_{eff}\to3,
\qquad
A_{eff}B_{eff}\to1,
\qquad
\Delta_{HH}^{Q}\to0,
\qquad
N_{phys}\to2.
}
\]

A mismatch between any two of these quantities falsifies the proposed binary-HDA universality class even if a spectral-dimension plateau happens to be near four.
