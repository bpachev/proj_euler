import proj_euler as pe
from math import log
cap = 7376507
#cap = 7
mod = 500500507
primes = pe.primes_and_mask(cap)[0]

divs = 500500 #2**4

rmask = []

for p in primes:
  t = p
  while t <= cap:
    rmask.append(t)
    t = t*t

s = 1
res = sorted(rmask)
for r in res[:divs]:
  s = (r*s) % mod
print s
