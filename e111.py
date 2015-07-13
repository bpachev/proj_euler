from proj_euler import MillerRabin as MR
from itertools import combinations as C
pow10 = [10**i for i in xrange(15)]

dig=10
s = 0
for d in [1,3,4,5,6,7,9]:
  num = d*((pow10[dig]-1)/9)
  for pos in xrange(10):
    for rep in xrange(10):
      if rep == d:
        continue
      t = num + (rep-d)*pow10[pos]
      if MR(t):
        print t
        s += t

for d in [0,2,8]:
  num = d*((pow10[dig]-1)/9)
  for pos in C(range(10),2):
    for r0 in xrange(10):
      if r0 == d:
        continue
      for r1 in xrange(10):
        if r1 == d:
          continue
        t = num + (r0-d) *pow10[pos[0]] + (r1-d) * pow10[pos[1]]
        if MR(t) and t > 10**9:
          print t
          s += t

print s
