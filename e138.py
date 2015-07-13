from proj_euler import isqrt

def is_sq(L):
  t = isqrt(L)
  if t*t == L:
    return True
  else:
    return False

s = 0
n = 1
m = 13
b = 16
sols = [1]
while True:
  t1 = (b*b*5)/4 + 1 + 2*b
  t2 = t1 - 4*b
  if is_sq(t1):
    L = isqrt(t1)
    s += L
    print L,b
    sols.append(b)
    n+=1
    if n%2==0:
      b = (b*sols[-1])/sols[-2]
    else:
      b = (b*sols[-2])/sols[-3]
    continue
  if n==m:
    print str(s) + " foo"
    break
  if is_sq(t2):
    L = isqrt(t1)
    s += L
    print L,b
    sols.append(b)
    n+=1
    if n%2==0:
      b = (b*sols[-1])/sols[-2]
    else:
      b = (b*sols[-2])/sols[-3]
  if n==m:
    print str(s) + " foo"
    break
  b += 2

print s
