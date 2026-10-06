# BQG local information conductance and additive resistance metric

Status: **positive construction for an additive phase-robust metric class + uniqueness no-go.**

This result continues the emergence branch after the pairwise-scalar no-go

$$
I_{ij}\not\mapsto \text{universal distance through one phase-independent }f(I_{ij}).
$$

The new idea is to stop interpreting a long-distance correlation magnitude as a distance. Instead, use **local reduced-state response as an edge conductance**, then construct distance from network composition.

---

## 1. Local physical input

For every nearest-neighbor edge

$$
e=(ij)
$$

let

$$
\rho_e=\rho_{ij}
$$

be the two-node reduced density matrix.

Introduce the relative logical twist generator

$$
\boxed{
K_e=\frac{Z_i-Z_j}{2}.
}
$$

The local quantum Fisher information of the unitary family

$$
\rho_e(\theta)=e^{-i\theta K_e}\rho_e e^{+i\theta K_e}
$$

is

$$
F_Q(\rho_e,K_e)
=2\sum_{a,b}
\frac{(\lambda_a-\lambda_b)^2}{\lambda_a+\lambda_b}
|\langle a|K_e|b\rangle|^2.
$$

Define the **relative-twist quantum-information conductance**

$$
\boxed{
g_e^{\rm QFI}=\frac14F_Q(\rho_e,K_e).
}
$$

The factor $1/4$ is not fitted: it is the standard Bures/Fisher line-element normalization

$$
ds_B^2=\frac14F_Q\,d\theta^2.
$$

Thus $g_e^{\rm QFI}$ is an operational local response coefficient, not a long-distance correlation proxy.

---

## 2. Exact critical reference value

For the thermodynamic critical XX-reduced BQG chain, nearest-neighbor correlators are

$$
C_x(1)=\frac{2}{\pi},
\qquad
C_z(1)=-\frac{4}{\pi^2}.
$$

The corresponding exact relative-twist QFI is

$$
\boxed{
F_{Q,*}=\frac{32}{\pi^2+4}.
}
$$

Therefore

$$
\boxed{
g_*=\frac{8}{\pi^2+4}.}
$$

Numerically

$$
F_{Q,*}\approx2.307203513,
\qquad
g_*\approx0.576800878.
$$

This is an exact analytic local scale of the critical reference state.

---

## 3. Conductance to resistance

Network theory supplies the composition rule.

For a positive local conductance $g_e$, define the edge resistance length

$$
\boxed{
\ell_e=\ell_*\frac{g_*}{g_e}.
}
$$

Here $\ell_*$ is the chosen reference unit and $g_*$ fixes that unit in the critical reference vacuum.

Then define the network metric

$$
\boxed{
d(i,j)=\min_{\gamma:i\to j}\sum_{e\in\gamma}\ell_e.
}
$$

For a chain there is only one simple path, so

$$
\boxed{
d(i,j)=\sum_{e=i}^{j-1}\ell_e.
}
$$

In a homogeneous phase

$$
\ell_e=\ell(m)
$$

and therefore exactly

$$
\boxed{
d_m(i,j)=|i-j|\,\ell(m).
}
$$

This remains additive independently of whether the global two-point mutual information is algebraic or exponential.

That is the key difference from the excluded ansatz

$$
d_{ij}=f(I_{ij}).
$$

---

## 4. Controlled critical-to-gapped gate

The same staggered oriented-volume deformation used previously is retained:

$$
H_m=H_0+m\sum_j(-1)^j Z_j
$$

in the XX frame, equivalently a staggered orientation bias in the original intertwiner frame.

A large-open-chain free-fermion gate computes the bulk nearest-neighbor reduced state and evaluates three local information strengths:

1. mutual information $I_e$;
2. squared Bures correlation distance from $\rho_i\otimes\rho_j$;
3. relative-twist QFI $F_Q(\rho_e,K_e)$.

All remain positive in both critical and gapped phases, and all decrease monotonically as the staggered mass increases in the tested controlled family.

Representative QFI-based normalized resistance lengths are approximately

| $m$ | $F_Q$ | $\ell_Q/\ell_*$ |
|---:|---:|---:|
| 0 | $\approx2.31$ | $\approx1$ |
| 0.2 | $\approx2.097$ | $\approx1.10$ |
| 0.5 | $\approx1.623$ | $\approx1.42$ |
| 1.0 | $\approx0.999$ | $\approx2.31$ |
| 2.0 | $\approx0.421$ | $\approx5.48$ |

Thus the orientation-mass deformation weakens local information conductance and stretches the emergent resistance length rather than changing the composition law.

---

## 5. Positive theorem for the metric class

For any graph with strictly positive local information conductances

$$
g_e>0,
$$

resistance edge lengths

$$
\ell_e\propto g_e^{-1}
$$

and shortest-path composition produce a genuine additive path metric:

$$
\boxed{
d(i,k)\le d(i,j)+d(j,k).
}
$$

On trees the path is unique, hence additivity along geodesics is exact.

For the BQG chain this gives

$$
\boxed{
\text{critical or gapped local state}
\to
\text{local information conductance}
\to
\text{edge resistance}
\to
\text{exact additive distance}.
}
$$

This construction is phase-robust at the level of the **rule**: the same local response functional and the same network composition law apply in both phases.

---

## 6. Why this does not contradict the previous no-go

The previous theorem excluded a global scalar reconstruction

$$
d(i,j)=f(I(i:j))
$$

because long-distance mutual information changes its asymptotic law between critical and gapped phases.

Here we never apply a nonlinear map to long-distance $I(i:j)$.

Instead:

1. infer a **local edge property** from $\rho_{i,i+1}$;
2. assign a local conductance;
3. compose the network locally.

Thus the geometry is generated by local network structure rather than by inverting a long-distance correlation law.

---

## 7. New uniqueness no-go

A second important result appears immediately.

The same local reduced state admits multiple natural monotone correlation/response quantities:

$$
I(\rho_{ij}),
$$

$$
D_B^2(\rho_{ij},\rho_i\otimes\rho_j),
$$

$$
\frac14F_Q(\rho_{ij},K_{ij}).
$$

All are positive local information measures, but they generate different phase-dependent edge scales.

Therefore

$$
\boxed{
\rho_{ij}\ \text{alone does not select a unique spatial metric functional.}
}
$$

Equivalently,

$$
\boxed{
\text{static local state}
\not\Rightarrow
\text{unique metric without an additional operational/dynamical principle}.
}
$$

This is not a failure of the additive construction. It tells us what the next derivation must supply.

---

## 8. Why QFI is currently the preferred candidate

Among the tested local quantities, relative-twist QFI is distinguished because it is not merely a measure of how correlated two nodes are.

It measures how strongly the physical edge state responds to a specified relative relational deformation.

So the preferred chain is now

$$
\boxed{
\rho_{ij}
\to
F_Q(\rho_{ij},K_{ij})
\to
g_{ij}
\to
\ell_{ij}=g_*\ell_*/g_{ij}
\to
\text{shortest-path metric}.
}
$$

But the final step to fundamental BQG is still open: the twist generator $K_{ij}$ and its normalization must be derived from the physical BQG constraint/history dynamics rather than chosen only because it is natural in the reduced XX representation.

---

## 9. Exact scope

### Established in this result

- a local-response conductance can be computed from the full nearest-neighbor reduced state;
- the relative-twist QFI has an exact critical reference value;
- the same QFI rule remains finite and positive in the controlled gapped phase;
- resistance composition gives an exactly additive chain metric in both phases;
- the old global pairwise-scalar no-go is bypassed because geometry is assembled locally;
- static $\rho_{ij}$ alone does not uniquely select the conductance functional.

### Not established

- that QFI conductance is the unique fundamental BQG metric source;
- that $K_{ij}$ is already derived from the full graph-changing BQG constraint;
- that the resulting metric gives $d_s=3$;
- that Lorentzian causal structure follows;
- that the reference length $\ell_*$ is already derived from first principles.

---

## 10. Next exact gate

The next calculation should no longer search for another scalar correlation function.

It should test whether the QFI-weighted graph Laplacian

$$
\boxed{
(L_g)_{ij}
=\delta_{ij}\sum_k g_{ik}-g_{ij}
}
$$

produces a consistent diffusion geometry and spectral dimension.

For the 1D chain it must reproduce

$$
d_s=1
$$

as a calibration.

Then the same local QFI rule should be applied, without retuning, to nontrivial connectivities: ring, square lattice, branching graph and eventually dynamical BQG gluing graphs.

This is the next nontrivial test because the graph Laplacian simultaneously probes local metric weights, diffusion, topology and dimension.
