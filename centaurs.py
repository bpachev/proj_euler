from scipy.misc import comb
from sympy import *

def f(t, b):
    if b == 0:
        return 1 if t==0 else 0
    return comb(t+b-1, t,True)
def eq_cases(n):
    return (n-1) * (n+1)**2 + 2*(n+1)

def slow_centaur(n):
    tot = eq_cases(n)
    for l_1 in xrange(n):
        for l_n in xrange(l_1+1,n+1):
            #last i for which l_i = l_1
            for i in xrange(1, n):
                #first j for which l_j = l_n
                for j in xrange(i+1,n+1):
                    #something i-j-1
                    mul = 2
                    if n-l_n: mul *= n-j+2
                    if l_1: mul *= i+1
                    things = j-i-1
                    boxes = l_n- l_1 - 1
                    inc = mul*f(things, boxes)
                    #print "l1=%d ln=%d i=%d, j=%d, inc=%d" % (l_1, l_n, i, j, inc)
                    tot += inc
    return tot

def p2(n,d2):
    m = n-d2
    return (m*(m+2)*(m+7))/6

def p1(n, d2):
    m = n-d2
    return (m+3)*(m)

def g(n, d1, d2):
    m = n-d2
    res = (m+3)*(m)
#    res += (n-d1-1) * (m*(m+2) - m*(m+1)*(2*m+1)/6 + (m+1)*m*(m+1)/2 )
    #By Wolfram, the above simplifies to
    res += (n-d1-1) * (m*(m+2)*(m+7))/6
#    for pos in xrange(1,m+1):
#        for val in xrange(1, n-d1):
#            inc = 1
#            if val: inc *= pos+1
#            if n-val-d1: inc *= n-d2-pos+2
#            res += inc
    return res
def C(n,k):
    return comb(n,k,True)

#a is a list of coefficients sum (r+i choose r) P(i) from i = 0 to n
def sum_comb_poly(coeffs, n, r):
    degree = len(coeffs()) - 1
    if degree:
        q_coeffs = coeffs[:-1]
        return coeffs[-1] * C(r+n+1, r+1) + (r+1) * sum_comb_poly(d, q, n-1, r+1)
    else:
        return coeffs[0] * C(r+n+1, r+1)

def slow_sum_comb_poly(P, n, r):
    tot=0
    for i in xrange(n+1):
        tot += C(r+i,i) * P(i)
    return tot

def slow2(n):
    tot = eq_cases(n)

    inc = 0
    #handle the cases when the value difference is 1 or n
    inc += g(n, 1, 1) #the value difference is 1
    #the value difference is n
    inc += (n-1) * (comb(2*n-3, n-1,True) - comb(2*n-3, n,True))
#    for t in xrange(n-1): inc += comb(n+t-2,n-2,True) * (-t)
#    for d2 in xrange(1, n): inc += f(d2-1, n-1)   * (n-d2)

    #difference in value
    d = symbols('d')
    p2_poly = Poly((n-d)*(n-d+2)*(n-d+7))
    p1_poly = Poly((n-d+3)*(n-d))
    print div(p2_poly,d)
    print p1_poly

    for d2 in xrange(1,n):
        #difference in position
        inc += C(n+d2-3, n-3) * ( p1_poly(d2) + (n-3) * p2_poly(d2)/6) - C(n+d2-3, n-4) * (d2 * p2_poly(d2)/6)

    return tot + 2*inc


def centaur(n):
    tot = eq_cases(n)


print slow_centaur(4)
print slow2(10)
