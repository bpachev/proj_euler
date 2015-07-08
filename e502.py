from proj_euler import matrix_mod_exp,safe_matrix_exp
import numpy as np

w = 10**12
h = 100
mod = 1000000007
#mod = 10**9
def CastleSum(h,w,mod=1000000007):
  T = np.zeros((4*h,4*h),dtype=np.int64)
  I = np.zeros(4*h,dtype=np.int64)
  for i in xrange(1,h+1):
    I[4*i + i%4-4] = 1
    for j  in xrange(1,h+1):
      d = abs(i-j)
      for r in xrange(4):
        T[4*j+(r+d)%4-4,4*i + r-4] = 1
#  res = matrix_mod_exp(w-1,T,I,mod)
  res = safe_matrix_exp(w-1,T,I,mod)
#  print T
#  print I
#  print res
  s = 0
  for i in xrange(4,4*h+4):
    if (i%4 + i/4) % 4 == 0:
      s = (s + res[i-4]) % mod
  return s

print "MOD = " + str(mod)
print "f("+str(w)+","+str(h)+") = " + str((CastleSum(h,w,mod) - CastleSum(h-1,w,mod)) % mod)
