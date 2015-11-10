from proj_euler import HarshadGen, MillerRabin,shanks_factorize

n=2*10**7
ord2 =0
t =n
res=i
l = []
for i in xrange(11):
 for j in xrange(7):
  t = 5**j*2**i
  if MillerRabin(t+1) and :
   l.append(t+1)
print l, len(l)
