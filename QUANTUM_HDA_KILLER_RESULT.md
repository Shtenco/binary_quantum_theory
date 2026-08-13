# Off-shell quantum HDA killer and route-normal completion

## Target fixed independently

The desired relation is not chosen after inspecting the Hamiltonian commutator:

$$
\omega=N\,dM-M\,dN,
\qquad
\beta=\sharp_{E,q}\omega,
$$

$$
\boxed{D_{\rm path}[\beta].}
$$

The preferred finite target is

$$
\boxed{
\frac32\{V,-i[H[N],H[M]]\}
\longrightarrow
\hbar D_{\rm path}[\sharp_{E,q}(N\,dM-M\,dN)].
}
$$

## Exact no-go for the old tensor factorisation

If

$$
H[N]=H_{\rm geom}[N]\otimes I_{\rm path},
$$

then

$$
[H[N],H[M]]=[H_{\rm geom}[N],H_{\rm geom}[M]]\otimes I_{\rm path}.
$$

Its path-derivative component is identically zero, while for generic
nonconstant lapses

$$
D_{\rm path}[\sharp(NdM-MdN)]\ne0.
$$

`bcqg_quantum_hda_killer.py` contains an explicit finite witness with normalized
path-channel residual

$$
\boxed{\Delta_{\rm factor}=1}.
$$

Therefore no increase of $J_{\max}$ can fix the off-shell HDA while the
Hamiltonian is proportional to $I_{\rm path}$.

## Constructive route-normal operator

The no-go also identifies the minimal missing structure. On the refined path
sheet define

$$
\Omega_q=\sqrt{-\Delta_{{\rm path},q}}
$$

and

$$
\boxed{
H_{\rm path}[N]=\frac12\{N,\Omega_q\}.
}
$$

Its principal symbol is

$$
h_N(x,p)=N(x)|p|_q,
\qquad
|p|_q=\sqrt{q^{ab}p_ap_b}.
$$

Using standard symbol calculus,

$$
\{h_N,h_M\}
=
q^{ab}(M\partial_bN-N\partial_bM)p_a,
$$

up to the single global orientation convention for the vector constraint. The
terms involving derivatives of the metric cancel pairwise. Thus the HDA metric
structure function is generated **without fitting its magnitude**.

The executable `scripts/path_normal_hda_gate.py` checks the finite spectral
quantum commutator on WKB route states. For carrier modes

$$
k=2,3,4,6,8,12,16,24
$$

the defect falls approximately as

$$
\boxed{\Delta_{\rm HDA}^{path}\sim k^{-2.14}},
$$

and reaches a few parts in $10^{-6}$ at the largest preregistered carrier.

This closes the **route-sector normal-deformation representation at principal
symbol / semiclassical level**.

## What already passes together

The killer now executes:

1. exact dual-$K_5$ lapse cochain;
2. generic flux/Hodge `sharp` reconstruction;
3. gauge-covariant elementary rerouting;
4. two-transverse vector-field path Lie algebra;
5. square-root route-normal HDA gate;
6. classical real-Ashtekar--Barbero $\beta$ cancellation;
7. conservative Peter--Weyl Lorentzian hit-wall enumeration.

## Single remaining operator task

The geometry and route sectors must now be coupled in the **same** Hamiltonian:

$$
\boxed{H_{\rm geom+route}[N].}
$$

It must preserve without refitting:

- endpoint SU(2) covariance;
- the fixed Lorentzian coefficient $(1+\beta^2)$;
- the Peter--Weyl safe cutoff;
- the frozen `sharp` map;
- the square-root route-normal principal symbol;
- nonconstant off-shell lapse dependence.

Then, and only then, the expensive joint HH calculation is meaningful.

## Status

Two statements are now cleanly separated:

$$
\boxed{H_{\rm geom}\otimes I_{\rm path}\ \text{is exactly ruled out}.}
$$

$$
\boxed{H_{\rm path}[N]=\tfrac12\{N,\sqrt{-\Delta_{path,q}}\}\ \text{has the correct HDA principal symbol}.}
$$

The **full route-coupled Peter--Weyl Lorentzian quantum HDA** remains OPEN.
