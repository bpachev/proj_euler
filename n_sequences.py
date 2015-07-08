import numpy as np
import proj_euler as pe


mod = 1000000009
n = 7500000

fact = {}
ifact = {}
fact[0] = 1
ifact[0] = 1

for j in xrange(1,n):
  fact[j] = (j * fact[j-1]) % mod
  ifact[j] = (pow(j,mod-2,mod) * ifact[j-1]) % mod

#Return the number of bounded n-sequences whose longest streak is at most k
# I think I've proven that S(n,k,m) = n*S(n,k,m-1) - (n-1)*S(n,k,m-k-1)
# S(n,k,1) = n for all k > 1. Any starting value is possible. Obviously m < 1 yields 0.
#The question is how to get from n back to 1 using decrements of k+1 and 1.
 
def numBoundedSeq(n,k):
  global fact
  global ifact
  global mod
  s = 0
  kdec = 0
  while (k+1)*kdec <= n:
    dec1 = n - (k+1)*kdec - 1
    if dec1 < 0:
      s = (s - pow(1-n,kdec-1,mod))
      kdec += 1
      continue 
    s = (s + pow(n,dec1,mod) * pow(1 - n, kdec, mod) * fact[dec1+kdec]*ifact[kdec]*ifact[dec1]) % mod
    if kdec:
      s = (s - pow(n,dec1+1,mod) * pow(1-n,kdec-1,mod) * fact[dec1+kdec]*ifact[kdec-1]*ifact[dec1+1]) % mod 
    kdec += 1 
  return (s*n) % mod


def F(n):
  global mod
  
  res = 0
  S = {0:0}
  for i in xrange(1,n+1):
    S[i] = numBoundedSeq(n,i)
    res = (res + i * (S[i] - S[i-1])) % mod
    while res < 0:
      res += mod
    
 # for k in xrange(n/2 + 1, n):
  #  if k == n-1:
   #   res = (res + k * 2 * (n-1) * n) % mod
   # else: 
    #  res = (res + k*(n - k - 1)*(n-1)*(n-1)*pow(n,n-k-1,mod)) % mod
     # res = (res + k * 2 * (n-1) * pow(n,n-k,mod)) % mod
  #Account for the n n-sequences with a value that is repeated n times
  return res % mod


print F(n)
