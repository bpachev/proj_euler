import numpy as np

cap = 100000

mask = np.ones(cap+1).astype(int)
l = [(1,1)]

for i in xrange(2,cap+1):
 if mask[i] == 1:
   l.append((i,i))
   for j in xrange(2*i,cap+1,i):
     mask[j] *= i
 else:
   l.append((mask[i],i))

k = 10000
print sorted(l)[k-1][1]
