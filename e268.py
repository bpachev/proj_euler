import proj_euler as pe
from itertools import combinations

primes = pe.primes_and_mask(100)[0]

def p100_free(n,primes):
  if n <=1:
    return n
  s = n
  for i,p in enumerate(primes):
    if p > n:
      break
    s -= p100_free(n/p,primes[i+1:])
  return s

cap = 10**16
t = cap

t -= p100_free(cap,primes)
for i in xrange(1,4):
 for c in combinations(primes,i):
  tprimes=[]
  for p in primes:
   if p not in c:
     tprimes.append(p)
  t -= p100_free(cap/reduce(lambda x,y:x*y,c),tprimes)
print t
