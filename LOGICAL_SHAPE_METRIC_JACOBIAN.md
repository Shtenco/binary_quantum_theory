# Exact logical shape -> tetrahedral metric Jacobian

Status: **exact local geometry bridge + finite-difference regression**.

The physical TT programme needs a concrete map from the logical shape doublet `(X,Z)` to metric perturbations. This map is now fixed locally around the regular tetrahedron.

For four equal face spins `j=1/2`, closure and the exact logical Pauli identities give the independent face-flux products

\[
E_1\cdot E_2=E_3\cdot E_4=-\frac14-\frac12Z,
\]

\[
E_1\cdot E_3=E_2\cdot E_4=-\frac14+\frac14Z-\frac{\sqrt3}{4}X,
\]

\[
E_1\cdot E_4=E_2\cdot E_3=-\frac14+\frac14Z+\frac{\sqrt3}{4}X,
\]

with `E_i^2=3/4`.

For the Gram matrix `G` of `E1,E2,E3`, tetrahedral flux reconstruction gives exactly

\[
\boxed{g(X,Z)=2\sqrt{\det G}\,G^{-1}.}
\]

At the regular oriented branches

```text
X=0, Z=0, Y=+1
X=0, Z=0, Y=-1
```

the same intrinsic background metric is

\[
g_0=
\begin{pmatrix}
2&1&1\\
1&2&1\\
1&1&2
\end{pmatrix}.
\]

The exact tangent matrices are

\[
M_X=\left.\frac{\partial g}{\partial X}\right|_0
=\begin{pmatrix}
\sqrt3/2&0&\sqrt3/2\\
0&-\sqrt3/2&-\sqrt3/2\\
\sqrt3/2&-\sqrt3/2&0
\end{pmatrix},
\]

\[
M_Z=\left.\frac{\partial g}{\partial Z}\right|_0
=\begin{pmatrix}
1/2&1&-1/2\\
1&1/2&-1/2\\
-1/2&-1/2&-1
\end{pmatrix}.
\]

They satisfy

\[
\boxed{\operatorname{Tr}(g_0^{-1}M_X)=\operatorname{Tr}(g_0^{-1}M_Z)=0}
\]

and

\[
\boxed{
\operatorname{Tr}(g_0^{-1}M_Ag_0^{-1}M_B)
=\frac32\delta_{AB}.
}
\]

Thus the two logical mirror-even shape directions map to a rank-two, orthogonal, equal-norm **trace-free metric tangent** with no free normalization except the common exact factor `3/2`.

The orientation coordinate `Y` is mirror odd and does not enter the intrinsic Gram reconstruction linearly. For a pure logical state near a regular branch,

\[
Y=\pm\sqrt{1-X^2-Z^2},
\]

so `dY=0` at first order. This independently confirms that the TT metric starts in the `(X,Z)` shape sector, not in `Y`.

The next global object is therefore

\[
K_{TT}=\Pi_{TT}M\Gamma_{shape}M^T\Pi_{TT},
\]

where the **local `M` is now fixed** and the remaining work is recursive spatial gluing, momentum dependence and Lorentzian/history propagation.

## Reproduction

```bash
python scripts/logical_shape_metric_jacobian_gate.py \
  --output verification_results/LOGICAL_SHAPE_METRIC_JACOBIAN.json
```

The gate also performs centered finite-difference checks of both derivatives and verifies zero linear determinant/volume change.
