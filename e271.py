from proj_euler import primes_and_mask
from CR_NEWTON_LAGRANGE import Lagrange_cr
from itertools import product

primes = primes_and_mask(100)[0]

a = primes[:14] #interested in product of first 14 primes

r = [[] for i in xrange(14)]
for j,p in enumerate(a):
  for i in xrange(1,int(p)):
    if (i**3-1)%p == 0:
      r[j].append(i)

s = 0
m = tuple(a)
print m
for res in product(*r):
 t = Lagrange_cr(res,m)
 if t > 1:
   s += t
print s
