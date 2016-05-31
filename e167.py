import numpy as np

def ulam(a,b,n):
    res = [a,b]
    for it in xrange(n-2):
        l = len(res)
        counts = {}
        for i in xrange(l):
            for j in xrange(i):
                s = res[i] + res[j]
                if s <= res[-1]:
                    continue
                if not s in counts: counts[s] = 1
                else: counts[s] += 1
        # print counts
        k = sorted(counts.keys())
        for el in k:
            if counts[el] == 1:
                res.append(el)
                break

    return res

def arr_to_bin(arr):
    res = 0
    for el in arr[::-1]:
        res *= 2
        if el:
            res += 1
    return res


def find_ulam_period(v):
    a = ulam(2,v,v+3)
    last = a[-1]
    mask = np.array([el in a for el in xrange(last-2*v,last+1,2)])
    i = 0
    bmask = arr_to_bin(mask)
    tmask = bmask
    p = 2**v
    diffs = []
    while True:
        new = (p * (tmask%2)) ^ (p & tmask)
        tmask /= 2
        tmask += new
        i += 1
        if tmask == bmask:
            return 2*i

find_ulam_period(21)

#for i in xrange(10,11):
#    a =  np.array(ulam(2,2*i+1,300), dtype=int)
#    print a[1:]-a[:-1]
