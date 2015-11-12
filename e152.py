from proj_euler import primes_and_mask,HarshadGen
from itertools import combinations,product
from fractions import Fraction as frac

def find_feasible(n,p):
 '''
 INPUTS:
 p -- a prime
 n -- a natural number, the cap
 RETURNS: a list of all sets (x1,...,xm) of natural numbers satisfying
 (i) 1<=xi<=n
 (ii) p|xi
 (iii) p^ord(p,prod(xi^2)) | sum i 1 to m, prod j not i (xj^2)
 NOTE: ord(p,k) is the exponent of p in the prime factorization of k
 '''
 yield ()
 r = range(1,n/p+1)
 sq=p*p
 for i in xrange(1,len(r)+1):
  for c in combinations(r,i):
   d = 1
   prod = 1
   for el in c:
    prod *= el*el*sq
    d *= sq
    while el%p == 0:
     d *= sq
     el/=p
   s = 0
   for el in c:
    s += prod/(el*el*sq)
   if not s%d:
    yield c

def solve(n):
 '''
 Solves PE problem 152.
 Finds all representations of 1/2 as the sum of distinct inverse squares with denominator at most n.
 For n = 45, the representations are: {2,3,4,6,7,9,10,20,28,35,36,45} and {2,3,4,6,7,9,12,15,28,30,35,36,45}, {2,3,4,5,7,12,15,20,28,35}
 '''

 excluded_primes = []
 cand_psets = []
  #HACK (sorry about this)
 sets = [5,7,13]
 for s in sets:
  cand_psets.append([])
  for st in find_feasible(n,s):
   if 13 not in st and 11 not in st:
    cand_psets[-1].append(set([s*el for el in st]))
 fdict1 = {}
  
 for set_comb in product(*cand_psets):
   finit = frac(0,1)
   for el in set_comb[0].union(set_comb[1].union(set_comb[2])):
      finit += frac(1,el*el)
   if finit in fdict1:
    fdict1[finit] += 1
   else:
    fdict1[finit] = 1
 total = 0
 rems = list(HarshadGen([2,3],n,exact=False))[2:]
 rems.remove(3)
 rems.remove(64)
 rems.remove(32)
 rems.remove(27)
 rems.remove(2*27)
 sf=frac(1,4)-frac(1,9)
 fracs = [sf]
 for el in rems:
  cfrac = frac(1,el*el)
  tf = []
  for f in fracs:
   t2 = f-cfrac
   if t2 in fdict1:
    total += fdict1[t2]
   tf.append(t2)
  fracs.extend(tf)
 return total 

print solve(80)
