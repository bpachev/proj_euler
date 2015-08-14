from proj_euler import isqrt
from fractions import gcd

def sqrt_lt(F,n):
  '''
  Returns true iff F[0]/F[1] < sqrt(n) 
  '''
  if F[0]*F[0] < n*F[1]*F[1]:
    return True
  else:
    return False 

def closest_sqrt_approx(A1,A2,n):
  '''
  INPUTS: A1, A2 -- tuples representing fractions.
  n -- a positive integer
  RETURN: (num,denom) the closer of A1 and A2 to sqrt(n)
  Very often, the error between convergents and the actual square root is very low.
  It is necessary to determine which approximation is more accurate.  
  This function uses only integer arithmetic, and is neccessary to avoid precision errors.
  '''
  if A1[0]*A2[1] < A1[1]*A2[0]:
    L = A1
    H = A2
  else:
    L = A2
    H = A1
  
  med = (A1[0]*A2[1] + A1[1]*A2[0],2*A1[1]*A2[1])
  if sqrt_lt(med,n):
    return H
  else:
    return L


def sqrt_approx(n,bound=10**12):
  t = isqrt(n)
  if t*t == n:
    return (t,1)
  L = (t,1)
  H = (1,0)
  while True:
    num,denom = L[0]+H[0],L[1]+H[1]
    g = gcd(num,denom) 
    if denom/g > bound:
     return closest_sqrt_approx(L,H,n)
      
    M = (num/g,denom/g)
    if M[0]*M[0] < n*M[1]*M[1]:
      L = M
    else:
      H = M


def convergents_sqrt_approx(n,bound=10**12):
  R = isqrt(n)
  if R*R == n:
    return (R,1)
  h = R
  k = 1
  h1 = 1
  h2 = 0
  k1 = 0
  k2 = 1
  P = 0
  Q = 1
  a = R
  while True:
    h = a*h1 + h2
    k = a *k1 + k2
    if k > bound:
      maxn = (bound-k2) / k1
      minn = (a+1)/2
      if minn==maxn and a%2==0:
       th,tk = minn*h1+h2,minn*k1+k2
       return closest_sqrt_approx((h1,k1),(th,tk),n)
      elif minn > maxn:
       return (h1,k1)
      else:
       return (maxn*h1+h2,maxn*k1+k2)
       
      break      
    h2 = h1
    k2 = k1    
    k1 = k
    h1 = h	  
    P = a*Q - P
    Q = (n - P*P) / Q
    a = (R+P)/Q
    

def solve(n,bound=10**12):
 s =0
 for i in xrange(2,n+1):
#  q = convergents_sqrt_approx(i,bound)
  q = sqrt_approx(i,bound)
  if q[1]==1:
   continue
  s += q[1]
 print s
 return s
solve(10**5)
