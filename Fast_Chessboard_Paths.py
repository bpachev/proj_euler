import numpy as np

def paths(n = 10**12-4,mod = 10**8):
#  Accum = np.eye(4).astype(int)
  T = np.array([[2,2,-2,1],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
  Accum = np.array([[8,4,1,1],[4,1,1,0],[1,1,0,0],[1,0,0,-1]])
  while n:
    if n % 2:
      Accum = np.remainder(T.dot(Accum),mod)
    T = np.remainder(T.dot(T),mod)
    n /= 2
  print Accum
  return Accum[0,0]

paths()
