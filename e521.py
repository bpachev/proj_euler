import proj_euler as pe
import timeit
import numpy as np
from bisect import bisect_left
import sys

cap = 10**int(sys.argv[1])
mP = min(5*10**7,int(cap**(2./3)))
primes,mask = pe.primes_and_mask(mP)

NP =  len(primes)

print "NUMP " +str(NP)
print "PCAP " + str(mP) 

f = lambda n : n*(n+1) / 2 

s = f(cap)

def prods(prod,sign, startNum,primes,NP):
  global s,cap
  if prod > cap:
    return
  
  for i in xrange(startNum,NP):
    if primes[i] > cap/prod:
      break  
    s += sign * (prod*primes[i] * f(cap/(prod*primes[i])) - primes[i] * (cap/(prod*primes[i])))
    prods(prod*primes[i], -1*sign,i+1,primes,NP)
  return
  

def pi(n):
  global NP
  pos = bisect_left(primes,n)
  if pos == NP:
    return NP
  return pos+1 if primes[pos] == n else pos


#for i, p in enumerate(primes):
 # s -= p * (f(cap/p) - cap/p)
  #for j in xrange(1,i+2):
   # for c in combinations(primes[:i],j):
    #  a = p
     # for x in c:
      # a *= x
      #s += (-1) ** (j-1) * (a*f(cap/a) - p*(cap/a))
#prods(1,-1,0,primes[:pi(int(cap**.5))],pi(int(cap**.5)))
print s-1
s = f(cap) - 1
d = pi(cap/mP)
#print d
#print mP
start = timeit.default_timer()
prods(1,-1,0,primes[:d],d)
print timeit.default_timer()-start
for i in xrange(d,NP):
  if primes[i] > cap/primes[i]:
    break
#  print primes[i]
  up = pi(cap/primes[i])
  lo  = i
#  print "up " + str(up) + " lo " + str(lo)
  pSum = sum(primes[lo:up])
#  print "PSum " + str(pSum)
#  print (primes[i]*pSum - primes[i]*(up - lo + 1))  
  s -= (primes[i]*pSum - primes[i]*(up - lo)) 
  
print s%10**10

