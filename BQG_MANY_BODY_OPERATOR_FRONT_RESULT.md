# BQG many-body operator front and exact gapped velocity

Status:
- **PROVED**: graph-local nested-commutator support theorem.
- **PROVED**: first nonzero endpoint \(Z\)-commutator order equals graph distance on the positive-coupling XX chain/tree path sector.
- **PROVED**: exact ballistic maximum group velocity of the homogeneous staggered-volume reduced model.
- **OPEN**: identification of this reduced propagation front with the full continuum Lorentz cone of physical BQG.

## 1. General graph-local many-body support theorem

Let

\[
H=\sum_X h_X
\]

be a finite-range many-body Hamiltonian on a graph \(G\), with every interaction term \(h_X\) supported either on one vertex or on one graph edge.

For a local operator \(O_i\) initially supported at vertex \(i\),

\[
O_i(t)=e^{iHt}O_i e^{-iHt}
=
\sum_{n=0}^{\infty}
\frac{(it)^n}{n!}\operatorname{ad}_H^n(O_i).
\]

Each commutator with a vertex term leaves support unchanged. Each commutator with an edge term can enlarge support by at most one graph step.

Therefore

\[
\boxed{
\operatorname{supp}\operatorname{ad}_H^n(O_i)
\subseteq
B_n(i),
}
\]

where \(B_n(i)\) is the radius-\(n\) graph ball.

Hence for a local probe \(O_j\),

\[
\boxed{
[\operatorname{ad}_H^n(O_i),O_j]=0
\qquad
n<d_G(i,j).
}
\]

Equivalently,

\[
\boxed{
[O_i(t),O_j]
=
O(t^{d_G(i,j)}).
}
\]

This is exact and model-independent inside the class of graph-local interactions.

It proves a strict algebraic locality hierarchy: information cannot appear at graph distance \(d\) before nested-commutator order \(d\).

---

## 2. Equality on the QFI-weighted XX path sector

Consider

\[
H_{\rm XX}
=
\sum_{\langle ab\rangle}
\frac{J_{ab}}{2}
(X_aX_b+Y_aY_b)
+
\sum_a h_a Z_a,
\qquad J_{ab}>0.
\]

For vertices \(i,j\) connected by a unique shortest path of length

\[
d=d_G(i,j),
\]

choose endpoint probes \(Z_i,Z_j\).

The general theorem gives zero for every order below \(d\).

At order \(d\), the ordered sequence of edge commutators along the unique shortest path generates a nonzero Pauli string spanning that path. Its coefficient is proportional to

\[
\prod_{e\in\gamma_{ij}}J_e,
\]

which is nonzero because every \(J_e>0\).

Diagonal \(h_aZ_a\) terms cannot reduce the required number of edge crossings.

Therefore

\[
\boxed{
\min\left\{
n:
[\operatorname{ad}_H^n(Z_i),Z_j]\neq0
\right\}
=
d_G(i,j)
}
\]

for this path/tree sector.

Thus the many-body operator algebra reproduces the same graph distance previously obtained from the one-particle propagator.

---

## 3. Homogeneous critical reduced chain

For the reduced BQG XX chain the Jordan-Wigner single-particle dispersion is

\[
\varepsilon(k)=-3\cos k.
\]

Hence

\[
v(k)=\left|\frac{d\varepsilon}{dk}\right|=3|\sin k|,
\]

so

\[
\boxed{
v_{\max}(0)=3.
}
\]

This is the exact ballistic front velocity in lattice-site units per reduced-model time unit.

---

## 4. Gapped staggered-volume phase

For

\[
H_m=H_0+m\sum_j(-1)^jZ_j
\]

the two-band dispersion is

\[
\boxed{
E_\pm(k)=\pm\sqrt{4m^2+9\cos^2k}.
}
\]

Its group velocity magnitude is

\[
v(k)
=
\frac{9|\sin k\cos k|}
{\sqrt{4m^2+9\cos^2k}}.
\]

Let

\[
x=\cos^2k.
\]

Then

\[
v^2(x)
=
\frac{81x(1-x)}{4m^2+9x}.
\]

The stationary condition is

\[
9x^2+8m^2x-4m^2=0.
\]

For \(m\neq0\),

\[
x_*=
\frac{-4m^2+\sqrt{16m^4+36m^2}}{9}.
\]

Substitution gives the exact simplification

\[
\boxed{
v_{\max}(m)
=
\sqrt{4m^2+9}-2|m|.
}
\]

Equivalent forms are

\[
\boxed{
v_{\max}
=
\sqrt{\Delta_{\rm sp}^2+9}
-
\Delta_{\rm sp},
\qquad
\Delta_{\rm sp}=2|m|,
}
\]

and

\[
\boxed{
v_{\max}
=
\frac{9}{\sqrt{4m^2+9}+2|m|}.
}
\]

Therefore

\[
v_{\max}(m)<3
\quad (m\neq0),
\]

and for large mass

\[
\boxed{
v_{\max}(m)
\sim
\frac{9}{4|m|}.
}
\]

---

## 5. Exact velocity-correlation-length identity

The already derived correlation length is

\[
\boxed{
\xi^{-1}
=
\operatorname{arsinh}\left(\frac{2|m|}{3}\right).
}
\]

Using

\[
e^{-\operatorname{arsinh}s}
=
\sqrt{1+s^2}-s,
\]

with

\[
s=\frac{2|m|}{3},
\]

we get

\[
\sqrt{4m^2+9}-2|m|
=
3e^{-\operatorname{arsinh}(2|m|/3)}.
\]

Hence

\[
\boxed{
\frac{v_{\max}(m)}{3}
=
e^{-1/\xi(m)}.
}
\]

This is an exact relation of the reduced staggered-volume model.

Interpretation:

- increasing the oriented-volume staggered mass increases the gap;
- the same deformation shortens the static correlation length;
- and it slows the ballistic information front;
- all three are locked by exact analytic identities.

This is much stronger than an empirical correlation.

---

## 6. What this establishes

The reduced BQG chain now has a coherent static/dynamical structure:

\[
\boxed{
m
\to
\Delta_{\rm sp}
\to
\xi
\to
v_{\max}.
}
\]

More explicitly,

\[
\boxed{
\Delta_{\rm sp}=2|m|,
}
\]

\[
\boxed{
\xi^{-1}=\operatorname{arsinh}(\Delta_{\rm sp}/3),
}
\]

\[
\boxed{
v_{\max}
=
\sqrt{\Delta_{\rm sp}^2+9}-\Delta_{\rm sp}
=
3e^{-1/\xi}.
}
\]

The many-body nested-commutator theorem also shows that no local operator front can appear before graph distance order.

---

## 7. What remains open

This is not yet the physical speed of light.

The following are still required:

1. projector-derived physical graph histories;
2. a theory-specific physical clock;
3. a many-body generator acting on those physical histories;
4. a controlled continuum/refinement limit;
5. an emergent isotropic cone;
6. matching of the same cone in gravity and matter/photon sectors.

Only after these steps may a lattice/operator front be promoted to a physical Lorentz cone.

The next target is therefore

\[
\boxed{
P_{\rm phys}
\to
\text{physical history}
\to
H_{\rm phys}^{\rm local}
\to
\text{operator front}
\to
v_{\rm causal}
\to
g_{\mu\nu}^{\rm Lorentz}.
}
\]
