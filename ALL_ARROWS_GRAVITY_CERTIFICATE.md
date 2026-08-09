# All-arrows gravity certificate

Status: **maximal composed mathematical/numerical bridge currently supported by the repository; the microscopic geometrogenesis arrow remains open**.

## 1. Correct dependency graph

The gravity programme is no longer a single fragile chain.  It has one common microscopic/coarse entrance and two independent downstream routes:

\[
(K_2,\rho_f,U_e)_{micro}
\dashrightarrow B^i_b
\]

followed by

\[
\boxed{
B^i_b
\to
\Delta_{simp}
\to g_U
\to A_B
\to F(A_B)
\to Einstein
}
\]

and the independent cross-check

\[
\boxed{
g_U
\to Regge
\to Fierz\text{--}Pauli
\to Einstein\text{--}Hilbert\ cubic
\to W_3\to0.}
\]

Regge is therefore a cross-validation branch, not a logically necessary intermediate step in the Plebański route.

## 2. Conditional bridge theorem

Suppose one frozen microscopic rule has a scaling window in which:

1. an oriented four-dimensional continuum complex emerges without a dimensional scaffold;
2. the blocked face-qubit variables define a nondegenerate adjoint-valued two-form triplet $B^i$;
3. the Plebański simplicity defect tends to zero;
4. a local compatible connection exists with $D_AB^i\to0$;
5. its curvature satisfies
   \[
   \bar F^{ij}\to0,
   \qquad
   \operatorname{Tr}F\to-\Lambda=\text{constant};
   \]
6. the appropriate Lorentzian reality conditions hold.

Then the Urbantke metric reconstructed from $B$ satisfies the vacuum Einstein equation

\[
\boxed{R_{\mu\nu}=\Lambda g_{\mu\nu}}
\]

in that continuum limit.  The tracefree part of the self-dual matrix $F^{ij}$ is not a defect: it is self-dual Weyl curvature.

Thus the conceptual burden of the gravity problem has moved upstream.  Once the correct simple $B$ phase is dynamically generated, the remaining classical GR bridge is highly constrained.

## 3. Single-data-path numerical control

`QUBIT_TO_EINSTEIN_END_TO_END.md` and `scripts/qubit_to_einstein_end_to_end.py` force the early arrows to act on the same face-qubit input data.

Positive control: unit Euclidean $S^4$ encoded only into six qubit density matrices per sample point.  Downstream reconstruction receives no metric, tetrad or connection.

| observable | result |
|:--|--:|
| qubit -> $B$ decoding error | `0.0` |
| max $\Delta_{simp}$ | `2.1274680382e-16` |
| max Urbantke conformal metric error | `3.3306690739e-16` |
| max $D_AB$ residual | `6.1920200345e-17` |
| max $\Delta_{ASD}$ | `8.6321136850e-09` |
| reconstructed $\Lambda$ | `2.999999897308107` |
| relative error vs exact $\Lambda=3$ | `3.4230631070e-08` |
| constancy defect of $\operatorname{Tr}F$ | `6.3528924421e-09` |

The strongest positive-control defect is therefore about

\[
\boxed{3.43\times10^{-8}}
\]

when the recovered cosmological curvature is included.

Negative control: a smooth, simple, nondegenerate, conformally-flat but non-Einstein geometry is encoded through the same face-qubit interface.  It passes qubit decoding, simplicity, Urbantke reconstruction and connection compatibility, but

\[
\boxed{
\min \Delta_{ASD}=0.737225989.
}
\]

The positive/negative separation in the ASD observable is approximately

\[
\boxed{8.54\times10^7}.
\]

Thus the composed test rejects the wrong geometry at the Einstein-curvature arrow instead of merely recognizing smoothness.

## 4. Independent Regge universality branch

The fixed-4D Regge branch tests different observables and does not use the Plebański curvature criterion as an input.

Existing finite-size exponents include:

- exact Regge gauge -> metric leakage: about `2.24--2.29`;
- full Fierz--Pauli matrix residual: about `1.77--2.10`;
- Fierz--Pauli coefficient-ratio error: about `2.02--2.48`;
- quadratic EH normalization error: about `1.87`;
- cubic EH normalization error: about `1.82`;
- nonlinear $c_3/c_2$ error: about `1.91`;
- cubic Ward defect: about `2.23` on the clean window.

Across these independent observables the mean exponent is

\[
\boxed{p=2.071}
\]

with between-observable standard deviation

\[
\boxed{0.215}.
\]

A conservative synthesis is therefore

\[
\boxed{
\epsilon_{Regge\to GR}\sim L^{-2.1\pm0.2},
}
\]

consistent with one leading $O(a^2)$ lattice-irrelevant correction.

A pooled log fit of the 42 underlying finite-size points, allowing a separate amplitude for every observable, gives approximately

\[
p=2.219\pm0.050,
\]

but this formal fit uncertainty must not be interpreted as a precision critical exponent because the observables are correlated and the scaling windows are short.

## 5. Dimension arrow: strongest current result is still negative/open

The calibrated dimension-blind null model gives for minimal binary reconvergence

\[
d_H\to1.992,
\qquad
d_s=2.0698\pm0.0181,
\]

so binary reconvergence by itself does **not** generate four dimensions.

There is a conditional structural selector:

\[
B\in\Omega^2,
\qquad F(A)\in\Omega^2,
\qquad B\wedge F\in\Omega^4.
\]

If the emergent microscopic action is required to be metric-free and built only from this $B$/$F$ sector with no extra degree-completing field or background volume form, top-form closure selects

\[
\boxed{d=4}.
\]

This is a structural condition, not a dynamical proof.  Independent topology, diffusion and dynamical-scaling gates must still return the same dimension from the frozen ensemble.

## 6. Arrow ledger

| arrow | current status |
|:--|:--|
| frozen causal/frame quantum rule -> ensemble | **OPEN** |
| face qubit + edge transport -> adjoint $B^i$ | **finite algebraic PASS** |
| ensemble -> 4D manifold/scaling phase | **OPEN; minimal null rule FAILS** |
| simple nondegenerate $B$ -> Urbantke metric | **finite/exact control PASS** |
| $B$ -> compatible $A_B$ | **finite algebraic/numerical PASS** |
| $(B,A_B,F)$ -> Einstein criterion | **single-path finite control PASS** |
| Einstein metric -> two graviton helicities in continuum perturbation theory | **conditional continuum result** |
| microscopic ensemble -> exactly two gapless physical modes | **OPEN** |
| reconstructed metric -> Regge -> FP/EH | **finite scaling evidence PASS** |
| nonlinear Regge Ward restoration | **finite scaling evidence PASS** |
| Lorentzian reality/unitary quantum measure | **OPEN** |
| chiral anomaly-free matter | **OPEN** |
| blind experimental prediction | **OPEN** |

## 7. Scientific conclusion

The statement supported now is stronger and narrower than `bits produce gravity`:

\[
\boxed{
\text{if a frozen microscopic face-qubit/connection dynamics produces the required simple 4D }B\text{-phase,}
\text{ then two independent downstream routes are already consistent with Einstein gravity.}
}
\]

The unresolved problem is not another coefficient of the Einstein action.  It is the upstream geometrogenesis/RG problem:

\[
\boxed{
\text{ONE FROZEN LOCAL RULE}
\dashrightarrow
\left(
D_{link}\to4,
\ d_s\to4,
\ z\to1,
\Delta_{simp}\to0,
\Delta_{ASD}\to0,
N_{gapless}=2
\right)
}
\]

in one common scaling window, without post-hoc projection or parameter changes.

Until that happens, the full microscopic theory is not closed.  If it does happen, the classical gravity part is no longer a vague analogy: the Plebański route supplies a direct conditional theorem to Einstein geometry, while the Regge branch supplies an independent $O(a^2)$ universality cross-check.
