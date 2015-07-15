import numpy as np

T = np.array([[3,1],[8,3]],dtype=np.int64)

x = np.array([2,5])

n = 20
s = 0
for i in xrange(n):
 s += x[0]-1
 print x[0]-1
 x = T.dot(x)

y = np.array([4,11])
for i in xrange(n):
 s += y[0]-1
 print y[0]-1
 y = T.dot(y)

print "sum %d" %s
