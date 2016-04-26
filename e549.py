from proj_euler import prime_fact_ord, binary_search
import numpy as np

def s(p, e):
    """
    returns the minimum n with p^e | n!
    """
    if e < p:
        return p*e
    i = p
    while True:
        if prime_fact_ord(p, p*i) >= e: return p*i
        i += 1

def solve(n):
    mask = np.zeros(n+1, dtype = int)
    cache = np.zeros(int (1 + 2 *np.log(n)), dtype = int)
    for i in xrange(2, n+1):
        if not mask[i]:
            t = n
            e = 1
            while t:
                cache[e] = s(i, e)
                inc = i**e
                for j in xrange(inc, n+1, inc): mask[j] = max(mask[j], cache[e])
                t /= i
                e += 1
    return np.sum(mask)

if __name__ == "__main__":
    print solve(10**8)
