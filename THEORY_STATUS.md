# Theory status — canonical ledger

**Frozen working frontier: 2026-08-15.**

The repository now develops **BCQG Candidate Theory v1.1**: a mathematically/computationally specified candidate quantum-gravity theory. It is **not** experimentally established and does not by itself establish antigravity, a fifth force, a new particle, or a dimensional physical energy scale.

Canonical entry points:

```text
START_HERE.md
BCQG_CANDIDATE_THEORY_V1_1.md
BCQG_CORE_CANDIDATE_V1.md
THEORY_STATUS.md
theory_gates.json
```

---

## 1. Kinematic and dimensional core — tested finite / conditional continuum

The frozen chain is

```text
binary routes
-> q=2
-> octahedral S2 local shell
-> minimal flag / recursive PL S3
-> d_space~3
-> z~1
-> 4D-like history.
```

Numerical anchors:

```text
d_H          = 2.999229782
z            = 0.998281156
d_s(slice)   = 3.004393867
d_s(history) ~ 4.004393867
16-cell seed Betti=(1,0,0,1)
PL tetrahedra: 16 -> 384 -> 9216.
```

The minimal flag globalization is part of the candidate definition. The stronger statement that the bare causal graph uniquely forces every possible nonflag globalization is not asserted.

---

## 2. Physical Euclidean ordering — preregistered finite PASS

The production Euclidean operator is

\[
\boxed{H_E^{sine}=(T-T^\dagger)/(2i)},
\qquad
\boxed{K=[V,H_E^{sine}]}.
\]

The preregistered physical-sine two-node gate gives

```text
support(H0)=support(H1)=37
||H0||=2.1712581763270546
||H1||=2.171258176327055
support([H0,H1])=514
||[H0,H1]||=2.8794538147049544
p_cross=1.0056948923496356
p_GG=2.007490390559045
p_joint=1.0076444430189475
Delta_joint(1/64)=0.020030338775070305.
```

No channel-dependent normalization/subtraction or post-result threshold change was used.

---

## 3. Quantum route normal — tested finite, including spin-changed sectors

Expectation-first square-root maps are nonlinear on superpositions and are retained only as semiclassical controls.

The quantum candidate is

\[
\boxed{
R_{op}[N]=\frac12\left\{N,
\sqrt{\hat Q^{ab}\hat P_a\hat P_b}
\right\}.
}
\]

Positivity follows from

\[
\hat Q^{ab}\hat P_a\hat P_b
=\sum_iB_i^\dagger B_i\ge0.
\]

The initial exact shared `4x4` sector gives

```text
Delta_R(1/64)=8.205159710207802e-7
p_R=0.9999594708960342.
```

More importantly, five distinct genuine higher-spin sectors reached by `H_E^sine` give

```text
p_R in [0.9998813243, 0.9999820816]
endpoint defects in [9.37065e-7, 3.63658e-6]
minimum checked spectral eigenvalue ~= -1.07e-14.
```

Thus the operator-first HDA mechanism survives actual geometry change on the checked sectors rather than only a logical expectation-valued surrogate.

Evidence:

```text
verification_results/PETER_WEYL_OPERATOR_ROUTE_SPINCHANGED_BLOCKS.json
run 31858615323
artifact 9244277324
sha256:c1af8de00183fddf328f6bdfba386e2320b842e10d3de98d90ad150b0876213c
```

---

## 4. Lorentzian amplitude, phase, sign and relative magnitude

The exact environment-unbiased raw logical one-body amplitude is

\[
\boxed{L_{raw,1body}=i\,1.3389293521464034\,Y+O(10^{-16})}.
\]

The nested K-K-V structure contains five Poisson brackets, hence

\[
\boxed{(1/i)^5=-i}.
\]

The code-bound Euclidean normalization is

\[
\boxed{H_E^{phys}=-\frac{2}{3\hbar}E_{raw}}.
\]

The Thiemann correction then fixes the Lorentzian relative sign and magnitude upstream. At `beta=hbar=1`:

\[
\boxed{
G_v=-\frac23E_v+\frac{32i}{9}L_{raw,v}.
}
\]

Equivalently, relative to the phase-completed Hermitian block `H_phase=-iL_raw`,

```text
bare repo H_L/H_phase = -16/9
full beta=1 correction/H_phase = -32/9.
```

These coefficients are not HDA fit parameters.

---

## 5. New finite result — Lorentzian multi-node environment correlations

The successful exact MITM environment-trace artifacts were reassembled before the final environment trace.

With source node `0`, nodes `3,4` fixed at `K=0`, and nodes `1,2` varied over `K=0/2`, the exact diagonal-environment Walsh decomposition gives coefficient-vector norms

```text
source local             = 0.33709171624286727
source x node1           = 0.03631787483605024
source x node2           = 0.006983526478664483
source x node1 x node2   = 0.01396705295732858.
```

Dominant raw pseudoscalar terms are

```text
Y I I   = +i 0.335901403339900
Y Z1 I  = -i 0.007028617222480
Y I Z2  = +i 0.002338130606599
Y Z1 Z2 = +i 0.004676261213198.
```

The reconstruction error is at most `1.11e-16`; worker physical leakage is at most `6.70e-16`.

Interpretation: the environment-unbiased one-body `Y` is the partial-trace result of a finite logical structure that contains neighbor-dependent diagonal correlations before tracing.

Scope restriction: the historical workers measured diagonal environment matrix elements only. Off-diagonal environment transitions remain unmeasured, so these coefficients are **not yet the complete physical multi-qubit Lorentzian Hamiltonian**.

Evidence:

```text
LORENTZIAN_MULTI_NODE_ENVIRONMENT_CORRELATION.md
verification_results/PETER_WEYL_LORENTZIAN_ENVTRACE_WALSH_NODE012.json
```

---

## 6. Signed operator-first full-HDA closure — conditional theorem

The current full candidate is

\[
\boxed{H[N]=G[N]+R_{op}[N]}.
\]

For smooth lapse probes

\[
N=\bar N+\epsilon n,
\qquad
M=\bar M+\epsilon m,
\]

the pure geometry antisymmetric smear satisfies

\[
N_0M_1-N_1M_0=O(\epsilon)
\]

with no zeroth-order term.

For a geometry change in the operator-first route sector, writing

\[
\Delta R_M=\frac{\bar M}{\epsilon}\Delta\widetilde\Omega+\Delta S_m,
\qquad
\Delta R_N=\frac{\bar N}{\epsilon}\Delta\widetilde\Omega+\Delta S_n,
\]

the apparent inverse-epsilon mixed term cancels algebraically in

\[
N_v\Delta R_M-M_v\Delta R_N.
\]

At every fixed regulator-safe finite Peter-Weyl cutoff, the local signed geometry operator is bounded. Since the diffeomorphism target on the frozen WKB family is `O(epsilon^-1)`,

\[
\boxed{C_{G\times R}/D=O(\epsilon)},
\qquad
\boxed{C_{GG}/D=O(\epsilon^2)}.
\]

Together with the tested operator-first route convergence on genuine spin-changed sectors,

\[
\boxed{
\Delta_{full}
=\Delta_{R,op}+O(\epsilon)+O(\epsilon^2)
\longrightarrow0
}
\]

on the declared fixed-cutoff WKB habitat.

This is a **conditional asymptotic closure theorem**, not an unconditional theorem on the full Hilbert space.

Evidence:

```text
FULL_OPERATOR_FIRST_HDA_CERTIFICATE.md
scripts/full_operator_first_hda_theorem_gate.py
verification_results/PETER_WEYL_OPERATOR_ROUTE_SPINCHANGED_BLOCKS.json
```

---

## 7. Conditional simultaneous-cutoff path

The frozen polynomial norm envelope is

```text
C_GxR/D = O(epsilon Jmax^(13/2))
C_GG/D  = O(epsilon^2 Jmax^13).
```

For

\[
J_{max}\sim\epsilon^{-\alpha},
\]

both vanish for

\[
0<\alpha<2/13.
\]

BCQG v1.1 freezes the explicit interior path

\[
\boxed{\alpha=1/8},
\]

so

\[
\boxed{C_{G\times R}/D=O(\epsilon^{3/16})},
\qquad
\boxed{C_{GG}/D=O(\epsilon^{3/8})}.
\]

This remains conditional on the norm envelope and is not a uniform arbitrary-path theorem.

---

## 8. Remaining channel-resolved finite falsifier

The exact geometry commutator is preregistered as

\[
\boxed{
[G_0,G_1]
=\frac49EE-\frac{64i}{27}(EL+LE)-\frac{1024}{81}LL.
}
\]

with walls

```text
EE : Jmax=5/2
EL : Jmax=9/2
LE : Jmax=9/2
LL : Jmax=13/2.
```

`EE` is complete:

```text
support=514
norm=2.879453814704955.
```

The original monolithic `EL/LE/LL` workers exhausted the six-hour runner wall before writing artifacts. This is a computational timeout, **not a physics FAIL**.

The finite five-point full collector remains an important independent falsifier for:

- unexpectedly large finite Lorentzian coefficients;
- scalar-projection/factor-ordering mistakes;
- full `G x R_op` implementation errors;
- habitat-specific anomalies invisible to the norm-level asymptotic theorem.

Frozen thresholds remain unchanged:

```text
p_cross in [0.75,1.25]
p_GG    in [1.75,2.25]
p_joint in [0.75,1.25]
Delta_joint(1/64)<0.05.
```

---

## 9. IR physical content and predictions

Conditional on first-class continuum HDA and a nondegenerate `D=3` metric sector, the retained DeWitt/Dirac chain gives

\[
\boxed{
\text{one massless spin-2 tensor sector with two TT helicities}
}
\]

and no non-decoupling scalar gravitational mode.

Core dimensionless predictions are collected in `BCQG_CANDIDATE_THEORY_V1_1.md` and include:

- `d_space -> 3`, `z -> 1`, 4D-like history;
- the full-HDA regulator hierarchy above;
- first-order logical Euclidean silence;
- a signed microscopic orientation/chirality sector;
- entangling two-node operator-first route channels;
- finite Lorentzian neighbor/multi-node logical correlations before environment tracing;
- positivity of the route symbol on physical spin sectors.

Absolute force strengths, eV splittings, ranges, meters and Newton normalization are **not** predicted until physical scale setting and matter coupling are derived.

---

## Canonical status statement

> **BCQG Candidate Theory v1.1 is conditionally closed at the signed operator-first asymptotic HDA level on the declared finite-cutoff WKB habitat and explicit `Jmax~epsilon^-1/8` continuum trajectory. It has preregistered physical-sine finite HDA evidence, operator-first route PASSes on genuine spin-changed sectors, upstream-fixed Lorentzian phase/sign/magnitude, an exact nonzero environment-unbiased Lorentzian one-body amplitude, and newly recovered finite multi-node diagonal correlations. The principal remaining work is not to invent another Hamiltonian, but to attack the frozen channel-resolved finite falsifier, off-diagonal environment blocks, independent habitats, a stronger uniform joint limit, and physical Newton/matter scale setting.**
