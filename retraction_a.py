from proj_euler import factor_range,prime_fact_ord,comb_factors,shanks_factorize
from scipy.misc import comb

def r_slow(n):
 r=1
 factors = shanks_factorize(n)
 for f in factors:
   r *= f**factors[f]+1
 return r-n 

def solve(N,mod=10**9+7):
 #Assumes a prime modulus
 f,primes = factor_range(N,primes=True)
 curr_fact = {p:0 for p in primes}
 s = 0
 R = 1
 mul_dict = {}
 for i in xrange(1,N/2+1):
  f1 = f[N+1-i] #mult
  f2 = f[i] #div
  
  for p in f1:
   if p in mul_dict:
    mul_dict[p] += f1[p]
   else:
    mul_dict[p] = f1[p]
  
  for p in f2:
   if p in mul_dict:
    mul_dict[p] -= f2[p]
   else:
    mul_dict[p] = -f2[p]
  
  
  
  mul = 1
  for p in mul_dict:
   if curr_fact[p]+mul_dict[p]:
    mul = (mul*(pow(p,curr_fact[p]+mul_dict[p],mod)+1))%mod
   if curr_fact[p]:
     mul = (mul * pow(pow(p,curr_fact[p],mod)+1,mod-2,mod)) % mod
  
  if not mul:
    continue
    
  R = (mul*R)%mod
  if N%2==0 and 2*i==N:
   s = s+R
  else:
   s = s+2*R
  while s > mod:
   s -= mod
  comb_factors(curr_fact,mul_dict)
  mul_dict = {}
 
 return (s+2 - pow(2,N,mod))%mod

print solve(10**7)

