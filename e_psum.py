import numpy as np
#print 2**1000

f = open("2_exp_1000.txt","r")
for line in f:
  d = np.array(list(line.strip())).astype(int)

print np.sum(d)
