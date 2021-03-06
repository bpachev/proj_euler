import numpy as np
from scipy.misc import comb
from proj_euler import safe_matrix_mul
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
 cache.append(accum)
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
 coeffs.append((n,2))
 for curr,next in izip(coeffs[:-1],coeffs[1:]):
  init[-1] = init[-1] + curr[1]
  #shifting factor 
  d = next[0]-curr[0]
  j = 0
  while d:
   if d %2:
     init = np.remainder(cache[j].dot(init),mod)
   j += 1
   d /= 2
 return init[-1]


x=0
mod = 10**9+7
for j in xrange(10,16):
 x = (x+s(10**j,j,j)) % mod
print x  
  
