import proj_euler as pe
import numpy as np

primes= pe.primes_and_mask(25)[0]
cap = 10**8
cands = sorted([el for el in pe.HarshadGen(primes, cap, exact=False)])
print len(cands)
seen = {}
for i, el in enumerate(cands):
    for other in cands[i:]:
        if other > 1.1*el:
            break
        else:
            s = el*other
            reps = 1
            if s not in seen:
                seen[s] = reps
            else: seen[s] += reps

m_dict = {i:np.inf for i in xrange(2,101)}
for el in seen:
    if seen[el] > 100 or seen[el]==1: continue
    m_dict[seen[el]] = min(m_dict[seen[el]], el)
print m_dict
print sum([m_dict[i] for i in xrange(2,101)])
