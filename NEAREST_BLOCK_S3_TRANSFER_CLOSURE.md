# Nearest-block S3 transfer closure and the first genuine momentum symbol

Status: **exact symmetry/geometry reduction of the remaining interblock calculation.  The six transfer amplitudes themselves remain microscopic Peter-Weyl outputs.**

The onsite depth-two kernel cannot by itself produce spatial momentum.  A true `C(omega,k)` requires amplitudes that move collective metric information between neighboring coarse tetrahedral blocks.

On the 16-cell seed the 16 coarse tetrahedra form the dual hypercube `Q4`: two coarse tetrahedra are neighbors when they differ in one sign choice and therefore share one triangular face.  Recursive PL refinement supplies the continuum sequence; the seed is the exact local incidence prototype.

---

## 1. Edge representation of a face-sharing pair

Take two neighboring tetrahedra sharing the face with vertices `(1,2,3)`.  Call their opposite apex vertices `A` and `B`.

Each six-edge carrier splits naturally into two triples:

```text
A_i : three apex-to-face edges
F_i : three edges of the shared face
```

and analogously on the second tetrahedron.

The stabilizer of the shared triangular face is `S3`.  Both triples carry its three-dimensional permutation representation

\[
\mathbf3=A_1\oplus E.
\]

Therefore each block edge carrier restricts as

\[
\boxed{
\mathbf6|_{S_3}
=(A_1\oplus E)_{apex}
\oplus
(A_1\oplus E)_{face}.
}
\]

The multiplicity of both `A1` and `E` is two.

---

## 2. Exact commutant count

An `S3`-equivariant `3x3` map between permutation triples has the form

\[
\boxed{
X=\alpha I+\beta(J-I),
}
\]

with two scalar coefficients.

Before reciprocity a general source-to-target six-edge cross map contains four such blocks:

```text
apex -> apex
apex -> face
face -> apex
face -> face
```

and therefore eight real orbit coefficients.

For the reciprocal parity-even quadratic kernel the forward/backward pair enters through the Hermitian/even combination.  In the shared-face irrep basis this is simply a real symmetric `2x2` matrix on the multiplicity space for each irrep:

\[
\boxed{
T_{A_1}^{even}
=\begin{pmatrix}a_1&m_1\\m_1&f_1\end{pmatrix},
}
\]

\[
\boxed{
T_E^{even}
=\begin{pmatrix}a_E&m_E\\m_E&f_E\end{pmatrix}\otimes I_E.
}
\]

Hence one face-sharing nearest-neighbor transfer is completely determined by

\[
\boxed{3+3=6}
\]

real scalar functions of frequency / shell depth.

This is the interblock analogue of the onsite `A1+E+T2` reduction.

---

## 3. One neighbor pair determines all four local directions

A tetrahedron has four faces and hence four nearest coarse neighbors.

The full tetrahedral `S4` action is transitive on these four faces.  Once the exact Peter-Weyl transport/relabeling representation `U_g` is fixed, the remaining nearest-neighbor transfers are generated from one canonical face pair:

\[
\boxed{
T_{g\delta}=U_gT_\delta U_g^{-1}.
}
\]

Thus the expensive microscopic calculation need not independently discover 24 or 36 arbitrary tensor entries for every direction.

It needs:

1. one canonical shared-face pair;
2. the six reciprocal `S3` transfer amplitudes;
3. exact `S4` transport to the other three faces;
4. a locality control at the next block separation.

---

## 4. Exact tetrahedral displacement moments

In a locally reconstructed regular metric frame choose the four unit face-normal / neighbor directions

\[
\mathbf n_1=\frac{(1,1,1)}{\sqrt3},
\]

\[
\mathbf n_2=\frac{(1,-1,-1)}{\sqrt3},
\]

\[
\mathbf n_3=\frac{(-1,1,-1)}{\sqrt3},
\]

\[
\mathbf n_4=\frac{(-1,-1,1)}{\sqrt3}.
\]

They satisfy

\[
\sum_a\mathbf n_a=0,
\]

and the exact second moment

\[
\boxed{
\sum_{a=1}^4n_a^in_a^j=\frac43\delta^{ij}.
}
\]

Therefore an equal scalar nearest-neighbor hopping stencil has an isotropic leading `k^2` symbol automatically.

The fourth moment is not fully rotationally isotropic:

\[
\sum_a(\mathbf k\cdot\mathbf n_a)^4
=\frac49\left[
\sum_i k_i^4+6\sum_{i<j}k_i^2k_j^2
\right].
\]

Equivalently, with

\[
Q_4^{cub}(\mathbf k)
=\sum_i k_i^4-\frac35(k^2)^2,
\]

\[
\boxed{
\sum_a(\mathbf k\cdot\mathbf n_a)^4
=\frac45(k^2)^2-\frac89Q_4^{cub}(\mathbf k).
}
\]

Thus the tetrahedral stencil supplies exactly the expected pattern:

```text
second derivative -> isotropic
fourth derivative -> isotropic + cubic/tetrahedral memory
```

without needing an anisotropic leading light cone.

---

## 5. Low-momentum moment expansion

For reciprocal nearest-neighbor block transfer `T_delta`, the even symbol is schematically

\[
C^{nn}(\mathbf k)
=\sum_\delta
\left[
T_\delta e^{i\mathbf k\cdot\mathbf r_\delta}
+T_\delta^\dagger e^{-i\mathbf k\cdot\mathbf r_\delta}
\right].
\]

For a real reciprocal even sector this becomes a cosine moment expansion:

\[
C^{nn}(\mathbf k)
=C^{nn}(0)
-\sum_\delta T_\delta^{even}(\mathbf k\cdot\mathbf r_\delta)^2
+\frac1{12}\sum_\delta T_\delta^{even}(\mathbf k\cdot\mathbf r_\delta)^4
+O(k^6).
\]

The exact coefficients depend on the convention used to count forward/backward neighbors; the derivative tensors themselves are unambiguous once that convention is frozen.

The second and fourth moment tensors are therefore direct finite sums of the six microscopic transfer amplitudes transported over the four tetrahedral directions.

No global periodic cubic lattice is required.

---

## 6. Why this produces the complete six-Wilson TT sector

A scalar equal-hopping limit yields only a restricted isotropic-plus-cubic pattern.

The actual Peter-Weyl transfer acts nontrivially on the two `A1/E` multiplicity spaces and is reoriented across the four faces.  After metric reconstruction and TT projection these internal matrices generate the complete six-dimensional parity-even quartic TT quotient described in `S4_TT_QUARTIC_COMPLETE_BASIS.md`.

The correct computational chain is therefore

\[
\boxed{
\text{one shared-face Peter--Weyl transfer}
\to 6\ S_3\text{ amplitudes}
\to 4\ S_4\text{-related neighbor matrices}
\to k^2,k^4\text{ moment tensors}
\to K_{TT}
\to 6\text{ physical quartic Wilson coefficients}.
}
\]

---

## 7. Locality control

Nearest-neighbor truncation is not assumed to be exact.

At least one next-separation class must be computed to bound

\[
\frac{\|T_{r>1}\|}{\|T_{nn}\|}.
\]

If the ratio does not decrease under refinement/blocking, the nearest-neighbor symbol is not a controlled effective description and the quartic prediction must remain open.

If it does decrease, further classes become a bounded finite-size/systematic uncertainty rather than new fit parameters.

---

## 8. The resulting finite production programme

The former phrase “do recursive RG until something converges” is now replaced by a concrete production graph:

```text
A. onsite full-E depth-two return                  [currently sharded]
B. canonical shared-face full-E transfer           [6 S3 amplitudes]
C. S4 transport to four neighbor directions        [exact representation]
D. next-separation locality control                 [finite falsifier]
E. second-moment tensor                             [leading cone test]
F. fourth-moment tensor                             [quartic TT sector]
G. full six-Wilson extractor 100/110/111/120        [exact inverse]
H. refinement/regulator extrapolation               [frozen]
I. one absolute scale                               [derive or one datum]
J. blind real-physics comparison                    [phase/delay/polarization]
```

This is the minimal honest path from the local 8.43% precursor to a physical momentum-dependent gravitational prediction.
