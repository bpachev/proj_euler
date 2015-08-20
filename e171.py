from itertools import combinations

d = 20
mod = 10**9
fact = [1]
for i in xrange(1,d+1):
 fact.append(fact[-1]*i)

C = lambda n,k : fact[n]/fact[k]/fact[n-k]
one_sum = [0] #k-th member is the sum of all nums < 10^d with k digits 1, and the rest 0
geo = ((10**20 -1)/9) % mod
for i in xrange(d):
 one_sum.append(geo*C(n-1,i-1))


squares = set(i*i for i in xrange(int((9*9*d)**.5)+1))
s = 0

for c in combinations(range(20),10):
  sq_sum = 0
  for i in xrange(1,10):
    sq_sum += (c[i]-c[i-1])*i*i
  if sq_sum not in squares:
    continue

    
  


