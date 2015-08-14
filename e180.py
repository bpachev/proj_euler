from fractions import Fraction
from proj_euler import FareyGen,isqrt


k = 35
s = set()
fracts = map(lambda t: Fraction(t[0],t[1]), list(FareyGen(k)))

def checkz(z,p):
 global k
 if p <0:
  return checkz(1/z,-p)
 elif p == 2:
  a,b = isqrt(z.numerator),isqrt(z.denominator)
  if a*a == z.numerator and b*b == z.denominator:
    return checkz(Fraction(a,b),1)
  else:
   return None
 elif p ==1:
  if z.denominator <= k and z < 1:
   return z
l = [-1,-2,1,2]
for x in fracts:
  for y in fracts:
   temp = x+y
   for p in l:
     z1 = checkz(x**p+y**p,p)
     if z1 is not None:
#       print x,y,z1,p
       s.add(temp+z1)

res = Fraction(0,1)
for f in s:
 res = res + f
print res
print res.numerator + res.denominator
