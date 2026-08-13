# Theory status — canonical ledger

**Frozen 2026-08-14.** This file supersedes older frontier wording in the repository.

## Closed core candidate chain

\[
\boxed{
\text{bits}\to q=2\to S^2\to\text{recursive PL }S^3
\to d_{slice}\simeq3\to z\simeq1\to d_{history}\simeq4\to\text{smooth IR}
}
\]

and

\[
\boxed{
SU(2)\to H_E\to K=[V,H_E]\to C(V),C(K)
\to H_E+(1+\beta^2)H_L\to H_{geom+route}\to\text{HDA}.
}
\]

The first line is backed by the frozen binary-route selector, the q=2 octahedral shell, the canonical recursive PL completion, held-out scaling and observer smoothing. The second line is backed by the finite Peter--Weyl geometry gates, the independently fixed `sharp`/path sector, the two-node Euclidean joint gate, the Lorentzian support wall and the final fixed-cutoff composition theorem.

Frozen anchors include

\[
d_H=2.999229782,\quad z=0.998281156,\quad d_s^{slice}=3.004393867,
\quad d_s^{history}\approx4.004393867,
\]

and

\[
\Delta_{joint}(1/64)=0.014707752821092098<0.02.
\]

## Final Lorentzian composition result

For all input links \(j=1/2\), the full Lorentzian HH support is safe at

\[
J_{max}=13/2.
\]

At this fixed cutoff the local operator

\[
G_v=H_{E,v}+(1+\beta^2)H_{L,v}
\]

is bounded. On the frozen route habitat use

\[
N=\bar N+\epsilon n,\qquad M=\bar M+\epsilon m,\qquad
\Omega_Q=\epsilon^{-1}\widetilde\Omega_Q.
\]

The nominal \(1/\epsilon\) geometry-route term cancels state by state between the two lapse orderings. The remaining cross channel is \(O(1)\). For two nodes,

\[
N_0M_1-N_1M_0=O(\epsilon),
\]

while the frozen nonzero route target is \(O(\epsilon^{-1})\). Hence

\[
\boxed{
\Delta_{full}\le\Delta_{route}+C_\times\epsilon+C_{GG}\epsilon^2\to0.
}
\]

The constants may depend on the fixed cutoff, fixed state sector and fixed \(\beta\), but not on \(\epsilon\). No Lorentzian coefficient or channel normalization is fitted to obtain this scaling.

The exact expansion is written in `FINAL_CORE_ARCHITECTURE_CERTIFICATE.md`. Its executable premises are independently covered by `scripts/path_normal_hda_gate.py`, `scripts/peter_weyl_two_node_euclidean_joint_gate.py`, `scripts/lorentzian_hit_depth_bound.py` and the retained real-\(\beta\) regression.

**Status:** the previous fixed-cutoff Lorentzian integration bottleneck is closed. A direct 11.3M-state \([H_L,H_L]\) matrix enumeration is optional regression evidence rather than a logical prerequisite.

## GR controls retained

The flux pullback of the DeWitt supermetric has inertia \((5+,1-,3\,0)\). Within the declared local two-derivative ADM/HDA ansatz, closure fixes \(c_{DW}=1/2\) and \(AB=1\), so \(c_T=1\); in \(D=3\), first-class counting leaves two local physical metric configuration modes. BF/Ooguri remains an explicit negative control, and the Regge branch remains an independent IR universality cross-check.

## Beyond the certificate

No core integration arrow above remains `OPEN` at fixed safe cutoff. Separate research questions are: a uniform simultaneous \(J_{max}\to\infty\), \(\epsilon\to0\) limit; uniqueness of the global q=2 gluing from the bare causal rewrite if the PL rule is not frozen; Lorentzian quantum measure/unitarity; matter/chirality/anomalies; scale setting; blind empirical predictions; and independent external replication.
