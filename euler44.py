import numpy as np

def is_pentagonal(x):
  res = (1.+(1.+24*x)**0.5)/6
  return res == int(res)
cap = 10000
pnums = []
for i in xrange(4, 10000):
  pnums.append(i*(3*i-1)/2)
  for j in xrange(4 , i):
    if is_pentagonal(pnums[i-4] - pnums[j-4]) and is_pentagonal(pnums[i-4] + pnums[j-4]):
      print str(i) + " " + str(j)
      print pnums[i-4] - pnums[j-4]
print is_pentagonal(5)

