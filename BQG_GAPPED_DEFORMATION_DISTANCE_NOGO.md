# BQG gapped deformation and scalar-distance no-go

Status: **EXACT for the defined reduced quadratic deformation; physical fundamentality of the deformation remains CANDIDATE.**

## 1. Starting point

The canonical reduced chain is unitarily equivalent to the open XX model

$$
H_0\simeq \frac32(M-1)I-\frac34\sum_j(X_jX_{j+1}+Y_jY_{j+1}),
$$

or after Jordan-Wigner

$$
H_0=\frac32(M-1)I-\frac32\sum_j(c_j^\dagger c_{j+1}+c_{j+1}^\dagger c_j).
$$

Its mutual information is critical:

$$
I_0(r)\sim \frac{\kappa}{r}.
$$

## 2. Minimal exactly solvable gapped deformation

Add a staggered logical field in the XX frame,

$$
\boxed{
H_m=H_0+m\sum_j(-1)^j Z_j.
}
$$

This remains quadratic after Jordan-Wigner. Since

$$
Z_j=1-2n_j,
$$

it is a staggered fermion mass / alternating onsite potential.

In the original intertwiner basis the XX-frame $Z$ axis is the rotated local $Y$ axis. Since the exact one-node oriented volume is

$$
Q_j=\frac{\sqrt3}{4}Y_j,
$$

the deformation is proportional, up to the fixed local rotation and normalization, to a staggered oriented-volume bias

$$
\boxed{
H_m-H_0\propto \sum_j(-1)^j Q_j.
}
$$

So the deformation has a direct local quantum-geometric interpretation rather than being introduced only as a numerical regulator.

## 3. Exact spectrum and gap

Using a two-site unit cell, the single-particle bands are

$$
\boxed{
E_\pm(k)=\pm\sqrt{(2m)^2+9\cos^2 k}.
}
$$

The minimum positive one-particle energy occurs at $k=\pi/2$:

$$
\boxed{
\Delta_{\rm sp}=2|m|.
}
$$

Thus every nonzero $m$ gaps the critical point.

## 4. Exact correlation length

The nearest complex branch point obeys

$$
\cos k_*=\pm i\frac{2m}{3}.
$$

Hence the inverse correlation length is

$$
\boxed{
\xi^{-1}=\operatorname{arsinh}\left(\frac{2|m|}{3}\right),
}
$$

or

$$
\boxed{
\xi(m)=\frac{1}{\operatorname{arsinh}(2|m|/3)}.
}
$$

For small $m$,

$$
\boxed{
\xi\sim\frac{3}{2|m|}.
}
$$

For the independent gate value $m=0.2$,

$$
\boxed{
\Delta_{\rm sp}=0.4,
\qquad
\xi\approx7.5221112995.
}
$$

## 5. Spin/intertwiner correlation asymptotics

The physical logical-spin transverse correlator still contains the Jordan-Wigner string and is represented by a Toeplitz determinant.

In the gapped phase its large-distance asymptotics has the form

$$
\boxed{
C_{xx}(r)\sim A(m)\,r^{-1/2}e^{-r/\xi}.
}
$$

The two-site mutual information is quadratic in the small connected correlators. Therefore

$$
\boxed{
I_m(r)\sim B(m)\,r^{-1}e^{-2r/\xi}.
}
$$

Thus the mutual-information correlation length is

$$
\boxed{
\xi_I=\frac{\xi}{2}.
}
$$

The reproducible finite-chain gate at $m=0.2$ confirms both asymptotic scales without diagonalizing the full $2^M$ spin Hilbert space.

## 6. Critical versus gapped phases

Critical reduced chain:

$$
\boxed{
I_0(r)\sim\frac{\kappa}{r}.
}
$$

Gapped staggered-volume phase:

$$
\boxed{
I_m(r)\sim B(m)r^{-1}e^{-2r/\xi}.
}
$$

The same underlying graph distance $r$ therefore produces qualitatively different $I(r)$ laws in two controlled phases of the same reduced model.

## 7. No-go theorem for a universal scalar distance $d=f(I)$

Assume a phase-independent scalar function $f$ is supposed to reconstruct a distance asymptotically proportional to graph distance:

$$
d(r)=f(I(r))\sim ar+b.
$$

### Critical phase

Because

$$
I_0(r)\sim\frac{\kappa}{r},
$$

we have

$$
r\sim\frac{\kappa}{I},
$$

so asymptotic linearity requires

$$
\boxed{
f(I)\sim \frac{A}{I}\qquad(I\to0).}
$$

### Gapped phase

Because

$$
I_m(r)\sim B r^{-1}e^{-2r/\xi},
$$

the exponential dominates the inversion and

$$
r=\frac{\xi}{2}\log\frac1I+O(\log\log(1/I)).
$$

Therefore asymptotic linearity requires

$$
\boxed{
f(I)\sim A'\log\frac1I\qquad(I\to0).}
$$

The two required asymptotics are incompatible.

Hence:

$$
\boxed{
\textbf{No single phase-independent scalar function }d=f(I_{ij})
\textbf{ can be asymptotically linear in both the critical and gapped phases.}
}
$$

This is a genuine no-go for using pairwise mutual information alone as a universal emergent metric coordinate in the present program.

## 8. Consequence for BQG emergence

The distance functional must depend on more structure than one scalar pair mutual information. Candidate additional data include:

- the local phase / gap data;
- the correlation length extracted from neighborhoods;
- the full reduced density matrix rather than only $I$;
- conditional mutual information;
- multipartite entanglement structure;
- graph Laplacian / transfer operator;
- information-geometric or modular-flow data.

The next frontier is therefore not to choose another post-hoc $f(I)$, but to construct a distance estimator from **network-level relational data** and test whether it is phase robust.

## 9. Reproducibility

Gate:

`python scripts/bqg_gapped_distance_nogo_gate.py`

The gate checks:

1. the exact gapped single-particle spectrum;
2. $\Delta_{\rm sp}=2|m|$;
3. $\xi^{-1}=\operatorname{arsinh}(2|m|/3)$;
4. finite-chain $C_{xx}$ asymptotics;
5. finite-chain mutual-information asymptotics;
6. $\xi_I=\xi/2$;
7. the critical/gapped scalar-distance incompatibility.
