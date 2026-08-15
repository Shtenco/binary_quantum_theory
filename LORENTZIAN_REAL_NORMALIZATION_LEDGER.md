# Lorentzian real-normalization and sign ledger

Status: **conditional analytic normalization/sign relation inside the declared Thiemann regularization and repository conventions**.

This file fixes the relative Lorentzian coefficient upstream of the HDA calculation. No HDA residual is used to choose its magnitude or sign.

---

## 1. Frozen Euclidean normalization

The independent tetrahedral combinatorial audit now gives

\[
\boxed{
H_E^{phys}=n_EH_{sine}^{raw},
\qquad
n_E=-\frac{2}{3\hbar}.
}
\]

See `EUCLIDEAN_SINE_NORMALIZATION_MATCH.md` and `scripts/euclidean_sine_normalization_match_gate.py`.

Thus the earlier state of this ledger in which `n_E` was still open is superseded.

---

## 2. Canonical Lorentzian identities

In the declared Thiemann sign convention,

\[
K^{phys}
=-\frac{1}{i\hbar}[V,H_E^{phys}],
\]

and the Lorentzian K-K-V correction is

\[
H^{corr}
=-\frac{8}{(i\hbar)^3}
\mathcal L(K^{phys},K^{phys},V).
\]

The repository structural operators are

\[
K_{raw}=[V,H_{sine}^{raw}],
\qquad
L_{raw}=\mathcal L(K_{raw},K_{raw},V).
\]

Therefore

\[
\boxed{
K^{phys}=\frac{i n_E}{\hbar}K_{raw}
}
\]

and

\[
\boxed{
H^{corr}=\frac{8in_E^2}{\hbar^5}L_{raw}.
}
\]

---

## 3. Five-bracket phase and signed real coefficient

The separately frozen five-bracket phase defines

\[
\boxed{H_{phase}=-iL_{raw}}.
\]

Hence

\[
L_{raw}=iH_{phase}
\]

and

\[
H^{corr}
=-\frac{8n_E^2}{\hbar^5}H_{phase}.
\]

Substituting

\[
n_E=-\frac{2}{3\hbar}
\]

gives the **signed** relation

\[
\boxed{
H^{corr}
=-\frac{32}{9\hbar^7}H_{phase}.
}
\]

The previous statement that only `|g_R|` was fixed is therefore superseded once the Euclidean normalization and the declared Thiemann sign convention are both retained.

A common sign reversal of the **entire** Hamiltonian constraint is a separate convention and does not permit flipping only the Lorentzian term relative to `H_E`.

---

## 4. Repository `H_L` convention

The repository defines the real-Barbero completion as

\[
\boxed{
G=H_E+(1+\beta^2)H_L.
}
\]

Therefore

\[
\boxed{
H_L
=-\frac{32}{9\hbar^7(1+\beta^2)}H_{phase}
}
\]

when the beta-dependent factor is written outside `H_L` as above.

For the first full finite test, freeze

\[
\beta=1,
\qquad
\hbar=1
\]

in structural units. Then

\[
\boxed{
H_L=-\frac{16}{9}H_{phase}
}
\]

and the full Lorentzian correction entering `G` is

\[
\boxed{
2H_L=-\frac{32}{9}H_{phase}.
}
\]

Since

\[
H_{phase}=-iL_{raw},
\]

the same beta=1 full correction can be implemented directly on the raw state as

\[
\boxed{
H^{corr}=\frac{32i}{9}L_{raw}.
}
\]

This last form is convenient for the exact sparse state-to-state code because the existing Lorentzian engine returns `L_raw`.

---

## 5. Frozen local and 16-cell coefficients

The exact environment-unbiased raw one-body amplitude is

\[
L_{raw,1body}=i c_LY,
\qquad
c_L=1.3389293521464034.
\]

Thus in `beta=hbar=1` structural units:

```text
phase-completed raw H_phase local Y = +1.3389293521464034
bare repository H_L local Y        = -2.3803188482602727
full Lorentzian correction local Y = -4.760637696520545.
```

The raw oriented 16-cell ideal mirror-pair structural split is

```text
42.84573926868491 * coefficient.
```

Hence the signed structural shifts are

```text
bare H_L pair coefficient        = -76.17020314432873
full beta=1 correction coefficient = -152.34040628865745.
```

These are **dimensionless relative operator coefficients**, not physical energies or force predictions.

---

## 6. Classical beta consistency

The separate classical identity remains

\[
H_E^{kin}=-\beta^2Q_{DW},
\qquad
H_L^{corr}=(1+\beta^2)Q_{DW},
\]

so

\[
H_E^{kin}+H_L^{corr}=Q_{DW}.
\]

The external `(1+beta^2)` factor must therefore not be counted twice in the full quantum HDA script.

---

## 7. No remaining Lorentzian coefficient fit

For the next beta=1 full two-node calculation the geometry operator is fixed as

\[
\boxed{
G_v^{raw-units}
=n_EH_{E,v}^{sine,raw}
+\frac{32i}{9}L_{raw,v},
\qquad n_E=-\frac23,
}
\]

if both terms are expressed in the same canonical structural units.

Equivalently, an overall common factor may be divided out of the entire constraint, but the **relative** `H_E : H_L` coefficient and sign are not adjustable.

The HDA calculation is therefore a prediction/falsifier, not a calibration of `H_L`.

---

## Reproduction

```bash
python scripts/euclidean_sine_normalization_match_gate.py --hbar 1
python scripts/lorentzian_real_normalization_gate.py
python scripts/lorentzian_repo_sign_gate.py --hbar 1 --beta 1
```
