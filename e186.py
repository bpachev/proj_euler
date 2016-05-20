import numpy as np
import networkx as nx

n = 10**6
T = np.zeros(n, dtype = np.int64)
for i in xrange(55):
 T[i] = (100003 - 200003*i + 300007*i**3) % n
for i in xrange(55,n):
 T[i] = (T[i-24] + T[i-55]) % n
