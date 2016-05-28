import numpy as np
import numpy.linalg as la
from itertools import combinations
from fractions import Fraction as frac

class lineSegment:
    def __init__(self, start, finish):
        self.a = start
        self.b = finish

    def intersection(self, other):
        #l1*a + (1-l1) *b = l2 * oa + (1-l2) * ob
        try:

            A = np.array([self.a-self.b, other.b-other.a]).T
            b = other.b - self.b
            d = int(A[0,0]*A[1,1]-A[1,0]*A[0,1])

            if not d:
                return None

            l1 = int(b[0]*A[1,1] - b[1]*A[0,1])
            l2 = int(b[1]*A[0,0] - b[0]*A[1,0])
            l1 = frac(l1, d)
            l2 = frac(l2, d)

            if l1 <=0 or l1 >= 1 or l2 <= 0 or l2 >= 1: return None

            return (int(self.a[0]-self.b[0]) * l1 + self.b[0], int(self.a[1]-self.b[1]) * l1 + self.b[1])

        except:
            return None

    def __str__(self):
        return str(self.a) + " " + str(self.b)

L1 = lineSegment(np.array([27, 44]), np.array([12, 32]))
L2 = lineSegment(np.array([46, 53]), np.array([17, 62]))
L3 = lineSegment(np.array([46, 70]), np.array([22, 40]))

def dist_intersections(segments):
    res = set()
    for L1, L2 in combinations(segments, 2):
        p = L1.intersection(L2)
        if p is not None:
            res.add(p)
    return len(res)

def bbshum_lines(nlines):
    res = []
    mat = np.zeros(4*nlines, dtype=np.int64)
    s = 290797
    for i in xrange(4*nlines):
        if i and i%4 == 0:
            res.append(lineSegment(mat[i-4:i-2], mat[i-2:i]))
        s = s*s % 50515093
        mat[i] = s % 500
    i = 4*nlines
    res.append(lineSegment(mat[i-4:i-2], mat[i-2:i]))

    return res

print dist_intersections(bbshum_lines(5000))
#print dist_intersections([L1, L2, L3])
