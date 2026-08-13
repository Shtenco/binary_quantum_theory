# Graviton helicity qubit, candidate infoton and vacuum-foam bridge

Status: **exact finite spin gate + conditional vacuum/resonance extension**.

This note sharpens the statement “graviton spin and infoton spin are bits”. The exact statement is subtler and stronger:

> a massless spin-2 graviton has two physical helicities, `+2` and `-2`, so its physical polarization space is two-dimensional and can be encoded as one logical qubit; four microscopic spin-1/2 qubits are the minimum number that can carry a collective `j=2` sector.

A two-state label by itself does **not** determine Lorentz spin. Therefore a proposed information quantum must acquire a definite transformation law before it can be called spin-2.

## 1. Four microscopic qubits contain one spin-2 sector

The already used tetrahedral face-qubit Hilbert space obeys

```text
(1/2)^4 = 2 x j=0 + 3 x j=1 + 1 x j=2.
```

The dimensions are

```text
2 + 9 + 5 = 16.
```

The `j=2` irrep has Casimir

```text
J^2 = j(j+1) = 6
```

and five magnetic states `m=-2,-1,0,+1,+2`.

The extremal states are exactly

```text
|+2> = |up up up up>
|-2> = |down down down down>.
```

The finite gate verifies `J^2=6`, `Jz=+2/-2`, and zero leakage of both states out of the `j=2` projector.

No set of fewer than four spin-1/2 constituents can reach total `j=2`, because `j_max=N/2`.

## 2. Why the physical graviton is a logical qubit

A generic massive spin-2 representation has five spin projections. A massless graviton has gauge redundancy and only two propagating tensor helicities. Choosing the propagation axis, the physical basis can be written

```text
|R> = |h=+2>
|L> = |h=-2>.
```

Linear `+` and `x` gravitational-wave polarizations are superpositions of these two helicities. Thus the **polarization** of one graviton is a qubit.

This does not mean that a graviton has only two possible occupation numbers. A gravitational-wave mode remains bosonic. The appropriate mode Hilbert space is schematically

```text
Fock occupation  x  C^2_helicity.
```

This distinction is crucial for vacuum fluctuations: the bit labels polarization; the bosonic oscillator supplies zero-point fluctuations and arbitrary occupation number.

## 3. Project definition of a CIMFIG “infoton”

The word `infoton` is used here only as a project-local name for a **candidate route/information-sector bosonic collective mode**. No Landauer-mass formula or external particle claim is imported.

Its polarization may be binary, but binary polarization alone does not fix spin. There are two sharply different possibilities:

1. **scalar/vector route mode** — it may carry information but cannot linearly hybridize with a graviton helicity `+/-2` channel;
2. **TT rank-2 collective route mode** — four or more microscopic route qubits can carry a `j=2` tensor channel, and its two massless helicities can form an information-sector logical qubit analogous to the graviton helicity qubit.

Therefore the theory gets a falsifier:

> direct graviton-infoton mode mixing requires a nonzero TT spin-2 component in the information-sector operator. If the microscopic route sector is purely scalar, the proposed linear resonance is forbidden by representation mismatch.

## 4. Quantum foam: what the bits do and what they do not do

A useful microscopic picture is

```text
smooth mean geometry
+ zero-mean quantum fluctuations
= fluctuating microscopic geometry.
```

The helicity bit alone is not the vacuum fluctuation. The fluctuation comes from the quantum state of the bosonic mode:

```text
<delta g> = 0,
<delta g^2> > 0.
```

The binary sector tells us which tensor polarization the fluctuation occupies. The oscillator/Fock sector tells us its amplitude statistics.

This gives a precise interpretation of “quantum foam” inside the candidate architecture: local geometry can have nonzero quantum variance even when its coarse-grained expectation approaches a smooth metric.

## 5. A new conditional prediction from the already frozen smoothing exponent

The repository measured a coarse-graining defect exponent

```text
delta g ~ b^-2.001707.
```

Suppose — this is an additional physical identification, not yet an established fact — that this quantity is the RMS of a stationary three-dimensional vacuum metric fluctuation with low-k power spectrum

```text
P_delta_g(k) ~ k^n.
```

For a self-similar coarse window in three spatial dimensions,

```text
Var(delta g_R) ~ R^-(3+n),
RMS(delta g_R) ~ R^-(3+n)/2.
```

Therefore

```text
n = 2p - 3
  = 2*2.001707 - 3
  = 1.003414.
```

So the candidate vacuum would not be independent white-noise bits. White noise would give `n=0` and RMS exponent `3/2`. The measured exponent, if reinterpreted as a quantum RMS, instead points to

```text
P_delta_g(k) ~ k^1.003414  as k -> 0.
```

That is a hyperuniform-like long-wavelength suppression: microscopic fluctuations may be strong while long-wavelength geometry becomes unusually smooth.

This is a **conditional blind prediction**. It can be falsified by a future direct computation of the quantum two-point function. If the true vacuum correlator does not reproduce this low-k law, the RMS interpretation of the old smoothing exponent is wrong.

## 6. How a gravitational wave can amplify a vacuum information mode

The symmetry-compatible interaction with any information sector is of the form

```text
H_int = -1/2 integral h_TT_ij T_I^ij d^3x.
```

A nonzero coupling requires a TT component of the information-sector stress/operator.

If a passing coherent gravitational wave periodically modulates the frequency of a bosonic information mode, the mode equation has Mathieu form

```text
q_ddot + omega_I^2 [1 + xi*h*cos(Omega_GW t)] q = 0.
```

Here `xi` is the dimensionless microscopic coupling that the present theory has **not yet derived**.

The first parametric instability band is centered at

```text
Omega_GW ~= 2 omega_I.
```

At exact resonance and weak modulation,

```text
mu ~= |xi*h| omega_I / 4,
```

where `mu` is the Floquet/squeezing growth exponent. The leading half-width is

```text
|Omega_GW - 2 omega_I| <~ |xi*h| omega_I / 2.
```

Quantum mechanically this is a squeezing / pair-excitation channel: the background wave supplies energy and amplifies vacuum fluctuations. It is not extraction of free energy from the vacuum.

A separate direct mode-conversion channel is possible if graviton and information modes have the same spin-2 quantum numbers and a bilinear mixing term; that resonance is centered at `omega_g ~= omega_I`. The parametric vacuum channel and the direct conversion channel are physically distinct.

## 7. Finite numerical resonance gate

The executable gate uses a deliberately visible test modulation `xi*h=0.02` and `omega_I=1`.

At `Omega_GW=2 omega_I` it obtains

```text
mu_numeric  = 0.004999941407...
mu_leading  = 0.005
relative error = 1.17e-5.
```

Off resonance at `1.8 omega_I` and `2.2 omega_I`, the Floquet growth is numerically zero at the gate tolerance.

Thus the resonance mechanism itself is verified. What is **not** verified is that nature supplies a CIMFIG infoton or a large enough coupling `xi`.

For orientation only, inserting `h=1e-21`, `f_GW=100 Hz`, and `xi=1` gives a resonant information-mode frequency of `50 Hz` and an e-folding time of roughly `4.0e11 years`. This is not a model prediction; it shows that present-day weak strains would produce a negligible direct effect unless the coupling, strain, coherence time, or early-universe conditions are very different.

## 8. What this closes and what it does not

### Closed / finite

- four spin-1/2 qubits contain exactly one `j=2` irrep;
- the extremal `m=+/-2` states form an exact two-state code inside that irrep;
- four is the minimal number of spin-1/2 microscopic bits capable of reaching `j=2`;
- the Mathieu/Floquet resonance gate reproduces the weak-modulation growth law and negative controls.

### Conditional but now sharply testable

- interpreting the frozen `delta g` exponent as quantum RMS predicts `P(k) ~ k^1.003414`;
- a TT information mode can resonantly mix with gravitational waves;
- a quadratic TT coupling gives vacuum squeezing near `Omega_GW=2 omega_I`.

### Still open

- derive the information-mode action from the microscopic route Hamiltonian;
- derive `xi` rather than introduce it as a coupling placeholder;
- compute the true vacuum two-point function and confirm or reject the hyperuniform inference;
- prove unitarity/positive quantum measure for the Lorentzian history;
- take the uniform joint `Jmax -> infinity`, `epsilon -> 0` limit;
- connect the resulting spectrum to a physical absolute scale and blind observations.

## 9. Relation to external primary literature

The representation-theory direction is consistent with the existence of qubit/spin models whose low-energy sector contains helicity `+/-2` modes; see Gu and Wen, arXiv:0907.1203. Quantum graviton vacuum/coherent/squeezed fluctuations have been studied using influence-functional methods; see Cho and Hu, arXiv:2112.08174. Gravitational-wave backgrounds can also affect quantum vacuum sectors in explicit field models; see Jones et al., arXiv:1706.09402.

These papers motivate mechanisms only. They do not validate the specific CIMFIG infoton hypothesis.

## Status

**Candidate-theory extension.** The spin-2 qubit decomposition is exact finite mathematics. The foam interpretation and graviton-infoton resonance are conditional physical hypotheses with explicit falsifiers and a missing microscopic coupling derivation.
