import proj_euler as pe

N = 50
primes = pe.primes_and_mask(N)[0]

def comb_squarefree(n,k):
  global primes
  for p in primes:
    t = pe.prime_fact_ord(p,n)-pe.prime_fact_ord(p,n-k)-pe.prime_fact_ord(p,k)
    if t > 1:
      return 0
  return 1

s = set()
prev = [0 for i in xrange(N+1)]
curr = []
for i in xrange(N+1):
  curr = [1]
  for j in xrange(N):
   curr.append(prev[j]+prev[j+1])
   if curr[-1] and comb_squarefree(i,j+1):
     s.add(curr[-1])
  prev = curr

print sum(s)      
