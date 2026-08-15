# Lorentzian real-normalization ledger

Status: **conditional analytic normalization relation inside the declared Thiemann regularization convention**.

This file removes one apparent free parameter without fitting the HDA residual.

The repository intentionally computes dimensionless structural operators. Let the one remaining real Euclidean normalization be defined by

\[
\boxed{
\hat H_E^{phys}=n_E\,\hat H_{sine}^{raw}.
}
\]

The constant `n_E` must be fixed by the Euclidean classical/small-loop normalization and the chosen units, **not** by minimizing a later HDA defect.

---

## 1. Primary canonical identities

In Thiemann's real-connection construction (the `beta=1` convention of the original 1996 formula),

\[
K=-\{V,H_E[1]\},
\]

so quantization gives

\[
\hat K^{phys}
=-\frac{1}{i\hbar}[\hat V,\hat H_E^{phys}].
\]

The Lorentzian K-K-V correction is built as

\[
\hat H^{corr}
=-\frac{8}{(i\hbar)^3}\,\mathcal L(\hat K^{phys},\hat V),
\]

where schematically

\[
\mathcal L(K,V)
=\sum \epsilon\,
\operatorname{Tr}
\left[
C(K)C(K)C(V)
\right]
\]

and `C` is linear in its operator argument.

The overall sign here follows the convention of Eq. (0.15) of Thiemann's `gr-qc/9606088`. A project-specific definition of `H_L` may absorb a real minus sign, but it cannot change the magnitude relation derived below.

---

## 2. Map to the repository's raw operators

The repository uses

\[
K_{raw}=[V,H_{sine}^{raw}]
\]

and

\[
L_{raw}=\mathcal L(K_{raw},V).
\]

Substituting

\[
H_E^{phys}=n_EH_{sine}^{raw}
\]

into the canonical definition of `K` gives

\[
\boxed{
K^{phys}
=\frac{i n_E}{\hbar}K_{raw}.
}
\]

Because the Lorentzian structural triple contains **two** `K` legs,

\[
\mathcal L(K^{phys},V)
=\left(\frac{i n_E}{\hbar}\right)^2L_{raw}
=-\frac{n_E^2}{\hbar^2}L_{raw}.
\]

Therefore the physical correction in the original Thiemann sign convention is

\[
\boxed{
H^{corr}
=\frac{8 i n_E^2}{\hbar^5}L_{raw}.
}
\]

The exact finite environment trace found

\[
L_{raw,1body}=i c_LY,
\qquad
c_L=1.3389293521464034.
\]

Hence

\[
\boxed{
H^{corr}_{1body}
=-\frac{8n_E^2}{\hbar^5}
\,c_LY
}
\]

in that sign convention.

Equivalently, relative to the phase-completed structural block

\[
H_{phase}=-iL_{raw}=c_LY,
\]

the remaining real coefficient has fixed magnitude

\[
\boxed{
|g_R|=\frac{8n_E^2}{\hbar^5}.
}
\]

Thus `g_R` is **not an independent force/mass/HDA knob** once `n_E` and the canonical unit convention are fixed.

---

## 3. What remains to fix `n_E`

The code-level `H_sine` intentionally omits the common continuum constants. Its exact Euclidean normalization must be matched once against the discretized small-loop expression

\[
H_E[N]
=2\int N\,\epsilon^{abc}
\operatorname{Tr}(F_{ab}\{A_c,V\})
\]

and the chosen tetrahedral/oriented-spec counting.

The original Thiemann triangulation has the elementary coefficient

\[
-\frac{2}{3i\hbar}
\]

multiplying its oriented holonomy-volume trace. The repository's `oriented_specs` and `T_sequences` already package cyclic permutations, loop reversal and the volume commutator differently, so it would be unsafe to copy `-2/3` directly as `n_E` without an explicit combinatorial normalization audit.

Therefore the next normalization calculation is narrowly defined:

```text
repository oriented_specs/T_sequences
        versus
one continuum tetrahedron epsilon^{ijk} trace
```

on a small-curvature classical control.

No HDA residual is used in this matching.

---

## 4. General real beta

The repository separately freezes the classical real-Barbero identity

\[
H_E^{kin}+H_L^{corr}=Q_{DW},
\]

with

\[
H_E^{kin}=-\beta^2Q_{DW},
\qquad
H_L^{corr}=(1+\beta^2)Q_{DW}.
\]

The factor `(1+beta^2)` therefore belongs to the physical real-connection completion and is not to be fitted against quantum HDA data.

The `beta=1` normalization relation above fixes how the raw K-K-V stack scales with the Euclidean normalization. The general-beta implementation must additionally keep the repository's declared beta conventions consistent in `A=Gamma+beta K`, `K`, flux normalization and the external `(1+beta^2)` coefficient.

---

## 5. Consequences

The apparent parameter hierarchy is reduced from

```text
n_E, g_R, beta, route normalization
```

to

```text
n_E fixed by Euclidean classical matching,
beta fixed/varied as a canonical parameter with the exact classical cancellation test,
route normalization fixed by the geometric sharp/square-root construction,
g_R derived quadratically from n_E.
```

The full HDA then becomes a **prediction/falsifier** of these independently fixed choices rather than a calibration procedure.

---

## 6. Scope

This ledger derives the relative dependence and phase from the declared canonical formulas. It does **not** yet assign a numerical `n_E` because the repository's tetrahedral combinatorial normalization has not been matched term-by-term to the continuum convention.

It also does not set an absolute energy scale, Newton constant or physical mirror splitting. Those require the separate scale-setting map.
