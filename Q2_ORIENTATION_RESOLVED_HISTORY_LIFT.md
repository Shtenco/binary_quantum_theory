# q=2 orientation-resolved reversible history lift

## Purpose

This note closes a narrower question than the full gravitational `g_YC` problem.
It asks whether the already-derived q=2 undirected Hamming/C4 dynamics admits a
minimal reversible **orientation-resolved** history lift in which the geometry
orientation pseudoscalar selects opposite history directions.

The answer is exact under a deliberately narrow set of assumptions:

- the history carrier is the already-derived minimal reversible `C8` shift;
- one microscopic history tick is deterministic and nearest-neighbor;
- the logical geometry orientation `Y_L=+/-1` is conserved during that tick;
- the tick is a real permutation lift, not an arbitrary complex unitary;
- simultaneous reversal of geometry orientation and history direction is a
  symmetry.

Under these assumptions the lift is unique up to the convention for which
orientation is called `+`.

This does **not** compute the coefficient of the full Lorentzian gravitational
constraint.  It identifies the exact odd/history channel of the minimal
reversible lift and shows how the old undirected q=2 adjacency is recovered
when orientation is unresolved.

---

## 1. Ingredients already present in the repository

The geometry-orientation operator is the logical Pauli

\[
Y_L=\begin{pmatrix}0&-i\\ i&0\end{pmatrix},
\qquad Y_L^2=I.
\]

Its eigenprojectors are

\[
P_\pm=\frac{I\pm Y_L}{2}.
\]

The minimal reversible history dilation derived in the preceding q=2 work is
an eight-state cycle with one-step shift

\[
U_8|k\rangle=|k+1\pmod 8\rangle,
\qquad U_8^8=I.
\]

History reversal satisfies

\[
R_hU_8R_h=U_8^{-1}.
\]

A logical geometry reflection `R_g` reverses the orientation pseudoscalar,

\[
R_gY_LR_g^{-1}=-Y_L.
\]

---

## 2. Minimal orientation-resolved one-tick lift

If positive geometry orientation advances one history edge and negative
orientation advances the opposite edge, the one-tick unitary is

\[
\boxed{
W=P_+\otimes U_8+P_-\otimes U_8^{-1}.
}
\]

Because the two `P_+` and `P_-` sectors are orthogonal and both shifts are
unitary,

\[
W^\dagger W=I.
\]

It also preserves geometry orientation,

\[
[W,Y_L\otimes I]=0,
\]

and is invariant under the simultaneous reversal

\[
(R_g\otimes R_h)W(R_g\otimes R_h)^{-1}=W.
\]

---

## 3. The locking operator is not inserted by hand

Define the even history kernel and odd history current

\[
H_{\rm even}=\frac{U_8+U_8^{-1}}{2},
\qquad
C_h=\frac{U_8-U_8^{-1}}{2i}.
\]

Then the Hermitian cosine and sine parts of the single unitary `W` are exactly

\[
\boxed{
\frac{W+W^\dagger}{2}=I\otimes H_{\rm even},
}
\]

and

\[
\boxed{
\frac{W-W^\dagger}{2i}=Y_L\otimes C_h.
}
\]

Therefore, in the normalization fixed by one unit history tick, the odd part of
the minimal orientation-resolved lift has coefficient

\[
\boxed{|g_{YC}^{\rm minimal\ sine}|=1.}
\]

The sign is only the convention for which geometry orientation is called
forward.

This is a **kinematic/minimal-lift coefficient**, not the coefficient of the
full gravitational effective Hamiltonian.

---

## 4. Why the old Hamming adjacency has `g_YC=0`

The original q=2 Hamming graph is undirected.  In Gray-cycle order its
adjacency is

\[
A_{C_4}=S_4+S_4^{-1}.
\]

The odd current is absent from this orientation-unresolved kernel.  Hence

\[
\boxed{g_{YC}^{\rm Hamming}=0.}
\]

This is not in conflict with the minimal oriented lift.  The oriented
information has simply been quotiented out.

---

## 5. Two history ticks recover the original q=2 graph exactly

The active states of the minimal `C8` dilation are the even sites

\[
0,2,4,6.
\]

On that sublattice

\[
U_8^2\big|_{\rm active}=S_4,
\qquad
U_8^{-2}\big|_{\rm active}=S_4^{-1}.
\]

Therefore

\[
W^2\big|_{\rm active}
=P_+\otimes S_4+P_-\otimes S_4^{-1}.
\]

If geometry orientation is unresolved, tracing/summing over the two
orientation sectors gives

\[
\boxed{
S_4+S_4^{-1}=A_{C_4}.
}
\]

After the fixed Gray-to-binary permutation

\[
00,01,11,10\longleftrightarrow00,01,10,11,
\]

this is exactly

\[
\boxed{
A_{q=2}=X\otimes I+I\otimes X,
}
\]

the frozen q=2 Hamming adjacency used elsewhere in the repository.

Thus the undirected q=2 graph can be interpreted, within the stated minimal
assumptions, as the orientation-unresolved quotient of two opposite directed
history sectors.

---

## 6. Minimality/uniqueness within the deterministic permutation class

Restrict one tick in each `Y_L` eigensector to one nearest-neighbor direction,

\[
U_8^{s_+},\quad U_8^{s_-},\qquad s_\pm\in\{+1,-1\}.
\]

Combined orientation reversal exchanges the `+` and `-` geometry sectors and
inverts the history shift.  Exact covariance therefore requires

\[
\boxed{s_-=-s_+.}
\]

The only two possibilities are

\[
(+1,-1),\qquad(-1,+1),
\]

which differ only by the convention for global history orientation.

So `Y_L x C_h` is not one arbitrary allowed nearest-neighbor channel inside
this minimal deterministic class: it is the unique odd part of the equivariant
one-tick lift, up to sign.

---

## 7. What this does and does not say about gravity

There are now three distinct statements which must not be conflated:

```text
g_YC^Hamming              = 0        EXACT for the orientation-unresolved seed
g_YC^minimal_sine         = +/-1     EXACT in one-tick normalized minimal lift
g_YC^gravity              = OPEN     requires the genuine physical history/constraint amplitude
```

The current Peter-Weyl repository already contains genuine amplitudes for
`H_E` and for the prerequisite

\[
K=[V,H_E],
\]

and it contains exact orientation/sign-channel classification for the
Lorentzian epsilon assembler.  But the full genuine-amplitude

\[
H_L\sim\epsilon\,C(K)C(K)C(V)
\]

has not yet been completed.  Therefore the physical gravitational `g_YC`
cannot honestly be read off yet.

The next microscopic calculation is sharply defined: complete the safe
Peter-Weyl Lorentzian amplitude, build the corresponding relational/history
kernel, and project that kernel onto the already frozen channel

\[
Y_L\otimes C_h.
\]

Only that number may be called `g_YC^gravity`.

---

## Status

**EXACT under stated minimal reversible-history assumptions:**

- orientation-resolved controlled shift `W`;
- unitarity and combined-reflection covariance;
- exact cosine/even and sine/odd decomposition;
- `|g_YC^minimal_sine|=1` in one-tick normalization;
- two-tick active restriction;
- recovery of the frozen q=2 Hamming adjacency after orientation is unresolved;
- uniqueness up to global orientation convention within the deterministic
  nearest-neighbor permutation class.

**OPEN PHYSICAL:**

- whether the full safe Peter-Weyl/physical-history dynamics realizes this
  minimal lift;
- the genuine gravitational coefficient `g_YC^gravity`;
- the physical clock/history interpretation of one `C8` tick.
