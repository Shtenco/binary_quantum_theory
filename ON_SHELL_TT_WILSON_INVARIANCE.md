# On-shell TT Wilson invariance: why the physical quartic prediction is six numbers

Status: **exact EFT/on-shell statement at leading four-derivative order around the massless Einstein TT pole.**

The complete spatial quartic TT quotient in `S4_TT_QUARTIC_COMPLETE_BASIS.md` has dimension six.  A natural question is whether a more general off-shell kernel containing `omega^4` and `omega^2 k^2` terms introduces additional physical coefficients.

For pole propagation, it does not: off-shell redundancies collapse onto the same six-dimensional on-shell quartic space.

---

## 1. Leading physical TT kernel

After the lower-derivative HDA/Einstein gates pass, choose a common positive field normalization so that

\[
\boxed{
K_0(\omega,\mathbf k)
=Z_T\left(-\omega^2+c_T^2k^2\right)I_{TT}.
}
\]

The leading massless pole is

\[
\omega^2=c_T^2k^2.
\]

Write the four-derivative correction as

\[
K=K_0+a_*^2\delta K_4+O(a_*^4\partial^6).
\]

`delta K4` may contain `omega^4`, `omega^2 k^2`, and `k^4` tensor structures off shell.

---

## 2. Local field redefinitions

Consider any parity-even local two-derivative field redefinition on the TT carrier,

\[
h\mapsto\left(I+a_*^2R_2(\omega,\mathbf k)\right)h.
\]

To first order in `a_*^2`, the quadratic kernel transforms as

\[
K\mapsto
K+a_*^2\left(R_2^\dagger K_0+K_0R_2\right)
+O(a_*^4).
\]

Therefore

\[
\boxed{
\delta K_4
\sim
\delta K_4+R_2^\dagger K_0+K_0R_2.
}
\]

All four-derivative terms proportional to the leading equation of motion are redundant for the pole location.

---

## 3. Pole shift is field-redefinition invariant

Let `epsilon_sigma` be a normalized leading TT polarization.  The first correction to the pole depends on

\[
\epsilon_\sigma^\dagger
\delta K_4
\epsilon_\sigma
\]

evaluated at

\[
\omega^2=c_T^2k^2.
\]

For a redundant shift,

\[
\epsilon_\sigma^\dagger
\left(R_2^\dagger K_0+K_0R_2\right)
\epsilon_\sigma=0
\]

on the leading pole.

Hence the first quartic pole correction is invariant under these local field redefinitions.

---

## 4. omega-dependent structures collapse into spatial degree four on shell

At parity-even four-derivative order the possible frequency powers are

```text
omega^4
omega^2 * (spatial degree 2)
spatial degree 4.
```

On the leading pole,

\[
\omega^2=c_T^2k^2,
\]

so

\[
\omega^4\to c_T^4(k^2)^2
\]

and

\[
\omega^2P_2(\mathbf k)\to c_T^2k^2P_2(\mathbf k).
\]

Both are homogeneous spatial degree-four tensors.

After imposing

\[
\operatorname{tr}h=0,
\qquad h_{ij}k_j=0,
\]

they therefore lie in the same exact six-dimensional quotient

\[
\boxed{
\mathcal W^{(4)}_{TT,S_4}
=\operatorname{span}\{W_1,\ldots,W_6\}.
}
\]

Thus the **off-shell** effective action can have more bookkeeping coefficients, but the leading physical quartic **pole response** is still described completely by six dimensionless numbers.

---

## 5. Physical definition of the six-vector

The clean observable-level definition is:

1. obtain the converged/Feshbach TT kernel `K_TT(omega,k)`;
2. verify the common massless leading pole and positive residue;
3. solve the two pole branches perturbatively or numerically at small `k`;
4. define

\[
\omega_\sigma^2
=c_T^2k^2\left[
1+a_*^2k^2e_{4,\sigma}(\hat n)+O(a_*^4k^4)
\right];
\]

5. use the frozen six-observable extractor to reconstruct

\[
\boxed{\mathbf c^{IR}=(c_1,\ldots,c_6)^{IR}.}
\]

This definition is insensitive to operators proportional to the leading TT equation of motion.

---

## 6. Consequence for eta2/zeta4

If the six-vector lies in the scalar-cubic nested subspace, `eta2` and `zeta4` are likewise on-shell pole coefficients.

They should be extracted from the pole branches or from an explicitly on-shell-reduced kernel, not from arbitrary off-shell Hessian entries.

The same applies to the single-`Q_tet` birefringence amplitude `gamma4`.

---

## 7. Failure condition

If different field/operator parametrizations give different extracted `c1...c6` **after solving the same physical poles and applying the same scale convention**, the extraction procedure is wrong or the derivative expansion is outside its controlled regime.

This supplies another implementation-level falsifier before external data are opened.
