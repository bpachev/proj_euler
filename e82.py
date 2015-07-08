import networkx as nx
import sys
import numpy as np

if len(sys.argv) <= 1:
  filename = "p082_matrix.txt"
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

curr_min = np.inf
for i in xrange(n):
  for j in xrange(n):
    t = m[i,0] + nx.shortest_path_length(G,n*i,n*j+n-1,weight="weight")
    if t < curr_min:
      curr_min = t
      print "Current Min: " + str(curr_min)
      print "i: " + str(i) + " j: " + str(j)

print "Final Min: " + str(curr_min)
