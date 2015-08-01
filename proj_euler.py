import numpy as np

def recur_mod(n ,T, I,mod = 10**8,matrix = False):
  '''
  Compute the n-th member of the linear recurrence with transition matrix T and initial values given by the matrix I.
  '''
  Accum = I
  n = n - T.shape[0] + 1
  while n:
    if n % 2:
      Accum = np.remainder(T.dot(Accum),mod)
    T = np.remainder(T.dot(T),mod)
    n /= 2
  if matrix:
    return Accum
  else:
    return Accum[0,0]

def matrix_mod_exp(n,T,I,mod):
  Accum = I
  while n:
    if n % 2:
      Accum = np.remainder(T.dot(Accum),mod)
    T = np.remainder(T.dot(T),mod)
    n /= 2
  return Accum

def safe_matrix_exp(n,T,I,mod):
  Accum = I
  while n:
    if n % 2:
      Accum = safe_matrix_vector_dot(T,Accum,mod)
    T = safe_matrix_mul(T,T,mod)
    n/= 2
  return Accum

#T is a circulant matrix. This allows us to compute T.dot(T) in O(n^2) instead of O(n^3)
def circulant_mod_exp(n,T,I,mod):
  k = T.shape[0] #dimension of matrix
  Accum = I
  while n:
    if n % 2:
#      Accum = np.remainder(T.dot(Accum),mod)
       Accum = safe_matrix_vector_dot(T,Accum,mod)
#    firstCol = np.remainder(T.dot(T[:,0]),mod)
    firstCol = safe_matrix_vector_dot(T,T[:,0],mod)
#    T = np.remainder(T.dot(T),mod)
    for i in xrange(k):
      T[:,i] = np.roll(firstCol,i)
    n /= 2
  return Accum

#avoids overflow when doing matrix-vector multiplication
def safe_matrix_vector_dot(M,v,mod=10**9):
  res = np.empty(M.shape[0],np.int64)
  for j in xrange(M.shape[0]):
    s = 0
    for i in xrange(v.shape[0]):
      s = (s + (M[j,i]%mod) * (v[i]%mod)) % mod
    res[j] = s
  return res

def safe_matrix_mul(A,B,mod):
  res = np.zeros((A.shape[0],B.shape[1]),np.int64)
  for i in xrange(B.shape[1]):
    for j in xrange(A.shape[1]):
      res[:,i] = np.remainder((res[:,i] + np.remainder(B[j,i]*A[:,j],mod)),mod)
  return res
    
def MillerRabin(n):
  '''
  For n < 341,550,071,728,321, this is a deterministic primality test
  '''
  n = int(n)
  if n == 1:
    return 0
  primes =  [2, 3, 5, 7, 11, 13, 17,37]
  for p in primes:
    if n == p:
      return 1
    if n % p == 0:
      return 0

  s = 0
  d = n-1
  while d % 2 == 0:
    s += 1
    d /= 2

  for p in primes:
      x = pow(p,d,n)
      if x == 1 or x == n-1:
        continue
      for i in xrange(s-1):
        x = pow(x,2,n)
        if x == n-1:
          break
        if x == 1:
          return 0
      if not x*x%n == 1:
        return 0

  return 1

def is_prime(n,cap,mask):
  if n <= cap:
    return mask[n]
  else:
    return MillerRabin(n)

#is are a and b permutations of one another?
def permu(a,b):
  d1 = map(int,list(str(a)))
  d2 = map(int,list(str(b)))
  if not len(d2) == len(d1):
    return False
  for i in xrange(10):
    n1 = 0
    n2 = 0
    for j in xrange(len(d2)):
      if d2[j] == i:
        n2 += 1
      if d1[j] == i:
        n1 += 1
    if not n1 == n2:
     return False
  return True

def is_palindrome(a):
  s = str(a)
  return s == s[-1::-1]

#For getting lots of small primes when I'm too lazy to use c
def primes_and_mask(n):
  mask = np.ones(n + 1)
  mask[0] = 0
  mask[1] = 0
  primes = []
  for i in xrange(2,n+1):
    if mask[i]:
      primes.append(i)
      j = i*i
      while j <= n:
        mask[j] = 0
        j += i
  return primes, mask

def mark_primes(n):
  mask = np.ones(n + 1)
  mask[0] = 0
  mask[1] = 0
  for i in xrange(2,n+1):
    if mask[i]:
      j = i*i
      while j <= n:
        mask[j] = 0
        j += i
  return mask


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def gcd(a,b):
  return a if not b else gcd(b,a%b)


def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def prime_fact_ord(p,n):
  o = 0
  a = p
  while a <= n:
    o += n/a
    a *= p
  return o

def base_repr(n,b):
  d = []
  while n:
    d.append(n%b)
    n /= b
  return d


def arithmetic(a,d,k):
 '''
 INPUTS:
 a -- starting member of arithmetic progression
 d -- difference between consecutive terms
 k -- number of terms
 
 RETURN:
 sum of arithmetic progression
 '''
 return (k*(2*a+d*(k-1))) / 2

def comb_factors(f1,f2):
 for f in f2:
   if f in f1:
     f1[f] += f2[f]
   else:
     f1[f] = f2[f]

def shanks_factorize(N,primes=None):
  n = N
  factors = {}
  if primes is not None:
   cap = int(n**.25)
   for p in primes:    
    if p > cap:
     break
    if p < n:
     if n % p==0:
      e = 0
      while n %p==0:
       n /= p
       e += 1
      factors[p] = e
     else:
      break
   if n ==1:
    return factors
  
  d = shanks_div(n)
  if d == n:
    factors[d] = 1
    return factors
  else:
    comb_factors(factors,shanks_factorize(d))
    comb_factors(factors,shanks_factorize(n/d))
    return factors
    


def shanks_div(n):
 '''
 Uses Shanks' Square Forms factorization to find a divisor of n.
 '''
 #Handle the special cases of n a square or prime.
 sq = isqrt(n)
 if sq*sq == n:
   return sq
 elif MillerRabin(n):
   return n
 else:
  k = 1
  while True:
    r = shanks_trial(n,k)
    if r >1 and r < n:
      return r
    else:
     k += 1
    if k > n:
      print MillerRabin(n),n
      raise Exception("Could not find a suitable multiple k in shanks_div.")
 
def shanks_trial(n,k):
 '''
 One run of Shanks' algorithm trying to find a divisor of n,
 and with the input multiple k.
 '''
 sq = isqrt(k*n) 
 P = sq
 Q0,Q1 = 1, k*n - P*P
 i=1
 while True:
   q = isqrt(Q1)
   if q*q == Q1 and not i%2:
     b = (sq - P)/ q
     P = b*q + P
     Q0 = q
     Q1 = (k*n-P*P)/Q0
     break
   i+=1
   if Q1 == 0:
    print n,k,Q1,Q0,P,sq,i
    if n%P==0:
     return P 
    else:
     return 1
   b = (sq+P)/Q1
   P_new = b*Q1 - P
   Q_new = Q0 + b*(P-P_new)
   P = P_new
   Q0 = Q1
   Q1 = Q_new
  
 while True:
   b = (sq+P)/Q1
   P_new = b*Q1 - P
   Q_new = Q0 + b*(P-P_new)
   if P == P_new:
     return gcd(P,n)
   P = P_new
   Q0 = Q1
   Q1 = Q_new
 
 

def factorize(n,primes):
  factors = []
  for p in primes:
   if p < n:
    if n % p==0:
     e = 0
     while n %p==0:
      n /= p
      e += 1
     factors.append([p,e])
   else:
    break
  if n > 1:
   factors.append([n,1])
  return factors

#Generate all divisors of n given its prime factorization
def divisors(factors):
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return  

def tot_fill(n):
  tot = np.arange(n,dtype=np.int64)
  tot[1] = 1
  for i in xrange(2,n):
   if tot[i] == i:
    for j in xrange(i,n,i):
     tot[j] = tot[j] - tot[j]/i
  return tot

#sieve on the sum of divisors
def sofd_fill(n):
  d = np.ones(n,dtype=np.int64)
  for i in xrange(2,n):
    for j in xrange(i,n,i):
      d[j] += i
  return d

def test_cores(l):
 t = 1
 n = 1
 for p in l:
   t *= (p-1)
   n *= p
 return ((t-1) % (n - t) == 0)

def HarshadGen(a,c,mul=1,exact=True):
 '''
 ARGS: a,c
 a -- an array of natural numbers
 c -- a cap
 Generates all numbers that are divisible by all of the members of a, and less than cap
 Assumes the elements of a are coprime (otherwise duplicates will occur)
 TODO: if exact is set to False, then allow for numbers divisible by a subset of a, but not all members.
 I.E if a=(2,3,5) then with exact=False, 6 is allowed, but not if exact=True  
 '''
 if exact:
  p=1
  for x in a:
   p*=x
  for y in HarshadGen(a,c/p,p,False):
    yield y
  
 else:
  yield mul
  for i,x in enumerate(a):
    if x > c:
     break
    e = x
    while e <= c:
     for y in HarshadGen(a[i+1:],c/e,mul*e,False):
      yield y
     e*=x
 

