import proj_euler as pe
import math

cap = 10000000
#cap = 10**7
primes = pe.primes_and_mask(cap)[0]

def M(p,q,N):
 m = 0
 a1 = p
 while a1*q <= N:
  t = a1 * (q ** (int(math.floor(math.log(N/float(a1))/math.log(q)))))
  if t > m:
    m = t
  a1 *= p
 return m

s = 0

for i,p1 in enumerate(primes):
  for j, p2 in enumerate(primes):
    if p1 == p2:
      continue
    if p2 > cap/p1:
      break
    s += M(p1,p2,cap)

print s/2

