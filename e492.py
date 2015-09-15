from proj_euler import primes_and_mask,isqrt
from numpy import zeros

def mod_frac(n,d,p):
 return (n*pow(d,p-2,p)) % p

#multiplication in Zp[sqrt(d)] , p prime
def mul_rads(a1,a2,b1,b2,d,p):
  return (a1*b1+d*a2*b2) % p, (a1*b2+b1*a2) % p

def a(N,p):
 '''
 Computes a(n), where a(n+1) = 6*a(n)^2+10*a(n) + 3, and a(1) = 1
 Note that 6*a(n+1)+5 = 36*a(n)^2+60*a(n)+23 = (6*a(n)+5)^2 - 2 
 Letting T(n) = 6*a(n)+5, T(n+1) = T(n)^2 - 2, which has a closed form of
 x^(2^n) + y^(2^n) where x and y are the roots of x^2 - a*x + 1, and a = T(0)
 So we need here to shift indices. a(n) is really n-1 applications of the map.
 We assume that mod is prime
 '''
 d =  11*11 - 4
 half = pow(2,p-2,p)
 a1,a2 = (11*half) % p, half #root 1, the second component is the coeficient of sqrt(11^2-4)
 b1,b2 = a1, p-half #root 2
 accum1 = (1,0)
 accum2 = (1,0)
 e = pow(2,N-1,p*p-1)
 while e:
  if e&1:
   accum1 = mul_rads(a1,a2,accum1[0],accum1[1],d,p)
   accum2 = mul_rads(b1,b2,accum2[0],accum2[1],d,p)
  a1,a2 = mul_rads(a1,a2,a1,a2,d,p)
  b1,b2 = mul_rads(b1,b2,b1,b2,d,p)
  e /= 2
 return ((accum1[0]+accum2[0]-5) * pow(6,p-2,p)) % p
  
A,B,N = 10**9,10**7,10**15
end=A+B
primes = primes_and_mask(isqrt(end))[0]

mask = zeros(B+1)
for p in primes:
 for t in xrange(-((-A)/p),end/p+1):
   mask[t*p-A] = 1

s = 0
for i in xrange(A,end+1):
  if not mask[i-A]:
    s += a(N,i)

print s 
