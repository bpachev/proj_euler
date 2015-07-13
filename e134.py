from proj_euler import primes_and_mask
from math import log,floor
cap = 10**6+4
p1_cap = 10**6
primes = primes_and_mask(cap)[0]

l = log(10)
pow10 = [10**i for i in xrange(7)]
s = 0

for i,p in enumerate(primes):
  if p > p1_cap:
    break
  if p < 5:
    continue
  
  digits = int(floor(log(p)/l)) + 1
  p10 = pow10[digits]
  p2 = primes[i+1]
  n = p + p10 * (((p2-p) * pow(p10,p2-2,p2)) % p2)
#  print n,p,p2,p10
  s += n
print s
