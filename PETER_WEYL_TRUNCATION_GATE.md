# Peter-Weyl truncation gate

Status: **exact finite SU(2) link-algebra result; replaces the special vector-5 interpretation by a systematic representation cutoff**.

## 1. Link Hilbert space

Use the electric/Peter--Weyl basis

\[
|j,m_L,m_R\rangle,
\qquad
\mathcal H^{J_{max}}_{link}
=\bigoplus_{j=0,1/2,\ldots,J_{max}}V_j^L\otimes V_j^R.
\]

Its exact dimension is

\[
\boxed{
D(J_{max})
=\sum_{j=0}^{J_{max}}(2j+1)^2
=\frac{(N+1)(N+2)(2N+3)}6,
\quad N=2J_{max}.
}
\]

Examples:

| Jmax | dimension | minimum binary qubits for generic encoding |
|--:|--:|--:|
| 1/2 | 5 | 3 |
| 1 | 14 | 4 |
| 3/2 | 30 | 5 |
| 2 | 55 | 6 |

Thus the previously identified five-state vector quantum link is exactly the first representation truncation

\[
\boxed{j=0\oplus j=1/2}.
\]

The next collective truncation adds `j=1` and has only fourteen states.

## 2. Exact fundamental holonomy operator

For the normalized Peter--Weyl basis, multiplication by the fundamental representation has matrix elements

\[
\boxed{
U_{ab}|jmn\rangle
=\sum_{J=j\pm1/2}
\sqrt{\frac{2j+1}{2J+1}}
C^{JM}_{jm,\frac12 a}
C^{JN}_{jn,\frac12 b}
|JMN\rangle,
}
\]

with terms beyond `Jmax` removed by the cutoff.

This automatically implements representation growth

\[
0\leftrightarrow\frac12\leftrightarrow1\leftrightarrow\frac32\cdots
\]

rather than introducing a separate ad-hoc collective-link rule.

## 3. Gauge covariance survives the cutoff exactly

Explicit matrices were constructed for `Jmax=1/2` and `Jmax=1`.  They satisfy

\[
[L^a,U_{mn}]
=(J^a_{1/2})_{pm}U_{pn},
\]

\[
[R^a,U_{mn}]
=U_{mp}(J^a_{1/2})_{pn}
\]

with maximum residual below

\[
\boxed{1.5\times10^{-16}}.
\]

For `Jmax=1`, the electric Casimir spectrum is

\[
0\;(1\times),
\qquad
3/4\;(4\times),
\qquad
2\;(9\times),
\]

exactly corresponding to `j=0,1/2,1`.

## 4. Truncation noncommutativity is confined to the cutoff wall

In the untruncated coordinate representation the multiplication operators commute as functions of the group.  Finite representation truncation produces a quantum-link commutator.  Sector-resolved calculation gives:

### Jmax=1/2

\[
[U,U]P_{j=0}=0,
\qquad
\|[U,U]P_{j=1/2}\|_{max}=1/\sqrt2.
\]

### Jmax=1

\[
[U,U]P_{j=0}=0,
\qquad
[U,U]P_{j=1/2}=O(10^{-16}),
\]

while the defect is entirely on `j=1`.

### Jmax=3/2 and 2

The same pattern continues: every sector strictly below `Jmax` has commutator residual at machine precision, while the entire cutoff defect is supported on `j=Jmax`.

Hence

\[
\boxed{
[U_{ab},U_{cd}]P_j=0
\quad\text{for }j<J_{max}
}
\]

in the explicit tests.

## 5. Finite-word cutoff theorem

The reason is Clebsch--Gordan locality in representation space.  One fundamental holonomy changes spin by at most `1/2`.  Therefore a word of length `r` starting in spin `j` cannot reach above

\[
j+r/2.
\]

Consequently, whenever

\[
\boxed{
j_{in}+r/2\le J_{max}},
\]

all intermediate representations required by the untruncated product remain inside the retained Peter--Weyl space.  The finite truncation therefore reproduces that word algebra exactly on the stated input sector.

This gives a very cheap regulator criterion: for a local Hamiltonian with bounded holonomy word depth, physical spin support only needs a finite additive margin below `Jmax`.  Cutoff contamination is a boundary-in-representation-space effect, not a uniform deformation of all low-spin states.

## 6. Consequence for the gravity programme

The microscopic carrier can now be written systematically as

\[
\boxed{
\mathcal H_{link}^{J_{max}}
=\bigoplus_{j\le J_{max}}V_j^L\otimes V_j^R,
}
\]

with exact Gauss symmetry at every finite cutoff.  The five-state model is its smallest geometrogenesis truncation; `Jmax=1` is the first truncation containing the non-scalar spin-1 tetrahedral volume sector.

A continuum/collective run should therefore increase `Jmax` while keeping the support of measured low-energy states separated from the cutoff wall.  Regulator universality can be tested by moving the wall outward without changing the frozen Hamiltonian coefficients.
