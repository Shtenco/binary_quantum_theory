# BF flatness versus GR: regular K5 curvature control

Status: **exact geometric negative control**.

The dual-K5 BF Hamiltonian in `K5_DUAL_BF_CONTROL.md` is an `EEF`-looking
projection of cycle flatness.  This file gives a simple geometric reason why
that is not the same as the Hamiltonian constraint of four-dimensional GR.

## 1. Intrinsic curvature of the regular K5 spatial triangulation

The boundary of a regular 4-simplex is a triangulation of `S^3` by five regular
tetrahedra.  Take every spatial edge length to be one.

A regular tetrahedron has interior dihedral angle

$$
\theta_3=\arccos\frac13.
$$

Every edge of the boundary 4-simplex belongs to exactly three tetrahedra, so
the three-dimensional Regge deficit at every one of the ten edges is

$$
\boxed{
\delta
=2\pi-3\arccos\frac13
=2.590307055157262\ldots
}
$$

and is manifestly not zero.

The Regge curvature sum is therefore

$$
\boxed{
\sum_e \ell_e\delta_e
=10\delta
=25.90307055157262\ldots
}
$$

For the convention

$$
\int d^3x\sqrt q\,R
\leftrightarrow
2\sum_e\ell_e\delta_e,
$$

this gives

$$
\boxed{
\int\sqrt q R
\simeq51.80614110314524.
}
$$

The five tetrahedra have total volume

$$
V_{tot}=5\frac{\sqrt2}{12}=0.5892556509887896\ldots
$$

so the corresponding average-curvature scale in this convention is

$$
\boxed{
\langle R\rangle_{Regge}
\simeq87.9179368347387.
}
$$

These numbers are only a normalization/control geometry; no continuum accuracy
is claimed for a five-tetrahedron triangulation.

## 2. Why this separates BF from GR

A nondegenerate BF flatness constraint requires trivial cycle holonomy,

$$
g_{cycle}=1,
$$

or its finite sign ambiguity in the projected formulation.  It therefore
removes precisely the kind of intrinsic cycle curvature represented by the
nonzero deficits above.

The canonical Hamiltonian constraint of four-dimensional GR does **not** say
that every spatial slice is intrinsically flat.  In real Ashtekar--Barbero/ADM
variables the intrinsic-curvature contribution is balanced by the
extrinsic-curvature kinetic sector (and, if present, matter and cosmological
terms).

Schematically,

$$
\boxed{
\text{GR constraint}
=\text{intrinsic curvature}
+\text{extrinsic-curvature terms}
+\Lambda/\text{matter}
=0,
}
$$

not

$$
\boxed{F=0.}
$$

Therefore an operator which enforces the Bonzom/Ooguri K5 flatness constraint
can have an elegant `EEF` form and a 15j physical kernel while still eliminating
spatial geometries which four-dimensional GR is allowed to carry.

## 3. Future regression use

The regular K5 geometry should be retained as a negative discriminator:

1. the BF control should detect nontrivial cycle curvature / fail flatness;
2. a genuine Lorentzian GR Hamiltonian should not reject the state merely
   because the intrinsic Regge deficit is nonzero;
3. it must instead test the full curvature-plus-extrinsic balance;
4. the large-spin/continuum version must recover the DeWitt kinetic signature
   and the nontrivial HDA structure function.

This is a cheap guard against accidentally returning to the topological BF
universality class while optimizing an `EEF`-looking finite Hamiltonian.
