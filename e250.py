import numpy as np

div = 250
old = np.zeros(div).astype(np.int64)
old[0] = 1
new = np.zeros(div).astype(np.int64)
mod = 10**16

n = 250250

for i in xrange(1,n+1):
  e = pow(i%div,i,div)
  for j in xrange(div):
    new[j] = (old[j] + old[(j-e)%div]) % mod
  if i == n:
    print new[0]-1
  temp = old
  old = new
  new = temp

print old[0]-1

