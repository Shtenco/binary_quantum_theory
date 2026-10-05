# BQG Three-Node Reduced Chain Result

**Date:** 2026-10-06  
**Status:** EXACT for the explicitly defined nearest-neighbor reduced gluing chain

---

## 1. Reduced three-node system

Each local physical node is the two-dimensional four-spin SU(2)-singlet intertwiner space

$$
\mathcal H_{\rm node}=\mathrm{span}\{|s\rangle,|t\rangle\}.
$$

For three nodes $A,B,C$,

$$
\boxed{
\mathcal H_{ABC}^{\rm red}
=\mathcal H_A\otimes\mathcal H_B\otimes\mathcal H_C,
\qquad \dim=8.
}
$$

No microscopic $2^{12}$ brute-force space is needed.

---

## 2. Nearest-neighbor Hamiltonian

Use the exact two-node reduced gluing operator on links $AB$ and $BC$:

$$
H_{AB}
=\frac32I-\frac34(X_AX_B+Z_AZ_B),
$$

$$
H_{BC}
=\frac32I-\frac34(X_BX_C+Z_BZ_C).
$$

Define

$$
\boxed{
H_3=H_{AB}+H_{BC}.
}
$$

This is an $8\times8$ exact matrix.

Its spectrum is

$$
\boxed{
\lambda_0=3-\frac{3\sqrt2}{2},
\qquad \deg=2,
}
$$

$$
\boxed{
\lambda_1=3,
\qquad \deg=4,
}
$$

$$
\boxed{
\lambda_2=3+\frac{3\sqrt2}{2},
\qquad \deg=2.
}
$$

Thus the ground space is exactly two-dimensional.

---

## 3. Symmetry-neutral ground state

Because of the exact ground degeneracy, choosing one arbitrary pure ground vector would inject an unnecessary convention.

Instead define the normalized ground-space projector

$$
\boxed{
\rho_0=\frac{P_0}{\mathrm{rank}(P_0)}=\frac{P_0}{2}.
}
$$

This is the symmetry-neutral state of the exact ground sector.

Each single logical node is maximally mixed:

$$
\boxed{
\rho_A=\rho_B=\rho_C=\frac12I,
}
$$

so

$$
S(A)=S(B)=S(C)=1\ \mathrm{bit}.
$$

---

## 4. Nearest-neighbor pair spectra

For the nearest pairs $AB$ and $BC$,

$$
\boxed{
\operatorname{Spec}\rho_{AB}
=
\operatorname{Spec}\rho_{BC}
=
\left\{
\frac{3-2\sqrt2}{8},
\frac18,
\frac18,
\frac{3+2\sqrt2}{8}
\right\}.
}
$$

Numerically,

$$
\{0.02144661,0.125,0.125,0.72855339\}.
$$

Therefore

$$
S(AB)=S(BC)
=
-\sum_k\lambda_k\log_2\lambda_k
\approx1.2017520734.
$$

Hence

$$
\boxed{
I(A:B)=I(B:C)
\approx0.7982479266\ \mathrm{bit}.
}
$$

---

## 5. Next-nearest pair spectrum

For the end nodes $A,C$,

$$
\boxed{
\operatorname{Spec}\rho_{AC}
=\left\{0,\frac14,\frac14,\frac12\right\}.
}
$$

Thus

$$
S(AC)=\frac32,
$$

and

$$
\boxed{
I(A:C)=\frac12\ \mathrm{bit}.
}
$$

Therefore

$$
\boxed{
I(A:B)=I(B:C)>I(A:C).
}
$$

This is the first minimal network-level result in the new emergence branch where quantum correlations distinguish graph distance $1$ from graph distance $2$.

---

## 6. Correlation-defined distance

For any strictly decreasing map

$$
d=f(I),
$$

the ordering is

$$
\boxed{
d(A:B)=d(B:C)<d(A:C).}
$$

For example, with the illustrative normalized choice

$$
d_{ij}=-\ln\left(\frac{I_{ij}}{2}\right),
$$

one gets

$$
d_{AB}=d_{BC}\approx0.91848,
$$

$$
d_{AC}=\ln4\approx1.38629.
$$

The ratio is

$$
\boxed{
\frac{d_{AC}}{d_{AB}}\approx1.5093.
}
$$

This is not additive graph distance, and it is not claimed to be fundamental. It is evidence that the correlation structure already resolves nearest and next-nearest separation.

---

## 7. Oriented-volume correlations

For each node,

$$
Q_i=\frac{\sqrt3}{4}Y_i.
$$

In the symmetry-neutral ground sector,

$$
\boxed{
\langle Q_AQ_B\rangle
=\langle Q_BQ_C\rangle
=-\frac3{32}.
}
$$

But

$$
\boxed{
\langle Q_AQ_C\rangle=0.
}
$$

Thus nearest-neighbor relative orientation remains correlated while the end-to-end orientation correlation vanishes in this minimal open chain.

This gives a second independent discriminator of graph distance:

$$
\boxed{
|\langle Q_iQ_j\rangle|:
\quad
\text{nearest}>\text{next-nearest}.
}
$$

---

## 8. What this establishes

Within the explicitly defined reduced nearest-neighbor model:

1. the three-node problem is exactly solvable in dimension $8$;
2. the ground sector is twofold degenerate;
3. the symmetry-neutral ground projector gives maximally mixed single nodes;
4. nearest-neighbor mutual information is exactly larger than next-nearest mutual information;
5. nearest-neighbor orientation correlations are nonzero while next-nearest orientation correlation vanishes;
6. a correlation-defined geometry therefore distinguishes graph separation already at three nodes.

The new chain is

$$
\boxed{
\text{local physical intertwiner qubits}
\to
\text{two-node entangled shape matching}
\to
\text{three-node correlation hierarchy}
\to
\text{first relational distance ordering}.
}
$$

---

## 9. What is still OPEN

This does not yet prove emergent continuum geometry.

The next questions are:

- does the correlation length remain finite or scale with chain size;
- what is the $M$-node spectrum and gap;
- does $I(r)$ exhibit exponential, algebraic, or critical decay;
- can one extract a spectral/correlation dimension from larger graphs;
- is the same reduced coupling derivable from the full BQG dynamics rather than postulated as a shape-matching penalty;
- what changes on 2D/3D connectivity graphs with the same local physical qubits.

---

## 10. Next computational strategy

Do not diagonalize $2^M$ blindly.

The Hamiltonian is

$$
H_M
=\sum_{\langle ij\rangle}
\left[
\frac32I-\frac34(X_iX_j+Z_iZ_j)
\right].
$$

Before numerics, exploit:

- global discrete symmetries;
- parity sectors;
- translational symmetry on periodic chains;
- free-fermion / spin-chain equivalences if available;
- transfer matrices;
- exact small-$M$ spectra as regression anchors.

The immediate next target is therefore to identify the exact many-node model class and solve its correlation scaling analytically or quasi-analytically before increasing $M$.

---

## Reproduction

Run:

```bash
python scripts/bqg_three_node_reduced_chain_gate.py
```

Expected final line:

```text
PASS
```
