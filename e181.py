cache = {}
def g(bound,n):
  global cache
  if bound[0] > n[0]:
    bound = n
  t = (bound,n)
  if t in cache:
    return cache[t]
  
  if n == (0,0):
    return 1
  elif bound == (0,0):
    return 0
  s = 0
  for W in xrange(min(bound[0],n[0])+1):
    for B in xrange(n[1]+1):
      if not W and not B:
        continue
      if W == bound[0]:
       if B > bound[1]:
        break
       else:
        s += g((W,min(bound[1],B)),(n[0]-W,n[1]-B))
      else:
       s += g((W,B),(n[0]-W,n[1]-B))
  
  cache[t] = s
  return s
n = (60,40)
print g(n,n) 
