import proj_euler as pe
import math
s = 0
cap = 10**6

primes = pe.primes_and_mask(cap)[0]

for p in primes:
  a = (p*p+13)/8 + 1
  b = int(math.ceil((p*p+13-2)/6.)) - 1
  if a <= b:
    s += b - a + 1

print 2*s #account for reflection
