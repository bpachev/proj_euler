import math

m = 0
d = 0
s = 0
for n in xrange(2,1001):
  R = int(math.floor(n**.5))
  if R*R == n:
    continue
  h = R
  k = 1
  h1 = 1
  h2 = 0
  k1 = 0
  k2 = 1
  P = 0
  Q = 1
  a = R
  i = 0
  while True:
    h = a*h1 + h2
    k = a *k1 + k2
    h2 = h1
    k2 = k1    
    k1 = k
    h1 = h	  
    P = a*Q - P
    Q = (n - P*P) / Q
    a = int(math.floor((R+P)/Q))
    i += 1
    if h**2 - n*k**2 == 1:
      if h > m:
        m = h
        d = n
      break
print m
print d
