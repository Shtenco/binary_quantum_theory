# BQG Many-Node Reduced Model: Exact XX / Free-Fermion Mapping

**Date:** 2026-10-06  
**Status:** EXACT for the current candidate reduced nearest-neighbor Hamiltonian

---

## 1. Starting point

The current reduced physical-node chain is

$$
\boxed{
H_M
=\sum_{i=1}^{M-1}
\left[
\frac32 I
-\frac34\left(X_iX_{i+1}+Z_iZ_{i+1}\right)
\right].
}
$$

Each site is not a microscopic spin but the two-dimensional SU(2)-invariant intertwiner sector of one four-spin node.

---

## 2. Local unitary rotation

Apply the same $\pi/2$ rotation about the logical $X$ axis on every site.

Under this rotation,

$$
X\to X,
\qquad
Z\to \pm Y,
$$

and the sign drops out of the nearest-neighbor product.

Therefore $H_M$ is unitarily equivalent to

$$
\boxed{
H_M^{XX}
=\frac32(M-1)I
-\frac34\sum_{i=1}^{M-1}
\left(X_iX_{i+1}+Y_iY_{i+1}\right).
}
$$

So the present reduced BQG chain is exactly the open XX spin chain, up to an additive constant and local basis rotation.

---

## 3. Jordan-Wigner reduction

Using

$$
X_iX_{i+1}+Y_iY_{i+1}
=2\left(c_i^\dagger c_{i+1}+c_{i+1}^\dagger c_i\right),
$$

the Hamiltonian becomes

$$
\boxed{
H_M
=\frac32(M-1)I
-\frac32\sum_{i=1}^{M-1}
\left(c_i^\dagger c_{i+1}+c_{i+1}^\dagger c_i\right).
}
$$

Thus the many-node reduced model is exactly free fermionic.

No exponential diagonalization is needed to obtain its spectrum.

---

## 4. Exact single-particle spectrum

For an open chain,

$$
k_n=\frac{n\pi}{M+1},
\qquad n=1,\ldots,M.
$$

The single-particle energies are

$$
\boxed{
\varepsilon_n=-3\cos\left(\frac{n\pi}{M+1}\right).
}
$$

Every many-body eigenvalue is

$$
\boxed{
E
=\frac32(M-1)
+\sum_{n=1}^{M}\varepsilon_n N_n,
\qquad N_n\in\{0,1\}.
}
$$

This gives the full $2^M$ spectrum from only $M$ one-particle levels.

---

## 5. Exact parity effect

For odd $M$, there is an exact zero mode:

$$
n_0=\frac{M+1}{2},
$$

because

$$
k_{n_0}=\frac\pi2,
\qquad
\varepsilon_{n_0}=0.
$$

Therefore the ground state is exactly twofold degenerate:

$$
\boxed{
M\ \text{odd}\Rightarrow g_0=2.
}
$$

This explains the twofold degeneracy found earlier for the three-node chain without any further diagonalization.

For even $M$, no zero mode exists and the ground state is unique:

$$
\boxed{
M\ \text{even}\Rightarrow g_0=1.
}
$$

---

## 6. Exact finite-size gap

For even $M$,

$$
\boxed{
\Delta_M^{\rm even}
=3\sin\left(\frac{\pi}{2(M+1)}\right).
}
$$

For odd $M$, after factoring out the exact ground-state zero-mode degeneracy, the first nonzero excitation gap is

$$
\boxed{
\Delta_M^{\rm odd}
=3\sin\left(\frac{\pi}{M+1}\right).
}
$$

Hence

$$
\boxed{
\Delta_M\to0
\quad\text{as}\quad
O(M^{-1}).
}
$$

The candidate reduced chain is therefore gapless in the thermodynamic limit.

---

## 7. Why this matters for the emergence program

The result changes the computational strategy completely.

The naive approach would diagonalize matrices of size

$$
2^M\times2^M.
$$

The exact mapping replaces this with a free one-particle problem of size

$$
M\times M.
$$

More importantly, it reveals that the current one-dimensional candidate gluing model is a critical free-fermion system rather than a generic interacting many-body model.

That means the next questions should be answered through exact correlation functions and asymptotics, not brute-force diagonalization.

---

## 8. Immediate next targets

The next exact calculations are:

1. derive the fermionic two-point function $\langle c_i^\dagger c_j\rangle$;
2. derive logical $X,Z,Y$ correlators as a function of separation $r$;
3. extract the asymptotic decay law of inter-node mutual information $I(r)$;
4. define a correlation length or prove its absence at criticality;
5. compare the same local node physics on chain, ring, square-lattice and branching graphs;
6. determine whether an emergent dimension estimator tracks the connectivity dimension or produces a nontrivial quantum-geometric value.

---

## 9. Important limitation

The mapping is exact, but only for the present candidate reduced gluing Hamiltonian.

It does **not** prove that fundamental BQG is the XX chain.

What it proves is:

$$
\boxed{
\text{current reduced shape-matching ansatz}
\equiv
\text{free-fermion XX model}.
}
$$

This equivalence is useful precisely because it makes the candidate easy to falsify and scale.

---

## Reproduction

Run:

```bash
python scripts/bqg_many_node_xx_mapping_gate.py
```

The script checks the exact free-fermion spectrum, ground-state parity effect and gap formulas against explicit spin-chain diagonalization for $M=2,3,4,5,6$.

Expected final line:

```text
PASS
```
