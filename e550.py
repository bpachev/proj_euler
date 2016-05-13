import numpy as np
import proj_euler as pe
from itertools import product
from CR_NEWTON_LAGRANGE import Lagrange_cr as cr

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

def count_representatives(c, n, pcounts, primes, excluded=set(), upper = None):
    """
    How many numbers with a given type of prime factorization less than n
    """
    if n == 0: return 0
    if len(c) == 1:
        if not c[0]: return 1
        new_n = int(n**(1./c[0]))
        if not new_n**c[0] <= n: print "Too big"
        elif not (new_n+1)**c[0] > n:
            new_n += 1

        if upper is not None:
            new_n = min(upper, new_n)
        return pcounts[new_n] - sum([1 if el <= new_n else 0 for el in excluded])


    tot = 0
    for p in primes:
        new_n = n / p**c[0]
        if not new_n:
            break
        if upper is not None and p >= upper:
            break
        if p in excluded: continue
        excluded.add(p)
        if c[1] == c[0]: tot += count_representatives(c[1:], new_n, pcounts, primes, excluded, p)
        else: tot += count_representatives(c[1:], new_n, pcounts, primes, excluded)
        excluded.remove(p)

    return tot

def class_divides(d, n):
    for el1, el2 in zip(d, n):
        if el1 > el2:
            return False
    return True

def mex(l):
    l = sorted(list(l))
    for i, el in enumerate(l):
        if el > i: return i
    return len(l)

if __name__ == "__main__":
    #print factor_num_to_nimber(23)
#    n = 32
#    k = 5
    n = 10**7
    k = 10**12
    mod = 987654321
    m1,m2 = 379721, 3**2*17**2
    assert m1*m2 == mod
    primes, mask = pe.primes_and_mask(n)
    pcounts = np.cumsum(mask.astype(np.int32))
    classes = pe.prime_equivalences(n)[0]
    classes.sort(key = lambda c: sum(c))
    nimber_cache = {}
#    print pcounts
    tot = 0
    for i,c in enumerate(classes):

#        tot += count_representatives(c[:first_zero], n, pcounts, primes)
        divs = []
        for e in classes[:i]:
            if class_divides(e, c):
                divs.append(nimber_cache[tuple(e)])

        vals = set()
        for d1, d2 in product(divs, divs):
            vals.add(d1^d2)
        nimber_cache[tuple(c)] = mex(vals)


    nnimbers = max(nimber_cache.values())
    nbits = len(bin(nnimbers - 1))-1
    nstates = 2**nbits
#    print nstates, nnimbers, nbits, nimber_cache.values()
    init = np.zeros(nstates, dtype = np.int64)
    for c in nimber_cache:
        first_zero = len(c)
        for j, el in enumerate(c):
            if el == 0:
                first_zero = j
                break
        inc = count_representatives(c[:first_zero], n, pcounts, primes)
        print inc, c, nimber_cache[c]
        init[nimber_cache[c]] += inc
    print init, np.sum(init)
    T = np.zeros((nstates, nstates), dtype = np.int64)
    for start in xrange(nstates):
        for transition in xrange(nstates):
            T[transition^start, start] += init[transition]
#    print T
    rems = []
    for mod in (m1,m2):
        res = pe.matrix_mod_exp(k-1, T, init, mod)
        rems.append((np.sum(res)-res[0]) % mod)
    print cr(rems, (m1,m2))
#    print tot, n

#solve(30,10**12,987654321)
