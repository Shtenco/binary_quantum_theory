# Physicalization pass 01 — actual results

Status: **first quantitative pass from the fixed candidate architecture toward physical scale and an observable propagator**.

This file records only results actually obtained in the pass. It does not promote the candidate to an experimentally established theory.

## 1. Absolute phase normalization: exact one-parameter no-go

The additive growth/composition equations were re-evaluated as a linear system. For the finite window `M=8` the equation matrix has shape `184 x 16`, rank `15` and therefore

\[
\boxed{\dim\ker A=1}.
\]

The unique null direction aligns with the linear vector `f(n) proportional to n` with overlap `1.0`.

Independent slopes

```text
0.1, 0.5, 1, sqrt(2), pi
```

all satisfy the same composition equations to numerical residual below `1e-14`.

Therefore

\[
\boxed{f(n)=s n}
\]

is fixed in form, while

\[
\boxed{s\text{ remains undetermined by composition alone}.}
\]

This proves that the remaining microscopic phase/action-normalization freedom is genuinely one-dimensional. Reproduction:

```bash
python scripts/phase_slope_no_go_gate.py
```

The HDA does not remove this Newton/time normalization freedom: the preferred densitized gate is explicitly scale-independent at first pass and permits one common scalar normalization after the directional structure is established.

## 2. Regge TT residue: intensive normalization tends to 1/8

The raw full-lattice Fierz--Pauli coefficient is extensive. Define

\[
Z_L=c_1(L)/L^4,
\]

where `c1` is the first coefficient in the full 10-component Fierz--Pauli fit of the metric Hessian.

For the lowest axial mode:

| L | `Z_L` |
|--:|--:|
| 3 | 0.1021131745 |
| 4 | 0.1114624530 |
| 5 | 0.1161306996 |

The independent Regge/EH normalization implies the continuum target

\[
\boxed{Z_\infty=1/8=0.125}.
\]

Before opening `L=6`, the frozen model

\[
Z_L=\frac18+\frac{C}{L^2}+\frac{D}{L^4}
\]

predicted

\[
Z_6^{pred}=0.11876923193907167.
\]

The held-out calculation gave

\[
\boxed{Z_6^{obs}=0.11876075461190198}
\]

with relative prediction error

\[
\boxed{0.00714\%}.
\]

This is documented in

```text
TT_REGGE_ZT_L6_PREREGISTRATION.md
TT_REGGE_ZT_L6_RESULT.md
```

and supports

\[
\boxed{Z_{TT}^{(\sum A\delta)}\to1/8}.
\]

Hence once the common effective Regge coefficient is fixed,

\[
\boxed{Z_T^{eff}\propto\lambda_R^{eff}/8}.
\]

`Z_T` is therefore not a second unrelated gravitational normalization.

## 3. First explicit connected TT propagator

The already-frozen reduced symplectic causal transfer has exact pole equation

\[
4\sin^2\frac\omega2
=r^2\sum_i4\sin^2\frac{k_i}{2},
\qquad r=\frac1{\sqrt3}.
\]

Thus its two-polarization free connected propagator is

\[
\boxed{
G^{TT}_{AB}(\omega,\mathbf k)
=\frac{\delta_{AB}}
{Z_T[4\sin^2(\omega/2)-r^2\sum_i4\sin^2(k_i/2)+i0]}.
}
\]

This is exact for the reduced TT transfer. It is not yet the full Peter--Weyl/history/RG propagator.

## 4. Quartic pole coefficient: scalar and cubic pieces

The exact small-momentum pole is

\[
\omega^2
=r^2k^2+\frac{r^2}{12}
\left[r^2(k^2)^2-\sum_i k_i^4\right]+O(k^6).
\]

Directional coefficient:

\[
\boxed{
\eta(\hat n)=\frac{r^2-\sum_i n_i^4}{12}.
}
\]

At `r^2=1/3`:

```text
axis          eta = -1/18
face diagonal eta = -1/72
body diagonal eta = 0
```

A numerical pole fit reproduces the analytic values with maximum error below `7.8e-10`.

Decompose the quartic tensor into a rotational scalar plus cubic anisotropy:

\[
Q_4^{cub}=\sum_i k_i^4-\frac35(k^2)^2.
\]

Then the bare reduced coefficients are

\[
\boxed{\eta_{2,bare}^{iso}=-1/45}
\]

and

\[
\boxed{\zeta_{4,bare}=-1/12}.
\]

Reproduction:

```bash
python scripts/tt_propagator_first_pass.py
```

These are **not yet** final physical coefficients. A final scalar LVK-style `eta_2` is allowed only if the full constrained/RG calculation shows that the cubic anisotropy flows away and gives a regulator-independent scalar limit.

## 5. Scale map and calibrated Planck illustration

The physical scale relation remains

\[
\boxed{
\lambda_R^{eff}=\frac{a_*^2}{8\pi\ell_P^2},
\qquad
\frac{a_*}{\ell_P}=\sqrt{8\pi\lambda_R^{eff}}.
}
\]

The central observer document already uses a microscopic `Planck` scale. If one explicitly chooses the calibration

\[
a_*=\ell_P,
\]

then

\[
\lambda_R^{eff}=\frac1{8\pi}.
\]

This is a **calibration convention**, not a derivation from bare bits.

If, only illustratively, the reduced scalar `-1/45` also survived the full RG unchanged, then

\[
A_4=-\frac{1}{45E_P^2}
\approx-1.49\times10^{-58}\;\mathrm{eV}^{-2}.
\]

This number is not preregistered as a theory prediction because the full microscopic `eta_2` has not yet been derived.

## 6. Why the raw Peter--Weyl return kernel is not the answer

The raw Euclidean return object

\[
K=P(H_{E,0}+H_{E,1})^2P=A^\dagger A
\]

is full rank on the 32-dimensional logical sector. The existing full master normalization therefore satisfies

\[
K(K+\mu^2I)^{-1}\to I_{32}
\]

as `mu -> 0`, and its pair partial trace tends to `I4`.

Thus raw second-order anisotropy cannot be used as physical TT stiffness.

## 7. New actual microscopic target now running

Spin parity identifies the first denominator-free higher-shell observable as

\[
\boxed{
\Lambda
=K^{-1/2}(PH_E^4P-K^2)K^{-1/2}.
}
\]

For basis states `|i>` this can be computed without constructing four powers explicitly:

\[
a_i=H_E|i\rangle,
\qquad
b_i=H_E^2|i\rangle,
\]

\[
K_{ij}=\langle a_i|a_j\rangle,
\qquad
(PH_E^4P)_{ij}=\langle b_i|b_j\rangle.
\]

The new executable

```text
scripts/peter_weyl_higher_shell_lambda_gate.py
```

uses the regulator-safe second-hit wall

\[
\boxed{J_{max}=5/2}
\]

and computes the actual `32 x 32` Lambda, its pair trace and its complete five-logical-qubit Pauli-weight decomposition.

This is the current microscopic bridge toward a genuine spatial TT kernel.

## Current physicalization frontier after pass 01

What is now closed:

```text
phase functional form          f(n)=s n, exactly one free slope
Regge intensive TT residue     -> 1/8, with held-out L=6 PASS
reduced connected TT G         explicit exact kernel
bare quartic tensor            eta_iso=-1/45, zeta_cubic=-1/12
```

What remains before a physical external prediction:

```text
1. actual higher-shell Peter-Weyl Lambda
2. recursive spatial/RG map from logical shape sector to TT field
3. Lorentzian/history completion of the same propagator
4. one declared scale calibration or independent derivation of the phase slope s
5. freeze eta_2 and A_4 before opening the external posterior
```

The project remains a candidate theory until that last chain survives an external blind comparison.
