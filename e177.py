import numpy as np
from math import sin,cos,sqrt,asin,acos
from itertools import product

s_arr = np.sin(np.arange(181)*np.pi/180)
c_arr = np.cos(np.arange(181)*np.pi/180)
sorted_s_arr = s_arr[:90]
tot = 0

cache = []
res = set()

for i in xrange(1,180):
 for j in xrange(1,180-i):
  cache.append([i,j,s_arr[i]/s_arr[180-i-j]])

def is_int_angled(el1,el2):
 a,b = el1[2],el2[2]
 c = sqrt(a**2+b**2-2*a*b*c_arr[el1[1]+el2[1]])
 theta = 180*asin(a/c * s_arr[el1[1]+el2[1]])/np.pi
 if abs(theta-round(theta)) < 1e-9:
    th = int(round(theta))
    t = [0]*8
    t[0],t[1] = el1[0],th+el2[1]-el1[0]
    t[2],t[3] = 180-th-el2[1]-el1[1], el1[1]
    t[4],t[5] = el2[1],th
    t[6],t[7] = 180-th-el2[0]-el2[1],el2[0]
    print t 
    for i in xrange(0,8):
     tt=t[i:]+t[:i]
     print tt,tt[::-1]
    return True
 return False

def iia(a1,a2,c1,c2):
 return is_int_angled([a1,a2,s_arr[a1]/s_arr[180-a2-a1]],[c1,c2,s_arr[c1]/s_arr[180-c2-c1]])

#print iia(20,30,60,40)
 
#cache=cache[:1]
l=len(cache)
for i in xrange(l):
 if i%1000==0:
  print "ON i=%d" % i
 for j in xrange(l):
  el1,el2=cache[i],cache[j]
  if el1[0]+el2[0] < 180 and el2[1]+el1[1] < 180 and el1[0]<=el2[0] and (el1[0]+el2[0])<=(el2[1]+el1[1]):
   a,b = el1[2],el2[2]
   c = sqrt(a**2+b**2-2*a*b*c_arr[el1[1]+el2[1]])
   theta = 180*acos((b**2+c**2-a**2)/(2*b*c))/np.pi
   if abs(theta-round(theta)) < 1e-9:
    th = int(round(theta))
    #check if the triangle is obtuse
#    if th < 90 and c**2+b**2 < a**2:
 #    th+=90
    t = [0]*8
    t[0],t[1] = el1[0],th+el2[1]-el1[0]
    t[2],t[3] = 180-th-el2[1]-el1[1], el1[1]
    t[4],t[5] = el2[1],th
    t[6],t[7] = 180-th-el2[0]-el2[1],el2[0]
    t=t[:1]+t[1:][::-1] #so corners that are part of the same angle stick together
    is_dup=False
    for k in xrange(0,8,2):
     tt=t[k:]+t[:k]
     if tuple(tt) in res or tuple(tt[::-1]) in res:
      is_dup=True
      break
    if not is_dup:	
     res.add(tuple(t))
print "Number of Candidates %d" % len(res)
f=open("e177_out_new.txt","w")
f.write(" ".join(map(str,res)))
f.close()

