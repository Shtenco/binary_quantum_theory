# First q=2 scalar effective-action attempt

Status: **exact local 1PI shape action derived; physical cosmological scalar action remains open.**

This calculation is deliberately fail-closed.  It starts from the already registered q=2 relational source positive control and asks whether the present source carrier is sufficient to produce a physical cosmological scalar kernel, dark-matter-like response, dark-energy-like background response, or gravitational lensing potentials.

The answer is now sharper than “not yet”: the current source layer yields a genuine exact local nonlinear 1PI action, but it spans the wrong local carrier for cosmological scalar gravity.  The missing directions can be identified explicitly.

## 1. Starting point

The registered finite relational source control has

\[
Z(j_X,j_Z)=\cosh r,
\qquad
r=\sqrt{j_X^2+j_Z^2},
\]

and

\[
W=\log Z=\log\cosh r.
\]

The mean field is radial,

\[
\mathbf m=\nabla_{\mathbf j}W,
\qquad
s=|\mathbf m|=\tanh r.
\]

Therefore

\[
r=\operatorname{artanh}s,
\qquad 0\le s<1.
\]

## 2. Exact local 1PI action

The Legendre transform is analytic:

\[
\boxed{
\Gamma_{shape}(s)
=s\,\operatorname{artanh}s
+\frac12\log(1-s^2)
}
\]

with

\[
\frac{d\Gamma}{ds}=\operatorname{artanh}s,
\qquad
\frac{d^2\Gamma}{ds^2}=\frac1{1-s^2}>0.
\]

Near the symmetric point,

\[
\boxed{
\Gamma_{shape}
=\frac{s^2}{2}
+\frac{s^4}{12}
+\frac{s^6}{30}
+\frac{s^8}{56}
+O(s^{10})
}
\]

and

\[
\lim_{s\to1^-}\Gamma_{shape}=\log2.
\]

This is the first exact nonlinear 1PI object obtained from the currently registered q=2 relational metric source.

It is still a positive-control 1PI object because the current C8 relational construction uses the declared control step `R=J`, not the actual graph-changing gravitational history.

## 3. Exact nonlinear metric volume

The exact q=2 face Gram matrix has determinant

\[
\boxed{
\det G(X,Z)
=\frac{(1-Z)[(Z+2)^2-3X^2]}{16}.
}
\]

For

\[
g(X,Z)=2\sqrt{\det G}\,G^{-1},
\]

one obtains

\[
\boxed{
\det g(X,Z)
=2\sqrt{(1-Z)[(Z+2)^2-3X^2]}.
}
\]

At the regular tetrahedron `(X,Z)=(0,0)` the linear intrinsic-volume response vanishes exactly.  Writing

\[
\ell_V=\frac12\log\det g,
\]

we find

\[
\left.\partial_X\ell_V\right|_0
=
\left.\partial_Z\ell_V\right|_0=0,
\]

and

\[
\boxed{
\left.\partial_A\partial_B\ell_V\right|_0
=-\frac38\delta_{AB}.
}
\]

Thus q=2 shape order changes the intrinsic volume from quadratic order onward.

This is **not** a dark-energy prediction.  `X` and `Z` are noncommuting quantum observables; their connected source Hessian cannot be reinterpreted as two simultaneously classical stochastic variables and inserted into the nonlinear determinant.  A vacuum/background backreaction requires the actual physical history/loop measure.

## 4. Exact conformal-mode obstruction

At the regular background

\[
g_0=
\begin{pmatrix}
2&1&1\\
1&2&1\\
1&1&2
\end{pmatrix},
\]

the registered metric tangents `M_X,M_Z` obey

\[
\boxed{
\operatorname{Tr}(g_0^{-1}M_X)=
\operatorname{Tr}(g_0^{-1}M_Z)=0.
}
\]

Their covariant shape Gram matrix is

\[
\boxed{
\operatorname{Tr}(g_0^{-1}M_Ag_0^{-1}M_B)
=\frac32\delta_{AB}.
}
\]

After whitening the background, the conformal direction is simply

\[
h_{conf}\propto I.
\]

Its projection onto the q=2 shape tangent vanishes exactly.

Hence the present q=2 source does **not** contain the spatial conformal/volume scalar that becomes the Bardeen potential `Phi` after a full scalar-gauge construction.

It also contains no independent lapse-response source, so it cannot supply `Psi` either.

This is a carrier no-go, not a numerical failure.

## 5. A local q=2 block is not a complete scalar shear carrier

The two q=2 shape directions span only a rank-two slice of the five-dimensional trace-free symmetric metric space.

In the orthonormal background frame, a unit scalar shear

\[
S(\hat n)=\sqrt{\frac32}
\left(\hat n\hat n^T-\frac13I\right)
\]

has direction-dependent overlap with the local q=2 shape tangent.  The exact gate gives, for example,

```text
100 : 1/9
010 : 1/9
001 : 1/9
110 : 25/36
111 : 0
```

so even the trace-free scalar-shear part cannot be identified with one universal local `X/Z` doublet before block transport and coarse graining.

## 6. Exact metric-tangent 1PI form

In the already registered flat-component convention,

\[
h=B\mathbf m,
\qquad
B^TB=\frac92I_2,
\]

so on the q=2 tangent

\[
s^2=\frac29\|h\|_F^2.
\]

Therefore

\[
\boxed{
\Gamma_{metric}[h]
=
\Gamma_{shape}
\left(\sqrt{\frac29\|h\|_F^2}\right)
}
\]

and

\[
\Gamma_{metric}
=
\frac19\|h\|_F^2
+\frac1{243}\|h\|_F^4
+\frac4{10935}\|h\|_F^6
+\cdots.
\]

The quadratic local kernel is

\[
\boxed{
K_{local}=\frac29P_{tangent},
}
\]

with rank two.

This reproduces and extends the previous zero-source pseudoinverse result: the whole local nonlinear potential is now known, not only its Hessian at the origin.

## 7. Interblock no-go from the presently justified source layer

Without adding a new microscopic history amplitude, the only justified multi-block extension of the registered finite source control is a product:

\[
Z_{N}=\prod_b Z_b,
\qquad
W_N=\sum_b W_b.
\]

Consequently

\[
\boxed{
\frac{\partial^2W_N}
{\partial j_{A,b}\partial j_{B,c}}
=0,
\qquad b\ne c.
}
\]

The connected cross-block Hessian is exactly zero.

On the dual `Q4` seed graph the local kernel is therefore identical on every graph-Laplacian eigenmode

\[
\lambda=0,2,4,6,8.
\]

No `k` dependence, no discrete Poisson denominator and no long-range scalar response can be obtained from the local source alone.

The existing nearest-block `S3` reduction shows how a genuine microscopic transfer will later generate an isotropic leading `k^2` symbol, but the six transfer amplitudes and their physical-history weighting remain open.

## 8. Immediate cosmological conclusion

From the current q=2 relational metric source alone,

\[
\boxed{
\rho_{hist}(a),\quad
\Phi(a,k),\quad
\Psi(a,k),\quad
\mu_{BQG}(a,k),\quad
\Sigma_{BQG}(a,k)
}
\]

are **not derivable**.

The reason is now decomposed into three exact missing ingredients:

1. **conformal/volume carrier** — absent from the fixed-spin `X/Z` source;
2. **lapse/clock-response carrier** — no physical lapse susceptibility is source-dressed in the projector;
3. **connected interblock physical history** — no nonfactorizing metric cumulant or momentum kernel exists yet.

## 9. The structurally preferred completion

The repository already points to a non-arbitrary candidate for item 1.

`FLUX_DEWITT_SIGNATURE_THEOREM.md` proves that common radial flux scaling

\[
E_f\to(1+\epsilon)E_f
\]

induces

\[
\delta q=q
\]

and has

\[
\boxed{Q_{DW}=-6},
\]

the unique local conformal DeWitt direction.

At fixed `j=1/2`, however, the face norm and absolute tetrahedral volume are frozen inside the two-dimensional intertwiner carrier.  `COLLECTIVE_J1_VOLUME_DYNAMICS.md` and `scripts/collective_volume_rg_gate.py` show that `j=1` is the first equal-spin four-valent sector in which the absolute volume is non-scalar.

The conditional symmetric blocking theorem supplies

\[
\boxed{
2\text{ active q=2 strands}
\longrightarrow
j=1.
}
\]

Therefore the next scalar construction should not invent a continuum scalar field.  It should source the already motivated collective radial/volume channel generated by representation growth.

See `Q2_COLLECTIVE_SCALAR_CARRIER.md`.

## 10. Reproduction

```bash
python scripts/q2_first_scalar_effective_action_gate.py \
  --output verification_results/Q2_FIRST_SCALAR_EFFECTIVE_ACTION.json
```

A green result certifies the exact local Legendre transform and the carrier/interblock obstruction.  It does **not** close `PHYSICAL_BACKGROUND_COSMOLOGY` or `PHYSICAL_SCALAR_COSMOLOGY`.
