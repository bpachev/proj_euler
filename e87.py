import proj_euler as pe
from itertools import product

cap = 5*10**7
primes, mask = pe.primes_and_mask(int(cap**.5)+1)

psquares = []
pcubes = []
pfourths = []

for p in primes:
  if p**4 < cap:
    psquares.append(p*p)
    pcubes.append(p**3)
    pfourths.append(p**4)
    
  elif p**3 < cap:
    psquares.append(p*p)
    pcubes.append(p**3)
    
  elif p*p < cap:
    psquares.append(p*p)
  else:
    break
    
admissible = {}

for combo in product(psquares,pcubes,pfourths):
  s = sum(combo)
  if s < cap:
    admissible[s] = 1
    
print len(admissible)
