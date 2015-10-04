import numpy as np
from scipy.misc import comb
from proj_euler import safe_matrix_vector_dot,safe_matrix_mul,safe_matrix_exp,matrix_mod_exp
from itertools import izip

def s(n,k,b,mod = 10**9+7):
 cache = []
 T = np.zeros((k+1,k+1),dtype=np.int64)
 T[:-1,1:] = np.eye(k,dtype=np.int64)
 for i in xrange(1,k+1+1):
   T[-1,-i] = -(-1)**i * comb(k+1,i,True)
 T = np.remainder(T,mod)
 accum = np.copy(T)
 tn = n 
 while tn:
  cache.append(accum)
  accum = safe_matrix_mul(accum,accum,mod)
  tn/=2
 init = np.zeros(k+1,dtype = np.int64)
 coeffs = [(0,1)]
 for i in xrange(1,k+1):
   num = b**i+1
   temp = []
   for t in coeffs:
    temp.append(t)
    if t[0] + num <= n:
     temp.append((t[0]+num,-t[1]))
   coeffs = temp 
 coeffs = sorted(coeffs)
 ns = set([t[0] for t in coeffs])
 if len(ns) < len(coeffs):
  print "discrepancy on %d" % k
 return 0
 coeffs.append((n,0))
 for curr,next in izip(coeffs[:-1],coeffs[1:]):
  init[-1] += curr[1]
  #shifting factor 
  d = next[0]-curr[0]
  j = 0
  while d:
   if d %2:
    init = safe_matrix_vector_dot(cache[j],init,mod)
   j += 1
   d /= 2
 return init[-1]


#print s(1000,10,5)
print sum([s(10**k,k,k) for k in xrange(10,16)]) % (10**9+7)
  
  
