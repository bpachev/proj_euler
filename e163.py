import numpy as np
import numpy.linalg as la
"""
Project Euler problem 163: Cross-hatched triangles.
"""

class lineSegment:
    def __init__(self, start, finish):
        self.a = start
        self.b = finish

    def intersects(self, other):
        #l1*a + (1-l1) *b = l2 * oa + (1-l2) * ob
        A = np.array([self.a-self.b, other.b-other.a]).T
        lambdas = la.solve(A, other.b - self.b)
        print lambdas
        return (lambdas[0] > 0 and lambdas[0] < 1) and (lambdas[1] > 0 and lambdas[1] < 1)

L1 = lineSegment(np.array([27, 44]), np.array([12, 32]))
L2 = lineSegment(np.array([46, 53]), np.array([17, 62]))
L3 = lineSegment(np.array([46, 70]), np.array([22, 40]))

print L1.intersects(L3)

def solve(n):
    """
    Any triangle is result of three intersections. Three lines, with each intersecting the other.
    There are 2 classes of lines, with each class containing 3 lines each (all 120-degree rotations of each other).
    The first class contains the lines forming the sides of the great (or host) triangle. There are n such lines of each type in this class.
    In the other class (containing orientations 90 deg, 210 deg, and 330 deg) have 2*n - 1 copies each.
    Thus we see that each class of triangles corresponds three types of lines.
    """
    pass
