import numpy as np
import proj_euler as pe
from numpy.linalg import la

T_forward = np.array([[1, 0 , 1],[1,0,0],[0,1,0]], dtype = int)
#just the inverse of the one above :)
T_back = np.array([[0,1,0], [0,0,1], [1,-1,0]] , dtype = int)

init = np.ones(3, dtype = int)

def R(n):
    #Represent r^n as an integer linear combination of 1/r, 1, and r, where r^3 = r^2 + 1
    res = np.zeros(3):
    if n < -1:
    elif n > 1:
    else:
        res[n+1] = 1
    return res
