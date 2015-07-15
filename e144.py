import numpy as np
from math import sqrt

def quad_roots(a,b,c):
  d = sqrt(b*b-4*a*c)
  return (-b+d)/(2.*a),(-b-d)/(2.*a)

def reflection_slope(p1,p2,orig_slope):
 '''
 p1 and p2 -- points in R2, represented by numpy arrays
 p2 is a point on the line to be reflected
 p1 is the point of intersection
 orig_slope -- slope of line of reflection
 RETURNS:
 slope, the slope of the reflected line
 '''
 
 v = np.array([1.,orig_slope])
 n = np.inner(v,v)
 Q = 2*np.outer(v,v)/n - np.eye(2)
 x = Q.dot(p2-p1) #the image of p2 (after translating everything by p1)
 if x[0] == 0:
   print "Vertical Slope"
   raise ValueError
 return x[1]/x[0]


lastPoint = np.array([0.,10.1])
currPoint = np.array([1.4,-9.6])
print currPoint
ntries = 40000
for i in xrange(ntries):
 x,y = currPoint[0],currPoint[1]
 #print x,y
 if abs(x) <= 0.01 and y > 0:
   print "IT's FREE after %d bounces " % i
   break
 normal_slope = y/(4*x)
 nSlope = reflection_slope(currPoint,lastPoint,normal_slope)
 m,b = nSlope, y - nSlope*x
 r1,r2 = quad_roots(4+m*m,2*m*b,b*b-100)
 #One of the solutions will be the original point, don't get that one
 #Note that things break if a vertical reflection occurs
 if abs(r1-x) > abs(r2-x):
   x = r1
 else:
   x = r2
 
 y = m*x + b
 #sanity check
 if abs(4*x*x+y*y - 100) > 1e-6:
   print "ERROR: point " +str((x,y)) +" not on ellipse" 
 
 lastPoint = currPoint
 currPoint = np.array([x,y])
 
