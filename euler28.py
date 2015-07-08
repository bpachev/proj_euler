import numpy as np
def num_100_distinct(mpow,num_pows,base=2):
  num = np.array([0 for k in xrange(1,num_pows+1)])
  for x in xrange(2,mpow+1):
    for i in xrange(2,num_pows+1):
      for j in xrange(1,i):
        if (i*x/j) <= mpow and i*x % j == 0:
 #         print str(base) + "^" + str(i*x) + " = " + str(base) + "^" + str(j*i*x/j)
          num[i-1]-=1
          break;
  return num
  
num = num_100_distinct(100,6)
#print str(num) + " " + str(np.sum(num))
#print str(num[:4]) + " " + str(np.sum(num[:4]))
print 99**2 - 4*49 + np.sum(num) + np.sum(num[:4])