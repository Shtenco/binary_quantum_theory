# Two-node regulator-safe Peter--Weyl x route Euclidean HDA preregistration

Status: **frozen before the first two-node joint calculation.**

## Operator and input

Use the existing genuine-volume, orientation-covariant Euclidean Peter--Weyl
node Hamiltonians at

$$
J_{\max}=\frac52
$$

on the frozen all-$j=1/2$, all-$K=0$ K5 input.  Use nodes `(0,1)` only.

On the common two-direction route habitat define

$$
R[N;Q_g]
=\frac12\left\{N,\sqrt{Q_g^{AB}P_AP_B}\right\},
$$

where

$$
Q_g^{AB}
=\frac12\left(Q_{g,0}^{AB}+Q_{g,1}^{AB}\right)
$$

is the average diagonal intertwiner flux Gram matrix from the two endpoint
nodes.  At each node use local non-shared legs `(1,2)` in that node's sorted
neighbour order.  No inverse volume is inserted.

The single smeared joint constraint is

$$
\boxed{
H[N]
=N(x_0)H_0^E+N(x_1)H_1^E+R[N;Q].
}
$$

There is one lapse $N$ and one constraint operator; the route term is not given
an independent multiplier or fitted coupling constant.

## Frozen lapse/route probe

Use a dimensionless periodic route sheet `(y,z)` of size `2 pi`, physical patch
scale `epsilon`, and

$$
P_{phys}=P_y/\epsilon.
$$

Freeze

$$
N(y,z)=0.9+\epsilon[0.13\sin y+0.07\cos z],
$$

$$
M(y,z)=1.1+\epsilon[0.11\cos y+0.09\sin z].
$$

Place node 0 at dimensionless `(0,0)` and node 1 at `(1,0)`, and use WKB probe

$$
f(y,z)=\exp[i(8y+7z)].
$$

Use path lattice `L=48` and regulator sequence

$$
\boxed{\epsilon=(1/4,1/8,1/16,1/32,1/64)}.
$$

No carrier, lattice size, metric legs or coefficients may be changed after
opening the results.

## Exact decomposition to report

Let

$$
a=N(x_0),\quad b=N(x_1),\quad c=M(x_0),\quad d=M(x_1).
$$

Then

$$
[G_N,G_M]=(ad-bc)[H_0^E,H_1^E].
$$

For the full joint commutator report separately

1. route-only residual relative to the frozen
   $D[Q(NdM-MdN)]$ target;
2. geometry--route cross norm divided by the same $D$ norm;
3. pure Euclidean geometry HH norm divided by $D$ norm;
4. complete joint residual divided by $D$ norm.

All geometry sectors must be combined before the final norm; orthogonality may
not be assumed if keys overlap.

## Frozen scaling predictions

For the smooth lapse placement above,

$$
ad-bc=O(\epsilon).
$$

The physical WKB diffeomorphism action has

$$
\|D f\|=O(\epsilon^{-1}).
$$

Therefore the parameter-free finite architecture predicts

$$
\boxed{\Delta_{EE}=O(\epsilon^2)}
$$

for the pure two-node geometry commutator relative to the RHS.

The already independent one-node result predicts

$$
\boxed{\Delta_{cross}=O(\epsilon)}.
$$

Consequently the complete residual should be cross dominated:

$$
\boxed{\Delta_{joint}=O(\epsilon)}.
$$

## Pass/fail rule

The two-node Euclidean gate passes only if all are true:

1. the actual safe $[H_0^E,H_1^E]$ is computed, not replaced by its known norm;
2. its un-smeared commutator norm reproduces `1.681559985798016` within `5e-8`;
3. route-only defect at the final regulator is below `1e-4`;
4. fitted cross exponent is in `[0.75,1.25]`;
5. fitted pure-geometry relative exponent is in `[1.75,2.25]`;
6. fitted full-joint exponent is in `[0.75,1.25]`;
7. final full-joint defect at `epsilon=1/64` is below `0.02`;
8. no per-channel normalization, refit or subtraction is performed.

A failure remains a failure; the test will not be weakened after observing the
result.

## Scope if it passes

A PASS would establish a **two-node Euclidean off-shell scaling control on one
frozen WKB habitat probe**.  It would still not prove the full quantum HDA,
because the Lorentzian $H_L$ amplitudes, operator-valued rather than diagonal
metric insertions, multiple habitat channels and collective-spin scaling would
remain to be tested.
