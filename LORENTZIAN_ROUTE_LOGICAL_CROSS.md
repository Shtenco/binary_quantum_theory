# Lorentzian × route logical cross: ordering discriminator

Status: **finite 2×2 logical diagnostic; not yet the full two-node HDA**.

This result combines the phase-completed Lorentzian logical one-body block with the independently computed isotropic route-metric orderings.

---

## 1. Lorentzian input

Per unit still-open real normalization `g_R`, the five-bracket phase completion gives

\[
H_L^{log}/g_R=c_LY,
\qquad
c_L=1.3389293521464034.
\]

---

## 2. Two route orderings

The frozen expectation-first isotropic average is scalar:

\[
\Omega_{exp}=0.8598466001022401\,I.
\]

The operator-first square-root diagnostic gives

\[
\Omega_{op}
\simeq
0.8197716816 I
-0.0347058975 X
+0.0200374593 Z.
\]

Its shape-plane norm is

\[
\sqrt{X^2+Z^2}=0.040074918545\ldots
\]

and it contains no `Y` component.

---

## 3. Hermitian cross generator

Define the local Hermitian cross diagnostic

\[
C_{L\times R}
=-i[H_L^{log},\Omega].
\]

### Expectation-first

Because `Omega_exp` is proportional to identity,

\[
\boxed{C_{L\times R}^{exp}=0.}
\]

### Operator-first

Using Pauli commutators,

\[
-i[c_LY,\Omega_{op}]
=2c_L(\Omega_ZX-\Omega_XZ).
\]

Numerically, per unit `g_R`,

\[
\boxed{
C_{L\times R}^{op}
=0.0536574847984\,X
+0.0929374897107\,Z.
}
\]

The shape coefficient norm is

\[
\boxed{0.1073149694526}
\]

and the Frobenius norm is

\[
\boxed{0.1517662852455}.
\]

Thus the two orderings are not merely different representations of the same finite logical operator: the operator-first route square root opens a concrete Lorentzian `X/Z` cross channel that the expectation-first isotropic average removes.

---

## 4. Relation to the asymptotic HDA theorem

This does **not** contradict the fixed-cutoff composition certificate.

The theorem states that a finite geometry-route cross coefficient enters the regulated HDA residual only at the declared suppressed order,

\[
C_{cross}/D=O(\epsilon)
\]

at fixed safe cutoff.

The new calculation fixes a finite logical coefficient that a future complete operator-first Lorentzian route calculation must reproduce before testing the `epsilon` scaling.

It therefore upgrades the route-ordering question from

```text
operator-first retains some X/Z anisotropy
```

to the sharper statement

```text
operator-first predicts a nonzero Lorentzian-route logical cross,
expectation-first predicts zero for the same isotropic one-body average.
```

---

## 5. Decision criterion

The route ordering must not be chosen because one cross coefficient is smaller.

The legitimate selector is the complete constraint algebra:

1. freeze one positive square-root/densitized ordering;
2. build the same ordering on the full geometry × route habitat;
3. include the phase- and normalization-completed `H_L`;
4. compute the two-node commutator;
5. require the correct HDA target without channel-specific subtraction or refitting.

Whichever ordering fails the full HDA is rejected.

---

## 6. Reproduction

```bash
python scripts/lorentzian_route_logical_cross_gate.py \
  --output verification_results/LORENTZIAN_ROUTE_LOGICAL_CROSS.json
```

---

## Scope

The quoted numbers are dimensionless logical coefficients per unit real Lorentzian normalization `g_R`. They are not physical energies and do not determine a fifth force. The result is an operator-ordering discriminator for the next HDA calculation.
