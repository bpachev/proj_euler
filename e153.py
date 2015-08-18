from proj_euler import FareyGen

cap = 10**8
sq = int(cap**.5)
cache = {0:0}

def T(n):
 return (n*(n+1)) / 2

def sum_sofd_slow(n,cap=True):
  global cache
  if n in cache:
    return cache[n]
  sq = int(n**.5)
  s = 0
  for i in xrange(1,n/(sq+1)+1):
   s += i*(n/i)
  
  for k in xrange(1,sq+1):
   s += k*((n/k)*(n/k+1)/2 - (n/(k+1))*(n/(k+1)+1)/2)
  cache[n] = s
  return s



s = sum_sofd_slow(cap)

for a,b in FareyGen(sq):
    s += 2*(a+b)*sum_sofd_slow(cap/(a*a+b*b))
s += 2*sum_sofd_slow(cap/(2))

    
print s
