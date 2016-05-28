import numpy as np
import networkx as nx

mod = 10**6
#n = 6*mod
n = 5*mod-3*10**5 - 4*10**4 - 8*10**3 - 7*10**2 - 36
T = np.zeros(n, dtype = np.int64)
real_edges = 0
for i in xrange(1, 56):
 T[i-1] = (100003 - 200003*i + 300007*i**3) % mod
for i in xrange(55,n):
 T[i] = (T[i-24] + T[i-55]) % mod
print "populated stuff"
G = nx.Graph()
for i in xrange(0,n,2):
    if not T[i] == T[i+1]: real_edges += 1
print real_edges, n/2
#    G.add_edge(int(T[i]), int(T[i+1]))
# print "built graph"
# lens = set()
# big_comp = None
# for comp in nx.connected_components(G):
#     l = len(comp)
#     if l > mod/2:
#         print l, 524287 in comp
#         big_comp = comp
#     lens.add(len(comp))
#
#
# print max(lens)
