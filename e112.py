import math
import numpy as np

def isBouncy(x):
  ds = np.array([int(d) for d in str(x)])
  temp = np.argsort(ds)
  if (np.array_equal(ds[temp], ds)):
    return False
  if (np.array_equal(ds[temp[::-1]],ds)):
    return False
  return True
  
def problem112( p = .90):
  bouncy_numbers = 0
  x = 100
  while True:
    if (isBouncy(x)):
      bouncy_numbers += 1
    if float(bouncy_numbers)/x >= p:
      print float(bouncy_numbers)/x
      return x
    x += 1


print problem112(.99)  