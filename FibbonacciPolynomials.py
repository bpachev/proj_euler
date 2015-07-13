from proj_euler import matrix_mod_exp
from CR_NEWTON_LAGRANGE import Lagrange_cr
import numpy as np

def FibboEval(n,x,mod):
  I = np.array([1,x,0],dtype=np.int64)
  A = np.array([[1,0,0],[x,x,x*x],[0,1,0]],dtype=np.int64)
  res = matrix_mod_exp(n-1,A,I,mod)
  return res[1]

m1 = 1492992 #2^11*3^6
m2 = 875875 #11*13*7^2, the product = 15!, the desired mod

n = 10**15

r1 , r2 = sum([FibboEval(n,x,m1) for x in xrange(1,101)]) % m1 , sum([FibboEval(n,x,m2) for x in xrange(1,101)]) % m2 

print r1,r2
print Lagrange_cr((r1,r2),(m1,m2))


