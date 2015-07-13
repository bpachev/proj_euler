import numpy as np
from proj_euler import gcd

cap = 3*10**4

nvals = 25

divDict = {i:[1] for i in xrange(1,cap)}


pmask = np.ones(cap+1,dtype = int)
tmask = np.ones(cap,dtype=int)
s = 0
count = 0

for i in xrange(2, cap):
  if pmask[i]:
    for j in xrange(i,cap,i):
      pmask[j] = 0
      tmask[j] *= i-1
      nl = []
      for d in divDict[j]:
        nl.append(d * i)
      divDict[j] = divDict[j] + nl
    pp = i*i
    while pp < cap:
      for j in xrange(pp,cap,pp):
        tmask[j] *= i
        nl = []
        for d in divDict[j]:
          if not d % (pp/i):
           nl.append(d * i)
        divDict[j] = divDict[j] + nl
      pp *= i
  elif not i % 3:
    continue
  else:
    for div in sorted(divDict[tmask[i]]):
      if pow(10,div,i) == 1:
        if (i-1) % div == 0:
          count += 1
          s += i
          print i
          break
        else:
          break
    if count == nvals:
      print "Sum %d" % s
      break

