from proj_euler import primes_and_mask, shanks_factorize
from math import log
from copy import copy
from scipy.misc import comb


def pascal_row(n):
    res = [1] * n

    for i in xrange(1,n-1):
        res[i] = res[i-1] * (n-i) / i
    return res
p_rows = [[1]]

def prime_equivalences(bound):
    """
    Let x,y be positive integers, with prime factorizations
    x = p_1^a_1 * ... * p_n ^ a_n
    y = q_1^b_1 * ... * q_n ^ b_n
    """

    primecap = int(log(bound) **2 / log(10) ) + 10
    primes = primes_and_mask(primecap)[0]
    temp = bound
    max_primes = 0
    for i, p in enumerate(primes):
        temp /= p
        if not temp:
            max_primes = i
            break

    res = []
    state = [0 for i in xrange(max_primes)]
    def recur(pind, bound, exp_bound):
        if bound == 0: return
        if exp_bound == 0: return
        if pind >= max_primes: return
        for exp in xrange(1, exp_bound+1):
            state[pind] = exp
            new_bound = bound / primes[pind]**exp
            if new_bound <= 0: break
            res.append(copy(state))
            recur(pind+1, new_bound, exp)
        #cleanup
        state[pind] = 0
    recur(0, bound, 100)
    return res, primes[:max_primes]

def C(n,i):
    return p_rows[n][i]

def combine_gozinta(a, b):
    #Let p, q be coprime with a and b giving the number of gozinta chains for each of each length
    a_len = len(a)
    b_len = len(b)
    target = [0 for i in xrange(a_len+b_len)]
    for i in xrange(1,a_len+1):
        for j in xrange(1,b_len+1):
            for k in xrange(max(i,j), i+j+1):
                #k choose i,  then i choose j+i-k
                target[k-1] += C(k,i) * C(i, j+i-k) * a[i-1]*b[j-1]
    return target

for i in xrange(200):
    p_rows.append(pascal_row(i+2))

bound = 10**16
classes, primes = prime_equivalences(bound)
tot = 0
for c in classes:
    g_rep = p_rows[c[0]-1]
    for el in c[1:]:
        if not el:
            break
        else:
            g_rep = combine_gozinta(g_rep, p_rows[el-1])
    g = sum(g_rep)
    if g > bound:
        continue
#    print g, c
    fact = shanks_factorize(g)
    rep = fact.values()
    trunc_rep = sorted(rep)[::-1]
    for i in xrange(len(rep), len(c)):
        trunc_rep.append(0)
    if trunc_rep == c:
        print g, fact, trunc_rep, c
        tot += g
print "Total "+str(tot)
