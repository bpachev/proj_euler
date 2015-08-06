from bisect import bisect_right,bisect_left
from proj_euler import nofd_fill
from blist import blist

def T(n,nofd):
 if n%2==0:
   return nofd[n/2]*nofd[n+1]
 else:
   return nofd[n]*nofd[(n+1)/2]

def solve(cap,mod = 10**18):
 s = 0
 t_arr = blist([])
 inversions = [0]
 nofd = nofd_fill(cap+2)
 for i in xrange(1,cap+1):
   if i % (5*10**5) == 0:
     print "ON %d" % i
   t = T(i,nofd)
   pos = bisect_right(t_arr,t)
   inversions.append(len(t_arr)-pos)
   t_arr.insert(pos,t)
 print "On Second Stage."
 del t_arr 
 t_arr = blist([])
 for j in xrange(cap,0,-1):
   t = T(j,nofd)
   pos = bisect_left(t_arr,t)
   s = (s + inversions[j]*pos) % mod
   t_arr.insert(pos,t)
   if j % (5*10**5) == 0:
     print "ON %d, sum = %d" % (j,s)    
 return s
print solve(6*10**7)

