from scipy.misc import comb
from math import factorial, log
import numpy as np

n = 10**6
k = 2000

k2 = 3


def P(k,n):
 global k2,cache
 if not k:
  return 1.
 if not n:
  return 1.
 if cache[k-1,n-1] >= 0:
   return cache[k-1,n-1]
 s = 0.
 for i in xrange(min(k2,k+1)):
   s += comb(k,i,True)*(1./n)**i*((n-1.)/n)**(k-i) * P(k-i,n-1)
 cache[k-1,n-1] = s
 return s
 
c = {}
def PN(n,k):
 global k2, c
 if k < k2:
   return 1.
 if n == 1:
   return 0. #if k<k2, already handled, so k>=k2
 if (n,k) in c:
   return c[(n,k)]
 s = 0.
 coeff = (float((n-n/2))/n)**k
 m = (n/2) / float(n-(n/2))
 for i in xrange(k+1):
   s += coeff*PN(n/2,i)*PN(n-n/2,k-i)
   coeff *= m
   coeff *= float((k-i))/(i+1) 
 c[(n,k)] = s
 return s

def N(n,k):
  s = 0
  c = 20
  facts = np.zeros(max(n+1,c)).astype(np.float64)
  for i in xrange(1,c):
    facts[i] = np.log(i) + facts[i-1]
    if not facts[i] == log(factorial(i)):
      print "Does not match for n = " + str(i)
  for i in xrange(c,n+1):
    x = i+1
    facts[i] = (x-1./2)*log(x)-x+(1./2)*log(2*np.pi)+1./(12.*x)
  print facts
  print np.log(2)
  for i in xrange(k%2,k+1,2):
    t = facts[k] + facts[n] - facts[i]  - facts[(k-i)/2] - facts[n-i-((k-i)/2)] - ((k-i)/2)*log(2) -k*log(n)
    s += np.exp(t)
#    s += factorial(k)*comb(n,i,True)*comb(n-i,(k-i)/2,True)/2.**((k-i)/2)
  
  return 1-s
print N(70,40)
print 1-PN(70,40)
