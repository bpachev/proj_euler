from CR_NEWTON_LAGRANGE import Lagrange_cr as chin
import proj_euler as pe

cap = 5000
lower = 1000
N = 10**18
K = 10**9

primes = pe.primes_and_mask(cap)[0][168:]
np=len(primes)
print np
s = 0

def binom(n,k,p):
  if k > n:
    return 0
  if not k:
    return 1
   
  if k < p:
    r = 1
    
    for i in xrange(k):
      r = ( r * pow(i+1,p-2,p) * (n-i))%p
    return r
  
  return (binom(n/p,k/p,p) * binom(n%p,k%p,p))%p

pc = {p:binom(N,K,p) for p in primes}

for i,p in enumerate(primes):
  for j in xrange(i+1,np):
    q = primes[j]
    r1 = chin((pc[p],pc[q]),(p,q))
    for r in primes[j+1:]:
      r2 = chin((r1,pc[r]),(p*q,r))
      s += r2

print s
  
