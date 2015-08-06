from proj_euler import matrix_mod_exp,MillerRabin
import numpy as np
from CR_NEWTON_LAGRANGE import Lagrange_cr

I = np.array([1,0],dtype=np.int64)
T = np.array([[1,1],[1,0]],dtype=np.int64)

start = 10**14
mod = 1234567891011
m1=1957137
m2=630803
if not m2*m1==mod:
 raise Exception("Incorrect modulus factorization.")

res1=matrix_mod_exp(start,T,I,m1)
res2=matrix_mod_exp(start,T,I,m2)

prev = Lagrange_cr((int(res1[1]),int(res2[1])),(m1,m2))
curr = Lagrange_cr((int(res1[0]),int(res2[0])),(m1,m2))

n = 10**5
count = 0
i = start+1
s = 0
while count < n:
 if MillerRabin(i):
   s += curr
   if s > mod:
    s -= mod
   count += 1
 curr,prev = curr+prev,curr
 if curr > mod:
  curr -= mod
 i += 1
print s 
  
 
