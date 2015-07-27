import numpy as np
from fractions import gcd
pcap = 10**7
sq=int(pcap**.5)

c1 = np.zeros(sq+1,dtype=np.int64) #n/k
c2 = np.zeros(sq+1,dtype=np.int64) #n
table = [[3,0,0],[3,2,0],[3,1,0],[3,3,1],[3,2,0],[3,4,1],[3,3,1],[3,5,2],[3,4,1],[3,6,3],[3,5,2],[3,7,4]]

def poly_sum(k,i):
 if k==0:
  return i+1
 elif k==1:
  return i*(i+1)/2
 elif k==2:
  return (i*(i+1)*(2*i+1))/6

def G(n):
 global table
 s = 0
 q,r = divmod(n,12)
 for j in xrange(12):
  if j <= r:
   i = q
  else:
   i = q-1 
#  print s,j,i
  for d in xrange(3):
   s += table[j][2-d]*poly_sum(d,i)
 return s  

def F(n,k=1):
 global s1,c1,c2
 if n==3:
  return 1
 if n <3:
  return 0
 if k <= sq and c1[k]:
  return c1[k]
 if n <= sq and c2[n]:
  return c2[n]
 
 s = G(n)
 div,q = 2,n/2
 while q >= 1:
   r = n % div
   div_next = div + r/q + 1
   s = s - (div_next-div) * F(n/div,k*div)
   div = div_next
   q = n/div_next
 
 if k <= sq:
  c1[k]=s
 if n <= sq:
  c2[n]=s
 return s
 
def f_slow(n):
 s = 0
 for c in xrange (1,n):
   for b in xrange(1,c+1):
     for a in xrange(1,b+1):
      if a+b+c<=n and c<a+b and gcd(a,gcd(b,c))==1:
        s += 1
 return s

def g_slow(n):
 s = 0
 for c in xrange (1,n):
   for b in xrange(1,c+1):
     for a in xrange(1,b+1):
      if a+b+c<=n and c<a+b:
        s += 1
 return s
 
 
#print F(pcap),G(pcap),f_slow(pcap),g_slow(pcap)
print F(pcap)

