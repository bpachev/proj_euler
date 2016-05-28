import numpy as np
import numpy.linalg as la
from itertools import combinations


tol = 1e-10
class lineSegment:
    def __init__(self, start, finish):
        self.a = start
        self.b = finish

    def intersection(self, other):
        #l1*a + (1-l1) *b = l2 * oa + (1-l2) * ob
        try:
            A = np.array([self.a-self.b, other.b-other.a]).T
            lambdas = la.solve(A, other.b - self.b)
            if (lambdas[0] > 0 and lambdas[0] < 1) and (lambdas[1] > 0 and lambdas[1] < 1):
                return lambdas[0] * (self.a-self.b) + self.b
            else:
                return None
        except:
            return None

#L1 = lineSegment(np.array([27, 44]), np.array([12, 32]))
#L2 = lineSegment(np.array([46, 53]), np.array([17, 62]))
#L3 = lineSegment(np.array([46, 70]), np.array([22, 40]))

def dist_intersections(segments):
    res = []
    for L1, L2 in combinations(segments, 2):
        p = L1.intersection(L2)
        if p is not None:
            res.append(tuple(p))
    res = sorted(res)
    last = res[0]
    tot = 1
    for el in res:
        if abs(el[0]-last[0]) < tol and abs(el[1] - last[1]) < tol:
            continue
        else:
            last = el
            tot += 1

    return tot

def bbshum_lines(nlines):
    res = []
    mat = np.zeros(4*nlines)
    s = 290797
    for i in xrange(4*nlines):
        if i and i%4 == 0:
            res.append(lineSegment(mat[i-4:i-2], mat[i-2:i]))
        s = s*s % 50515093
        mat[i] = s % 500
#    print mat
    return res

print dist_intersections(bbshum_lines(5000))
