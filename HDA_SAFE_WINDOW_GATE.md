# HDA safe-window gate

Status: **classical spectral benchmark PASS; microscopic quantum HDA still OPEN**.

The future Lorentzian quantum-link theory must be judged against the hypersurface-deformation algebra only in a regulator-safe sector. There are two independent regulator walls.

## 1. Spin wall

For a Peter--Weyl cutoff

\[
\mathcal H_{link}^{J_{max}}=\bigoplus_{j\le J_{max}}V_j^L\otimes V_j^R,
\]

a word of `r` fundamental holonomies cannot feel the cutoff when

\[
\boxed{j_{phys}+r/2<J_{max}.}
\]

## 2. Momentum wall

For lapse Fourier modes `N_k`, `M_p`, the `HH` bracket contains momentum `k+p`. Therefore the spatial discretization is safe only when

\[
\boxed{|k|,|p|,|k+p|\ll k_{Nyquist}.}
\]

A violation outside either safe window is not evidence for a physical HDA anomaly.

## 3. Classical benchmark

Use the ADM Hamiltonian

\[
H[N]=\int d^3x\,N\left[\frac{\pi_{ab}\pi^{ab}-\frac12\pi^2}{\sqrt q}-\sqrt q\,R\right]
\]

and the diffeomorphism generator written as

\[
D[\beta]=\int d^3x\,\pi^{ab}\mathcal L_\beta q_{ab}.
\]

The continuum algebra requires

\[
\boxed{\{H[N],H[M]\}=D[\beta]},
\qquad
\beta^a=q^{ab}(N\partial_bM-M\partial_bN).
\]

`scripts/classical_hda_safe_window_gate.py` computes `H[N]` and `H[M]` independently on a periodic 3D spectral grid, obtains their functional derivatives with automatic differentiation, forms the canonical Poisson bracket, and only then compares it to `D[beta]`.

For one fixed smooth low-mode state with `N=sin(x)`, `M=sin(y)`:

| L | relative HDA defect |
|--:|--:|
| 4 | 5.8461024e-4 |
| 5 | 1.4516924e-5 |
| 6 | 3.6365623e-7 |
| 7 | 4.6492005e-9 |
| 8 | 4.9969145e-11 |

with

\[
\Delta_{HH}=\frac{|\{H[N],H[M]\}-D[\beta]|}{|\{H[N],H[M]\}|+|D[\beta]|}.
\]

The rapid convergence is a **regulator control**, not evidence for the microscopic quantum theory.

## 4. Correct quantum target

For a low-spin coherent state `|Psi_j>` and safe low Fourier modes define

\[
\boxed{
\Delta^{Q}_{HH}(j,k,p)=
\frac{\|P_{safe}([\hat H[N_k],\hat H[N_p]]-i\hbar\hat D[\hat q^{ab}(N_k\partial_bN_p-N_p\partial_bN_k)])|\Psi_j\rangle\|}
{\|P_{safe}[\hat H[N_k],\hat H[N_p]]|\Psi_j\rangle\|+\|P_{safe}\hat D[\cdots]|\Psi_j\rangle\|}
}
\]

where `P_safe` removes states touching either regulator wall.

The gravity candidate passes only if, in one common scaling window,

\[
\Delta^Q_{HH}\to0,
\qquad
\Delta_\beta\to0,
\qquad
\operatorname{inertia}K_E\to(5+,1-,3\,0),
\qquad z\to1.
\]

## 5. Beta projection

For real Ashtekar--Barbero variables the raw Euclidean curvature contains terms linear and quadratic in `beta`. Therefore Immirzi universality must be tested **modulo Gauss/diffeomorphism constraints**, not on the unprojected Hamiltonian:

\[
\boxed{
\Delta_\beta=
\frac{\|P_{G,D}(H^{(\beta_1)}-H^{(\beta_2)})P_{G,D}\|}
{\|P_{G,D}HP_{G,D}\|}
\to0.
}
\]

This prevents a false finite-graph failure from terms that are constraint/boundary contributions in the continuum theory.

## Interpretation

The project now has a clean hierarchy:

1. **classical HDA implementation:** independently verified in a momentum-safe spectral window;
2. **finite gauge kinematics:** Peter--Weyl spin wall is analytically controlled;
3. **Lorentzian quantum dynamics:** still open and must pass both walls simultaneously;
4. only after that may the two physical graviton modes be inferred from the first-class constraint count and independently checked spectrally.
