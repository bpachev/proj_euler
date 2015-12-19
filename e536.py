from proj_euler import *
from fractions import gcd

primes,mask,pcap = None,None,None

def lcm(a,b):
 return a*b/gcd(a,b)

def carmichael_seive(n):
 primes = primes_and_mask(n)[0]
 mask = [1] * n
 for p in primes[1:]:
  for x in xrange(p,n,p):
   if not x%(p*p):
    d,e = pord(x,p)
    mask[x] = lcm(mask[x],(p-1)*(d/p))
   else:
    mask[x] = lcm(mask[x],p-1)
 return mask 

def check_r(n,m,minp,r,l):
 s = 0
 mink = (minp-r)/l
 maxk = (min(n/m,m+4)-r)/l
 #now search for primes >= minp, < n/m
 # We know primes are of the form p = k*l+r
 for k in xrange(max(0,mink),maxk+1):
  p = l*k+r   
  if mask[p] and m%p and p >=minp:
   if not (m*p+3) % (p-1): 
    s += m*p
#    print m*p
 
 return s 

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
 if nump >= 2:
  pi = bisect_right(primes,n/m)
  minp = primes[lowerInd+1] 
  if (min(n/m,m+4)-minp)/l < (pi-lowerInd):
   r = solve_lin_mod_eq(m,l-3,l)
   if r is None:
    return s
   if type(r) is list:
    for rem in r:
     s += check_r(n,m,minp,rem,l)
   else:
    s += check_r(n,m,minp,r,l)
  
  else:
   for p in primes[lowerInd+1:pi+1]:
    if not (m*p+3) % l and not (m+3)%(p-1):
      s += m*p
   
 bound = int((n/m)**(.5))
 i=lowerInd+1
 while primes[i]<=bound:
    s += m_search(n,nump+1,m*primes[i],lcm(l,primes[i]-1),i)
    i+=1
  
 return s   

def test(n):
 s = 0
 for i,x in enumerate(carmichael_seive(n)):
  if x > 1:
   if not (i+3) % x and i%9:
    print i
    s += i
 print s+3

def solve(n):
 global primes,mask,pcap
 pcap = int(n**.5)
 primes,mask = primes_and_mask(pcap)
 s = 32
 bnd = int(n**(1./3)+1)
 i=1
 while primes[i] < bnd:
  i2=i+1
  while primes[i2]*primes[i2] < n/primes[i]:
    s += m_search(n,2,m=primes[i]*primes[i2],l=lcm(primes[i]-1,primes[i2]-1),lowerInd=i2)
    i2+=1
  i+=1
 print "Total Sum: %d " % s
solve(10**12)
#test(10**6) 
