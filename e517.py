from scipy.misc import comb
import math

def MillerRabin(n):
  '''
  For n < 341,550,071,728,321, this is a deterministic primality test
  '''
  if n == 1:
    return 0

  primes =  [2, 3, 5, 7, 11, 13, 17]
  for p in primes:
    if n == p:
      return 1
    if n % p == 0:
      return 0

  s = 0
  d = n-1
  while d % 2 == 0:
    s += 1
    d /= 2

  for p in primes:
      x = pow(p,d,n)
      if x == 1 or x == n-1:
        continue
      for i in xrange(s-1):
        x = x*x % n
        if x == n-1:
          break
        if x == 1:
          return 0
      if not x*x % n == 1:
        return 0

  return 1


mod =1000000007
mcache = {-1:0,0:1}
icache = {-1:0,0:1}

c1 = 1
c2 = 1
for i in xrange(1,10**7 + 10**4):
  c1 = (c1*i) % mod
  mcache[i] = c1
  icache[i] = pow(c1,mod-2,mod)
    
def G(n):
 global mod
 global mcache
 global icache
 r = 0
 sq = math.sqrt(n)
 #count terminal states
 for dec1 in xrange(0,int(math.floor(sq))+ 1):
  imax = int(math.floor(n - sq * dec1))
  imin = int(math.ceil(n - sq * (dec1 + 1)))
  imin = max(imin,0)
  r = (r + mcache[imax + dec1]*icache[imax]*icache[dec1] - mcache[imin + dec1-1]*icache[imin-1]*icache[dec1]) % mod
  if r < 0:
    r += mod
  r = (r + mcache[imin + dec1-1]*icache[imin-1]*icache[dec1]) % mod
 return r

print G(90)
  
s = 0
for n in xrange(10**7,10**7 + 10**4):
  if not MillerRabin(n):
    continue
  s = (s + G(n)) % mod
print s

#dec1 is the number of times sqrt(n) is subtracted from n
#dec2 is the number of times 1 is subtracted from n
def G_old(dec1,dec2):
  global sq
  global n
  global cache
  global mcache #factorials modulo modulus
  global icache #inverse factorials
  global mod  
  if dec1 in cache:
    if dec2 in cache[dec1]:
      return cache[dec1][dec2]
  else:
    cache[dec1] = {}
  
  #I really hope I don't run into significant floating point error
  max_depth = int(math.floor((n - dec1*sq - dec2) / sq))
  if max_depth == 0:
    cache[dec1][dec2] = 1
    return 1
  elif max_depth == 1:
    cache[dec1][dec2] = int(math.ceil((n - (dec1 + 1)*sq - dec2)))
    return cache[dec1][dec2]
  else:
    res = 0
    for i in xrange(max_depth+1):
      res = (res + mcache[max_depth]*icache[i]*icache[max_depth-i]*G(dec1 + i, dec2 + max_depth - i)) % mod
    cache[dec1][dec2] = res
    return res
    
       
