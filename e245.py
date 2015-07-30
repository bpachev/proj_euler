from proj_euler import is_prime,primes_and_mask
import numpy as np
n = 10**6+7*10**5

def cores_sieve(n):
 tot = np.arange(n,dtype=np.int64)
 tot[1] = 1
 factors = [[] for i in xrange(n)]
 for i in xrange(2,n):
  if tot[i] == i:
    for j in xrange(i,n,i):
      tot[j] = tot[j] - tot[j]/i
      factors[j].append(i)
  if i-1 > tot[i]:
    if (tot[i]-1) % (i-tot[i]) == 0:
       print i,factors[i]

def find_pairs(n):
  primes,mask = primes_and_mask(int(n**.5)+1)
  for p in primes[1:]:
   for k in divisors(p**2-p-1):
     

def test_cores(l):
 t = 1
 n = 1
 for p in l:
   t *= (p-1)
   n *= (p-1)
 return ((t-1) % (n - t) == 0)
