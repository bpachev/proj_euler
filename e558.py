import numpy as np
import proj_euler as pe
import numpy.linalg as la
from fractions import Fraction as frac
from sys import argv

outfile = open(argv[1], "w")

T_forward = np.array([[1, 0 , 1],[1,0,0],[0,1,0]], dtype = int)
#just the inverse of the one above :)
T_back = np.array([[0,1,0], [0,0,1], [1,-1,0]] , dtype = int)
init = np.ones(3, dtype = int)
cache = {}
def R(n):
    #Represent r^n as an integer linear combination of 1/r, 1, and r, where r^3 = r^2 + 1

    if n in cache:
        return cache[n]

    res = np.zeros(3, dtype = int)
    if n < -1:
        mat = pe.mat_exp(-1-n, T_back)
        res = mat[-1]
    elif n > 1:
        mat = pe.mat_exp(n-1, T_forward)
        res = mat[0]
    else:
        res[1-n] = 1
    cache[n] = res
    return res
#print R(-50)

r = 1.465571231876768026656731
log_r = np.log(r)
#exps = set()
def repr_size(n):
#    print "Called with " +str(n)
    max_pow = int(np.log(n)/np.log(r))
    curr = np.zeros(3, dtype = int)
    curr[1] = n
    terms = 1
    temp = R(max_pow)
    curr -= temp
    exp = max_pow-3
#    print max_pow
    while not rep_zero(curr):
        temp = R(exp)
        if slow_rep_positive(curr-temp):
    #        print exp
            curr -= temp
            terms += 1
            exp -= 3
        else:
            exp -= 1
    outfile.write(str(exp)+"\n")
#    exps.add(exp)
    return terms

eps = 1e-4
def r_less(a, b):
    abs_a = abs(a)
    # is r less than b + sqrt(a) ?
    m1 = (abs_a + 3*b*b - 2*b)
    if a < 0: m1 = -m1
    m2 = (3*abs_a*b - abs_a + b**3 - b*b - 1)
    #is m1 root(a) + m2 >= 0
    mag_comp =abs_a*m1*m1 >= m2*m2
    if m1 >= 0:
        if m2 >= 0:
            return True
        else:
            return mag_comp
    else:
        if m2 < 0:
            return False
        else:
            return not mag_comp

def slow_rep_positive(rep):

        a,b,c = int(rep[0]), int(rep[1]), int(rep[2])
        if a == 0:
            if b == 0:
                return c >= 0
            else:
                return r_less(0, frac(c, b))

        d = b*b - 4*a*c
#        print "disc ",d
        #then the polynomial is always positive or negative for r real, with sign given by the leading coefficient
        if d < 0:
            return a >= 0
#        D = frac(d, 4*a*a)
#        C = frac(-b, 2*a)
        r1, r2 = None, None
#        m1 = (D + 3*C*C - 2*C)
        #m1 = frac(d+3*b*b+4*a*b, 4*a*a)
        #m2 = (3*D*C - D + C**3 - C*C - 1)
        #m2 = frac(-3*d*b-2*a*d-b**3-2*a*b*b-8*a**3, 8*a**3)
        m2 = -3*d*b-2*a*d-b**3-2*a*b*b-8*a**3
        m1 = d+3*b*b+4*a*b
        mag_comp = d*m1*m1 >= m2*m2
        if m1 >= 0:
            if m2 >= 0:
                r1 = True
                r2 = not mag_comp
            else:
                r1 = mag_comp
                r2 = False
        else:
            if m2 < 0:
                r1 = False
                r2 = mag_comp
            else:
                r1 = not mag_comp
                r2 = True
        if a > 0:
            return (r1 and r2) or (not r1 and not r2)
        else:
            return (r1 and not r2) or (r2 and not r1)

def rep_positive(rep):
    p_r = r*rep[0] + rep[1] + rep[2]/r
    if abs(p_r) > eps:
        return p_r >= 0
    else:
        return slow_rep_positive(rep)

def rep_zero(rep):
    return rep[0] == 0 and rep[1] == 0

def solve(n, start_ind = 2, start_tot = 1):
    tot = start_tot
    for j in xrange(start_ind, n+1):
        tot += repr_size(j*j)
        msg = "On %d, total %d" % (j, tot)
        outfile.write(str(msg)+"\n")
        if j%5000 == 0: print msg
    return tot

def out(msg):
    outfile.write(str(msg)+"\n")
    print msg

#print repr_size(1012423**2)
out(solve(5*10**6, start_ind = 1012423, start_tot = 40590809))
#for j in xrange(2,50):
#    print repr_size(j)
#test = np.array([ 9 ,60 ,73])
#print rep_positive(test)
#print test.dot(np.array([r*r, r, 1]))
#print slow_rep_positive(test)
#print min(exps)
