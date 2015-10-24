import numpy as np

def find_min_triangle1(arr):
 MIN = np.inf
 n = arr.shape[0]
 for row in xrange(n):
  for col in xrange(row+1):
   s = arr[row][col]
   tmin = s   
   for nrow in xrange(row+1,n):
    s += np.sum(arr[nrow][col:nrow-row+1])
    if s < tmin:
     tmin = s
   if tmin < MIN:
    MIN = tmin
 return MIN

def find_min_triangle2(arr):
 MIN = np.sum(np.sum(arr))
 n = arr.shape[0]
 csums = np.cumsum(arr,axis=1)
 for starti in xrange(n):
  if not starti:
   for endi in xrange(starti,n):
    s = csums[n-1][endi]
    for j in xrange(1,endi-starti+1):
     s += csums[n-1-j][endi-j]
     if s > 0:
      s = 0
    if s < MIN:
      MIN = s
      print "NEW MIN: %d" % s
   
  else:
   dec = csums[n-1][starti-1]  
   for endi in xrange(starti,n):
    s = csums[n-1][endi] - dec
    for j in xrange(1,endi-starti+1):
     s += csums[n-1-j][endi-j] - csums[n-1-j][starti-1]
     if s > 0:
      s = 0
    if s < MIN:
      MIN = s
      print "NEW MIN: %d" % s
 return MIN


def solve(n=1000):
 arr = np.zeros((n,n),dtype=int)
 mod = 2**20
 d = 2**19
 t = 0
 for row in xrange(n):
  for col in xrange(row+1):
    t = (615949*t + 797807) % mod
    arr[row][col] = t-d
 return find_min_triangle2(arr)

print solve(1000)

   	
