import numpy as np
import numpy.linalg as la
from scipy.misc import comb

d = 32
T = np.zeros((d,d)).astype(np.float64)
x = np.ones(d).astype(np.float64)

for i in xrange(d):
  for j in xrange(i+1):
   T[i,j] = comb(i+1,i-j)
  T[i,:] = T[i,:] / (2.**(i+1))

np.set_printoptions(precision=15)
print la.solve(np.identity(d)-T,x)

