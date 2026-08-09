# First regulator-safe Peter--Weyl K5 HH column

Status: **regulator-safe first-column diagnostic; Euclidean/genuine-volume HDA still FAILS. Full Lorentzian HDA remains OPEN.**

## Why this calculation is different from the old 140D result

The old vector-5 model is the `Jmax=1/2` Peter--Weyl truncation. A local
Hamiltonian can hit one link twice and an `HH` composition can hit a shared
link four times. Therefore an all-`j=1/2` boundary requires

$$
\boxed{J_{max}^{safe}=\frac12+2=\frac52}.
$$

The calculation below uses

$$
\mathcal H_{link}^{J_{max}}
=\bigoplus_{j\le J_{max}}V_j^L\otimes V_j^R
$$

with `Jmax=5/2`, exact Clebsch--Gordan multiplication by the fundamental
holonomy, oriented four-valent intertwiners, and the genuine local volume

$$
\boxed{V_v=\sqrt{|J_1\cdot(J_2\times J_3)|}}.
$$

The volume acts on the full magnetic node tensor between holonomy factors.
Projection to the Gauss/intertwiner basis is performed only after a complete
gauge-invariant local term. Projecting after every fundamental holonomy would
erase charged intermediate states and can make the Hamiltonian vanish
spuriously.

The orientation convention is the same geometric tetrahedral convention that
restores all-pair permutation covariance in the `Jmax=1/2` diagnostic: for the
sorted four-neighbour list, the triple omitting neighbour `r` receives sign
`(-1)^r`.

## 1. One genuinely safe HH column

Input state:

- all ten K5 links: `j=1/2`;
- all five four-valent recoupling labels: `K=0`.

The exact sparse calculation evaluates both orders

$$
H_0H_1|\psi_0\rangle,
\qquad
H_1H_0|\psi_0\rangle
$$

and subtracts them. The resulting commutator has

$$
\boxed{\|[H_0,H_1]\psi_0\|=1.681559985798016}
$$

and, after numerical zero pruning, 510 spin-network output states.

The norm-squared returning to the original all-`j=1/2` 32-dimensional sector is

$$
\boxed{f_{1/2}=0.29790166313739946},
$$

hence

$$
\boxed{f_{out}=0.7020983368626005},
\qquad
\boxed{\epsilon_{out}=0.8379130843128066}.
$$

The actually reached maximum spin is only

$$
\boxed{j_{max}^{reached}=\frac32<\frac52},
$$

so this column is safely separated from the representation wall.

The fixed-sector part is not random: the two surviving all-`j=1/2` amplitudes
are an antisymmetric exchange of the node-0/node-1 intertwiner excitation, with
equal magnitude and opposite sign. A tangential-like shape component therefore
survives, but it is accompanied by a large physical spin-changing channel.

### Interpretation

The old `Jmax=1/2` graph leakage cannot be blamed only on the cutoff. A first
genuinely safe column still has a large out-of-sector component. Remaining
suspects are now operator content and ordering, especially the missing real-
Ashtekar--Barbero Lorentzian term, plus the later continuum limit.

This is **not** yet a full HDA failure: only one safe input column has been
computed and the correct discrete tangential generator `D(k,l)/(3V)` has not
been subtracted. It is sufficient, however, to reject the hypothesis that
raising `Jmax` alone automatically restores the fixed-simplex algebra.

## 2. The old BF vertex is not the physical-volume kernel

The independently contracted old five-tetrahedron state `V5` has 12 nonzero
components and norm squared `7/18` before normalization. Applying the same
regulator-safe genuine-volume node Hamiltonian gives

$$
\boxed{\|H_0^{safe}|V_5\rangle\|=1.4002194669856702}.
$$

After pruning numerical zeros:

- output support: 251 spin-network states;
- component remaining in the original all-`j=1/2` 32D sector: **zero**;
- maximum spin reached: `j=1`.

Therefore

$$
\boxed{
H_v^{old}|V_5\rangle=0
\quad\not\Rightarrow\quad
H_v^{safe}|V_5\rangle=0.
}
$$

The earlier unique `V5` kernel remains a valuable exact **BF/15j-like finite
constraint result**, but it is not universal under replacement of the
occupancy-projector volume by the genuine Peter--Weyl four-valent volume.
Preserving `V5` must therefore not be used as a tuning condition for the
canonical Hamiltonian.

## 3. Canonical and covariant routes must not be mixed

There are now two distinct consistency routes.

### Canonical real-SU(2) route

The Peter--Weyl calculation is a canonical Ashtekar--Barbero calculation. The
phase space is already expressed in the SU(2) connection/flux variables. An
EPRL simplicity projector should **not** be inserted as another operator before
the canonical Hamiltonian. The next canonical sequence is

$$
\boxed{
H_E
\;\longrightarrow\;
H_E+H_L^{(\beta)}
\;\longrightarrow\;
\Delta_\beta
\;\longrightarrow\;
\Delta_{HH}^{Q}.
}
$$

### Covariant BF/spinfoam route

The independent covariant route starts from a BF/Spin(4) or Lorentzian
bivector description and uses simplicity to select gravitational data,

$$
\boxed{
BF\xrightarrow{\;P_{simp}\;}\text{EPRL/FK-like gravity amplitudes}.
}
$$

That route remains an important cross-check of the same semiclassical gravity,
but it is not a sequential preprocessing step inside the real-SU(2) canonical
Hamiltonian.

This distinction matters because the old `V5` state is BF-like whereas the new
Peter--Weyl Hamiltonian is canonical. Their mismatch is therefore information,
not something to remove by forcing the old state to remain a kernel.

## 4. Why the next exact calculation is tractable

The complete regulator-safe Euclidean `HH` reachable space is already bounded
combinatorially:

- 4193 Gauss-admissible global spin assignments;
- total exact spin-network dimension at most 24364;
- only 163 distinct local four-spin quartets;
- local intertwiner multiplicity never exceeds 3.

Therefore future calculations should cache local CG/recoupling/volume blocks
and act directly in the reachable Gauss basis rather than use magnetic-state
brute force.

## 5. Current joint canonical pass condition

The canonical candidate advances only if one common collective window gives

$$
\boxed{
\Delta_\beta\to0,
\qquad
\Delta_{HH}^{Q}\to0,
\qquad
\operatorname{inertia}K_E\to(5+,1-,3\,0),
\qquad
z\to1.
}
$$

Only after that may the two physical tensor degrees of freedom be inferred
from first-class Dirac counting and independently checked spectrally.
