import numpy as np

def make_vals(n):
    mod= 10**9+7
    vals = np.zeros(n, dtype = np.int64)
    t0 = 0
    for i in xrange(1,n):
        t0 = (t0*t0+45) % mod
        vals[i] = t0
    return vals


def solve(n):
    vals = make_vals(n)
    scores = vals.copy()
    sums = np.zeros(n+1, dtype = scores.dtype)
    sums[1:] = np.cumsum(vals)
#    print vals, sums
    for n_nums in xrange(1,n):
        scores[:-n_nums] = sums[n_nums+1:] - sums[:-n_nums-1] - np.minimum(scores[1:n-n_nums+1], scores[:-n_nums])
    print np.sum(vals[1::2])
    print scores[0]

solve(10**4)
