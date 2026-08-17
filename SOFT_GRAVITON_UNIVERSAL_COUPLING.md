# Massless spin-2 consistency -> universal gravitational coupling

Status: **conditional infrared S-matrix theorem; microscopic realization in the candidate history remains a gate.**

Once an infrared theory contains a Lorentz-invariant interacting massless helicity-2 particle with the usual pole structure, soft-graviton gauge consistency imposes universal coupling to energy-momentum.  This supplies the correct bridge from a massless graviton sector to the equivalence-principle/common-metric interpretation.

The classic source is S. Weinberg, *Photons and Gravitons in S-Matrix Theory: Derivation of Charge Conservation and Equality of Gravitational and Inertial Mass*, Physical Review 135 (1964) B1049, DOI `10.1103/PhysRev.135.B1049`.

---

## 1. Soft graviton factor

For a soft graviton momentum `q`, the leading external-leg pole has the form

\[
\mathcal M_{n+1}
\sim
\left[
\sum_i \eta_i\kappa_i
\frac{p_i^\mu p_i^\nu\varepsilon_{\mu\nu}}
{p_i\cdot q}
\right]\mathcal M_n,
\]

where `eta_i=+1/-1` distinguishes outgoing/incoming legs and `kappa_i` is provisionally allowed to depend on species.

A massless spin-2 polarization has the gauge redundancy

\[
\varepsilon_{\mu\nu}
\to
\varepsilon_{\mu\nu}+q_\mu\xi_\nu+q_\nu\xi_\mu.
\]

Gauge independence of the physical soft amplitude requires

\[
\boxed{
\sum_i\eta_i\kappa_i p_i^\mu=0.
}
\]

Ordinary momentum conservation gives

\[
\sum_i\eta_i p_i^\mu=0.
\]

For arbitrary scattering among different species, the two identities are compatible generically only when

\[
\boxed{\kappa_i=\kappa}
\]

for every species coupled to the same massless graviton.

This is the soft-S-matrix form of gravitational universality/equality of gravitational and inertial response.

---

## 2. Minimal two-species algebra control

Consider elastic scattering `a+b -> a+b` with momenta

\[
p_1+p_2=p_3+p_4.
\]

Soft gauge consistency would require

\[
-\kappa_a p_1-\kappa_b p_2+\kappa_a p_3+\kappa_b p_4=0.
\]

Eliminate `p4=p1+p2-p3`:

\[
\boxed{
(\kappa_b-\kappa_a)(p_1-p_3)=0.
}
\]

For generic non-forward scattering `p1!=p3`,

\[
\boxed{\kappa_a=\kappa_b.}
\]

Repeating through connected species yields one universal gravitational coupling.

---

## 3. Contrast with the compact U(1) soft condition

For a massless spin-1 field the leading soft factor is proportional to

\[
\sum_i\eta_i q_i\frac{p_i\cdot\varepsilon}{p_i\cdot q}.
\]

Gauge independence requires

\[
\boxed{\sum_i\eta_i q_i=0,}
\]

which is charge conservation.  It does **not** force every species to have the same electric charge.

This matches the candidate architecture:

```text
massless spin-2 -> universal gravitational coupling;
compact Hopf U1 -> quantized charge lattice, with species-dependent integer representations allowed.
```

---

## 4. Common metric consequence

If the candidate's physical history produces

- a Lorentz-invariant massless helicity-2 pole;
- a valid soft factorization regime;
- positive unitary residues;

then different low-energy sectors cannot consistently choose unrelated gravitational couplings while interacting with that single graviton.

The common-metric/equivalence-principle structure is therefore an infrared consistency consequence, not an arbitrary coupling convention.

This strengthens `COMMON_PHOTON_GRAVITON_LIGHT_CONE_THEOREM.md`: once the Maxwell field is part of the same Lorentz-invariant low-energy S matrix, its stress-energy couples to the universal graviton.

---

## 5. What the microscopic theory must still demonstrate

The soft theorem is conditional on an infrared S-matrix/pole regime.  The repository must still derive that regime from its physical projector/history construction.

Required gates include

1. a physical massless TT pole;
2. positive residue/unitarity;
3. Lorentz-covariant soft limit;
4. factorization of the soft pole;
5. the Ward identity above;
6. a common `kappa` across the derived photon/fermion/other sectors.

Failure of universal soft coupling would falsify the claimed ordinary massless-graviton infrared phase or imply that one of its assumptions is not realized.

---

## 6. Scope boundary

This theorem does not derive the numerical value of Newton's constant.  It says that once one coupling scale is fixed, the same gravitational coupling applies universally in the stated IR regime.

Nor does it derive the Standard Model charge assignments; compact `U(1)` only constrains the representation/charge lattice once a matter carrier is derived.
