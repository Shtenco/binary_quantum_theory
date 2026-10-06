# BQG Asymptotic Mutual-Information Geometry

**Date:** 2026-10-06  
**Status:** EXACT reduction + analytic XX/Fisher-Hartwig asymptotics for the current candidate reduced chain

---

## 1. Starting point

The current many-node reduced BQG gluing model is locally unitarily equivalent to the zero-field open XX chain,

$$
H_M\simeq
\frac32(M-1)I
-\frac34\sum_{i=1}^{M-1}(X_iX_{i+1}+Y_iY_{i+1}).
$$

In the thermodynamic bulk limit the Jordan-Wigner map gives a half-filled free-fermion sea.

The one-body correlator is exact:

$$
\boxed{
C_f(r)
=\langle c_0^\dagger c_r\rangle
=\frac{\sin(\pi r/2)}{\pi r},
\qquad r\neq0.
}
$$

Thus the fermionic correlator alone is $O(r^{-1})$, but the physical logical-spin transverse correlator contains the Jordan-Wigner string and must not be identified with $C_f(r)$.

---

## 2. Logical-spin correlators

At zero field and half filling,

$$
\langle X_0X_r\rangle
=\langle Y_0Y_r\rangle
\equiv C_x(r),
$$

and

$$
\boxed{
C_z(r)
=\langle Z_0Z_r\rangle
=-4|C_f(r)|^2
=-\frac{4\sin^2(\pi r/2)}{\pi^2r^2}.
}
$$

Therefore

$$
C_z(r)=0\quad(r\;\text{even}),
$$

and

$$
C_z(r)=-\frac{4}{\pi^2r^2}\quad(r\;\text{odd}).
$$

The transverse correlator has the exact Toeplitz-determinant representation

$$
\boxed{
C_x(r)
=\det_{1\le j,k\le r}G_{j-k-1},
}
$$

with

$$
G_n=\frac{2\sin(\pi n/2)}{\pi n},
\qquad G_0=0.
$$

The Fisher-Hartwig asymptotics of this determinant gives

$$
\boxed{
C_x(r)
=A_x\,r^{-1/2}\left[1+O(r^{-2})\right],
}
$$

up to the standard subleading parity/oscillatory corrections.

For the present Pauli normalization, numerical evaluation of the exact determinant approaches

$$
A_x\approx0.58835.
$$

The exponent $1/2$, not the fitted amplitude, is the structurally important quantity.

---

## 3. Exact two-node reduced density matrix at separation r

Translation invariance, zero one-site magnetization and U(1) symmetry give

$$
\boxed{
\rho_{0r}
=\frac14\left[
I\otimes I
+C_x(r)(X\otimes X+Y\otimes Y)
+C_z(r)Z\otimes Z
\right].
}
$$

Hence its four eigenvalues are

$$
\boxed{
\lambda_{1,2}
=\frac{1+C_z}{4},
}
$$

$$
\boxed{
\lambda_{\pm}
=\frac{1-C_z\pm2C_x}{4}.
}
$$

Each single-node state is maximally mixed,

$$
\rho_0=\rho_r=\frac{I}{2},
\qquad S(\rho_0)=S(\rho_r)=1\ \text{bit}.
$$

Therefore the exact two-node mutual information is

$$
\boxed{
I(r)
=2+\sum_{a=1}^{4}\lambda_a(r)\log_2\lambda_a(r).
}
$$

This is the exact thermodynamic-limit answer once the Toeplitz determinant $C_x(r)$ is supplied.

---

## 4. Analytic large-r expansion

For large $r$,

$$
C_x(r)=O(r^{-1/2}),
\qquad
C_z(r)=O(r^{-2}).
$$

Expanding the entropy about the maximally mixed pair state $I_4/4$ gives

$$
\boxed{
I(r)
=\frac{C_x(r)^2}{\ln2}
+\frac{C_z(r)^2}{2\ln2}
+O(C_x^4,C_x^2C_z,C_z^3).
}
$$

Since $C_x^2=O(r^{-1})$ while $C_z^2=O(r^{-4})$,

$$
\boxed{
I(r)
=\frac{A_x^2}{\ln2}\frac1r
+O(r^{-2}).
}
$$

Define

$$
\kappa\equiv\frac{A_x^2}{\ln2}.
$$

With $A_x\approx0.58835$,

$$
\boxed{
\kappa\approx0.4994,
}
$$

so numerically

$$
\boxed{
I(r)\approx\frac{0.50}{r}\ \text{bit}
}
$$

in the asymptotic bulk regime.

The reproduction gate gives, for example,

$$
rI(r)\to0.5
$$

from both even and odd subsequences.

**Central asymptotic result:**

$$
\boxed{
I(r)\propto r^{-1}.
}
$$

---

## 5. Consequence for candidate information distances

This result discriminates distance maps.

### 5.1 Negative-log map

Suppose

$$
d_{\log}(r)
=-\ell_*\ln\frac{I(r)}{I_*}.
$$

Since $I(r)\sim\kappa/r$,

$$
\boxed{
d_{\log}(r)
=\ell_*\ln r+\text{constant}+o(1).
}
$$

Therefore a negative-log mutual-information map does **not** reproduce the linear graph distance of the present critical chain.

This is a useful falsification result.

### 5.2 Inverse-information map

If instead

$$
d_{\rm inv}(r)
=\ell_*\frac{I_*}{I(r)},
$$

then

$$
\boxed{
d_{\rm inv}(r)
\sim\frac{\ell_*I_*}{\kappa}\,r.
}
$$

Thus an inverse-information map can reproduce a linear asymptotic distance in this specific model.

However this does **not** prove that $1/I$ is the fundamental BQG distance. Choosing a map after seeing the answer would be post-hoc unless an independent principle selects it.

---

## 6. Stronger interpretation: distance map depends on correlation phase

The calculation exposes a general issue.

For a gapped phase with

$$
I(r)\sim e^{-r/\xi},
$$

a logarithmic map naturally gives

$$
-\ln I(r)\sim r/\xi.
$$

But the current reduced chain is critical and gapless. Its correlations decay algebraically:

$$
I(r)\sim r^{-1}.
$$

Hence

$$
-\ln I(r)\sim\ln r.
$$

Therefore no universal claim of the form

$$
d\propto-\ln I
$$

can be made across both critical and gapped regimes without additional structure.

A genuine BQG distance must either:

1. be derived from an information metric rather than chosen ad hoc;
2. depend on the RG/correlation regime;
3. use a path/additive construction built from local information weights;
4. or emerge from a different observable than raw pair mutual information.

---

## 7. What is proved here

For the current candidate 1D reduced BQG gluing Hamiltonian:

1. the thermodynamic bulk is exactly a half-filled free-fermion XX chain;
2. $C_f(r)=\sin(\pi r/2)/(\pi r)$ exactly;
3. $C_z(r)=-4|C_f(r)|^2$ exactly;
4. $C_x(r)$ is an exact Toeplitz determinant with Fisher-Hartwig asymptotic $r^{-1/2}$;
5. the exact two-node density matrix is fixed by $C_x,C_z$;
6. the mutual information obeys
   $$I(r)\sim\kappa/r;$$
7. therefore $-\ln I(r)\sim\ln r$, not $r$;
8. $1/I(r)\sim r$, but interpreting this as physical distance remains a candidate choice, not a derivation.

---

## 8. New frontier

The next non-post-hoc problem is now sharper:

$$
\boxed{
\text{derive the distance functional from BQG structure itself}
}
$$

rather than choosing $f(I)$ after observing $I(r)$.

The cheapest discriminating routes are:

- information-geometric/Bures/Fisher distance between local reduced states;
- additive edge length from conditional mutual information;
- modular-Hamiltonian response;
- graph geodesic reconstructed from local correlation weights;
- comparison of critical and deliberately gapped deformations of the same reduced gluing model.

The last option is especially important: if a controlled mass/gap deformation changes

$$
I(r):\quad r^{-1}\to e^{-r/\xi},
$$

while the underlying graph geometry stays one-dimensional, then any proposed universal distance map can be falsified immediately.

---

## Reproduction

Run:

```bash
python scripts/bqg_mutual_information_asymptotic_gate.py
```

The gate evaluates exact Toeplitz determinants at selected separations, verifies

$$
C_x(r)\propto r^{-1/2},
$$

and checks

$$
I(r)\propto r^{-1},
\qquad rI(r)\to\text{nonzero constant}.
$$
