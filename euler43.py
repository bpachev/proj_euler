import itertools
import numpy as np

d = range(0,10)
primes = np.array([2,3,5,7,11,13,17])
tens = np.array([10**(10-k) for k in xrange(1,11)])
s = 0
def is_good(p):
  global primes
  for x in xrange(7):
    if not (p[x+1]*100 + p[x+2]*10 + p[x+3]) % primes[x] == 0:
      return False 
  return True

for p in itertools.permutations(d):
  if p[0]:
    if is_good(p):
      s += np.inner(np.array(p),tens)

print s
