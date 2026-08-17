# C6 -> TT -> exact quartic Wilson-coefficient extraction

Status: **exact symmetry/kinematic extraction map; final microscopic inputs from the full depth-two/Lorentzian C6 kernel remain pending**.

This note closes the algebraic part of the current physicalization bottleneck:

\[
C_6(\omega,k)
\longrightarrow
K_{TT}(\omega,k)
\longrightarrow
\{\eta_2^{IR},\zeta_4^{IR}\}.
\]

Once the microscopic six-edge kernel has been computed, no generic quartic tensor fit is needed.

---

## 1. S4 reduces the six-edge kernel to three orbit functions

For the six unordered edges of a tetrahedron, any `S4`-invariant kernel has the form

\[
\boxed{
C_6(\omega,\mathbf k)
=a(\omega,\mathbf k)I
+b(\omega,\mathbf k)A_{adj}
+c(\omega,\mathbf k)O_{opp}.
}
\]

Its irreducible eigenvalues are

\[
\lambda_{A_1}=a+4b+c,
\]

\[
\boxed{\lambda_E=a-2b+c},
\]

\[
\boxed{\lambda_{T_2}=a-c}.
\]

Therefore the unique tetrahedral splitting of the five traceless metric components is

\[
\boxed{
\Delta_{ET}=\lambda_E-\lambda_{T_2}=2(c-b).
}
\]

The common spin-2 stiffness is conveniently

\[
\kappa_5=\frac{2\lambda_E+3\lambda_{T_2}}5.
\]

This step uses no continuum fit.

---

## 2. Exact shape-to-metric and TT projection

Let `M` denote the already-derived local logical-shape-to-metric Jacobian and `Pi_TT(n)` the continuum TT projector for propagation direction `n`.

The physical quadratic tensor kernel is obtained schematically as

\[
\boxed{
K_{TT}(\omega,k\mathbf n)
=\Pi_{TT}(\mathbf n)
M\,\Gamma_{shape}(\omega,k\mathbf n)M^T
\Pi_{TT}(\mathbf n).
}
\]

Equivalently, when the six-edge metric kernel itself is the coarse variable, use the fixed six-edge-to-metric Jacobian before `Pi_TT`.

In a parity-even non-birefringent sector the two physical TT eigenvalues agree in the IR.  If they do not, the polarization splitting must be reported as an additional observable rather than averaged away.

---

## 3. Normalize the leading light cone first

For each direction `n`, solve the TT pole

\[
\det K_{TT}(\omega,k\mathbf n)=0
\]

for the positive-frequency branch and expand

\[
\omega^2
=c_T^2 k^2
+c_T^2 a_*^2 k^4\,e_4(\mathbf n)
+O(a_*^4k^6).
\]

The leading coefficient `c_T^2` is fixed from the common `k^2` term.  A direction-dependent `k^2` coefficient that survives the IR is a failure of rotational/Lorentz restoration and must not be hidden inside the quartic fit.

The dimensionless directional quartic coefficient is

\[
\boxed{
e_4(\mathbf n)
=\lim_{k\to0}
\frac{\omega^2-c_T^2k^2}
{c_T^2a_*^2k^4}.
}
\]

---

## 4. Unique isotropic + cubic decomposition

In three spatial dimensions the zero-angular-mean cubic invariant is

\[
\boxed{
Q_4^{cub}(\mathbf n)
=\sum_{i=1}^3 n_i^4-\frac35.
}
\]

Hence

\[
\boxed{
e_4(\mathbf n)
=\eta_2^{iso}
+\zeta_4^{cub}Q_4^{cub}(\mathbf n).
}
\]

For the three preregistered high-symmetry directions:

### Axis `(100)`

\[
Q_{100}=1-\frac35=\frac25,
\]

so

\[
e_{100}=\eta_2+\frac25\zeta_4.
\]

### Face diagonal `(110)`

For `n=(1,1,0)/sqrt(2)`,

\[
\sum_i n_i^4=\frac12,
\qquad
Q_{110}=-\frac1{10},
\]

hence

\[
e_{110}=\eta_2-\frac1{10}\zeta_4.
\]

### Body diagonal `(111)`

For `n=(1,1,1)/sqrt(3)`,

\[
\sum_i n_i^4=\frac13,
\qquad
Q_{111}=-\frac4{15},
\]

hence

\[
e_{111}=\eta_2-\frac4{15}\zeta_4.
\]

---

## 5. Closed-form extraction: no free tensor fit

The first two directions determine both Wilson coefficients exactly:

\[
\boxed{
\zeta_4
=2\left(e_{100}-e_{110}\right),
}
\]

\[
\boxed{
\eta_2
=\frac15e_{100}+\frac45e_{110}.
}
\]

Independently, the second and third directions give

\[
\boxed{
\zeta_4
=6\left(e_{110}-e_{111}\right).
}
\]

Therefore the third direction is a held-out algebraic consistency test:

\[
\boxed{
e_{100}-4e_{110}+3e_{111}=0
}
\]

for a pure isotropic-plus-cubic quartic tensor.

A statistically significant violation means one of three things:

1. higher angular invariants are already important in the fit window;
2. finite-size/regulator contamination is not under control;
3. the assumed `S4`/cubic effective description is incomplete.

It must not be repaired by adding coefficients after opening the result without a new preregistration.

---

## 6. Exact positive control: the already-known reduced bare propagator

The reduced TT pole gives

\[
e_{100}=-\frac1{18},
\qquad
e_{110}=-\frac1{72},
\qquad
e_{111}=0.
\]

The closed formulas produce

\[
\zeta_{4,bare}
=2\left(-\frac1{18}+\frac1{72}\right)
=-\frac1{12},
\]

and

\[
\eta_{2,bare}
=\frac15\left(-\frac1{18}\right)
+\frac45\left(-\frac1{72}\right)
=-\frac1{45}.
\]

The consistency identity is exact:

\[
-\frac1{18}
-4\left(-\frac1{72}\right)
+3(0)=0.
\]

Thus the extractor reproduces the frozen reduced-model result with no fit freedom.

---

## 7. What remains genuinely dynamical

The algebraic bridge is now closed:

\[
\boxed{
C_6
\to (a,b,c)
\to (\lambda_E,\lambda_{T_2})
\to K_{TT}
\to (e_{100},e_{110},e_{111})
\to (\eta_2,\zeta_4).
}
\]

The remaining unknown is not the extraction formula.  It is the **renormalized microscopic kernel itself**:

\[
C_6^{RG}(\omega,k;b)
\]

and its regulator/scale convergence.

The physical preregistration therefore asks whether

\[
\eta_2(b)\to\eta_2^{IR},
\qquad
\zeta_4(b)\to\zeta_4^{IR}
\]

while the leading `k^2` `E/T2` splitting goes to zero.

---

## 8. Falsification conditions

The physical branch fails if any of the following occurs:

- a finite direction-dependent leading `k^2` cone survives in the IR;
- TT poles become ghost/tachyonic;
- `eta2` or `zeta4` do not converge under the frozen blocking prescription;
- the three-direction identity remains violated in the scaling window;
- the answer depends materially on a regulator choice that is not an irrelevant deformation;
- the external observable requires post-hoc retuning of these coefficients.

This is the exact reason the project can now speak of a forthcoming **blind dimensionless gravitational prediction** rather than an unspecified future RG calculation.
