import numpy as np
from math import acos,sin,cos,ceil
from matplotlib import pyplot as plt
from scipy.integrate import odeint,quad


def path_len(nbots=3,rinit=.999,niter = 100,delta=2*np.pi/1000,d2=10,tol=1e-6):
 hinit = (1-rinit**2)**.5
 pos = np.array([rinit,0,hinit])
 theta = 2*np.pi/nbots
 ct,st = np.cos(theta),np.sin(theta) 
 rotarr = np.array([[ct,st],[-st,ct]])
 p2 = np.zeros(3)
 plen = 0.
 i=0
 while abs(1.-pos[2]) > tol and i < niter:
  p2[:2] = rotarr.dot(pos[:2])
  p2[2]  = pos[2]
  d = pos.dot(p2)
  ang = abs(acos(d))/d2
  plen += ang
  p2 = p2-d*pos #orthogonalize
  p2 = p2/p2.dot(p2)**.5 #normalize
  pos = cos(ang)*pos + sin(ang)*p2
  i += 1
 print i,pos,pos.dot(pos)
 return plen

def path_len2(nbots=3,rinit=.999,niter = 100,delta=.001):
 hinit = (1-rinit**2)**.5
 pos = np.array([rinit,0,hinit])
 theta = 2*np.pi/nbots
 ct,st = np.cos(theta),np.sin(theta) 
 rotarr = np.array([[ct,st],[-st,ct]])
 p2 = np.zeros(3)
 plen = 0.
 while abs(1.-pos[2]) < delta:
  p2[0] = ct*pos[0]
  p2[1] = st*pos[0]
  p2[2]  = pos[2]
  p2 = p2-pos.dot(p2)*pos #orthogonalize
  p2 = p2/p2.dot(p2)**.5 #normalize
  pos[2] += delta
  pos[0] = (1-pos[2])**.5	
  plen += delta/p2[2]
  
 print pos
 return plen

def path_len3(nbots=3,rinit=.999,tol=1e-6,l=1000):
 hinit = (1-rinit**2)**.5
 pos = np.array([rinit,0,hinit])
 theta = 2*np.pi/nbots
 ct,st = np.cos(theta),np.sin(theta) 
 rotarr = np.array([[ct,st],[-st,ct]])
 plen = 0
 def xfunc(pos,t):
  p2 = np.zeros(3) 
  if abs(1-pos[2]) < 1e-7:
   return p2  
  p2[:2] = rotarr.dot(pos[:2])
  p2[2]  = pos[2]
  p2 = p2-np.dot(pos,p2)*pos #orthogonalize
  p2 = p2/p2.dot(p2)**.5 #normalize
  return p2
 
 print odeint(xfunc,pos,[0,l],mxstep=200000,atol=1e-13,rtol=1e-13)


def path_len4(nbots=3,rinit=.999,tol=1e-6,l=1000):
 hinit = (1-rinit**2)**.5
 theta = 2*np.pi/nbots
 ct = np.cos(theta) 
 plen = 0
 def zfunc(z,t):
  d = ct + (z*z)*(1-ct)
  res = z*((1-d)/(1+d))**.5
  return res
# dom = np.linspace(0,l,int(l*100))
 #sol = odeint(zfunc,hinit,dom,mxstep=200000,atol=1e-10,rtol=1e-10)
 #plt.plot(dom[-100:],sol[-100:])
 #plt.show()
 #print sol[-10:]
 print quad(lambda z : 1./zfunc(z,0),hinit,1.)

path_len4(nbots=3)

def bisect_search(targ=10):
 nbots = 2
 l = 2/.85
 while l < targ:
  print nbots,l
  nbots *= int(ceil(targ/l))
  l = path_len(nbots=nbots,d2=5*10**3)

 lo = nbots/2
 hi = nbots
 print hi,l

 while hi-lo>1:
  med = (hi+lo)/2
  mval = path_len(nbots=med,d2=5*10**3)
  if mval > targ:
   hi = med
   l = mval
  else:
   lo = med
  print med,mval
 print hi,l

#print path_len(niter=10**6,nbots=144,d2=10000)
