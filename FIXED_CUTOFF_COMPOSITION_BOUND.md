# Fixed-cutoff composition bound

Status: **proved inside the explicitly stated fixed-cutoff finite-dimensional assumptions; not full quantum HDA closure**.

This note records a composition estimate for the declared geometry-plus-route habitat. It is deliberately not called a final certificate: the result does not prove graph-changing, multi-node, regulator-independent quantum general relativity.

## 1. Fixed assumptions

At the all-`j=1/2` input, the finite Lorentzian support analysis supplies a regulator-safe Peter-Weyl cutoff. For fixed finite cutoff and fixed finite real `beta`, define

$$
G_v=H_{E,v}+(1+\beta^2)H_{L,v}.
$$

On the frozen habitat family

$$
N=\bar N+\epsilon n,
\qquad
M=\bar M+\epsilon m,
\qquad
\Omega_Q=\epsilon^{-1}\widetilde\Omega_Q,
$$

with route operator

$$
R_Q[A]=\frac12\{A,\Omega_Q\}.
$$

For a geometry transition `Q_0 -> Q_g`, write

$$
\Delta\widetilde\Omega
=\widetilde\Omega_{Q_0}-\widetilde\Omega_{Q_g},
$$

and collect the finite lapse-dependent pieces into `Delta S_n` and `Delta S_m`.

Then

$$
\Delta R_M
=\frac{\bar M}{\epsilon}\Delta\widetilde\Omega+\Delta S_m,
\qquad
\Delta R_N
=\frac{\bar N}{\epsilon}\Delta\widetilde\Omega+\Delta S_n.
$$

## 2. Cross-term cancellation

At a node `v`, with

$$
N_v=\bar N+\epsilon n_v,
\qquad
M_v=\bar M+\epsilon m_v,
$$

the cross combination expands as

$$
\begin{aligned}
N_v\Delta R_M-M_v\Delta R_N
={}&\bar M n_v\Delta\widetilde\Omega
-\bar N m_v\Delta\widetilde\Omega\\
&+\bar N\Delta S_m-\bar M\Delta S_n\\
&+\epsilon(n_v\Delta S_m-m_v\Delta S_n).
\end{aligned}
$$

The apparent `1/epsilon` term cancels state by state. This cancellation is algebraic and does not require fitting a Lorentzian coefficient.

For two nodes,

$$
\begin{aligned}
N_0M_1-N_1M_0
={}&\epsilon\left[
\bar N(m_1-m_0)+\bar M(n_0-n_1)
\right]\\
&+\epsilon^2(n_0m_1-n_1m_0),
\end{aligned}
$$

so the pure-geometry coefficient has no zeroth-order term.

## 3. Relative scaling on the frozen WKB carrier

On the declared nonzero WKB carrier, physical route derivatives scale as

$$
\|D_{path}[\sharp(NdM-MdN)]\|=O(\epsilon^{-1}).
$$

Therefore, under the fixed-cutoff assumptions,

$$
\boxed{
\frac{\|C_{cross}\|}{\|D\|}=O(\epsilon),
\qquad
\frac{\|C_{GG}\|}{\|D\|}=O(\epsilon^2)
}
$$

and the composed defect obeys

$$
\boxed{
\Delta_{full}
\le
\Delta_{route}
+C_{cross}\epsilon+C_{GG}\epsilon^2.
}
$$

If the route defect tends to zero on the same frozen family, the additional fixed-cutoff cross and pure-geometry contributions are asymptotically suppressed in this composition estimate.

## 4. Evidence used

The bound composes previously retained finite results:

- `scripts/path_normal_hda_gate.py` and `QUANTUM_HDA_KILLER_RESULT.md` for the route-normal principal-symbol target;
- `scripts/peter_weyl_two_node_euclidean_joint_gate.py` and `PETER_WEYL_TWO_NODE_EUCLIDEAN_RESULT.md` for the observed two-node Euclidean scaling hierarchy;
- `scripts/lorentzian_hit_depth_bound.py` for the finite support/cutoff wall;
- `LORENTZIAN_BETA_CANCELLATION.md` for the fixed real-`beta` coefficient control.

## 5. Exact claim boundary

This result does **not** establish any of the following:

```text
full graph-changing multi-node off-shell quantum HDA closure
uniform Jmax -> infinity and epsilon -> 0 control
a regulator-independent physical Hilbert space
derivation of the geometric sector from the microscopic binary dynamics
experimental confirmation
```

Those items remain separate open gates in `theory_gates.json` and `THEORY_STATUS.md`.

The correct status is therefore:

$$
\boxed{
\text{fixed-cutoff composition bound: retained}
\quad\neq\quad
\text{full quantum-GR closure}.
}
$$
