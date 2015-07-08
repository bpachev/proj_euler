import numpy as np
l = 100

e_cont = lambda n: 2*(n+1)/3 if n % 3 == 2 else 1

contf = [0 for k in xrange(l)]
contf[0] = 2
for x in xrange(1,l):
  contf[x] = e_cont(x)
  
num = 1
denom = contf[-1]

for n in range(2,l)[::-1]:
  tmp = denom
  denom = denom*contf[n-1] + num
  num = tmp
  
num = 2*denom + num
print np.sum(np.array(list(str(num))).astype(int))
print str(num) + " " + str(denom)
