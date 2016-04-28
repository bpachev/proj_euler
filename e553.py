import proj_euler as pe
import numpy as np

mod = 10**9+7
max_n = 10**4
fact, ifact = pe.mod_fact_cache(mod, max_n = max_n)

def comb(n,k):
    if k > n: return 0
    if n < mod:
        return (((int(fact[n]) * int(ifact[k])) % mod )* int(ifact[n-k])) % mod
    n_digits, k_digits = pe.base_repr(n, mod), pe.base_repr(k, mod)
    res = 1
    for top, bot in zip(n_digits, k_digits):
        res = (res * C(top, bot)) % mod
    return res

def double_power_set(n):
    #for prime mods, the totient is p-1
    return pow(2, pow(2, n, mod-1) -1 ,mod)


def C(n,k):
    #build cache tables
    cache = np.zeros((n+1, k+1), dtype=int)
    for j in xrange(1, n+1):
        #all possible graphs
        cache[j,1] = cache[j-1,1] + double_power_set(j) - double_power_set(j-1)
        for i in xrange(0, j-1):
            cache[j,1] -= (comb(j-1, i) * (double_power_set(j-1-i)-1) * (cache[i+1,1]-(i+1)*cache[i,1])) % mod
            cache[j,1] %= mod
#    for i in xrange(2,k+1):
    return cache[n,k]
print C(3,1)
