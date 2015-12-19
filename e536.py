from proj_euler import *
from fractions import gcd

primes,mask,pcap = None,None,None

def lcm(a,b):
 return a*b/gcd(a,b)

def carmichael_seive(n):
 primes = primes_and_mask(n)[0]
 print primes
 mask = [1] * n
 for p in primes[1:]:
  for x in xrange(p,n,p):
   if not x%(p*p):
    d,e = pord(x,p)
    mask[x] = lcm(mask[x],(p-1)*(d/p))
   else:
    mask[x] = lcm(mask[x],p-1)
 return mask 

def m_search(n,nump,m=1,l=1,lowerInd=0):
 '''
 INPUTS:
  n -- the maximum allowable number
  m -- the current 
  nump -- the number of primes allowed in the composite
  l -- L(m)
 DESCRIPTION: 
  Finds all odd squarefree composites m for which L(m) | m+3
  L is in this case the carmichael function
 RETURNS:
  s, the sum of all m satisfying L(m) | m+3, m < n 
 '''
 global primes,mask,pcap
 if nump < 0 or lowerInd>=len(primes)-1:
  return 0
 
 s = 0

 r = solve_lin_mod_eq(m,l-3,l)
 if r is None:
  return s
 minp = primes[lowerInd+1]
 mink = (minp-r)/l
 maxk = (n/m-r)/l
 #now search for primes >= minp, < n/m
 # We know primes are of the form p = k*l+r
 for k in xrange(max(0,mink),maxk):
  p = l*k+r   
  if is_prime(p,pcap,mask) and m%p:
   if not (m*p+3) % lcm(l,p-1): 
    s += m*p
    print m*p
 
 bound = int((n/m)**(1./(nump+1)))
 for i,p in enumerate(primes[lowerInd+1:],lowerInd+1):
   if p > bound:
    break
   else:
    s += m_search(n,nump+1,m*p,lcm(l,p-1),i)
  
 return s   

def test(n):
 for i,x in enumerate(carmichael_seive(n)):
  if x > 1:
   if not (i+3) % x:
    print i,x

def solve(n):
 global primes,mask,pcap
 pcap = int(n**.5)
 primes,mask = primes_and_mask(pcap)
 s = 3 + m_search(n,0) #don't do even numbers, count 1 & 2
 print "Total Sum: %d " % s
solve(1000)
test(1000) 
