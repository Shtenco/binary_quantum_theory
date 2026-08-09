# Canonical Micro Architecture V1

Status: **operator architecture narrowed to a small falsifiable class; M0 is not yet declared closed because the full finite Lorentzian update/operator-ordering and held-out continuum run are not implemented.**

## 1. Microscopic carrier

Use a spatial spin-network/quantum-link description rather than treating one Euclidean face qubit as a four-dimensional Lorentz connection.

- each dual spatial link carries a finite-dimensional `SU(2)` quantum-link Hilbert space;
- the minimal nontrivial spinor quantum-link representation is four-dimensional, hence encodable by two qubits per link;
- left/right flux generators satisfy the exact local `SU(2)` Gauss algebra;
- node intertwiners are gauge-invariant subspaces of the incident link Hilbert spaces, not replacement degrees of freedom for the links.

For a closed four-valent dual graph with `N_v` nodes, the number of links is `N_e=2 N_v`.  At the minimal four-state link truncation this is

\[
\boxed{4N_v\text{ microscopic qubits}}
\]

before optional topology/occupancy registers.  This is a resource count, not a continuum claim.

## 2. Exact microscopic geometry facts

For four incident spin-1/2 face carriers,

\[
(1/2)^{\otimes4}=2(0)\oplus3(1)\oplus1(2),
\]

so the Gauss-singlet node sector is two-dimensional.  The corresponding logical operators contain tetrahedral shape and oriented-volume information, as derived in `SPATIAL_QUBIT_GEOMETRY_BRIDGE.md`.

However the absolute volume at fixed `j=1/2` is scalar:

\[
Q=\frac{\sqrt3}{4}Y_L,
\qquad
V\propto\sqrt{|Q|}=\frac{3^{1/4}}2 I_L.
\]

Therefore a dynamics permanently confined to the microscopic four-spin-1/2 intertwiner has

\[
[O,V]=0
\]

for every operator `O` acting only inside that two-dimensional subspace.  It cannot support a nontrivial Thiemann-type volume commutator.

The first collective equal-spin tetrahedral sector with nontrivial absolute volume is

\[
\boxed{j=1\quad(N_{face}=2\text{ aligned micro qubits})},
\]

where

\[
\operatorname{spec}Q=\{-\sqrt3,0,+\sqrt3\}.
\]

At `j=3/2`,

\[
\operatorname{spec}Q\approx\{-4.43706,-1.29904,+1.29904,+4.43706\},
\]

already giving two nonzero absolute-volume scales.  Thus representation/collective-spin growth is not optional: it is required both by semiclassicality and by nontrivial volume dynamics.

## 3. Collective RG targets

A coarse face containing `N` approximately aligned microscopic spin-1/2 carriers has

\[
j=N/2,
\qquad
\frac{\Delta J_\perp}{|\langle J\rangle|}=N^{-1/2}.
\]

For `N_face ~ b^2`,

\[
\boxed{\Delta n\sim b^{-1}}.
\]

The four-valent equal-spin intertwiner space grows as

\[
\boxed{\dim\operatorname{Inv}(V_j^{\otimes4})=2j+1=N+1},
\]

so the microscopic geometry qubit grows into a semiclassical shape space rather than remaining a qubit.

Exact tetrahedral flux reconstruction gives the independent scaling laws

\[
\boxed{A\sim b^2,\qquad V\sim b^3}.
\]

The combined held-out spatial targets are therefore

\[
A\sim b^2,
\qquad
V\sim b^3,
\qquad
\Delta n\sim b^{-1},
\qquad
d_s^{slice}\to3.
\]

## 4. Kinematic topology/re-coupling rule

Pure changes of coupling tree are represented by the exact `SU(2)` Racah/F move.  For the microscopic spin-1/2 singlet sector one convention gives

\[
F_{1/2}=
\begin{pmatrix}
1/2&-\sqrt3/2\\
\sqrt3/2&1/2
\end{pmatrix}.
\]

No adjustable mixing angle is introduced.  Higher-spin versions are fixed by `6j` symbols.  The pentagon/Biedenharn--Elliott identity is the kinematic coherence condition for sequences of such recouplings.

This closes only basis/retriangulation coherence.  It does not imply that two overlapping physical Hamiltonian updates commute.

## 5. Gravity Hamiltonian class

A pure plaquette quantum-link Hamiltonian has a Yang--Mills `F^2` continuum structure and is rejected as the gravity Hamiltonian.

At leading derivative order, local `SU(2)` covariance, orientation sensitivity, linearity in curvature and absence of a background metric select the classical Euclidean gravitational scalar

\[
H_E\sim\frac{\epsilon_{ijk}E^iE^jF^k}{V}.
\]

For the finite quantum theory the inverse volume should not be quantized literally.  Use a holonomy-volume-commutator regularization of the Thiemann type.  Schematically,

\[
\boxed{
\hat H_E(v)
\propto
\sum_{IJK}\epsilon^{IJK}
\operatorname{Herm}
\operatorname{Tr}
\left[
(\hat U_{\alpha_{IJ}}-\hat U_{\alpha_{IJ}}^\dagger)
\hat U_{s_K}[\hat U_{s_K}^\dagger,\hat V_v]
\right].
}
\]

At a four-valent node there are only `C(4,3)=4` oriented triples, so this leading local operator has a compact finite support.

The full real-connection Lorentzian constraint must add the standard extrinsic-curvature correction generated from commutators involving the Euclidean constraint and volume; it is **not** a new arbitrary tensor structure.

For the first pure-gravity falsification run set

\[
\Lambda=0
\]

and treat the Barbero--Immirzi parameter as a regulator/universality variable, not as a fitted physical number.  Operator ordering and finite-link representation are likewise preregistered regulator choices and must later be varied without retuning observables.

## 6. Exact Gauss protection

Because flux and curvature transform in the adjoint, the contraction

\[
\epsilon_{ijk}E^iE^jF^k
\]

is an `SU(2)` scalar.  If the volume is also gauge invariant, the finite regulated Hamiltonian can be constructed to commute with the local Gauss generators:

\[
\boxed{[G_v^a,H]=0}
\]

exactly at the cutoff.  The hard closures are therefore the spatial-diffeomorphism and Hamiltonian-Hamiltonian sectors, not Gauss invariance.

## 7. Constraint counting target

Canonical gravity begins with

\[
9+9=18
\]

phase-space dimensions per continuum point.  Seven first-class constraints

\[
3G+3D+1H
\]

remove fourteen phase-space dimensions, leaving

\[
\boxed{4\text{ physical phase dimensions}=2\text{ configuration modes}}.
\]

Therefore the primary spin-2 gate is not a manually TT-projected Hessian.  It is restoration of a rank-seven first-class constraint system.  Exactly two physical modes then follow by Dirac counting; the TT/massless spectrum is an independent cross-check of their spin and dispersion.

## 8. Cheap Lorentzian signature gate

Before the expensive nonlinear HDA test, fit the coarse kinetic quadratic form on symmetric spatial metric perturbations to

\[
Q[h]=a\,h_{ij}h_{ij}+b(\operatorname{tr}h)^2.
\]

Rotationally invariant GR requires

\[
\boxed{b/a\to-1}.
\]

Equivalently the DeWitt supermetric fingerprint is

\[
\boxed{\operatorname{spec}G_{DW}\propto(-2,1,1,1,1,1)},
\]

one negative conformal direction and five positive traceless directions before Hamiltonian reduction.  After constraints, physical TT modes must be positive.  An all-positive coarse supermetric is Euclidean-like; extra negative physical directions signal ghosts.

## 9. Common continuum prediction system

A successful frozen rule must satisfy one common window:

\[
A\sim b^2,
\quad
V\sim b^3,
\quad
\Delta n\sim b^{-1},
\quad
d_s^{slice}\to3,
\]

\[
m_{phys}\sim b^{-1},
\quad
z\to1,
\quad
d_s^{history}=1+3/z\to4,
\]

\[
b/a\to-1,
\quad
\Delta_{shape}\to0,
\quad
\Delta_{HDA}\to0,
\quad
m_{unwanted}/m_{phys}\to\infty.
\]

The independent fixed-Regge branch has now passed a held-out `O(a^2)` prediction test and supplies the downstream targets

\[
\epsilon_{FP},\epsilon_{EH},W_3\sim b^{-2}.
\]

Collective-spin coherent-state algebra naturally predicts the same hierarchy:

\[
\text{field fluctuations}\sim b^{-1},
\qquad
\text{mean/operator corrections}\sim b^{-2}.
\]

## 10. What is still missing before M0 can be marked frozen

1. an explicit finite matrix representation of the chosen quantum-link operator on each link;
2. a fixed Hermitian ordering for the Euclidean and Lorentzian Hamiltonian operators;
3. a topology/occupancy register if physical graph-changing moves, rather than pure recouplings, are allowed;
4. the exact causal scheduling rule for overlapping local Hamiltonian updates;
5. a fixed initial ensemble and measure;
6. a preregistered finite-size sequence and stopping/falsification rule.

Until those six items are encoded, this file is a sharply constrained architecture, not a completed microscopic theory.
