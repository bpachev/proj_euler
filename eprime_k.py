import proj_euler as pe
import numpy as np
cap = 10**6
mask = np.ones(cap)

def f(p):
 return (pow((p-2),p-2,p) + pow((p-3)*(p-2),p-2,p) + pow((p-2)*(p-3)*(p-4),p-2,p)) % p
s = 0
for i in xrange(2,cap):
  if mask[i]:
    for j in xrange(i*i,cap,i):
      mask[j] = 0
    p = i
    if i >= 5:
      s += f(p)
print s
