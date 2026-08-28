# q=2 oriented history: dihedral bridge from winding to phase conjugation and geometry orientation

## Result class

**EXACT GROUP/REPRESENTATION THEORY.**

This file separates two symmetry sectors that must not be conflated:

- the additive winding group of a complete oriented history, `Z`, whose unitary characters form `U(1)`;
- the discrete orientation-reversal/sign sector, represented by a `Z2` involution.

Their correct joint algebra is a semidirect product, not a direct identification.

---

## 1. Oriented history group

Let `T` advance an oriented history by one lifted step and let `R` reverse its orientation. Then

\[
R^2=1,
\qquad
RTR=T^{-1}.
\]

On the universal cover the translation subgroup is

\[
\langle T\rangle\cong\mathbb Z.
\]

Therefore the oriented history symmetry is

\[
\boxed{
G_{\rm hist}^{\rm oriented}
=\mathbb Z\rtimes_{n\mapsto-n}\mathbb Z_2
\cong D_\infty.
}
\]

For a finite `C_N` history carrier this reduces to the ordinary finite dihedral group

\[
D_N=\langle T,R\mid T^N=1,\ R^2=1,\ RTR=T^{-1}\rangle.
\]

---

## 2. Winding characters become conjugate phase pairs

A unitary character of the translation subgroup is

\[
\chi_\theta(n)=e^{in\theta},
\qquad \theta\in[0,2\pi).
\]

The exact Pontryagin dual statement is

\[
\widehat{\mathbb Z}\cong U(1).
\]

Orientation reversal sends

\[
n\mapsto-n,
\]

hence

\[
\chi_\theta(n)
\mapsto
\chi_\theta(-n)
=e^{-in\theta}
=\overline{\chi_\theta(n)}.
\]

Equivalently,

\[
\boxed{
R:\theta\leftrightarrow-\theta
}
\]

and generic `+theta/-theta` sectors form the conjugate pair exchanged by reflection.

This is the exact group-theoretic bridge

\[
\boxed{
\text{history orientation reversal}
\longleftrightarrow
\text{complex conjugation of the winding phase}.
}
\]

---

## 3. History current

Define the Hermitian oriented-history current

\[
C_h=\frac{T-T^\dagger}{2i}.
\]

Since `RTR=T^{-1}=T^dagger`,

\[
RC_hR=-C_h.
\]

On the phase character sector,

\[
T\mapsto e^{i\theta},
\]

so, up to the forward-shift sign convention,

\[
C_h\mapsto\sin\theta.
\]

Therefore the odd part of history direction is literally the sine coordinate on the emergent phase circle.

---

## 4. Geometry orientation

For the q=2 four-face singlet geometry, the exact local oriented triple-product operator is

\[
Q=\frac{\sqrt3}{4}Y_L.
\]

The logical S4 sign-character theorem gives

\[
U_gY_LU_g^\dagger
=\operatorname{sgn}(g)Y_L.
\]

Thus `Y_L` is the unique one-cell logical pseudoscalar channel selected by the S4 sign twirl.

This discrete geometric sign character is **not** the same group as the continuous winding character. The two sectors only share the fact that both reverse sign under their appropriate orientation involution.

---

## 5. Unique minimal diagonal-reflection invariant

Because

\[
Y_L\mapsto-Y_L,
\qquad
C_h\mapsto-C_h,
\]

the bilinear

\[
\boxed{
H_{\rm lock}=g_{YC}\,Y_L\otimes C_h
}
\]

is invariant under simultaneous reversal:

\[
(Y_L,C_h)\mapsto(-Y_L,-C_h).
\]

On a phase-character sector its eigenvalue has the structure

\[
E_{\rm lock}\propto y\sin\theta,
\qquad y=\pm1.
\]

Hence a nonzero microscopic coefficient would energetically correlate geometric chirality with one of the conjugate history-phase directions without explicitly breaking the combined orientation symmetry.

---

## 6. What is and is not proved

### Exact

\[
\mathbb Z\rtimes\mathbb Z_2=D_\infty,
\]

\[
\widehat{\mathbb Z}=U(1),
\]

\[
R:\theta\to-\theta,
\]

\[
RC_hR=-C_h,
\]

and, with the already-proved q=2 geometry sign rule,

\[
(Y_L\otimes C_h)
\text{ is invariant under diagonal reversal.}
\]

### Not implied by this theorem

The theorem does not determine

\[
g_{YC}.
\]

It also does not turn the Hamiltonian constraint history into physical time or construct the physical projector.

The coefficient must be measured from the actual graph-changing gravitational operator. That is the role of the separate complete 32D Peter–Weyl source-`Y` history-current gate.

---

## 7. Relation to the Lorentzian sign sector

Existing finite Peter–Weyl evidence already shows a nonzero S4-sign/pseudoscalar `Y` channel in the Lorentzian operator after environment averaging and minimal Hermitian completion.

That result proves that the **geometric sign sector is dynamically populated** in the current Lorentzian candidate. It does not by itself prove that its coefficient is the same `g_YC` multiplying the winding-history current above.

The remaining bridge is therefore sharply stated:

\[
\boxed{
\text{resolve the Lorentzian }Y\text{ amplitude by oriented history character }\theta
}
\]

and test whether its odd phase dependence is proportional to `sin(theta)` or a more general allowed odd character function.

That is a finite operator-identification problem, not a question of inventing complex numbers by hand.
