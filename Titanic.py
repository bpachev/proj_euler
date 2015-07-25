from fractions import gcd
from SummatoryTotient import TotientSum



#This works for n = 111
n=111
s = 0
mod = 10**8

#functions to sum tot(n)
f0 = lambda x: 1
g0 = lambda n,m: (n*(n+1)/2)%m
fsum0 = lambda x,y,m: (y-x)%m

#functions to sum n*tot(n)
f1 = lambda x: x
g1 = lambda n,m: (n*(n+1)*(2*n+1)/6)%m
fsum1 = lambda x,y,m: g0(y-1,m)-g0(x-1,m)

#functions to sum n^2*tot(n)
f2 = lambda x: x*x
g2 = lambda n,m: ((n*(n+1)/2)**2)%m
fsum2 = lambda x,y,m: g1(y-1,m)-g1(x-1,m)

t0 = TotientSum(6,f0,fsum0,g0,mod)
print t0.weighted_sum(lambda x:1)
t2 = TotientSum(6,f1,fsum1,g1,mod)
t2 = TotientSum(6,f2,fsum2,g2,mod)

def f(x):
 global mod
 if x > 2: 
  return (pow(2,x,mod)-1-x-x*(x-1)/2)%mod
 else:
  return 0
def f_sum(m):
 global mod
 if m < 3:
   return 0
 return (pow(2,m+1,mod) - 1 - (m+1)*m*(m-1)/6 - ((m+1)*m)/2 - (m+1)) % mod
 
def T(n,d,k):
 global mod
 t = 0
# for l in xrange(3,n/d+1):
  #leftovers from playing around with code, will fix
#  t += f(l)*d*k
#  t += d*f(l)*k
 m = n/d
 t += 2*d*k*f_sum(m)
 t += f(m+1)*((n+1)**2 -(k+d)*m*(n+1)+d*k*m*m)
 t += f(m)*(-(n+1)**2 +(d+k)*(n+1)*(m+1)-d*k*(m+1)*(m+1))
 
# t += f(n/d+1)*(n-k*(m)+1)*(n%d+1)
# t += f(n/d) * (n-k*(m)+1-k)*(d-n%d-1)
 #if k = d-1 what about negativity?
 #Not sure, but it works
  
# print t,d,k
 return t%mod

def slow_titanic(n):
 s = 0
 for d in xrange(1,n+1):
   for k in xrange(1,d+1):
     if gcd(k,d) == 1:
       if d>1:
         s += 4*T(n,d,k)
       else:
         s += 2*T(n,d,k)
 return s

print (pow(2,(n+1)**2,mod) -1 - slow_titanic(n) - (n+1)*2*f(n+1) - (n+1)**2)%mod
      


