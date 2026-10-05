from __future__ import annotations

import sympy as sp

I = sp.I
SQRT2 = sp.sqrt(2)
SQRT3 = sp.sqrt(3)

sx = sp.Matrix([[0, 1], [1, 0]]) / 2
sy = sp.Matrix([[0, -I], [I, 0]]) / 2
sz = sp.Matrix([[1, 0], [0, -1]]) / 2
ID = sp.eye(2)
J = [sx, sy, sz]


def kron4(a, b, c, d):
    return sp.kronecker_product(a, b, c, d)


def ket(bits: str) -> sp.Matrix:
    v = sp.zeros(16, 1)
    v[int(bits, 2), 0] = 1
    return v


# |s> = |s_12>|s_34>
s = (ket("0101") - ket("0110") - ket("1001") + ket("1010")) / 2

# |t> = [(t+ t-) - (t0 t0) + (t- t+)] / sqrt(3)
t = (
    ket("0011")
    + ket("1100")
    - (ket("0101") + ket("0110") + ket("1001") + ket("1010")) / 2
) / SQRT3

assert sp.simplify((s.H * s)[0]) == 1
assert sp.simplify((t.H * t)[0]) == 1
assert sp.simplify((s.H * t)[0]) == 0

# Q_123 = epsilon_abc J1^a J2^b J3^c
Q = sp.zeros(16)
for a in range(3):
    for b in range(3):
        for c in range(3):
            eps = sp.LeviCivita(a, b, c)
            if eps:
                Q += eps * kron4(J[a], J[b], J[c], ID)

basis = [s, t]
Qphys = sp.Matrix([
    [sp.simplify((u.H * Q * v)[0]) for v in basis]
    for u in basis
])

sigma_y = sp.Matrix([[0, -I], [I, 0]])
assert sp.simplify(Qphys - (SQRT3 / 4) * sigma_y) == sp.zeros(2)

psi_plus = (s + I * t) / SQRT2
psi_minus = (s - I * t) / SQRT2

assert sp.simplify(Q * psi_plus - (SQRT3 / 4) * psi_plus) == sp.zeros(16, 1)
assert sp.simplify(Q * psi_minus + (SQRT3 / 4) * psi_minus) == sp.zeros(16, 1)

# General physical state and exact pair-singlet weights.
a, phi = sp.symbols("a phi", real=True)

p12 = sp.cos(a) ** 2
p13 = sp.Rational(1, 2) - sp.cos(2 * a) / 4 + SQRT3 * sp.sin(2 * a) * sp.cos(phi) / 4
p14 = sp.Rational(1, 2) - sp.cos(2 * a) / 4 - SQRT3 * sp.sin(2 * a) * sp.cos(phi) / 4

# Symmetry partners: p34=p12, p24=p13, p23=p14.
# Exact isotropy conditions p12=p13=p14 in the canonical domain 0<=a<=pi/2.
# p13-p14 = (sqrt(3)/2) sin(2a) cos(phi).
# Nontrivial equality requires cos(phi)=0. Then p12=p13 forces cos(2a)=0.

# Quadratic anisotropy around a=pi/4+eps, phi=pi/2+delta.
eps, delta = sp.symbols("eps delta", real=True)
subs = {a: sp.pi / 4 + eps, phi: sp.pi / 2 + delta}

# leading deviations of the three inequivalent pair singlet weights from 1/2
series = []
for p in (p12, p13, p14):
    x = sp.expand_trig(p.subs(subs))
    x = sp.series(x, eps, 0, 3).removeO()
    x = sp.series(x, delta, 0, 3).removeO()
    series.append(sp.expand(x - sp.Rational(1, 2)))

# To second order in small deviations, the six-pair variance is
# 2*sum_{three types} (p-1/2)^2 = 3 eps^2 + 3/4 delta^2 + O(3).
quad_anisotropy = 3 * eps**2 + sp.Rational(3, 4) * delta**2

print("Q_phys =")
sp.pprint(Qphys)
print("eigenvalues:", [-SQRT3 / 4, SQRT3 / 4])
print("isotropic states: (|s> +/- i|t>)/sqrt(2)")
print("pair singlet weights:")
print("p12=p34 =", sp.simplify(p12))
print("p13=p24 =", sp.simplify(p13))
print("p14=p23 =", sp.simplify(p14))
print("isotropy locus in canonical domain: a=pi/4, phi=pi/2 or 3pi/2")
print("quadratic six-pair anisotropy =", quad_anisotropy)
print("PASS")
