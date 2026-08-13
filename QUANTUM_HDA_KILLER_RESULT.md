# Off-shell quantum HDA killer: factorized-Hamiltonian no-go

## Target fixed independently

The desired canonical continuum relation is not chosen after looking at the
Hamiltonian commutator. Its RHS has already been built independently:

$$
\omega=N\,dM-M\,dN,
$$

$$
\beta=\sharp_{E,q}\omega,
$$

$$
\boxed{
D_{\rm path}[\beta].
}
$$

The preferred finite target is the densitized, inverse-volume-free form

$$
\boxed{
\frac32\{V,-i[H[N],H[M]]\}
\longrightarrow
\hbar D_{\rm path}[\sharp_{E,q}(N\,dM-M\,dN)].
}
$$

## Exact structural no-go for the current Hamiltonian domain

The current regulator-safe Peter--Weyl Hamiltonian acts on geometry/spin data,
while the nontrivial diffeomorphism representation lives on a separate refined
path/rerouting register. If the operator still factorises as

$$
H[N]=H_{\rm geom}[N]\otimes I_{\rm path},
$$

then identically

$$
[H[N],H[M]]
=
[H_{\rm geom}[N],H_{\rm geom}[M]]\otimes I_{\rm path}.
$$

Its path-derivative/traceless component is therefore exactly zero.

For generic nonconstant lapses, however,

$$
\beta=\sharp(NdM-MdN)\ne0
$$

and the already verified path representation gives

$$
D_{\rm path}[\beta]\ne0.
$$

`bcqg_quantum_hda_killer.py` supplies an explicit smooth finite witness. After
normalising by the nonzero RHS norm, the factorised path-channel residual is

$$
\boxed{\Delta_{\rm factor}=1}.
$$

This is independent of $J_{\max}$. Therefore increasing the Peter--Weyl cutoff,
adding more spin-network states, or changing numerical precision cannot repair
the off-shell HDA while $H$ remains proportional to the identity on path space.

## What already passes

The same killer script executes the independent prerequisites:

1. exact dual-$K_5$ lapse cochain
   $$\omega_{vw}=N_vM_w-N_wM_v;$$
2. generic flux/Hodge `sharp` reconstruction;
3. gauge-covariant elementary path rerouting;
4. two-transverse vector-field path Lie algebra with approximately $O(a^2)$
   defect;
5. classical real-Ashtekar--Barbero $\beta$ cancellation;
6. conservative Peter--Weyl hit-wall enumeration for the full Lorentzian HH
   support.

Thus the missing object is no longer ambiguous.

## Single required architecture change

The Hamiltonian itself must become

$$
\boxed{H_{\rm geom+route}[N]}
$$

and each local move must include a **gauge-covariant controlled rerouting** on
the same cylindrical/path domain used by $D_{\rm path}$.

It must preserve, without refitting:

- exact endpoint SU(2) covariance;
- the fixed Lorentzian coefficient $(1+\beta^2)$;
- the Peter--Weyl regulator-safe hit bound;
- nonconstant lapse dependence;
- the independently frozen `sharp` and $D_{\rm path}$ definitions.

Only after this coupling exists is the expensive HH amplitude calculation
scientifically meaningful.

## Status

The result is a **successful falsifier**, not a positive HDA closure:

$$
\boxed{
H_{\rm geom}\otimes I_{\rm path}
\quad\text{is ruled out for nontrivial off-shell HDA.}
}
$$

The full route-coupled Lorentzian quantum HDA remains OPEN.
