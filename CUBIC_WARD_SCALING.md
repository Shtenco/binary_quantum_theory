# Cubic Ward scaling on the 4D Regge scaffold

Status: **direct nonlinear finite-lattice gauge-restoration evidence; not a proof of the full microscopic theory**.

## Question

The quadratic Fierz--Pauli test and the direct cubic Regge/EH action comparison still leave a crucial possibility: a discretization can approximate selected action coefficients while failing the nonlinear gauge identity that ties the free spin-2 theory to Einstein self-interaction.

This calculation tests that identity directly.

Take

\[
g_{\mu\nu}=\delta_{\mu\nu}+\lambda h_{\mu\nu}
\]

and a periodic infinitesimal vector field $\xi^\mu$.  The Lie derivative splits as

\[
\delta g_{\mu\nu}
=\delta_0 g_{\mu\nu}+\lambda\,\delta_1 g_{\mu\nu},
\]

with

\[
\delta_0 g_{\mu\nu}=\partial_\mu\xi_\nu+\partial_\nu\xi_\mu
\]

and

\[
\delta_1 g_{\mu\nu}
=\xi^\rho\partial_\rho h_{\mu\nu}
+h_{\rho\nu}\partial_\mu\xi^\rho
+h_{\mu\rho}\partial_\nu\xi^\rho.
\]

At order $\lambda^2$ diffeomorphism invariance requires

\[
\boxed{\delta_0S_3+\delta_1S_2=0}.
\]

We extract the two terms **separately** by directional finite differences of the action and define

\[
\boxed{
W_3=
\frac{|\delta_0S_3+\delta_1S_2|}
{|\delta_0S_3|+|\delta_1S_2|}
}.
\]

No TT projector is used.

## Continuum control

The same deterministic three-wave metric field used in `REGGE_EH_CUBIC_BRIDGE.md` is combined with

\[
\xi^\mu(x)=v^\mu\sin(2\pi x_1/L),
\]

where $v\propto(0.7,-0.2,0.4,0.1)$.

The continuum Einstein--Hilbert action is recomputed directly from Christoffels and the Ricci tensor with spectral derivatives.  At `L=5` the separated coefficients are approximately

\[
\delta_0S_3=-134.5147571,
\qquad
\delta_1S_2=+134.5147569,
\]

which gives

\[
\boxed{W_3^{EH}\simeq5.7\times10^{-10}}.
\]

At `L=6` the independent control gives $W_3^{EH}\simeq8.3\times10^{-10}$.  Thus the numerical extraction itself resolves the Ward cancellation to about nine decimal orders.

## Regge result

The identical $h$ and $\xi$ fields are mapped to the finite 4D Regge lattice through edge contractions.  The result is:

| L | $\delta_0S_3$ | $\delta_1S_2$ | $W_3$ |
|--:|--:|--:|--:|
| 3 | -16.06816 | 21.97258 | 0.155213 |
| 4 | -34.98604 | 39.41650 | 0.0595471 |
| 5 | -51.43277 | 55.10237 | 0.0344449 |
| 6 | -67.15733 | 70.27322 | 0.0226725 |
| 7 | -82.35137 | 85.05254 | 0.0161356 |
| 8 | -97.16726 | 99.54813 | 0.0121031 |

The Ward defect falls monotonically across all tested sizes.

A power fit gives

\[
W_3\sim L^{-2.56}
\]

on `L=3..8`,

\[
W_3\sim L^{-2.30}
\]

on `L=4..8`, and, using the cleaner asymptotic window,

\[
\boxed{W_3\sim L^{-2.23}}
\]

on `L=5..8`.

The observed power is compatible with the interpretation that the violation is a lattice artefact that vanishes at least approximately as the leading $O(k^2)$ correction.

## Robustness

The result is insensitive at the quoted precision to the finite-difference and amplitude windows.  For example:

- `L=5`, varying `lambda_max=0.02..0.04` and `alpha=1e-5..1e-4` keeps $W_3$ in approximately `0.0344447..0.0344468`;
- `L=6` under the same variation keeps $W_3$ in approximately `0.0226722..0.0226736`.

This stability is much smaller than the finite-size trend itself.

## What has actually changed

Before this calculation the repository had:

1. exact/finite linear gauge null checks;
2. a continuum spin-2 bootstrap;
3. a nonlinear spectral ADM HDA calculation performed **inside** a continuum ADM ansatz;
4. local nonlinear Regge probes.

Those did not directly show that a nonlinear gauge identity is restored by the Regge discretization.

The new result supplies exactly that missing finite-lattice check on a fixed 4D scaffold:

\[
\boxed{
\delta_0S_3+\delta_1S_2
\longrightarrow0
\quad\text{as the lattice is refined in the tested sequence.}
}
\]

Together with the unprojected quadratic result and the direct cubic action comparison, the current finite-Regge chain is now

\[
\boxed{
\text{full metric Hessian}\to\text{Fierz--Pauli},
\qquad
S_2,S_3\to S_{EH},
\qquad
W_3\to0.
}
\]

## What this still does not prove

The result is **not** yet the full binary-gravity bridge, because the calculation starts from a predefined 4D Regge scaffold and a smooth metric field used to probe it.  Still open are:

1. deriving the Regge/metric phase from one frozen microscopic edge-bit/frame rewrite rule set;
2. showing that $d_s\to4$ without putting four dimensions into the scaffold;
3. showing exactly two gapless physical spin-2 modes and ghost decoupling in that microscopic ensemble;
4. regulator/blocking independence of the effective coefficients;
5. Lorentzian quantum measure/unitarity;
6. matter, chirality and anomaly cancellation;
7. experiment.

Thus this closes an important **Regge -> nonlinear GR** sub-bridge, while the larger

\[
\text{binary rules}\dashrightarrow\text{Regge/metric phase}
\]

arrow remains the principal open derivation.

## Reproduction

```bash
python scripts/cubic_ward_scaling.py \
  --sizes 3 4 5 6 7 8 \
  --grid 8 \
  --lam-max 0.03 \
  --nlam 9 \
  --alpha 3e-5 \
  --output verification_results/cubic_ward_scaling.json
```
