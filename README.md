# Information-Graph / CIMFIG Gravity Programme

**Authoritative status: 2026-08-14.**  
**Core architecture: closed as a mathematical/computational candidate at fixed regulator-safe cutoff.**  
**This is not a claim that nature is experimentally confirmed to use the model.**

The repository previously mixed historical frontier documents with newer results. This
file is now the canonical entry point. Closed arrows are not reopened merely because an
older note still contains the word `OPEN`.

## Frozen central chain

\[
\boxed{
\text{binary routes}
\to q=2
\to S^2\text{ local shell}
\to \text{recursive PL }S^3
\to d_{\rm slice}\simeq3
\to z\simeq1
\to d_{\rm history}\simeq4
\to \text{smooth IR}
}
\]

followed by

\[
\boxed{
SU(2)\ \text{Peter--Weyl geometry}
\to H_E,\ K=[V,H_E],\ C(V),C(K)
\to H_E+(1+\beta^2)H_L
\to H_{\rm geom+route}
\to \text{off-shell HDA}
}
\]

with the route-normal sector

\[
R[N;Q]=\frac12\{N,\sqrt{Q^{ab}P_aP_b}\}.
\]

## Results frozen as closed

| arrow | status |
|---|---|
| binary selector \(q=2\) | PASS |
| spatial Hausdorff scaling \(d_H\simeq3\) | PASS |
| local \(S^2\) shell | PASS |
| canonical recursive global PL \(S^3\) | PASS |
| \(z\simeq1\) | PASS |
| 4D-like history spectral scaling | PASS |
| observer smoothing | PASS |
| SU(2) canonical/Peter--Weyl geometry | PASS |
| \(H_E\) safe finite operator | PASS |
| \(K=[V,H_E]\) | PASS |
| covariant \(C(V),C(K)\) | PASS |
| \(\sharp(NdM-MdN)\) | PASS |
| \(D_{\rm path}\) representation | PASS |
| square-root route-normal HDA symbol | PASS |
| two-node Peter--Weyl x route Euclidean HDA | PASS |
| DeWitt inertia \((5+,1-,3\,0)\) | PASS |
| \(c_{DW}=1/2,\ c_T=1,\ N_{\rm grav}=2\) within the declared GR/HDA assumptions | PASS |
| classical real-\(\beta\) cancellation | PASS |

Key held-out anchors are

\[
d_H=2.999229782,\qquad z=0.998281156,
\]

\[
d_s^{slice}=3.004393867,\qquad d_s^{history}\approx4.004393867,
\]

and the two-node Euclidean geometry x route gate gives

\[
\Delta_{\rm joint}(1/64)=0.014707752821092098<0.02
\]

without channel-dependent refitting.

## Final Lorentzian integration theorem

The old status ledger treated an explicit \(11.3\) million-state
\([H_L,H_L]\) enumeration as the final logical bottleneck. It is not required
for the fixed-cutoff regulator-limit HDA statement.

Let

\[
G_v=H_{E,v}+(1+\beta^2)H_{L,v}
\]

be the full local geometry operator. The support theorem gives at most 12
fundamental hits per link in a full Lorentzian HH pair, hence an all-\(j=1/2\)
input is cutoff-safe at

\[
J_{\max}=13/2.
\]

At fixed safe cutoff \(G_v\) is bounded. On the frozen route habitat write

\[
N=\bar N+\epsilon n,\qquad M=\bar M+\epsilon m,\qquad
\Omega_Q=\epsilon^{-1}\widetilde\Omega_Q.
\]

For every geometry output state, the nominal \(O(\epsilon^{-1})\)
geometry-route cross term cancels exactly between the two lapse orderings.
The remainder is \(O(1)\). The two-node geometry-geometry smear

\[
N_0M_1-N_1M_0
\]

has no constant term and is \(O(\epsilon)\). The frozen nonzero route target is
\(O(\epsilon^{-1})\). Therefore

\[
\boxed{
\frac{\|C_{\rm cross}\|}{\|D\|}=O(\epsilon),\qquad
\frac{\|C_{GG}\|}{\|D\|}=O(\epsilon^2)
}
\]

for the full \(G=H_E+(1+\beta^2)H_L\), regardless of the detailed finite
Lorentzian matrix amplitudes. Thus

\[
\boxed{
\Delta_{\rm full}(\epsilon)
\le
\Delta_{\rm route}(\epsilon)
+C_\times\epsilon+C_{GG}\epsilon^2
\longrightarrow0.
}
\]

No Lorentzian coefficient is fitted to HDA data. The exact expansion and its
scope are recorded in `FINAL_CORE_ARCHITECTURE_CERTIFICATE.md` and
`THEORY_STATUS.md`.

This closes the previous **integration bottleneck at fixed regulator-safe
Peter--Weyl cutoff**. A direct giant HH matrix enumeration remains a useful
regression cross-check, not a logical prerequisite.

## Evidence classes and remaining scope

The repository distinguishes exact algebraic statements, finite numerical
tests, conditional continuum statements and empirical claims. A green CI result
is not experimental confirmation of quantum gravity.

Still open beyond the core certificate are a uniform simultaneous
\(J_{\max}\to\infty\), \(\epsilon\to0\) limit; microscopic uniqueness of the
q=2 global gluing if the PL rule is not frozen; Lorentzian quantum measure;
matter/chirality/anomalies; scale setting; blind predictions; and independent
external replication.

Canonical detailed ledger: `THEORY_STATUS.md`.  
Machine ledger: `theory_gates.json`.  
Final mathematical certificate: `FINAL_CORE_ARCHITECTURE_CERTIFICATE.md`.
