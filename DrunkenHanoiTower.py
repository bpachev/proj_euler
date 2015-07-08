import numpy as np
def leg(start,stop,startInd,stopInd,n):
  if startInd > stopInd:
    return (n-stop)**2 - (n-start)**2
  else:
    return (stop-1)**2 - (start-1)**2


p = {(0,1):0,(0,2):1,(1,2):0,(1,0):0,(2,0):0,(2,1):0}
n = 10000
mod = 10**9
K , t  = 10,(3,6,9)
s = 0
for i in xrange(n):
#  print p
#  print K
#  print t
  for l in p:
    if l == (1,0):
     s = (s + (p[l]+1)*leg(t[l[0]],t[l[1]],l[0],l[1],K)) % mod    
    else:
     s = (s + p[l]*leg(t[l[0]],t[l[1]],l[0],l[1],K) ) % mod

  c = dict()
  c[(0,1)] = (p[(1,0)] + p[(0,2)]) % mod
  c[(0,2)] = (p[(1,2)] + p[(0,1)] + 1) % mod
  c[(1,2)] = (p[(2,1)] + p[(0,2)]) % mod
  c[(1,0)] = (p[(0,1)] + p[(2,0)] + 1 ) % mod
  c[(2,0)] = (p[(2,1)] + p[(1,0)] ) % mod
  c[(2,1)] = (p[(1,2)] + p[(2,0)] + 1 ) % mod
      
  p = c
  K, t = (10*K)%mod , ((3*t[0])%mod,(6*t[1])%mod,(9*t[2])%mod)

print s
