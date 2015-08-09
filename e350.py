from proj_euler import generic_sieve_fill
from math import log

g = 10**6
l = 10**12
mod = 101**4
n = 10**18

cache = [1]
for i in xrange(1,int(log(g)/log(2))+1):
  t = pow(i+1,n,mod)
  for j in xrange(i):
    t = (t - (i+1-j)*cache[j]) % mod
  cache.append(t)

f = lambda prod,i,e: (prod * cache[e]) % mod

mask = generic_sieve_fill(g+1,f)
s = 0
for i in xrange(1,g+1):
  s = (s + (((l/i) -g+1)%mod) * (mask[i]%mod)) % mod
print s

