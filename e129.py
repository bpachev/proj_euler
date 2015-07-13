from proj_euler import MillerRabin

cap = 10**6

r = 10**3 #search range (experimental)

divs = {i:[i] for i in xrange(cap,cap+r)}

#A function written because I'm too lazy to sieve for the totients
#I've already computed the divisors of n, why not use them to get the totient?
def tot_from_divs(n,divs):
  if len(divs) <= 1:
    return n-1 #prime
  pList = []
  t = 1
  for d in divs:
    f = 1
    for p in pList:
      if d %p == 0:
        f = 0
        break
    if not f:
      continue #Not a prime divisor
    
    pList.append(d)
    if n%d:
      print "ERROR: %d not a divisor of %d" % (d,n)
    n /= d
    t *= (d-1)
    while n % d == 0:
      n /= d
      t *= d
  return t


for div in xrange(2,(cap+r)/2):
  for i in xrange(div*(cap/div),cap+r,div):
    if i in divs:
      divs[i].append(div)
f = 1
for i in xrange(cap,cap+r):
    t = tot_from_divs(i,sorted(divs[i]))
    if i % 3 == 0:
      o = 1
      temp = i
      while not temp %3:
        temp /= 3
        o *= 3
      t_new = (t*3) / 2
      t_real = (((t*3)/2)/o)
      if t_new < cap:
        continue
      A = 0
      for div in sorted(divs[t_new]):
        if t_real % div:
          continue
        if pow(10,div,i/o) == 1:
          A = div
          break
      if o*A > cap:
          print "Answer %d" % i
          f = 0
      
    if t < cap:
      continue
    for div in sorted(divs[t]):
      if pow(10,div,i) == 1:
         if div > cap:
           print "Answer %d" % i
           print t
           f = 0
           break
         else:
#           print "A(%d) = %d" % (i,div)
           break
    if not f:
      break
