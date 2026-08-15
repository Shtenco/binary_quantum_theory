# Operator-first route kernel safety theorem

Status: **proved algebraic kernel lemma + exhaustive finite audit on the frozen one-step physical support**.

The production route operator is

\[
R_{op}[N]=\frac12\{N,\Omega(p)\},\qquad
\Omega(p)=A(p)^{1/2},
\]

with

\[
A(p)=Q^{ab}p_ap_b=\sum_i B_i(p)^\dagger B_i(p)\ge0,
\qquad
B_i(p)=\sum_a J_a^i p_a.
\]

A positive semidefinite symbol may have zero eigenvalues.  The usual nonsingular formula for differentiating a matrix square root is therefore not, by itself, a sufficient argument on every reached sector.  The required HDA identity can nevertheless be extended through the kernel without assuming invertibility.

## 1. Exact kernel lemma

For any vector `v`,

\[
\langle v|A|v\rangle=\sum_i\|B_i v\|^2.
\]

Hence

\[
\boxed{\ker A=\bigcap_i\ker B_i.}
\]

For a momentum direction `p_c`,

\[
\partial_c A
=\sum_i\left[(\partial_cB_i)^\dagger B_i+B_i^\dagger(\partial_cB_i)\right].
\]

If `u,v in ker A`, then every `B_i u=B_i v=0`, and therefore

\[
\boxed{P_0(\partial_cA)P_0=0},
\]

where `P_0` projects onto `ker A`.

## 2. Kernel-safe Sylvester equation

Let `Omega=sqrt(A)`.  Differentiating `Omega^2=A` requires only a solution of

\[
\boxed{\Omega X_c+X_c\Omega=\partial_cA.}
\]

In an eigenbasis of `Omega`, the Sylvester superoperator has eigenvalues
`omega_r+omega_s`.  Its only zero block is the kernel-kernel block.  The lemma above shows that the corresponding block of `partial_c A` is exactly zero, so the equation is solvable even when `Omega` is singular.

The solution need not be unique inside `ker A`; this is irrelevant to the HDA principal structure because the required quantity is the anticommutator `Omega X_c+X_c Omega`, which is unique and equals `partial_c A`.

For the BCQG symbol,

\[
\partial_{p_c}A=Q^{cb}p_b+Q^{ac}p_a,
\]

and for Hermitian symmetric `Q^{ab}` this is the matrix form of the desired `2 Q^{cb}p_b` structure function.

## 3. Exhaustive finite audit

The executable gate checks every distinct fixed-spin route sector reached by one physical `H_E^sine` action from the frozen all-`j=1/2` seed, over the 25 momentum modes used by the route regression.

Frozen result:

```text
reached sectors                    33
momentum modes                     25
derivative rows                  1650
singular PSD cases                 24
minimum eigenvalue(A)     -7.105427357601002e-15
max ||Q.p|| on ker(A)      1.9133237149764433e-15
max ||P0 dA P0||            1.8736833294989963e-15
max Sylvester residual       1.7614399735154202e-13
```

All negative eigenvalues are numerical roundoff around zero.  The declared acceptance thresholds are `1e-10` for kernel and Sylvester defects.

## 4. Consequence

Zero modes of the positive operator-first route symbol do not create an unaccounted HDA structure-function obstruction on the complete one-step physical route support of the frozen habitat.  This closes the singular-symbol loophole in the principal anticommutator argument.

## Scope

This theorem proves kernel compatibility of the Sylvester anticommutator and exhaustively tests the declared finite route blocks.  It does **not** assert global Frechet differentiability of the matrix square-root map through arbitrary rank-changing families, nor does it replace the exact finite sparse-Fourier route commutator tests.

Reproduction:

```bash
python scripts/operator_route_kernel_safety_gate.py \
  --output verification_results/OPERATOR_ROUTE_KERNEL_SAFETY.json
```
