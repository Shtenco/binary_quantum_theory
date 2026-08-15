# Lorentzian × route logical cross — signed beta=1 regression

Status: **finite 2×2 signed logical regression; not yet the full graph-changing two-node HDA**.

This result combines three independently frozen ingredients:

1. the exact phase-completed Lorentzian logical one-body block;
2. the operator-first logical route square root;
3. the signed relative Lorentzian coefficient fixed from the Euclidean/Thiemann normalization ledger.

---

## 1. Lorentzian input

The exact raw amplitude and five-bracket phase give

\[
H_{phase}^{log}=c_LY,
\qquad
c_L=1.3389293521464034.
\]

The normalization/sign ledger fixes, for `beta=hbar=1`,

\[
\boxed{H_L^{bare}=-\frac{16}{9}H_{phase}},
\]

and the full Lorentzian correction entering

\[
G=H_E+2H_L
\]

is

\[
\boxed{H_{corr}^{full}=-\frac{32}{9}H_{phase}}.
\]

There is no longer an open local normalization `g_R` in this regression.

---

## 2. Route orderings

Historical expectation-first isotropic average:

\[
\Omega_{exp}=0.8598466001022401I.
\]

Operator-first square-root logical average:

\[
\Omega_{op}
\simeq
0.8197716816I
-0.0347058975X
+0.0200374593Z.
\]

The operator-first shape-plane norm is

\[
\sqrt{X^2+Z^2}=0.040074918545\ldots
\]

with no `Y` component.

Expectation-first is retained only as a semiclassical historical control because a state-dependent expectation-first square-root map is nonlinear on quantum superpositions.

---

## 3. Unit phase-completed cross

Define

\[
C_{L\times R}=-i[H^{log},\Omega].
\]

Since `Omega_exp` is scalar,

\[
\boxed{C_{L\times R}^{exp}=0}.
\]

For the operator-first route block,

\[
-i[c_LY,\Omega_{op}]
=2c_L(\Omega_ZX-\Omega_XZ),
\]

so the unit phase-completed cross is

\[
\boxed{
C_{phase\times R}^{op}
=0.0536574847984X
+0.0929374897107Z.
}
\]

Its shape coefficient norm is

\[
0.1073149694526
\]

and Frobenius norm

\[
0.1517662852455.
\]

---

## 4. Signed bare repository `H_L` cross

Multiplying by the independently frozen

\[
-16/9
\]

gives

\[
\boxed{
C_{H_L^{bare}\times R}^{op}
=-0.0953910840860X
-0.1652222039301Z.
}
\]

The signed bare-HL shape coefficient norm is

\[
\boxed{0.1907821679157}
\]

and the Frobenius norm is

\[
\boxed{0.2698067293253}.
\]

---

## 5. Signed full beta=1 Lorentzian correction cross

For the actual full correction in

\[
G=H_E+2H_L,
\]

the phase scale is

\[
-32/9.
\]

Therefore

\[
\boxed{
C_{H_{corr}^{full}\times R}^{op}
=-0.1907821681721X
-0.3304444078603Z.
}
\]

The signed full-correction shape coefficient norm is

\[
\boxed{0.3815643358315},
\]

with Frobenius norm

\[
\boxed{0.5396134586507}.
\]

These values are now a **regression target** for the logical component of the future full graph-changing `G × R_op` calculation.

---

## 6. Relation to HDA scaling

A nonzero finite cross coefficient is not an anomaly by itself. The fixed-cutoff composition theorem requires its contribution relative to the diffeomorphism target to scale as

\[
C_{cross}/D=O(\epsilon).
\]

The physical test is therefore not whether the signed `X/Z` coefficient vanishes, but whether the complete off-shell graph-changing cross obeys the frozen regulator scaling with the correct diffeomorphism target.

The coefficient cannot be tuned away: route ordering, Lorentzian sign and relative magnitude are all fixed upstream.

---

## 7. Reproduction

```bash
python scripts/lorentzian_route_logical_cross_gate.py \
  --output verification_results/LORENTZIAN_ROUTE_LOGICAL_CROSS.json
```

---

## Scope

The numbers above are dimensionless structural logical coefficients in `beta=hbar=1` units. They are not eV/Joule energies and do not establish a fifth force. The role of this calculation is narrower and stronger: it freezes a signed logical subchannel that the exact two-node `H_E^sine+(1+beta^2)H_L+R_op` commutator must reproduce before its regulator scaling is judged.
