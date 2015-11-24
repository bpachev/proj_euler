cache = {}
def f(s,n,l):
 if (s,n,l) in cache:
  return cache[(s,n,l)]
 if s == 0:
  if l==0:
   return 1
  else:
   return 0
 if s < 0:
  return 0
 if l <= 0 and s > 0:
  return 0
 if n<=0 and s > 0:
  return 0
 t=0
 for i in xrange(1,n+1):
  t += f(s-i*i,i-1,l-1)
 cache[(s,n,l)] = t
 return t

def solve(n,k):
 max_sum = sum([i*i for i in xrange(n-k+1,n+1)])
 dist_sums = 0
 for s in xrange(1,max_sum+1):
  n_occurs = f(s,n,k)
  if n_occurs == 1:
   dist_sums += s
 return dist_sums
for i in xrange(1,51):
 print solve(100,i),i
# tcache = {}
 #for c in cache:
  #if c[2] == i:
   #tcache[c]= cache[c]
 #del cache
 #cache = tcache
