from scipy.misc import comb
from decimal import Decimal,getcontext

k = 32
s = 1
for i in xrange(1,k+1):
  if i %2:
    s += comb(k,i,True)/(2.**i-1)
  else:
    s -= comb(k,i,True)/(2.**i-1)

getcontext().prec = 15
print Decimal(s)
