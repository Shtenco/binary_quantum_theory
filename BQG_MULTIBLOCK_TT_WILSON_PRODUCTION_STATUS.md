# BQG five-block bridge — production status

Status: **downstream microscopic signed-gravity extraction is executable on a compressed orthonormal P/Q Krylov basis; the actual five-block E/S amplitude contraction and the connected physical 1PI bridge remain open.**

No new microscopic dynamics is introduced.

## Frozen operator

\[
\boxed{G_{frozen}=-\frac23H_E^{sine}-\frac{32}{9}S},
\qquad
S=-\frac{i}{2}(L_{raw}-L_{raw}^\dagger).
\]

`R_op` is not part of this gravitational TT spatial precursor.

## Correct retained carrier

The frozen six q directions of one block are the already-derived background-orthogonal strict-interior q4 coarse-edge boundary tangents, ordered

```text
(01),(02),(03),(12),(13),(23).
```

They are the same q frame used by the measured map `M_hq`. The static maximal-symmetric j=3 block is rank one and is not a production metric carrier.

For the centered patch use the actual 16-cell parent tetrahedron `0` and its four shared-face neighbours. This gives 30 labelled q directions.

Let their raw overlap matrix be

\[
K_P=V^\dagger V.
\]

The diagonal is unit-normalized by the frozen tangent rule; cross-block overlaps are measured rather than forced to zero.

## Production basis without dense Hilbert materialization

The boundary tensors are not expanded into a dense `2^24` basis. The heavy producer computes overlaps and operator matrix elements by exact tensor-network contraction.

1. Whiten the retained span only:

\[
Q_P=V K_P^{-1/2}.
\]

2. Generate target-independent E/S histories, project out `span(Q_P)`, and whiten their residual Gram. Call the resulting orthonormal complement `Q_Q`.

3. Form the small orthonormal effective basis

\[
W=[Q_P,Q_Q].
\]

4. Measure directly

\[
E_W=W^\dagger H_E^{sine}W,
\qquad
S_W=W^\dagger S W,
\]

plus compression leakage

\[
\eta_O=\|(1-WW^\dagger)OW\|/\|OW\|,
\qquad O\in\{H_E^{sine},S\}.
\]

The production seam requires the declared basis to be closed at the frozen tolerance and refuses target fitting.

## Signed compressed operator

`scripts/bqg_signed_5block_operator_assembler.py` consumes `E_basis`, `S_basis`, raw `P_gram`, labels/geometry and provenance and forms only

\[
G_W=-\frac23E_W-\frac{32}{9}S_W.
\]

It never asks for a full microscopic `N x N` Hilbert matrix.

## Schur in orthonormal P/Q space

With

\[
G_W=\begin{pmatrix}A&B\\B^\dagger&D\end{pmatrix}
\]

the extractor uses

\[
C_{eff}^{orth}=A-BD^+B^\dagger.
\]

A zero/gapless Q mode coupled to P causes the hard stop

```text
GAPLESS_COUPLED_Q_MODE_REQUIRES_PROMOTION
```

rather than an `i eta` or fitted denominator.

The effective quadratic form is returned to the original labelled q frame:

\[
C_{eff}^{q}=K_P^{1/2}C_{eff}^{orth}K_P^{1/2},
\]

and the normalized-state Hessian is

\[
\boxed{K_q=2\Re C_{eff}^{q}-2C_{00}\Re K_P}.
\]

Then

\[
K_h=M_{hq}^{-T}K_qM_{hq}^{-1}.
\]

The spatial center+four-neighbour Fourier symbol is TT-projected and tested for masslessness, positive/isotropic leading k2, reciprocity and exact closure in the frozen six-dimensional quartic basis.

A passing run may emit only

\[
\boxed{\mathbf c_{micro,spatial}^{BQG}}.
\]

`c_BQG_IR` remains null.

## Existing reusable upstream results

The recovered `research/bcqg-core-candidate-v1` branch already supplies:

- L1 closed 16-cell habitat: 384 fine tetrahedra / 768 dual links;
- 16 canonical parent blocks, four face-neighbours each;
- exact physical-sine Euclidean action;
- exact complete six-link SU(2) face recoupling;
- exact strict q4 boundary contraction and six-edge tangent rank;
- exact background removal and canonical orthonormal six-edge frame;
- q4 crossing/environment sectors restoring full source rank 24;
- one-E face support through j<=4;
- conservative one-S face support through j<=6;
- depth-2 target-independent wall through j<=9;
- Hermitian Lorentzian primitives;
- measured full-rank `M_hq`, with condition number sqrt(2);
- sparse Gram/whitening and Schur-gap algorithms.

These are reused as operator primitives, not redefined.

## Remaining heavy amplitude calculation

```text
actual center parent 0 + four face-neighbours
 -> construct the 30 frozen strict-boundary q tangents
 -> exact shared-face gluing / complete recoupling
 -> target-independent E/S depth<=2 boundary histories
 -> P whitening, Q residual whitening
 -> direct tensor-network E_W and S_W matrix elements
 -> leakage / support-wall closure
 -> signed G_W
 -> Q-gap / Schur
 -> K_q -> measured M_hq -> K_h(k) -> TT
 -> c_micro_spatial_BQG
```

No GR ratio, TT result, observed dispersion or Wilson target may alter the basis.

## Physical bridge still required

The microscopic spatial precursor is not a physical graviton 1PI function. The physical vector requires the separate existing-constraint chain

\[
\boxed{
\{C_A\}
\to P_{phys}/\eta
\to Z_{phys}[J_g]
\to W_{phys}[J_g]
\to\Gamma_{phys}[g]
\to\Gamma_{TT}^{(2)}(\omega,\mathbf k)
\to\mathbf c_{BQG}^{IR}.
}
\]

Only the final connected physical pole data may be called `c_BQG_IR`.