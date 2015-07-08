import networkx as nx
import sys
import numpy as np

if len(sys.argv) <= 1:
  filename = "p083_matrix.txt"
else:
  filename  = sys.argv[1]

fp = open(filename,"r")
m = np.loadtxt(fp,delimiter=",",dtype=int)
fp.close()

n = m.shape[0]
G = nx.DiGraph()

for i in xrange(n):
  for j in xrange(n):
    if i+1<n:
      G.add_edge(n*i+j,n*(i+1)+j, weight=m[i+1,j])
    if j+1 < n:
      G.add_edge(n*i+j,n*i+j+1, weight=m[i,j+1])    
    if i:
      G.add_edge(n*i+j,n*(i-1)+j, weight=m[i-1,j])
    if j:
      G.add_edge(n*i+j,n*i+j-1, weight=m[i,j-1])

print m[0,0] + nx.shortest_path_length(G,0,n*(n-1)+(n-1),weight="weight")

