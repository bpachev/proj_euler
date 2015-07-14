from proj_euler import gcd,prime_fact_ord
from bisect import bisect_right

h = []
cap = 10**12
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
exp2 = o2-o5 #Significant exponent of 2 in final product
h = sorted(h) #numbers divisible only by 2 and 5
print len(h)
res = 1 #init to one
for i in xrange(1,min(cap+1,mod)):
  if gcd(i,10) == 1:
    e = 0 #the exponent by i in the final product
    for m in h:
      if m*i > cap:
        break
      max_r = ((cap/m) - i) / mod #maximum r with m*(r*mod+i) <= cap
      e += max_r+1
    res = (res  * pow(i,e,mod)) % mod

res = (res * pow(2,exp2,mod)) % mod
print res
     
