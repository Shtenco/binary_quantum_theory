# Hermitian completion of the full Lorentzian operator

Status: **candidate operator-definition correction + executable finite consistency gate**.

## 1. Why the correction is required

The exact environment-unbiased one-body projection is

\[
L_{raw,1body}=i\,1.3389293521464034\,Y,
\]

so on that projected block the five-bracket phase `-i` produces a Hermitian `Y` Hamiltonian.

However, reconstruction of exact fixed-environment MITM blocks shows that the **unsymmetrized full raw operator** also contains real `X/Z` coefficients before environment tracing. A diagonal block of an anti-Hermitian operator would itself be anti-Hermitian, so these finite exact blocks prove that one must not globally assume

\[
L_{raw}^\dagger=-L_{raw}
\]

for the unsymmetrized microscopic ordering.

Therefore the historical raw-code shorthand

\[
G_v=-\frac23E_v+\frac{32i}{9}L_{raw,v}
\]

is valid only on sectors where `L_raw` is already anti-Hermitian, including the clean environment-unbiased one-body `iY` projection.

## 2. Production candidate completion

A quantum Hamiltonian constraint must use a symmetric/Hermitian Lorentzian block. The minimal completion of the already-declared raw ordering is its anti-Hermitian projection followed by the universal five-bracket phase:

\[
\boxed{
H_{phase}^{sym}
=-\frac{i}{2}(L_{raw}-L_{raw}^\dagger).
}
\]

This operator is exactly Hermitian:

\[
(H_{phase}^{sym})^\dagger=H_{phase}^{sym}.
\]

At `beta=hbar=1`, the upstream signed normalization therefore gives

\[
\boxed{
H_{corr}^{sym}
=-\frac{32}{9}H_{phase}^{sym}
=\frac{16i}{9}(L_{raw}-L_{raw}^\dagger).
}
\]

If a particular sector already obeys `L_raw^dagger=-L_raw`, this reduces identically to

\[
\boxed{H_{corr}^{sym}=\frac{32i}{9}L_{raw}},
\]

so all previously accepted pure-`iY` one-body numbers remain unchanged.

## 3. Effect on the recovered conditional multi-node block

In a Hermitian Pauli basis, if

\[
L_{raw}=\sum_A z_A P_A,
\]

then

\[
H_{phase}^{sym}=\sum_A \operatorname{Im}(z_A)P_A.
\]

Thus the real unsymmetrized `X/Z` pieces are removed by the physical Hermitian completion, while the imaginary pseudoscalar `Y` correlations survive.

For the exact diagonal environment cube of nodes `1,2` with nodes `3,4` fixed at `K=0`, the surviving phase-completed coefficients are

```text
Y I I    = +0.3359014033398999
Y Z1 I   = -0.00702861722247964
Y I Z2   = +0.002338130606598994
Y Z1 Z2  = +0.004676261213197787
```

and the full signed `beta=hbar=1` correction is

```text
Y I I    = -1.1943161007640883
Y Z1 I   = +0.02499063901326094
Y I Z2   = -0.008313353267907534
Y Z1 Z2  = -0.016626706535814353.
```

The environment-unbiased one-body value remains

\[
\boxed{-4.760637696520545\,Y}
\]

in structural units.

## 4. Covariance

The completion preserves every unitary covariance relation already proved for the raw operator. If

\[
L'_{raw}=U L_{raw}U^\dagger,
\]

then

\[
L'_{raw}-L_{raw}'^\dagger
=U(L_{raw}-L_{raw}^\dagger)U^\dagger.
\]

Thus taking the anti-Hermitian part does not spoil the S4/frame covariance of the declared ordering.

## 5. Consequence for the finite HDA falsifier

The earlier channel preregistration using the shorthand `+(32 i/9)L_raw` remains a useful **raw-ordering diagnostic**, but it is no longer the final physical finite Hamiltonian whenever the raw block has a nonzero Hermitian part.

The next physical channel-resolved calculation must therefore use

\[
\boxed{
G_v^{phys}
=-\frac23E_v
+\frac{16i}{9}(L_{raw,v}-L_{raw,v}^\dagger)
}
\]

at `beta=hbar=1`, followed by the same operator-first `R_op` and the same frozen lapse/HDA thresholds.

No coefficient has been adjusted to improve HDA. The change is forced by Hermiticity after exact finite evidence showed that the unsymmetrized raw ordering is not globally anti-Hermitian.

## 6. Scope

This is the **minimal Hermitian completion** of the current raw ordering and is promoted as the production candidate definition.

It does not prove uniqueness among every conceivable microscopic symmetric ordering. That stronger uniqueness question remains open. The appropriate falsifier is now to compare alternative symmetry-preserving orderings against the completed finite HDA and continuum limit rather than treating a non-Hermitian unsymmetrized block as physical.

Executable gate: `scripts/lorentzian_hermitian_completion_gate.py`.
