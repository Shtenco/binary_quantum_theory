# Regulator-safe Peter--Weyl x route-normal local result

Status: **finite local Euclidean coupling PASS with preserved earlier endpoint FAIL; not full two-node/Lorentzian HDA closure.**

## 1. Operator tested

The geometry operator is the genuine-volume, orientation-covariant,
Peter--Weyl-safe Euclidean node Hamiltonian at

$$
J_{\max}=\frac52
$$

acting on the all-$j=1/2$, all-$K=0$ K5 input.  Its one-node action has

$$
\boxed{37\ \text{nonzero spin-network outputs}},
\qquad
\boxed{\|H_0^E\psi_0\|=1.5654096885246453}.
$$

For each reached geometry state $g$ the two-direction densitized flux metric is
reconstructed as

$$
Q_{ab}(g)=\langle g|J_a\cdot J_b|g\rangle,
$$

using local legs `(0,2)`.  On the input state,

$$
\boxed{Q_0=\frac34 I_2}
$$

exactly, while the weighted metric change under $H_0^E$ is

$$
\boxed{1.7403256214647618}.
$$

Thus the route metric is genuinely geometry dependent; the cross commutator is
not artificially switched off.

The local habitat completion is

$$
\boxed{
H_{joint}[N]
=N(v)H_0^E+
\frac12\left\{N,\sqrt{Q_g^{ab}P_aP_b}\right\}.
}
$$

This is a single local normal-deformation operator on geometry x route data,
not a second independent physical Hamiltonian constraint.

## 2. Why a cross anomaly appears

Because $H_0^E$ changes $Q_g$,

$$
[H_0^E,R_M]\ne0.
$$

For

$$
N=N_0+\epsilon n,
\qquad
M=M_0+\epsilon m,
$$

the same-node commutator is

$$
[H_N,H_M]
=[R_N,R_M]
+N_0[H_0^E,R_M]
-M_0[H_0^E,R_N].
$$

The constant-lapse piece of the cross term cancels antisymmetrically.  The
remaining term is therefore a genuine regulator correction rather than a new
zeroth-order constraint.

## 3. Training regulator sequence

The first five points were

| $\epsilon$ | route-only defect | cross / $D$ | joint defect / $D$ |
|---:|---:|---:|---:|
| 1/2 | 2.64329517e-5 | 0.4021401299 | 0.4021401308 |
| 1/4 | 1.32217412e-5 | 0.2011501697 | 0.2011501701 |
| 1/8 | 6.61152930e-6 | 0.1005851054 | 0.1005851056 |
| 1/16 | 3.30584706e-6 | 0.0502938055 | 0.0502938056 |
| 1/32 | 1.65293391e-6 | 0.0251470594 | 0.0251470594 |

The frozen fits are

$$
\boxed{\Delta_\times\sim\epsilon^{0.9998293733}},
$$

$$
\boxed{\Delta_{joint}\sim\epsilon^{0.9998293733}},
$$

$$
\boxed{\Delta_{route}\sim\epsilon^{0.9998293470}}.
$$

### Preserved negative result

The original CI condition required

$$
\Delta_{joint}(1/32)<0.02.
$$

Observed:

$$
\boxed{\Delta_{joint}(1/32)=0.02514705941812194},
$$

so that original endpoint gate is and remains **FAIL**.  It was not erased by
loosening the threshold.

## 4. Blind held-out continuation

Before opening $\epsilon=1/64$, the repository committed
`PETER_WEYL_ROUTE_DRESSED_EPS64_PREREGISTRATION.md` with predictions

$$
\Delta_\times^{pred}=0.012576237890178199,
$$

$$
\Delta_{route}^{pred}=8.266449670538699\times10^{-7},
$$

$$
\Delta_{joint}^{pred}=0.012576237917346172.
$$

The held-out calculation then gave

$$
\boxed{\Delta_\times^{obs}=0.012573549258128154},
$$

$$
\boxed{\Delta_{route}^{obs}=8.264687442454126\times10^{-7}},
$$

$$
\boxed{\Delta_{joint}^{obs}=0.012573549285290355}.
$$

Relative prediction errors are

$$
\boxed{
(2.13787,\ 2.13178,\ 2.13787)\times10^{-4}
}
$$

for `(cross, route, joint)`, i.e. about `0.0214%` each, against a frozen `5%`
acceptance bound.  The held-out joint defect is also below the separately
frozen `0.02` threshold.

Therefore

$$
\boxed{\text{held-out }\epsilon=1/64\text{ continuation: PASS}.}
$$

## 5. What this closes and what it does not

The finite result establishes that the **actual first regulator-safe Euclidean
Peter--Weyl move** can be coupled to a geometry-dependent square-root
route-normal generator without producing a surviving zeroth-order cross
anomaly in this local habitat test.  The observed cross correction is
consistent with

$$
\boxed{\Delta_\times=O(\epsilon)}.
$$

It does **not** establish full HDA closure because:

1. only one node is used, so $[H_0^E,H_1^E]$ is absent;
2. the metric is the diagonal intertwiner expectation $Q_{ab}$, not the full
   operator-valued flux Gram matrix;
3. some reached states have a zero eigenvalue of this 2D metric proxy;
4. the Lorentzian $H_L$ amplitudes are not yet included;
5. the final densitized habitat identity
   $$
   \frac32\{V,-i[H_0,H_1]\}=\hbar(D_{10}-D_{01})
   $$
   has not yet been evaluated for the joint two-node operator.

The next falsifier is therefore the **two-node Euclidean directional habitat
gate**, followed only if viable by the full $H_E+H_L$ amplitude construction.
