tot = {}
d = 8
for i in xrange(d):
  tot[5**(8-i)*2**(8+i)] = 5**(8-i-1)*2**(8+i+1)

for i in xrange(1,2*d+1):
  tot[2**i] = 2**(i-1)

tot[1] = 1

def hyper(a,b,mod):
  global tot
  if b == 1:
    return a % mod
  
  if mod == 1:
    return 0
  
  r = hyper(a,b-1,tot[mod])
  return pow(a,r,mod)

print hyper(1777,1855,10**8)

