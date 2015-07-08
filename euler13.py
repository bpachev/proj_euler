import numpy as np

def sum_nums(filename):
  nums = np.zeros((100,50))
  f = open(filename,"r")
  i = 0
  for line in f:
    nums[i,:] = np.array(list(line.strip())).astype(np.uint8)
    i += 1
    
  n = nums.sum(axis=0)
  for x in xrange(n.size-1,0,-1):
    n[x-1] += n[x] // 10
    n[x] = n[x] % 10
  x = " "
  for d in n:
    x += str(int(d))
  print "Sum " + x
  
sum_nums('e13_nums.txt')