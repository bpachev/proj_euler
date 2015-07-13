import numpy as np

n = 10**3
m = 10**10
cache  = {}

for a in xrange(3,n):
  for b in xrange(2-a%2,a,2):
    as1,bs1 = a**2,b**2
    t1,t2 = (as1+bs1 )/2, (as1-bs1 )/2 
    if t1 not in cache:
      cache[t1] = [t2]
    else:
      cache[t1].append(t2)
#print cache
for x in cache:
  if len(cache[x]) == 1:
    continue
  for y in cache[x]:
    if not y in cache:
      continue
    for z in cache[x]:
      if z in cache[y]:
        print x,y,z
        print x+y+z
