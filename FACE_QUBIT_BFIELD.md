# Face-qubit -> adjoint two-form blocking

Status: **exact finite gauge-covariance identity for a candidate microscopic variable; dynamics and geometrogenesis remain open**.

## Minimal local carrier

The Plebański bridge needs an internal triplet of two-form coefficients `B^i`, `i=1,2,3`.  This does **not** require three independent qubits on each face.

For one qubit density operator `rho_f` on an oriented microscopic 2-cell `f`, define its Bloch vector

\[
\boxed{
b_f^i={\rm Tr}(\rho_f\sigma^i),
\qquad i=1,2,3.
}
\]

The three Pauli expectation values are the three real components of one binary quantum degree of freedom.  Under an internal frame change

\[
\rho_f\mapsto U_f\rho_fU_f^\dagger,
\qquad U_f\in SU(2),
\]

the Bloch vector transforms in the adjoint `SO(3)` representation.

Thus the microscopic roles can be cleanly separated:

\[
\boxed{
\text{oriented face }f
\times
\text{one qubit Bloch vector }b_f^i
\longrightarrow
\text{adjoint-valued discrete 2-form coefficient}.
}
\]

The face supplies the 2-cell/cochain degree; the qubit supplies the internal `i=1,2,3` degree.  No metric area is assigned at this stage.

## Gauge-covariant blocking

Let `P_f in SU(2)` parallel-transport the local face frame to one chosen block frame.  A block coefficient can be formed from transported local density operators,

\[
\mathcal B_{\rm block}
=
\sum_{f\subset B}
\epsilon_f\,
P_f\rho_fP_f^\dagger,
\]

or equivalently at the adjoint level

\[
B_{\rm block}^i
=
\sum_{f\subset B}
\epsilon_f\,
R(P_f)^i{}_j b_f^j,
\]

where `epsilon_f=+/-1` is the combinatorial orientation and `R(P)` is the `SO(3)` adjoint rotation.  More generally the sum is performed separately for each coarse 2-cell rather than collapsing all faces into one coefficient.

Under independent local frame changes `g_f` and one block-frame change `G`,

\[
\rho_f\to g_f\rho_fg_f^\dagger,
\]

\[
P_f\to G P_f g_f^\dagger.
\]

All arbitrary local gauges cancel, leaving only

\[
\boxed{
B_{\rm block}\to R(G)B_{\rm block}.
}
\]

Therefore gauge-invariant internal contractions and the Plebański simplicity defect do not depend on arbitrary microscopic frame choices.

## Finite verification

`scripts/face_qubit_bfield_gate.py` tests 32 random trials with 17 face qubits per block.

Worst numerical errors are approximately

\[
\boxed{
\epsilon_{SU(2)\to SO(3)}=2.0\times10^{-16},
}
\]

\[
\epsilon_{R^TR-I}=9.2\times10^{-16},
\qquad
|\det R-1|=7.8\times10^{-16},
\]

and for independent gauge rotations on all faces,

\[
\boxed{
\epsilon_{\rm block,cov}=2.74\times10^{-15},
\qquad
\epsilon_{\|B\|}=2.66\times10^{-15}.
}
\]

Thus the proposed microscopic-to-coarse variable is algebraically gauge-covariant to machine precision.

## What one qubit does **not** provide

This construction must not be overinterpreted.

A single qubit does not encode:

- a complete continuum two-form by itself;
- a metric area of its face;
- a graviton;
- Plebański simplicity;
- four dimensions;
- the Einstein equations.

Those properties can emerge only collectively from the pattern of many oriented faces, their incidence relations, their edge transports and the frozen dynamics.

## Candidate microscopic state

The gravity-specific microscopic portion of CIMFIG can therefore be sharpened to

\[
\boxed{
\Omega_{\rm grav}
=
(K_2,\{\rho_f\}_{f\in K_2},\{U_e\}_{e\in K_1}),
}
\]

where `K_2` is an oriented causal 2-complex or the 2-skeleton of a dynamically generated complex, `rho_f` are face qubits and `U_e in SU(2)` are edge transports.

Gauge transformations act locally in the usual connection/adjoint manner.  The coarse-graining map to `B^i` is fixed before dynamics is tested.

The still-missing object is **not** the kinematic map.  It is the frozen local update law for

\[
(K_2,\rho_f,U_e)
\longrightarrow
(K'_2,\rho'_f,U'_e)
\]

that must dynamically generate the required dimension, simplicity and Einstein defects.

## Downstream gates

If a frozen rule is supplied, the same generated ensemble can be passed through the existing chain:

\[
\boxed{
\text{face qubits + edge transport}
\to B^i_b
\to \Delta_{\rm simp}(b)
\to g_U(b)
\to A_B(b)
\to \Delta_{\rm ASD}(b)
\to \text{Regge/FP/EH/Ward cross-checks}.
}
\]

The key scientific requirement is that none of the desired sectors be restored by a post-hoc projection.

## Reproduction

```bash
python scripts/face_qubit_bfield_gate.py \
  --faces 17 \
  --trials 32 \
  --output verification_results/face_qubit_bfield_gate.json
```
