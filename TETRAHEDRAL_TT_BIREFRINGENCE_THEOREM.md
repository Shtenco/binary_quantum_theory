# Exact tetrahedral spin-2 -> TT birefringence theorem

Status: **exact representation/TT-projection theorem; no microscopic coefficient or experimental datum is fitted here.**

The first refined six-edge metric carrier has traceless decomposition

\[
\mathrm{Sym}^2_0(\mathbb R^3)=E\oplus T_2.
\]

The unique `S4`-invariant traceless splitting operator is normalized in this repository as

\[
\boxed{
Q_{tet}=\frac35P_E-\frac25P_{T_2}.
}
\]

This note proves that a nonzero momentum-dependent coefficient multiplying `Q_tet` predicts **both** the scalar cubic angular modulation and a fixed polarization birefringence pattern.  Averaging the two TT poles loses information.

---

## 1. Concrete spin-2 realization

Represent a traceless metric perturbation by a real symmetric `3x3` tensor `h` with Frobenius inner product

\[
\langle h_1,h_2\rangle=\operatorname{Tr}(h_1h_2).
\]

Under the tetrahedral/cubic action,

- `E` is the two-dimensional diagonal traceless subspace;
- `T2` is the three-dimensional off-diagonal subspace.

Thus

\[
Q_{tet}h
=\frac35 h_{diag}-\frac25 h_{off}.
\]

For a unit propagation direction `n`, let `Pi_TT(n)` be the orthogonal projector onto the two-dimensional transverse-traceless plane.  Define

\[
\boxed{
Q_{TT}(\hat n)=\Pi_{TT}(\hat n)Q_{tet}\Pi_{TT}(\hat n)
\big|_{TT}.
}
\]

Its two eigenvalues `q_+(n),q_-(n)` are physical polarization invariants; they do not depend on the arbitrary plus/cross basis chosen inside the TT plane.

---

## 2. Three exact high-symmetry directions

Direct projection gives:

### Axis `(100)`

One TT polarization is diagonal (`E`) and the orthogonal cross polarization is off-diagonal (`T2`):

\[
\boxed{
\operatorname{spec}Q_{TT}(100)=\left\{\frac35,-\frac25\right\}.
}
\]

Hence

\[
\frac{q_++q_-}{2}=\frac1{10},
\qquad
q_+-q_-=1.
\]

### Face diagonal `(110)`

\[
\boxed{
\operatorname{spec}Q_{TT}(110)=\left\{\frac7{20},-\frac25\right\}.
}
\]

so

\[
\frac{q_++q_-}{2}=-\frac1{40},
\qquad
q_+-q_-=\frac34.
\]

### Body diagonal `(111)`

The TT plane is degenerate under the residual three-fold symmetry:

\[
\boxed{
\operatorname{spec}Q_{TT}(111)=\left\{-\frac1{15},-\frac1{15}\right\}.
}
\]

Therefore

\[
\frac{q_++q_-}{2}=-\frac1{15},
\qquad
q_+-q_-=0.
\]

The body diagonal is an exact no-birefringence direction for this single tetrahedral spin-2 operator.

---

## 3. Scalar cubic invariant is the polarization trace

Define

\[
Q_4^{cub}(\hat n)=\sum_i n_i^4-\frac35.
\]

The TT trace obeys the exact identity

\[
\boxed{
\frac12\operatorname{Tr}_{TT}Q_{TT}(\hat n)
=\frac14Q_4^{cub}(\hat n).
}
\]

A quick symmetry proof is sufficient: the left-hand side is an even tetrahedral scalar of degree four with zero spherical average, so at this order it must be proportional to the unique `l=4` cubic invariant.  Evaluating `(100)` fixes the proportionality to `1/4`.  Direct symbolic projection verifies the identity.

Thus if the quartic TT pole is

\[
e_{4,\pm}(\hat n)
=\eta_2+\gamma_4 q_\pm(\hat n),
\]

then its polarization average is

\[
\bar e_4(\hat n)
=\eta_2+\frac{\gamma_4}{4}Q_4^{cub}(\hat n).
\]

Comparing with the scalar convention

\[
\bar e_4=\eta_2+\zeta_4Q_4^{cub}
\]

gives the exact bridge

\[
\boxed{\zeta_4=\frac{\gamma_4}{4}.}
\]

The microscopic `E-T2` quartic coefficient is therefore four times the scalar cubic coefficient extracted from the polarization-averaged pole.

---

## 4. A stronger blind prediction: fixed birefringence ratios

The polarization splitting is

\[
\Delta e_4(\hat n)
=e_{4,+}-e_{4,-}
=\gamma_4(q_+-q_-).
\]

Using `gamma4=4 zeta4`:

\[
\boxed{\Delta e_{100}=4\zeta_4,}
\]

\[
\boxed{\Delta e_{110}=3\zeta_4,}
\]

\[
\boxed{\Delta e_{111}=0.}
\]

Hence, whenever one `Q_tet` operator dominates the leading parity-even tetrahedral correction,

\[
\boxed{
\Delta e_{100}:\Delta e_{110}:\Delta e_{111}=4:3:0.
}
\]

This ratio is independent of the absolute lattice/Planck scale and independent of the magnitude of the microscopic anisotropy.  It is therefore a cleaner blind consistency test than any one dimensional coefficient.

---

## 5. Physical velocity and phase birefringence

For

\[
\omega^2=c^2k^2\left[1+a_*^2k^2e_{4,\pm}(\hat n)+\cdots\right],
\]

\[
\frac{v_{g,+}-v_{g,-}}{c}
=\frac32a_*^2k^2\Delta e_4(\hat n)+\cdots.
\]

Thus

\[
(100):\quad
\boxed{
\frac{\Delta v_{pol}}{c}=6a_*^2k^2\zeta_4,
}
\]

\[
(110):\quad
\boxed{
\frac{\Delta v_{pol}}{c}=\frac92a_*^2k^2\zeta_4,
}
\]

\[
(111):\quad \boxed{\Delta v_{pol}=0}
\]

at leading quartic order.

With `a_*^2=8 pi lambda_R_eff ell_P^2` these become

\[
(100):\quad
\boxed{
\frac{\Delta v_{pol}}{c}
=48\pi\lambda_R^{eff}\zeta_4\left(\frac{E}{E_P}\right)^2,
}
\]

\[
(110):\quad
\boxed{
\frac{\Delta v_{pol}}{c}
=36\pi\lambda_R^{eff}\zeta_4\left(\frac{E}{E_P}\right)^2.
}
\]

At fixed frequency the accumulated polarization phase difference is

\[
\Delta\phi_{pol}
=-\frac12La_*^2\left(\frac\omega c\right)^3\Delta e_4.
\]

Therefore

\[
(100):\quad
\boxed{
\Delta\phi_{pol}
=-16\pi\lambda_R^{eff}\zeta_4\frac{L}{\ell_P}\left(\frac{E}{E_P}\right)^3,
}
\]

\[
(110):\quad
\boxed{
\Delta\phi_{pol}
=-12\pi\lambda_R^{eff}\zeta_4\frac{L}{\ell_P}\left(\frac{E}{E_P}\right)^3,
}
\]

and the body diagonal vanishes at this order.

---

## 6. Why this corrects the earlier scalar-only language

`C6_TO_TT_WILSON_COEFFICIENTS.md` correctly warned that unequal TT eigenvalues must be reported instead of averaged away.  The theorem here makes that warning constructive:

```text
microscopic E/T2 quartic coefficient gamma4
        |\
        | \-- polarization average --> zeta4 = gamma4/4
        |
        \---- polarization splitting --> fixed 4:3:0 high-symmetry pattern
```

Thus a future full `C6(omega,k)` result should report at least

- `eta2_IR`;
- `gamma4_IR` or equivalently `zeta4_IR`;
- both TT pole branches;
- the `4:3:0` birefringence consistency test when the single-`Q_tet` description applies.

A significant additional independent TT splitting structure would mean that more than one tetrahedral/cubic spin-2 Wilson operator is active and must be preregistered before external comparison.

---

## 7. Scope guard

The already measured `0.08430036026012608` is a **local Euclidean tangent-kernel** ratio.  The theorem does not identify that UV number with `gamma4_IR` or `4 zeta4_IR`.

The legal chain remains

\[
C_6^{RG}(\omega,k)
\to \Delta_{ET}(\omega,k)
\to \gamma_4^{IR}
\to \zeta_4^{IR}=\gamma_4^{IR}/4
\to \{\bar e_4,\Delta e_4\}
\to \{\text{directional dispersion, birefringence}\}.
\]

The value of this theorem is that, once the momentum-dependent coefficient is known, the polarization physics is fixed with no extra fit parameter.
