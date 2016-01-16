from proj_euler import primes_and_mask,isqrt,MillerRabin
from bisect import bisect_left
import sys

sys.setrecursionlimit(10**6)


primes = primes_and_mask(10**6)[0]

f = [0,1]
for i in xrange(43):
 f.append(f[-1]+f[-2])

def pi(n):
  pos = bisect_left(primes,n)
  return pos+1 if primes[pos] == n else pos

cache = {}
def phi(x, a):
  if (x, a) in cache:
    return cache[(x, a)]
  if a == 1:
    return (x + 1) // 2
  t = (x+1) // 2
  for i in xrange(1,a):
   t -= phi(x // primes[i], i)
#  t = phi(x, a-1) - phi(x // primes[a-1], a-1)
  cache[(x, a)] = t
  return t
def fpi(n):
 if n <= len(primes):
  return pi(n)
 a = pi(isqrt(n))
 return phi(n,a) + a - 1


def S(n):
 if n < 4:
  return fpi(n)
 res = 2*fpi(n) + n/2 -2
 if MillerRabin(n) or MillerRabin(n-1):
  res -= 1
 print n

 if n < 6:
  return res
 
 c = n/2
 res += (c-2)*(n+1) - (c*(c+1) - 6)
 return res
#print S(1000),S(100),S(10),S(7)
print sum([S(n) for n in f[3:]]) 

