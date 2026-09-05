# BQG spectral-history graph: exact finite cyclic closure of the physical master history

Status: **spectral-history closure theorem and fail-closed production architecture added; full physical BQG history is not yet emitted because the production Lorentzian/HDA packet remains open.**

## 1. Purpose

The useful mathematical part of spectral-graph models is the operator/spectral machinery itself:

- positive self-adjoint graph/master operators;
- spectral measures;
- heat kernels;
- zeta functions and return probabilities;
- Krylov/Lanczos compression;
- reconstruction of matrix functions from a cyclic spectral measure.

BQG does **not** import a guessed Watts--Strogatz graph, a chosen node count `N`, a prescribed degree `K`, a nonlocal-link probability `p`, fitted interaction-channel weights, or an identification of a master-constraint eigenvalue with a particle mass.

Instead, the spectral graph is **derived from the already-defined BQG master constraint**.

The production chain is

```text
actual BQG constraint family
        -> M_BQG >= 0
        -> declared boundary/source seed V
        -> block Krylov cyclic subspace K(M_BQG,V)
        -> block-Jacobi / spectral quotient J_V
        -> matrix-valued spectral measure dSigma_V(lambda)
        -> V^dag f(M_BQG) V
        -> zero spectral weight / physical projector
        -> existing O_rel -> Z_BQG -> W_BQG -> Gamma_BQG
```

No dark-matter, dark-energy, mass, coupling, or cosmological datum enters this construction.

---

## 2. Finite cyclic spectral-closure theorem

Let `M=M^dag >= 0` be a finite regulated master constraint and let the seed block `V` have orthonormal columns.

Define the cyclic block-Krylov space

\[
\mathcal K_r(M,V)=\operatorname{span}\{V,MV,M^2V,\ldots,M^rV\}.
\]

Apply rank-revealing block Lanczos/Gram--Schmidt, obtaining orthonormal blocks `Q_n`.  In a non-deflated presentation the recurrence is

\[
M Q_n = Q_{n-1}B_n^\dagger+Q_nA_n+Q_{n+1}B_{n+1},
\]

with `A_n=A_n^dag` and the off-diagonal blocks `B_n` determined by the residual factorization.

The finite block-Jacobi matrix

\[
J_r=Q^\dagger M Q,
\qquad Q=(Q_0,\ldots,Q_r),
\]

is the **BQG spectral-history graph** on this seed.  Its block vertices are Krylov layers, its diagonal block weights are `A_n`, and its adjacent block-edge weights are `B_n`.

If the next residual vanishes,

\[
\boxed{B_{r+1}=0,}
\]

then `K_r` is invariant under `M`.  Consequently for every bounded Borel function `f` on the finite spectrum,

\[
\boxed{
V^\dagger f(M)V
=E_0^\dagger f(J_r)E_0,
}
\]

where `E_0` embeds the seed into the first Lanczos block.

Therefore the finite regulated boundary history closes **exactly**:

\[
\boxed{
H_V(\sigma)
=V^\dagger e^{-\sigma M}V
=E_0^\dagger e^{-\sigma J_r}E_0,
}
\]

and the zero-projector overlap is

\[
\boxed{
G_{V,0}
=V^\dagger\mathbf 1_{\{0\}}(M)V
=E_0^\dagger\mathbf 1_{\{0\}}(J_r)E_0
=\lim_{\sigma\to\infty}H_V(\sigma).
}
\]

Here `sigma` is the master heat/projector-flow parameter.  It is **not** relational proper time and is **not** the physical frequency `omega`.

---

## 3. Matrix-valued spectral measure

Let

\[
J_r u_a=\lambda_a u_a.
\]

Define the positive matrix weights

\[
W_a=E_0^\dagger u_a u_a^\dagger E_0.
\]

Then the seed spectral measure is

\[
\boxed{
d\Sigma_V(\lambda)
=\sum_a W_a\,\delta(\lambda-\lambda_a)d\lambda,
}
\]

and

\[
V^\dagger f(M)V
=\int f(\lambda)d\Sigma_V(\lambda).
\]

In particular,

\[
\mu_n=V^\dagger M^nV
=\int \lambda^n d\Sigma_V(\lambda).
\]

Thus the already-measured BQG master moments are not a separate construction: they are moments of the same spectral graph that eventually yields the projector.

---

## 4. Moment/Hankel construction

A useful independent construction of the same finite cyclic quotient starts from certified moments.

For depth `r`, form the block Hankel matrices

\[
\mathcal H_r=[\mu_{i+j}]_{i,j=0}^{r},
\qquad
\mathcal H_r^{(1)}=[\mu_{i+j+1}]_{i,j=0}^{r}.
\]

The first matrix is the Gram matrix of the raw block Krylov family

\[
(V,MV,\ldots,M^rV).
\]

Whitening the numerical support of `H_r` and projecting `H_r^(1)` produces a finite Hermitian quotient operator `T_r`.  Its matrix-valued Gauss spectral measure reproduces the supplied Krylov moments.

A particularly useful exact finite closure certificate is rank stabilization:

\[
\boxed{
\operatorname{rank}\mathcal H_{r+1}
=\operatorname{rank}\mathcal H_r.
}
\]

With a certified numerical error bound, this means `M^(r+1)V` introduces no new cyclic direction, hence the Krylov space is invariant.  In production BQG, numerical rank stabilization is accepted only when an upstream error certificate is supplied; a visually small singular value is not enough.

The preferred production certificate remains the direct block-Lanczos residual norm because it measures termination without reconstructing high powers.

---

## 5. Current Euclidean history frontier

For the orthonormal 32-state q=2 boundary seed `V0`, the Euclidean normal master already has

\[
\mu_0=I_{32},
\qquad
\mu_1=V_0^\dagger M_EV_0=M_{EE}.
\]

The current history-targeted producer computes

\[
Y=M_EV_0=\sum_v H_v^E H_v^E V_0
\]

in the frozen Hermitian Euclidean convention, after which

\[
\mu_2=Y^\dagger Y.
\]

The first genuine master-Krylov residual Gram is therefore

\[
\boxed{
R_1
=\mu_2-\mu_1^\dagger\mu_1
=Y^\dagger(I-V_0V_0^\dagger)Y
\succeq0.
}
\]

If `R1=0` within a certified error bound, the Euclidean boundary cyclic space closes at depth zero and

\[
V_0^\dagger e^{-\sigma M_E}V_0=e^{-\sigma\mu_1}
\]

becomes an exact statement **for that finite Euclidean regulated sector**.

If `R1` has positive rank, factor it to form the next normalized block `Q1`, evaluate one further master action, obtain `A1` and the next residual `B2`, and continue.  No dense ambient Peter--Weyl matrix is required.

---

## 6. Source-complete spectral graph

Closing only

\[
V_0^\dagger P_0V_0
\]

is not sufficient to claim a physical two-point kernel or `Gamma^(2)`.

For a declared source family `O_A`, the spectral seed must contain every state required by the desired source derivative.  For a quadratic source claim a safe finite seed is generated from

\[
\boxed{
\mathcal V_{\Gamma^{(2)}}
=\operatorname{span}\{V_0,\ O_AV_0,\ O_AO_BV_0\}_{A,B\in\mathcal S},
}
\]

with the exact relational/time-ordered convention used by the existing source machinery.

A block spectral graph built from this source-enriched seed simultaneously supplies all projector matrix elements needed by the zero-source amplitude, one-source derivative and quadratic connected Hessian on the declared source packet.

For the full generating functional to all orders one would need the corresponding full source-generated cyclic algebra.  BQG does **not** need that stronger object before computing the finite scalar/TT quadratic kernels already targeted by the physicalization programme.

---

## 7. Spectral diagnostics imported without phenomenological fitting

Once the graph is derived, rather than guessed, several diagnostics are legitimate.

### Seed return probability

\[
P_V(\sigma)
=\frac1{d_V}\operatorname{Tr}
\left(V^\dagger e^{-\sigma M}V\right).
\]

### Constraint spectral dimension

\[
\boxed{
d_{s,M}^{(V)}(\sigma)
=-2\frac{d\ln P_V}{d\ln\sigma}
=2\sigma\,
\frac{\sum_a\lambda_a e^{-\sigma\lambda_a}\operatorname{tr}W_a}
{\sum_a e^{-\sigma\lambda_a}\operatorname{tr}W_a}.
}
\]

This is a **master/constraint spectral-flow diagnostic**.  It is not automatically the dimension of physical spacetime.  Any identification with a continuum spacetime spectral dimension requires an independent refinement/geometry theorem.

### Seed-weighted zeta function

On the positive spectral support,

\[
\boxed{
\zeta_V(s)
=\sum_{\lambda_a>0}
\operatorname{tr}(W_a)\lambda_a^{-s}.
}
\]

This can diagnose refinement stability and scaling.  It is not used to manufacture particle masses or fundamental constants.

---

## 8. What is explicitly rejected

The following moves are forbidden in the BQG spectral-history pipeline:

```text
choose N,K,p,xi to obtain desired physics;
fit graph-channel weights to observed forces;
select a spectral resonance because it matches a known particle mass;
identify sqrt(master eigenvalue) with particle mass;
interpret master heat sigma as physical time;
interpret a master resolvent parameter z as physical omega;
tune beta/lambda to create a zero mode or a dark sector;
add Krylov depth until a desired near-zero happens without a predeclared convergence test.
```

The positive eigenvalues of `M_BQG` measure violation of the declared constraints at the finite regulator.  Physical particle poles, masses and propagation laws may only be read later from the source-dressed physical effective kernel `Gamma_BQG^(2)(omega,k)`.

---

## 9. Fail-closed physical emission rule

The spectral graph may emit a **physical** BQG history/projector only if all of the following hold on the same declared production packet:

1. the seed cyclic history has a certified finite termination or controlled convergent limit;
2. the master domain is complete for the declared regulated problem;
3. the master constraint family is production-certified;
4. the quantum HDA target is certified on the same habitat, or explicit independent `D_target` columns are included in the master;
5. the seed is complete for the correlator/source claim being emitted.

Otherwise the graph is retained as a spectral diagnostic and `physical_projector_emitted=false`.

---

## 10. Status

The spectral-history **mathematical architecture is now closed** at finite regulator:

\[
\boxed{
M_{BQG}\to\mathcal K(M,V)\to J_V\to d\Sigma_V
\to V^\dagger e^{-\sigma M}V
\to V^\dagger P_0V.
}
\]

The current actual Euclidean BQG computation has reached `mu0`, `mu1` and the direct `mu2` producer.  Full physical BQG history remains open only because the production Lorentzian master data and quantum `HH <-> D_target` habitat certificate have not yet been completed on the same physical domain.

That distinction is deliberate: **the route to close history no longer requires a new physical hypothesis; it requires completion of the already-defined microscopic constraint packets and spectral termination/refinement tests.**
