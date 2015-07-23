import numpy as np
from proj_euler import safe_matrix_exp,matrix_mod_exp

T = np.zeros((9,9),dtype=np.int64)
T[1:,:8] = np.eye(8,dtype=np.int64)
T[0,:] = np.ones(9,dtype=np.int64)

init = np.array([2**(8-i) for i in xrange(0,9)],dtype=np.int64)
#print T
#print init
d = 9
mod = 10**d
overall = [[0,0] for i in xrange(d*9+1)] #sofdigits:[number of nums,sum of nums]
last = [[0,0] for i in xrange(d*9+1)]
overall[0][0]=1
last[0][0] = 1
curr = [[0,0] for i in xrange(d*9+1)]
for i in xrange(1,d+1):
  curr = [[0,0] for i in xrange(d*9+1)]
  #After iteration i, curr[s] should be [number of nums with digit sum =s, i digits, and sum of those nums]
  for s in xrange(9*d+1):
    if not last[s][0]:
      continue
    for j in xrange(1,10):
      curr[s+j][0] += last[s][0]
      curr[s+j][1] += 10*last[s][1]+j*last[s][0]
  for s in xrange(9*d+1):
    overall[s][0] += curr[s][0]
    overall[s][1] += curr[s][1]
#  print curr[:11]
  last = curr
S = 0
#handle 13 separately
S = overall[13][1]
for i in xrange(9,13):
  S = (S+curr[i][1]*(2**(12-i)))%mod #2**(i-1) ordered additive partitions of i

def G(n):
  global T,init
  v = matrix_mod_exp(n-1,T,init,mod)
  return v[-1]

#then pows >= 2
for e in xrange(2,18):
 b = 13**e
 for i in xrange(1,9*d+1):
   c = G(b-i) % mod
   S = ( S +(curr[i][1]%mod)*c ) % mod
print S

