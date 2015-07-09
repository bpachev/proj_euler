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
  if n == 1:
    return 0

  primes =  [2, 3, 5, 7, 11, 13, 17]
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
        x = x*x % n
        if x == n-1:
          break
        if x == 1:
          return 0
      if not x*x % n == 1:
        return 0

  return 1

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

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def gcd(a,b):
  return a if not b else gcd(b,a%b)

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


def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

