# Euclidean sine normalization match

Status: **conditional analytic combinatorial match to the original Thiemann tetrahedral trace convention**.

This calculation fixes the common real normalization of the repository's physical sine-order Euclidean operator without fitting an HDA residual.

---

## 1. Continuum / tetrahedral reference

For one tetrahedron `Delta`, Thiemann's Euclidean regularization is

\[
H^E_\Delta[N]
=-\frac{2N_v}{3i\hbar}
\epsilon^{ijk}
\operatorname{Tr}
\left(
 h_{\alpha_{ij}}
 h_{e_k}[h_{e_k}^{-1},V]
\right).
\]

The six nonzero permutations of `epsilon^{ijk}` pair as

\[
(123)-(213),
\quad
(231)-(321),
\quad
(312)-(132).
\]

Since reversing `i,j` reverses the small loop,

\[
h_{\alpha_{ji}}=h_{\alpha_{ij}}^{-1},
\]

the epsilon sum is exactly three cyclic forward-minus-reverse loop contributions.

---

## 2. Repository combinatorics

For each omitted face / tetrahedron, `oriented_specs(v)` emits exactly the three cyclic specs

```text
(v,a,b,c)
(v,b,c,a)
(v,c,a,b).
```

For each spec, `T_sequences` already contains the forward/reverse loop difference

```text
pf - pr
```

together with the volume commutator ordering.

Therefore the repository has already performed the `6 -> 3 forward-minus-reverse` epsilon pairing. No additional factor of two is introduced when matching the oriented tetrahedral sum.

The physical Hermitian structural ordering is

\[
H_{sine}^{raw}
=\frac{O-O^\dagger}{2i},
\]

where `O` denotes the complete three-cyclic oriented raw trace sum for the tetrahedral/node contribution.

---

## 3. Symmetric canonical operator

The unsymmetrized canonical coefficient is

\[
c_E=-\frac{2}{3i\hbar}.
\]

Because `c_E` is purely imaginary, symmetric completion gives

\[
\frac12\left(c_EO+(c_EO)^\dagger\right)
=\frac{c_E}{2}(O-O^\dagger).
\]

Comparing with

\[
H_{sine}^{raw}=\frac{O-O^\dagger}{2i}
\]

yields

\[
\boxed{
H_E^{canonical}
=n_E H_{sine}^{raw},
\qquad
n_E=c_E i=-\frac{2}{3\hbar}.
}
\]

Thus, in dimensionless `hbar=1` structural units,

\[
\boxed{n_E=-2/3.}
\]

A common overall sign of the total Hamiltonian constraint can of course be reversed without changing its zero set; the important result is the relative normalization inherited by all nested `K=[V,H_E]` terms.

---

## 4. Consequent Lorentzian normalization

Using

\[
K^{canonical}
=-\frac{1}{i\hbar}[V,H_E^{canonical}]
\]

and the two-K Lorentzian triple gives

\[
|g_R|
=\frac{8n_E^2}{\hbar^5}
=\boxed{\frac{32}{9\hbar^7}}
\]

relative to the phase-completed repository raw K-K-V block.

For `hbar=1` structural units,

\[
\boxed{|g_R|=32/9\simeq3.555555555555556.}
\]

The exact local phase-completed logical coefficient was

\[
c_L=1.3389293521464034.
\]

Therefore the normalized one-body structural magnitude is

\[
\boxed{
\frac{32}{9}c_L
=4.760637696520545\ldots
}
\]

per logical node, before the general-real-`beta` external coefficient convention and before setting an absolute physical unit.

For the ideal oriented 16-cell mirror pair, the corresponding structural splitting magnitude becomes

\[
\boxed{
\frac{32}{9}\times42.84573926868491
=152.34040628865745\ldots
}
\]

in `hbar=1` raw canonical units.

These are **not eV/Joule predictions**. They are normalized dimensionless operator coefficients.

---

## 5. Assumptions that must remain explicit

The match assumes:

1. the repository's auxiliary fundamental trace uses the same standard SU(2) fundamental trace convention as the reference tetrahedral formula;
2. `oriented_specs` represents the four oriented tetrahedra/faces with its recorded signs;
3. `T_sequences` forward/reverse path pair is the same `alpha_ij` / `alpha_ji` pairing used in the epsilon reduction;
4. no additional continuum coupling constant has been hidden inside the dimensionless volume operator.

These assumptions are testable code/convention statements. If any is changed, this normalization certificate must be recomputed.

---

## 6. Why this is scientifically preferable to an HDA fit

The normalization is fixed upstream by the Euclidean classical limit. The Lorentzian magnitude then follows quadratically through

\[
K\propto[V,H_E].
\]

The later two-node `H_E+H_L+R_Q` HDA calculation therefore receives a fixed relative Lorentzian magnitude. It is not allowed to tune `g_R` to minimize the commutator residual.

That turns the complete Lorentzian HDA calculation into a genuine falsifier.
