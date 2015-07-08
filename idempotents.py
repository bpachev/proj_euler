import numpy as np
from proj_euler import egcd

cap = 10**7
mask = np.ones(cap+1).astype(int)

s = 0
for i in xrange(2,cap+1):
 s += mask[i]
 for j in xrange(2,min(i,cap/i+1)):
   d, x, y = egcd(i,j)
   if not d == 1:
     continue
   t = mask[i*j]
   i1 = (x % j) * i
   i2 = (y%i)*j
   if i2 > t:
     t = i2
   if i1 > t:
     t = i1
   mask[i*j] = t

print s

