from proj_euler import tot_fill,shanks_factorize
from fractions import gcd
from CR_NEWTON_LAGRANGE import Lagrange_cr,EEA

arr = tot_fill(1005001)
su = 0

 

for m in xrange(10**6,10**6+5000):
 for n in xrange(10**6,m):
  fm = arr[m]
  fn = arr[n]
  d,s,t = EEA(n,m)
  if (fn-fm) % d ==0:
   su +=  (fm + ((fn-fm)/d) *t*m) % (m*n/d)
   
  
print su  
