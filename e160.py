from proj_euler import gcd,prime_fact_ord
from bisect import bisect_right

h = []
cap = 20
mod = 10**5

t = 1
while t <= cap:
  t5 = 1
  while t*t5 <= cap:
    h.append(t*t5)
    t5 *= 5
  t *= 2
    
o2 = prime_fact_ord(2,cap)
o5 = prime_fact_ord(5,cap)

for i in xrange(1,min(cap+1,mod)):
  
