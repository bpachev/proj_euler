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

print countBoundedTuples(350,30)
