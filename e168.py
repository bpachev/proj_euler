r=0
for n in xrange(1,100):
 for k in xrange(1,10):
  for c in xrange(1,10):
   t = (10**n-c)*k  
   d = 10*c-1
   if t%d==0:
    if (t/d) < 10**(n-1):
     continue
#    print (10*t/d+k),c,n,c*(10*t/d+k)
    r+=(10*t/d+k)
print r
print r%10**5
