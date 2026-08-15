# Operator-first route normal: quantum selection and matrix HDA

Status: **analytic operator-selection result + exploratory finite logical HDA PASS**.

The earlier route tests used expectation-valued flux metrics as an efficient semiclassical habitat. The logical ordering audit also constructed an operator-first spectral square root. This note separates their roles.

## 1. Quantum linearity selects operator-first

A physical Hamiltonian constraint must act linearly on the Hilbert space. An expectation-first map of the schematic form

\[
F(\psi)=\sqrt{\langle\psi|\hat Q|\psi\rangle}\,\psi
\]

is state dependent and is not a linear operator unless the expectation is constant on the entire relevant state space.

A two-state witness is enough. Let

\[
Q=\operatorname{diag}(1,4).
\]

Then

\[
F(|0\rangle)=|0\rangle,
\qquad
F(|1\rangle)=2|1\rangle,
\]

while on

\[
|+\rangle=(|0\rangle+|1\rangle)/\sqrt2
\]

one gets

\[
F(|+\rangle)=\sqrt{2.5}\,|+\rangle,
\]

which is not

\[
(F|0\rangle+F|1\rangle)/\sqrt2.
\]

The norm defect is

\[
\boxed{0.5065407286\ldots}.
\]

Thus expectation-first is retained only as a semiclassical diagnostic/regression device.

## 2. Positive operator-first construction

On

\[
\mathcal H_G\otimes\mathcal H_R,
\]

geometry fluxes commute with route momenta because they act on different tensor factors. Define

\[
B_i=\sum_a J_a^i\otimes P_a.
\]

Then

\[
\boxed{
A=Q^{ab}\otimes P_aP_b
=\sum_i B_i^\dagger B_i\ge0.
}
\]

Therefore the unique positive spectral square root exists on the natural domain:

\[
\boxed{\Omega=A^{1/2}}.
\]

The production route-normal candidate is

\[
\boxed{R[N]=\frac12\{N,\Omega\}}.
\]

This is a linear operator and is symmetric/self-adjoint subject to the usual domain completion.

## 3. Operator-valued HDA principal symbol

For a frozen local geometry and classical route momentum `p`, let

\[
\Omega(p)^2=Q^{ab}p_ap_b.
\]

Differentiate the matrix identity:

\[
\boxed{
\Omega\,\partial_{p_c}\Omega
+(\partial_{p_c}\Omega)\Omega
=2Q^{cb}p_b.
}
\]

The leading matrix-valued Moyal commutator of

\[
h_N=N(x)\Omega(p),
\qquad
h_M=M(x)\Omega(p)
\]

contains exactly this anticommutator, so

\[
\frac1{i\hbar}[R[N],R[M]]
\leadsto
Q^{ab}(M\partial_bN-N\partial_bM)p_a
\]

up to the already frozen global orientation convention.

Thus operator-valued `Q` does **not** spoil the required HDA structure function at principal-symbol order.

## 4. Finite logical matrix test

The exact logical flux matrices are

\[
Q^{00}=Q^{11}=\frac34 I,
\]

\[
Q^{01}=Q^{10}
=-\frac14 I-\frac{\sqrt3}{4}X+\frac14Z.
\]

A direct 2-component spectral route calculation was run on `L=48` with the same lapse family and WKB convention used by the earlier route gates.

For carrier `k=8` and logical state `K=0`, the defects are

| epsilon | operator-first matrix route defect |
|---:|---:|
| 1/4  | `6.139684459e-6` |
| 1/8  | `3.069835330e-6` |
| 1/16 | `1.534994124e-6` |
| 1/32 | `7.675542020e-7` |
| 1/64 | `3.837772425e-7` |

with

\[
\boxed{p=0.9999608966}.
\]

This is about a factor `2.15` smaller at the endpoint than the historical expectation-metric route defect `8.264687442e-7` on the corresponding carrier.

## 5. Logical-state robustness

At `epsilon=1/64`, carrier `8`:

| logical spinor | endpoint defect | fitted epsilon exponent |
|:--|--:|--:|
| `K0` | `3.837772425e-7` | `0.999960897` |
| `K2` | `3.777455511e-7` | `0.999954760` |
| `(K0+K2)/sqrt2` | `3.556974081e-7` | `0.999934467` |
| `(K0+iK2)/sqrt2` | `3.822415237e-7` | `0.999959885` |
| fixed random spinor | `3.821429625e-7` | `0.999959609` |

The matrix HDA scaling is therefore not an artifact of one logical basis state.

## 6. Carrier robustness

At `epsilon=1/64`:

```text
k=2   defect=3.888079967e-6
k=4   defect=1.206217863e-6
k=8   defect=3.837772425e-7
k=16  defect=1.041823281e-7.
```

Every checked carrier has an epsilon exponent within about `1.5e-4` of one.

## 7. Consequence for the candidate

The production quantum route sector should use

\[
\boxed{
R_{op}[N]
=\frac12\left\{N,
\sqrt{\hat Q^{ab}\hat P_a\hat P_b}
\right\}
}
\]

with the square root taken **before** expectation values.

Expectation-first results remain useful as semiclassical controls and historical finite regressions, but they are not the final quantum Hamiltonian definition.

This also makes the finite Lorentzian × route `X/Z` cross channel from `LORENTZIAN_ROUTE_LOGICAL_CROSS.md` a genuine candidate contribution rather than an optional ordering curiosity.

## 8. Remaining task

The next full finite falsifier must combine, in one linear operator,

```text
H_E^sine
+ phase/normalization-completed H_L
+ R_operator-first
```

on the geometry-changing two-node habitat. The present logical route PASS establishes that replacing the expectation-valued route surrogate by the quantum operator-first square root does not destroy the HDA mechanism.
