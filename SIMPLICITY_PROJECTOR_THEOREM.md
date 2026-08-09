# Simplicity projector theorem

Status: **exact linear-algebraic statement for the finite Euclidean EPRL simplicity map; separates the physical constraint subspace from normalization conventions**.

## 1. Normalization-independent object

Let

\[
F:\mathcal H_j^{inv}\to
\mathcal H_{j^+}^{inv}\otimes\mathcal H_{j^-}^{inv}
\]

be an injective finite-spin EPRL fusion/simplicity map.  Its physical image is selected by the orthogonal projector

\[
\boxed{
P_{simp}=F(F^\dagger F)^{-1}F^\dagger.
}
\]

For any invertible change of basis/normalization `A` on the domain,

\[
F\to FA,
\]

one has exactly

\[
\boxed{P_{simp}[FA]=P_{simp}[F].}
\]

Therefore the raw map and the locally isometrized map

\[
F_{iso}=F(F^\dagger F)^{-1/2}
\]

define the **same simplicity subspace** even when their coordinate amplitudes differ appreciably at small spin.

A normalization-independent positive constraint is

\[
\boxed{H_{simp}=I-P_{simp}\ge0},
\]

with eigenvalue `0` on the simplicity image and `1` on its orthogonal complement.

## 2. Exact codimension for Euclidean EPRL, 0<gamma<1

Use

\[
j^\pm=\frac{1\pm\gamma}{2}j.
\]

For four equal boundary spins, the SU(2) intertwiner dimension is

\[
\dim\mathcal H_j^{inv}=2j+1.
\]

The unconstrained Spin(4)=SU(2)+ x SU(2)- intertwiner product has dimension

\[
\begin{aligned}
d_{BF}
&=(2j^++1)(2j^-+1)\\
&=[(1+\gamma)j+1][(1-\gamma)j+1].
\end{aligned}
\]

If `F` is injective, its image rank is

\[
d_{simp}=2j+1.
\]

Hence the forbidden BF codimension is exactly

\[
\boxed{
N_{forbidden}
=d_{BF}-d_{simp}
=(1-\gamma^2)j^2.
}
\]

The surviving fraction is

\[
\boxed{
f_{simp}(j,\gamma)
=\frac{2j+1}
{[(1+\gamma)j+1][(1-\gamma)j+1]}
\sim\frac{2}{(1-\gamma^2)j}.
}
\]

Thus for fixed nondegenerate `gamma` the gravity/simplicity image occupies a fraction `O(1/j)` of the unconstrained BF intertwiner product at large spin.

## 3. gamma=1/3 sequence used in the repository

For

\[
(j,j^+,j^-)
=(3/2,1,1/2),(3,2,1),(9/2,3,3/2),(6,4,2),(15/2,5,5/2),
\]

one gets

| j | BF dimension | simplicity rank | forbidden directions | surviving fraction |
|--:|--:|--:|--:|--:|
| 3/2 | 6 | 4 | 2 | 0.666667 |
| 3 | 15 | 7 | 8 | 0.466667 |
| 9/2 | 28 | 10 | 18 | 0.357143 |
| 6 | 45 | 13 | 32 | 0.288889 |
| 15/2 | 66 | 16 | 50 | 0.242424 |

The computed Gram matrices are positive on all five tested domain spaces, so the finite fusion maps are injective there.

## 4. Relation to coherent geometry

`EPRL_COHERENT_FUSION_SCALING.md` establishes a complementary fact: the raw highest-spin simplicity map preserves Livine--Speziale coherent geometry rays exactly in the tested sequence, while forcing a local isometry changes those rays slightly at finite spin.

These facts are compatible:

- the **image subspace** is normalization-independent;
- a choice of coordinates/measure inside that image is not;
- semiclassical geometry provides a physical criterion for comparing those coordinate prescriptions;
- full theory unitarity belongs to the Hermitian Fock/history evolution, not to the rectangular simplicity map itself.

## 5. Consequence for BF -> GR architecture

The clean finite formulation is therefore

\[
\boxed{
\text{BF Hilbert/dynamics}
\quad+\quad
H_{simp}=I-P_{simp}
\quad\longrightarrow\quad
\text{constrained gravity sector}.
}
\]

At large spin the simplicity constraint is not a weak perturbation of BF: it removes an asymptotically dominant fraction of the unconstrained intertwiner directions.

Different Immirzi parameters change the finite representation split and therefore the raw projector dimensions.  Regulator/universality tests across `gamma` must compare reconstructed physical observables after simplicity, not demand equality of raw projectors living in different representation spaces.
