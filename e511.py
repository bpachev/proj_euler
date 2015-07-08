import proj_euler as pe
import numpy as np

#n = 1111
#k = 24
mod = 10**9
#divs = [1,11,101,1111]

#n = 4
#k = 11
#divs = [1,2,4]

n = 1234567898765
k = 4321
divs = [1  ,  5  ,  41  ,  205  ,  25343  ,  126715  ,  237631  ,  1039063  ,  1188155  ,  5195315  ,  9742871  ,  48714355  ,  6022282433  ,  30111412165  ,  246913579753  ,  1234567898765 ]


init = np.array([0 for j in xrange(k)])
init[n%k] = 1 #initially one possibility in state n mod k
T = np.zeros((k,k)).astype(np.int64)

for i in xrange(k):
  for d in divs:
    T[i][(i-d)%k] = 1

#for d in divs:
 # print "d: " + str(d) + " d mod k " + str(d%k)

#print T
#print pe.matrix_mod_exp(n,T,init,mod)[0]
print pe.circulant_mod_exp(n,T,init,mod)[0]    


