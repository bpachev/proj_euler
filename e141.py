from fractions import gcd
n = 10**12

squares = set()

for i in xrange(int(n**.5)):
  squares.add(i*i)
s = 0
res = set()
for x1 in xrange(1,int(n**(1./4)) + 1):
  for x2 in xrange(x1+1,int( ((n-x1*x1)/float(x1))**(1./3) ) + 1):
    if not gcd(x1,x2) == 1:
      continue
    r = 1
    while True:
      t = r*x1*x1 + x2**3 * x1 * r*r
      if t > n:
        break
      if t in squares:
        res.add(t)
        print t
      r += 1

print sum(res)
