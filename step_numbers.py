cache={}
def f(d,l,has_0,has_9):
 global cache
 if d<0 or d>9:
  return 0
 if d==0:
  has_0=True
 elif d==9:
  has_9=True  
 if l==1:
  if has_0 and has_9:
   return 1
  else:
   return 0
 t=(d,l,has_0,has_9)
 if t in cache:
  return cache[t]
 res=f(d+1,l-1,has_0,has_9)+f(d-1,l-1,has_0,has_9)
 cache[t]=res
 return res
def g(n):
 return sum([f(i,n,False,False) for i in xrange(1,9)])+f(9,n,False,True)
def solve(n):
 print [g(i) for i in xrange(1,n+1)]
 return sum([g(i) for i in xrange(1,n+1)])
print solve(40)
