import numpy as np
s = 0
for x in xrange(1,1001):
  s += x**x % 10**10
print s % 10**10