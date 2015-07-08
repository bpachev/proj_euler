import numpy as np
import proj_euler as pe

maxSum = 1548136
cap = 5000
mod = 10**16
primes,mask = pe.primes_and_mask(maxSum)

old = np.zeros(maxSum+1).astype(np.int64)
new = np.zeros(maxSum+1).astype(np.int64)

old[0] = 1
s = 0
for p in primes:
  if p > cap:
    break
  s += p
  for j in xrange(p):
    new[j] = old[j]
  for j in xrange(p,s+1):
    new[j] = (old[j] + old[j-p]) % mod
  
  temp = old
  old = new
  new = temp
res = 0

for p in primes:
  res = (res + old[p]) % mod

print res
