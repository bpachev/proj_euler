import proj_euler as pe
import numpy as np
#n = 5*10**4
mod = 1000000123
fact, ifact = pe.mod_fact_cache(mod, max_n = 5*10**3+2)

def P(k, r, n):
    q, rem = divmod(n-1,k)
    rem += 1
    dividers = q
    divs = np.zeros(dividers+2,np.int64)
    #number of pieces available
    divs[0] = 1
    divs[1] = pow(int(ifact[k]), r, mod)
    for i in xrange(2, dividers+1):
        for j in xrange(1, i+1):
            divs[i] -=  (-1) ** (j%2) * pow(int(ifact[j*k]), r, mod) * divs[i-j]
            divs[i] %= mod
#    print divs, rem, q
    for j in xrange(1, len(divs)):
#        print divs[-j-1], j
        divs[-1] -= (-1) ** (j%2) * pow(int(ifact[(j-1)*k+rem]), r, mod)  * divs[-j-1]
        divs[-1] %= mod
    return (divs[-1] * pow(int(fact[n]), r, mod)) % mod

def Q(n):
    tot = 0
    for k in xrange(1,n+1):
        tot += P(k, n, n)
    return tot

print P(7,5,30)
