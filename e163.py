import numpy as np
from numpy import pi
import numpy.linalg as la
import pylab as pl
from matplotlib import collections  as mc
from itertools import combinations, product

"""
Project Euler problem 163: Cross-hatched triangles.
"""

def anchor_transform(anchor, mat, point):
    return anchor + mat.dot(point-anchor)

class lineSegment:
    def __init__(self, start, finish):
        self.a = np.array(start)
        self.b = np.array(finish)

    def __repr__(self):
        return str(tuple(self.a)) +","+str(tuple(self.b))
    def __str__(self):
        return str(tuple(self.a)) +","+str(tuple(self.b))


    def intersects(self, other):
        #l1*a + (1-l1) *b = l2 * oa + (1-l2) * ob
        A = np.array([self.a-self.b, other.b-other.a]).T
        lambdas = la.solve(A, other.b - self.b)
#        print lambdas
        return (lambdas[0] > 0 and lambdas[0] < 1) and (lambdas[1] > 0 and lambdas[1] < 1)

    def anchor_transform(self, anchor, mat):
        return lineSegment(anchor_transform(anchor, mat, self.a), anchor_transform(anchor, mat, self.b))

    def elongate(self, distance):
        vec = self.b - self.a
        delta = distance * vec / la.norm(vec)
        return lineSegment(self.a-delta, self.b + delta)


#L1 = lineSegment(np.array([27, 44]), np.array([12, 32]))
#L2 = lineSegment(np.array([46, 53]), np.array([17, 62]))
#L3 = lineSegment(np.array([46, 70]), np.array([22, 40]))

#print L1.intersects(L3)

def rot(theta):
    c,s = np.cos(theta), np.sin(theta)
    return np.array([[c, s],[-s, c]])

def plot_lines(lines):
    lines = map(lambda s: [tuple(s.a), tuple(s.b)], reduce(lambda a,b: a+b,lines))
    lc = mc.LineCollection(lines,  linewidths=2)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    pl.show()


def solve(n):
    """
    Any triangle is result of three intersections. Three lines, with each intersecting the other.
    There are 2 classes of lines, with each class containing 3 lines each (all 120-degree rotations of each other).
    The first class contains the lines forming the sides of the great (or host) triangle. There are n such lines of each type in this class.
    In the other class (containing orientations 90 deg, 210 deg, and 330 deg) have 2*n - 1 copies each.
    Thus we see that each class of triangles corresponds three types of lines.
    """

    theta1 = pi/6
    h = np.cos(theta1)

    #let the corner be at the bottom left
    lines = []
    #first do horizontal lines
    horiz = []
    for i in xrange(n):
        horiz.append(lineSegment(np.array([.5*(i),i*h]), np.array([n-.5*i,i*h])))
    lines.append(horiz)

    vert = []
    for i in xrange(1,2*n):
        vert.append(lineSegment([i*.5, 0],[i*.5, min(i,2*n-i)*h]))
    lines.append(vert)

    center = np.array([n*.5, n*h/3])

    r1 = rot(2*pi / 3)
    r2 = rot(-2*pi / 3)
    lines.append([s.anchor_transform(center, r1) for s in horiz])
    lines.append([s.anchor_transform(center, r2) for s in horiz])
    lines.append([s.anchor_transform(center, r1) for s in vert])
    lines.append([s.anchor_transform(center, r2) for s in vert])


    lines = map(lambda t: map(lambda s: s.elongate(.1), t), lines)
#    plot_lines(lines)
    tot = 0
    for a,b,c in combinations(lines, 3):
        for l1, l2, l3 in product(a, b, c):
            if l1.intersects(l2) and l2.intersects(l3) and l3.intersects(l1):
                tot += 1
    #now count all triple intersections
    extras = n*n + 3 + ((n+1)*(n+2)/2 -3) * 20
    return tot - extras

print solve(36)
