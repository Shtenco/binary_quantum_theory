# Higher-shell Peter–Weyl Lambda -> exact S4 RG seed

Status: **exact symmetry reduction of the completed finite higher-shell result; recursive physical RG remains open**.

This certificate combines two already-established pieces:

1. the exact diagonal `S4` twirl theorem for neighboring logical geometry qubits;
2. the completed 32-dimensional higher-shell Peter–Weyl observable `Lambda`.

The point is to reduce the next RG problem to the smallest symmetry-allowed coupling space before any continuum fit is attempted.

## 1. Exact S4 invariant space

For one logical geometry qubit the full face-permutation twirl gives

```text
T1(I)=I
T1(X)=T1(Y)=T1(Z)=0.
```

For two neighboring logical geometry qubits under the same tetrahedral face permutation on both cells, the invariant operator space has dimension three:

\[
\boxed{
\operatorname{Inv}_{S_4}
=\operatorname{span}\{II,\ XX+ZZ,\ YY\}.
}
\]

Therefore every mirror-even two-cell coarse kernel has the exact form

\[
\boxed{
K_{S4}
=c_0 II
+J_{shape}(XX+ZZ)
+J_{orient}YY.
}
\]

No local field or `XZ/ZX` label artifact survives this twirl.

The single symmetry-allowed departure from pseudospin Heisenberg isotropy is

\[
\boxed{
\Delta_{aniso}=J_{orient}-J_{shape}.
}
\]

Thus the anisotropy part of the two-cell RG is one-dimensional.

## 2. Apply the theorem to the completed higher shell

The exact environment-averaged pair trace of

\[
\Lambda
=K^{-1/2}(PH_E^4P-K^2)K^{-1/2}
\]

has raw pair Pauli coefficients

```text
II = 12.860443113390883
XX = +0.37774066046324317
YY = +0.7912767588958898
ZZ = +0.3482393696564814
XZ = +0.025548867283080617
ZX = +0.025548867283081103
IX = XI = -0.2179785470085...
IZ = ZI = -0.1258499727929...
```

The canonical bipartite `B`-sublattice Heisenberg-frame rotation acts as

```text
(X,Y,Z)_B -> (-X,+Y,-Z)_B.
```

Hence the diagonal couplings become

```text
J_X = -0.37774066046324317
J_Y = +0.7912767588958898
J_Z = -0.3482393696564814.
```

The exact `S4` twirl then removes the local fields and off-diagonal `XZ/ZX` terms and averages the two shape axes:

\[
J_{shape}=\frac{J_X+J_Z}{2}.
\]

Numerically,

\[
\boxed{
J_{shape}=-0.3629900150598623
}
\]

and

\[
\boxed{
J_{orient}=+0.7912767588958898.
}
\]

Therefore the canonical higher-shell coarse seed is

\[
\boxed{
\Lambda_{pair}^{S4,B}
=12.860443113390883\,II
-0.3629900150598623(XX+ZZ)
+0.7912767588958898\,YY.
}
\]

## 3. One-dimensional anisotropy coordinate

The unique symmetry-allowed anisotropy is

\[
\boxed{
\Delta_{\Lambda}
=J_{orient}-J_{shape}
=1.1542667739557522.
}
\]

Useful scale-free ratios are

```text
J_shape/c0       = -0.0282253116676750
J_orient/c0      = +0.0615279545128563
Delta_Lambda/c0  = +0.0897532661805313
J_orient/|Jshape|=  2.1798857435937924
```

Thus the anisotropic component is about `8.98%` of the scalar pair coefficient in this finite normalized higher shell.

This ratio is **not** yet a physical Lorentz-violation parameter. It is the correct symmetry-reduced microscopic RG seed.

## 4. Why this materially simplifies the next calculation

Before the twirl, the completed logical observable is a nontrivial `32 x 32` Hermitian matrix with Pauli support through weight five.

For the two-cell coarse geometry channel, exact tetrahedral symmetry means the physical RG does not need to track an arbitrary 16-parameter pair operator. After the declared twirl it needs only

```text
c0(b)
J_shape(b)
J_orient(b)
```

or, after removing the overall scalar normalization,

```text
Jbar(b)
Delta_aniso(b).
```

For rotational restoration the decisive dimensionless gate is simply

\[
\boxed{
R_{aniso}(b)
=\frac{J_{orient}(b)-J_{shape}(b)}{|c_0(b)|}
\longrightarrow 0.
}
\]

At the completed local higher shell,

\[
\boxed{R_{aniso}^{local}=0.0897532661805313.}
\]

A nonzero regulator-independent limit would instead define an anisotropic fixed point.

## 5. Connection to the TT quartic tensor

The reduced causal TT transfer independently contains a cubic spatial quartic invariant

\[
Q_4^{cub}=\sum_i k_i^4-\frac35(k^2)^2
\]

with bare coefficient

\[
\zeta_{4,bare}=-1/12.
\]

The exact logical `S4` anisotropy `Delta_Lambda` and the spatial cubic coefficient `zeta_4` are **not identified by assumption**.

The next recursive PL/Peter–Weyl calculation must derive their map. The important new simplification is that both sides now have a single symmetry-allowed anisotropy coordinate:

```text
logical side: Delta_aniso(b)
spatial TT side: zeta4_cub(b)
```

This gives a sharply testable bridge instead of a generic matrix-fitting problem.

## 6. Next RG gate

The minimal next calculation is therefore

\[
\boxed{
\Delta_{\Lambda}^{local}
\to
\Delta_{\Lambda}(b)
\to
\zeta_4^{cub}(b)
\to
\zeta_4^{IR}.
}
\]

Three preregistered outcomes remain:

```text
Delta/c0 -> 0 and zeta4 -> 0       rotational restoration
Delta/c0 -> nonzero fixed value    anisotropic fixed point
no stable refinement limit          physicalization FAIL
```

No external Lorentz-violation data are used in selecting this coordinate or its sign.

## Reproduction

Given the exact higher-shell JSON artifact:

```bash
python scripts/peter_weyl_higher_shell_s4_rg_seed.py \
  --input verification_results/PETER_WEYL_HIGHER_SHELL_LAMBDA.json \
  --output verification_results/PETER_WEYL_HIGHER_SHELL_S4_RG_SEED.json
```

## Scientific boundary

This certificate proves a symmetry reduction and records the finite RG seed. It does not prove that the microscopic orientation anisotropy survives to macroscopic spacetime, and it does not identify the logical pseudospin directly with a laboratory preferred direction.