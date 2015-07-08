import proj_euler as pe
import numpy as np

#cap = 100000000
cap = 1000000
s = 0
op = 0

primes,mask = pe.primes_and_mask(cap)

factorDict = {}
for p in primes:
  j = 2*p
  while j <= cap:
    if mask[j-1]:
      t = j
      e = 0
      while t % p == 0:
        t /= p
        e += 1
      if j not in factorDict:
        factorDict[j] = [(p,2*e)]
      else:
        factorDict[j].append((p,2*e))
    j += p

factorDict[3] = [(3,2)]

nump = len(primes)
print "nump: " + str(nump)

#print factorDict
 
def factorGenerator(n):
  global primes
  t = n
  for i, p in enumerate(primes):
    if p*p > t:
      if t > 1:      
        yield (t,2)
      return 
    exp = 0
    while not t % p:
      t /= p
      exp += 1
    if exp:
     yield (p, 2*exp)
 
  
def divisorGen(n):
    global factorDict
#    factors = list(factorGenerator(n))
    factors = factorDict[n]
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
  
print list(factorGenerator(48))

for i, p in enumerate(primes):
  b1 = p + 1
  if not i % 10**4:
    print "On " + str(i) + "th prime, sum: " + str(s)
  for d in divisorGen(b1):
    k = b1*b1/d
    if k <= cap and d <= cap and not d == b1:
      if mask[d-1]:
        if mask[k-1]:
          s += b1 + d + k - 3
print s/2


#primes = np.array(primes)

#for i in xrange(nump-2):
 # a1 = primes[i] + 1
  #j = i + 1
  #while True:
   # if j == nump:
    #  break
   # b1 = primes[j] + 1
    #c1 = (b1*b1)/float(a1)
   # j += 1
    #if c1 > cap:
     # break
    #if (b1*b1) % a1:
     # continue
    #if not mask[int(c1) - 1]:
     # continue
    #else:
     # s += a1 + b1 + c1 - 3
  #op += j-i

print s
