# Sharp-spin linear metric-response obstruction

## Result

The current six-column collective carrier `W_g` is an exact dynamical Hilbert-space carrier, but the original sharp all-`j=1/2` Peter-Weyl seed is **not** yet a semiclassical background with a nonzero linear expectation-value metric response.

The reason is a representation-sector selection rule, not a numerical accident.

## 1. Direct-sum structure

The spin-network Hilbert space decomposes into orthogonal fixed-irrep sectors

\[
\mathcal H=\bigoplus_{\mathbf j}\mathcal H_{\mathbf j}.
\]

The homogeneous seed lies in one sharp sector `j0` with every microscopic edge at `j=1/2`.

Every basis state entering the strict-interior `q=4` columns used to build `W_g` changes exactly four microscopic doubled-spin labels. Therefore

\[
P_{\mathbf j_0}W_g=0,
\qquad \langle\Omega_0|W_g=0.
\]

This orthogonality is already checked by `collective_l1_microscopic_edge_lift_gate.py`.

## 2. Flux metric is spin preserving

Flux generators act inside a fixed SU(2) irrep. Products such as

\[
\hat Q^{ab}\sim \hat J^a\hat J^b
\]

and volume/flux functions can mix intertwiner labels at fixed edge spins, but do not change the edge representation labels themselves. Hence for every spin-preserving geometric observable `O_g`,

\[
P_{\mathbf j}\,O_g\,P_{\mathbf j'}=0\qquad(\mathbf j\ne\mathbf j').
\]

Therefore

\[
\boxed{\langle\Omega_0|O_g|w_A\rangle=0}
\]

for each column of `W_g`.

## 3. Consequence for direct metric calibration

For

\[
|\psi(q)\rangle=\frac{|\Omega_0\rangle+W_gq}{\sqrt{1+q^Tq}},
\]

a spin-preserving metric observable has no term linear in `q`:

\[
\left.\frac{\partial\langle O_g\rangle}{\partial q_A}\right|_{q=0}=0.
\]

Thus the linear calibration matrix required by the DeWitt extractor,

\[
B_{eA}=\left.\frac{\partial\langle \hat y_e\rangle}{\partial q_A}\right|_0,
\]

obeys

\[
\boxed{B=0}
\]

on the sharp-spin seed whenever `y_e` is built from spin-preserving flux/metric observables.

Accordingly the current sharp-spin seed cannot be used to turn the Hilbert-space `W_g` coordinates into a classical linear metric perturbation by expectation values. Any `c_eff` obtained by setting `B=I` here would be a coordinate convention, not a BCQG derivation.

## 4. Required resolution

The collective GR science run must use a target-independent background with overlapping representation support, for example a Gauss-projected coherent/refinement packet, and demonstrate directly that its metric-response Jacobian `B` is nonsingular and stable under refinement.

This does **not** invalidate the six-edge carrier. The previous exact results remain:

- 24 fine Euclidean source directions;
- exact six-channel intrinsic boundary image;
- exact six-edge/Sym^2 metric representation isomorphism;
- canonical six-column microscopic isometry.

What changes is the status of the word `metric`: on the sharp seed the six channels are a **metric-labelled dynamical carrier**, while a classical metric tangent requires a coherent background with nonzero linear response.

## 5. Photon consequence

The same selection rule clarifies the optical interpretation.

On a sharp-spin background a spin-preserving metric/Hodge observable has no first-order expectation shift along a single `W_g` excitation, so a classical mean fringe displacement need not appear at first order. Quantum fluctuations can nevertheless enter the path coherence

\[
\mathcal C_{12}=\langle\Psi_g|U_2^\dagger U_1|\Psi_g\rangle
\]

at second order, producing phase variance and potentially visibility loss.

On a coherent background with nonzero `B`, the standard linear eikonal phase channel is restored. This gives two experimentally distinct regimes rather than forcing a classical metric interpretation onto a sharp spin-network basis state.

## Status

`PROVED_SELECTION_RULE` for spin-preserving geometric observables on the frozen sharp-spin seed. Construction and validation of the coherent collective background remain open.
