import numpy as np

n = 2000
T = np.zeros((n,n),dtype=float)

def max_sum(a):
  '''
  a -- a 1-d numpy array
  RETURNS:
  m -- the maximum sum of consecutive elements of the array
  '''
  l = a.shape[0] #length of array
  
  if l == 1:
    return a[0]
  m1,m2 = np.amax(np.cumsum(a[l/2-1::-1])), np.amax(np.cumsum(a[l/2:]))
  m = max(m1+m2,max_sum(a[:l/2]),max_sum(a[l/2:]))
  return m
def max_table_sum(a):
  '''
  a -- a 2-d square numpy array
  RETURNS:
  m -- the maximum among sums of consecutive elements
  rows, columns, diagonals and off-diagonals are counted
  '''
  m = -np.inf
  n = a.shape[0]
  #rows and cols
  for i in xrange(n):
    t1 = max_sum(a[:,i])
#    print a[:,i]
#    print t

    if t1 > m:
     m = t1
     print t1
    t2 = max_sum(a[i,:])
#    print a[i,:]
#    print t
    if t2 > m:
     m = t2
     print t2
  print "max after considering rows/cols %d" % m
  x = np.fliplr(a)
  for i in xrange(-n+1,n):
    t3 = max_sum(a.diagonal(i))
#    print a.diagonal(i)
#    print t
    if t3 > m:
      m = t3
      print t3
    
    t4 = max_sum(x.diagonal(i))
#    print t
#    print x.diagonal(i)
    if t4 > m:
      m = t4
      print t4
  print "Final Max % d" % m
  return m

max_sum(np.array([1,2,-3,4,-1,3,-2,3,5]))
norma = lambda x: (x % 1000000) - 500000
POS = lambda x: divmod(x,n)

#populate array
for i in xrange(1,56):
 T[0,i-1] = norma(100003 - 200003*i + 300007*i**3)
for i in xrange(55,n*n):
 T[POS(i)] = norma(T[POS(i-24)] + T[POS(i-55)]+1000000)   
max_table_sum(T)
