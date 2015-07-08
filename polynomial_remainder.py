import numpy as np
from scipy.misc import comb
import sys

p = int(sys.argv[1])

#too much memory
#fact = np.zeros(p,dtype = int)
#ifact = np.zeros(p,dtype = int)

ifact2 = {}

def mod_inv(k):
  global p
  return pow(k, p-2,p)

#def init_facts(p):
  #fact[0] = 1
  #ifact[0] = 1
  #for i in xrange(1,p):
    #fact[i] = (i * fact[i-1]) % p
    #ifact[i] = (mod_inv(i) * ifact[i-1]) % p
  #fact[0] = 0

def qbinomial(n,m,p):
  global ifact2
  if n < m or m < 0:
    return 0
 
  res = 1
  for k in xrange(n - m + 1,n+1):
    res = (res * k) % p
  if not ifact2.has_key(m):
    q = 1
    for k in xrange(1,m+1):
      q = (q * mod_inv(k)) % p
      
    ifact2[m] = q
  
  return (res * ifact2[m]) % p

def binomial_mod(n,m,p):
  '''
  Implementation of Lucas theorem.
  INPUTS -- n and m natural numbers, n >= m
  p prime
  RETURNS n choose m mod p
  '''
#  global fact #factorials mod p
 # global ifact #inverse factorials mod p
  r = 1
  while m:    
    r_m = m % p
    m = m//p
    r_n = n % p
    n = n//p
#    print "inputs " + str((r_n,min(r_m,r_n - r_m)))
 #   print str(comb(r_n,min(r_m,r_n - r_m))) + " " + str(qbinomial(r_n,min(r_m,r_n - r_m),p))
    r *= (qbinomial(r_n,min(r_m,r_n - r_m),p)) % p
    if not r:
      return r
  return r % p

def remainder_coeff(n,m,l,p):
  '''
  Let r(x) be the polynomial remainder of division of x^n by (x-1)^m.
  This function returns the absolute value of the l-th coefficient of r(x).
  (mod p) given to the program
  '''
#  init_facts(p)

  res = 0
  r2 = 0
  for k in xrange(0,l+1):
    res = (res + binomial_mod(m-1-k,l-k,p) * binomial_mod(n-1-k,m-1-k,p)) % p
  #  print "inputs " + str((m-1-k,l-k))
   # print str(binomial_mod(m-1-k,l-k,p)) + " " + str(comb(m-1-k,l-k,exact = True) % p) 
    #r2 += comb(m-1-k,l-k,exact = True)*comb(n-1-k,m-1-k,exact = True)
 # print r2 % p
  return res

print remainder_coeff(10**13,10**12,10**4,p)