import proj_euler as pe
#n is a bound on the sum
#maxVal is a strict upper bound on the tuple elements
#All tuple elements are distinct
def boundedTuples(n,maxVal):
  if maxVal == 1 or not n:
    return [[]]
  
  l = []
  for mVal in xrange(1,min(n+1,maxVal)):
    for t in boundedTuples(n-mVal,mVal):
      l.append([mVal] + t)
  return l

cache = {}

def countBoundedTuples(n,maxVal,minVal=1):
  global cache
  if maxVal == minVal or not n:
    return 1
  if (n,maxVal) in cache:
    return cache[(n,maxVal)]
  s = 0
  for mVal in xrange(minVal,min(n+1,maxVal)):
    s += countBoundedTuples(n-mVal,mVal,minVal)
  cache[(n,maxVal)] = s
  return s

cap = 6
primes = pe.primes_and_mask(cap)[0]

def enum_periods(a,n):
# print a,n
 s = 0
 for i,d in enumerate(a):
  if d > n:
    return s
  e = d
  while e <= n:
    s += (1 + enum_periods(a[i+1:],n-e))
    e *= d
 return s

cache = {}
def coprime_hack(n,maxp=10**10):
  global cache,primes
  bound = min(n,maxp-1)
  if (n,bound) in cache:
   return cache[(n,bound)]
  s = 0
  if bound < 2:
    return 1
  for p in primes:
   if p <= bound:
     e = p
     while e <= bound:
       s += coprime_hack(n-e,p)
       e *= p
  return s
print coprime_hack(cap),enum_periods(primes,cap)
