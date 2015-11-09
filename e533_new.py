from proj_euler import primes_and_mask
from math import log
import numpy as np

n = 2*10**7
logs = np.zeros(n)
mods = np.ones(n,dtype=int)
mod = 10**9
primes = primes_and_mask(n)[0]

def carmichael(p,k):
 if p == 2:
  if k <=2:
   return 2**(k-1)
  else:
   return 2**(k-2)
 else:
  return (p-1)*p**(k-1)

for p in primes:
 lp = log(p)
 k = 1
 while True:
  d = carmichael(p,k)
  if d > n:
   break
  lg = k*lp
  for i in xrange(d,n,d):
   logs[i] += lp
   mods[i] = (mods[i]*p) % mod
  k += 1
mind = np.argmax(logs)
print mods[mind]+1
  
