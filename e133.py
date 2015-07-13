from proj_euler import primes_and_mask

cap = 10**5

primes,mask = primes_and_mask(cap)

pDivDict = {p:[1] for p in primes}
for i in xrange(2,cap):
  j = i
  while j < cap:
    if mask[j+1]:
      pDivDict[j+1].append(i)
    j += i

#IF p =5, 10^n never is 1 mod p!!!!!
s = 5 #account for 2 and 3
for p in primes:
  if p == 2:
    continue
  s += p
  for div in sorted(pDivDict[p]):
    if pow(10,div,p) == 1:
      t = div
      while not t % 5:
        t  /= 5
      while not t % 2:
        t /= 2
      if t == 1:
        s -= p
        break
print s
      
