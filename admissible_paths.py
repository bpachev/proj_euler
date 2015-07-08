from itertools import product

sq = set()
bsq = set()
psq = {}
CAP = 1000

fact = {}
ifact = {}
fact[0] = 1
ifact[0] = 1
mod = 1000000007

for j in xrange(1,2*CAP+1):
  fact[j] = (j * fact[j-1]) % mod
  ifact[j] = (pow(j,mod-2,mod) * ifact[j-1]) % mod

for i in xrange(1,int((2*CAP)**.5)+1):
  bsq.add(i*i)
  if i*i <= CAP:
   sq.add(i*i)
  
for p in product(sq,sq):
  q = p[0]+p[1]
  if q in bsq:
    if q in psq:
      psq[q].append(p)
    else:
     psq[q] = [p]

print psq
