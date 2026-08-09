# Off-shell habitat target for the graph-changing HDA

Status: **required target; stronger than fixed-graph projection and stronger than on-shell/group-averaged vanishing.**

## 1. Why group averaging alone is insufficient

The graph-changing correction in `GRAPH_CHANGING_HDA_TARGET.md` removes one
false requirement: a Thiemann/QSD Hamiltonian is allowed to change spin-network
graphs, so the HH commutator need not remain inside one fixed triangulation.

There is an opposite danger, however.  Testing only on fully diffeomorphism-
invariant/group-averaged states can be too weak, because the diffeomorphism
constraint itself vanishes there.

Lewandowski and Marolf introduced a vertex-smooth habitat precisely to make an
off-shell comparison possible.  They found that for a large class of
Thiemann-type proposals the Hamiltonian commutator vanishes identically on the
habitat even though the inverse-metric-weighted diffeomorphism generator has a
well-defined nontrivial action.  Thus

$$
\boxed{
[H[N],H[M]]'=0
}
$$

is **not** a satisfactory notion of quantum HDA closure when

$$
D[q^{ab}(N\partial_bM-M\partial_bN)]'\ne0.
$$

Primary references:

- T. Thiemann, QSD, arXiv:gr-qc/9606089.
- T. Thiemann, QSD III, arXiv:gr-qc/9705017.
- J. Lewandowski and D. Marolf, *Loop constraints: A habitat and their algebra*,
  arXiv:gr-qc/9710016.

## 2. Three levels which must not be conflated

### Level A -- kinematical covariance

The regulated Hamiltonian transforms covariantly under graph relabelings /
spatial diffeomorphisms:

$$
U(\phi)H[N]U(\phi)^{-1}=H[\phi_*N].
$$

Necessary, not sufficient.

### Level B -- on-shell/group-averaged closure

The commutator has the expected equivalence/vanishing property after complete
diffeomorphism group averaging.  Necessary for the physical Hilbert space, but
still too weak to detect the Lewandowski--Marolf failure mode.

### Level C -- off-shell habitat closure

On a space where infinitesimal vertex motion is represented nontrivially,

$$
\boxed{
[H[N],H[M]]'
\longrightarrow
i\hbar D[\beta]',
\qquad
\beta^a=q^{ab}(N\partial_bM-M\partial_bN).
}
$$

This is the target relevant to a continuum Dirac algebra claim.

## 3. Finite vertex-smooth analogue for the K5 programme

A finite test functional should depend on both the abstract spin network and
smooth vertex data,

$$
F_{f}[s]=F_f(\Gamma,j,\iota;x_1,\ldots,x_n),
$$

where `f(x_1,...,x_n)` is a declared smooth test function.  The dual action is

$$
(H'[N]F_f)[s]=F_f[H[N]s].
$$

For the first finite experiments choose a fixed basis of test functions before
looking at the HH output, for example

$$
1,
\quad x_v^a,
\quad x_v^ax_w^b,
\quad e^{ik\cdot x_v}
$$

with low momenta only.

The constant functional is only a normalization/control channel.  A correct
off-shell test **must include functions with nonzero derivatives**, otherwise a
wrong identically-zero commutator can pass trivially.

## 4. Discrete simplex structure function

The independently verified classical 4-simplex benchmark gives

$$
\boxed{
\{H(k),H(k')\}
=
\frac{1}{3V_{tet}}
\left[D(k'k)-D(kk')\right].
}
$$

Therefore the finite quantum test should use the same boundary geometry and
compare the dual HH action with the dual of this explicit tangential
vertex-deformation vector field.

For a smooth test function `f`, the right-hand side is evaluated as a
first-order differential operator,

$$
D_{kk'}f
=
\sum_v \delta x_v^a(kk')\,\frac{\partial f}{\partial x_v^a}.
$$

This gives a nonzero scalar benchmark even when the Hamiltonian itself changes
the graph.

## 5. Preregistered defect

For each declared geometry, lapse pair and test functional define

$$
\boxed{
\Delta_{HH}^{off}[f]
=
\frac{
\left|
([H[N],H[M]]'F_f)[s]
-i\hbar(D[\beta]'F_f)[s]
\right|
}{
|([H[N],H[M]]'F_f)[s]|
+|\hbar(D[\beta]'F_f)[s]|
+\varepsilon
}.
}
$$

The aggregate gate is the maximum over a preregistered small basis of
nonconstant low-frequency `f`, not the minimum and not a post-hoc selected
functional.

A second diagnostic should explicitly report

$$
R_{zero}
=
\frac{
\|[H,H]'F\|
}{
\|D'F\|
}
$$

on channels where `D'F` is known to be nonzero.  A systematic
`R_zero -> 0` is the Lewandowski--Marolf ultralocal/zero-commutator failure
mode, not a PASS.

## 6. Relation to the K5 automorphism quotient

The exact K5 `S5` quotient already reduces the first safe HH column from 305
spin assignments to 26 abstract spin-graph orbits.  This is useful as a label-
removal preprocessing step, but

$$
\boxed{
S_5\text{ automorphism quotient}\ne\text{full diffeomorphism habitat}.
}
$$

It does not represent continuous vertex motion and therefore cannot by itself
supply the structure function.

## 7. Efficient next calculation

Before implementing the full 11-million-state Lorentzian support, do the
following smaller test:

1. freeze one regular/nondegenerate 4-simplex geometry;
2. choose two nonconstant low-order vertex-smooth functionals `f1,f2`;
3. compute the classical `D(k,l)f` values exactly;
4. attach the same vertex data to the first regulator-safe `Jmax=5/2` quantum
   reachable states;
5. evaluate the dual Euclidean HH response on those functionals;
6. check explicitly whether the old commutator is nontrivial in the same
   channels as the classical `D` action.

This will reveal immediately whether the current regularization has the known
`[H,H]'=0` habitat pathology.  Only after this test is understood should the
full real-SU(2) Lorentzian correction be used for the expensive off-shell
closure calculation.
