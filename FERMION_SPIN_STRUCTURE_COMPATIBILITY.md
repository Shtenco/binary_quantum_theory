# Fermion compatibility of the selected global geometry

Status: **exact topological prerequisite; not a derivation of the Standard Model matter sector.**

The q=2 geometric construction selects a global spatial slice in the PL homeomorphism class of `S3`.  This has an important matter-sector consequence: globally defined spin-1/2 fields are topologically allowed, and there is no multiplicity of inequivalent spatial spin structures.

---

## 1. S3 is spin

The three-sphere is the Lie group

\[
S^3\simeq SU(2).
\]

Every Lie group is parallelizable.  Therefore its tangent bundle is trivial and in particular

\[
\boxed{w_2(S^3)=0.}
\]

Hence `S3` admits a spin structure.

Equivalently, the canonical left-invariant frame on `SU(2)` gives a global orthonormal triad and its spin lift.

---

## 2. The spin structure is unique

On an oriented spin manifold, equivalence classes of spin structures form an affine space/torsor over

\[
H^1(M,\mathbb Z_2).
\]

For `S3`,

\[
H^1(S^3,\mathbb Z_2)=0.
\]

Therefore

\[
\boxed{\#\operatorname{SpinStructures}(S^3)=1.}
\]

No additional discrete spin-sector choice is required by the selected spatial topology.

---

## 3. Direct mod-2 certificate on the 16-cell boundary

The seed simplicial complex has

```text
C0:  8 vertices
C1: 24 edges
C2: 32 triangles
C3: 16 tetrahedra.
```

Over `GF(2)` the simplicial boundary maps have ranks

\[
\boxed{
\operatorname{rank}\partial_1=7,
\quad
\operatorname{rank}\partial_2=17,
\quad
\operatorname{rank}\partial_3=15.
}
\]

The chain identities hold exactly,

\[
\partial_1\partial_2=0,
\qquad
\partial_2\partial_3=0.
\]

Hence the mod-2 Betti numbers are

\[
\boxed{(b_0,b_1,b_2,b_3)=(1,0,0,1).}
\]

In particular `b1=0`, giving the required `H^1(S3,Z2)=0` certificate directly on the finite seed.

Barycentric subdivision preserves the PL topology, so this spin-structure count is unchanged by the frozen recursive refinement.

---

## 4. 3+1 history

For a product-like smooth scaling window

\[
\mathcal M\simeq S^3\times\mathbb R,
\]

the spatial spin structure extends along the contractible time factor.  Thus ordinary four-dimensional Dirac/Weyl spinor bundles are globally compatible with the candidate history topology.

This is a **compatibility statement**, not a derivation that the microscopic theory necessarily contains dynamical fermions.

---

## 5. Relation to the existing SU(2) geometry

The appearance of `SU(2)` in the Peter-Weyl geometric sector and the fact that `Spin(3)=SU(2)` make spinor kinematics natural on each spatial slice.

This must not be confused with deriving the electroweak `SU(2)` gauge group.  In the current theory the established `SU(2)` role is spatial/spin geometry.

Any internal gauge `SU(2)` acting on matter would require a separate microscopic derivation.

---

## 6. What this closes and what it does not

### Closed

- selected spatial topology is spin;
- the seed has `H^1(Z2)=0` directly;
- the spatial spin structure is unique;
- spin-1/2 fields can be globally defined on the `S3` slice and its product-like 3+1 history.

### Not derived

- existence/number of fermion species;
- chirality of the physical matter spectrum;
- color `SU(3)` or electroweak internal gauge groups;
- three generations;
- Yukawa matrices;
- particle masses or mixing angles;
- anomaly cancellation.

Those remain genuine matter-sector bottlenecks and must not be inferred from the gravitational `E/T2` split or Peter-Weyl eigenvalues.

---

## 7. Matter-sector next gate

The next legitimate step is not mass numerology.  It is to derive a microscopic fermionic carrier/Grassmann or equivalent spinorial excitation and show that its long-distance kinetic operator approaches a chiral/Dirac principal symbol on the same emergent tetrad:

\[
\boxed{
D_{IR}\sim i e_a^{\ \mu}\gamma^a\nabla_\mu.
}
\]

Only after such a carrier exists does it make sense to ask which internal gauge representations and mass-generating operators are dynamically selected.
