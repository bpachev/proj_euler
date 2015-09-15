from proj_euler import primes_and_mask
from math import log

primes = primes_and_mask(10**4)[0]

def is_counterexample(p,q):
  if p == q:
    return False	
  mod = (p-1)*(pow(q,p)-1) / (q-1)
  res = pow(p,q,mod)-1
  if not res:
    return True
  else:
   return False

exp_bound = 10000
for i,p in enumerate(primes):
 if p < exp_bound:
   if i%100==0:
     print "On %d" % i
   for q in primes:
     if is_counterexample(p,q):
       print "Counterexample found at %d,%d" % (p,q)
 else:
  break
