# Global 16-cell assembly of the Lorentzian logical one-body term

Status: **conditional finite composition theorem from independently tested ingredients**.

This result combines the exact local Lorentzian amplitude, the canonical five-bracket complex phase, the exact 16-cell facet orientation signs and the Lorentzian epsilon sign covariance.

It changes the interpretation of the one-body `Y` term: on the globally oriented 16-cell it is a field conjugate to the staggered orientation order parameter, not a mediator mass.

---

## 1. Local amplitude

The exact environment-unbiased Peter-Weyl calculation gives

\[
L_{raw,1body}=i c_L Y,
\qquad
c_L=1.3389293521464034,
\]

up to numerical errors of order `1e-16`.

The five-bracket quantization phase gives, before the remaining real normalization,

\[
-iL_{raw,1body}=c_LY.
\]

Write the still-open real normalization/sign as `g_R`. A positively oriented local frame therefore carries

\[
H_{L,v}^{1body}=g_R c_LY_v.
\]

---

## 2. 16-cell orientation sign

A tetrahedral boundary facet of the 16-cell is labelled by a four-bit word `b`. The exact facet orientation sign is

\[
\eta_b=(-1)^{\operatorname{popcount}(b)}.
\]

The independently defined staggered mirror variable uses the same `eta_b`.

The Lorentzian 24-term epsilon assembler transforms in the `S4` sign character, so transporting the local positively oriented coefficient to the globally oriented 16-cell contributes precisely this facet sign.

Therefore

\[
\boxed{
H_{L,16}^{1body}
=g_Rc_L\sum_{v=1}^{16}\eta_vY_v.
}
\]

With

\[
\Sigma=\frac1{16}\sum_v\eta_vY_v,
\]

we obtain

\[
\boxed{
H_{L,16}^{1body}=16g_Rc_L\Sigma.
}
\]

Numerically,

\[
16c_L=21.422869634342455.
\]

---

## 3. Ideal mirror-order vacua

For the two classical staggered configurations

\[
Y_v=\chi\eta_v,
\qquad
\chi=\pm1,
\]

we have

\[
\Sigma=\chi
\]

and hence

\[
E_\chi^{struct}=16g_Rc_L\chi.
\]

The structural pair splitting is therefore

\[
\boxed{
|\Delta E|_{struct}
=32c_L|g_R|
=42.84573926868491|g_R|.
}
\]

The per-cell splitting coefficient is

\[
\boxed{2c_L=2.677858704292807}.
\]

These are dimensionless structural coefficients until `g_R` is physically normalized.

---

## 4. Orientation factor is essential

The staggered vacua satisfy

\[
\sum_vY_v
=\chi\sum_v\eta_v
=0
\]

because the 16-cell contains eight `eta=+1` and eight `eta=-1` facets.

So an incorrectly assembled orientation-even one-body term

\[
\sum_vY_v
\]

would cancel on the ideal staggered vacua.

The actual sign-covariant Lorentzian assembly instead gives

\[
\sum_v\eta_vY_v=16\chi.
\]

This provides a useful negative control: the nonzero global field is specifically a consequence of the independently verified epsilon/frame orientation covariance.

---

## 5. Which mirror symmetry is affected?

Two transformations must be distinguished.

### Internal mirror at fixed global orientation

Keep the simplicial orientation convention fixed and send

\[
Y_v\to-Y_v.
\]

Then

\[
\sum_v\eta_vY_v\to-\sum_v\eta_vY_v.
\]

Thus a nonzero renormalized `g_R c_L` explicitly lifts the two internal staggered configurations on a fixed global orientation.

### Simultaneous global-orientation reversal and mirror

If the transformation also reverses the global orientation,

\[
\eta_v\to-\eta_v,
\qquad
Y_v\to-Y_v,
\]

then

\[
\eta_vY_v\to\eta_vY_v.
\]

The Lorentzian one-body term is invariant under this combined transformation.

Therefore the physics depends on which transformation is declared gauge, global parity, or an independent internal mirror operation in the completed theory. That question must be fixed before calling the two configurations physically distinct degenerate vacua.

---

## 6. Consequence for the mirror branch

The previously studied spontaneous two-vacuum mirror picture cannot simply ignore the Lorentzian one-body amplitude.

At fixed global orientation, an exact degenerate internal pair requires at least one of:

1. the fully normalized/refined one-body coefficient flows to zero;
2. additional local terms cancel it by a symmetry fixed before fitting;
3. the two configurations are related only together with global orientation reversal, which is identified as gauge-equivalent or otherwise physically redundant.

If none occurs, the Lorentzian sector acts like a longitudinal staggered field and selects one sign of `Sigma` rather than leaving an exact spontaneous `Z2` pair.

This is **not** a mediator mass and not a fifth-force potential. It is a one-body orientation-field term.

---

## 7. Reproduction

```bash
python scripts/lorentzian_16cell_global_assembly_gate.py \
  --output verification_results/LORENTZIAN_16CELL_GLOBAL_ASSEMBLY.json
```

The gate includes a negative control showing that omitting the required orientation sign makes the unsigned field vanish on both ideal staggered vacua.

---

## 8. Scientific scope

The coefficient `42.84573926868491` is a **dimensionless structural splitting per unit absolute real normalization**. No Joules, eV, force strength or physical range can be assigned until the remaining Lorentzian normalization and absolute scale are derived.

The result is nevertheless a sharp model-selection constraint: the completed theory must decide whether the Lorentzian longitudinal field survives refinement, cancels, or is rendered symmetry-equivalent by global orientation reversal.
