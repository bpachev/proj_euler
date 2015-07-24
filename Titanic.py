from fractions import gcd

#This works for n = 111
#
n=111
s = 0
mod = 10**8
def f(x):
 if x > 2: 
  return (pow(2,x,mod)-1-x-x*(x-1)/2)%mod
 else:
  return 0
def T(n,d,k):
 t = 0
 for l in xrange(3,n/d+1):
  #leftovers from playing around with code, will fix
  t += f(l)*d*k
  t += d*f(l)*k
 t += f(n/d+1)*(n-k*(n/d)+1)*(n%d+1)
 t += f(n/d) * (n-k*(n/d)+1-k)*(d-n%d-1)
 #if k = d-1 what about negativity?
 #Not sure, but it works
  
# print t,d,k
 return t

for d in xrange(1,n+1):
  for k in xrange(1,d+1):
    if gcd(k,d) == 1:
      if d>1:
        s += 4*T(n,d,k)
      else:
        s += 2*T(n,d,k)

print (pow(2,(n+1)**2,mod) -1 - s - (n+1)*2*f(n+1) - (n+1)**2)%mod
      


