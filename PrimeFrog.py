#Project euler problem 329 "Prime Frog"

import proj_euler as pe
import numpy as np
cap = 500
croaks = "PPPPNNPPPNPPNPN"
#croaks = "PP"
max_depth = len(croaks)
denom = 500*6**max_depth/2
print "Total possibilities: " + str(denom)

primes,mask = pe.primes_and_mask(cap)

curr = np.ones(cap,dtype=np.int64)
for croak in croaks:
  prev = curr
  curr = np.ones(cap,dtype=np.int64)
  #Count croaks multiplicities. For each path on a prime, P gets croaked twice
  #For each on a non-prime, N gets croaked twice
  if croak == "P":
    for i in xrange(cap):
      if mask[i+1]:
        prev[i] *= 2
  else:
    for i in xrange(cap):
      if not mask[i+1]:
        prev[i] *= 2
  
  #compute transitions
  curr[1:cap-1] = prev[:cap-2] + prev[2:cap]
  curr[0] = prev[1]
  curr[cap-1] = prev[cap-2]
  #double count the contributions from the end squares
  curr[1] += prev[0]
  curr[cap-2] += prev[cap-1]   
num = np.sum(prev)   
print "Total admissible possibilities " + str(num)

d = pe.gcd(denom,num)
print "Reduced fraction " + str(num/d) + "/" + str(denom/d)

