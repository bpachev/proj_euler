import numpy as np
from fractions import gcd
from proj_euler import is_square, isqrt

def check_cut(a,b,c,d):

  r1 = np.array([float(b)/(a+b), float(a)/(c+a)])
  r2 = np.ones(2) - r1
  r1 = r1 * (c+d)/ (a+b)
  r1[0] += float(b)/(a+b)

  r2 = r2 * (b+d)/ (a+c)
  r2[1] += float(c)/(a+c)
  print r1, r2

def int_check_cut(a,b,c,d):
    s = a + b + c + d
    r1 =  s * b * (a+c) - a * (b+a) * (b+d)
    r2 = s * c * (a+b) - a * (c+a) * (c+d)
    if not r1 or not r2:
        print r1, r2, a,b,c,d

def solve(n):
    tot = 0
    res = set()
    for A in xrange(1,n+1):
        for a in xrange(1, A-2):
            num, denom = a*a, A+a
            g = gcd(num, denom)
            p = num/g
            q = denom/g
            #now b*c/d = p/q, thus q divides d, and d <= A-a
            for k in xrange(1, (A-a)/q+1):
                #hence b*c = k*p, and b+c = A-a-d
                prod = k*p
                s = A - a - k*q
                D = s*s - 4 *prod
                if is_square(D):
                    tot += A
#                    print "Works for ",A,a, (s-isqrt(D))/2, (s+isqrt(D))/2, k*q
    return tot
print solve(10**3)
            #we know b*c * ( 2*a + d + b+c) = a^2*d
            #thus b * c < a*a*d/(2*a+d), b+c < cap - a - d
            #hence b = root(c * x^2 + [2a+d+c^2]x + )

#n = 55
#for a in xrange(1,n-3):
#    for c in xrange(1, n-a-1):
#        for b in xrange(1, min(n-a-c-1, c+1)):
#            d = n-a-b-c
#            int_check_cut(a,b,c,d)
