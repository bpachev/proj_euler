import numpy as np

OP = lambda x : (-(x)**11 - 1) / (-x-1)
v =  OP(np.arange(1,13))
s = 0
for i in xrange(0,10):
  t = np.polyfit(np.arange(1,i+2),v[:i+1],i)
  s += np.polyval(t,i+2)
print s
