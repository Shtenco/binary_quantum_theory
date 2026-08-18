# Exact Peter–Weyl higher-shell Lambda result

Status: **exact finite Peter–Weyl result at the proven second-hit regulator wall; physical TT interpretation still requires recursive spatial/RG and Lorentzian completion**.

This certificate records the completed GitHub Actions calculation produced by `scripts/peter_weyl_higher_shell_lambda_gate.py` for the canonical all-`j=1/2` logical sector.

The calculation uses no external experimental data and no fitted energy denominator.

## 1. Observable

With

\[
H=H_{E,0}+H_{E,1},
\qquad
P H P=0
\]

by the exact doubled-spin parity grading, define

\[
K=P H^2 P
\]

and the denominator-free next-shell observable

\[
\boxed{
\Lambda
=K^{-1/2}\left(PH^4P-K^2\right)K^{-1/2}.
}
\]

Equivalently, for the parity-odd block-Lanczos chain,

\[
B_1^\dagger B_1=K,
\qquad
B_2^\dagger B_2=\Lambda.
\]

The logical space has dimension

\[
\boxed{32}.
\]

The safe second-hit wall is

\[
\boxed{J_{\max}=5/2}.
\]

## 2. Exact CI completion

GitHub Actions run `31852849936` completed the previously heavy column 28 and assembled all 32 exact sparse columns.

Final artifact:

```text
peter-weyl-higher-shell-lambda-repaired
```

The assembled gate reports

```text
passed = true
column_count = 32
first_order_projection_max = 0
second_max_spin = 1.5
Jmax_used = 2.5
```

Thus the computation stays strictly inside the proven second-hit regulator wall.

## 3. K spectrum and conditioning

The first return matrix is full rank:

\[
\boxed{\operatorname{rank}K=32}.
\]

Numerically,

```text
lambda_min(K) = 4.306075987001578
lambda_max(K) = 13.352781352746604
cond(K)       = 3.100916331493829
```

so the normalized higher-shell construction does not rely on a singular or nearly singular first-return matrix.

## 4. Positivity of the genuine next-shell contribution

Define

\[
M=PH^4P-K^2.
\]

The exact finite result is positive:

```text
lambda_min(M) = 47.97777674967158
lambda_max(M) = 186.90234422317016
```

with reconstruction residual

```text
||PH^4P-(K^2+M)|| = 5.685018423077146e-14.
```

Therefore the nontrivial higher-shell signal is not produced by subtractive numerical noise.

## 5. Full Lambda spectrum

The 32 eigenvalues are

```text
10.635759878291307
10.749188473049227
10.948254998563979
11.203697321038089
11.217111924680566
11.238483255052877
11.72412078259753
11.726235435423392
12.27376763547725
12.285943989692049
12.300288543551432
12.553234293953327
12.595993972998919
12.75789204804228
12.761104327215268
12.792753856346671
12.901515192461392
13.130107762511681
13.231645376417646
13.251281669420791
13.311583592563565
13.506971430929555
13.572897188530659
13.674022572076892
13.684221660612984
13.986497971114504
14.075891828438376
14.188812789177696
14.647599045033248
14.751347843002623
14.796025304276027
15.059927665966466
```

Hence

\[
\boxed{\lambda_{\min}(\Lambda)=10.635759878291307},
\]

\[
\boxed{\lambda_{\max}(\Lambda)=15.059927665966466}.
\]

The spectral ratio is

\[
\boxed{
\lambda_{\max}/\lambda_{\min}=1.4159710108447772
}.
\]

The mean eigenvalue is

\[
\boxed{\bar\lambda=12.860443113390883},
\]

with standard deviation

\[
\boxed{\sigma_\lambda=1.2195317610399998}.
\]

Thus

\[
\boxed{\sigma_\lambda/\bar\lambda=0.0948281292}.
\]

The direct Frobenius distance from a scalar identity is

\[
\boxed{
\frac{\|\Lambda-\bar\lambda I\|_F}{\|\Lambda\|_F}
=0.09440461833276048.
}
\]

So the normalized second-shell dynamics is decisively **not** a scalar multiple of the identity.

## 6. Pair trace: orientation survives normalization

After tracing over the three environment logical qubits and rotating to the canonical pair frame, the leading pair couplings are

```text
shape coupling       = -0.3629900150598623
orientation coupling = +0.7912767588958898
Delta                = +1.1542667739557522
```

or

\[
\boxed{
J_{orient}-J_{shape}=1.1542667739557522.
}
\]

The orientation coupling is about

\[
\boxed{2.1798857436}
\]

times the magnitude of the averaged shape coupling.

The largest nonidentity five-logical-qubit Pauli coefficient is

\[
\boxed{c_{IIIYY}=0.7912767588958898},
\]

followed by

```text
IIIXX = +0.37774066046324317
IIIZZ = +0.3482393696564814
IIZII = +0.25325327590795566
ZIIZZ = +0.24058535040395024
```

The Pauli-weight coefficient norms are

```text
weight 0 : 12.860443113390883
weight 1 : 0.4375105330087459
weight 2 : 0.9868534078515151
weight 3 : 0.4592875221813049
weight 4 : 0.33259698809518135
weight 5 : 0.019920255574414788
```

Therefore the first genuine normalized higher-shell observable retains structured one-, two-, three-, four- and five-logical-qubit dynamics rather than reducing to a local scalar return amplitude.

## 7. Block-Lanczos identity

The reconstructed hopping matrices satisfy

```text
||B1^dag B1-K||       = 1.6159818436452347e-13
||B2^dag B2-Lambda||  = 1.6449045564883447e-13
```

and hence support the continued-fraction representation

\[
G_0(z)=
\left[
 zI-B_1^\dagger
 \left(zI-B_2^\dagger G_2(z)B_2\right)^{-1}
 B_1
\right]^{-1},
\]

recursively continued through further shells.

This is the mathematically clean bridge from the finite Peter–Weyl Hamiltonian to a genuine resolvent/propagator construction.

## 8. What the result means physically

What is established:

```text
PH_E P = 0                         exact parity result
K=P H_E^2 P                        positive, full rank
M=P H_E^4 P-K^2                    positive
Lambda                             exact 32x32 non-scalar observable
orientation/shape splitting        survives K normalization
block-Lanczos second hopping       reconstructed exactly
```

What is **not** established yet:

```text
Lambda = physical graviton stiffness          NOT YET
Lambda eigenvalues = particle masses           NO
orientation splitting = Lorentz violation      NOT YET
bare lattice axis = physical preferred frame   NOT YET
```

A direct identification of the Lambda eigenvalues with Standard-Model masses is already structurally disfavoured: its spectral dynamic range is only `1.41597`, far too small to encode the observed charged-lepton hierarchy by a simple linear or square-root map.

## 9. Next unique calculation

The next bridge is now sharply defined:

\[
\boxed{
\Lambda_{local}
\rightarrow
\text{recursive PL/Peter--Weyl blocking}
\rightarrow
K^{TT}_{RG}(\omega,\mathbf k)
\rightarrow
\eta_2^{IR},\zeta_4^{IR}.
}
\]

The existing reduced transfer predicts the bare quartic tensor

\[
\eta_{2,bare}^{iso}=-\frac1{45},
\qquad
\zeta_{4,bare}=-\frac1{12}.
\]

The physical question is whether the exact higher-shell anisotropy flows to

\[
\zeta_4^{IR}=0
\]

or to a nonzero regulator-independent fixed coefficient.

Either outcome is falsifiable once the common microscopic normalization and physical scale are frozen.

## Scientific boundary

This file promotes the higher-shell calculation from a CI artifact to a canonical finite result. It does **not** promote any bare coefficient to a law of nature and does not use external data to choose the result.