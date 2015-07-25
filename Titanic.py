from fractions import gcd
from SummatoryTotient import TotientSum



#This works for n = 111
n=10**10
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

t0 = TotientSum(n,f0,fsum0,g0,mod)
t1 = TotientSum(n,f1,fsum1,g1,mod)
t2 = TotientSum(n,f2,fsum2,g2,mod)



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

def sum_component(n,c):
 '''
 For testing purposes. Sums a function c(n,d,k) over all d and k coprime, d != 1, d<= n,d>k
 '''
 s = 0
 for d in xrange(1,n+1):
   for k in xrange(1,d):
     if gcd(k,d) == 1:
         s = (s+c(n,d,k))%mod
 return s
 
def t2_comp(m):
 return 4*f_sum(m) - 2*(m+1)*(m+1)*f(m) + 2*m*m*f(m+1)
def t1_comp(m):
 global n
 return 6*(n+1)*(f(m)*(m+1)-f(m+1)*(m))
def t0_comp(m):
 global n
 return 4*(n+1)*(n+1)*(f(m+1)-f(m))

t2.Sum(n)
#t2.weighted_sum(t2_comp)
t1.Sum(n)
#print t1.weighted_sum(t1_comp)
t0.Sum(n)
#print t0.weighted_sum(t0_comp)
def c2_test(n,d,k):
  m=n/d
  return 4*(2*d*k*f_sum(m)+d*k*m*m*f(m+1)-d*k*(m+1)*(m+1)*f(m))
def c1_test(n,d,k):
  m = n/d
  return 4*(f(m)*(d+k)*(m+1)*(n+1)-(d+k)*m*(n+1)*f(m+1))
def c0_test(n,d,k):
  m = n/d
  return 4*(n+1)**2*(f(m+1)-f(m))
def tit_comp(n,d,k):
  return c0_test(n,d,k)+c1_test(n,d,k)+c2_test(n,d,k)

s = (t0.weighted_sum(t0_comp)+t1.weighted_sum(t1_comp)+t2.weighted_sum(t2_comp)+2*T(n,1,1))%mod
print s
#print sum_component(n,tit_comp)%mod
#print sum_component(n,lambda n,d,k : 4*T(n,d,k))%mod


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
#print slow_titanic(n)%mod

print (pow(2,(n+1)**2,mod) -1 - s - (n+1)*2*f(n+1) - (n+1)**2)%mod
      


