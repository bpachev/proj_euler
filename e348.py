from proj_euler import is_palindrome
cap = 10**9

cache = {}
#print is_palindrome(456)
for sq in xrange(int(cap**.5)+1):
  t = sq*sq
  for cube in xrange(int((cap-sq)**(1./3))+1):
    c = cube**3
    if not is_palindrome(t+c):
      continue
    if t+c not in cache:
      cache[t+c] = 1
    else:
      cache[t+c] += 1
s = 0
for k in cache:
  if cache[k] == 4:
    print k
    s += k
print "Sum: %d" % s

