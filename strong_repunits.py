cap = 10**12

sr = set()

for i in xrange(2,int(cap**.5)+1):
  t = i**2 + i + 1
  if t >= cap:
    break
  while t < cap:
    sr.add(t)
    t = i*t +1

print 1+sum(sr)

