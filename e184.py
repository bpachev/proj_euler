import numpy as np
import proj_euler as pe

def solve(n):
    if n>2:
        lines = list(pe.FareyGen(n-1))
    else:
        lines = []
    flipped = [(b,a) for a,b in lines]
    lines = [(1,0)] + lines + [(1,1)] + flipped[::-1]
    counts = np.zeros(len(lines), dtype = np.int64)
    for i, el in enumerate(lines):
        counts[i] = pe.isqrt(((n)**2-1)/(el[0]**2 + el[1]**2))

    csums = np.cumsum(counts)
    print counts
    tot = 0
    for i, el in enumerate(lines):
        if not i: continue
        tot += counts[i] * csums[i-1] * (csums[-1]-csums[i] + csums[-1])

    return 4 * tot


print solve(105)
