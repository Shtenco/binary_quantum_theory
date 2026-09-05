# BQG physical-history adapter — shortest no-new-formalism route

Status: **executable adapter contract.** This document does not redefine the physicalization architecture. It connects the actual BQG graph-changing constraint family to the already existing relational Hilbert/history, source, Gamma and observable machinery.

## 1. What is already done and must be reused

The repository already contains:

1. the finite master-constraint theorem and spectral physical projector;
2. an exact C8 constrained relational Hilbert/history sector;
3. exact gauge-invariant relational source operators;
4. an executable `P -> O_rel -> Z[J] -> W[J] -> Gamma^(2)` finite source bridge;
5. a geometric-boundary-time protocol for physical `omega`;
6. TT, six-Wilson and real-observable dictionaries;
7. Regge/TT normalization controls and a reduced connected TT propagator positive control.

Therefore none of these objects is to be re-invented for scalar cosmology or dark-sector work.

## 2. The only microscopic adapter that remains

The production input must be one common regulated habitat carrying the actual constraint family

\[
\boxed{
\mathcal C_{BQG}^{(\epsilon)}
=\{H^E_v,\ H^L_v,\ D_I\}
}
\]

unless a stated subset has already been exactly reduced or proved redundant on that same habitat.

From it construct

\[
\boxed{
\mathbb M_{BQG}
=\sum_A C_A^\dagger C_A
}
\]

(or the preregistered positive label metric generalization), followed by the exact or controlled near-zero physical sector

\[
\boxed{P_{BQG}}.
\]

No observable parameter is used in constructing this projector.

## 3. Reuse the existing history/source stack unchanged

Once `P_BQG` is available, the downstream path is the already registered one:

\[
\boxed{
P_{BQG}
\to O_{rel}
\to Z_{BQG}[J]
\to W_{BQG}[J]
\to \Gamma_{BQG}.
}
\]

The new executable `scripts/bqg_physical_history_adapter_gate.py` regression-tests this interface on the existing C8 relational control by reconstructing its physical projector from the constraint `C=I-G` alone. The reconstructed projector must agree with the analytic `P_rel`, and the resulting source and metric Hessians must reproduce the existing exact q=2 source gate.

This makes the eventual replacement

```text
C8 combined constraint
        ->
actual {H_E,H_L,D}
```

a change of input, not a change of physicalization formalism.

## 4. Three sectors of one generating functional

Dark matter, lensing and dark energy are not separate phenomenological models. They are possible sectors of the same `Gamma_BQG`.

### Scalar finite-frequency/momentum sector

After the already required scalar gauge/Dirac reduction,

\[
\Gamma^{(2)}_{scalar}(\omega,k)
\]

classifies the result as:

- analytic/contact response;
- constraint/Poisson long-range response;
- or an additional genuine propagating scalar pole.

Only the last case can be discussed as an extra physical scalar degree of freedom. A modified Poisson response can mimic dark-matter phenomenology without a new particle, but must also pass the universal conserved-source and lensing tests.

### TT sector

\[
\Gamma^{(2)}_{TT}(\omega,k)
\]

feeds the already closed six-Wilson and real-observable map. No new TT observable dictionary is needed.

### Homogeneous background sector

\[
\Gamma_{FLRW}[a,N]
\]

must come from absolute physical history amplitude ratios with one fixed normalization convention. Background-by-background normalization is forbidden because it can erase a genuine volume/vacuum term.

From the same functional one may derive

\[
\rho_{hist}(a),\quad p_{hist}(a),\quad w_{hist}(a).
\]

## 5. Production bundle contract

Every actual BQG constraint-history bundle must freeze before diagonalization:

- regulator/refinement level;
- common habitat/basis identity;
- `H_E` ordering and normalization;
- `H_L` ordering, epsilon convention and relative coefficient convention;
- diffeomorphism/route constraint convention or explicit proof of prior reduction;
- boundary embedding and refinement map;
- source-operator definitions;
- hashes of all input matrices/operators.

The adapter must fail closed if any required operator is missing or acts on a different habitat.

## 6. Forbidden shortcuts

The following do not count as physicalization:

```text
P_boundary M P_boundary -> call its kernel P_phys
constraint resolvent z -> rename z as omega
K1 Gram eigenvalue -> call it physical mass/gap
j=1 volume eigenvalue -> call it dark energy
observer smoothing b^-2 -> call it 1/k^2 propagator
missing H_L or D -> fit a phenomenological correction
normalize Z[a;0]=1 separately for every background -> infer Lambda=0
```

## 7. Current actual BQG input status

The regulator-safe Euclidean calculations already show that the bare 32D q=2 boundary carrier has no common five-node Euclidean zero direction and that its first outgoing layer has full rank 160. These are input diagnostics, not physical observables.

The sharded full 24-term Lorentzian epsilon calculation was cancelled by the CI runner during its heavy amplitude step; no physical zero/nonzero conclusion follows from that cancellation.

The Euclidean `K1` Ritz second-action calculation is running independently. Its result is a dressing diagnostic, not yet `P_BQG` because the common-habitat full `H_L + D` family is still required.

## 8. Shortest legal programme

\[
\boxed{
\{H_E,H_L,D\}
\to P_{BQG}
\to \text{existing relational/history stack}
\to \text{existing }Z/W/\Gamma
\to
\begin{cases}
\Gamma^{(2)}_{scalar}(\omega,k),\\
\Gamma^{(2)}_{TT}(\omega,k),\\
\Gamma_{FLRW}[a,N]
\end{cases}
\to \text{existing observable dictionaries}.
}
\]

This is the production programme. No dark-matter or dark-energy parameter is allowed to enter before the final sector diagnostics are computed.
