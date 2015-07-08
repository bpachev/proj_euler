import proj_euler as pe
import numpy as np
import math
cap = 10**5
sig2 = np.zeros(cap).astype(np.int64)

s = 0
for i in xrange(1,cap):
#  j = i
  sq = i*i
#  while j < cap:
 #   sig2[j] += sq
  #  j += i
  sig2[i::i] = sig2[i::i] + sq
  s2 = sig2[i]
  t = pe.isqrt(s2)
  
  if t*t == s2:
    s += i

print s
