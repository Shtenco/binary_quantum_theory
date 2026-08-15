# Peter-Weyl Lorentzian environment-trace result

Status: **exact finite raw-amplitude result + unresolved physical Hermitian ordering/prefactor**.

This document promotes a completed calculation from the research branch into the canonical candidate workstream. It supersedes the older raw question

```text
P H_L P = 0 ?
```

at the structural-amplitude level.

It does **not** yet supply the final physical Lorentzian Hamiltonian normalization.

---

## 1. Frozen calculation

The exact safe-cutoff calculation was run at

```text
Jmax = 7/2
```

on the all-`j=1/2` logical source sector. The four neighboring logical nodes were traced with the unbiased diagonal environment

```text
I_env / 16,
```

covering all

```text
16
```

environment bitstrings with `K=0/2` on each neighboring node.

For one ordered triple

```text
T_abc = Tr_aux[C_a(K_sine) C_b(K_sine) C_c(V)]
```

the Euclidean operator used inside

```text
K_sine=[V,H_E^sine]
```

was the already validated sine-Hermitian ordering

```text
H_E^sine=(T-T^dagger)/(2i).
```

The full oriented node sum is reconstructed from the exact local `S4` orbit:

```text
L_eps,1body = -24 T_sgn(Tbar_123),
epsilon(123)=-1.
```

The companion covariance control uses an independently computed `(1,3,2)` ordered triple.

---

## 2. Reproducibility provenance

The source calculation completed successfully in GitHub Actions on

```text
research/pw-lorentzian-envtrace-orbit
commit ed0949bee6f7e21658f3ef054b9f23d6f167c611
workflow run 31836134627.
```

The final evidence artifact had

```text
artifact id = 9234841784
sha256      = 02bc763845516cf19251604c033a12d450ecf7b82c733e89f414e37ab5ba3a8b.
```

The frozen JSON is now committed at

```text
verification_results/PETER_WEYL_LORENTZIAN_ENVTRACE_ORBIT.json.
```

The exact block and orbit reconstruction code is now retained in this branch:

```text
scripts/peter_weyl_lorentzian_envtrace_block_gate.py
scripts/peter_weyl_lorentzian_envtrace_orbit_collector.py
scripts/peter_weyl_lorentzian_logical_projection_gate.py
scripts/peter_weyl_lorentzian_logical_projection_v2_gate.py
```

---

## 3. Exact finite result

The independent `S4` covariance test gives

```text
relative covariance error
 = 1.3976239359266602e-15.
```

The maximum physical complete-basis / volume leakage is

```text
6.532094795930893e-16.
```

The full 24-term environment-unbiased raw one-body operator is

```text
L_raw ~=
[[ 0, +1.3389293521464034],
 [-1.3389293521464032, 0]]
```

up to `O(1e-16)` complex roundoff.

Its Frobenius norm is

```text
1.8935320488648653.
```

In the logical Pauli basis,

```text
I = 0
X ~= 1.11e-16
Y = (1.841289307431073e-16
     + 1.3389293521464034 i)
Z = 0.
```

Therefore the structural result is

\[
\boxed{
L_{raw,1body}
 = i\,1.3389293521464034\,Y
 + O(10^{-16}).
}
\]

In particular,

\[
\boxed{P L_{raw} P\ne0}.
\]

The result is orientation/sign-sector odd, exactly as selected by the `S4` sign representation.

---

## 4. Crucial ordering fork

The raw structural operator is anti-Hermitian to numerical precision. Therefore the two elementary Hermitian completions behave very differently.

Even Hermitian projection:

\[
H_{even}
=\frac{L_{raw}+L_{raw}^\dagger}{2}
\simeq0.
\]

Anti-Hermitian-to-Hermitian completion:

\[
H_{odd}
=\frac{L_{raw}-L_{raw}^\dagger}{2i}
\simeq
1.3389293521464034\,Y.
\]

The latter has eigenvalues

\[
\boxed{
\lambda=\pm1.3389293521464034
}
\]

before any overall canonical `kappa/beta/hbar` normalization.

This is **not** permission to choose the second ordering because it produces a desired mirror split. The physical Lorentzian ordering and overall `i`/sign/prefactor must be fixed independently from the canonical quantization and classical-limit prescription.

Executable audit:

```bash
python scripts/peter_weyl_lorentzian_onebody_ordering_gate.py \
  --output verification_results/PETER_WEYL_LORENTZIAN_ONEBODY_ORDERING.json
```

---

## 5. What is closed

The following old uncertainty is now removed:

```text
Does the genuine Peter-Weyl K-K-V stack have a nonzero
logical Lorentzian one-body structural amplitude after an
unbiased environment trace and the full 24-term S4 orbit?
```

Answer:

```text
YES.
```

The answer is not inferred from support counting. It is an exact finite amplitude calculation with all 16 logical environment states and an independent S4 covariance control.

---

## 6. What remains open

The correct frontier is now:

1. fix the final physical Hermitian Lorentzian ordering and overall canonical prefactor independently of this result;
2. determine whether the completed one-body term survives, vanishes, or changes normalization under that prescription;
3. compute the completed two-node `H_E+H_L+R_Q` commutator on the same route habitat;
4. verify that the Lorentzian one-body term does not generate an anomalous `O(1)` contribution relative to the HDA target;
5. repeat on independent logical environments / higher collective-spin sectors and along the controlled cutoff trajectory.

Until item 1 is fixed, the raw `iY` coefficient must not be called a physical mirror mass or an experimentally meaningful energy splitting.

---

## Scientific interpretation

The strong result is narrower than a new force claim but more useful for the gravity programme:

> the Lorentzian Peter-Weyl amplitude stack is dynamically nontrivial in the logical sector; the remaining ambiguity is now an operator-ordering/normalization problem rather than a missing-amplitude problem.

That is the new canonical Lorentzian frontier.
