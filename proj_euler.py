import numpy as np
from random import randint
from fractions import gcd as frac_gcd
from math import floor,ceil
from bisect import bisect_right

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

def dict_to_transition_matrix(tdict,states,rev_dict=False):
 #Takes a transition dictionary mapping states to possible outcomes
 #currently doesn't support weights
 k=states
 rd={} #dict mapping states to the state number
 for i,s in enumerate(k):
  rd[s]=i
 l=len(k)
 T = np.zeros((l,l),dtype=np.int64)
 for s1 in tdict:
  i1=rd[s1]
  for s2 in tdict[s1]:
   T[rd[s2],i1] += 1
 if rev_dict:
  return T,rd
 else:
  return T

start_primes = [2, 3, 5, 7, 11, 13, 17,37]
    
def MillerRabin(n):
  '''
  For n < 341,550,071,728,321, this is a deterministic primality test
  '''
  global start_primes
  n = int(n)
  if n == 1:
    return 0
  primes = start_primes 
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

def solve_lin_mod_eq(a,b,mod):
 #Returns all solutions to the linear equation ax=b (mod)
 d,x,y = egcd(a,mod)
 if d > 1:
  if b%d:
   #No solutions exist
   return None
  else:
   s = solve_lin_mod_eq(a/d,b/d,mod/d)
   return [(s+i*(mod/d))%mod for i in xrange(d)] 
 else:
  return (x*b) % mod

def mod_inv(a,mod):
 #return the modular inverse of a mod d
 d,x,y = egcd(a,mod) #so ax+mod*y equiv d mod a*mod
 return x % mod if d==1 else False

def gcd(a,b):
  return a if not b else gcd(b,a%b)

def comp_gcd(a,b):
  return a if not b else comp_gcd(b,comp_mod(a,b))

def comp_mod(a,b):
 q = a/b
 q = floor(q.real+.5) + floor(q.imag+.5)*1j
 return a -b*q

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def is_square(n):
  t = isqrt(n)
  return t*t==n

def pord(n,p):
 e,d=0,1
 while n%p == 0:
  e+=1
  d*=p
  n/=p
 return d,e 

def prime_fact_ord(p,n):
  '''
  The highest power of p that divides n!, p prime
  '''
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

def lin_sum(n):
 return n*(n+1)/2
def square_sum(n):
 return n*(n+1)*(2*n+1) / 6

def factor_range(N,primes=False):
 '''
 Factor every number from 1 to N.
 '''
 factors = [{} for i in xrange(N+1)]
 if primes:
  p = []
 for i in xrange(2,N+1):
   if not len(factors[i]):
     if primes:
       p.append(i)
     a = i
     e = 1
     while a <= N:
       for x in xrange(a,N+1,a):
         factors[x][i] = e
       e += 1
       a *= i
 if primes:
  return factors,p
 return factors  

def quad_factor_range(a,b,c,N):
 '''
 factor the quadratic a*x^2 + b*x + c for all integers from 0 to N (inclusive)
 '''
 d = b*b - 4*a*c
 primes = primes_and_mask(N)[0]
 n_arr = [a*i*i+b*i+c for i in xrange(N+1)]
 factors = [{} for i in xrange(N+1)]
 for p in primes:
  if p == 2:
    res = []
    if not c%2:
     res.append(0)    
    if not (a+b+c)%2:
     res.append(1)
  elif not a%p:
    if b%p:
     res = [(-c*pow(b,p-2,p))%p]
    elif c %p:     
     continue
    else:
     res = range(p)
  else:
    sq = mod_sqrt(d,p)
#    print d,p,sq
    if not sq:
      continue
    a_inv = pow(2*a,p-2,p)
    res = [((-b+sq)*a_inv)%p,((-b-sq)*a_inv)%p]
#    print res
  for q in xrange(0,N+1,p):
    for r in res:
     ind=r+q
     if ind <= N:
       temp = n_arr[ind]
       if not temp:
        continue
       e=0
       while temp%p==0: 
        temp /=p
        e += 1
       factors[ind][p] = e
       n_arr[ind]=temp
  
 for ind in xrange(N+1):
   if n_arr[ind]==1:
    continue
   else:
    comb_factors(factors[ind],shanks_factorize(n_arr[ind]))
 return factors     

def mod_sqrt(n,p):
 '''
 Compute sqrt(n) mod p where p is a prime
 '''
 n = n % p
 Q = p-1
 if not pow(n,Q/2,p) == 1:
   return 0
 
 while True:
  z = randint(2,Q)
  if pow(z,Q/2,p) == p-1:
    break
 
 S = 0
 while Q % 2 == 0:
  Q /= 2
  S += 1
 c = pow(z,Q,p)
 R = pow(n,(Q+1)/2,p)
 M = S
 t = pow(n,Q,p)
 while not t == 1:
  i = 0
  temp = t
  while not temp ==1:
    i += 1
    temp = (temp * temp) % p
  
  b = pow(c,pow(2,M-i-1,p-1),p)
  R = (R*b) % p
  t = (t*b*b)%p
  c = (b*b) % p
  M = i
  
 return R
 

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
#    print n,k,Q1,Q0,P,sq,i
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

#sieve on the number of divisors
def nofd_fill(n):
  d = np.ones(n,dtype=np.int64)
  for i in xrange(2,n):
    for j in xrange(i,n,i):
      d[j] += 1
  return d

#Sieve on a general multiplicative function. Not mobius or anything which is one at primes.
def generic_sieve_fill(n,f):
  mask = np.ones(n,dtype=np.int64)
  for i in xrange (2,n):
    if mask[i] == 1:
      e = 1
      a = i
      while a < n:
        for j in xrange(a,n,a):
          if (j/a) % i:
            mask[j] = f(mask[j],i,e)
        a *= i
        e += 1
  return mask

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
 If exact is set to False, then allow for numbers divisible by a subset of a, but not all members.
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

def FareyGen(denom): 
 a,b = 0,1
 c,d = 1,denom
 while True:
  yield (c,d)
  if c == denom-1 and d == denom:
    break
  t1,t2 = c,d
  c,d = (denom + b)/d*c - a, ((denom + b)/d)*d - b
  a,b = t1,t2
 
def prime_square_repr(p):
   '''
   INPUTS:
   p -- a prime congruent to 1 mod 4
   RETURNS:
   (a,b) -- integers such that a^2 + b^2 = p
   '''
   if p%4 == 3:
     raise Exception("Primes 3 mod 4 cannot be wriiten as the sum of 2 positive squares.")
   if p == 2:
     return [1,1]
   e = (p-1) / 2   
   while True:
     k = randint(2,p-2)
     if pow(k,e,p) == p-1:
       break
   k = pow(k,e/2,p)
   d = comp_gcd(k+1j,p+0j)
   if abs(d) ==1:
     d = comp_gcd(k-1j,p+0j)
   return sorted([abs(int(d.real)),abs(int(d.imag))])
 
def two_square_repr(f,cache={}):
  '''
  f -- the prime factorization of a positive integer n
  f is a dict mapping prime p to exponent e in the prime factorization.
  cache -- cache[p] = (a,b) a^2 + b^2 = p, a and b nonegative integers.
  Returns a list of ordered pairs 0<=a<=b with a^2 + b^2 = n.
  If no representations exist, returns an empty list.
  ''' 
  mul = 1
  reps = set([(0,1)])
  for p in f:
   e = f[p]
   if p%4==3:
    if e%2:
     return []
    else:
     mul *= p**(e/2)
     continue
   new_reps = set()
   if p in cache:
     rep = cache[p]
   else:
     rep = prime_square_repr(p)
   
   if p==2:
     #if e is odd, we have some extra representations
     mul *= 2**((e-e%2)/2)
     e=e%2
          
   for i in xrange(e):
     new_reps = set()
     for r in reps:
       if not r[0]:
         new_reps.add((r[1]*rep[0],r[1]*rep[1]))
       else:
         new_reps.add((abs(r[0]*rep[1]-r[1]*rep[0]),r[1]*rep[1]+r[0]*rep[0]))
         new_reps.add(tuple(sorted([r[1]*rep[1]-r[0]*rep[0],r[0]*rep[1]+r[1]*rep[0]])))
     reps = new_reps
  
  new_reps = []
  for r in reps:
    new_reps.append((mul*r[0],mul*r[1]))
   
  return new_reps

def sphere_points(r):
  '''
  Returns a list of all lattice points on a sphere of radius r centered at the origin.
  '''
  mul = 1
  while r % 2 == 0:
    mul *= 2
    r /= 2
  
  primes = primes_and_mask(r)[0]
  factors = [[] for i in xrange(r+1)]
  for p in primes:
    if p==2:
      for i in xrange(r%2,r+1,2):
        factors[i].append(2)
    
    else:
      for i in xrange((p-r)%p,r+1,p):
        factors[i].append(p)
      for i in xrange(r%p,r+1,p):
        factors[i].append(p)
  
  for i,f in enumerate(factors):
    if i==r:
     yield (r*mul,0,0)
     yield (-r*mul,0,0)
     continue
  
    t = (r-i)*(r+i)
    fact = {}
    for p in f:
      if p in fact:
        continue
      fact[p] = 0
      while t%p==0:
       fact[p]+=1
       t /= p
    if t > 1:
     fact[t] = 1
    for rep in two_square_repr(fact):
      if not rep[0]:
       for j in xrange(2):
        s = (-1)**j*mul
        yield (i*mul,rep[0],s*rep[1])
        yield (i*mul,s*rep[1],rep[0])
        if i:
          yield (-i*mul,rep[0],s*rep[1])
          yield (-i*mul,s*rep[1],rep[0])
        
       continue
      for j in xrange(4):
        s1 = (-1)**(j&1)*mul
        s2 = (-1)**(j/2)*mul
        yield (i*mul,s1*rep[0],s2*rep[1])
        if i:
         yield (-i*mul,s1*rep[0],s2*rep[1])
        if not rep[0] == rep[1]:
          yield (i*mul,s1*rep[1],s2*rep[0])
          if i:
           yield (-i*mul,s1*rep[1],s2*rep[0])
      

def argsort(seq):
  return sorted(range(len(seq)), key=seq.__getitem__)
def init_fact(n):
  fact = [1]
  for i in xrange(1,n+1):
     fact.append(i*fact[-1])
  return fact

#Find the nth permutation in S_f
def fact_base(n,f):
  rep = []
  rem = range(1,f+1)
  fact = init_fact(f-1) 
  for i in xrange(f):
   q = n/fact[-i-1]
   n -= q * fact[-i-1]
   rep.append(rem[q])
   rem.remove(rem[q]) 
  return rep
  
  
    
