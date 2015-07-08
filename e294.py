import proj_euler as pe
import numpy as np

n = 11**12
k = 23
#mod = 10**9

T = np.zeros(((k+1)*k,(k+1)*k)).astype(np.int64)
init = np.zeros((k+1)*k).astype(np.int64)
init[0] = 1

for d in xrange(10):
  for i in xrange((k+1)*k):
    s = i/k #sum
    m = i%k #mod-state
    m_new = ((10*m) + d) % k
    if s + d <= k:
      T[k*(s+d) + m_new,i] = 1

r1 = pe.matrix_mod_exp(n,T,init,2**9)[k*k]
r2 = pe.matrix_mod_exp(n,T,init,5**9)[k*k]

print "mod 2^9: " + str(r1) + " mod 5^9 " + str(r2) 




















