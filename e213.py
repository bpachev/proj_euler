#Benjamin pachev's solution to the Flea Circus problem
import numpy as np
from numpy.linalg import matrix_power
from itertools import product

n = 30

def state_to_ind(state):
    return state[0] * n + state[1]

def ind_to_state(ind):
    return ind / n, ind % n

def valid_state(state):
    return (0 <= state[0] < n) and (0 <= state[1] < n)

def solve():
    nstate = n**2
    M = np.zeros((nstate, nstate))
    
    for i in xrange(nstate):
        state = ind_to_state(i)
        inds = []
        for v, h in product([1,-1], [0,1]):
            new_state = (state[0] + v*(1-h), state[1] + v*h)
            if valid_state(new_state):
                inds.append(state_to_ind(new_state))
        
        denom = float(len(inds))
        for j in inds:
            M[j,i] = 1./denom
        
    A = matrix_power(M, 50)
    res = 0
    for i in xrange(nstate):
        res  += np.exp(np.sum(np.log(1 - A[i])))
    print "{:.6f}".format(res)

solve()    
