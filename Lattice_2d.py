import numpy as np

def lattice2d(a,b,sigma = 3./4):
  '''
  INPUTS: a and b, two numpy arrays with integer entries, both of the same length.
  RETURN the magnitude of the integer linear combination of a and b with shortest length.
  '''
  while True:
    b_mag = np.inner(b,b)
    mu = np.inner(a,b)/np.inner(b,b)
    if abs(mu) > .5:
      a = a - int(mu)*b
      mu = np.inner(a,b)/np.inner(b,b)
    a_star = a - mu*b
    if np.inner(a_star,a_star) < (sigma - mu*mu)*b_mag:
      a,b = b,a
    else:
      print a
      print b
      return np.sum(np.abs(b))
    


print lattice2d(np.array([-1, 3, 28]), np.array([-11, 125, 40826]))
