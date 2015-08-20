from proj_euler import primes_and_mask,mod_sqrt,shanks_factorize,MillerRabin,comb_factors,quad_factor_range

def r_slow(n):
 r=1
 factors = shanks_factorize(n)
 for f in factors:
   r *= f**factors[f]+1
 return r-n 

def solve_1(cap,mod=10**9+7):
 primes = primes_and_mask(cap)[0]
 R = [1 for i in xrange(cap+1)]
 N = [i**4+4 for i in xrange(cap+1)]

 sq = [0,0,0,0]
 for p in primes:
  if p == 2:
    for i in xrange(1,cap+1):
      mul = 1
      while N[i]%2==0:
       N[i]/=2
       mul*=2
      if mul>1:
       R[i] = (R[i]*(mul+1))%mod
    continue
  sq[0] = mod_sqrt(p-4,p)
  if not sq[0]:
   continue
  sq[2] = mod_sqrt(sq[0],p)
  sq[3] = mod_sqrt(p-sq[0],p)
  sq[0] = (p-sq[3])%p
  sq[1] = (p-sq[2])%p
 # print p,sq
  for q in xrange(0,cap+1,p):
    for r in sq:
      if r and r <= cap-q:
        mul=1
        while N[q+r]%p==0:
         mul *= p
         N[q+r]/=p
        if mul > 1:
         R[q+r] = (R[q+r]*(mul+1))%mod
 print "Completed seiving."
 c=0
 s = 0
 for i,r in enumerate(R):
  if i==0:
   continue
  n = N[i]
  if n ==1:
    s =  (s + r -i**4-4)%mod
    continue
  factors = shanks_factorize(n)
  for f in factors:
    if f>1:
     r = (r*(f**factors[f]+1))%mod
  if len(factors)>=2:
   c +=1
  s =  (s + r -i**4-4)%mod
 print s 
 print c
 return s

def solve_2(cap,mod=10**9+7):
 f = quad_factor_range(1,0,1,cap+1)
 s = 0
 for i in xrange(1,cap+1):
   comb_factors(f[i-1],f[i+1])
   r = 1
   for p in f[i-1]:
     r = (r * (pow(p,f[i-1][p],mod)+1)) % mod 
   s += r
   while s > mod:
    s -= mod
   s = (s - i**4-4)%mod
 return s
print solve_2(10**7)

