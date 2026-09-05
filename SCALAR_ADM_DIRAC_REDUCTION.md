# Scalar ADM Dirac reduction and q=2 exact seed

Status: **exact reduction algorithm + one exact local conformal-volume seed; theory-specific physical scalar kernel still requires microscopic history entries.**

This note starts strictly after the already-derived local q=2 shape 1PI and collective j=1 volume carrier.  It does **not** return to the Hamiltonian/HDA/projector construction.

The target scalar basis is

\[
\chi_{\rm scalar}=(\delta N,\,B,\,\zeta,\,E,\ldots).
\]

The central rule is that lapse and longitudinal shift are constraint variables until the physical history proves otherwise.  They are never promoted to propagating scalar modes by numerical inversion of a singular block.

## 1. Two legal quadratic reductions

Write

\[
K=
\begin{pmatrix}
K_{cc}&K_{cp}\\
K_{pc}&K_{pp}
\end{pmatrix},
\]

where `c` denotes auxiliary/constraint variables and `p` the retained response variables.

If `K_cc` is exactly invertible, the legal finite reduction is

\[
\boxed{
K_{\rm red}=K_{pp}-K_{pc}K_{cc}^{-1}K_{cp}.
}
\]

The new gate proves that this object is invariant under every invertible redefinition of the constraint coordinates.

If lapse/shift are strict Lagrange multipliers, `K_cc` is singular or zero and the Schur formula is **not** used with a pseudoinverse.  Instead the multiplier equations

\[
A p=0
\]

are imposed first, the quadratic form is pulled back to `ker A`, and only then are gauge directions quotiented.

This distinction is essential: a Moore--Penrose inverse of a zero multiplier block can leave a nonzero apparent scalar stiffness even when the exact constraint plus gauge quotient has zero physical scalar dimension.

## 2. Exact controls

`scripts/scalar_adm_dirac_response_gate.py` contains three separate controls.

### Pure-gravity-like scalar control

One multiplier imposes

\[
\zeta=0,
\]

while `E` is a gauge direction.  The exact reduced scalar dimension is

\[
\boxed{0}.
\]

A naive pseudoinverse treatment of the singular multiplier block would instead retain a rank-one quadratic form.  The gate therefore explicitly detects the spurious-mode failure mode.

### Genuine extra-scalar control

Add one gauge-invariant scalar `s` with

\[
K_s(\omega,k)=\omega^2-\frac14k^2-2.
\]

The same constraint/gauge reduction leaves exactly one physical scalar, with

\[
\omega^2=\frac14k^2+2,
\qquad
\frac{\partial K_s}{\partial\omega^2}=1>0.
\]

Thus the engine distinguishes a real extra pole from a constraint artefact.

### Conserved matter/probe control

For flat Fourier momentum

\[
q_\mu=(-\omega,0,0,k),
\]

the gate constructs one symmetric scalar stress tensor satisfying

\[
\boxed{q_\mu T^{\mu\nu}=0}.
\]

The same `T^{mu nu}` generates both the `Psi` and spatial-trace/`Phi` source components.  There is no independent lensing normalization.  This is a reference interface only; the BQG normalization still has to come from the same physical history/one-scale convention.

## 3. New exact q=2 conformal-volume seed

The j=1 normalized volume control already gives

\[
\Gamma_V(p)
=p\log p+(1-p)\log(1-p)-p\log2+\log3,
\qquad p_0=\frac23.
\]

Define the local logarithmic mean-volume coordinate

\[
\boxed{
\zeta_V=\frac13\log\frac{p}{p_0}
}
\]

so that

\[
p=p_0e^{3\zeta_V},
\qquad
\frac{V}{V_0}=e^{3\zeta_V}.
\]

This is the same local volume law as the conformal metric parametrization

\[
q_{ij}=e^{2\zeta}q^{(0)}_{ij}.
\]

At the symmetric point the exact derivatives are

\[
\Gamma_V'(0)=0,
\]

\[
\boxed{\Gamma_V''(0)=18},
\]

\[
\Gamma_V'''(0)=216,
\qquad
\Gamma_V''''(0)=3078.
\]

Therefore the first exact local scalar-ADM seed contains one known entry,

\[
\boxed{K_{\zeta_V\zeta_V}^{\rm local}=18},
\]

in the **kinematic j=1 positive-control normalization**.

This is not yet the physical FLRW/Bardeen `zeta`: the physical history still has to fix how the coarse volume source is weighted and normalized.

## 4. Known-mask scalar block

The current honest local seed in the basis

\[
(\delta N,B,\zeta_V,E)
\]

is

\[
K_{\rm seed}=\begin{pmatrix}
?&?&?&?\\
?&?&?&?\\
?&?&18&?\\
?&?&?&?
\end{pmatrix}.
\]

The question marks are **unknown microscopic-history entries**, not zeros.

The exact fixed-spin `X/Z` shape sector remains linearly orthogonal to the conformal direction and is not renamed `zeta_V`.

## 5. Interblock momentum seed

The tetrahedral nearest-neighbor geometry obeys

\[
\sum_a n_a n_a^T=\frac43 I.
\]

Hence if the future connected physical history supplies one reciprocal scalar nearest-neighbor transfer amplitude `tau` and physical edge scale `a`, then

\[
\tau\sum_a\left[1-\cos(a\,k\cdot n_a)\right]
=
\boxed{\frac23\tau a^2 k^2}+O(k^4).
\]

The isotropic `k^2` coefficient is therefore geometrically fixed once `tau` is actually derived.  Neither `tau` nor the common physical scale is fitted here.

## 6. Production fail-closed contract

The reduction engine accepts `BQG_SCALAR_ADM_BLOCK_V1` packets.  A reduced kernel may be labelled physical only if all of the following are explicit:

```text
theory_specific_history
volume_to_zeta_normalization_derived
lapse_response_derived
longitudinal_shift_response_derived
connected_interblock_kernel
ward_identity_certified
conserved_source_coupling
```

and the packet carries nonempty hashes for the physical history, volume source, lapse response, shift response, Ward certificate and source coupling.

If any item is absent,

```text
physical_kernel_emitted = false
science_status = REDUCTION_ONLY_PHYSICAL_INPUTS_INCOMPLETE
```

This is intentional.  A local volume Hessian, a lapse cochain or a constraint-resolvent transfer coefficient is not silently promoted to

\[
\Gamma_{\rm scalar}^{(2)}(\omega,k).
\]

## 7. What is now actually left

The algebra of scalar constraint/gauge reduction is no longer an open design problem.  The remaining inputs are concrete microscopic outputs:

1. projected lapse-response susceptibility and couplings to the volume/shear response;
2. longitudinal shift/shear constraint-response block;
3. connected interblock scalar transfer amplitudes from the theory-specific physical history;
4. one conserved matter/probe coupling with a Ward certificate;
5. the physical coarse-volume normalization that turns the kinematic `zeta_V` coordinate into the physical scalar response variable.

Once these entries exist, the existing production engine gives the reduced kernel without a new formalism:

\[
\boxed{
K_{\rm ADM}\to K_{\rm red}\to
\Gamma_{\rm scalar}^{(2)}(\omega,k)
}
\]

and only then may poles, residues, `c_s^2`, `mu_BQG` and `Sigma_BQG` be read.
