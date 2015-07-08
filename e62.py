import itertools

cap = 10**4
cubes = np.array([k*k*k for k in xrange(1000,cap)])


def permu(a,b):
  d1 = map(int,list(str(a)))
  d2 = map(int,list(str(b)))
  if not len(d2) == len(d1):
    return False
  for i in xrange(10):
    n1 = 0
    n2 = 0
    for j in xrange(len(d2)):
      if d2[j] == i:
        n2 += 1
      if d1[j] == i:
        n1 += 1
    if not n1 == n2:
     return False
  return True

print permu(41063625,41063625)

for i in xrange(1000,cap):
  n = 0
  for j in xrange(i,cap):
    if permu(cubes[i],cubes[j]):
      n += 1
  if n > 3:
    print str(c1) + " " + str(n)
