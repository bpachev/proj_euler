import numpy as np
import math

s = 0
for n in xrange(2,101):
  R = int(n**.5)
  if R*R == n:
    continue
  digits = np.zeros(100)
  p10 = n
  curr_num = 0
  for j in xrange(100):
    i = -1
    while curr_num**2 < p10:
      curr_num += 1
      i += 1
    curr_num  = curr_num - 1
    curr_num  = curr_num*10
    p10 *= 100
    digits[j] = i 
  s += np.sum(digits)
print s
