import proj_euler as pe
import numpy as np

def solve(n):
    primes = np.array(pe.primes_and_mask(n)[0], dtype = np.int64)
    pi = len(primes)
    #product of first k primes mod p, for each prime
    mod_prods = 2*np.ones(pi, dtype=np.int64)
    a_mods = np.ones(pi, dtype = np.int64)
    #a_0 is 0, I guess
    a = 1
    mask = primes == -1

    for i in xrange(1, pi):
        #we want to find the smallest k with k*p_1*...*p_i + A_i = t*p_(i+1) + (i+1)
        #solving this equation mod p_(i+1) for k yields the answer
        p = primes[i]
        k = ((i+1 - a_mods[i]) * pe.mod_inv(mod_prods[i], p)) % p
        a_mods[i:] = (a_mods[i:] + k*mod_prods[i:]) % primes[i:]
        mod_prods[i:] *= p
        mod_prods[i:] %= primes[i:]
        mask[a_mods==0] = True
    print np.sum(primes[mask])
solve(50)
