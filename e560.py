import numpy as np
import proj_euler as pe

def nimber_exp(n, init, mod):
    T = init.copy()
    exp = n-1
    while exp:
        if exp % 2:
            init  = combine_counts(T, init, mod)
        T = combine_counts(T, T, mod)
        exp /= 2
    return init

def solve(n, k, mod = 10**9+7):
    primes = pe.primes_and_mask(n)[0]
    pi = len(primes) + 1
    nstates = 2 ** (len(bin(pi-1))-2)
    nimber_counts = np.zeros(nstates, dtype = np.int64)
    mask = np.zeros(n, dtype = np.int64)
#    pcounts = np.cumsum(mask.astype(int))
    for i, p in enumerate(primes, 1):
        mask[p] = i
        for j in xrange(p*p, n, p):
            if mask[j]:
                mask[j] = min(mask[j], i)
            else:
                mask[j] = i
    bcounts = np.bincount(mask)
    nimber_counts[2:len(bcounts)] = bcounts[2:]
    nimber_counts[1] = 1
    nimber_counts[0] = bcounts[1]
    nimber_counts = nimber_exp(k, nimber_counts, mod)

    print nimber_counts[0]

def slow_combine_counts(a, b, mod):
    n = a.size
    res = np.zeros(n, dtype = a.dtype)
    for i in xrange(n):
        for j in xrange(n):
            res[i^j] += (a[i]*b[j]) % mod
            res[i^j] %= mod
    return res

def combine_counts(a, b, mod):
    n = a.size
    if n <= 2:
        return slow_combine_counts(a,b, mod)
    pivot = n/2
    a %= mod
    b %= mod
    u = combine_counts(a[:pivot]+a[pivot:], b[:pivot]+b[pivot:], mod)
    v = combine_counts(a[:pivot]-a[pivot:], b[:pivot]-b[pivot:], mod)

    res = np.zeros(n, dtype = a.dtype)
    res[:pivot] = ((u + v) * pe.mod_inv(2, mod)) % mod
    res[pivot:] = ((u - v) * pe.mod_inv(2, mod)) % mod
    return res

solve(10**3, 10**3)
