import proj_euler as pe
import math
from bisect import bisect_right

def cake_icing(a,b,c):
    #the list of brown-pink boundaries
    bounds = []
    steps = 0
    a_n, b_n, c_n = 1./a, 1./b, 1./math.sqrt(c)
    rem = 0.
#    last_pos = 0
    while True:
        steps += 1
        r = steps%3
        q = steps/3
        if r == 1:
            #do a step
            new_r = (rem+a_n)%1.

        elif r == 2:
            #do b step
            new_r = (rem+b_n)%1.
        else:
            #do c step
            new_r = (rem+c_n)%1.

        i1 = bisect_right(bounds, rem)
        bounds.insert(i1, rem)
        i2 = bisect_right(bounds, new_r)
        print new_r, i1
        bounds.insert(i2, new_r)
#        print bounds

        if i1 < i2:
            for i in xrange(i1+2,i2+1):
                bounds[i] = rem+new_r - bounds[i]
        else:
            for i in xrange(i2):
                #transform it
                bounds[i] = (rem+new_r - bounds[i]) %1.
            for i in xrange(i1, len(bounds)):
                #transform it
                bounds[i] = (rem+new_r - bounds[i]) %1.
        bounds = sorted(bounds)

        rem = new_r
#        print bounds
        if steps > 5: break
        if not len(bounds): return steps
cake_icing(9, 10, 11)
