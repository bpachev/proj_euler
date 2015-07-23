from bisect import bisect_right
import numpy as np
from fractions import gcd

cap = 120000
mask = np.ones(cap,dtype=int)
l = [(1,1)]
s = 0
for i in xrange(2,cap):
  #prime
  if mask[i] == 1:
    for j in xrange(i,cap,i):
      mask[j] *= i
  
  
  m = i/mask[i]
  for t in l:
    if t[0] > m:
      break
    if t[0]*mask[i-t[1]] > m:
      continue
    if gcd(i,t[1]) > 1:
      continue
    else:
#      print i,t[1],i-t[1]
      s += i
      #break

  #add to sorted list of (i, rad(i)) pairs
  te = (mask[i],i)
  pos = bisect_right(l,te)
  l.insert(pos,te)
  
print (s-2)/2

