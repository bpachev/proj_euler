import numpy as np

def solve(n):
 mod= 10**9+7
 vals = np.zeros(n)
 t0 = 0
 for i in xrange(1,n):
  t0 = (t0*t0+45) % mod
  vals[i] = t0
 
 for n_nums in xrange(1,n+1): 
