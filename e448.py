import numpy as np
from proj_euler import arithmetic,gcd
cap = 99999999019
mod = 999999017
sq = int(cap**.5)
c1 = np.zeros(sq+1,np.int64) #F(n/k), k <= int(sqrt(n))
c2 = np.zeros(sq+1,np.int64) #F(k), k <= int(sqrt(n)) 

max_cache = int(cap**(2./3))+1
totSum = np.arange(max_cache,dtype=np.int64)

for i in xrange(2,max_cache):
  if totSum[i] == i:
    for j in xrange(i,max_cache,i):
      totSum[j] = totSum[j] - totSum[j]/i
  totSum[i] = (i*totSum[i]/2 + totSum[i-1]) % mod

def G(n,mod):
 return ((n*(n+1)*(n+1))/2 - (n*(n+1)*(2*n+1)) / 6) % mod

def F(n,k=1):
 global c1,c2,sq,mod,max_cache,totSum
 if n == 1:
   return 1
 if n < max_cache:
   return totSum[n]
 if n <= sq and c2[n]:
   return c2[n]
 if k <=sq and c1[k]:
   return c1[k]   
 s = G(n,mod)
# print s,n
 q,div = n/2,2
 while q >= 1:
   r = n % div
   div_next = div + r/q + 1
   s = ( s - (arithmetic(div,1,div_next-div)%mod) * F(n/div,k*div)) % mod
   div = div_next
   q = n/div_next
 if n <= sq:
   c2[n] = s
 if k <=sq:
   c1[k] = s
 return s   
s = 0

div,q,r = cap,1,0
while div >= 1:
 q,r = divmod(cap,div)
 q1,r1 = divmod((div-r),(q+1))
 if not r1:
   q1 = q1-1
 s = (s + (q1+1)*F(q,div)) % mod
 div = div-q1-1

print s


