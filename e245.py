from proj_euler import is_prime,primes_and_mask,divisors,shanks_factorize
import numpy as np
n = 10**5
pcap = int(n**.5)+1
primes,mask = primes_and_mask(pcap)


def test_cores(l):
 t = 1
 n = 1
 for p in l:
   t *= (p-1)
   n *= p
 return ((t-1) % (n - t) == 0)

def cores_backtrack(cap,pairs,l):
  s = 0
  if l[-1] not in pairs:
    return 0
  
  for p in pairs[l[-1]]:
    if cap < p:
      continue
    if test_cores(l+[p]):
      s += reduce(lambda x,y:x*y,l)*p
      print l+[p]
      print reduce(lambda x,y:x*y,l)*p
    s += cores_backtrack(cap/p,pairs,l+[p])
  return s
      

def cores_sieve(n):
 tot = np.arange(n,dtype=np.int64)
 tot[1] = 1
 s = 0
 factors = [[] for i in xrange(n)]
 for i in xrange(2,n):
  if tot[i] == i:
    for j in xrange(i,n,i):
      tot[j] = tot[j] - tot[j]/i
      factors[j].append(i)
  if i-1 > tot[i]:
    if (tot[i]-1) % (i-tot[i]) == 0:
     s += i
#     print i
     print i,factors[i],factors[i-1]
   #  print (i-1) / (i-tot[i]), factors[(i-1) / (i-tot[i])]
 return s

#search for solutions of the form m*q, q the largest prime factor, m with k prime factors.
#lowerInd is the lowest prime index into the sieved array of primes.
#The last prime in the recursion.
def m_search(n,k,m=1,phi=1,lowerInd=0):
 global primes,mask,pcap
 s = 0
 if k == 0:
   f = shanks_factorize(m*phi-phi+m,primes[:15])
   for d in divisors([[bas,f[bas]] for bas in f]):
     q,r = divmod(F-phi,m-phi)
     if r == 0 and q > primes[lowerInd] and q*m <= n and is_prime(q,pcap-1,mask):
       s += q*m
       print q*m
 
 for i,p in enumerate(primes[lowerInd+1:],lowerInd+1):
   if 
  
 return s   


def find_pairs(n):
  global primes,mask
  s = 0
  pairs = {}
  for p in primes[1:]:
   num = p**2-p+1
   f = shanks_factorize(num,primes[:15])
   for k in divisors([[bas,f[bas]] for bas in f] ):
    q = num/k - p + 1
    if q > 0 and q > p and q*p <= n and is_prime(q,pcap-1,mask):
      s += p*q
#      print p,q
      if p not in pairs:
       pairs[p] = [q]
      else:
       pairs[p].append(q)
  print "Sum over semi-primes %d" % s  
  #now do backtracking pair-combos
  for p1 in pairs:
   for p2 in pairs[p1]:
    s += cores_backtrack(n/p1/p2,pairs,[p1,p2])
  return s

print find_pairs(n)
#print cores_sieve(n)


