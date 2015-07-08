import sys
import numpy as np
from itertools import combinations

if len(sys.argv) <= 1:
  filename = "p345_matrix.txt"
else:
  filename  = sys.argv[1]

fp = open(filename,"r")
m = np.loadtxt(fp,delimiter=" ",dtype=int)
fp.close()

n = m.shape[0]

cache = {}

#deprecated
def matrixSum(m,excludedRows = (),excludedCols=()):
  global n,cache
#  print excludedRows,excludedCols
  if (excludedRows,excludedCols) in cache:
    return cache[(excludedRows,excludedCols)]
  
  if len(excludedCols) == n:
    return 0
  mx = 0
  for i in xrange(n):
    if i in excludedRows:
      continue
    for j in xrange(n):
      if j in excludedCols:
        continue
      t = m[i,j] + matrixSum(m,tuple(sorted(list(excludedRows)+[i])),tuple(sorted(list(excludedCols)+[j])))
      if t > mx:
        mx = t
  if len(excludedCols) > 7:
    cache[(excludedRows,excludedCols)] = mx
  return mx

#fast one
def newMatrixSum(mat,incRows,incCols):
  global cache
  #print "called with args " +str(incRows) + " " + str(incCols)
  if (incRows, incCols) in cache:
    return cache[(incRows, incCols)]
  
  l = len(incRows)
  if len(incRows) == 1:
    return mat[incRows[0],incCols[0]]
    
  m = 0
  for firstCols in combinations(list(incCols),l/2):
     lCols = tuple([c for c in incCols if c not in firstCols])
     t1 = newMatrixSum(mat,incRows[:l/2],firstCols)
     t2 = newMatrixSum(mat,incRows[l/2:],lCols)     
     if t1+t2 > m:
       m = t1+t2
  cache[(incRows,incCols)] = m
  return m
  
print newMatrixSum(m,tuple(xrange(n)),tuple(xrange(n)))
  
  
