import proj_euler as pe

n = 4
g = 13
cap = 10**10
#for n in xrange(4,cap):
#  if 3*n-g < 20:
#    print n,g,g%(n+1),g - 2*n
#  if g == 3*n:
#   print g,n
#  if not pe.gcd(n+1,g) == 1:
#    print n
#  g = g + pe.gcd(n+1,g)
#print g






last = 20
r = 10
while True:
#  print last,r
  n = last
  n_start = n
  g = 2*last + 2
  while n <= n_start + r:
    d = pe.gcd(n+1,g)
    g = g + d
    if d != 1:
      last = n
 #     print "Changing last to %d" % n
    n += 1
  diff = last - n_start
  print diff,last
#  print diff/float(last)
  if 2*last > cap:
    print 2*last + cap + 2
    break
  if last < 10**6:
    r = last ** .7
  else:
    r = 4*last ** .5
  last *= 2
    
