cap = 10000

s = 0
for a in xrange(1,cap-1):
  t = 27*a**2 + (2*a-1)**3
  if t%27:
    continue
  m = t/27
  for b in xrange(cap-a-1,0,-1):
    if a + b + m / (b**2) > cap:
      continue
    if m % b**2 == 0:
      s += 1
print s

