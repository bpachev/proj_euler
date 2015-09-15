from scipy.integrate import quad
import numpy as np
from math import cos,sin,sqrt


def C(a,b):
 def f(x):
  c,s = cos(x),sin(x)
  d = a*a*c**2 + b*b * s**2
  return sqrt(((b*b-a*a)*s*c)**2 / d + d)
 return quad(f,0,2*np.pi)[0]

print C(1,4) + C(3,4)
 

