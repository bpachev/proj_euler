from proj_euler import primes_and_mask
from proj_euler import MillerRabin
import sys

primes,mask = primes_and_mask(10**4)


def concat(a,b):
  return int(str(a)+str(b))

def slower_is_prime(n):
  global primes
  for p in primes:
    if p*p > n:
      return 1
    if not n % p:
      return 0
  return 1

prime_dicts = {p:set() for p in primes}

for p1 in primes:
  for p2 in primes:
    if MillerRabin(concat(p1,p2)) and MillerRabin(concat(p2,p1)):
      prime_dicts[p1].add(p2)
best_sum = 10**20

for p1 in primes:
  for p2 in primes:
    if p2 >= p1:
     break
    i = prime_dicts[p1].intersection(prime_dicts[p2])
    if len(i) and p2 in prime_dicts[p1]:
       for p3 in i:
         j = i.intersection(prime_dicts[p3])
         if len(j) <= 1:
           continue
         for p4 in j:
           for p5 in j.intersection(prime_dicts[p4]):
             s = p1 + p2 + p3 + p4 +p5 
             if s < best_sum:
               print s
               print p1,p2,p3,p4,p5
               best_sum = s

print best_sum 

#chains = [[3,7]]
#induct on chain length
#for i in xrange(3,5):
 #chains_new = []
 #for p in primes:
  # for chain in chains:
   #  match = 1
    # for c in chain:
     #  if not MillerRabin(concat(c,p)) or not MillerRabin(concat(p,c)):
      #   match = 0
       #  break
     #if match:
      # chains_new.append(chain + [p])
 #print chains_new
 #chains = chains_new
 
#primes,mask = primes_and_mask(10**6)

#print len(primes)

#for chain in chains:
 # for prime in primes:
  #   match = 1
   #  for c in chain:
    #   if not MillerRabin(concat(c,p)) or not MillerRabin(concat(p,c)):
     #    match = 0
      #   break
    # if match:
     #  print chain + [p]
  
