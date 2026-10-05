# BQG Two-Node Reduced Gluing Result

**Date:** 2026-10-06  
**Status:** EXACT for the explicitly defined reduced two-node shape-matching Hamiltonian

---

## 1. Why this calculation is cheap

Each four-spin $j=1/2$ SU(2)-invariant node has only two physical intertwiner states:

$$
\mathcal H_{\rm phys}^{(4)}=\mathrm{span}\{|s\rangle,|t\rangle\},
\qquad \dim=2.
$$

For two nodes $A,B$ we therefore work directly in

$$
\boxed{
\mathcal H_{AB}^{\rm red}
=\mathcal H_A^{\rm phys}\otimes\mathcal H_B^{\rm phys},
\qquad \dim=4.
}
$$

No $2^8=256$ brute-force Hilbert space is needed for this reduced test.

---

## 2. Three local shape channels

In the local logical basis $|0\rangle=|s\rangle$, $|1\rangle=|t\rangle$, the three pair-singlet projectors are

$$
\boxed{
P_{12}=\frac12(I+Z),
}
$$

$$
\boxed{
P_{13}=\frac12I+\frac{\sqrt3}{4}X-\frac14Z,
}
$$

$$
\boxed{
P_{14}=\frac12I-\frac{\sqrt3}{4}X-\frac14Z.
}
$$

They satisfy

$$
P_a^2=P_a,
$$

and

$$
\boxed{
P_{12}+P_{13}+P_{14}=\frac32I.
}
$$

Their Bloch vectors form a trine in the logical $X$-$Z$ plane.

---

## 3. Minimal reduced gluing Hamiltonian

Define an explicitly modelled shape-matching penalty by demanding equality of the three local pair-shape channels:

$$
\boxed{
H_{\rm glue}
=\sum_{a\in\{12,13,14\}}
\left(P_a^{(A)}-P_a^{(B)}\right)^2.
}
$$

This is positive semidefinite by construction.

Using the trine identities, it collapses exactly to

$$
\boxed{
H_{\rm glue}
=\frac32I
-\frac34\left(X_A X_B+Z_A Z_B\right).
}
$$

In the ordered basis

$$
\{|ss\rangle,|st\rangle,|ts\rangle,|tt\rangle\},
$$

the exact matrix is

$$
\boxed{
H_{\rm glue}
=
\begin{pmatrix}
\frac34&0&0&-\frac34\\
0&\frac94&-\frac34&0\\
0&-\frac34&\frac94&0\\
-\frac34&0&0&\frac34
\end{pmatrix}.
}
$$

Its spectrum is

$$
\boxed{
\operatorname{Spec}H_{\rm glue}
=\left\{0,\frac32,\frac32,3\right\}.
}
$$

---

## 4. Unique zero-mismatch state

The unique zero eigenstate is

$$
\boxed{
|\Phi^+\rangle
=\frac{|ss\rangle+|tt\rangle}{\sqrt2}.
}
$$

Therefore exact matching of all three reduced shape channels does **not** select a product of two locally sharp tetrahedra.

It selects a maximally entangled state of the two physical intertwiner qubits.

The Schmidt coefficients are

$$
\left(\frac1{\sqrt2},\frac1{\sqrt2}\right),
$$

so each node separately has

$$
\boxed{
S(A)=S(B)=1\ \text{bit}.
}
$$

This is the first genuinely network-level result of the new BQG emergence branch.

---

## 5. What happens to oriented volume

From the one-node exact result,

$$
Q=\frac{\sqrt3}{4}Y.
$$

Thus

$$
Q_A=\frac{\sqrt3}{4}Y_A,
\qquad
Q_B=\frac{\sqrt3}{4}Y_B.
$$

On the zero-mismatch state $|\Phi^+\rangle$,

$$
\boxed{
\langle Q_A\rangle=\langle Q_B\rangle=0.
}
$$

Moreover

$$
Q_A^2=Q_B^2=\frac3{16}I,
$$

so

$$
\boxed{
(\Delta Q_A)^2=(\Delta Q_B)^2=\frac3{16}.
}
$$

Each node therefore loses a sharp local orientation.

But the relative orientation is exact:

$$
\boxed{
Q_AQ_B|\Phi^+\rangle
=-\frac3{16}|\Phi^+\rangle.
}
$$

Hence

$$
\boxed{
\langle Q_AQ_B\rangle=-\frac3{16}.
}
$$

In the present local orientation convention, the two node volumes are perfectly anti-correlated.

So the reduced gluing model converts

$$
\text{local sharp orientation}
$$

into

$$
\boxed{
\text{sharp relational orientation between nodes}.
}
$$

---

## 6. Exact Bell spectrum of mismatch

The four Bell states diagonalize $H_{\rm glue}$:

$$
|\Phi^+\rangle=\frac{|ss\rangle+|tt\rangle}{\sqrt2},
\qquad E=0,
$$

$$
|\Phi^-\rangle=\frac{|ss\rangle-|tt\rangle}{\sqrt2},
\qquad E=\frac32,
$$

$$
|\Psi^+\rangle=\frac{|st\rangle+|ts\rangle}{\sqrt2},
\qquad E=\frac32,
$$

$$
|\Psi^-\rangle=\frac{|st\rangle-|ts\rangle}{\sqrt2},
\qquad E=3.
$$

Thus the complete two-node reduced problem is analytically solved.

---

## 7. Interpretation

The one-node result was

$$
\text{sharp local volume}
\Longleftrightarrow
\text{local pair-spectrum isotropy}.
$$

The new two-node result adds a qualitatively different layer:

$$
\boxed{
\text{exact inter-node shape matching}
\Longrightarrow
\text{maximal intertwiner entanglement}.
}
$$

and simultaneously

$$
\boxed{
\text{local orientation becomes uncertain}
\quad\text{while}\quad
\text{relative orientation becomes sharp}.
}
$$

This is a concrete finite realization of a relational principle: some geometric information can move from one-node observables into correlations between nodes.

---

## 8. Critical limitation

The result above is mathematically exact **for the stated reduced Hamiltonian**

$$
H_{\rm glue}=\sum_a(P_a^{(A)}-P_a^{(B)})^2.
$$

What is not yet proved is that this exact operator is the unique or fundamental BQG gluing Hamiltonian descending from the full graph-changing dynamics.

Therefore:

- the spectral result is **EXACT**;
- the use of this $H_{\rm glue}$ as physical BQG dynamics is presently **CANDIDATE**.

This distinction is mandatory.

---

## 9. Next gate

The next computationally elegant step is not a larger local Hilbert space but a chain of three reduced physical nodes:

$$
\dim(\mathcal H_{ABC}^{\rm red})=2^3=8.
$$

Use nearest-neighbor couplings

$$
H_3=H_{AB}+H_{BC}
$$

and solve exactly:

1. ground-state degeneracy;
2. pair mutual informations $I(A:B)$, $I(B:C)$, $I(A:C)$;
3. orientation correlations $\langle Q_AQ_B\rangle$, $\langle Q_BQ_C\rangle$, $\langle Q_AQ_C\rangle$;
4. whether relational distance becomes additive or nontrivial;
5. whether correlation geometry distinguishes nearest from next-nearest nodes.

This is the first minimal test in which an emergent graph distance can be compared to a correlation-defined distance.

---

## Reproduction

Run:

```bash
python scripts/bqg_two_node_reduced_gluing_gate.py
```

Expected final line:

```text
PASS
```
