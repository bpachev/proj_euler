#the number of ways a number can be written as sums of powers of two with no power used more than twice
def f(n):
  if not n:
    return 0
  if n == 1:
    return 1
  elif n%2:
    return f(n/2)
  
  e = 0
  while n%2 == 0:
    n /= 2
    e += 1
  if n == 1:
    return e+1
  return e*f(2*(n/2)) + f(n/2)

print f(10**25)
