# Physical C6 closure: the entire spin-2 frontier is two scalar functions

Status: **exact S4/representation reduction plus EFT matching conditions.  The remaining numerical task is to compute the momentum derivatives of these functions from the frozen microscopic dynamics.**

The phrase “compute the full `6x6` kernel” overstates the physical number of unknowns.  On the six unordered edges of a tetrahedral block,

\[
C_6(\omega,\mathbf k)=aI+bA_{adj}+cO_{opp}
\]

has irreducible channels

\[
A_1\oplus E\oplus T_2.
\]

The trace mode `A1` is removed from the physical TT sector.  Therefore the whole traceless spin-2 problem is exactly two scalar functions.

---

## 1. Exact reduction

Define

\[
P_5=P_E+P_{T_2},
\]

\[
\boxed{
Q_{tet}=\frac35P_E-\frac25P_{T_2}.
}
\]

The irrep eigenvalues are

\[
\lambda_E=a-2b+c,
\qquad
\lambda_{T_2}=a-c.
\]

Define their dimension-weighted mean and difference:

\[
\boxed{
\kappa_5
=\frac{2\lambda_E+3\lambda_{T_2}}5,
}
\]

\[
\boxed{
\Delta_{ET}
=\lambda_E-\lambda_{T_2}
=2(c-b).
}
\]

Then identically on the five-dimensional traceless metric carrier,

\[
\boxed{
C_5(\omega,\mathbf k)
=\kappa_5(\omega,\mathbf k)P_5
+\Delta_{ET}(\omega,\mathbf k)Q_{tet}.
}
\]

This is not an approximation.  The normalization of `Q_tet` is chosen so that its E/T2 eigenvalue difference is exactly one:

\[
\frac35-\left(-\frac25\right)=1.
\]

Therefore the coefficient multiplying `Q_tet` is literally the E/T2 eigenvalue difference.

---

## 2. GR/HDA infrared conditions

A flat, parity-even, reciprocal gravitational fixed point must not contain a physical TT mass or a finite leading spin-2 polarization anisotropy.

Accordingly the small-derivative expansion must satisfy, after the common field normalization is chosen,

\[
\kappa_5(\omega,\mathbf k)
=Z_T\left[
-\omega^2+c_T^2k^2
+c_T^2a_*^2\eta_2 k^4
+O(\partial^6)
\right],
\]

while the tetrahedral splitter must begin beyond the two-derivative Einstein term:

\[
\boxed{
\Delta_{ET}(\omega,\mathbf k)
=Z_Tc_T^2a_*^2\gamma_4 k^4
+O(\partial^6)
}
\]

in the simplest parity-even single-`Q_tet` quartic sector.

More generally, a complete off-shell derivative expansion may contain independent quartic structures involving `omega^4` and `omega^2 k^2`; the physical dispersion coefficient is obtained after solving the pole.  What is forbidden at an Einstein/DeWitt IR fixed point is a surviving `Q_tet` contribution at order

```text
partial^0, omega^2, or k^2
```

that produces a finite mass, kinetic-residue split or direction/polarization-dependent leading light cone.

These are direct falsifiers rather than quantities to be absorbed into `eta2` or `zeta4`.

---

## 3. Two Wilson derivatives

Once a frozen low-momentum interpolation of the microscopic kernel exists, the physical quartic information is reduced to:

1. the scalar spin-2 four-derivative coefficient in `kappa5`;
2. the tetrahedral four-derivative coefficient in `Delta_ET`.

Schematically, in an on-shell spatial convention,

\[
\boxed{
\eta_2
=\frac{1}{Z_Tc_T^2a_*^2}
\left[\text{coefficient of }k^4\text{ in }\kappa_5\right],
}
\]

\[
\boxed{
\gamma_4
=\frac{1}{Z_Tc_T^2a_*^2}
\left[\text{coefficient of }k^4\text{ in }\Delta_{ET}\right].
}
\]

No generic tensor fit remains.

The exact TT representation theorem then gives

\[
\boxed{\zeta_4=\gamma_4/4.}
\]

Thus the physical frontier is

```text
microscopic Peter-Weyl dynamics
 -> a(omega,k), b(omega,k), c(omega,k)
 -> kappa5(omega,k), Delta_ET(omega,k)
 -> TWO four-derivative Wilson coefficients
 -> eta2_IR, gamma4_IR
 -> zeta4_IR = gamma4_IR/4
 -> scalar dispersion + fixed polarization birefringence pattern
```

---

## 4. Why the local 8.43% number is not yet gamma4

At the first q4 refined tangent level the repository has measured

\[
\frac{\Delta_{ET}}{\kappa_5}=0.08430036026012608.
\]

That calculation is a local Euclidean tangent Gram at one refinement scale.  It does **not** separate

- zero-derivative onsite response;
- two-derivative interblock transport;
- four-derivative irrelevant operators;
- frequency dependence;
- Feshbach/return corrections.

Therefore the legal inference is only

\[
\boxed{
0.08430036\ \text{is a nonzero microscopic spin-2 tetrahedral anisotropy precursor}.
}
\]

The illegal shortcut is

\[
0.08430036=\gamma_4^{IR}=4\zeta_4^{IR}.
\]

The full depth-two calculation now being sharded measures the next dynamical local return.  The subsequent interblock/momentum calculation must determine the derivative order and coefficient.

---

## 5. Where momentum comes from

A parent-only block return gives an onsite contribution.  Physical spatial momentum requires transport between coarse blocks.  In a local coarse basis `P,Q`, write

\[
C_{6,PQ}(\omega)
\]

and Fourier/normal-mode transform the spatial block indices:

\[
\boxed{
C_6(\omega,\mathbf k)
=\sum_{\delta} C_6^{(\delta)}(\omega)
 e^{i\mathbf k\cdot\delta}.
}
\]

For a real reciprocal parity-even sector, opposite transports pair so that the physical quadratic kernel is even in momentum.  Odd tetrahedral pseudoscalars belong to the separate orientation/mirror sector and are not silently mixed into the parity-even gravity prediction.

The already-proved PL Galerkin identity

\[
P^TL_{g+1}P=\frac14L_g
\]

fixes the purely geometric rescaling, but it cannot determine the nonseparable Peter-Weyl E/T2 transport coefficients.  Those are the remaining microscopic dynamical data.

---

## 6. Minimal cross-block target

The next calculation does not need an arbitrary long-range matrix.  Locality requires measuring the first nonvanishing block-separation classes and checking decay of further classes.

For neighboring tetrahedral blocks, the shared-face stabilizer strongly reduces the cross-kernel.  After projection to the physical metric/TT sector, only the Wilson combinations contributing to `kappa5` and `Delta_ET` are retained.

The preregistered hierarchy is therefore:

1. onsite full-E depth-two return;
2. nearest-block full-E depth-two transfer;
3. next-separation locality control;
4. low-momentum symbol;
5. `kappa5`, `Delta_ET` derivative extraction;
6. TT poles and the three-direction/birefringence identities.

This is a finite calculation chain, not an unspecified future RG programme.

---

## 7. Rotational restoration clarified

A finite `zeta4` multiplying `a_*^2 k^4` is an **irrelevant** anisotropic correction.  It does not prevent the leading IR light cone from becoming rotationally invariant because

\[
\frac{a_*^2k^4}{k^2}=a_*^2k^2\to0
\qquad (k\to0).
\]

Therefore the correct IR requirement is not necessarily `zeta4 -> 0`.  The hard requirement is

\[
\boxed{
\text{no surviving anisotropy at derivative order }\le2.
}
\]

Two physically distinct outcomes are both admissible:

- `gamma4 -> 0`: rotational symmetry is restored faster than the leading irrelevant order;
- `gamma4 -> finite`: the theory retains a Planck/block-scale suppressed directional memory while still approaching an isotropic Einstein light cone at low energy.

Failure occurs if an anisotropic mass, `omega^2` residue or `k^2` cone split survives the declared continuum/RG limit.

---

## 8. Final physical dictionary

The gravity/light sector can now be written as

\[
\boxed{
q=2
\to D_{space}=3
\to z\simeq1
\to E\oplus T_2
\to C_5=\kappa_5P_5+\Delta_{ET}Q_{tet}
\to K_{TT}
\to (\eta_2,\gamma_4)
\to \zeta_4=\gamma_4/4
\to \{v_g,\delta\phi,\Delta v_{pol},\Delta\phi_{pol}\}
\to \text{blind experiment}.
}
\]

Everything after the two microscopic Wilson derivatives is algebraically fixed.  The remaining calculation is to obtain those derivatives from the frozen interblock Peter-Weyl dynamics with controlled refinement and regulator errors.
