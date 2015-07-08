import math
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
        

s = 0
e = math.exp(1)
for i in xrange(5,10000+1):
  n1 = math.floor(i/e)
  n2 = n1 + 1
  if not n1:
    n1 = .1
  m = 0
  if n1 * (math.log(i) - math.log(n1)) > n2 * (math.log(i) - math.log(n2)):
    m = n1
  else:
    m = n2
  m /= egcd(i,m)[0]
  while not m % 2:
    m /= 2
  while not m % 5:
    m /= 5
  if m == 1:
    s -= i
  else:
    s += i
    
print s
