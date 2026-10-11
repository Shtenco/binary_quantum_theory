import json
from pathlib import Path
import sympy as s
x,d=s.symbols('x d',positive=True)
# Exact normalized spectral form on Phi=span{x^(k/2)}.
forms=[[s.simplify(s.integrate(x**s.Rational(i+j,2),(x,0,d))/d) for j in range(6)] for i in range(6)]
lim=s.Matrix([[s.limit(v,d,0,dir='+') for v in row] for row in forms])
assert lim==s.diag(1,0,0,0,0,0)
# Every constraint insertion sqrt(x) vanishes in the limiting form.
assert all(s.limit(s.integrate(x**s.Rational(i+j+1,2),(x,0,d))/d,d,0,dir='+')==0 for i in range(6) for j in range(6))
# Linearized Einstein symbol annihilates longitudinal gauge fluctuations.
g=s.diag(-1,1,1,1); k=s.Matrix(s.symbols('k0:4')); v=s.Matrix(s.symbols('v0:4'))
h=k*v.T+v*k.T; ku=g*k; k2=(k.T*ku)[0]; tr=s.trace(g*h); kh=h*ku; kk=(ku.T*h*ku)[0]
G=s.Matrix(4,4,lambda a,b:s.expand((k2*h[a,b]+k[a]*k[b]*tr-k[a]*kh[b]-k[b]*kh[a]+g[a,b]*(kk-k2*tr))/2))
assert G==s.zeros(4)
# A summable refinement error admits a uniform tail bound.
n=s.symbols('n',integer=True,nonnegative=True); tail=s.summation(s.Rational(1,2)**n,(n,8,s.oo))
assert tail==s.Rational(1,128)
out={'spectral_model':'L2(0,1), M=x, C=sqrt(x), a_delta=delta; identity refinements', 'normalized_form_limit_rank':lim.rank(),'constraint_insertions_vanish':True,'fixed_positive_metric':'q_ab=delta_ab times identity, det q=1','connected_metric_covariance':0,'massless_TT_pole':False,'linear_Einstein_gauge_symbol_exact':True,'summable_error_tail_from_n8':str(tail),'BQG_premises_proved':False}
Path(__file__).with_name('checks.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
