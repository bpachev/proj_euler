from fractions import gcd
from itertools import combinations
cap = 1000
pairs = {i:[] for i in xrange(cap)} #p and q s.t. p*p+p*q+q*q is a square

#According to http://www.had2know.com/academics/integer-triangles-120-degree-angle.html
#the generating formula is m and n with p = m^2-n^2 and q = 2*m*n + n^2, m > n
# sqrt(p^2+p*q+q^2) = m^2+m*n+n^2

for m in xrange(1,int(cap**.5)):
 sm = m*m
 for n in xrange(1,m):
  p,q = sm-n*n,2*m*n+n*n
  if p+q < cap:
   pairs[p].append(q)
   pairs[q].append(p)
   print p,q
print pairs[195],pairs[264],pairs[325]
for p in pairs:
 for q,r in combinations(pairs[p],2):
  if q in pairs[r] or r in pairs[q]:
   print p,q,r,p+q+r
  

