cache={}
def count_hex(n,hasA=False,has1=False,has0=False):
 if hasA and has1 and has0:
  return 16**n
 elif not n:
  return 0
 if (n,hasA,has0,has1) in cache:
  return cache[(n,hasA,has0,has1)]
 t = 13*count_hex(n-1,hasA,has1,has0)+count_hex(n-1,True,has1,has0)+count_hex(n-1,hasA,True,has0)+count_hex(n-1,hasA,has1,True)
 cache[(n,hasA,has0,has1)]=t
 return t

s=0
for i in xrange(16):
 s += count_hex(i,hasA=True)+13*count_hex(i)+count_hex(i,has1=True)
print str(hex(s)).upper()[2:]
  
