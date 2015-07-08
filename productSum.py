import numpy as np

cap = 12000
mask = np.zeros(cap+1)

#N is a bound on the product, k is a uniform bound on each member
def genBoundedTuples(N, k,currProd,currSum,numElements):
  global mask
  global cap
  if currProd > N:
    return
  m = currProd - currSum + numElements
  if m <= cap and m >= numElements and numElements >= 2:
    if not mask[m]:
      mask[m] = currProd
    elif currProd < mask[m]:
      mask[m] = currProd
  for i in xrange(2,min(N/currProd,k)+1):
    genBoundedTuples(N,i,currProd*i,currSum +i,numElements+1)
  return

genBoundedTuples(2*cap,2*cap/2,1,0,0)

maxes = set()
s = 0
for i in xrange(2,cap+1):
  if mask[i] in maxes:
    continue
  s += mask[i]
  maxes.add(mask[i])
print s
