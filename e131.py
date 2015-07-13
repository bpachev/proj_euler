from proj_euler import MillerRabin

cap = 10**6

s = 0
for i in xrange(1,cap):
  d = (i+1)**3 - i**3
  if d >= cap:
    break
  if MillerRabin(d):
    s += 1

print s
  
