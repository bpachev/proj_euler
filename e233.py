import numpy as np
import proj_euler as pe

#420 = 4*105 = 4*105 = 4*5*3*7
#Hence if r(2,n) = 105, and p1^a1*...*pn^an is the part of n consisting of primes congruent to 1 (4)
# then B = (a1+1)*..*(an+1) = 210, or 211 or 213 (given suitable constraints on the power of 2 in the prime factorization of n)
#However, 211 is prime, and 213 = 71*3, so for decently small caps no n exists with such a factorization

#For my cap of interest (10^11), powers greater than 16 are impossible
#Hence B is decomposed as  6*7*5,2*3*5*7, 14*15,14*3*5,15*2*7,10*5*7 Subtracting 1 from each number in the preceding factorizations . . .

#Forget the above comments, I re-read the description and the problem is different than I thought.

#cap = 10**22
#cap = 10**11
cap = 10**11
#pCap = 10**6
pCap = cap/(5**3*13**2)
badpCap = cap/(5**3*13**2*17)	
mask = np.ones(pCap).astype(int)
mask[0] = 0
mask[1] = 0
goodPrimes = [] #congruent to 1 mod 4
badPrimes = [] #congruent to 3 mod 4
for i in xrange(pCap):
  if mask[i]:
    if i%4 == 1:
      goodPrimes.append(i)
    if i%4 == 3 and i <= badpCap:
      badPrimes.append(i)
    j = i*i
    while j < pCap:
      mask[j] = 0
      j += i

def boundedPrimeProducts(plist,cap):
  yield 1
  for i,p in enumerate(plist):
   a = p
   while a < cap:     
     for prod in boundedPrimeProducts(plist[i+1:],cap/a):
       yield a*prod
     a *= p

print "Done with Prime Sieve"
muls = sorted(list(boundedPrimeProducts(np.array([2]+badPrimes),pCap)))
print "Done with muls"

#has the property that prod(element+1) = 105
#twoTuples = [(34,2),(14,6),(20,4)]
#threeTuples = [(6,4,2)]
twoTuples = [(17,1),(7,3),(10,2)]
threeTuples = [(3,2,1)]


s = 0

for t in twoTuples:
  for p1 in goodPrimes:
    f1 = p1**t[0]
    if f1 > cap:
      break
    for p2 in goodPrimes:
      if p2 == p1:
        continue
      f2 = p2**t[1]
      F = f1*f2
      if F > cap:
        break

      for m in muls:
        if m*F > cap:
          break
        s += F*m
      

for t in threeTuples:
  for p1 in goodPrimes:
    f1 = p1**t[0]
    if f1 > cap:
      break
    for p2 in goodPrimes:
      if p2 == p1:
        continue
      f2 = p2**t[1]
      if f2*f1 > cap:
        break
      for p3 in goodPrimes:
        if p3 == p1 or p3 == p2:
          continue
        f3 = p3**t[2]
        F = f1*f2*f3
        if F > cap:
          break
        
        for m in muls:
          if m*F > cap:
            break
          s += F*m

print s
  
