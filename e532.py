import numpy as np
from math import acos,sin,cos,ceil
from matplotlib import pyplot as plt
from scipy.integrate import odeint


def path_len(nbots=3,rinit=.999,niter = 100,delta=2*np.pi/1000,d2=30,tol=1e-6):
 hinit = (1-rinit**2)**.5
 pos = np.array([rinit,0,hinit])
 theta = 2*np.pi/nbots
 ct,st = np.cos(theta),np.sin(theta) 
 rotarr = np.array([[ct,st],[-st,ct]])
 p2 = np.zeros(3)
 plen = 0.
 i=0
 while abs(1.-pos[2]) > tol:
  p2[:2] = rotarr.dot(pos[:2])
  p2[2]  = pos[2]
  d = pos.dot(p2)
  ang = abs(acos(d))/d2
  plen += ang
  p2 = p2-d*pos #orthogonalize
  p2 = p2/p2.dot(p2)**.5 #normalize
  pos = cos(ang)*pos + sin(ang)*p2
  i += 1
 print i
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

def path_len3(nbots=3,rinit=.999,tol=1e-6):
 hinit = (1-rinit**2)**.5
 pos = np.array([rinit,0,hinit])
 theta = 2*np.pi/nbots
 ct,st = np.cos(theta),np.sin(theta) 
 rotarr = np.array([[ct,st],[-st,ct]])
 plen = 0
 def xfunc(pos,t):
  p2 = np.zeros(3) 
  p2[:2] = rotarr.dot(pos[:2])
  p2[2]  = pos[2]
  p2 = p2-np.dot(pos,p2)*pos #orthogonalize
  p2 = p2/p2.dot(p2)**.5 #normalize
  return p2
 
 print odeint(xfunc,pos,np.linspace(0,980),mxstep=20000)

path_len3(nbots=800)

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
