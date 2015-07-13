from proj_euler import MillerRabin

s = 0
cap = 5*10**7
for i in xrange(2,cap):
  if MillerRabin(2*i*i-1):
    s += 1

print s

