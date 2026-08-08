# Field-norm derivation and lattice artefacts

## Eight steps

1. Continuum TT: \(h_{\mu\nu}(x)=\varepsilon_{\mu\nu}\cos(k\cdot x)\), \(\|\varepsilon\|_F=1\).
2. Continuum Euclidean EH: \(S_{\mathrm{cont}}=k^2/4\).
3. Lattice elongation: \(\delta\ell/\ell \simeq n^\mu n^\nu\varepsilon_{\mu\nu}\).
4. Fifteen edge types → \(e=M\varepsilon\in\mathbb{R}^{15}\); embed in 30D Fourier mode (cos sector).
5. Regge form \(Q_{\mathrm{edge}}=v^T H_{\mathrm{kin}} v\) with \(H_{\mathrm{kin}}=-H_{\mathrm{Regge}}\).
6. Edge-norm Rayleigh \(=Q_{\mathrm{edge}}/\|v\|^2\) mixes kinetics with \(\|M\varepsilon\|\).
7. Field-norm: \(Q_{\mathrm{field}}=Q_{\mathrm{edge}}/\|\varepsilon\|_F^2\) (= \(Q_{\mathrm{edge}}\) if unit Frobenius).
8. \(c_{\mathrm{eff}}:=Q_{\mathrm{field}}/(k^2/4)\). Target: \(c_{\mathrm{eff}}\to 1\).

## Artefacts

| source | effect |
|---|---|
| \(M\) overcomplete (15→10), cond≈8 | anisotropic stretch |
| diagonal edges | non-continuum weights |
| cos-only embedding | O(1) factor |
| finite-difference Hessian | truncation |
| finite \(L,k\) | dispersion O((ka)²) |
| units of background_q | overall scale in H |

## Extrapolation (L=3)

Linear fit: \(c_{\mathrm{eff}} \approx 31.4 - 0.64\,k^2\).

\[
c_{\mathrm{eff}}(k\to 0)\approx 31 \neq 1.
\]

Sign of TT kinetics under \(H_{\mathrm{kin}}\) remains correct; **absolute continuum coefficient is not matched**.

## Spin foams

Not used as an escape hatch. Different Hilbert space; continuum limit open in that program too; would discard Gate C2 / Ward progress without fixing \(c_{\mathrm{eff}}\).

## Status

Derivation and artefacts documented. IR Einstein **open**.
