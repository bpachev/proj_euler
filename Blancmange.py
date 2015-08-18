from math import floor,pi
from matplotlib import pyplot as plt
import numpy as np

def blanc(x,it=60):
  if it <=0:
   return 0 #as far as a computer is concerned 
  if x > 1:
    x = x - floor(x)
  if x < 0:
    return blanc(-x)
  if x <= .5:
    return x + .5*blanc(2*x,it-1)
  else:
    return 1 - x + .5*blanc(2*x-1,it-1)

def int_blanc(x,it=60):
  if x > 1:
   return floor(x)*.5 + int_blanc(x-floor(x))
  if it <= 0:
   return 0
  if x < 0:
   return -1*int_blanc(-x)
  if x <= .5:
   return .25 * int_blanc(2*x,it-1) + x*x/2
  else:
   # 1/2 < x <= 1
   return .5 - int_blanc(1-x,it-1)

def plot_blanc(npoints=1000):
  X = np.linspace(0,1,npoints)
  Y = np.empty(npoints)
  for i in xrange(npoints):
   Y[i] = blanc(X[i])
  plt.plot(X,Y)
  plt.show()

def bin_blanc_search(a,b,f,tol=1e-10):
  m = (a+b)/2.
  d = f(m) - blanc(m)
#  print d,m,f(a)-blanc(,f(b)
  if abs(d) < tol:
    return m
  if d < 0: 
    return bin_blanc_search(a,m,f,tol)
  else:
    return bin_blanc_search(m,b,f,tol)


f = lambda x: .5 - (1./16 - (x-.25)**2)**.5
a = bin_blanc_search(0,.25,f)
b = .5
print int_blanc(b)-int_blanc(a)


