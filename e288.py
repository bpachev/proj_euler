p = 61
mod = 61**10

seed = 290797
T = seed
ms = 50515093
s = 0
coeff = 0
n = 10**7

for i in xrange(n):
  coeff = (1 + p*coeff) % mod
  T = (T*T) % ms
  temp = T % p
  s = (s +(coeff * temp)) % mod
print s
