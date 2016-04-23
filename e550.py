import numpy as np
from proj_euler import matrix_mod_exp
from itertools import product

def num_factor_sieve(n):
  res = np.zeros(n+1, dtype = int)
  for i in xrange(2,n+1):
    if res[i] > 0:
      continue
    for j in xrange(i,n+1,i):
      t = j
      while t%i == 0:
        t /= i
        res[j] += 1
  return res

def solve(n,k,mod):
  sieve = num_factor_sieve(n)
  print sieve
  nimber_counts = np.bincount(sieve)[1:]
  nnimbers = len(nimber_counts)
  nbits = len(bin(nnimbers - 1))-2
  nstates = 2**nbits
  init = np.zeros(nstates, dtype = np.int64)
  init[:nnimbers] = nimber_counts
  T = np.zeros((nstates, nstates), dtype = np.int64)
  for start in xrange(nstates):
   for transition in xrange(nstates):
     T[transition^start, start] = init[transition]
  res = matrix_mod_exp(k-1, T, init, mod)
  print res, np.sum(res)-res[0]

def factor_num_to_nimber(n):
  l = [0]
  for j in xrange(1,n):
   next = 0
   v = []
   for el1, el2 in product(l,l):
     v.append(el1^el2)
   v.sort()
   for i, el in enumerate(v):
     next = el+1
     if el > i:
      next = i
      break
   l.append(next)
  
  return l
   
print factor_num_to_nimber(23)

#solve(30,10**12,987654321)
