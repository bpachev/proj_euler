from proj_euler import two_square_repr,primes_and_mask
from itertools import combinations

n = 150
primes = primes_and_mask(n)[0]
good_primes = []
for p in primes:
 if p%4==1:
   good_primes.append(p)

s = 0

for i in xrange(1,len(good_primes)+1):
 for c in combinations(good_primes,i):
  f = {p:1 for p in c}
  for t in two_square_repr(f):
    s += t[0]

print s


