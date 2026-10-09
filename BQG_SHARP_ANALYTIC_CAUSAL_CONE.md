# BQG sharp analytic propagation cone

Status:
- **PROVED** for the homogeneous reduced free-fermion chain in the stated momentum convention.
- **PROVED** for the gapped staggered-volume deformation inside its analytic strip.
- **OPEN** as a statement about the continuum Lorentz cone of full physical BQG.

## 1. Why the generic Lieb-Robinson estimate is not enough

For a nearest-neighbour many-body Hamiltonian with edge term norm bounded by \(J\), the standard weighted-norm argument gives a valid but loose estimate of the form

\[
\|[A_i(t),B_j]\|
\le
C
\exp[-\mu(d_G(i,j)-v_{\rm LR}(\mu)|t|)]
\]

with a velocity controlled by an interaction norm.

For the current reduced XX chain, this bound is parametrically much larger than the exact quasiparticle front.

Because the chain is exactly free-fermionic, we can do better and derive the propagation exponent directly from the analytic continuation of the exact dispersion.

---

# 2. Critical chain: exact Bessel cone

For \(m=0\),

\[
\varepsilon(k)=-3\cos k.
\]

The one-particle propagator at separation \(r\) is

\[
\boxed{
U_r(t)=i^r J_r(3t).
}
\]

Using the Fourier representation and shifting

\[
k\to k+i\mu,
\qquad \mu>0,
\]

gives

\[
\boxed{
|U_r(t)|
\le
\exp[-\mu r+3|t|\sinh\mu].
}
\]

Therefore the exponential cone velocity at fixed \(\mu\) is

\[
\boxed{
v_\mu^{(0)}
=
3\frac{\sinh\mu}{\mu}.
}
\]

Since

\[
\frac{\sinh\mu}{\mu}>1
\quad(\mu>0)
\]

and

\[
\lim_{\mu\to0^+}
3\frac{\sinh\mu}{\mu}
=
3,
\]

we obtain

\[
\boxed{
v_{\rm front}^{(0)}=3=v_{\max}(0).
}
\]

More precisely, for every \(v>3\) there exists \(\mu>0\) such that

\[
|U_r(t)|
\le
e^{-\mu(r-v|t|)}.
\]

Thus the critical chain has an exponentially suppressed exterior for every cone strictly wider than the exact ballistic front.

---

# 3. Gapped staggered-volume chain

The two-band dispersion is

\[
\boxed{
E_\pm(k)
=
\pm\sqrt{4m^2+9\cos^2k}.
}
\]

The branch points of the analytic continuation satisfy

\[
4m^2+9\cos^2(k+i\mu)=0.
\]

The closest branch point to the real axis occurs at

\[
k=\frac{\pi}{2},
\]

and therefore

\[
\boxed{
\mu_c
=
\operatorname{arsinh}\left(\frac{2|m|}{3}\right).
}
\]

But the previously derived correlation length obeys

\[
\boxed{
\xi^{-1}
=
\operatorname{arsinh}\left(\frac{2|m|}{3}\right).
}
\]

Hence

\[
\boxed{
\mu_c=\xi^{-1}.
}
\]

So the same complex-momentum singularity that fixes the static correlation length also fixes the maximal contour displacement available for the dynamical propagation bound.

---

# 4. Exact imaginary-energy growth inside the analytic strip

Let

\[
0<\mu<\mu_c.
\]

Write

\[
x=\cos^2k,
\qquad
s=\sinh^2\mu.
\]

For

\[
E(k+i\mu)^2
=
4m^2+9\cos^2(k+i\mu),
\]

maximizing the imaginary part over real \(k\) gives

\[
\boxed{
\sup_k |\Im E(k+i\mu)|
=
\frac{v_{\max}(m)}{2}\sinh(2\mu),
}
\]

where

\[
\boxed{
v_{\max}(m)
=
\sqrt{4m^2+9}-2|m|.
}
\]

One convenient intermediate result is that the maximizing

\[
x_*=\cos^2k_*
\]

is

\[
\boxed{
x_*
=
\frac{
(2\sinh^2\mu+1)
\left(
2|m|\sqrt{4m^2+9}-4m^2
\right)
-
9\sinh^2\mu
}{9},
}
\]

which remains in the physical interval throughout the open analytic strip.

At this \(x_*\),

\[
(\Im E)^2
=
\sinh^2\mu\,\cosh^2\mu
\left[
9+8m^2-4|m|\sqrt{4m^2+9}
\right].
\]

The bracket is exactly

\[
\left(\sqrt{4m^2+9}-2|m|\right)^2
=
v_{\max}^2.
\]

Hence the result follows.

**Status: PROVED.**

---

# 5. Sharp exponential cone in the gapped phase

The Bloch Hamiltonian satisfies

\[
H(k)^2=E(k)^2 I.
\]

Therefore

\[
e^{-iH(k)t}
=
\cos(E t)I
-
i\frac{\sin(E t)}{E}H(k).
\]

For every fixed

\[
0<\mu<\mu_c
\]

the contour-shifted matrix prefactor remains bounded because the contour stays away from the branch point.

Thus there exists a finite \(C_m(\mu)\) such that the real-space propagator obeys

\[
\boxed{
\|U_r(t)\|
\le
C_m(\mu)
\exp\left[
-\mu r
+
\frac{v_{\max}(m)}2
|t|\sinh(2\mu)
\right].
}
\]

Define

\[
\boxed{
v_\mu(m)
=
v_{\max}(m)
\frac{\sinh(2\mu)}{2\mu}.
}
\]

Then

\[
\boxed{
\|U_r(t)\|
\le
C_m(\mu)
e^{-\mu[r-v_\mu(m)|t|]}.
}
\]

Since

\[
\frac{\sinh(2\mu)}{2\mu}>1
\]

for finite positive \(\mu\),

\[
v_\mu(m)>v_{\max}(m),
\]

but

\[
\boxed{
\lim_{\mu\to0^+}v_\mu(m)
=
v_{\max}(m).
}
\]

Hence for every velocity

\[
v>v_{\max}(m)
\]

one can choose sufficiently small allowed \(\mu\) such that

\[
v_\mu(m)<v,
\]

and propagation outside \(r=v|t|\) is exponentially suppressed.

Therefore the exact asymptotic ballistic cone is

\[
\boxed{
v_{\rm front}(m)=v_{\max}(m).
}
\]

---

# 6. Static-dynamic singularity unification

We now have three exact statements controlled by the same \(m\):

\[
\boxed{
\Delta_{\rm sp}=2|m|,
}
\]

\[
\boxed{
\xi^{-1}
=
\mu_c
=
\operatorname{arsinh}(\Delta_{\rm sp}/3),
}
\]

\[
\boxed{
v_{\rm front}
=
v_{\max}
=
\sqrt{\Delta_{\rm sp}^2+9}-\Delta_{\rm sp}.
}
\]

And, as derived previously,

\[
\boxed{
\frac{v_{\rm front}}{3}
=
e^{-1/\xi}.
}
\]

So the nearest complex-momentum singularity simultaneously determines:

1. exponential static correlation decay;
2. the analyticity strip of the propagator;
3. the family of rigorous exponential propagation cones.

This is the strongest current causal result of the reduced emergence model.

---

# 7. Interpretation

The reduced model now has the exact chain

\[
\boxed{
m
\to
\Delta_{\rm sp}
\to
\mu_c=\xi^{-1}
\to
v_{\rm front}=v_{\max}.
}
\]

The quantity \(v_{\rm front}\) is not fitted.

It is obtained independently from:

- the maximum real group velocity;
- the \(\mu\to0\) limit of the exponential contour cone.

The two agree exactly.

---

# 8. Scope boundary

This result is still **not** the physical speed of light of BQG.

It is a theorem of the reduced homogeneous free-fermion / staggered-volume model.

To promote it to a gravitational causal cone still requires

\[
P_{\rm phys}
\to
\text{physical graph histories}
\to
H_{\rm phys}
\to
\text{refinement limit}
\to
\text{common gravity/matter cone}.
\]

In particular, the present theorem does not yet prove Lorentz invariance, universality across particle species, or a continuum metric null cone.
