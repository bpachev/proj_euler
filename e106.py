from scipy.misc import comb
from itertools import combinations

cap = 12
#num subset pairs of equal size
numPairs = 0
dec = 0
for i in xrange(2,cap/2+1):
  numPairs += comb(cap,i,True)*comb(cap-i,i,True)
  for c in combinations(range(cap),i):
    allowable = []
    for j in xrange(c[0],cap):
      if j not in c:
        allowable.append(j)
    for upper in combinations(allowable,i):
      flag = 1
      for k in xrange(i):
        if c[k] >= upper[k]:
          flag = 0
          break
      if flag:
#        print c
 #       print upper
        numPairs -= 2
      
      
print numPairs/2

