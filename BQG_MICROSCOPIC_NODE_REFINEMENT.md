# BQG microscopic node-refinement bridge

Status: **implemented finite test.**

The ancilla-assisted edge theorem shows that a spin increase

\[
j\to j+\frac12
\]

requires one new binary spin-\(1/2\) strand per edge.

For the first nontrivial four-valent node refinement

\[
j=\frac12\to1,
\]

add four fresh q=2 endpoint spinors, one on each face.  The four ancillas are
placed in a Gauss-singlet state

\[
|\chi\rangle
\in
\mathrm{Inv}_{SU(2)}[(1/2)^{\otimes4}],
\]

which is itself two-dimensional.

Each old edge plus its ancilla is then projected to the symmetric spin-1
channel,

\[
V_{1/2}\otimes V_{1/2}\to V_1.
\]

After all four edge blockings, project onto the coarse four-spin-1 singlet
space.

This defines a linear node map

\[
T_\chi:
\mathcal H_{1/2}^{\rm sing}
\to
\mathcal H_{1}^{\rm sing}.
\]

Because \(|\chi\rangle\) has two singlet components, the microscopic
construction spans two maps \(T_0,T_1\).

The gate tests whether the already registered canonical refinement intertwiner

\[
W=
\begin{pmatrix}
0&2/3\\
1&0\\
0&-\sqrt5/3
\end{pmatrix}
\]

belongs exactly to

\[
\operatorname{span}\{T_0,T_1\}.
\]

A PASS would prove that the canonical logical refinement map can be generated
from the original binary q=2 microstructure by:

\[
\boxed{
\text{fresh q=2 ancilla singlet}
\to
\text{symmetric edge blocking}
\to
\text{Gauss projection}.
}
\]

The remaining physical question would then be which ancilla singlet the actual
graph-changing/refinement dynamics prepares.
