# EPRL coherent-fusion scaling

Status: **finite Euclidean simplicity-map result on a regular tetrahedral semiclassical ray; not yet a Lorentzian continuum vertex test**.

## Question

The small-spin EPRL-type control showed that replacing the raw fusion map `F` by a locally isometrized map

\[
F_{iso}=F(F^\dagger F)^{-1/2}
\]

changes the resulting finite-spin vertex by several percent.  A naive universality criterion would demand

\[
F^\dagger F\to cI
\]

on the entire intertwiner Hilbert space.  The calculations below show that this criterion is too strong and physically misleading.

For `gamma=1/3`, use the admissible sequence

\[
(j,j^+,j^-)=(3/2,1,1/2),(3,2,1),(9/2,3,3/2),(6,4,2).
\]

## Full-Hilbert result: no global isometrization

Define

\[
G_j=F_j^\dagger F_j,
\qquad
\Delta_F=\frac{\|G_j-(\operatorname{tr}G_j/d_j)I\|_F}{\|G_j\|_F}.
\]

| j | `Delta_F` | sqrt(cond(G)) |
|--:|--:|--:|
| 3/2 | 0.1386195 | 1.2018504 |
| 3 | 0.2355229 | 1.3253084 |
| 9/2 | 0.2929473 | 1.4305936 |
| 6 | 0.3322650 | 1.5231858 |

Thus the complete fusion map does **not** approach a scalar isometry on the full intertwiner space over this sequence.

## Semiclassical coherent ray: the opposite behavior

Use a Livine--Speziale coherent tetrahedron with regular outward normals

\[
(1,1,1),\ (1,-1,-1),\ (-1,1,-1),\ (-1,-1,1)
\]

normalized to unit length.  Let `|C_j>` be its normalized invariant intertwiner coefficients.

Compare the normalized images

\[
\widehat{F_j C_j}
\quad\text{and}\quad
\widehat{F_{iso,j}C_j}.
\]

| j | fidelity raw/isometrized | infidelity |
|--:|--:|--:|
| 3/2 | 0.9958201984 | 4.1798016e-3 |
| 3 | 0.9975354173 | 2.4645827e-3 |
| 9/2 | 0.9992186666 | 7.8133343e-4 |
| 6 | 0.9997187018 | 2.8129815e-4 |

The prescription ambiguity on this geometric ray decreases by a factor about `14.86` from `j=3/2` to `j=6`.  A simple four-point power fit gives

\[
1-\mathcal F_{coh}\sim j^{-1.89},
\]

but this exponent is reported only as a finite-window diagnostic; the last points fall faster and no asymptotic exponent is claimed.

## Exact coherent-factorization identity

More importantly, the **raw** fusion map preserves the coherent geometric structure exactly in the tested sequence:

\[
\boxed{
F_j|C_j(\{n_f\})\rangle
\propto
|C_{j^+}(\{n_f\})\rangle\otimes
|C_{j^-}(\{n_f\})\rangle
}
\]

with numerical fidelity `1` to machine precision for all four spins.

This is not an accidental regular-tetrahedron fit.  It follows from the highest-spin leg embedding

\[
Y_\gamma|j,n\rangle
=|j^+,n\rangle\otimes|j^-,n\rangle,
\qquad j=j^++j^-,
\]

combined with the invariant projectors: the product of separate `+` and `-` invariant projectors is contained in the diagonally invariant sector, so the diagonal group average does not alter the final separately invariant projection.

Thus the physically relevant universality criterion is not global `F^dag F -> cI`.  It is preservation of the semiclassical geometric manifold and regulator-independence of observables supported on that manifold.

## Interpretation

The calculation resolves the apparent small-spin normalization ambiguity:

1. the raw group-projected simplicity map has an exact geometric property;
2. forcing a local Hilbert-space isometry distorts that geometric ray;
3. the distortion decreases rapidly with collective spin;
4. unitarity of the complete theory should be imposed on the Fock/history Hamiltonian evolution, not by demanding that every rectangular simplicity/fusion map be unitary by itself.

This matches the known large-spin role of EPRL fusion coefficients: they map semiclassical SO(3)/SU(2) intertwiner data to semiclassical left/right data.  It also keeps the main continuum target unchanged: the full Lorentzian vertex/constraint dynamics must still show regulator-independent large-spin GR behavior.
