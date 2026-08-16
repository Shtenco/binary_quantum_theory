# BCQG collective depth-two gravitational return — preregistration

## Purpose

The homogeneous direct gravitational six-edge block is structurally zero:

\[
P_g H_E P_g=0,\qquad P_gSP_g=0,
\qquad P_gGP_g=0,
\]

where `P_g=W_g W_g^dagger` and, at `beta=hbar=1`,

\[
G=-\frac23E-\frac{32}{9}S.
\]

Therefore the first nontrivial gravitational metric dynamics must be measured through excursions outside the six-edge carrier and return.

This file freezes the first **denominator-free** depth-two observable before its full `E/S` amplitudes are known.

## 1. Projected outgoing columns

Let

\[
Q_\perp=1-P_0-P_g
\]

on the declared first-block boundary Hilbert space, with `P_0` the normalized static background projector. If later dynamical support reveals additional retained zero-order states, their projector must be declared before recomputing the science result; they may not be added after inspecting the GR target.

Define

\[
X_E=Q_\perp E W_g,
\qquad
X_S=Q_\perp S W_g.
\]

The denominator-free channel matrices are

\[
\boxed{L_{EE}=X_E^\dagger X_E},
\]

\[
\boxed{L_{SS}=X_S^\dagger X_S},
\]

\[
\boxed{L_{ES}=X_E^\dagger X_S+X_S^\dagger X_E}.
\]

All three are Hermitian; `L_EE` and `L_SS` are positive semidefinite, while `L_ES` need not be.

## 2. Signed full geometry combination

Because

\[
G=aE+bS,
\qquad a=-\frac23,\quad b=-\frac{32}{9},
\]

we have the exact algebraic identity

\[
\boxed{
L_G=(Q_\perp GW_g)^\dagger(Q_\perp GW_g)
=\frac49L_{EE}+\frac{1024}{81}L_{SS}+\frac{64}{27}L_{ES}.
}
\]

The coefficient `64/27` multiplies the already symmetrized cross matrix `L_ES=X_E^dagger X_S+X_S^dagger X_E`. No additional factor of two is permitted in the collector.

The collector must store `L_EE`, `L_SS` and `L_ES` separately before forming `L_G`.

## 3. S4 reduction

For an exactly homogeneous first block, each Hermitian return matrix is `S4` invariant and is determined by three representative real matrix elements

```text
a = diagonal / same edge
b = adjacent edge
c = opposite edge
```

with

\[
\boxed{\lambda_{A_1}=a+4b+c},
\qquad
\boxed{\lambda_E=a-2b+c},
\qquad
\boxed{\lambda_{T_2}=a-c}.
\]

The producer computes amplitudes without using any GR target. The external universality analysis may then transport the channels through the measured metric map.

## 4. Metric calibration transport

The independently measured first-block map obeys

\[
M_{hq}^TM_{hq}
=\frac16(P_{A_1}+P_E)+\frac13P_{T_2}.
\]

Consequently a physical metric Hessian with equal `E` and `T2` eigenvalues corresponds at this finite block to the raw `q`-space ratio

\[
\lambda_{T_2}^{(q)}=2\lambda_E^{(q)}.
\]

If a later **physical effective Hamiltonian Hessian** has the DeWitt value `c=1/2`, its blind raw-coordinate ratio is

\[
\lambda_{A_1}^{(q)}:\lambda_E^{(q)}:\lambda_{T_2}^{(q)}
=-\frac12:1:2.
\]

These ratios are external discriminators only. They must not be inserted into the return-amplitude producer.

## 5. Strict-E precursor

Before the full production `E` calculation, one computational control is allowed:

\[
E_{strict}=\sum_{u=1}^{24}E_u^{strict},
\]

where each chamber contributes only its unique plaquette/source word whose entire active cone is internal to the chosen coarse tetrahedron.

This sector is the same strict-interior construction that generates the six-edge carrier. Its first-step q4 support has maximum doubled spin 2. In a second strict word the source `c` link can be hit at most twice and every plaquette link at most once, so

\[
\boxed{j_{max}^{strict\ E^2}=2}
\]

is an exact strict-only wall.

The strict result is labelled

`STRICT_E_DEPTH2_RETURN_PRECURSOR`

and may not be substituted for the complete `E` term in `L_G`.

## 6. Acceptance / diagnostics

Every amplitude-level return result must report:

- exact support / cutoff used;
- boundary/outside-label leakage;
- background-return amplitude;
- direct return into all six `W_g` directions;
- `Q_perp` representative values `(a,b,c)`;
- `A1/E/T2` eigenvalues;
- imaginary/Hermiticity defects;
- S4 covariance checks;
- worker/shard provenance;
- no target-dependent support pruning.

For `L_EE` and `L_SS`, negative irrep eigenvalues beyond numerical tolerance are an implementation/definition failure because these matrices are Gram matrices.

## 7. What this observable is not

`L_G` is **not** yet the physical Feshbach/Schrieffer-Wolff effective Hamiltonian. It contains no energy denominator. Therefore no `c_DeWitt_eff` is reported from `L_G` alone.

A physical second-order scalar requires a separately frozen resolvent such as

\[
-P C Q\,(Q C_0Q-E_0)^{-1}Q C P,
\]

with its spectrum/conditioning reported before the external GR comparison.

## Status

`PREREGISTERED_DENOMINATOR_FREE_DEPTH2_RETURN`.
