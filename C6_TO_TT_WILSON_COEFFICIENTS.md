# Restricted C6 -> TT -> eta2/zeta4 extractor

Status: **exact extractor for the preregistered isotropic-plus-one-cubic-harmonic subfamily.  It is no longer claimed to span the complete generic nonzero-momentum S4 TT quartic sector.**

The complete general theorem is now `S4_TT_QUARTIC_COMPLETE_BASIS.md`, which proves that a parity-even generic directed-momentum TT quartic kernel has six independent physical Wilson structures after `tr(h)=0` and `h.k=0` are imposed.

This file remains important for two reasons:

1. it is an exact positive-control extractor for the reduced bare propagator;
2. it defines a **nested two-parameter hypothesis** that the future six-coefficient microscopic result can either pass or falsify.

---

## 1. Correct symmetry scope

For an onsite `k=0` six-edge kernel,

\[
C_6^{(0)}=aI+bA_{adj}+cO_{opp}
\]

is exact and gives

\[
\lambda_E=a-2b+c,
\qquad
\lambda_{T_2}=a-c,
\]

\[
\Delta_{ET}=2(c-b).
\]

For a generic nonzero vector momentum the exact law is instead

\[
\boxed{
C_6(g\mathbf k)=U_gC_6(\mathbf k)U_g^{-1}.
}
\]

Therefore a generic fixed direction need not commute with the full `S4` action.  The physical quartic TT quotient is six-dimensional, not two-dimensional.

---

## 2. Nested scalar cubic hypothesis

Suppose, **after the full six-coefficient extraction**, the polarization-averaged quartic pole is compatible with the restricted form

\[
\boxed{
\bar e_4(\hat n)
=\eta_2^{iso}
+\zeta_4^{cub}Q_4^{cub}(\hat n),
}
\]

where

\[
Q_4^{cub}(\hat n)
=\sum_i n_i^4-\frac35.
\]

For the high-symmetry directions,

\[
Q_{100}=\frac25,
\qquad
Q_{110}=-\frac1{10},
\qquad
Q_{111}=-\frac4{15}.
\]

Hence

\[
e_{100}=\eta_2+\frac25\zeta_4,
\]

\[
e_{110}=\eta_2-\frac1{10}\zeta_4,
\]

\[
e_{111}=\eta_2-\frac4{15}\zeta_4.
\]

The first two determine

\[
\boxed{
\zeta_4=2(e_{100}-e_{110}),
}
\]

\[
\boxed{
\eta_2=\frac15e_{100}+\frac45e_{110}.
}
\]

The third is then a held-out identity:

\[
\boxed{
e_{100}-4e_{110}+3e_{111}=0.
}
\]

Equivalently,

\[
\zeta_4=6(e_{110}-e_{111}).
\]

These formulas are exact **inside this nested hypothesis**.

---

## 3. Why three directions are not a complete general extractor

The complete TT quartic basis has dimension six.

The full polarization-resolved information available at `(100),(110),(111)` spans only rank five of that six-dimensional space.  Therefore no algebraic manipulation of only those three directions can reconstruct the most general `S4` quartic response.

`S4_TT_QUARTIC_COMPLETE_BASIS.md` adds the preregistered generic direction `(120)` and gives an exact rational six-observable matrix with

\[
\det A=\frac1{699840000}\ne0.
\]

The future production analysis must perform that full extraction first.

Only then is it legitimate to ask whether the six-vector lies in the smaller `eta2/zeta4` subspace.

---

## 4. Exact positive control: reduced bare propagator

The already-frozen reduced TT pole has

\[
e_{100}=-\frac1{18},
\qquad
e_{110}=-\frac1{72},
\qquad
e_{111}=0.
\]

The nested extractor gives

\[
\boxed{
\zeta_{4,bare}=-\frac1{12},
}
\]

\[
\boxed{
\eta_{2,bare}=-\frac1{45}.
}
\]

and the held-out identity is exact:

\[
-\frac1{18}-4\left(-\frac1{72}\right)+3(0)=0.
\]

So the script `scripts/c6_tt_wilson_extractor.py` remains a correct regression/positive-control tool for this restricted model.

---

## 5. Nested single-Qtet polarization hypothesis

A second restricted hypothesis is

\[
e_{4,\pm}(\hat n)=\eta_2+\gamma_4q_\pm(\hat n),
\]

where `q_±` are the eigenvalues of the TT projection of

\[
Q_{tet}=\frac35P_E-\frac25P_{T_2}.
\]

`TETRAHEDRAL_TT_BIREFRINGENCE_THEOREM.md` proves

\[
\boxed{\zeta_4=\gamma_4/4}
\]

for the polarization average and

\[
\boxed{
\Delta e_{100}:\Delta e_{110}:\Delta e_{111}=4:3:0
}
\]

for the polarization splitting.

Again: this is a parameter-free **consistency pattern** after the full six-Wilson result is known, not a reason to force the microscopic result into one splitter.

---

## 6. Scientific decision tree

The correct post-production analysis is now:

```text
full interblock Peter-Weyl kernel
 -> TT projection
 -> extract six general quartic Wilson coefficients c1...c6
 -> test full-rank internal consistency
 -> test eta2 + zeta4 Q4 nested hypothesis
 -> test single-Qtet 4:3:0 birefringence nested hypothesis
 -> if passed: report eta2, zeta4 as compressed physical description
 -> if failed: report the stronger full six-coefficient prediction
```

No additional tensor term may be added or removed after viewing an external posterior without a new preregistration.

---

## 7. Scope guard for the 8.43% precursor

The measured first-refinement value

\[
\Delta_{ET}/\kappa_5=0.08430036026012608
\]

belongs to a local Euclidean tangent kernel.  It is not `zeta4`, not `gamma4`, and not any one of the six generic infrared Wilson coefficients until the interblock derivative expansion is performed.

The bridge remains

\[
\boxed{
\text{local }\Delta_{ET}
\to\text{interblock }C_6(\omega,\mathbf k)
\to K_{TT}
\to(c_1,\ldots,c_6)
\to\text{nested reductions if passed}
\to\text{experiment}.
}
\]
