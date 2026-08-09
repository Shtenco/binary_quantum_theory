# DeWitt coefficient selected by HDA closure

Status: **classical identity + independent finite spectral regression**.

Consider the one-parameter family

\[
H_c[N]=\int d^3x\,N\left[\frac{\pi_{ab}\pi^{ab}-c\pi^2}{\sqrt q}-\sqrt q\,R\right].
\]

With the canonical ADM conventions used by `scripts/classical_hda_safe_window_gate.py`, direct variation gives

\[
\boxed{
\{H_c[N],H_c[M]\}
=D[\beta]
+4\left(c-\frac12\right)
\int d^3x\,\pi\left(N\nabla^2M-M\nabla^2N\right),
}
\]

where

\[
\beta^a=q^{ab}(N\partial_bM-M\partial_bN).
\]

For generic canonical data and arbitrary lapses the second term can vanish identically only when

\[
\boxed{c=\frac12.}
\]

Therefore the ordinary first-class hypersurface-deformation algebra selects the GR inverse-DeWitt trace coefficient rather than leaving it as a free kinetic parameter.

## Independent numerical regression

On the same smooth low-mode `L=7` state used by the classical HDA safe-window benchmark:

| c | HDA defect against `D[beta]` |
|--:|--:|
| 0.20 | 8.078e-2 |
| 0.30 | 5.534e-2 |
| 0.40 | 2.846e-2 |
| 0.45 | 1.444e-2 |
| **0.50** | **4.65e-9** |
| 0.55 | 1.486e-2 |
| 0.60 | 3.018e-2 |
| 0.70 | 6.223e-2 |
| 0.80 | 9.635e-2 |

The measured bracket shift is linear in `c-1/2`.  Dividing the measured shift by

\[
I=\int d^3x\,\pi(N\nabla^2M-M\nabla^2N)
\]

gives the predicted coefficient `4(c-1/2)` to roughly `10^-6` relative precision on this finite spectral grid.

## Consequence for CIMFIG/quantum-link gravity

The two previously separate Lorentzian targets are now linked:

1. flux-space DeWitt inertia must approach
   \[
   (5+,1-,3\,0),
   \]
   with the three null directions equal to Gauss/frame rotations;
2. the quantum constraint algebra must approach the HDA;
3. HDA closure itself fixes the trace kinetic coefficient to `c=1/2`.

Thus a microscopic model that yields a different trace coefficient cannot be repaired by merely rescaling Newton's constant.  Unless an additional first-class constraint changes the theory, it belongs to a different universality class (for example a lambda-deformed/Hořava-like kinetic theory), not GR.

## Quantum killer test

In the double safe window of `HDA_SAFE_WINDOW_GATE.md`, reconstruct the quadratic kinetic form of the microscopic constraint and fit

\[
K=\pi_{ab}\pi^{ab}-c_{eff}(j,k)\pi^2+\cdots.
\]

The same held-out run must satisfy

\[
\boxed{c_{eff}\to\frac12}
\]

and

\[
\boxed{\Delta^Q_{HH}\to0.}
\]

These are not independent knobs: failure of the first generically produces the explicit scalar anomaly term above in the second.
