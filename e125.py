def is_palindrome(t):
  ts = str(t)
  return ts == ts[-1::-1]

seen =  set()
cap = 10**8
s = 0
for sq in xrange(1,int(cap**.5)+1):
  i = sq+1
  t = sq*sq + i*i  
  while t < cap:
    if is_palindrome(t) and t not in seen:
      s += t
      seen.add(t)
    i += 1
    t += i*i

print s
    
