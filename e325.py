import numpy as np
import proj_euler as pe

def check(x,y):
    if x > 2*y: return False
    d = pe.gcd(x,y)
    x/=d
    y/=d
    its = 0
    while y > 1:
        if x >= 2*y : return its%2
        x -= y
        its += 1
        x,y = max(x,y), min(x,y)
#        print x,y
    return its%2


def solve(n):
  """
  Solve PE problem 325 for n.
  """
  tot = 0
  fibs = pe.fibb(n)
  print zip(fibs[1:-1], fibs[2:])
  cands = set()
  phi = (5**.5+1)/2
  for x in xrange(1,n+1):
    fl = int(x/phi)
#    tot += x*(x-fl-1) + (x*(x-1)-(fl)*(fl+1)) / 2
    tot += x*(-fl) + (-(fl)*(fl+1)) / 2

        #   for f1, f2 in zip(fibs[1:-1], fibs[2:]):
        #       if abs(f2*y-f1*x) == pe.gcd(x,y):
        #           cands.add((x,y))

  return tot + 3*pe.square_sum(n)/2 + pe.lin_sum(n)/2
print solve(10**4)
#print check(10,9)
