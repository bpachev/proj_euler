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


def find_ulam_num(v, n):
    a = ulam(2,v,v+3)
    last = a[-1]
    mask = np.array([el in a for el in xrange(last-2*v,last+1,2)])
    bmask = arr_to_bin(mask)
    tmask = bmask
    p = 2**v
    d = 0
    diffs = [0]
    while True:
        new = (p * (tmask%2)) ^ (p & tmask)
        tmask /= 2
        tmask += new
        d += 2
        if new:
            diffs.append(d)
            d = 0

        if tmask == bmask:
            break

    diffs = np.cumsum(np.array(diffs))
    N = len(diffs)-1
    D = diffs[-1]
    diff = n-len(a)
    if diff < 0:
        return a[n-1]
#    print diffs, a[-1], N, D
    return D * (diff / N) + diffs[diff % N] + a[-1]

print sum ([find_ulam_num(2*i+1, 10**11) for i in xrange(2, 11)])
#print find_ulam_num(9,37)
#print ulam(2,9,37)
#for i in xrange(10,11):
#    a =  np.array(ulam(2,2*i+1,300), dtype=int)
#    print a[1:]-a[:-1]
