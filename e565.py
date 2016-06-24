import numpy as np
import proj_euler as pe

d = 2017
#n = 10**11
n = 10**6
#we want 6*k+2 <= n
first_power_primes = np.load("e565primes.npy")
plist = [(p,p) for p in first_power_primes]
"""
for k in xrange(1, (n/d)/6):
    p = d*k*6+1
    if pe.MillerRabin(p): first_power_primes.append(p)
    p += 4*d
    if pe.MillerRabin(p): first_power_primes.append(p)
print len(first_power_primes)
np.save("e565primes",np.array(first_power_primes))
"""
print len(first_power_primes)
sq = pe.isqrt(n)
primes = pe.primes_and_mask(sq)[0]

max_power = int(np.log(n)/np.log(2))
powers = {}
for power in xrange(2, max_power):
    powers[power] = []
    for p in primes:
        exp = p**power
        if exp > n:
            break
        if p%2017 == 2016: continue
        if (exp*p-1) % 2017 == 0:
            plist.append(exp, p)

plist = sorted(plist)
def sum_excluded(n, divs, maximum = None):
    #assumes divs is sorted
    if n <= 1: return n
    if maximum is None: maximum = n+1
    tot = n*(n+1) / 2
    for d in divs:
        if d >= maximum: break
        tot -= d*sum_excluded(n/d, divs, d)
    return tot

#print plist
def sum_candidates(n, excluded=[], maximum = None):
    if maximum is None: maximum = n
    tot = 0
    if n <= 1: return n
    if len(excluded): tot += sum_excluded(n, sorted(excluded))
    for exp, p in plist:
        excluded.append(p)
        tot += exp*sum_candidates(n/exp, excluded)
        excluded.pop()
        if exp > n: break
    return tot
print sum_candidates(10**9)
