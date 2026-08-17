# Newton constant: physical metric normalization and soft-coupling protocol

Status: **parameter-identification protocol; no numerical physical G is claimed.**

The hypersurface-deformation algebra fixes the relative gravitational tensor structure in the declared ADM family, but it does not fix the overall normalization of the action.  Therefore a numerical Newton constant cannot be read from HDA closure alone.

A second subtlety is field normalization: a graviton two-point residue by itself is not an invariant value of `G` if the metric perturbation can still be rescaled arbitrarily.

---

## 1. Freeze the metric variable geometrically first

The candidate construction has an explicit shape-to-metric map.  In the physical multi-block theory this map must be extended to a dimensionless metric variable `g_mu_nu` whose normalization is fixed by geometric length/angle observables.

Once this geometric convention is frozen, an arbitrary rescaling

```text
h -> lambda h
```

is no longer a harmless field convention: it would change the relation between `h` and measured geometry.

This is the prerequisite for interpreting the 1PI curvature coefficient physically.

---

## 2. Read G from the physical 1PI curvature coefficient

In the Einstein scaling window write

\[
\Gamma[g]
= C_R\int d^4x\sqrt{-g}\,R+\cdots.
\]

In the standard convention

\[
C_R=\frac1{16\pi G}.
\]

Therefore, after the metric normalization and action/quantum normalization are frozen,

\[
\boxed{G=\frac1{16\pi C_R}.}
\]

The coefficient must come from the **physical** history/1PI action, not the constraint spectral resolvent alone.

---

## 3. Dimensionless first prediction

Let `a_*` be the physical coarse length unit of the scaling window.  Define

\[
\boxed{g_N=G/a_*^2.}
\]

The first zero-fit gravitational-strength prediction is `g_N`, entirely in internal geometric units.

The absolute conversion to SI units requires the same common length/action calibration used by the rest of the physicalization programme.  This calibration is performed only after all dimensionless predictions are frozen.

---

## 4. Independent soft-graviton cross-check

Canonical normalization of the graviton can be written conventionally as

\[
g_{\mu\nu}=\eta_{\mu\nu}+\kappa h^{(c)}_{\mu\nu},
\]

with

\[
\boxed{\kappa^2=32\pi G}
\]

in the standard four-dimensional Einstein convention.

The soft-graviton theorem requires the same `kappa` for every matter/gauge species in the Lorentz-invariant massless-spin-2 regime.

Thus the project obtains an independent consistency triangle:

```text
geometric metric normalization
        | \
        |  \ physical 1PI R coefficient
        |   \
        v    v
      G_from_R  <---->  G_from_soft_kappa
```

The two determinations must agree within regulator/refinement/truncation errors.

---

## 5. Why the two-point residue is not enough by itself

For a canonical field rescaling `h_c -> lambda h_c`, the quadratic residue and interaction coupling transform inversely.  An isolated residue can therefore be changed by convention.

What is physical is the combined relation between

- the geometrically normalized metric perturbation;
- the kinetic/1PI coefficient;
- the universal soft coupling to conserved energy-momentum.

The repository must not identify a finite Regge/Peter-Weyl residue with `G` unless this normalization triangle has been completed.

---

## 6. Relation to Planck length

After `G` and the quantum action normalization are fixed,

\[
\ell_P^2=\frac{\hbar G}{c^3}.
\]

In natural units this is often written `l_P^2=G`, but that is a unit convention, not an independent prediction.

The theory should therefore freeze dimensionless ratios such as `G/a_*^2` before presenting a Planck-length conversion.

---

## 7. Falsification gates

A claimed Newton constant requires:

1. physical-projector/history/refinement convergence;
2. a geometrically normalized emergent metric;
3. a stable local Einstein coefficient `C_R` in the 1PI derivative expansion;
4. positive TT residue;
5. universal soft coupling in the matter/gauge sectors;
6. agreement of `G_from_R` and `G_from_soft`;
7. no gravitational datum used to tune the microscopic branch before freeze.

---

## 8. Canonical arrow

\[
\boxed{
\text{shape/length geometry}
\to g_{\mu\nu}^{phys}
\to \Gamma[g]
\to C_R
\to G
\leftrightarrow
\kappa_{soft}.
}
\]

This is the legitimate route to Newton's constant.  HDA closure, a finite TT residue, or an arbitrary Peter-Weyl eigenvalue alone is insufficient.
