# Lorentzian multi-node environment correlation

Status: **tested finite diagonal-environment result**.

This result is reconstructed entirely from the successful exact MITM environment-trace run `31836393368` (`head 7a44506a3b17a341381a720ac27eae78b81e27b0`). No new Peter-Weyl amplitudes are fitted or approximated.

## Construction

For source node `0`, the historical environment-trace calculation evaluated all 24 epsilon-oriented Lorentzian triples

\[
T_{abc}=\operatorname{Tr}_{aux}
[C_a(K)C_b(K)C_c(V)]
\]

for every diagonal logical environment. The exact meet-in-the-middle identity

\[
\langle f|C_a(K)_{ij}|s\rangle
=-\langle C_a(K)_{ji}f|s\rangle
\]

was used, so the expensive final generalized `C(K)` state was not approximated; its matrix element was evaluated exactly by moving it to the bra.

The batch-0 artifact from each of the 24 ordered triples contains environments `0,1,2,3`. With source node `0`, those four environments are

```text
env 0 : (K0,K1,K2,K3,K4)=(0,0,0,0,0)
env 1 : (0,2,0,0,0)
env 2 : (0,0,2,0,0)
env 3 : (0,2,2,0,0).
```

Thus nodes `1` and `2` form a complete two-bit diagonal environment cube while nodes `3,4` remain fixed at `K=0`.

For every environment, all 24 raw matrices were assembled using the already frozen epsilon signs. Worker physical basis/volume leakage is bounded by

```text
6.694456401674905e-16.
```

The four reconstructed matrices reproduce themselves from the Walsh expansion with maximum error

```text
1.1102230246251565e-16.
```

## Exact raw Walsh/Pauli decomposition

Write `Z1=+1/-1` for node-1 `K=0/2` and similarly for node 2. The diagonal-environment source operator is expanded as

\[
L_{raw}^{diag}
=A_{00}
+A_{10}Z_1
+A_{01}Z_2
+A_{11}Z_1Z_2,
\]

where each `A` is a `2x2` source-node matrix.

The nonzero Pauli coefficients are

```text
XI1I2   = -0.0187971397169953
YI1I2   = +i 0.335901403339900
ZI1I2   = +0.0211598660748926

XZ1I2   = +0.0286678677309539
YZ1I2   = -i 0.00702861722247964
ZZ1I2   = -0.0211598660748929

XI1Z2   = +0.00658048534263948
YI1Z2   = +i 0.00233813060659899

XZ1Z2   = +0.0131609706852786
YZ1Z2   = +i 0.00467626121319779.
```

The corresponding coefficient-vector norms are

```text
source local                    0.33709171624286727
source x node1                  0.03631787483605024
source x node2                  0.006983526478664483
source x node1 x node2          0.01396705295732858.
```

Hence, in this conditional diagonal projection,

```text
node1-correlated / local ~= 10.7739 %
node2-correlated / local ~=  2.0718 %
three-body-diagonal / local ~= 4.1434 %.
```

The dominant pseudoscalar remains the local

\[
\boxed{YI_1I_2=i\,0.335901403339900},
\]

but it is not the whole finite logical structure. In particular,

\[
\boxed{YZ_1I_2=-i\,0.00702861722248},
\]

\[
\boxed{YI_1Z_2=+i\,0.00233813060660},
\]

\[
\boxed{YZ_1Z_2=+i\,0.00467626121320}.
\]

Thus the environment-unbiased one-body `Y` obtained after tracing all four neighboring logical nodes hides finite neighbor-dependent diagonal correlations before that trace.

## Direct single-neighbor comparison

With nodes `2,3,4` frozen at `K=0`, switching node 1 from `K=0` to `K=2` changes the assembled source matrix by Frobenius norm

```text
0.13275316144945404.
```

In the resulting two-qubit diagonal block, the neighbor-`Z` correlated coefficient-vector norm is

```text
0.046935330342430755
```

versus local coefficient norm

```text
0.3391208765333603,
```

a ratio

```text
0.13840295183895465.
```

## Interpretation

This result sharpens the microscopic prediction of BCQG:

> the raw Lorentzian logical sector is not purely a one-body chirality field before environment tracing; it carries a hierarchy of finite diagonal correlations with neighboring intertwiner states.

It also explains why the environment partial trace can be extremely clean (`Y` only) while fixed-environment calculations can contain additional `X/Z` structure: the trace removes environment-correlated pieces.

## Scope restriction

This is **not** yet the complete two- or three-node Lorentzian Hamiltonian. The historical environment-trace workers measured

\[
\langle e|L|e\rangle
\]

for diagonal environments. They did not measure off-diagonal terms

\[
\langle e'|L|e\rangle,\qquad e'\ne e.
\]

Therefore the coefficients above establish genuine environment dependence of the exact diagonal matrix elements, but they must not be interpreted as the full physical multi-qubit interaction until the off-diagonal environment blocks are also evaluated.

Frozen machine evidence:

`verification_results/PETER_WEYL_LORENTZIAN_ENVTRACE_WALSH_NODE012.json`.
