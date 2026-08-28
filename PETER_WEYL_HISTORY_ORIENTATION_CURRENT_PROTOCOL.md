# Peter–Weyl microscopic geometry ↔ history orientation-current protocol

## Status

**PREREGISTERED PHYSICALIZATION GATE — result not assumed in this document.**

This protocol asks one narrow question:

> Does the already-existing graph-changing Peter–Weyl Euclidean constraint dynamics contain a first-history-shell operator component that correlates the sign of tetrahedral quantum geometry with ordered microscopic history direction?

It does **not** identify the constraint-history label with physical time, and it does not construct the physical rigging map, physical inner product, continuum photon, or experimental observable.

---

## 1. Frozen microscopic input

Use the canonical all-`j=1/2` K5 Gauss carrier. Each of the five tetrahedra has the two-dimensional intertwiner space

\[
K_v\in\{0,2\},
\]

so the active logical carrier has

\[
\dim\mathcal H_{\rm active}=2^5=32.
\]

At one preregistered source tetrahedron, `v=0`, the exact oriented triple-product operator obeys

\[
Q_0=\frac{\sqrt3}{4}Y_0.
\]

Therefore logical Pauli `Y_0` is the frozen local geometry-orientation pseudoscalar.

The Euclidean graph-changing constraint uses the already-corrected sine-Hermitian ordering

\[
H_E^{\rm sine}
=\sum_s \epsilon_s\frac{T_s-T_s^\dagger}{2i}.
\]

For each active input state define the history-resolved images

\[
B_+|\psi\rangle=\sum_s\epsilon_sT_s|\psi\rangle,
\qquad
B_-|\psi\rangle=\sum_s\epsilon_sT_s^\dagger|\psi\rangle.
\]

The implementation must independently reconstruct

\[
H_E^{\rm sine}|\psi\rangle
=-\frac{i}{2}B_+|\psi\rangle
+\frac{i}{2}B_-|\psi\rangle
\]

on all 32 columns before any locking coefficient is interpreted.

The one-shell cutoff is frozen to

\[
J_{\max}=\frac32,
\]

which is the complete spin wall reached from `j=1/2` by one Euclidean graph-changing history shell.

---

## 2. Two independent orientation-current operators

The rate-asymmetry operator is

\[
D_{\rm rate}
=B_+^\dagger B_+-B_-^\dagger B_-.
\]

It asks whether forward and reverse ordered histories have different total transition weight after returning to the active carrier.

The coherent phase-asymmetry operator is

\[
D_{\rm phase}
=\frac{B_+^\dagger B_--B_-^\dagger B_+}{2i}.
\]

It asks a different question: whether the two history orientations interfere with a nontrivial Hermitian phase-current even if their separate norms agree.

Thus

\[
D_{\rm rate}=0
\]

does **not** imply

\[
D_{\rm phase}=0.
\]

In operator notation, if

\[
A=\sum_s\epsilon_sT_s,
\]

then on the active carrier

\[
D_{\rm rate}=P(A^\dagger A-AA^\dagger)P,
\]

while

\[
D_{\rm phase}
=\frac{P[(A^\dagger)^2-A^2]P}{2i}.
\]

The old symmetric return kernel `P(H_E^sine)^2P` does not separately determine these two quantities.

---

## 3. Why one local trace is insufficient

A first attempt might inspect only

\[
g_Y=\frac{\operatorname{Tr}(Y_0D)}{\operatorname{Tr}(Y_0^2)}.
\]

That is only the coefficient of

\[
Y_0\otimes I_1\otimes I_2\otimes I_3\otimes I_4.
\]

It can vanish even when the microscopic operator contains, for example,

\[
Y_0\otimes Z_1,
\qquad
Y_0\otimes X_1,
\qquad
Y_0\otimes Y_2Z_3.
\]

The first can cancel after an environment trace. The latter two can also vanish on every fixed-`K` diagonal environment because they require coherent environment superpositions.

Therefore a complete first-shell no-go requires exhausting the whole source-`Y` operator sector.

---

## 4. Frozen complete 256-string source-Y audit

For each

\[
P_r\in\{I,X,Y,Z\},\qquad r=1,2,3,4,
\]

compute

\[
c_{P_1P_2P_3P_4}[D]
=\frac1{32}
\operatorname{Tr}\!\left[
(Y_0\otimes P_1\otimes P_2\otimes P_3\otimes P_4)^\dagger D
\right].
\]

There are exactly

\[
4^4=256
\]

such coefficients for `D_rate` and another 256 for `D_phase`.

Because five-qubit Pauli strings are an orthogonal operator basis, vanishing of all 256 coefficients is equivalent to vanishing of the entire component of `D` containing local geometry pseudoscalar `Y_0` on the declared 32-dimensional active carrier.

This is the strongest first-shell statement made by this gate.

---

## 5. Preregistered classification

The result must be assigned to exactly one of the following classes separately for `D_rate` and `D_phase`.

### A. `INTRINSIC_NONZERO_FIRST_SHELL`

The coefficient of

\[
Y_0\otimes I^{\otimes4}
\]

is nonzero above the frozen relative tolerance.

Interpretation: the first-shell orientation/history correlation survives the maximally mixed logical environment.

### B. `K_BASIS_ENVIRONMENT_CONDITIONED_FIRST_SHELL`

The intrinsic coefficient vanishes, but a source-`Y` coefficient with only `I/Z` environment factors is nonzero.

Interpretation: locking exists for diagonal logical environments but cancels in the unbiased trace.

### C. `COHERENT_ENVIRONMENT_CONDITIONED_FIRST_SHELL`

All `I/Z` environment source-`Y` coefficients vanish, but at least one source-`Y` string containing environmental `X` or `Y` is nonzero.

Interpretation: the locking requires coherent logical surroundings and is invisible both to the maximally mixed trace and to fixed-`K` classical environments.

### D. `ZERO_ALL_SOURCE_Y_PAULI_CHANNELS_FIRST_SHELL_WITHIN_TOL`

All 256 source-`Y` coefficients vanish within the frozen tolerance.

Interpretation: this is a complete first-history-shell no-go for geometry-orientation locking inside the canonical 32D all-`j=1/2` active carrier of the Euclidean K5 Peter–Weyl regulator.

It is **not** a no-go for higher history shells, Lorentzian dynamics, another regulator limit, or the physical history/projector construction.

---

## 6. Frozen numerical tolerance

Let

\[
I_{\rm hist}=\frac1{32}\operatorname{Tr}
(B_+^\dagger B_+ + B_-^\dagger B_-).
\]

The source-`Y` coefficient zero threshold is

\[
\tau_Y=10^{-10}\max(I_{\rm hist},10^{-30}).
\]

No threshold is chosen after seeing the coefficient spectrum.

---

## 7. Important structural control: absolute volume does not trivially insert the sign

On the pure spin-`1/2` logical tetrahedron,

\[
Q=\frac{\sqrt3}{4}Y,
\]

but the production volume operator is

\[
V=\sqrt{|Q|}.
\]

Hence the two opposite orientation eigenstates have the same local absolute volume on the initial logical carrier.

A nonzero source-`Y` history-current coefficient therefore cannot be explained by simply inserting the sign of `Q` through the input absolute-volume eigenvalue. It must arise through ordered holonomy/history interference and the changed-spin intermediate sectors of the graph-changing constraint.

---

## 8. If the Euclidean first shell is zero

The next preregistered target is not an arbitrary larger brute-force Euclidean calculation.

The Lorentzian operator has different parity structure: the existing doubled-spin grading makes `H_E` odd and `H_L` even, so

\[
P H_E P=0
\]

while

\[
P H_L P
\]

is not forbidden by that grading.

The existing exact SU(2) scalar-channel analysis of the Lorentzian `C(K)C(K)C(V)` triple leaves only five rank histories:

```text
000
011
101
110
111
```

Therefore the next physicalization gate after a complete Euclidean source-`Y` first-shell zero is a finite five-channel Lorentzian orientation-current calculation, not an unrestricted Hilbert-space search.

---

## 9. Claim boundary

A nonzero result proves only a **finite microscopic constraint-history correlation** in the declared K5 regulator and carrier.

It does not prove:

- that the history label is physical time;
- that the constraint resolvent is a physical frequency propagator;
- a physical rigging map or history measure;
- a dynamical Maxwell photon;
- a continuum `U(1)` coupling constant;
- an experimental Lorentz-violation signal;
- a Standard-Model mass or fine-structure constant.

The physical bridge remains

\[
\hat H[N]
\to \mathcal P_{\rm phys}
\to Z[J_g]
\to \Gamma[g]
\to \Gamma^{(2)}_{\rm metric}
\to K_{TT}(\omega,k),
\]

or an independently derived relational-clock/deparametrized route.

The present gate attacks only one earlier missing microscopic link:

\[
\boxed{
\text{geometry orientation}
\stackrel{?}{\longleftrightarrow}
\text{ordered graph-changing history current}
}
\]

without assuming the answer.
